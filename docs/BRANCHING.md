# Branch-Strategie und Bereinigung

## Standard-Branches und Entwicklungsweg

Der vorgesehene Entwicklungsweg lautet:

```text
feature/* → development → test → main
```

| Branch | Zweck |
|---|---|
| `main` | stabiler, freigegebener Produktionsstand und Default-Branch |
| `test` | Integrations- und Teststand vor der Freigabe |
| `development` | Zusammenführung laufender Entwicklungen |

Änderungen werden über Pull Requests eingebracht. Die CI muss auf Pull Requests und
Pushes zu allen Branches laufen; `ci.yml` und `secret-scan.yml` prüfen diese Ereignisse.
Die Secret-Scan-Prüfung bleibt dabei unverändert.

## Schutzregeln

Schutzregeln werden in den GitHub-Repository-Einstellungen durch eine Repository-Administration
eingerichtet; eine Markdown-Datei oder ein Template kann diese Einstellungen nicht erzwingen.
Für `main`, `test` und `development` sind jeweils mindestens erforderlich:

- Pull Requests statt direkter Pushes; keine Force-Pushes oder Branch-Löschung.
- Alle zugehörigen CI- und Secret-Scan-Prüfungen als erforderliche Statuschecks.
- `main` nur für freigegebene Änderungen; `test` und `development` nur über den beschriebenen
  PR-Weg aktualisieren.

Branch-Regeln sind vor Ort zu prüfen, bevor sie als aktiv gelten. Vorhandene Schutzregeln dürfen
nicht abgeschwächt oder umgangen werden.

## Ersteinrichtung und Zuständigkeit

GitHub erstellt bei einer Template-Kopie den Default-Branch. Diese t0003-Vorlage legt keine
zusätzlichen Remote-Branches oder GitHub-Schutzregeln an. Der optionale Generator
`t0004-ai-project-generator` ist eine lokale, netzwerkfreie Datei-CLI und übernimmt diese
GitHub-Einrichtung ebenfalls nicht. Bis ein gesonderter, freigegebener Provisionierungsweg
existiert, muss eine Repository-Administration `development` und `test` am geprüften
Ausgangscommit anlegen, sodass alle drei Branches zunächst auf denselben Commit zeigen,
`main` als Default bestätigen und die Schutzregeln manuell setzen. Bestehende Repositories
werden nicht automatisch verändert.

## Regelmäßiger, rein lesender Branch-Audit

Der Workflow `Branch-Audit` läuft wöchentlich (montags), nach veröffentlichten Releases und
manuell über **Actions → Branch-Audit → Run workflow**. Er benötigt nur `contents: read` und
`pull-requests: read`, schreibt den Bericht in die GitHub-Actions-Zusammenfassung und löscht
niemals Branches. API- oder Berechtigungsfehler lassen den Lauf sichtbar fehlschlagen.

Jeder Branch-Bericht enthält Branch-Name, Datum des letzten Commits, Inaktivität, Merge-Status,
zugehörigen PR und Begründung:

- **Löschung empfohlen**: ein zugehöriger PR ist gemergt, seine Spitze entspricht exakt der
  Branch-Spitze und sein Ziel entspricht dem vorgesehenen Zielbranch.
- **Manuelle Prüfung empfohlen**: seit mehr als 30 Tagen inaktiv ohne geklärte Integration,
  ein PR wurde ohne Merge geschlossen, das Ziel/Branch-Spitze passt nicht oder Daten fehlen.
  Mehr als 60 Tage Inaktivität wird ausdrücklich ausgewiesen; es wird trotzdem nichts gelöscht.
- **Behalten**: `main`, `test`, `development`, von GitHub geschützte Branches, Branches mit
  offenem PR, `release/*`/`hotfix/*` sowie kürzlich geänderte Branches.

Nur ein PR-Merge in den vorgesehenen Zielbranch gilt als automatische Integrations-Evidenz.
Branches ohne passenden PR werden nie zur Löschung empfohlen, auch wenn sie in GitHub als
vergleichbar erscheinen. Der Audit erkennt keine Arbeit, die außerhalb des Remote-Branches und
der GitHub-Pull-Requests liegt. Vor einer tatsächlichen Löschung ist immer eine ausdrückliche
Benutzerfreigabe erforderlich; die Löschung selbst erfolgt außerhalb dieses Audits.
