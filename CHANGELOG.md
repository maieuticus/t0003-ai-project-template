# Changelog

Alle wesentlichen Änderungen am Template. Format: [SemVer](https://semver.org/lang/de/). Das
Template wird getrennt vom Generator versioniert. Kategorien: Arbeitsregeln, Specify/Tooling,
Projektstruktur, Adapter, CI, Sicherheit, Breaking Changes, Migrationshinweise.

## [Unveröffentlicht] – 0.1.0-dev

### Projektstruktur
- Neutrales Template: README, `AGENTS.md`, `config/project.yaml`, DV-Konzept, Handoff, Quickstarts.

### Specify/Tooling
- Wählbar: Spec Kit (gepinnt 1.0.7, Windows-sicherer Python-Wrapper) und OpenSpec (gepinnt 1.15.0).
- `scripts/sdd.py`, `check.py`, `status.py`, `update_check.py`.

### Adapter
- `.github/copilot-instructions.md` verweist nur auf `AGENTS.md`.

### CI
- GitHub Actions mit `contents: read`: Template-Tests und Praxistest einer Projektkopie.
