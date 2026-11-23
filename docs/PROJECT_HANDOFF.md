# Projektübergabe

Flüchtiger Arbeitsstand für den Wechsel zwischen Agenten und Umgebungen. Er ändert keine
Architekturentscheidungen (diese stehen in [DV_KONZEPT.md](DV_KONZEPT.md) und den Specs). Keine
Secrets, Tokens oder Zugangsdaten eintragen. Git hat bei Widersprüchen Vorrang.

## Aktueller Stand

- Stand: 2026-11-23
- Branch/Basis: `feature/issue-9-autocrlf-regression`, basiert auf `main` nach PR #10
  (`d4d4426`).
- Aktive Aufgabe: PR #11 für Issue #9 ist offen; CI und Review stehen aus.
- Erledigt:
  - Issue #7 umgesetzt: Standard und Beispiele in `docs/DIAGRAMS.md`, Arbeitsregel in `AGENTS.md`.
  - `scripts/diagrams.py` erzeugt Mermaid-PNGs und optionale SVGs sowie PNGs aus SVG-Quellen;
    der Projektcheck prüft Quellen, Ausgaben, Alt-Texte und anklickbare Großansichten offline.
  - Mermaid-Beispiel und generierte PNG-/SVG-Ausgaben lokal erstellt und wiederholt geprüft.
  - PR #6 und PR #8 sind gemergt; die vorherige Angabe, PR #8 sei offen, war veraltet.
  - Branch-Audit implementiert als read-only API-Bericht mit Wochen-, manuellem und Release-Trigger.
- PR #10 (`Add read-only branch audit to template`) wurde am 2026-11-23 gemergt.
- Issue #9: Regressionstest ergänzt, der einen isolierten Checkout mit `core.autocrlf=true`
  prüft und die tatsächlichen `.gitattributes`-Regeln sowie SHA-256-Prüfsummen für SVG- und
  Mermaid-Dateien in `docs/diagrams/` verifiziert.
- Offen: Automatische Anlage zusätzlicher GitHub-Branches und Schutzregeln ist nicht enthalten;
  t0004 bleibt gemäß bestätigtem Audit-only-Umfang netzwerkfrei.
- Issue #9 beschreibt fehlende Abdeckung, keinen aktuell nachgewiesenen Fehler.
- Blocker: Keine technische Blockade. Merge braucht separate ausdrückliche Freigabe.
- Letzte lokale Prüfergebnisse: `python scripts/check.py` und `git diff --check` erfolgreich;
  Template-Tests 30 bestanden, 3 netzwerkabhängige SDD-Tests übersprungen (33 insgesamt).
  Lokaler Lauf auf Linux; CI für PR #11 läuft auf Ubuntu, Windows und Gitleaks.
- Synchronisierung: `origin/main` ist lokal auf den Merge-Commit `d4d4426` aktualisiert.
  Branch `feature/issue-9-autocrlf-regression` ist gepusht; PR #11 ist offen. Kein Release und
  keine Änderung an produktiven Projekt-Repositories.

## Nächster Schritt

CI-Ergebnisse und Review für PR #11 abwarten. Merge braucht separate ausdrückliche Freigabe.

## Entscheidungen und Quellen

Verweise auf verbindliche Entscheidungen (DV-Konzept, Specs). Hier nichts neu entscheiden.

## Probleme

t0004 unterstützt derzeit nur t0003 0.1.0 und erstellt keine GitHub-Repositories oder Remote-
Branches. Neue Template-Version und Kompatibilitätserweiterungen müssen gesondert abgestimmt
werden; kein Release im Rahmen dieser Änderung.
