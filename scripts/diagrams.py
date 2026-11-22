"""Build and validate versioned documentation diagrams."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
from urllib.parse import unquote, urlsplit

MANIFEST = ".diagram-manifest.json"
MERMAID_VERSION = ".mermaid-cli-version"
SHARP_VERSION = ".sharp-cli-version"
SKIP_DIRS = {".git", ".venv", "node_modules", ".artifacts", "__pycache__", "target", "dist", "build",
             "exports", "backups"}
IMAGE = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)\)")
LINKED_IMAGE = re.compile(r"\[\s*!\[([^\]]*)\]\(([^)\s]+)\)\s*\]\(([^)\s]+)\)")
VERSION = re.compile(r"[0-9]+\.[0-9]+\.[0-9]+")


def sources(root: Path) -> list[Path]:
    result = []
    for directory, names, files in os.walk(root):
        relative = Path(directory).relative_to(root)
        if relative.parts[:2] == ("docs", "references"):
            names[:] = []
            continue
        names[:] = [name for name in names if name not in SKIP_DIRS and not (Path(directory) / name).is_symlink()]
        for name in files:
            path = Path(directory) / name
            if path.is_symlink() or path.suffix not in {".mmd", ".svg"}:
                continue
            if path.suffix == ".svg" and path.with_suffix(".mmd").is_file():
                continue
            result.append(path)
    return sorted(result)


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def versions(root: Path) -> dict[str, str]:
    result = {}
    for filename, key in ((MERMAID_VERSION, "mermaid_cli"), (SHARP_VERSION, "sharp_cli")):
        try:
            version = (root / filename).read_text(encoding="utf-8").strip()
        except OSError as error:
            raise ValueError(f"{filename}: Version-Pin kann nicht gelesen werden: {error}") from error
        if not VERSION.fullmatch(version):
            raise ValueError(f"{filename}: stabile Version MAJOR.MINOR.PATCH erforderlich.")
        result[key] = version
    return result


def load_manifest(root: Path) -> dict | None:
    path = root / MANIFEST
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(f"{MANIFEST}: ungültig oder nicht lesbar: {error}") from error
    if not isinstance(data, dict) or not isinstance(data.get("sources"), dict):
        raise ValueError(f"{MANIFEST}: erwartete ein Objekt mit einem 'sources'-Objekt.")
    return data


def output_paths(root: Path, source: Path, entry: dict | None = None) -> list[Path]:
    outputs = [source.with_suffix(".png")]
    if source.suffix == ".mmd":
        svg = source.with_suffix(".svg")
        previous = entry.get("outputs", {}) if isinstance(entry, dict) else {}
        if svg.exists() or (isinstance(previous, dict) and svg.relative_to(root).as_posix() in previous):
            outputs.append(svg)
    return outputs


def _target_path(markdown: Path, target: str) -> Path | None:
    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc:
        return None
    path = unquote(parsed.path)
    return (markdown.parent / path).resolve() if path else markdown.resolve()


def _embedding_errors(root: Path, image_path: Path) -> list[str]:
    errors, embedded = [], False
    image = image_path.resolve()
    for directory, names, files in os.walk(root):
        relative_directory = Path(directory).relative_to(root)
        if relative_directory.parts[:2] == ("docs", "references"):
            names[:] = []
            continue
        names[:] = [name for name in names if name not in SKIP_DIRS and not (Path(directory) / name).is_symlink()]
        for name in files:
            markdown = Path(directory) / name
            if markdown.suffix != ".md" or markdown.is_symlink():
                continue
            relative = markdown.relative_to(root)
            try:
                text = markdown.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError):
                continue
            text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
            linked = list(LINKED_IMAGE.finditer(text))
            for match in IMAGE.finditer(text):
                if _target_path(markdown, match.group(2)) != image:
                    continue
                embedded = True
                if not match.group(1).strip():
                    errors.append(f"{relative}: Diagramm-PNG ohne Alt-Text: {match.group(2)}")
                zoom = any(
                    wrapper.start() <= match.start() and wrapper.end() >= match.end()
                    and _target_path(markdown, wrapper.group(3)) == image
                    for wrapper in linked
                )
                if not zoom:
                    errors.append(f"{relative}: Diagramm-PNG braucht eine anklickbare PNG-Großansicht: {match.group(2)}")
    if not embedded:
        errors.append(f"{image_path.relative_to(root)}: PNG wird in keiner Markdown-Datei eingebettet.")
    return errors


def check(root: Path) -> list[str]:
    diagram_sources = sources(root)
    manifest_path = root / MANIFEST
    if not diagram_sources and not manifest_path.exists():
        return []
    try:
        pinned = versions(root)
        manifest = load_manifest(root)
    except ValueError as error:
        return [str(error)]
    if manifest is None:
        return [f"{MANIFEST}: fehlt; python scripts/diagrams.py build ausführen."]

    errors = []
    if manifest.get("schema_version") != 1:
        errors.append(f"{MANIFEST}: nicht unterstützte schema_version.")
    if manifest.get("tools") != pinned:
        errors.append(f"{MANIFEST}: Renderer-Versionen weichen von den Pins ab; Build erneut ausführen.")

    recorded = manifest["sources"]
    source_names = {path.relative_to(root).as_posix() for path in diagram_sources}
    for name in sorted(recorded.keys() - source_names):
        errors.append(f"{MANIFEST}: Quelle entfernt oder umbenannt: {name}; Ausgaben und Eintrag bereinigen.")
    for name in sorted(source_names - recorded.keys()):
        errors.append(f"{MANIFEST}: Quelle nicht registriert: {name}; python scripts/diagrams.py build ausführen.")

    for source in diagram_sources:
        name = source.relative_to(root).as_posix()
        entry = recorded.get(name)
        if not isinstance(entry, dict):
            errors.append(f"{MANIFEST}: ungültiger Eintrag für Quelle: {name}")
            continue
        if entry.get("sha256") != file_hash(source):
            errors.append(f"{name}: Quelle seit dem letzten Diagramm-Build geändert.")
        expected = output_paths(root, source, entry)
        expected_names = {path.relative_to(root).as_posix() for path in expected}
        output_hashes = entry.get("outputs")
        if not isinstance(output_hashes, dict):
            errors.append(f"{MANIFEST}: Ausgaben für {name} fehlen oder sind ungültig.")
            continue
        for unexpected in sorted(output_hashes.keys() - expected_names):
            errors.append(f"{MANIFEST}: unerwartete Ausgabe für {name}: {unexpected}")
        for output in expected:
            output_name = output.relative_to(root).as_posix()
            if output.is_symlink():
                errors.append(f"{output_name}: Diagramm-Ausgabe darf kein Symlink sein.")
                continue
            if not output.is_file():
                errors.append(f"{name}: Ausgabe fehlt: {output_name}; python scripts/diagrams.py build ausführen.")
                continue
            if output_name not in output_hashes:
                errors.append(f"{MANIFEST}: Prüfsumme für Ausgabe fehlt: {output_name}")
            elif output_hashes[output_name] != file_hash(output):
                errors.append(f"{output_name}: Ausgabe seit dem letzten Diagramm-Build geändert.")
            if output.suffix == ".png":
                errors.extend(_embedding_errors(root, output))
    return errors


def _run(root: Path, command: list[str]) -> None:
    result = subprocess.run(command, cwd=root, check=False)
    if result.returncode:
        raise RuntimeError(f"Diagramm-Renderer fehlgeschlagen (Exitcode {result.returncode}): {' '.join(command)}")


def _check_runtime() -> None:
    node, npm = shutil.which("node"), shutil.which("npm")
    if not node or not npm:
        raise ValueError("Diagramme erstellen benötigt Node.js 22.13+ und npm.")
    result = subprocess.run([node, "--version"], capture_output=True, text=True, check=False)
    match = re.fullmatch(r"v(\d+)\.(\d+)\.\d+.*", result.stdout.strip())
    if not match or (int(match.group(1)), int(match.group(2))) < (22, 13):
        raise ValueError(
            f"Diagramme erstellen benötigt Node.js 22.13+, gefunden: {result.stdout.strip() or 'unbekannt'}."
        )


def build(root: Path, include_svg: bool) -> int:
    diagram_sources = sources(root)
    if (root / MANIFEST).is_symlink():
        print(f"{MANIFEST}: Manifest darf kein Symlink sein.", file=sys.stderr)
        return 1
    try:
        pinned = versions(root)
        old_manifest = load_manifest(root)
    except ValueError as error:
        print(error, file=sys.stderr)
        return 1
    if not diagram_sources:
        if old_manifest and old_manifest["sources"]:
            print(f"{MANIFEST}: enthält keine vorhandene Diagrammquelle; veraltete Einträge bereinigen.", file=sys.stderr)
            return 1
        print("Keine Diagrammquellen gefunden.")
        return 0

    old_entries = old_manifest["sources"] if old_manifest else {}
    current_names = {path.relative_to(root).as_posix() for path in diagram_sources}
    removed = sorted(old_entries.keys() - current_names)
    if removed:
        print(f"{MANIFEST}: entfernte Quellen und ihre Ausgaben zuerst bereinigen: {', '.join(removed)}", file=sys.stderr)
        return 1
    _check_runtime()

    entries = {}
    for source in diagram_sources:
        name = source.relative_to(root).as_posix()
        old_entry = old_entries.get(name)
        png = source.with_suffix(".png")
        if source.suffix == ".mmd":
            svg = source.with_suffix(".svg")
            previous = old_entry.get("outputs", {}) if isinstance(old_entry, dict) else {}
            make_svg = include_svg or svg.exists() or (
                isinstance(previous, dict) and svg.relative_to(root).as_posix() in previous
            )
            if png.is_symlink() or (make_svg and svg.is_symlink()):
                raise ValueError(f"{name}: Diagramm-Ausgaben dürfen keine Symlinks sein.")
            npm_exec = [
                "npm", "exec", "--yes", f"--package=@mermaid-js/mermaid-cli@{pinned['mermaid_cli']}", "--",
            ]
            _run(root, [
                *npm_exec, "mmdc", "-i", str(source), "-o", str(png),
                "--scale", "2", "--backgroundColor", "white",
            ])
            if make_svg:
                _run(root, [
                    *npm_exec, "mmdc", "-i", str(source), "-o", str(svg),
                    "--scale", "2", "--backgroundColor", "white",
                ])
            outputs = [png, *([svg] if make_svg else [])]
        else:
            if png.is_symlink():
                raise ValueError(f"{name}: Diagramm-Ausgaben dürfen keine Symlinks sein.")
            _run(root, [
                "npm", "exec", "--yes", f"--package=sharp-cli@{pinned['sharp_cli']}", "--", "sharp",
                "--input", str(source), "--output", str(source.parent / "{name}.png"),
                "--density", "192", "--format", "png",
            ])
            outputs = [png]
        entries[name] = {
            "sha256": file_hash(source),
            "outputs": {path.relative_to(root).as_posix(): file_hash(path) for path in outputs},
        }

    manifest = {"schema_version": 1, "tools": pinned, "sources": entries}
    (root / MANIFEST).write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    errors = check(root)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Diagramm-Ausgaben und Markdown-Einbettung: OK")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("build", "check"))
    parser.add_argument("--svg", action="store_true", help="bei Mermaid zusätzlich SVG-Ausgaben erzeugen")
    args = parser.parse_args()
    if args.command == "check":
        if args.svg:
            parser.error("--svg gilt nur für build.")
        errors = check(Path(__file__).resolve().parents[1])
        if errors:
            print("\n".join(errors), file=sys.stderr)
            return 1
        print("Diagrammquellen, Ausgaben und Markdown-Einbettung: OK")
        return 0
    return build(Path(__file__).resolve().parents[1], args.svg)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    try:
        sys.exit(main())
    except (OSError, ValueError, RuntimeError) as error:
        print(f"Diagramme: {error}", file=sys.stderr)
        sys.exit(1)
