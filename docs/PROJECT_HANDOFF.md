# Projektübergabe

Flüchtiger Arbeitsstand für den Wechsel zwischen Agenten und Umgebungen. Er ändert keine
Architekturentscheidungen (diese stehen in [DV_KONZEPT.md](DV_KONZEPT.md) und den Specs). Keine
Secrets, Tokens oder Zugangsdaten eintragen. Git hat bei Widersprüchen Vorrang.

## Aktueller Stand

- Stand: 2026-11-22
- Branch/Basis: `main` / `17ed6c7`; die aktuelle Änderung ist noch nicht committet.
- Aktive Aufgabe: Issue #7 – PNG-first-Standard und lokale Diagrammprüfungen ergänzen.
- Erledigt:
  - Issue #7 umgesetzt: Standard und Beispiele in `docs/DIAGRAMS.md`, Arbeitsregel in `AGENTS.md`.
  - `scripts/diagrams.py` erzeugt Mermaid-PNGs und optionale SVGs sowie PNGs aus SVG-Quellen;
    der Projektcheck prüft Quellen, Ausgaben, Alt-Texte und anklickbare Großansichten offline.
  - Mermaid-Beispiel und generierte PNG-/SVG-Ausgaben lokal erstellt und wiederholt geprüft.
  - PR #6 ist gemergt; die vorherige Handoff-Angabe „offen“ war veraltet.
- Offen: Feature-Branch, Commit, Push und PR-Erstellung; vom Benutzer freigegeben, noch nicht ausgeführt.
- Blocker: keiner. Windows-CI wurde für diese Änderung noch nicht ausgeführt.
- Letzte lokale Prüfergebnisse (Ubuntu 24.04): `python scripts/check.py` erfolgreich;
  Template-Tests 21 erfolgreich, 3 netzwerkabhängige SDD-Tests übersprungen;
  `python scripts/diagrams.py build --svg` und anschließender Check erfolgreich.
- Synchronisierung: Issue #7 offen; lokale Änderungen sind nicht committet.

## Nächster Schritt

Freigegebene Änderungen auf einem Feature-Branch veröffentlichen; kein Merge oder Release ohne
separate Freigabe.

## Entscheidungen und Quellen

Verweise auf verbindliche Entscheidungen (DV-Konzept, Specs). Hier nichts neu entscheiden.

## Probleme

t0004 unterstützt derzeit nur t0003 0.1.0. Neue Template-Version und Kompatibilitätserweiterung
müssen gesondert abgestimmt werden; kein Release im Rahmen dieser Änderung.
