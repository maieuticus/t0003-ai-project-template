# Projekt

> Dieses Projekt wurde aus `t0003-ai-project-template` erstellt. Es ist technologieneutral:
> Sprache, Datenbank und Architektur sind noch nicht festgelegt. Zuerst kommt die Idee.

## Einstieg

1. Beschreibe deine Projektidee frei in einer Sitzung mit deinem KI-Agenten.
2. Der Agent klärt Anforderungen, empfiehlt ein SDD-Werkzeug (Spec Kit oder OpenSpec) und
   schlägt eine Architektur vor. Du gibst beides frei.
3. Danach richtet der Agent nur das Nötige ein.

Kurzanleitung: [docs/QUICKSTART.md](docs/QUICKSTART.md) · SDD-Wahl:
[docs/SDD_QUICKSTART.md](docs/SDD_QUICKSTART.md)

## Wichtige Dateien

| Datei | Zweck |
|---|---|
| [AGENTS.md](AGENTS.md) | Arbeitsregeln für alle KI-Agenten |
| [docs/DV_KONZEPT.md](docs/DV_KONZEPT.md) | verbindliche Projektbeschreibung und Architektur |
| [docs/PROJECT_HANDOFF.md](docs/PROJECT_HANDOFF.md) | aktueller Arbeitsstand für die Übergabe |
| [config/project.yaml](config/project.yaml) | Projekt-, Template- und SDD-Metadaten |
| [CHANGELOG.md](CHANGELOG.md) | Änderungen des Templates |

## Prüfen

```text
python scripts/check.py        # Dokumente, Pflichtdateien, projektspezifische Prüfungen
python scripts/status.py       # dokumentierten Arbeitsstand anzeigen
```

## Secret-Schutz einrichten

Neue Projekte erhalten die Gitleaks-Konfiguration und den
GitHub-Actions-Workflow aus dem Template.

### Lokale Einrichtung (Windows, Linux, Codespaces)

1. Git, Python und Gitleaks installieren (getestet: 8.30.1).
2. Pre-Commit installieren: `python -m pip install pre-commit`
3. Im Projektverzeichnis ausf?hren: `python scripts/setup_security.py`

Unter Windows kann Gitleaks mit
`winget install --id Gitleaks.Gitleaks --exact --source winget`
installiert werden. Unter Linux ist Gitleaks separat zu installieren.

Die Einrichtung erfolgt einmal pro Git-Arbeitskopie und kann
wiederholt werden. Fremde Hooks werden nicht ?berschrieben.

### Sicherheitspr?fungen

- Vor Commits: lokaler Gitleaks-Pre-Commit-Hook.
- Bei Push/Pull Request: GitHub-Actions-Workflow secret-scan.yml.
- Vor Merge: CI-Check in GitHub-Branch-Regeln als Pflichtpr?fung einrichten.

Wichtig: Git-Hooks werden beim Klonen nicht automatisch aktiviert.
Eine automatische Codespaces-Installation ist noch nicht eingerichtet.
Der CI-Workflow muss separat auf GitHub getestet werden.
Secret-Scanner bieten keinen vollst?ndigen Schutz vor Datenlecks.
