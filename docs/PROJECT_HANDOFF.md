# Projektübergabe

Flüchtiger Arbeitsstand für den Wechsel zwischen Agenten und Umgebungen. Er ändert keine
Architekturentscheidungen (diese stehen in [DV_KONZEPT.md](DV_KONZEPT.md) und den Specs). Keine
Secrets, Tokens oder Zugangsdaten eintragen. Git hat bei Widersprüchen Vorrang.

## Aktueller Stand

- Stand: 2026-11-15
- Branch/Basis: `feature/references-dv-konzept` / `4319e05` (aktueller Commit: siehe Git)
- Aktive Aufgabe: optionales Rohmaterial als Grundlage des Ideen-Dialogs integrieren.
- Erledigt:
  - `docs/references/` als unverbindlichen Eingangsbereich und beide Einstiegswege dokumentiert.
  - Agentenregeln für Auswertung, Quellen, Freigaben, Datenschutz und Schutz der Originale ergänzt.
  - Projektcheck nimmt Originalmaterial von Syntax- und Linkprüfung aus; die Ordner-README bleibt geprüft.
  - Template-Kopie mit widersprüchlichen Markdown-Quellen geprüft; die Originale und das
    DV-Konzept bleiben unverändert. Spec-Kit- und OpenSpec-Tests schützen die Quelldateien.
- Offen: menschliches Review und Freigabe für PR #6; CI nach Windows-Testkorrektur erneut prüfen.
- Blocker: Windows-CI meldete einen plattformabhängigen Pfadvergleich im neuen Test; erneute CI ausstehend.
- Letzte lokale Prüfergebnisse: `python scripts/check.py` und
  `python -m unittest discover -s .github/template-tests -v` erfolgreich (19 Tests, Linux).
  GitHub Actions: Linux und Gitleaks erfolgreich; Windows nach Testkorrektur erneut ausstehend.
- Dialogsimulation: `idee.md` verlangt Offline-Betrieb, `anforderungen.md` eine permanente
  Internetverbindung. Der Widerspruch bleibt offen; zu klären ist, welche Betriebsweise in welchen
  Situationen gelten soll. Keine bestätigte Entscheidung und keine Übernahme ins DV-Konzept.
  Dies ist ein manueller Szenariodurchlauf, kein interaktiver Agenten-E2E-Test.
- Synchronisierung: siehe Git; PR #6 offen.

## Nächster Schritt

CI-Ergebnis und Dialogverhalten prüfen; menschliches Review-Gate vor Merge beachten.

## Entscheidungen und Quellen

Verweise auf verbindliche Entscheidungen (DV-Konzept, Specs). Hier nichts neu entscheiden.

## Probleme

t0004 unterstützt derzeit nur t0003 0.1.0. Neue Template-Version und Kompatibilitätserweiterung
müssen gesondert abgestimmt werden; kein Release im Rahmen dieser Änderung.
