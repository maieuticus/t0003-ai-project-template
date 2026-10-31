# Projektübergabe

Flüchtiger Arbeitsstand für den Wechsel zwischen Agenten und Umgebungen. Er ändert keine
Architekturentscheidungen (diese stehen in [DV_KONZEPT.md](DV_KONZEPT.md) und den Specs). Keine
Secrets, Tokens oder Zugangsdaten eintragen. Git hat bei Widersprüchen Vorrang.

## Aktueller Stand

- Stand: 2026-10-31
- Branch/Basis: `feature/derived-project-checks` / `3368240` (aktueller Commit: siehe Git)
- Aktive Aufgabe: Template für abgeleitete Projekte mit technologieabhängigen Checks vorbereiten.
- Erledigt:
  - PR #1 gemergt: neutrale Main-Template-Basis (Spec Kit + OpenSpec auswählbar).
  - PR #2 gemergt: Handoff-Export/Import-Check inklusive Wrapper-Regressionstests.
  - Projektcheck bleibt in Linux-/Windows-CI allgemein aktiv; Template-Tests mit
    Neutralitätsannahmen laufen dort nur im t0003-Ursprungsrepository.
  - Synthetisches Projekt mit `src/` und Python-Check deckt Erfolg und Fehlerweitergabe ab.
- Offen: PR-Review und GitHub-Actions-Ergebnisse prüfen; kein automatischer Merge.
- Blocker: keine
- Letzte lokale Prüfergebnisse: `python scripts/check.py` und
  `python -m unittest discover -s .github/template-tests -v` erfolgreich (18 Tests).
  Linux-/Windows-CI: siehe PR; zum Zeitpunkt dieser Übergabe noch ausstehend.
- Synchronisierung: siehe Git und PR.

## Nächster Schritt

PR und Linux-/Windows-CI prüfen; anschließend menschliches Review-Gate beachten.

## Entscheidungen und Quellen

Verweise auf verbindliche Entscheidungen (DV-Konzept, Specs). Hier nichts neu entscheiden.

## Probleme

t0004 unterstützt derzeit nur t0003 0.1.0. Neue Template-Version und Kompatibilitätserweiterung
müssen gesondert abgestimmt werden; kein Release im Rahmen dieser Änderung.
