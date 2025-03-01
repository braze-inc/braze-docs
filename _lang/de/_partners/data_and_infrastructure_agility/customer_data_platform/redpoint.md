---
nav_title: Redpoint
article_title: Redpoint 
description: "Die Redpoint to Braze-Integration ermöglicht es Ihnen, Braze-Benutzerprofile mit Ihren Erstanbieterdaten zu ergänzen und anzureichern."
alias: /partners/redpoint/
page_type: partner
search_tag: Redpoint
---

# Redpoint

> [Redpoint][2] ist eine Technologieplattform, die Vermarktern eine vollständig integrierte Plattform für die Orchestrierung von Kampagnen bietet. Nutzen Sie die Segmentierungs-, Planungs- und Automatisierungsfunktionen von Redpoint, um zu steuern, wie und wann CDP-Daten in Braze importiert werden.

Die Integration von Braze und Redpoint ermöglicht es Ihnen, Braze-Segmente auf der Grundlage Ihrer Redpoint CDP-Daten zu erstellen. Redpoint bietet zwei Modi für die Übermittlung von Daten an Braze: 

1. **Braze Onboarding und Upsert-Modus**: "Upserts" ein Benutzerprofil von Redpoint in Braze. Dies ist für das Onboarding oder die Aktualisierung von Benutzerdatensätzen gedacht, wenn sich Daten geändert haben. 
2. **Braze Append** Modus: Aktualisiert ein Benutzerprofil, wenn dieser Benutzer bereits in Braze existiert. 

Sie werden für jeden Modus eine Exportvorlage und einen Ausgangskanal konfigurieren.

{% alert note %}
"Upsert" ist eine Kombination aus den Wörtern "Update" und "Insert". Sie wird verwendet, wenn Sie einen neuen Datensatz in eine Datenbanktabelle einfügen möchten, wenn er noch nicht existiert, oder den Datensatz aktualisieren möchten, wenn er bereits existiert. Im Wesentlichen prüft upsert, ob ein bestimmter Datensatz in der Datenbank vorhanden ist. Wenn der Datensatz vorhanden ist, wird er aktualisiert, und wenn er nicht vorhanden ist, wird ein neuer Datensatz eingefügt.
{% endalert %}

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br>Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | [Ihre REST-Endpunkt-URL][1]. Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
| Redpoint Data Management Artefakte | Die Integration von Braze wird durch eine Reihe von Redpoint Data Management-Artefakten unterstützt. Kontaktieren Sie den [Redpoint Support][3], um die Artefakte für Ihre Version von Redpoint Data Management anzufordern. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, können Sie einen API-Schlüssel unter **Entwicklerkonsole** > **API-Einstellungen** erstellen.
{% endalert %}

## Redpoint CDP benutzerdefinierte Attribute

Die folgenden benutzerdefinierten Redpoint-Attribute können zu einem Braze-Benutzerprofil hinzugefügt werden.

| Feld               | Beschreibung                                                                                                       |
| ------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `rpi_cdp_attributes` | Das Redpoint CDP-Profil-Attributobjekt                                                                                  |
| `rpi_audience_outputs`| Array von Zielgruppen-Ausgabe-Tags, auf die der Benutzer in einer Redpoint Outbound Delivery Braze-Kanalausführung abzielt         |
| `rpi_offers`         | Array von Angebots-Tags, auf die der Benutzer in einer Redpoint Outbound Delivery Braze-Kanalausführung abzielt                   |
| `rpi_contact_ids`    | Array von Kontakt-IDs aus der Angebotshistorie, auf die der Benutzer in einer Redpoint Outbound Delivery Braze-Kanalausführung abzielt     |
| `rpi_channel_exec_ids`| Array von Kanalausführungs-IDs, auf die der Benutzer in einer Redpoint Outbound Delivery Braze-Kanalausführung ausgerichtet ist       |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![][4]{: style="max-width:75%;"}

## Integration

### Schritt 1: Vorlagen einrichten

#### Schritt 1a: Erstellen Sie die Vorlage Braze Onboarding und Upsert

Erstellen Sie in Redpoint Interaction (RPI) eine neue Exportvorlage und nennen Sie sie **Braze Onboarding and Upsert**. Diese Vorlage definiert die wichtigsten Zuordnungen zwischen dem Redpoint CDP und dem Braze-Benutzerprofil sowie alle zusätzlichen benutzerdefinierten Attribute, die Sie Ihren Benutzerprofilen in Braze hinzufügen möchten.

Ziehen Sie Redpoint CDP-Attribute in die Spalte **Attribut**. Setzen Sie jeden **Kopfzeilenwert** auf das entsprechende Braze [Benutzerattribut][17]. 

In der folgenden Tabelle sind die Redpoint CDP-Attribute und die entsprechenden Braze-Attribute aufgeführt:

| Rotpunkt-Attribut | Kopfzeile Wert |
|--------------------|------------------|
| PID                | `external_id`    |
| Erster Name          | `first_name`     |
| Nachname          | `last_name`      |
| Primäre E-Mail      | `email`          |
| Primäres Land    | `country`        |
| DOB                | `dob`            |
| Geschlecht             | `gender`         |
| Primäre Stadt       | `home_city`      |
| Primäres Telefon      | `phone`          |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Fügen Sie das Attribut **Output Name** aus der Tabelle **Angebotsverlauf** hinzu. Zum Schluss fügen Sie alle zusätzlichen benutzerdefinierten Redpoint-Attribute hinzu, die Sie in Braze einbinden möchten. Nachfolgend finden Sie beispielsweise eine Vorlage für das Onboarding und Upsert mit Bildung, Einkommen und Familienstand als zusätzliche Attribute.

![][7]{: style="max-width:75%;"}

#### Schritt 1b: Erstellen Sie die Vorlage Braze Append

Erstellen Sie eine zweite Exportvorlage für reine Anhängevorgänge mit dem Namen **Braze Append**.

Sie werden nur zwei Attribute für diese Vorlage festlegen. Legen Sie für **PID** den **Wert für die Kopfzeile** auf `external_id` fest. Legen Sie für **Output Name** die **Kopfzeile** als `output_name` fest.

![Eine Beispiel-Exportvorlage mit den Attributen `external_id` und Output-Name.][8]{: style="max-width:75%;"}

#### Schritt 1c: Datumsformat einstellen

Wechseln Sie für beide Exportvorlagen auf die Registerkarte **Optionen** und setzen Sie das **Datumsformat** auf den Wert **Benutzerdefiniertes Format**. Legen Sie das Format als **jjjj-MM-tt** fest.

![Auf der Registerkarte Optionen ist das Datumsformat auf jjjj-MM-tt eingestellt.][16]{: style="max-width:75%;"}

### Schritt 2: Ausgehende Kanäle erstellen

Erstellen Sie im RPI zwei neue Kanäle. Stellen Sie beide Kanäle auf **Auslieferung** ein. Nennen Sie einen Kanal **Braze Onboarding und Upsert** und den anderen **Braze Append**.

![][9]{: style="max-width:75%;"}

{% alert note %}
Prüfen Sie nach dem ersten Onboarding Ihrer CDP-Datensätze in Braze, ob nachfolgende Redpoint Interaction-Workflows, die den Braze Onboarding- und Upsert-Channel verwenden, so konzipiert sind, dass sie nur Datensätze auswählen, die seit der ersten Onboarding-Synchronisierung geändert wurden.
{% endalert %}

### Schritt 3: Konfigurieren Sie die Kanäle

#### Schritt 3a: Vorlage und Exportpfadformat festlegen

Navigieren Sie zur Registerkarte **Allgemein** im Bildschirm **Konfiguration der** Kanäle. Legen Sie die Exportvorlage für den jeweiligen Kanal fest. 

Als nächstes definieren Sie für beide Kanäle ein **Exportpfadformat**, das auf ein gemeinsames Netzwerk, ein Dateiübertragungsprotokoll oder einen externen Inhaltsanbieter verweist, auf den sowohl Redpoint Interaction als auch Redpoint Data Management zugreifen können. 

![][10]{: style="max-width:75%;"}

Das Format des Exportverzeichnisses ist auf beiden Kanälen identisch und sollte mit `\\[Channel]\\[Offer]\\[Workflow ID]` enden.

![][11]{: style="max-width:50%;"}

#### Schritt 3b: Konfigurieren Sie die Ausführung nach der Ausführung

Wechseln Sie im Bildschirm **Konfiguration der** Kanäle auf die Registerkarte **Post Execution**. 

Aktivieren Sie das Kontrollkästchen **Nach der Ausführung**, um eine Service-URL nach der Channel-Ausführung aufzurufen. Geben Sie die URL Ihres Redpoint Data Management Webservice ein. Dieser Eintrag wird sowohl in Ihrem Onboarding- als auch in Ihrem Append-Channel identisch sein.

![][14]{: style="max-width:75%;"}

### Schritt 4: Einrichten von Braze-Komponenten in Redpoint Data Management 

Das Archiv mit den Artefakten von Redpoint Data Management (RPDM) zur Unterstützung der Braze-Integration enthält eine README mit detaillierten Anweisungen zum Einrichten der erforderlichen Komponenten. Beachten Sie die folgenden Details, wenn Sie Ihre Integration konfigurieren. 

#### Schritt 4a: Aktualisieren Sie die RPI-to-Braze-Automatisierung mit Ihrem Braze-REST-Endpunkt und dem Basis-RPI-Ausgabeverzeichnis 

Nachdem Sie die Artefakte von Braze in Redpoint Data Management importiert haben, öffnen Sie die Automatisierung mit dem Namen **AUTO_Process_RPI_to_Braze** und aktualisieren die folgenden beiden Automatisierungsvariablen mit den Werten für Ihre Umgebung:

* **BRAZE_API_URL**: Der Braze REST Endpunkt
* **BASE_OUTPUT_DIRECTORY**: Das gemeinsame Ausgabeverzeichnis von Redpoint Interaction und Redpoint Data Management

![][5]{: style="max-width:40%;"}

#### Schritt 4b: Aktualisieren Sie das Projekt RPI to Braze append 

Das Redpoint Data Management-Projekt mit dem Namen **PROJ_RPI_to_Braze_Append** enthält das Exportschema für Auslieferungsdateien und Mappings für das benutzerdefinierte Attributobjekt `rpi_cdp_attributes` in Braze. 

Aktualisieren Sie das Dateieingabeschema und das Document Injector Tool namens **RPI auf Braze Document Injector** mit allen zusätzlichen benutzerdefinierten CDP-Attributen, die in Ihrer Exportdateivorlage definiert sind. Dieses Beispiel zeigt die zusätzliche Zuordnung von Bildung, Einkommen und Familienstand:

![][6]{: style="max-width:40%;"}

## Verwendung der Integration

Der Braze-Kanal für Auslieferungen kann jetzt in Redpoint Interaction-Workflows genutzt werden. Befolgen Sie die Standardverfahren zur Erstellung von Auswahlregeln und Zielgruppen in RPI und zur Erstellung der zugehörigen Workflow-Zeitpläne und Auslöser. 

Um die Synchronisierung einer RPI Audience-Ausgabe mit Braze zu ermöglichen, erstellen Sie ein Auslieferungsangebot und verknüpfen es entweder mit dem **Braze Onboarding und Upsert** oder dem **Braze Append-Kanal**. Dies hängt davon ab, ob Sie neue Datensätze in Braze erstellen oder zusammenführen möchten, oder ob Sie nur Kampagnendaten hinzufügen möchten, wenn der Datensatz bereits in Braze vorhanden ist.

![][13]{: style="max-width:80%;"}

Sobald der Workflow in RPI erfolgreich ausgeführt wurde, können die von RPI bezogenen Orchestrierungs- und CDP-Daten nun zur Erstellung von Segmenten in Braze verwendet werden.

![][12]{: style="max-width:80%;"}

Sie können die mit Redpoint verbundenen Eigenschaften im Benutzerprofil einsehen.

![][15]{: style="max-width:80%;"}

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://www.redpointglobal.com
[3]: https://support.redpointglobal.com/hc/en-us/restricted?return_to=https%3A%2F%2Fsupport.redpointglobal.com%2Fhc%2Fen-us
[4]: {% image_buster /assets/img/redpoint/rpi_to_braze_custom_attributes.png %}
[5]: {% image_buster /assets/img/redpoint/rpi_to_braze_auto_variables.png %}
[6]: {% image_buster /assets/img/redpoint/rpi_to_braze_doc_injector_mappings.png %}
[7]: {% image_buster /assets/img/redpoint/rpi_to_braze_upsert_export_format.png %}
[8]: {% image_buster /assets/img/redpoint/rpi_to_braze_append_export_format.png %}
[9]: {% image_buster /assets/img/redpoint/rpi_to_braze_channel_config_general.png %}
[10]: {% image_buster /assets/img/redpoint/rpi_to_braze_channel_config_specific.png %}
[11]: {% image_buster /assets/img/redpoint/rpi_to_braze_export_directory_setup.png %}
[12]: {% image_buster /assets/img/redpoint/rpi_to_braze_build_braze_segment.png %}
[13]: {% image_buster /assets/img/redpoint/rpi_to_braze_rpi_canvas.png %}
[14]: {% image_buster /assets/img/redpoint/rpi_to_braze_channel_config_post_execution.png %}
[15]: {% image_buster /assets/img/redpoint/rpi_to_braze_record_example.png %}
[16]: {% image_buster /assets/img/redpoint/rpi_to_braze_export_format_config.png %}
[17]: {{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields
