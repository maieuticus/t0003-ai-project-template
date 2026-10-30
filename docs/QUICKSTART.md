# Quickstart

Kurzanleitung für den ersten Start. Es sind nur Kommandos aufgeführt, die in diesem Template
geprüft wurden; Grenzen stehen am Ende.

## 1. Projekt starten

1. Auf GitHub **Use this template** wählen und ein privates Repository erstellen.
2. Öffnen in **VS Code** (lokal klonen) oder in **GitHub Codespaces** (Code → Codespaces → neu).
   Voraussetzung: Git und Python 3.11+. Docker wird nicht benötigt.
3. Optional in `config/project.yaml` den Projektnamen eintragen.

## 2. Agent starten

Du installierst und startest den Agenten selbst. Das Template installiert nichts und startet
keinen Agenten automatisch.

- **GitHub Copilot (VS Code/Chat):** Repository öffnen; Copilot liest `.github/copilot-instructions.md`,
  die auf `AGENTS.md` verweist.
- **Copilot CLI / Codex / andere:** im Projektordner starten. Sage am Anfang: _„Lies AGENTS.md und
  docs/PROJECT_HANDOFF.md und beginne mit dem Ideen-Dialog.“_ Nicht jedes Werkzeug liest `AGENTS.md`
  automatisch; dieser Satz ist der sichere Start.

## 3. Idee → SDD-Wahl → Architektur

1. Beschreibe deine Projektidee frei.
2. Der Agent klärt Anforderungen und empfiehlt Spec Kit oder OpenSpec. Bestätige.
3. Der Agent führt `python scripts/sdd.py select speckit|openspec` aus. Details:
   [SDD_QUICKSTART.md](SDD_QUICKSTART.md).
4. Der Agent schlägt eine Architektur vor. Erst nach deiner Freigabe richtet er Technik ein.

## 4. Setup, Check, Status

```text
python scripts/sdd.py select speckit      # Setup des gewählten SDD-Werkzeugs
python scripts/check.py                   # Check: Dokumente, Pflichtdateien, Projektprüfungen
python scripts/status.py                  # Status: Handoff, Git, SDD, Template-Version
python scripts/update_check.py            # optional: neuere Template-Version veröffentlicht?
```

## 5. Arbeit wieder aufnehmen oder Agent wechseln

Der Agent pflegt `docs/PROJECT_HANDOFF.md` nach wesentlichen Schritten. Neue Sitzung: Agent bitten,
den Handoff zu lesen und mit `git status` abzugleichen. Wechsel zwischen Umgebungen funktioniert nur
über Git (committen und pushen, in der anderen Umgebung pullen).

## 6. Mit ChatGPT besprechen

Bitte den Agenten um einen **Export**: kompakt (der Handoff) oder umfassend. Ergebnisse von
ChatGPT gibst du dem Agenten zurück; er vergleicht sie zuerst mit dem aktuellen Repo und fragt vor
jeder Übernahme.

## Grenzen

Geprüft: Python-Skripte unter Linux/Codespaces. Windows und macOS sind nicht manuell geprüft (CI
prüft Windows). Keine Agenten-E2E-Tests; welche Agenten welche Startdatei lesen, ist je Werkzeug
unterschiedlich.
