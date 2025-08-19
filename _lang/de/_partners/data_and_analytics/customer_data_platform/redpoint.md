---
nav_title: Redpoint
article_title: Redpoint 
description: "Die Redpoint to Braze Integration erlaubt Ihnen das Onboarding und die Anreicherung von Nutzerprofilen von Braze mit Ihren First-Party-Daten."
alias: /partners/redpoint/
page_type: partner
search_tag: Redpoint
---

# Redpoint

> [Redpoint](https://www.redpointglobal.com) ist eine Technologieplattform, die Marketern eine vollständig integrierte Plattform für die Orchestrierung von Kampagnen bietet. Nutzen Sie die Segmentierungs-, Zeitplanungs- und Automatisierungsfunktionen von Redpoint, um zu steuern, wie und wann CDP-Daten in Braze importiert werden.

_Diese Integration wird von Redpoint gepflegt._

## Über die Integration

Die Integration von Braze und Redpoint erlaubt es Ihnen, Segmente von Braze auf der Grundlage Ihrer Redpoint CDP-Daten zu erstellen. Redpoint bietet zwei Modi für die Übergabe von Daten an Braze: 

1. **Braze Onboarding und Upsert** Modus: "Fügt ein Nutzerprofil von Redpoint nach Braze ein. Diese Funktion ist für das Onboarding oder das Update von Nutzer:innen gedacht, wenn sich Daten geändert haben. 
2. **Braze Append-Modus**: Aktualisiert ein Nutzerprofil, wenn dieser Nutzer:innen bereits in Braze existiert. 

Sie konfigurieren eine Exportvorlage und einen ausgehenden Kanal für jeden Modus.

{% alert note %}
"Upsert" ist eine Kombination aus den Wörtern "Update" und "Insert". Es wird verwendet, wenn Sie einen neuen Datensatz in eine Datenbanktabelle einfügen möchten, wenn er noch nicht existiert, oder den Datensatz aktualisieren möchten, wenn er bereits existiert. Im Wesentlichen prüft upsert, ob ein bestimmter Datensatz in der Datenbank vorhanden ist. Wenn der Datensatz vorhanden ist, wird er aktualisiert, und wenn er nicht vorhanden ist, wird ein neuer Datensatz eingefügt.
{% endalert %}

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br>Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | [Ihre URL für den REST-Endpunkt]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
| Redpoint Daten Management Artefakte | Die Braze Integration wird von einer Reihe von Redpoint Data Management Artefakten unterstützt. Kontaktieren Sie den [Redpoint Support](https://support.redpointglobal.com/hc/en-us/restricted?return_to=https%3A%2F%2Fsupport.redpointglobal.com%2Fhc%2Fen-us), um die Artefakte für Ihre Version von Redpoint Data Management anzufordern. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Redpoint CDP angepasste Attribute

Die folgenden angepassten Attribute von Redpoint können zu einem Nutzerprofil von Braze hinzugefügt werden.

| Feld               | Beschreibung                                                                                                       |
| ------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `rpi_cdp_attributes` | Das Redpoint CDP Profil Attribut Objekt                                                                                  |
| `rpi_audience_outputs`| Array von Tags für die Ausgabe von Zielgruppen, in denen die Nutzer:innen bei der Ausführung eines Redpoint Outbound Delivery Braze-Kanals zusammengestellt sind         |
| `rpi_offers`         | Array von Tags für Angebote, auf die der Nutzer:innen bei der Ausführung eines Redpoint Outbound Delivery Braze Kanals targetiert wird                   |
| `rpi_contact_ids`    | Array von Kontakt-IDs aus dem Verlauf von Angeboten, bei denen der Nutzer:innen in einer Ausführung des Redpoint Outbound Delivery Braze Kanals targeting ist     |
| `rpi_channel_exec_ids`| Array der IDs der Kanalausführungen, bei denen der Nutzer:innen in einer Redpoint Outbound Delivery Braze Kanalausführung targeting ist       |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/redpoint/rpi_to_braze_custom_attributes.png %}){: style="max-width:75%;"}

## Integration

### Schritt 1: Templates einrichten

#### Schritt 1a: Erstellen Sie das Braze Onboarding und Upsert Template

Erstellen Sie in Redpoint Interaction (RPI) eine neue Exportvorlage und nennen Sie sie **Braze Onboarding and Upsert**. Diese Vorlage definiert die wichtigsten Abbildungen zwischen dem Redpoint CDP und dem Braze Benutzerprofil, zusammen mit allen zusätzlichen angepassten Attributen, die Sie Ihren Nutzerprofilen in Braze hinzufügen möchten.

Ziehen Sie Redpoint CDP-Attribute in die Spalte **Attribute**. Setzen Sie den **Wert jeder Kopfzeile** auf das entsprechende Braze [Nutzer:in-Attribut]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields). 

In der folgenden Tabelle sind die CDP-Attribute von Redpoint und die entsprechenden Attribute von Braze aufgeführt:

| Rotpunkt Attribut | Kopfzeile Wert |
|--------------------|------------------|
| PID                | `external_id`    |
| Erster Name          | `first_name`     |
| Nachname          | `last_name`      |
| Primäre E-Mail      | `email`          |
| Primäres Land    | `country`        |
| DOB                | `dob`            |
| Geschlecht             | `gender`         |
| Primärer Ort       | `home_city`      |
| Primäres Telefon      | `phone`          |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Fügen Sie das Attribut **Output Name** aus der Tabelle **Verlauf des Angebots** hinzu. Fügen Sie schließlich alle weiteren angepassten Attribute von Redpoint hinzu, die Sie in Braze einbinden möchten. Im Folgenden sehen Sie beispielsweise ein Template für Onboarding und Upsert mit Bildung, Einkommen und Familienstand als zusätzliche Attribute.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_upsert_export_format.png %}){: style="max-width:75%;"}

#### Schritt 1b: Erstellen Sie das Braze Append Template

Erstellen Sie eine zweite Exportvorlage für reine Append-Operationen namens **Braze Append**.

Sie werden nur zwei Attribute für diese Vorlage festlegen. Legen Sie für **PID** den **Wert für die Kopfzeile** auf `external_id` fest. Legen Sie für **Output Name** die **Kopfzeile** als `output_name` fest.

![Eine Beispiel-Exportvorlage mit den Attributen `external_id` und output name.]({% image_buster /assets/img/redpoint/rpi_to_braze_append_export_format.png %}){: style="max-width:75%;"}

#### Schritt 1c: Datumsformat einstellen

Für beide Export-Templates navigieren Sie zum Tab **Optionen** und setzen das **Datumsformat** auf den Wert von **Benutzerdefiniertes Format**. Legen Sie das Format als **jjjj-MM-tt** fest.

![Auf dem Tab Optionen ist das Datumsformat auf jjjj-MM-tt eingestellt.]({% image_buster /assets/img/redpoint/rpi_to_braze_export_format_config.png %}){: style="max-width:75%;"}

### Schritt 2: Ausgehende Kanäle erstellen

Erstellen Sie im RPI zwei neue Kanäle. Stellen Sie beide Kanäle auf **Auslieferung** ein. Nennen Sie einen Kanal **Braze Onboarding und Upsert**, und den anderen **Braze Append**.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_channel_config_general.png %}){: style="max-width:75%;"}

{% alert note %}
Prüfen Sie nach dem anfänglichen Onboarding Ihrer CDP-Datensätze in Braze, ob nachfolgende Redpoint Interaction-Workflows, die den Braze Onboarding- und Upsert-Kanal verwenden, so konzipiert sind, dass sie nur Datensätze auswählen, die seit der anfänglichen Onboarding-Synchronisierung geändert wurden.
{% endalert %}

### Schritt 3: Konfigurieren Sie die Kanäle

#### Schritt 3a: Template und Exportpfadformat festlegen

Wechseln Sie im Bildschirm **Konfiguration der** Kanäle auf den Tab **Allgemein**. Legen Sie die Exportvorlage für den jeweiligen Kanal fest. 

Als nächstes definieren Sie auf beiden Kanälen ein **Exportpfadformat**, das auf ein gemeinsames Netzwerk, ein Dateiübertragungsprotokoll oder einen Standort eines externen Inhaltsanbieters verweist, der sowohl für Redpoint Interaction als auch für Redpoint Data Management zugänglich ist. 

![]({% image_buster /assets/img/redpoint/rpi_to_braze_channel_config_specific.png %}){: style="max-width:75%;"}

Das Format des Exportverzeichnisses ist auf beiden Kanälen identisch und sollte mit `\\[Channel]\\[Offer]\\[Workflow ID]` enden.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_export_directory_setup.png %}){: style="max-width:50%;"}

#### Schritt 3b: Konfigurieren Sie die Ausführung nach der Ausführung

Wechseln Sie im Bildschirm **Konfiguration der** Kanäle auf den Tab **Post Execution**. 

Markieren Sie das Kontrollkästchen **Nach der Ausführung**, um eine Dienst-URL nach der Ausführung des Kanals aufzurufen. Geben Sie die URL Ihres Redpoint Data Management Webdienstes ein. Dieser Eingang wird sowohl auf Ihrem Onboarding- als auch auf Ihrem Append-Kanal identisch sein.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_channel_config_post_execution.png %}){: style="max-width:75%;"}

### Schritt 4: Einrichten von Braze-Komponenten in Redpoint Data Management 

Das Archiv mit den Artefakten von Redpoint Data Management (RPDM) zur Unterstützung der Braze Integration enthält eine README mit detaillierten Anweisungen zur Einrichtung der erforderlichen Komponenten. Beachten Sie bei der Konfiguration Ihrer Integration die folgenden Details. 

#### Schritt 4a: Aktualisieren Sie die RPI to Braze Automatisierung mit Ihrem Braze REST Endpunkt und dem Basis-RPI-Ausgabeverzeichnis 

Nachdem Sie die Artefakte zu Braze in Redpoint Data Management importiert haben, öffnen Sie die Automatisierung mit dem Namen **AUTO_Process_RPI_to_Braze** und aktualisieren die folgenden beiden Automatisierungsvariablen mit den Werten für Ihre Umgebung:

* **BRAZE_API_URL**: Der Braze REST Endpunkt
* **BASE_OUTPUT_DIRECTORY**: Das gemeinsame Ausgabeverzeichnis von Redpoint Interaction und Redpoint Data Management

![]({% image_buster /assets/img/redpoint/rpi_to_braze_auto_variables.png %}){: style="max-width:40%;"}

#### Schritt 4b: Aktualisieren Sie das RPI to Braze Append Projekt 

Das Redpoint Data Management-Projekt mit dem Namen **PROJ_RPI_to_Braze_Append** enthält das Exportschema für die ausgehende Zustellung und die Abbildungen für das angepasste Attribut-Objekt `rpi_cdp_attributes` in Braze. 

Aktualisieren Sie das Dateieingabeschema und das Document Injector Tool namens **RPI to Braze Document Injector** mit allen zusätzlichen angepassten Attributen, die in Ihrem Template für die Exportdatei definiert sind. Dieses Beispiel zeigt die zusätzliche Abbildung von Bildung, Einkommen und Familienstand:

![]({% image_buster /assets/img/redpoint/rpi_to_braze_doc_injector_mappings.png %}){: style="max-width:40%;"}

## Verwendung der Integration

Der Kanal von Outbound Delivery Braze kann jetzt innerhalb der Redpoint Interaction-Workflows genutzt werden. Befolgen Sie die Standardverfahren zum Erstellen von Auswahlregeln und Zielgruppen in RPI und zum Erstellen der zugehörigen Zeitpläne und Trigger für den Workflow. 

Um die Synchronisierung einer RPI Audience-Ausgabe mit Braze zu ermöglichen, erstellen Sie ein Angebot für die ausgehende Zustellung und verknüpfen es entweder mit dem **Braze Onboarding und Upsert** oder dem **Braze Append-Kanal**. Dies hängt davon ab, ob Sie die Absicht haben, neue Datensätze in Braze zu erstellen oder zusammenzuführen, oder ob Sie nur Daten aus Kampagnen anhängen möchten, wenn der Datensatz bereits in Braze vorhanden ist.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_rpi_canvas.png %}){: style="max-width:80%;"}

Sobald der Workflow in RPI erfolgreich ausgeführt wurde, können die Orchestrierung und die CDP-Daten, die von RPI stammen, nun zur Erstellung von Segmenten in Braze verwendet werden.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_build_braze_segment.png %}){: style="max-width:80%;"}

Sie können die mit Redpoint verbundenen Eigenschaften im Nutzerprofil einsehen.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_record_example.png %}){: style="max-width:80%;"}


