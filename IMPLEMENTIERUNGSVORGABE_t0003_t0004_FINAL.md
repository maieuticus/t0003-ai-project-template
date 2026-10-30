# Neues KI-Projekt-Template und externer Generator – Implementierungsvorgabe

**Stand:** 28.10.2026, einschließlich Abendbeschlüssen  
**Status:** Finale fachliche Umsetzungs- und Ablaufvorgabe einschließlich der bis zum Abend des 28.10.2026 bestätigten Entscheidungen; **keine pauschale Implementierungsfreigabe**  
**Ziel:** zwei **neu aufzubauende**, getrennte GitHub-Repositories: Haupt-Template `t0003-ai-project-template` und Generator `t0004-ai-project-generator` (**Technologie-Präfix `t`, Schema und Nummern `0003`/`0004` vom Nutzer bestätigt; Kollisionsprüfung vor GitHub-Erstellung erforderlich**). Das bisherige `template-spec-kit` bleibt unverändert als Quell-/Referenzrepository erhalten.  
**Wissensbasis:** Architekturgespräch vom 28.10.2026 einschließlich der nachträglich bestätigten Entscheidungen zu **Neugründung statt Umbau**, **ausgelagertem Generator**, **separater Release-Versionierung**, **Pflichtinventur**, **zwei optionalen SDD-Systemen (Spec Kit und OpenSpec)**, **Python-CLI, modularen Profilen, zwei Generatormodi, Quickstarts** und **Praxis-End-to-End-Tests**; früherer Architektur-Snapshot vom 27.10.2026 (Analyse auf Basis von Commit `ecbae85` einschließlich lokaler Änderungen); `AGENTS_template_entwurf.md` vom 28.10.2026.  
**Wichtig:** Die zugrunde liegende Bestandsanalyse ist ein Snapshot, keine aktuelle Repositoryprüfung. Vor jeder Codeänderung den tatsächlichen Branch, Commit, Arbeitsbaum, alle relevanten Dateien und bestehende Tests im Repository ermitteln. Nicht vorhandene Pfade, Features oder Tests nicht als existent ausgeben.

---

## BENUTZUNG – so startest du die Umsetzung (verbindliche Reihenfolge)

**Du erhältst eine einzige Markdown-Datei mit allen Entscheidungen, Aufgaben, Tests, Freigabepunkten und einem Startauftrag.** Die Datei führt keine GitHub-Aktion von selbst aus. Ein Coding-Agent muss sie ausdrücklich lesen und die Phasen kontrolliert abarbeiten.

1. Im bisherigen GitHub-Konto das **private**, zunächst leere Repository **`t0003-ai-project-template`** selbst erstellen. Vorher Namens-/ID-Kollision prüfen; **noch nicht** das Generator-Repository als Abkömmling eines unfertigen Templates erzeugen. GitHub-Template-Eigenschaft des Haupt-Repos erst passend konfigurieren und mit echter Kopie prüfen.
2. Diese Datei im neuen Haupt-Repo unter **`IMPLEMENTIERUNGSVORGABE.md`** ablegen (nicht nur in den Chat kopieren). Optional zusätzlich `AGENTS_template_entwurf.md` als Referenz bereitstellen, falls vorhanden.
3. Das neue Repo in Codespaces, VS Code, Copilot CLI, Codex oder einem anderen Agenten mit Repo-Zugriff öffnen und folgenden **Startauftrag** senden:

   > Lies `IMPLEMENTIERUNGSVORGABE.md` vollständig. Das ist die verbindliche Ziel- und Ablaufvorgabe. Beginne **nur mit Phase 0 (Read-only-Analyse)**. Frage mich jetzt nach der GitHub-URL bzw. dem lesbaren lokalen Pfad meines bisherigen `template-spec-kit`. Verifiziere anschließend die Erreichbarkeit und den Git-Stand. Erstelle zunächst das Funktionsinventar und einen konkreten Übernahme-/Umsetzungsplan, zeige die kurze Statusübersicht und **warte vor der Implementierung auf meine Freigabe**. Arbeite nach Freigabe die nummerierten Phasen mit Checks, Dokumentation und den vorgesehenen Entscheidungspunkten durch. Das Alt-Repo darf niemals verändert werden. Stelle Rückfragen nur bei tatsächlichen Blockern oder Freigabeentscheidungen.

4. **Erst bei diesem Start** nennt der Nutzer den Link zum alten Repository (oder einen lesbaren lokalen Checkout). Ist es privat, zunächst die nötige **Leseberechtigung** bereitstellen; keinen Link erfinden und keine pauschalen Schreibrechte verlangen. Falls die Quelle nicht erreichbar ist, nur diese Analyse als blockiert melden; keine Quellinformationen behaupten.
5. Inventur und Übernahmematrix prüfen/freigeben; danach wird **zuerst das neutrale Haupt-Template** entwickelt, separat getestet und als stabile Baseline freigegeben.
6. **Danach** das zweite **private** Repository **`t0004-ai-project-generator`** im selben GitHub-Konto selbst **aus der freigegebenen Version** von `t0003-ai-project-template` erzeugen (oder nach ausdrücklicher Nutzerentscheidung das agentengestützte Anlegen autorisieren). Die Agentin/der Agent führt die Implementierungsarbeit in diesem zweiten Repo nur durch, wenn der Workspace-Zugriff darauf tatsächlich besteht.
7. Python-Generator, Profile, Tests, SemVer/Release und abgesicherte CLI einrichten, beide Repos integrieren, mit temporären Beispielprojekten einschließlich Spec Kit und OpenSpec testen. Erst nach bestandenen Prüfungen die erste Gesamtversion freigeben.
8. Anschließend kann ein neues Projekt wie **Lands of Glory** aus dem Haupt-Template entstehen. Es bekommt zunächst **Inhalte und Entscheidungen**, nicht ungeprüft die alte Technikstruktur; **Spec Kit** wird für dieses Projekt ausgewählt. Andere Projekte dürfen **OpenSpec** wählen.

**Freigabelogik:** Statusmeldungen sind informativ und blockieren nicht. **Analyse-/Architektur-/Änderungsfreigaben** sowie echte GitHub-Rechte- oder Kostenentscheidungen bleiben ausdrücklich. Der Agent darf nach einer genehmigten Etappe Routinearbeiten und Tests ohne ständiges Nachfragen erledigen. Ein privates Repo oder eine `AGENTS.md` ersetzt keine technische Berechtigung.

---

## 0. Auftrag an den implementierenden KI-Agenten

Plane und realisiere nach den vorgesehenen Freigaben **zwei neue Repositories** in kontrollierten Etappen. Das bisherige `template-spec-kit` ist **nur lesende Quelle**, nicht Ziel für Umbauten, Löschungen oder erzwungene Migration. Beginne mit Audit und einer nachvollziehbaren Zuordnung von Alt-Funktionen zu den neuen Repositories; nicht mit Kopieren des gesamten Quell-Repos.

1. **Altes Repository read-only** prüfen; Branch, Commit, Arbeitsbaum, Tests und lokale Abweichungen erfassen. Den vorhandenen Analyse-Snapshot mit dem echten Stand abgleichen.
2. **Funktionsinventar** mit Quelle, nachgewiesenem Funktionsstatus und Zuordnung erstellen: `DIREKT INS NEUE TEMPLATE / ANPASSEN / INS GENERATOR-REPO / NICHT ÜBERNEHMEN`. Alte Dateien nicht blind replizieren.
3. Für jede Etappe betroffene Dateien, Abhängigkeiten, Tests, Migrationswirkung und notwendige Entscheidungen nennen.
4. Konflikte mit bestätigten Architekturentscheidungen und alle neuen Grundsatzentscheidungen offenlegen. **Vor strukturellen/destruktiven Änderungen, bedeutender Architekturabweichung oder der Implementierungsphase die vorgesehenen menschlichen Freigaben einholen.**
5. Nach Freigabe in **neuen** Arbeits-Repositories/Branches in kleinen Commits oder PR-Schritten umsetzen. Die Erstellung von GitHub-Repositories, Pushes oder Veröffentlichungen setzt tatsächlich verfügbare Rechte und die hierfür nötige Autorisierung voraus. Keine Secrets, Produktionsänderungen, zusätzlichen Konto-Rechte oder externen Veröffentlichungen ohne separate Autorisierung.
6. Geeignete Tests ausführen; Fehlschläge innerhalb des genehmigten Rahmens beheben. Nicht ausführbare Prüfungen ausdrücklich benennen.
7. Dokumentation und Übergabe aktualisieren; in einer kurzen Tabelle berichten: `Status | Arbeitsschritt | Kurzbeschreibung`, anschließend Blocker/Freigaben.

**Definition des Ergebnisses:** (1) ein **neues** GitHub-Projekt-Template, dessen direkte Kopie technologieneutral und sofort für Spezifikation nutzbar ist, und (2) ein **eigenes** versioniertes Generator-Repository mit den sinnvoll übernommenen alten Generatorfunktionen. Hinzu kommen portablen KI-Regeln, gemeinsame Übergabe, kontrollierte Aktualisierung, Migrationsablauf und automatische sowie praktische End-to-End-Tests. Das alte Repository bleibt erhalten. **Das reale Implementieren ist nicht allein durch dieses Dokument genehmigt.**

---

## 1. Verbindliche Architekturentscheidungen aus dem Gespräch

**D-01 – Neutraler Projektstart / „Ideen zuerst“.** GitHub **Use this template** liefert ohne zusätzlichen Pflichtgenerator ein sofort für Planung, Anforderungen und Spec-Driven Development nutzbares Repository. Keine Programmiersprache, Datenbank oder vollständige Anwendung vorentschieden. Eine KI macht nach freier Projektbeschreibung einen Architekturvorschlag; die Person genehmigt ihn vor Aufbau der konkreten technischen Umgebung.

**D-02 – SDD werkzeugneutral, zwei gleichberechtigte Startoptionen.** SDD gilt auch für kleine Projekte, proportional zum Umfang. **Spec Kit (Specify) UND OpenSpec müssen in Release 1 wählbar und funktionsfähig integriert sein.** Kein Projekt wird automatisch auf eines festgelegt. Nach Projektidee empfiehlt die KI eine Option mit kurzer Begründung; der Nutzer bestätigt; Auswahl und Tool-Version werden in `config/project.yaml` dokumentiert. Für Lands of Glory ist **Spec Kit** vorgesehen. Die bereits vorhandene sichere Specify-Integration bleibt als geprüfte Option erhalten; OpenSpec wird ergänzend integriert. Wechsel des SDD-Systems nur nach gesondertem Migrationsplan, nie durch stilles Überschreiben bestehender Specs.

**D-03 – Umgebung und SDD-Werkzeug nur nach Bedarf.** Docker/Compose und Devcontainer sind optional. Nach Architekturfreigabe darf die KI innerhalb real gewährter Rechte die nötigen projektbezogenen Abhängigkeiten einrichten, testen und reparieren. **Im bewusst gewählten Devcontainer wird nur das zuvor ausgewählte SDD-Werkzeug** reproduzierbar vorbereitet; außerhalb davon erfolgt ein bewusst ausgelöster Bootstrap. Die neutralen Startadapter/Anleitungen für beide Alternativen müssen ohne Generator verfügbar sein.

**D-04 – Keine ungefragte Agenteninstallation.** Keine automatische Codex-, Copilot- oder andere KI-CLI-Installation, kein Login, kein Agenten-Autostart im generischen Template oder dessen Devcontainer. Offizielle Installationswege nur als **optionale Benutzeraktion** dokumentieren bzw. nach ausdrücklicher Auswahl durchführen. Keine pauschalen Berechtigungserweiterungen, YOLO-Modi oder Deaktivierung von Betriebssystemsicherheit.

**D-05 – Eine kanonische Regelquelle.** `AGENTS.md` enthält allgemeine agentenunabhängige Arbeitsregeln. Copilot-, Codex-, OpenCode-, Kimi- und künftige Adapter sind dünn und duplizieren sie nicht. Keine verbindlichen hardcodierten Modellnamen oder Reasoning-Stufen.

**D-06 – Gezielte Eigenständigkeit, klare Gates.** Genehmigte Routinearbeit, interne Dateiänderungen, Projekt-Setup, Tests und Korrekturen erfolgen ohne unnötige Rückfragen. Architektur-/Umfangsänderungen, Rechte-/Secret-Zugriffe, destruktive Schritte, Deployment, externe Veröffentlichungen und Kosten erfordern die jeweils nötige Entscheidung/Berechtigung. Bestehende **Analyze- und Review-Gates** erhalten. Textregeln erteilen keine technischen Rechte.

**D-07 – Drei gemeinsame Funktionen.** `Setup`, `Check` und `Status` beschreiben Arbeitsabläufe, **nicht drei zwingend neue Skripte**. Bestehende native Werkzeuge verwenden; nur dort Hilfsskripte hinzufügen, wo mehrere stabile Schritte gebündelt werden müssen.

**D-08 – Kompakter nichtblockierender Status.** Nach wichtigen Meilensteinen, Übergängen, Blockaden und vor tatsächlichen Freigaben eine knappe Darstellung `Status | Arbeitsschritt | Kurzbeschreibung` (je Aufgabe idealerweise eine Zeile); darunter nächster Schritt, Blocker und erforderliche Freigabe. Keine künstlichen Prozentangaben, keine Pause für reine Information.

**D-09 – Agentenübergreifender Projektkontext.** Eine gemeinsame `docs/PROJECT_HANDOFF.md` mit Projektstand, aktueller Arbeit, offenen Aufgaben, Entscheidungen/Quellen, Problemen, Prüfergebnissen und Fortsetzung. Bei wesentlichen Schritten und vor geplantem Wechsel pflegen. `AGENTS.md` weist alle Agenten darauf hin; konkrete Erkennung pro Agent überprüfen. Unterschiedliche Arbeitsumgebungen benötigen Git-Synchronisierung. Architekturentscheidungen bleiben in ihren verbindlichen Dokumenten.

**D-10 – Externer Austausch mit ChatGPT.** Kompakte Übergabe kann als Markdown hochgeladen/einkopiert werden; für fundierte Architekturgespräche ist **auf Anfrage ein umfassender Export** aus dem Repo möglich. Rückimport wird **zuerst mit dem aktuellen Repo verglichen**, Konflikte und Abweichungen seit Export werden ausgewiesen, Entscheidungen erst nach menschlicher Freigabe übernommen. Keine ungeprüften externen Vorschläge als operative Anweisungen ausführen.

**D-11 – Template-Versionierung und Updateprüfung.** Bei Beginn einer Arbeitssitzung, sofern Template-Ursprung erreichbar ist, nach veröffentlichten Änderungen des zentralen Template-Repos schauen. Informieren, Relevanz beurteilen und bei Bedarf einen Änderungsplan vorschlagen. **Keine automatische Übernahme** in Projekte. Version/Herkunft und zuletzt übernommener Stand sollen nachvollziehbar sein. Nicht erreichbarer Ursprung blockiert normale Projektarbeit nicht.

**D-12 – Bestandsmigration.** Im **neuen** Repo soll die KI per natürlicher Anfrage das **alte** Repo, möglichst nur lesend, prüfen und einen Übernahmeplan erstellen können. Zwei Strategien vergleichen: (A) frisches Repo aus aktuellem Template + gezielter Import, für kleine/kaum entwickelte Altprojekte bevorzugt; (B) zielgerichtetes In-place-Update im Alt-Repo, häufig für etablierte Projekte. KI-/Tokenaufwand qualitativ mitberücksichtigen. Umsetzung erst nach Genehmigung, Altrepo als Rückfall erhalten, Tests durchführen.

**D-13 – Automatische Qualitätssicherung.** Bei Änderungen am Template laufen automatisch CI-Prüfungen über GitHub Actions. Zu prüfen sind ein neutral kopiertes Projekt, **Spec Kit und OpenSpec separat**, optionale Umgebungen/Profile, Handoff sowie Migrationsabläufe und negative Fehlerfälle. Testfehler sichtbar machen, nicht als Erfolg ausgeben.

**D-14 – Bestehenden Generator nicht ersatzlos löschen.** Nützliche Profile/Dienstvorlagen erhalten, sofern sie zu D-01 passen; **Generator/Scaffolding optional**, niemals Pflichtvoraussetzung für den Start. Wo bestehende Konstruktion D-01 widerspricht, umstrukturieren statt den alten zweistufigen Ablauf beizubehalten.

**D-15 – Zwei neue Repositories statt Umbau.** Das bestehende `template-spec-kit` bleibt als unveränderte, lesbare Referenz erhalten. Es werden ein **neues neutrales Haupt-Template** und anschließend ein **separates Generator-Repository** angelegt. Keine direkte Modernisierung des alten Repos als Standardweg. Das neue Haupt-Template erhält einen neuen dauerhaften Namen, **nicht** den bisherigen Namen; die alte Git-Historie ist als Referenz erhalten, muss nicht in die neue übertragen werden.

**D-16 – Generator-Repositories aus dem neuen Template ableiten.** Erst das neutrale Haupt-Template erstellen, prüfen und als nutzbaren Stand freigeben. Das separate Generator-Repository dann **einmalig auf dieser Template-Basis** anlegen und gezielt um Generatorcode, Schnittstellen, Tests und Release-Mechanismen ergänzen. **Keine zyklische Bootstrap-Abhängigkeit**: Der Generator muss ohne Aufruf seiner eigenen Generatorfunktionen initialisierbar sein. Normalen Projektkopien dürfen keine Generator-Quelltexte beigefügt werden.

**D-17 – Getrennte stabile Versionen und Freigabe.** Für Haupt-Template und Generator gilt je eine unabhängige Versionierung. Neue Generator-Versionen und Template-Versionen dürfen in existierende Projekte **nicht automatisch** eingespielt werden. Die KI prüft bei Sitzungsstart auf Updates, sofern die Quelle erreichbar ist; sie meldet Änderungen/Relevanz und erstellt einen Freigabevorschlag. Projektverwendung erfolgt mit einer nachvollziehbar fixierten, getesteten **stabilen und explizit freigegebenen** Generator-Version, nicht unkontrolliert mit `main`/`latest`.

**D-18 – Pflichtinventur und vollständiger Abgleich.** Vor der Übernahme aus dem Alt-Template alle funktionalen Bestandteile mit evidenzbasiertem Teststatus inventarisieren, pro Funktion vier Wege abwägen (`übernehmen`, `anpassen`, `auslagern`, `weglassen`) und einen freizugebenden Übernahmeplan vorlegen. Nach Umsetzung die Inventurliste gegen die beiden neuen Repositories/Tests abgleichen. Tokenarme strukturierte Skriptinventur vor selektiver KI-Detailanalyse bevorzugen.

**D-19 – Verpflichtender realitätsnaher Praxistest.** Jede zur Freigabe vorgesehene Haupt-Template-Version wird durch ein **temporäres, echtes Projekt aus dem Template** validiert, nicht nur durch statische Tests. Es prüft mindestens neutralen Start, Spec-Kit/Anweisungen, Projektübergabe und – nach Integration – den freigegebenen externen Generator. Automatische CI-Prüfungen bleiben zusätzlich Pflicht. Fehler verhindern die Freigabe; Testartefakte nach dokumentierter Prüfung bereinigen.

**D-20 – Chronologischer, freigabefähiger Implementierungsfahrplan.** Der Umsetzungsplan muss für **jedes Repository** Voraussetzungen, betroffene Dateien, konkrete Arbeiten, Nachweise, erforderliche Entscheidungen, Freigabe-Gates und Rückfalloptionen enthalten. Die IDs und Repository-Namen sind durch den Nutzer vor Beginn der Umsetzung festgelegt: `t0003-ai-project-template` und `t0004-ai-project-generator`. Vor GitHub-Erstellung technisch sicherstellen, dass die Namen und IDs im maßgeblichen Namensraum nicht bereits verwendet werden. Bei Kollision nicht eigenmächtig umnummerieren, sondern Rückfrage stellen.

**D-21 – Bestehende Technologie-Namenskonvention für Repositories übernehmen.** Nach der vom Nutzer aus seiner `AGENTS.md` wiedergegebenen Regel gilt für technische Artefakte die Typkennung `t` (Technologie) beziehungsweise `i` (Infrastruktur), jeweils gefolgt von einer vierstelligen, typbezogen verwalteten ID, einem Bindestrich und einem sprechenden Bezeichner (Beispiele für Dokumente: `t0014-mockoon.md`, `i0004-synology-ds218plus.md`). Für **beide geplanten GitHub-Repositories** wird das Schema nun ausdrücklich ebenfalls verwendet, **ohne `.md`-Endung**: `t0003-ai-project-template` und `t0004-ai-project-generator`. Beide gehören zur Kategorie **Technologie/Entwicklungswerkzeug**, nicht Infrastruktur. Keine zusätzlichen neuen Typen wie `tpl` oder `tool`. Die Nummern `0003` und `0004` sind ausdrücklich gewählt; ihre tatsächliche freie Belegung ist nicht geprüft und muss vor Anlage der Repositories abgeglichen werden.

**D-22 – Private Eigenverwendung.** Beide Repositories werden im **gleichen bisherigen GitHub-Konto**, zunächst **privat**, durch den Nutzer angelegt und ausschließlich von ihm verwendet. Keine öffentliche Veröffentlichung, kein Lizenzmodell/Open-Source-Release ohne gesonderte Entscheidung. Eigene interne Git-Tags und Releases sind unabhängig davon zulässig.

**D-23 – Python-Generator mit einheitlicher CLI.** Die Generatorimplementierung erfolgt in **Python**. Eine plattformneutrale CLI ist die zentrale Schnittstelle, nicht Agenten-spezifische Magie. Verbindlich unterstützt werden **Windows, Linux und GitHub Codespaces**; **macOS wird nicht als unterstütztes Ziel verlangt**. Lokal installierbar, auf Wunsch automatischer Bezug **einer konkret freigegebenen, fixierten GitHub-Release-Version**; keine unkontrollierten Installationen oder Upgrades. Die exakten CLI-Kommandos legt der Agent nach Inventur fest und testet sie.

**D-24 – Zwei Generator-Modi.** **Neuaufbau**: aus einem neutralen Projekt und nach Architekturfreigabe ausgewählte technische Module bereitstellen. **Bestandsübernahme**: bestehendes Repository (zunächst read-only) analysieren und Vergleich **neues Repo + selektive Übernahme** versus **Update im alten Repo** mit konkreten Übernahmevorschlägen, Risiken und Token-/Arbeitsaufwand anbieten. Die Analyse umfasst **Dokumente, Code, Bilder/Assets, Konfigurationen, Tests und gegebenenfalls Datenbank-/Deploymentschnittstellen**; Secrets nicht in Exporte übernehmen. Für **Lands of Glory** ist ein neues Repo mit Übernahme des entschiedenen fachlichen Wissens und Spec Kit vorgesehen, nicht eine pauschale technische Kopie.

**D-25 – Vorschau, Sicherung, Rollback.** Der Generator zeigt **immer zuerst eine Dry-run-Vorschau inklusive Diffs und Konflikten**, fragt die ausdrückliche Freigabe ab und verändert erst danach Dateien. **Vor Änderungen an bestehenden Dateien sichere Backups/Snapshots** anlegen (auch nicht-committete Änderungen respektieren). Niemals still überschreiben. Danach automatisierte Prüfungen; bei Fehlern einen **kontrollierten, sicheren Rückfall** anbieten, ohne nicht zugehörige Zwischenarbeit zu löschen. Automatisches hartes `git reset`/Löschen ist unzulässig.

**D-26 – Modul- und Konfigurationsmodell.** Der Generator hat einen kleinen Kern und getrennte optionale Technologie-/Service-Module. **V1 unterstützen**: Python, Java, TypeScript, Docker/Compose, PostgreSQL, GitHub Actions sowie optionale Webmodule React und PixiJS und Monitoring mit Prometheus/Grafana. **Colyseus und Keycloak** sind bedarfsabhängige Zusatzmodule; keine Pflichtinfrastruktur. Der Agent empfiehlt Module **erst aus den Anforderungen**, legt genehmigte Technologie-/SDD-Auswahl und Modul-Versionen in `config/project.yaml` ab. Keine automatische Auswahl nur wegen vorhandener Module.

**D-27 – Nachvollziehbare Versionsspur.** Template und Generator werden **getrennt mit Semantic Versioning (`MAJOR.MINOR.PATCH`)** verwaltet. Projektmetadaten speichern Template-Herkunft, wirklich übernommene Template-Version, Generator-Version (sofern verwendet), SDD-Werkzeug und verwendete Modulversionen. Generator-/Template-Kompatibilität vor Änderungen prüfen; nur genehmigte stabile Versionen. `CHANGELOG.md` mit verständlichen Änderungen, Breaking Changes und Migrationshinweisen pflegen.

**D-28 – Deutsche Quickstarts, englischer Code.** Jedes neue Projekt enthält eine **kurze deutschsprachige Quickstart-Anleitung**: erster Start, VS Code/Codespaces, Copilot/Copilot CLI, Codex bzw. weitere tatsächlich unterstützte Agenten, CLI-/Terminalstart, SDD-Wahl und Startkommando, Setup/Check/Status, Tests und Arbeitswiederaufnahme. **Code, Schnittstellen und gängige technische Bezeichner auf Englisch**. Nur real geprüfte Kommandos dokumentieren; für noch nicht getestete Umgebungen Grenzen markieren.

**D-29 – Abnahmetests für beide SDD-Systeme und beide Modi.** Vor Gesamtfreigabe reale, temporäre Testprojekte für **(1) Neuaufbau mit Spec Kit, (2) Neuaufbau mit OpenSpec, (3) Bestandsübernahme mit Spec Kit, (4) Bestandsübernahme mit OpenSpec** prüfen, einschließlich Quickstart, CLI-Vorschau/Freigabe, Dateikonflikt/Backup, Rollback und Versionsnachweis. Für umfangreiche Kombinationen gezielte Smoke-Tests je Modul und gründliche Kernfälle; keine unnötige vollständige Matrix jedes Produkts erzwingen.

**D-30 – Repository-Link zur Laufzeit erfragen.** Die GitHub-URL des alten `template-spec-kit` wird **nicht jetzt** in dieses Dokument geschrieben. Beim **ersten Start der Implementierung im neuen Haupt-Repo** fragt der Coding-Agent den Nutzer gezielt nach der URL oder einem lesbaren lokalen Pfad. Er prüft die Quelle vor Analyse und behandelt sie ausschließlich read-only. Bei fehlendem Zugriff freundlich anhalten und Zugang/Alternativpfad anfragen; nicht erraten. Dies ist eine notwendige erste Ausführungsfrage, nicht ein erneut offener Architekturpunkt.


### Noch nicht abschließend individuell bestätigt

Die folgenden **Detailentscheidungen sind Implementierungsempfehlungen, keine stillschweigend erteilten Genehmigungen**:

- **O-01 (nur technisches Detail):** Repo-Trennung, **Python, CLI, Windows/Linux/Codespaces, fixierte lokale Installation, Dry-run/Freigabe** sind entschieden. Nach der Alt-Repo-Inventur nur noch **konkrete Paket-/CLI-Syntax, Verteilung, SDD-Adapter und Abhängigkeits-Pins** technisch ausarbeiten; keine Grundsatzfrage erneut stellen.
- **O-02 (ID-Kollisionsprüfung vor Repository-Erstellung):** Die **Namensnotation und die konkreten IDs sind entschieden**: `t` = Technologie, vierstellige typbezogene ID, Bindestrich, sprechender Bezeichner. Festgelegt sind `t0003-ai-project-template` und `t0004-ai-project-generator`. Vor Anlage die vorhandenen Technologie-IDs in der maßgeblichen Vergabeliste und die GitHub-Repo-Namen auf Kollision prüfen; bei Belegung dokumentieren und den Nutzer nach einer alternativen ID fragen, nicht stillschweigend ändern. Aus den Dokumentbeispielen allein ist die Verfügbarkeit nicht ableitbar.
- **O-03:** Beide Repos privat im selben Konto, vom Nutzer angelegt, nur Eigenverwendung. Offen bleiben nur ggf. konkret notwendige zusätzliche GitHub-Rechte und Repositoryziele. Sicherheitsvorgabe: im generischen Template **keine ownerbezogenen Schreibrechte**, projektspezifisch nur mit ausdrücklicher Zustimmung.
- **O-04:** Umfang und Ausführungsort teurer CI-Matrix-/Cloud-/Codespaces-E2E-Tests; echte Tests priorisieren, aber Kosten und Rechte separat freigeben.
- **O-05:** Welche Agentenadapter zum ersten Release nachweislich getestet werden können. Keine volle Gleichwertigkeit behaupten, wenn nur dokumentiert.

Die Umsetzung darf diese Details vorschlagen und eine sichere, reversible Standardlösung vorsehen; neue Berechtigungen, Kosten oder strukturell weitreichende Änderungen verlangen die passenden Freigaben.

---

## 2. Bestandsprüfung: verpflichtend vor jedem Eingriff

Das Quellenmaterial vom 27.10.2026 nennt folgenden **damaligen**, zu verifizierenden Stand:

- Python-Generator mit Kern, Profilen (`neutral`, `Python`, `TypeScript`, `Java/Maven`) und optionalen Diensten (`PostgreSQL`, `Keycloak`, `Prometheus/Grafana`, FastAPI/PostgreSQL-Rezept).
- `AGENTS.md`, zusätzliche `.github`-Agentenanweisungen, `config/project.yaml`, `docs/DV_KONZEPT.md`, Specify-Wrapper für POSIX/PowerShell.
- Specify 1.0.7, uv-Fallback 0.12.15, Toolumgebung `.artifacts/specify/`; Windows Python-Entrypoint als Smart-App-Control-kompatible Lösung.
- Optionale Devcontainer-Landschaft mit Python 3.13, Compose, GitHub CLI Feature und `postCreateCommand`; bisherige automatische Copilot-Installation über `curl ... | sudo bash`.
- Vorhandene Spec-Kit-Workflow-Gates, GitHub Actions mit `contents: read`, hardcodierte `maieuticus/*`-Zusatzrechte und Referenzziele.
- Unvollständiger Context-/Decision-Handoff im Arbeitsbaum, Status-Task für `folderOpen`, automatischer VS-Code-Taskstart auf `off`.
- CI-Bau/Compose bislang nicht identisch mit vollständigem Devcontainer-Post-Create-Lifecycle; Mock-basierter Regressionstest, vollständiger Codespace-Lauf nicht belegt.

**Zu Beginn tatsächliche Inventarliste erstellen**: Pfad/Datei, Zweck, Aufrufstelle, Verbraucher (Template-Maintainer oder erzeugtes Projekt), Tests, Installations-/Rechtewirkungen, beabsichtigte Maßnahme, potentielle Breaking Changes. Dazu reale Git-Diffs und laufende Änderungen berücksichtigen. Vorhandene Features nicht doppelt implementieren und nicht ungefragt lokale Arbeit überschreiben.

**Pflicht-Ergebnis (tabellarisch):** `ID | Funktion | Quellpfade | Funktionsstatus und Nachweis | Ziel (Template/Generator/entfällt) | Aktion | Begründung | Risiko | Test | Aufwand`. Status mindestens **nachweislich funktioniert / unklar oder ungetestet / nachweislich fehlerhaft**. Die KI entscheidet nicht allein anhand eines Dateinamens, ob eine Funktion funktioniert.

**Tokenarme Arbeitsweise:** zunächst `git ls-files`, Dateibaum, Manifest-/Konfigurationslisten und vorhandene Testberichte skriptgestützt erfassen; auffällige Integrationspunkte gezielt lesen; nur für konfliktreiche, sicherheitsrelevante oder unklare Funktionen tief in Quellcode einsteigen. Sensible Inhalte nicht in den Export übernehmen. Bei unklarem Versionsstand dem Nutzer die Lücke zeigen. **Das alte Repo bleibt read-only.**

**Analyze-Gate A:** Vor jeder Übertragung Inventur und Übernahme-/Auslassungsmatrix zur Entscheidung vorlegen. Nach dem Aufbau wird jede Inventurposition als `übernommen / ersetzt / bewusst entfallen / offen` mit Link zum Test- oder Dateinachweis markiert.

---

## 3. Neues Template: sofort nutzbares neutrales Projekt

### 3.1 Mindestumfang des erzeugten Repository-Roots

**Zielstruktur (Pfadnamen sind vorgeschlagene Konvention; vorhandene gleichwertige Pfade bevorzugen):**

```text
<neues-projekt>/
├── README.md                        # Einstieg: Projektidee, Spezifikationsstart
├── AGENTS.md                        # einzige kanonische KI-Arbeitsanweisung
├── .gitignore                       # keine Secrets, Tool-Caches oder generierten Daten
├── config/
│   └── project.yaml                 # Projekt- und Template-Herkunft
├── docs/
│   ├── DV_KONZEPT.md                # verbindliche Projektbeschreibung, anfangs schlank
│   └── PROJECT_HANDOFF.md           # aktueller, anfangs leer/initialer Stand
├── docs/SDD_QUICKSTART.md          # Auswahl und Start: Spec Kit ODER OpenSpec
├── .specify/                        # nur notwendige kompatible Spec-Kit-Startdateien
└── scripts/                         # schlanke wählbare SDD-/Bootstrap-Hilfen
```

Je nach tatsächlichem Spec-Kit-Workflow zusätzliche **erforderliche** Constitution-/Spec-Vorlagen und sichere Editoradapter behalten. Die Struktur ist **keine Pflicht, künstlich leere Verzeichnisse anzulegen**. Konkreter Anwendungscode oder Laufzeitkonfigurationen werden nicht ohne genehmigte Architektur generiert. Ein passendes Testskelett/grundlegender Check ist zulässig, sofern sprachneutral und ohne Pflichtinstallation.

### 3.2 GitHub-Template-Kopie muss wirklich sauber sein

GitHubs Template-Funktion kopiert den Repository-Inhalt, **nicht selektiv nur ein Unterverzeichnis**. Deshalb dürfen Wartungswerkzeuge des bisherigen Generators oder seine Sprach-/Dienstprofile nicht versehentlich als unnötiger Ballast in **jedem** neuen Projekt landen.

**Verbindlicher Auftrag:** Das **neue** Haupt-Template wird bewusst ohne Generator-Quelldateien und ohne Sprach-/Dienstprofile erstellt. Der bisherige Generator wird anhand der freigegebenen Inventur **in ein eigenes Repository** übertragen (kein Einbetten in jedes neue Projekt). Konkrete Start- und Aufrufmechanik nach Audit entwerfen. Wertvolle Generatorfunktionen nur nach Beleg oder gesonderter Behandlung ihrer Unklarheiten übernehmen; jedes migrierte Modul regressionsprüfen.

**Akzeptanztest:** Simuliere realistisch „Use this template“ oder prüfe mit einem temporären tatsächlich erzeugten Projekt. **Ohne** Generatorlauf muss dieses Projekt Anforderungen dokumentieren, die KI-Regeln nutzen und den SDD-Start ermöglichen; es enthält keine ungefragten Technologieprofile, Agenteninstallationen, produktspezifischen Zugangsdaten oder nicht benötigte Generator-Interna.

### 3.3 Erster Dialog im neuen Projekt

- KI liest Projektkontext; erkennt neutralen Anfangszustand.
- Fragt bzw. verarbeitet freie Idee; klärt Anforderungen und Erfolgskriterien, hält sie im Spec-Workflow fest.
- Bietet Architekturvorschlag mit konkreten Alternativen, Trade-offs und nötigen Diensten; **wartet auf die erforderliche Architekturfreigabe**.
- Nach Freigabe optionales Scaffolding **oder** direkte Einrichtung im Projekt: Die Architektur bestimmt das Werkzeug, nicht umgekehrt.
- Handoff und Dokumentation aktuell halten; keine Dummy-App oder Datenbank als Standard erzwingen.

---

### 3.4 Neues Generator-Repository: Zielbild und Abgrenzung

Das Generator-Repository wird **erst nach Freigabe eines funktionsfähigen Haupt-Templates** einmalig aus diesem erstellt und als eigenes Projekt gepflegt. Es erbt `AGENTS.md`, DV-Konzept, SDD/Specify und Übergabe; Generatorbestandteile werden **nur hier** ergänzt. Nach tatsächlichem Audit kann folgende beispielhafte Struktur angepasst werden:

```text
<t0004-ai-project-generator>/
├── AGENTS.md
├── README.md
├── docs/
│   ├── DV_KONZEPT.md
│   ├── PROJECT_HANDOFF.md
│   └── GENERATOR_CONTRACT.md
├── .specify/                    # ausgewähltes SDD-System, keine Pflichtdoppelstruktur
├── src/                        # echte Python-CLI/Generatorlogik nur bei belegtem Bedarf
├── profiles/                   # nur geprüfte, bewusst gewählte Profile
├── tests/                      # Unit-, Integrations- und Regressionstests
├── .github/workflows/          # CI mit Minimalrechten
├── VERSION                     # oder eine andere EINHEITLICHE Versionsquelle
└── CHANGELOG.md
```

**Generator-Vertrag (`docs/GENERATOR_CONTRACT.md`, bei Implementierung konkretisieren):**

- **Python-CLI als verbindlicher Aufruf**, definierte Subcommands/Optionen, Exitcodes, unterstützte Plattformen Windows/Linux/Codespaces, minimale Umgebung und klare Fehlerrückgaben;
- vor Aufruf **Architekturfreigabe** und Bestimmung eines **stabilen, explizit freigegebenen Tags/Commits**;
- **zwingender Standardmodus Vorschau/Plan (`dry-run`)** mit Diffs, anzulegenden/zu ändernden Dateien, Konflikten, Abhängigkeiten und optionalen Kosten; schreibender `apply`-Schritt nur nach ausdrücklicher Freigabe;
- idempotente Wiederholung soweit technisch möglich, **Backups vor Änderungen bestehender Dateien**, kein ungefragtes Überschreiben, gezielte Konfliktentscheidung und **sicherer Rollback ohne Verlust fremder Zwischenarbeit**;
- sichere Template-Einbindung ohne obligatorische Netzwerk-Installation, keine dynamische Ausführung beliebiger Skripte ohne Prüfung; Zugriff auf GitHub und Toolinstallationen nur mit vorhandenen Berechtigungen;
- Generator-Version und angewendetes Profil im Projekt nachvollziehbar vermerken, ohne zweite widersprüchliche Metadatenwahrheit zu schaffen;
- Regressionen für aus dem alten Repository übernommene Profile, inklusive Windows/POSIX wo einschlägig;
- Generator lässt sich **selbst ohne Generator** entwickeln, testen und veröffentlichen.

**Wichtig:** Die Namen und Struktur sind **Vorschläge**, keine behaupteten realen Dateien. Erst Audit, dann konkrete Modul-/Paketentscheidung. Es besteht keine Pflicht, jedes alte Profil unverändert weiterzuführen; nicht übernommene Funktionen müssen jedoch ausdrücklich nach Inventur freigegeben werden.

---

## 4. KI-Arbeitsregeln, Sicherheit und plattformneutrale Integration

1. **`AGENTS.md` als Single Source of Truth:** Den vorhandenen Entwurf `AGENTS_template_entwurf.md` als fachliche Grundlage verwenden, aber vorhandene projektspezifische Regeln/Constitution und aktuelle Repo-Regeln **vor dem Ersetzen diffen**. Inhaltliche Duplikate in Copilot-Profilen, `.github/copilot-instructions.md` usw. durch knappe Verweise/Adapter ersetzen; funktional notwendige native Dateien belassen.
2. **Agentenadapter:** Für Codex, Copilot, OpenCode, Kimi und weitere Agenten dokumentieren, welche Startregel/Adapterdatei sie tatsächlich auswerten. Nicht voraussetzen, dass jedes Werkzeug `AGENTS.md` oder ein beliebiges Handoff automatisch liest. Fehlende Erkennung möglichst durch **minimalen Adapter**, eine kleine Bootstrapanweisung oder klare Startanweisung lösen. Die **Wahrheit** bleibt in den gemeinsamen Repo-Dateien.
3. **Rechte:** `AGENTS.md` steuert Verhalten, **nicht** GitHub-, Host-, Sandbox- oder API-Permissions. Minimalrechte als Ausgangspunkt; zusätzliche technische Berechtigungen werden nur im tatsächlichen Client oder Projekt gezielt vergeben.
4. **Autonomie:** Genehmigte Worktree-Änderungen, projektbezogene Container, Checks, Reparaturen und Dokumentation eigenständig durchführen; tatsächliche Tool-Sandbox-/Runtime-Freigaben beachten. Keine eigenständige Privilegienausweitung, Secret-Exfiltration, produktiven Deployments, destruktiven Datenoperationen, externen Schreibaktionen oder bezahlten Ressourcen.
5. **SDD-Gates:** Bestehende Sequenz `specify → plan → tasks → analyze → human Analyze gate → implement → checks → converge → human Review gate` erhalten. Workflow-Freigaben und Betriebssystemrechte sind getrennte Mechanismen.
6. **Modellwahl:** Keine fest verdrahteten Modellnamen, Reasoning-Stufen oder Agentenpräferenzen als global verbindliche Regel.
7. **Status:** Einheitliche Kurzform; kein eigener Statusdienst nötig. Automatische Meldung ist ein Verhaltensziel, keine Garantie für Tool-Hooks ohne Test.

**Abnahmetest:** Mindestens Codex und Copilot an realistischen Projektstarts prüfen; für andere Agenten, die zum Release nicht ausführbar sind, den Integrationsstand als „dokumentiert, nicht E2E-verifiziert“ kennzeichnen. Sicherstellen, dass der Einstieg den Handoff anfordert und nicht bloß zufällig einmal gelesen wurde.

---

## 5. Spec-Driven Development und optionale Entwicklungsumgebung

### 5.1 Gleichwertige Werkzeuge ab Release 1: Spec Kit und OpenSpec

- Die **Methodik** (Anforderungen → geklärte Spezifikation → Plan → Aufgaben → Umsetzung → Prüfung → Review) ist agenten- und toolneutral in `AGENTS.md` beschrieben. **Spec Kit (Specify) und OpenSpec** müssen **beide** in Version 1 über dokumentierte, tatsächlich getestete Wege aktivierbar sein.
- Beim **neuen neutralen Projektstart keine Pflichtwahl und keine ungefragte globale Installation**. Eine KI stellt nach deiner Projektidee die Unterschiede und eine begründete Empfehlung dar. Du gibst die Auswahl frei; danach `config/project.yaml` aktualisieren und nur das gewählte System bootstrappen. Wahl bei späterem Bedarf möglich, aber vorher Migrationsplan für bestehende Spezifikationen und Freigabe.
- **Spec Kit:** Vorhandene getestete Version-Pins, uv-/Python-Wrapper und besonders den PowerShell/Windows-Python-Entrypoint als sicherheitsverträgliche Lösung nach Bestandsprüfung erhalten. Keine Deaktivierung von Windows-Schutzfunktionen. Kein ungetestetes Upgrade der CLI bei der Übernahme.
- **OpenSpec:** Eigene getestete Einrichtungs-/Startanleitung und möglichst schlanke Adapter, inkl. nachgewiesener Unterstützung für Copilot/Codex und CLI, anlegen. Benötigte Laufzeit und Versions-Pins erst nach Prüfung offizieller Anforderungen festlegen; keine unbestätigten Kommandos in Quickstarts.
- Sowohl **Spec Kit als auch OpenSpec** benötigen einen funktionsfähigen Ablauf unter Windows, Linux und Codespaces. Nicht jede KI-Oberfläche verwendet dieselben Slash-Commands; tatsächliche Zuordnung dokumentieren und testen. Kompatibilitätsunterschiede offen ausweisen.
- **Lands of Glory:** neues Repo aus dem fertigen Template, **Spec Kit** explizit wählen und die bestätigten Regeln/Entscheidungen aus dem bisherigen fachlichen Material übernehmen. Keine ungeprüfte Neu-Implementation oder Architekturübertragung.

### 5.2 Docker/Devcontainer

- Devcontainer, Docker und Compose sind **optional**. Für kleine Projekte soll CLI-/SDD-Start ohne Docker möglich sein.
- Nach Projektarchitektur- und SDD-Wahl nur benötigte Python-/Java-/TypeScript-Werkzeuge bzw. Dienste einrichten. In einem bewusst gewählten Devcontainer das **ausgewählte** SDD-System reproduzierbar bereitstellen.
- **Kein ungefragter Agenteninstaller**: automatischen Copilot-CLI-Installer und dessen `sudo`-Kette aus generischem `postCreate` entfernen. Keine automatisch startenden KI-Sitzungen oder Logins.
- Globale Hoständerungen, OS-Sicherheitsänderungen und externe Schreibrechte nur nach ausdrücklicher Genehmigung. `.env`-Beispiele und read-only-Mounts sauber handhaben; keine echten Secrets in Git.
- Generatorinstallation: **lokale, pinbare Python-CLI**; Abruf einer **freigegebenen stabilen GitHub-Version** nur auf bewussten Auftrag. Klare Signale für Offline-Fall und Versionskonflikt.

### 5.3 Prüfungen

- Spec-Kit- und OpenSpec-Bootstrap jeweils in POSIX/Windows/Codespaces soweit technisch realisierbar testen; tatsächliche Abdeckung ausweisen, statt Plattformgleichheit zu behaupten.
- Besonders bei Spec Kit die bestehende Windows-Sicherheitsanforderung als Regressionstest erhalten.
- Echten Devcontainer-Post-Create-Prozess getrennt vom bloßen Compose-Build prüfen; ausgewähltes SDD-System wird korrekt vorbereitet, kein KI-Agent ungefragt installiert.
- GitHub Actions und ausführbarer Quickstart müssen zu denselben stabilen Pin-Versionen passen.

---

## 6. Gemeinsame Übergabe und externer Architektur-Abgleich

### 6.1 Kanonische Informationen

- `docs/PROJECT_HANDOFF.md`: **flüchtiger Arbeitsstand**: Standdatum, betroffener Branch/Commit, aktive Aufgabe, erledigt, offen, Blocker, letzte Prüfergebnisse, konkreter nächster Schritt, nicht synchronisierte Änderungen.
- `docs/DV_KONZEPT.md`: verbindliche Projektbeschreibung/Architektur, soweit bestätigt.
- Bestehende Specs/Constitution/ggf. ADRs: kanonische verbindliche Anforderungen, Begründungen und Freigaben. Neue ADR-Struktur nur wenn ausreichend Nutzen besteht; keine künstliche Dateivermehrung.
- `AGENTS.md`: Verhaltensregeln und Verweise, **keine** Kopie des laufenden Projektstandes.

**Invariante:** Ein Status-Update darf genehmigte Architekturentscheidungen nicht unbemerkt ändern. Handoff verweist auf Entscheidungen. Git-Status und reale Dateien haben Vorrang vor veralteten Zusammenfassungen.

### 6.2 Laufender Pflegeprozess

- Beim Start der Sitzung Handoff lesen und mit realem Repositoryzustand abgleichen.
- Nach **wesentlichen** Implementierungs-/Entscheidungs-/Testmeilensteinen und vor geplantem Agentenwechsel Handoff aktualisieren; keine unnötige Änderung nach jedem Befehl.
- Git-Synchronisierung zwischen Arbeitsumgebungen berücksichtigen. **Nicht eigenmächtig pushen**, falls technische Freigabe/Workflow dies nicht vorsieht; Synchronisierung als offen ausweisen.
- Secrets, Personen-/Zugangsdaten, Tokens und sensible Laufzeitwerte nie in Handoff/Export schreiben.

### 6.3 Auf Anfrage exportieren, extern besprechen, geprüft rückimportieren

1. **Export:** Kompakt = `PROJECT_HANDOFF.md`; vollständig = ein generiertes Markdown-Artefakt, das Repo-Stand, Architektur, Specs, Implementierungsstand, verknüpfte Entscheidungen, offene Fragen, Tests und Quellpfade/Commit enthält. Vor Ausgabe Geheimnisse prüfen/ausfiltern. Die Aufbereitung erfolgt bei Nachfrage, nicht per ständigem Cloud-Aufruf.
2. **Externe Diskussion:** ChatGPT oder andere KI erhält Markdown. Rückgabe ist vorläufig und darf keine Rechte oder Entscheidungen selbst erteilen.
3. **Importanalyse:** Ergebnis gegen **aktuelle** Dateien und den gespeicherten Exportstand vergleichen. Neue Punkte, Widersprüche, fehlende Informationen und mögliche Auswirkungen kategorisieren; Eingriffe an genehmigten Architekturentscheidungen markieren.
4. **Freigabe:** Verständliche Entscheidungsvorlage (übernehmen / anpassen / verwerfen / offen); erst danach verbindliche Dokumente bzw. Implementierung aktualisieren.
5. **Abschluss:** Aktualisierte Entscheidung, Tests, Version und Handoff dokumentieren. Funktionierende bereits begonnene Context-/Decision-Handoff-Komponenten nach Möglichkeit integrieren, nicht parallel neu erfinden.

**Abnahmetest:** Ein externer Vorschlag widerspricht der aktuellen Architektur und wird **nicht** automatisch eingebaut; ein Export aus einem älteren Commit führt beim Reimport zu einer Warnung, wenn sich das Repository inzwischen verändert hat.

---

## 7. Template-Herkunft, Releases und Updateprüfung

### 7.1 Vorgeschlagenes Metadatenschema

Bestehende `config/project.yaml` bevorzugen, statt eine zweite Datenquelle einzuführen. **Beispiel, kein Beleg für aktuell vorhandene Felder:**

```yaml
project:
  name: ""
template:
  source: "<konfigurierte GitHub-Repo-URL>"
  release: "<letzte übernommene veröffentlichte Version>"
  base_commit: "<SHA der zugrunde liegenden Template-Revision>"
  last_update_check: null
```

Metadaten sollen reale Herkunft/Revision verlässlich abbilden; keine erfundenen Versionsnummern. Die Herkunft muss in den neu erzeugten Repositories gesetzt sein; falls GitHub „Use this template“ keinen dynamischen Wert einträgt, mit **dokumentierter fester Release-Metadatei im Template selbst** arbeiten und bei der Kopie nur projektindividuelle Angaben ergänzen. Sicherstellen, dass die Angabe später nicht irrtümlich mit der aktuellen Upstream-Version gleichgesetzt wird.

### 7.2 Releases und Änderungsübersicht

- Definierte veröffentlichte Template-Versionen (z. B. SemVer-Tags) und ein nachvollziehbares `CHANGELOG.md`/Release-Notes-Konzept.
- Relevante Änderungskategorien: Arbeitsregeln, Specify/Tooling, Projektstruktur, Adapter, CI, Sicherheit, optionale Profile, Breaking Changes und Migrationshinweise.
- Die **zuletzt angewendete** Template-Version eines Projekts unabhängig von der **verfügbaren Upstream-Version** verwalten.

### 7.3 Nichtblockierende Prüfung

- **Bei Arbeitssitzungsstart**, sofern Netzwerk und Zugriff vorhanden: verfügbare veröffentlichte Version und Änderungen mit Projektstand vergleichen; Ergebnis knapp melden. Bei Bedarf konkrete Differenzen/Betroffenheit analysieren.
- Keine Pflicht zur Netzwerkfreigabe, zum Credential-Login oder zur externen Schreibaktion allein für die Prüfung; Netzwerkversagen/fehlende Berechtigung melden, Arbeitsauftrag normal fortsetzen.
- Relevanz vor ausführlicher Analyse eingrenzen: zuerst Metadaten/Changelog und nur betroffene Dateien vergleichen; große wiederholte Token-intensive Gesamtreviews vermeiden.
- Nicht automatisch updaten; nach Freigabe in prüfbaren Schritten durchführen, projektindividuelle Änderungen erhalten und dokumentierte Version erst nach erfolgreicher Anwendung erhöhen.
- **Technikgrenze:** Eine reine Agentenregel garantiert keine Hintergrundprüfung. Für ausgewählte Umgebungen eine kleine **explizit ausführbare** portabel getestete Prüfroutine vorsehen, sofern nötig; Startintegration nur dort als „automatisch“ bezeichnen, wo zuverlässig nachgewiesen.

**Abnahmetests:** (a) aktueller Projektstand → „keine neue Version“; (b) veralteter Projektstand → Updatehinweis/Betroffenheit, **keine Dateiänderung**; (c) kein Netzwerk → verständliche Meldung, kein Abbruch; (d) projektspezifische Abweichung → Konfliktwarnung statt Überschreiben.

---

### 7.4 Zwei unabhängige Release-Spuren

- **Haupt-Template:** Git-Tags/Releases kennzeichnen getestete, genehmigte Zustände. Die Erstellung des Generator-Repos erfolgt von einem freigegebenen Haupt-Template-Stand; spätere Änderungen am Template werden dem Generator nur **geprüft und mit Freigabe** angeboten.
- **Generator:** eigener stabiler Release-Kanal, eigenes Changelog und Kompatibilitätsübersicht zu Template-Versionen. In einem Projekt muss die **tatsächlich verwendete Generator-Version** nachvollziehbar sein.
- Keine unkontrollierte Benutzung von `main`/`latest` als Generator-Abhängigkeit; Download-/Cache-/Pinning-Verfahren ist zu implementieren und zu testen, wenn ein automatischer Aufruf vorgesehen ist.
- Beim Updatecheck nach Möglichkeit beide Quellen abfragen; Ausfall/Offline-Modus meldet „nicht geprüft“ statt still „aktuell“. Keinerlei ungefragte Updates.

---

## 8. Übernahme aus einem alten Repository („Template Migration“)

Diese Fähigkeit muss **im frisch erzeugten Projekt** durch KI-Anweisungen und einen einfachen reproduzierbaren Ablauf nutzbar sein, ohne zuvor ein eigenständiges großes Migrationsframework zu programmieren.

**Auslöser (natürliche Sprache):** „Analysiere mein altes Repository und schlage vor, was ich sinnvoll in dieses neue Projekt übernehmen soll.“

**Voraussetzung:** Nutzer benennt das Altprojekt und erteilt den für die Analyse nötigen Zugriff. Altprojekt zunächst **read-only**; kein heimliches Klonen geschützter Quellen oder Nutzung ungewährter Credentials.

**Analyseablauf:**

1. Altprojekt und neues Template-Repositorium inventarisieren: Git-Status, Sprache/Dienste, vorhandener Code, Dokumentation, Tests, Spezifikationen, Konfiguration, Datenhaltungs-/Migrationsabhängigkeiten, Geheimnisse (nur Vorhandensein, nicht Inhalte exportieren).
2. Relevantes Material markieren: **unverändert kopieren / transformieren / neu erzeugen / nicht übernehmen**. Altes Template-Gerüst nicht blind übernehmen.
3. **Strategie A** (neues Repo + selektiver Import) und **Strategie B** (In-place-Modernisierung) anhand Umfang, Betriebseinbindung, Git-Historie, Tests, Risiken, Kompatibilität und **qualitativem KI-/Tokenaufwand** vergleichen. Keine unbelegten absoluten Token-/Zeitersparnisse behaupten.
4. Prüfen, ob Datenbankdaten, Deployments, Secrets, GitHub-Integrationen oder CI besonders gesichert/migriert werden müssten. **Keine Live-Datenbank oder Produktion ohne neue Genehmigung anfassen.**
5. Konkreten Migrations- und Testplan mit Rückfallweg vorlegen und **Freigabe abwarten**.
6. Danach genehmigte Dateiübernahme möglichst unverändert, nur nötige Anpassungen, Integrations- und Regressionstests, Handoff-/Template-Version dokumentieren.

**Sonderfälle:** Ausgangs-Template-Version unbekannt → Unsicherheit dokumentieren; nicht erraten. Altes Repo enthält uncommittete Änderungen → nicht überschreiben; vorher sichern/entscheiden. Ein neuer Dateikopiervorgang überträgt **nicht automatisch Git-Historie**; falls Historienkontinuität gewünscht, ausdrücklich planen. Ein neues GitHub-Repo ersetzt nicht automatisch Issue-, Release-, Branch-Protection- oder Deployment-Konfigurationen.

**Abnahmetest:** Kleines Testprojekt mit 2–3 funktionsfähigen Dateien und eigenen Dokumenten: Analyse erkennt selektiv zu übernehmendes Material, erstellt zwei Strategien und führt **vor Freigabe keinerlei Schreibvorgang** aus. Nach Freigabe bleiben Altdateien unverändert, importierter Code funktioniert und neues Standardgerüst bleibt erhalten.

---

## 9. GitHub-Rechte, Referenz-Repositories und externe Integrationen

**Ist (zu verifizieren):** GitHub Actions `contents: read`, Devcontainer-spezifische `maieuticus/*`-Rechte `contents: read`, `issues: write`, sowie feste Einträge in `config/repositories.yaml`.

**Implementierungsempfehlung zur Freigabe:**

- Generisches Template soll **keine owner-/organisationsspezifischen Zusatzrechte** oder feste Contributor-/Referenz-Repositories ungeprüft an neue Projekte vererben.
- Standard GitHub Actions **Least Privilege**, wo anwendbar `contents: read`. Zusätzliche Rechte nur bei tatsächlich benötigtendem Feature, kleinster Scope, dokumentierter projektspezifischer Opt-in.
- Externe Referenzen grundsätzlich optional und read-only; feste Maintainer-Ziele aus dem generischen Projektkopf entfernen oder in bewusste projektbezogene Konfiguration verschieben.
- Existierende Maintainer-Workflows nicht stillschweigend zerstören: vor Migration Verbraucher/Abhängigkeiten ermitteln; Trennung auf Projekt- und Maintainer-Seite testen.
- GitHub-App-/OAuth-/Token-/Cloud-Rechte **nicht** aus dieser Spezifikation ableiten oder erhöhen. Vor einem realen Cloudtest separat Freigabe für Quelle, Secrets, Ressourcenkosten und Schreibumfang einholen.

**Abnahmetest:** Aus frischem Template erstelltes Repository fordert keine fremden orgbezogenen Schreibrechte an und enthält keine festverdrahteten `maieuticus/*`-Ziele. Ein bewusst konfiguriertes Projekt kann zusätzliche Rechte separat erhalten.

---

## 10. Testkonzept und GitHub Actions

### 10.1 Pflichtprüfungen bei Pull Requests und relevanten Pushes

1. **Struktur/Schema:** erforderliche Dateien und Links vorhanden; `project.yaml`/Template-Metadaten plausibel; Markdown/YAML/Shell-Konfiguration gültig; keine doppelt kanonischen Regeln.
2. **Neutraler Template-Start:** direkte GitHub-Template-Kopie realistisch nachbilden; ohne Generator/Spezial-Login/agentenabhängige Installation SDD-Einstieg erfolgreich; keine ungefragten Sprache-/DB-Profile.
3. **Spec Kit und OpenSpec:** separater funktionsfähiger Startpfad je Werkzeug; Version-Pins; POSIX/Windows-/PowerShell-Regressionsprüfungen für Spec Kit; OpenSpec-CLI/Adapter und Doku prüfen. Keine Windows-Sicherheitsdeaktivierung.
4. **Devcontainer:** erforderliche Konfiguration/Compose validieren, Container tatsächlich erstellen und relevante `postCreate`-Schritte testen; **ausgewähltes Spec Kit oder OpenSpec ja, ungefragter Agenteninstaller nein**.
5. **Handoff:** Test für Erzeugung/Aktualisierung, leere Ausgangsübergabe, keine Überschreibung genehmigter Entscheidungen, Export-/Rückimport-Konflikt (soweit Funktionen implementiert).
6. **Template-Update:** Tests für gleiche/neue Version, nicht verfügbaren Ursprung, eigene Anpassungen; Updatehinweis ohne Dateiveränderung.
7. **Migration:** Vergleichsplan aus kleinem Altprojekt, read-only bis Freigabe, selektive Übernahme und Funktionsprüfung.
8. **Generator/Optionen:** Bestehende sinnvolle Python-/TypeScript-/Java- und Dienstvorlagen regressionsprüfen **an ihrem künftigen Speicherort**, nicht durch erzwungenes Einbetten in jedes neue Projekt.
9. **Security/Permissions:** keine Secrets, keine automatischen Agenteninstaller, keine impliziten GitHub-Schreibrechte; auf Dateiebene nachprüfen.

### 10.2 CI-Konfiguration

- Automatischer Start auf Pull Requests und relevanten Pushes; fail-fast bei gefährlichen Grundregressionen, aber aussagekräftige Einzelresultate.
- Möglichst deterministische, lokal reproduzierbare Tests; Versions-Pins erhalten. Netzwerkintensive/teure E2E-Prüfungen gegebenenfalls in klar ausgewiesene zusätzliche Jobs/Release-Gates auslagern.
- Keine Standard-CI, die für normale Template-Checks zusätzliche GitHub-Secrets, Produktionsumgebung oder `sudo`-Installationen verlangt.
- Die vorherige **Lücke zwischen Compose-Build und tatsächlichem Post-Create-Lifecycle** explizit schließen oder bis dahin sichtbar als nicht abgedeckt ausweisen.
- Failing CI darf nicht als releasefähig markiert werden. Neue Template-Version erst nach vereinbarten Pflichtprüfungen veröffentlichen.

### 10.2a Verpflichtender Praxistest als Release-Gate

1. Aus dem **freizugebenden Haupt-Template** ein temporäres, isoliertes Projekt **wie bei „Use this template“** erzeugen; keine Generatorquellen übernehmen.
2. Ersten Projektstart und „Ideen zuerst“ prüfen: README/Spec-Start, `AGENTS.md`/tatsächliche Agentenadapter, `docs/PROJECT_HANDOFF.md`, optionaler Spec-Kit-Start.
3. Einen dokumentierten KI-Umgebungswechsel mit realem Handoff demonstrieren (welche Agenten getestet wurden, welche nicht); keine universelle Auto-Erkennung behaupten.
4. Später nach Integration eine **freigegebene** Generator-Version nutzen: Vorschau → ausdrücklich freigegebene Architektur → ein kleines bewusst gewähltes Scaffolding-Profil → Build/Test, Versionsnachweis und Fehlerfall.
5. Abgleich aller erforderlichen Funktionsinventur-Positionen mit dem neuen Zielzustand; fehlende Funktionen und bewusste Abweichungen offenlegen.
6. **Scheitert ein Pflichtschritt, keine Freigabe.** Temporäre Artefakte sicher bereinigen; keine externen Kosten oder GitHub-Mutationen ohne die dafür nötige Genehmigung.

CI soll kostengünstige Prüfungen bei PR/Push ausführen. Schwerere echte Cloud-/Agentenprüfungen können auf das Release-Gate beschränkt sein, wenn ihre Kosten/Berechtigungen separat geklärt sind; ein nicht durchgeführter Test darf nicht als bestanden gelten.

### 10.3 Prüfmatrix / dokumentierte Nachweise

| Szenario | Erwarteter Nachweis |
|---|---|
| GitHub-Template-Kopie | **Temporäres reales Projekt** startet neutral ohne Generator; keine Generatorquellen |
| Kleinprojekt ohne Docker | Planung und wählbares SDD-Werkzeug funktionieren ohne Containerpflicht |
| Gewählter Devcontainer | Ausgewähltes Spec Kit oder OpenSpec vorbereitet; Agenten nicht automatisch installiert |
| Codex / Copilot | gemeinsame Anweisungen und Handoff nachvollziehbar gelesen |
| Kimi / OpenCode | Adapter geprüft oder Teststatus ausdrücklich dokumentiert |
| Externer ChatGPT-Rückimport | Konflikte sichtbar, keine Übernahme ohne Freigabe |
| Template-Version veraltet | Hinweis/Plan, keine Selbstaktualisierung |
| Altprojektmigration | Plan vor Mutation; Altrepo als Rückfall erhalten |
| Generator-Release & Integration | Separater Repo-Release/Changelog, freigegebene Version gepinnt; Dry-run, Scaffolding und Regression erfolgreich |
| Generator-Selbstbootstrap | Generator-Repo ist aus freigegebenem Haupt-Template initialisiert und benötigt keinen eigenen Generator zum Start |
| Inventur-Abdeckung | Jede Quelle ist übernommen, angepasst, ausgelagert oder freigegeben verworfen, mit Nachweis |
| GitHub-Rechte | Kein ownerbezogener Schreibzugriff im generischen Projekt |
| Windows | Specify-Einstieg ohne Sicherheitsfunktion abzuschalten |

---

## 11. Chronologischer Umsetzungsfahrplan für beide neuen Repositories

**Verbindliche Reihenfolge:** **Nutzerbestätigte `t`-IDs vor Anlage gegen Bestand prüfen → Alt-Repo lesen → Übernahme freigeben → neues neutrales Haupt-Template `t0003-ai-project-template` aufbauen → Haupt-Template prüfen und freigeben → daraus Generator-Repo `t0004-ai-project-generator` erstellen → Alt-Generator gezielt übertragen → Generator freigeben → beide integrieren und Ende-zu-Ende testen → Migration von Altprojekten prüfen → Abschlussdokumentation.**

Bei jedem Schritt im Statusbericht `Status | Arbeitsschritt | Kurzbeschreibung`, daneben **aktueller Befund, nächster Schritt, Blocker, konkrete Freigabe**. Keine erfundenen Prozentwerte oder unnötigen Zwischenfreigaben.

### Schritt 0 – Read-only-Inventur des alten `template-spec-kit`

- **Voraussetzungen:** lesender Repo-Zugriff, Quellbranch/-Commit, bekannte Baseline und `AGENTS_template_entwurf.md` (wenn vorhanden).
- **Arbeiten:** Git-Bestand, Struktur, Testfälle, Generatorprofile, Devcontainer/Specify, Handoff, Security/CI inventarisieren; Funktionsstatus mit Nachweisen erfassen; reproduzierbare Bestandsaufnahme möglichst skriptbasiert.
- **Ergebnis/Dateien:** Inventur-MD/CSV (Quellpfad, Funktion, Testergebnis), Vergleich zur alten Implementierungsvorgabe; keine Quelländerung.
- **Freigabe-Gate A:** Matrix `übernehmen / anpassen / Generator / weglassen` samt Risiken, Auswirkung und grobem KI-/Tokenaufwand zur Zustimmung vorlegen.
- **Test/Rückfall:** Alt-Repo unverändert; `git status`/Commit sichern und Wiederholbarkeit der Analyse prüfen.

### Schritt 1 – Neues Haupt-Template aufbauen (`t0003-ai-project-template`)

- **Voraussetzungen:** freigegebene Übernahmematrix; technische Rechte zur Repoerstellung vorhanden; vor GitHub-Anlage Kollisionsprüfung für `t0003` und den Repo-Namen erfolgreich abgeschlossen.
- **Arbeiten:** von leerem, **neuem** Repo ausgehen, nur freigegebene neutrale Teile selektiv übernehmen; README, `.gitignore`, `AGENTS.md`, **wählbare Spec-Kit-/OpenSpec-Startpfade**, `docs/DV_KONZEPT.md`, `docs/PROJECT_HANDOFF.md`, **deutsche Quickstarts**, Versionsherkunft, minimale sichere Bootstraps/Adapter und Actions. **Keine** alten Generatorquellen, Technologieprofile, Secrets oder zwingenden Container.
- **Ergebnis/Dateien:** schlüssiges Minimal-Template, dokumentierter Datei-/Feature-Abgleich und offene Punkte.
- **Gate B:** Projektstart, Spec Kit **und OpenSpec als Alternativen**, Regeln und Quickstart ohne Generator nachweisen; neue Architekturabweichungen vor Umsetzung klären.
- **Rückfall:** eigener neuer Branch/Commits; altes Repo bleibt Referenz.

### Schritt 2 – Haupt-Template pflegen, CI/Praxistest und Grundversion freigeben

- **Arbeiten:** Startregeln und Agentadapter realitätsnah testen, Handoff/Export/Rückimport und Updatecheck sicher gestalten; GitHub Actions mit minimalen Rechten und Regressionstests; temporäres Projekt durch `Use this template` oder exakte Simulation erstellen.
- **Ergebnis:** verifizierter, dokumentierter **freigegebener Ausgangsstand** des Haupt-Templates, auf dessen Basis das Generator-Repo erzeugt werden kann (Tag/Commit eindeutig notieren).
- **Gate C:** Haupt-Template darf allein nutzbar sein. **Endgültige Gesamtfreigabe** des Zwei-Repo-Systems erst nach späterem Integrationstest.
- **Rückfall:** fehlerhaften Kandidaten nicht als stabile Version deklarieren; neues Repo bleibt reversibel.

### Schritt 3 – Eigenes Generator-Repository aus dem neuen Template erstellen

- **Voraussetzungen:** Gate C und eindeutiger Haupt-Template-Stand.
- **Arbeiten:** **neues** Generator-Repo aus dem freigegebenen Haupt-Template initialisieren, dabei dieselben Arbeitsregeln, Spec-/Review-Prozesse und Handoff übernehmen. Zwecks Bootstrap **keinen Generator für den Generator verlangen**. Anschließend Generator-spezifisches `DV_KONZEPT`, README, `GENERATOR_CONTRACT`, CI, Versionsquelle und Tests ergänzen.
- **Ergebnis:** separates, zunächst funktionsarm startfähiges Generator-Projekt; Versionsbezug zum Haupt-Template dokumentiert.
- **Gate D:** Bootstrapping und fehlende zyklische Abhängigkeiten prüfen; keine ungefragten Schreibrechte oder Installationen.
- **Rückfall:** neues Repo unabhängig; das ursprüngliche `template-spec-kit` bleibt unverändert.

### Schritt 4 – Alte Generatorfunktionen gezielt übertragen und freigeben

- **Voraussetzungen:** freigegebene Funktion-für-Funktion-Matrix aus Schritt 0.
- **Arbeiten:** alte Generatorlogik und benötigte Profile **selektiv** in das Generator-Repo übernehmen; Python-CLI mit Modulen/`project.yaml`, **Vorschau mit Diffs → Freigabe → Backup → Apply → Tests → kontrollierter Rückfall**, Version-Pin, Konfliktvermeidung und Fehlercodes implementieren. **V1-Module:** Python, Java, TypeScript, Docker/Compose, PostgreSQL, GitHub Actions, React, PixiJS, Prometheus/Grafana; Colyseus/Keycloak nur als bewusst gewählte Ergänzungen. Bestehende Profile nur soweit vorgesehen und geprüft übernehmen. Eingesparte/entfallene Funktionen samt Begründung dokumentieren.
- **Ergebnis:** CI-geprüfter **Python-CLI-Generator** mit modularen optionalen Profilen, **zwei Modi** (neu / bestehend), sicherem Preview/Backup/Rollback, **eigenem stabilem, ausdrücklich freigegebenem SemVer-Release** und Kompatibilitätsdokument.
- **Gate E:** relevante Legacy-Regressionen bestanden und keine versehentlichen Überschreibungen; Generator unabhängig ausführbar.
- **Rückfall:** auf vorherigen Generator-Tag wechseln; alte Quelle lesend erhalten.

### Schritt 5 – Beide Repositories verbinden und integriert testen

- **Arbeiten:** im Haupt-Template **nur Verweis/Schnittstellenbeschreibung**, keine Generator-Quelldateien, aufnehmen; Generatorversion auf freigegebenen Tag/Commit fixieren; sicheren Abruf/Aufruf, Offline-Fall, Compatibility-Check und Statusmeldung prüfen.
- **Ergebnis:** vollständiger Praxistest `neues Projekt → Idee → Specs → Architekturfreigabe → Generator-Dry-run → Scaffolding → Tests → Handoff` inkl. Fehler- und Rückfallfall.
- **Gate F:** **Gesamtsystem nur freigeben, wenn Pflichtprüfungen inklusive realem temporärem Testprojekt bestanden sind.** Agentenunterschiede transparent ausweisen.
- **Rückfall:** Generator-Aufruf deaktivieren oder freigegebenes älteres Release pinnen; Template weiterhin neutral nutzbar.

### Schritt 6 – Migrationsablauf für bestehende Projekte prüfen

- **Arbeiten:** kleines Altprojekt inklusive Dokumentation, Code, Bildern, Konfiguration und Tests lesend untersuchen, Strategie A (neues Repo mit selektivem Import) gegen B (In-place-Update) nach Umfang, Risiko und KI-/Tokenaufwand vergleichen. Plan als Vorschlag vorlegen, erst nach Freigabe ausführen und Tests wiederholen.
- **Gate G:** **Beide Generator-Modi und beide SDD-Optionen** im realistischen Vergleich getestet; Altprojekt bleibt erhalten; Übernahmebericht, Inventur und Vergleich zeigen, ob benötigte Funktionen vollständig abgedeckt sind.

### Schritt 7 – Release- und Übergabedokumentation abschließen

- **Arbeiten:** Versionen/Kompatibilität, Changelogs, Checklisten, Testnachweise, offene Punkte, **deutsche Quickstarts für VS Code, Codespaces, Copilot/Copilot CLI, Codex, Terminal/CLI, Setup/Check/Status und SDD-Auswahl**, Besonderheiten je OpenCode/Kimi/ChatGPT sowie konkrete geprüfte Start-Prompts vervollständigen. Code/technische IDs englisch.
- **Gate H:** keine unerledigten Release-Blocker; dokumentierte Grenzen tatsächlich geprüfter Agenten und Umgebungen.

### Schritt 8 – Abschluss der Namens- und Release-Dokumentation

- **Bereits vor Schritt 1 beschlossen:** Die beiden Namen sind `t0003-ai-project-template` und `t0004-ai-project-generator`; Technologie-Präfix, vierstellige IDs und Bindestrich entsprechen der vereinbarten Notation.
- **Technischer Nachweis vor Repo-Erstellung:** die Nummern `t0003`/`t0004` und die GitHub-Namen müssen in den maßgeblichen Bestandslisten frei sein. Bei Kollision den Konflikt dem Nutzer vorlegen, keine automatische Umnummerierung.
- Abschließend die tatsächlich angelegten Repositories, Metadaten, Git-Remotes, Links und Dokumentation konsistent verifizieren; keine stillen Umbenennungen. Das alte `template-spec-kit` bleibt als Referenz erhalten.
- **Gate:** Freigabe- und Testnachweise vollständig dokumentiert; die bereits bestätigte Namenswahl nicht erneut als offene Architekturentscheidung behandeln.

**Gate-Regel:** Reine Statusmeldungen blockieren nicht. Jede ausdrückliche Freigabe gilt nur für die konkret vorgelegte Etappe, nicht pauschal für unbekannte künftige Repo-Mutationen, Kosten, Berechtigungen oder destruktive Aktionen.

---

## 12. Maßnahmenkatalog: bestehende Mechanismen

| Mechanismus | Zielaktion | Konkret |
|---|---|---|
| GitHub Use this template / heutige Zweistufigkeit | **VEREINFACHEN** | Direkt nutzbarer neutraler Root statt Pflichtgenerator |
| Python-Generator und Profilwissen | **SELEKTIV INS NEUE GENERATOR-REPO** | Nach inventarisierter, freigegebener Übernahme mit Regressionstests; altes Repo unverändert |
| Sicherung vor Überschreiben von Dateien | **BEHALTEN** | In optionalem Scaffolding und Migration weiter nutzen |
| `AGENTS.md` | **BEHALTEN / AKTUALISIEREN** | Einzige kanonische allgemeine Regeln |
| Doppelte Copilot-Regeln / starre Modellvorgaben | **VEREINFACHEN** | Dünne Verweise statt redundanter Vorgaben |
| Specify-Pins, ps/sh/Python-Wrapper | **BEHALTEN, als wählbare Option** | Reproduzierbar, Windows sicher |
| Specify im gewählten Devcontainer | **BEHALTEN, nur bei SDD-Wahl Spec Kit** | Automatisch im bewusst gewählten Container |
| Ungefragter Copilot-Installer in postCreate | **ENTFERNEN** | Keine automatische Agenteninstallation |
| Agent-Login/-Start | **BEHALTEN: bewusst** | Nur nach Benutzerwahl |
| Devcontainer, Compose und Projekttechnologie | **OPTIONAL MACHEN** | Nur nach Nutzen und Architekturentscheid |
| Analyze-/Review-Gates | **BEHALTEN** | Menschliche Freigaben, nicht OS-Rechte |
| Handoff-Skill im Arbeitsbaum | **VERVOLLSTÄNDIGEN** | Prüfen und in gemeinsamen Handoff integrieren |
| `docs/PROJECT_HANDOFF.md` | **NEU ERGÄNZEN** | Gemeinsamer wechselbarer Projektkontext |
| ChatGPT-Export/Rückimport | **NEU ERGÄNZEN** | Auf Anfrage exportieren; Rückimport analysieren/freigeben |
| Herkunft und Release-Version | **NEU ERGÄNZEN** | In vorhandener Konfiguration, keine doppelte Wahrheit |
| Updateprüfung | **NEU ERGÄNZEN** | Sitzungsstart, nichtblockierend, keine Selbstübernahme |
| Altprojektmigration | **NEU ERGÄNZEN** | Vergleich A/B, Freigabe, selektive Übernahme |
| GitHub Actions | **IN BEIDEN REPOS EINRICHTEN** | Template-Copy/Praxistest; Generator-Regressionen, Spec Kit UND OpenSpec, PostCreate und Sicherheit |
| Owner-gebundene Zusatzrechte und Ziele | **VERSCHIEBEN / VEREINFACHEN** | Nur projektspezifisches Opt-in; nach Rechtefreigabe |
| Status-Task/Autostart | **VEREINFACHEN** | Agentenverhalten, keine unnötige Pflicht-Automation |

---

## 13. Abnahmebedingungen für das Gesamtprojekt

Der Aufbau des **neuen Zwei-Repository-Systems** gilt **erst dann** als abgeschlossen, wenn:

- [ ] das bisherige `template-spec-kit` lesend analysiert und **nicht** zum Umbauziel wurde;
- [ ] für alle relevanten Alt-Funktionen eine **evidenzbasierte Inventur** und freigegebene Zuordnung `übernehmen / anpassen / Generator / nicht übernehmen` existiert;
- [ ] zwei **neue**, getrennte Repositories mit dokumentierter Herkunft existieren und der Generator auf Basis des freigegebenen Haupt-Templates initialisiert wurde, **ohne Selbst-Generator-Abhängigkeit**;
- [ ] ein Benutzer durch **Use this template** direkt ein neutrales, brauchbares Repository erhält;
- [ ] kein Generator vor der ersten Anforderungs-/Spec-Diskussion laufen muss;
- [ ] `AGENTS.md` die kanonischen Regeln enthält und Agentenadapter sie nicht duplizieren;
- [ ] **Spec Kit und OpenSpec** ab V1 separat nutzbar und tatsächlich getestet sind, inkl. sicherem Specify/Windows-Bootstrap;
- [ ] eine gewählte Devcontainer-Umgebung **das ausgewählte SDD-Werkzeug** bereitstellt, **aber** Codex/Copilot/sonstige Agenten nicht ungefragt installiert;
- [ ] Architekturfreigaben, technische Permissions und Routineautonomie unterschieden und nachvollziehbar sind;
- [ ] gemeinsame Übergaben nach relevanten Schritten gepflegt und beim Agentenwechsel wirksam eingelesen werden (pro getesteter Umgebung nachgewiesen);
- [ ] ein ausführlicher Markdown-Export angefordert werden kann und externe Ergebnisse erst nach Abgleich und Freigabe verbindlich werden;
- [ ] jedes Projekt seine echte Template-Herkunft/version kennt und beim Sitzungseinstieg veröffentlichte Neuerungen erkennen **kann**, soweit Zugriff vorhanden ist;
- [ ] kein Template-Update ohne Freigabe in ein bestehendes Projekt eingespielt wird;
- [ ] eine KI in einem neuen Repo ein altes Repo zunächst read-only analysieren und einen A-/B-Migrationsplan vorlegen kann;
- [ ] Generator und Template **getrennt** versioniert sind; ein Projekt nur eine stabile ausdrücklich freigegebene Generator-Version benutzt, neuere Versionen nicht ungefragt einspielt;
- [ ] GitHub Actions in **beiden** neuen Repositories bei relevanten Änderungen die verpflichtenden Tests ausführen und Fehler sichtbar machen;
- [ ] **vor Freigabe ein reales temporäres Testprojekt** den neutralen Start und – nach Integration – den freigegebenen Generator erfolgreich durchlaufen hat;
- [ ] kein normal erzeugtes Repo fremde ownerbezogene Schreibrechte, Geheimnisse oder unnötige Runtime-/Generator-Interna erbt;
- [ ] jede übernommene Alt-Funktion gegen Inventar und Tests nachweisbar abgedeckt oder ihr Wegfall ausdrücklich genehmigt ist;
- [ ] der chronologische Ablauf mit allen Gates und Rückfallwegen dokumentiert ist;
- [ ] die bereits festgelegten IDs `t0003`/`t0004` vor der GitHub-Erstellung gegen die maßgebliche Technologie-ID-Liste und die GitHub-Repo-Namen geprüft wurden und keine Kollision vorliegt;
- [ ] beide Repos **privat**, im selben vom Nutzer gewählten GitHub-Konto, angelegt sind; keine öffentliche Lizenz/Veröffentlichung vorausgesetzt wird;
- [ ] Generator als **Python-CLI** auf Windows, Linux und Codespaces getestet ist; macOS ist nicht erforderlich;
- [ ] Generator-Module nach genehmigtem `config/project.yaml` angeboten und nur bei Bedarf eingerichtet werden;
- [ ] Generator **Neuaufbau** und **Bestandsmigration** mit konkreten Vorschlägen, Dry-run, Freigabe, Diffs, Sicherung, sicheren Rollback und Fehlerprüfungen beherrscht;
- [ ] **vier Release-Praxistests** (Neu/Bestand × Spec Kit/OpenSpec) bestanden sind, plus wesentliche Modul-Smoke-Tests und Sicherheitsnegativfälle;
- [ ] jeder Startpunkt eine **deutsche, getestete Quickstart-Doku** enthält und Changelog/SemVer/Herkunft nicht widersprüchlich sind;
- [ ] der Agent beim Start nach dem **alten Repo-Link fragt**, wenn nicht angegeben, ohne Quellzugriff zu erfinden;
- [ ] das Ergebnis mit realen Testnachweisen, verbleibenden Einschränkungen, Versionsstand und nächstem Schritt dokumentiert ist.

**Kein Erfolgskriterium wird durch bloße Dokumentation als erfüllt markiert, wenn es eine technische Funktion voraussetzt.** Wo ein bestimmter Agent, eine Plattform oder ein Cloud-Szenario nicht getestet werden konnte, muss der Releasebericht das ausdrücklich sagen.

---

## 14. Direkt verwendbarer Startauftrag für Codex, Copilot oder andere Coding-Agenten

> **Auftrag: Neues, neutrales KI-Projekt-Template und separaten Generator nach freigegebener Inventur aufbauen.** Das bisherige `template-spec-kit` ist eine **read-only-Quelle** und darf weder modernisiert noch überschrieben oder gelöscht werden. Arbeite anhand dieser Implementierungsvorgabe und bestätigter Entscheidungen; fasse noch nicht implementierte Dinge nicht als vorhanden auf.
>
> **Startfrage:** Frage mich vor der Alt-Repo-Analyse **nach der GitHub-URL oder dem lesbaren lokalen Pfad** zu meinem bisherigen `template-spec-kit`; ich trage sie erst dann ein. Ich habe die zwei neuen privaten Repos selbst angelegt bzw. lege das Generator-Repo erst nach dem freigegebenen Haupt-Template an. **Zuerst nur Analyse:** Erfasse dann Git-Stand, Funktionen, Profile, Tests, Dokumentation, Handoff und Konfigurationen möglichst skriptgestützt. Ordne jede relevante Funktion `direkt übernehmen / anpassen / in separates Generator-Repo auslagern / nicht übernehmen` zu, jeweils mit Quellpfad, Testergebnis, Begründung, Risiko und grobem Aufwand. Erstelle die vollständige Entscheidungs- und Übernahmematrix, **ohne Quelldateien oder Repositories zu verändern**. Hole Freigabe für den Plan ein.
>
> **Dann etappenweise:** Unterstütze **Spec Kit und OpenSpec ab Release 1**, ohne eine Pflichtwahl vorzuschreiben. Errichte nach Freigabe ein **neues** technologieneutrales Haupt-Template `t0003-ai-project-template`, teste dessen echte Template-Kopie und gib einen nutzbaren Stand frei. Erstelle **danach** ein neues Generator-Repository **aus genau diesem Template-Stand** namens `t0004-ai-project-generator`, ohne zyklischen Generator-Bootstrap. Übertrage nur die freigegebenen Alt-Generatorfunktionen, implementiere eine dokumentierte sichere Schnittstelle (inkl. Dry-run, stabiler freigegebener Version, Konflikt-/Rollback-Regel) und sichere sie mit Regressionstests ab.
>
> **Generator-Anforderungen:** Python-CLI auf Windows, Linux und Codespaces; lokale, freigegebene Versionsinstallation; SemVer und `project.yaml`; modulare optionale Profile für Python, Java, TypeScript, Docker, PostgreSQL, Actions, React, PixiJS und Prometheus/Grafana sowie bedarfsabhängig Colyseus/Keycloak. Zwei Modi: neues Projekt und Bestandsübernahme; verpflichtende Vorschau/Diffs/Freigabe/Backup/Tests/rollback-sichere Behandlung. **Integration:** Führe beide Repositories über versionierte Schnittstellen zusammen, nicht durch Mitkopieren des Generatorquellcodes in gewöhnliche Projekte. Prüfe reale Agentenstarts, `AGENTS.md`/Handoff, den Ideen-zuerst-Ablauf, Architektur-Gates, Version- und Updateprüfung sowie ein temporäres Ende-zu-Ende-Testprojekt. GitHub Actions und Praxistest sind Release-Pflicht; bei Fehlern keine Freigabe.
>
> **Risikoregel:** Bei zusätzlichen Berechtigungen, Kosten, fremden Konten, Deployment, destruktiven Änderungen, neuen wesentlichen Architekturentscheidungen oder Veröffentlichungen jeweils vorab die nötige Zustimmung einholen. Routinetests und genehmigte Arbeit dürfen ohne unnötige Bestätigung weiterlaufen. Berichte kompakt `Status | Arbeitsschritt | Kurzbeschreibung`, mit nächstem Schritt, Blockern und Freigabebedarf.
>
> **Abnahme und Handbuch:** Vier Praxisszenarien (Neuaufbau/Migration mit Spec Kit und OpenSpec), realistische Konflikt- und Rollback-Tests sowie deutsche Quickstarts (VS Code/Codespaces, Terminal, Copilot/Codex, Setup/Check/Status, SDD-Wahl); erst dann Release. **Namensregel:** Verwende die vom Nutzer festgelegten Namen `t0003-ai-project-template` und `t0004-ai-project-generator`. **Vor** der GitHub-Erstellung sicherstellen, dass beide IDs und Repo-Namen im relevanten Bestand frei sind; bei Kollision Entscheidung anfordern. Abschließend Inventur-Abdeckung, Tests, bekannte Lücken und nächste Schritte dokumentieren.


---

## 15. Operative Arbeitspakete – fortlaufende Umsetzung nach Freigabe

Die Phasen aus Abschnitt 11 sind verbindlich. Diese Arbeitspakete dienen als **prüfbare Aufgabenliste**, nicht als Erlaubnis, Freigabepunkte zu überspringen:

| Paket | Repository | Ergebnis | Abnahme |
|---|---|---|---|
| AP-00 – Quelle lesen | neues Template / altes Repo read-only | Repo-URL abgefragt, Inventar, Teststatus, Übernahmematrix | Nutzer genehmigt Funktionszuordnung |
| AP-01 – neutraler Kern | `t0003-ai-project-template` | schlanke Copy, `AGENTS.md`, DV-Konzept, Handoff, Konfiguration | echte Template-Kopie ohne Generator nutzbar |
| AP-02 – SDD-Adapter | Haupt-Template | Spec Kit und OpenSpec wählbar und startbar | beide separat unter Zielumgebungen getestet |
| AP-03 – KI/Quickstarts | Haupt-Template | kurze deutsche Starts und Anweisungen für CLI, VS Code, Codespaces, Copilot, Codex, andere Agenten | nur nachgewiesene Pfade, Testprotokoll |
| AP-04 – Template-Checks | Haupt-Template | GitHub Actions, Updatecheck, Handoff-Export/-Import, CI und Release-Vorschau | Gates & Praxisbeispiel grün |
| AP-05 – Generator-Repo | `t0004-ai-project-generator` | private Kopie des freigegebenen Haupt-Templates, Generator-Konzept, Python-Projekt | keine zirkuläre Abhängigkeit |
| AP-06 – Module | Generator | Kern und bedarfsbezogene V1-Module; `project.yaml` als Eingabe | optionale Auswahl, reproduzierbares Profil |
| AP-07 – CLI-Sicherheit | Generator | `plan`/Dry-run, Diffs, Bestätigung, Snapshot, `apply`, Check, sicherer Rollback | bestehende Datei wird nie ungefragt überschrieben |
| AP-08 – zwei Modi | Generator | Neubau und Altprojektübernahme mit konkreten Vorschlägen | Alt-Repo unverändert bis Freigabe |
| AP-09 – Release/Integration | beide | getrennte SemVer-Releases, gepinnte Installation, Compatibility-Check | kein `latest`/Auto-Upgrade |
| AP-10 – Praxistest | beide / temporäre Repos | 2 Modi × 2 SDD-Werkzeuge plus Konflikt-/Rollback-Negativtests | alle Pflichtfälle erfolgreich |
| AP-11 – Übergabe | beide | aktualisierte MDs, Changelogs, Status, offene Punkte, Releasenachweis | Review-Freigabe |

### Erwartete `config/project.yaml`-Struktur (Entwurf, nach Audit konkretisieren)

Die Datei soll **kein** vorab festgelegtes Java-, Python- oder Docker-Projekt erzwingen. Nach der jeweils freigegebenen Auswahl können z. B. folgende **illustrative** Werte erscheinen; der implementierende Agent muss das konkrete Schema dokumentieren und validieren:

```yaml
project:
  name: "example-project"
template:
  source: "<realer-Repo-URL>"
  version: "<tatsaechlich-uebernommener-Release>"
  base_commit: "<tatsaechlicher-Commit>"
sdd:
  tool: "spec-kit"  # oder "openspec"; vor Auswahl null
  version: "<freigegebene-Version>"
generator:
  version: "<freigegebener-Release-oder-null>"
  mode: "new"       # oder "migrate"; nur nach Freigabe
modules:
  selected: []       # z.B. [python, docker, postgres] nach Freigabe
```

Keine Fantasiewerte als reale Versionen committen. Werks- und Projektmetadaten dürfen nicht unbeabsichtigt gegeneinander laufen. Im **frischen** Template bleiben Auswahlfelder zunächst ungesetzt/neutral.

### Konzeptioneller Generator-CLI-Vertrag (Syntax festzulegen und zu testen)

Die **Funktionen** sind verbindlich, nicht diese beispielhaften Subcommand-Namen:

- `version`: tatsächlich installierte stabile CLI-Version und Toolkompatibilität anzeigen.
- `check`: Repo-Voraussetzungen, `project.yaml`, verfügbare Module/SDD-Integration, Rechte, Tools und Konfigurationskonflikte prüfen.
- `plan`: Projektkonfiguration + ggf. read-only Alt-Repo analysieren, konkrete Änderungen/Module/Diffs/Tests ausgeben; **keine Mutationen**.
- `apply`: genehmigten Plan (möglichst anhand Plan-ID/Hash und unveränderter Ausgangsbasis) nach Snapshot durchführen. Bei veränderter Basis erneut planen/freigeben.
- `verify`: generierte Lösung prüfen, Testnachweise protokollieren.
- `restore`: kontrollierte Rücknahme **nur der vom Generator verursachten Änderungen**, mit Prüfung anderer Arbeitsänderungen. Bei unsicherem Zustand stattdessen manuelle Wiederherstellungsoptionen anzeigen.

Wichtige Besonderheit: Ein Coding-Agent darf `apply` **nicht** als Ersatz für die benutzerspezifische Freigabe aufrufen. Automatisierung und technisches Tool-Permissions-Modell bleiben getrennt.

### Projektübernahme – zwei unterschiedliche Wege

**A: Neubeginn und selektiver Import (für Lands of Glory bevorzugt).** In einem frischen Repo aus `t0003` werden die bestätigten Spielregeln, Spezifikationen, Daten/Assets und relevanter Anwendungscode **einzeln bewertet**. Im Fall von Lands of Glory wird **Spec Kit** gewählt, zunächst der fachliche Stand übernommen und erst dann über Architektur/Implementierung entschieden. Kein ungeprüfter Import alter Generator-/Docker-/KI-Konfigurationen.

**B: Bestand aktualisieren (für etablierte Projekte).** Der Agent analysiert das laufende Repo, vorhandene Änderungen, Template-Abweichungen und Tests. Es folgt ein Plan in eigenem Branch mit Sicherungen, Konfliktliste, Tests und Rückfall. Ein echter Upgrade wird nur nach Freigabe durchgeführt. Weder Benutzer-Datenbanken noch produktive Deployments werden ohne zusätzliche Autorisierung angefasst.

**Keine großen KI-Leseoperationen ohne Not:** Liste zuerst Pfade, Git-Status, Versionsdateien und Testberichte maschinell auf. Lese fachlich bedeutende, konfliktträchtige oder unsichere Dateien dann gezielt. Zusammenhängende Dokumente nur im für die konkrete Entscheidung nötigen Umfang verarbeiten. Jede wegzulassende relevante Funktion muss begründet und bestätigt sein.

### Quickstart – verpflichtender Dokumentationsinhalt

Die Nutzer-Doku jedes neu erzeugten Projekts muss folgende **kurze, konkret geprüfte** Antworten enthalten:

1. **Wo starte ich?** Lokales Windows/VS Code, Linux-Terminal oder GitHub Codespaces.
2. **Wie starte ich Copilot/Copilot CLI oder Codex?** Tatsächlich unterstützter Startweg, Voraussetzungen und nötiger Login; keine behauptete automatische Anmeldung.
3. **Wie wähle/öffne ich Spec Kit oder OpenSpec?** Unterschiede und getestete Bedienung je Client, inklusive eines kleinen ersten Spec-Beispiels.
4. **Was tun Setup, Check und Status?** Einheitliche Arbeitsaufträge bzw. geprüfte Befehle mit kurzer Erklärung.
5. **Wie setze ich eine Sitzung fort?** `AGENTS.md` und `docs/PROJECT_HANDOFF.md` lesen, Git-Synchronisierung prüfen; nur bei Bedarf ausführlichen MD-Export erstellen.
6. **Wie aktiviere ich Module?** Architekturempfehlung → Freigabe → `project.yaml` → Generator-Dry-run → Freigabe → Setup → Tests.
7. **Wie update oder migriere ich?** Nur Vorschlag und Kompatibilitäts-/Konfliktprüfung, keine automatische Dateiübernahme.

**Hinweis:** Nicht getestete Kommandos nicht als ausführbar darstellen. Agenten können abweichende native Trigger benötigen, selbst wenn gemeinsame Markdown-Anweisungen existieren.

### Abschlussnachweis des Coding-Agenten

Die finale Übergabe enthält mindestens die Tabelle `Status | Arbeitsschritt | Kurzbeschreibung` und danach: tatsächliche GitHub-URLs, Release-Tags/Commits, geprüfte Plattformen und Agenten, vier Praxistest-Ergebnisse, abgesicherte alte Funktionen und bekannte Lücken, aktueller Handoff, nächste Schritte und konkrete vom Nutzer noch benötigte Freigaben. Keine fiktiven Erfolgsmeldungen.

---

### Geltungsgrenze

Dieses Dokument ist eine **aktualisierte fachlich-technische Arbeitsvorgabe** auf Basis des früheren Entwurfs und der nachfolgenden Beschlüsse, **nicht** ein verifizierter Datei-für-Datei-Patch. Die tatsächliche Repo-Struktur, existierende Tests und gegebenenfalls nachfolgende Entscheidungen haben Vorrang vor Annahmen aus der Bestandsaufnahme. Technische Umsetzung, CI-Läufe, reale Agenten-/Codespaces-Tests und Änderungen am GitHub-Repository stehen noch aus.
