# Projektübergabe

Flüchtiger Arbeitsstand für den Wechsel zwischen Agenten und Umgebungen. Er ändert keine
Architekturentscheidungen (diese stehen in [DV_KONZEPT.md](DV_KONZEPT.md) und den Specs). Keine
Secrets, Tokens oder Zugangsdaten eintragen. Git hat bei Widersprüchen Vorrang.

## Aktueller Stand

- Stand: 2026-11-23
- Branch/Basis: `feature/branch-audit-template` / `aa7f013`; PR #10 ist offen.
- Aktive Aufgabe: Branch-Strategie und rein lesenden Branch-Audit in t0003 verankern.
- Erledigt:
  - Issue #7 umgesetzt: Standard und Beispiele in `docs/DIAGRAMS.md`, Arbeitsregel in `AGENTS.md`.
  - `scripts/diagrams.py` erzeugt Mermaid-PNGs und optionale SVGs sowie PNGs aus SVG-Quellen;
    der Projektcheck prüft Quellen, Ausgaben, Alt-Texte und anklickbare Großansichten offline.
  - Mermaid-Beispiel und generierte PNG-/SVG-Ausgaben lokal erstellt und wiederholt geprüft.
  - PR #6 und PR #8 sind gemergt; die vorherige Angabe, PR #8 sei offen, war veraltet.
  - Branch-Audit implementiert als read-only API-Bericht mit Wochen-, manuellem und Release-Trigger.
- Offen: Automatische Anlage zusätzlicher GitHub-Branches und Schutzregeln ist nicht enthalten;
  t0004 bleibt gemäß bestätigtem Audit-only-Umfang netzwerkfrei.
- Blocker: Keine technische Blockade. Die ausgeschlossene Remote-Ersteinrichtung bleibt eine
  offene Anforderung für einen gesondert freizugebenden Provisionierungsweg.
- Letzte lokale Prüfergebnisse: `python scripts/check.py` erfolgreich; Template-Tests 29
  bestanden, 3 netzwerkabhängige SDD-Tests übersprungen (32 insgesamt); `git diff --check` und
  Python-Syntaxprüfung erfolgreich. GitHub Actions für Linux, Windows und Gitleaks sind in PR #10
  erfolgreich.
- Synchronisierung: Branch ist gepusht und PR #10 offen. Kein Release und keine Änderung an
  produktiven Projekt-Repositories.

## Nächster Schritt

PR #10 reviewen und nach ausdrücklicher Freigabe mergen. Merge und Release brauchen eine separate
Freigabe.

## Entscheidungen und Quellen

Verweise auf verbindliche Entscheidungen (DV-Konzept, Specs). Hier nichts neu entscheiden.

## Probleme

t0004 unterstützt derzeit nur t0003 0.1.0 und erstellt keine GitHub-Repositories oder Remote-
Branches. Neue Template-Version und Kompatibilitätserweiterungen müssen gesondert abgestimmt
werden; kein Release im Rahmen dieser Änderung.
