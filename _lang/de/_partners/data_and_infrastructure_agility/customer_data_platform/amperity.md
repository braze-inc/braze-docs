---
nav_title: Amperität
article_title: Amperität
alias: /partners/amperity/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Amperity, einer umfassenden Plattform für Unternehmenskundendaten, die es Ihnen ermöglicht, Amperity-Benutzer zu synchronisieren, Daten zu vereinheitlichen, Daten über AWS S3-Buckets an Braze zu senden und mehr."
page_type: partner
search_tag: Partner

---

# Amperität

> [Amperity](https://amperity.com/) ist eine umfassende Plattform für Unternehmenskundendaten, die Marken dabei hilft, ihre Kunden kennenzulernen, strategische Entscheidungen zu treffen und konsequent die richtigen Maßnahmen zu ergreifen, um ihre Kunden besser zu bedienen. Amperity bietet intelligente Funktionen für die Vereinheitlichung des Datenmanagements, Analysen, Einblicke und Aktivierung.

{% multi_lang_include video.html id="06G0lxaSjgk" align="right" %}

Die Integration von Braze und Amperity bietet eine einheitliche Sicht auf Ihre Kunden über beide Plattformen hinweg. Diese Integration ermöglicht es Ihnen:
- **Kundenprofile synchronisieren**: Übertragen Sie Benutzerdaten und benutzerdefinierte Attribute von Amperity auf Braze. 
- **Erstellen und versenden Sie Zielgruppen**: Erstellen Sie Segmente, die Listen aktiver Kunden und die zugehörigen benutzerdefinierten Attribute an Braze zurückgeben, und senden Sie sie an Braze.
- **Verwalten Sie Datenaktualisierungen**: Steuern Sie die Häufigkeit, mit der Aktualisierungen für benutzerdefinierte Attribute an Braze gesendet werden.
- **Daten vereinheitlichen**: Vereinheitlichen Sie Daten über verschiedene von Amperity unterstützte Plattformen und Braze.
- **Synchronisieren Sie Braze-Daten mit Amazon S3**: Verwenden Sie Braze Currents, um Engagement-Daten aus Braze-Kampagnen zu integrieren. Damit können Sie die Daten im Apache Avro-Format mit Amazon S3 synchronisieren.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Amperity-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Amperity-Konto](https://amperity.com/request-a-demo). |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br> Dieser kann im Braze-Dashboard erstellt werden, indem Sie zu **Entwicklerkonsole** > **Rest-API-Schlüssel** > **Neuen API-Schlüssel erstellen** navigieren. |
| Hartlöt-Instanz | Ihre Braze-Instanz erhalten Sie von Ihrem Braze-Onboarding-Manager oder Sie finden sie auf der [API-Übersichtsseite]({{site.baseurl}}/api/basics#endpoints). |
| Braze REST Endpunkt | Ihre Braze-Endpunkt-URL. Ihr Endpunkt hängt von Ihrer Braze-Instanz ab. |
| Anschluss für Ströme (optional) | Der S3 Currents Anschluss. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Datenzuordnung

Sowohl Standard- als auch benutzerdefinierte Attribute können von Amperity an Braze gesendet werden, so dass Sie Kundenprofile in Braze mit Daten aus verschiedenen Quellen über Amperity anreichern können. Die spezifischen Attribute, die Sie senden können, hängen von den Daten in Ihrem Amperity-System und den Attributen ab, die Sie in Braze eingerichtet haben.

Lesen Sie unten, um mehr über diese Eigenschaften zu erfahren.

### Standard-Attribute 

[Profilattribute]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields) beschreiben, wer Ihre Kunden sind. Sie sind oft mit der Identität des Kunden verbunden, wie z. B.:
- Namen
- Geburtsdaten
- E-Mail-Adressen
- Telefonnummern

### Angepasste Attribute 

[Benutzerdefinierte Attribute]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/) in Braze sind Felder, die von Ihrer Marke bestimmt werden. Wenn Sie möchten, dass Amperity benutzerdefinierte Attribute verwaltet, die bereits in Braze vorhanden sind, passen Sie die von Amperity gesendete Ausgabe an die Namen an, die bereits in Ihrem Braze-Arbeitsbereich vorhanden sind. Dies kann Folgendes beinhalten:
- Kaufhistorien
- Loyalitätsstatus
- Wertstufen
- Aktuelle Daten zum Engagement

Überprüfen Sie die Namen der benutzerdefinierten Attribute, die von Amperity an Braze gesendet werden sollen. Amperity fügt ein benutzerdefiniertes Attribut hinzu, wenn es keinen passenden Namen gibt.

Benutzerdefinierte Attribute werden nur für die Benutzer aktualisiert, die eine passende `external_id` oder `braze_id` in Braze haben.

### Amperity-Publikum

Audiences, die von Amperity mit Braze synchronisiert werden, werden in Benutzerprofilen als benutzerdefinierte Attribute gespeichert. Diese können dann verwendet werden, um diese Benutzer in Braze anzusprechen.

![Dropdown-Liste der Filter mit benutzerdefinierten Attributen, die in der Kategorie Benutzerdefinierte Daten angezeigt werden.][1]{: style="max-width:60%;"}

![Dropdown-Liste mit benutzerdefinierten Attributen wie "l12m_frequency" und "l12m_monetary".][2]{: style="max-width:40%;"}

### Datentypen

Folgende Datentypen werden unterstützt:
- Boolesch
- Datum
- Datetime
- Dezimalzahlen (decimal)
- Schwimmer
- Integer
- String
- Varchar

Der verwendete Datentyp hängt von der Art des Attributs ab. Eine E-Mail-Adresse wäre zum Beispiel eine Zeichenkette, während das Alter eines Kunden eine ganze Zahl sein könnte.

### Duplizierung von Attributen

Vermeiden Sie das Senden von benutzerdefinierten Attributen, die die Standardfelder des Benutzerprofils duplizieren. Geburtsdaten sollten zum Beispiel als Benutzerprofilfeld mit dem Namen "dob" an Braze gesendet werden, um dem Standardattribut von Braze zu entsprechen. Wenn sie als "Geburtstag", "Geburtsdatum" oder eine andere Zeichenfolge gesendet werden, wird ein benutzerdefiniertes Attribut erstellt, und die Werte im Feld "dob" werden nicht aktualisiert.

### Datenpunkte

Amperity verfolgt, was sich zwischen den Synchronisierungen mit Braze ändert, und den Status der Sendungen insgesamt. Amperity sendet Braze nur die Listenmitgliedschaft und andere ausgewählte Attribute, die sich seit der letzten Synchronisierung geändert haben.  

## Integration

### Schritt 1: Erfassen Sie Konfigurationsdetails für Braze

1. Erstellen Sie einen Braze REST API-Schlüssel für Ihren Braze-Arbeitsbereich mit den Berechtigungen `users.track` unter **Benutzerdaten**. Der Endpunkt `users.track` synchronisiert das Amperity-Publikum mit Braze als benutzerdefiniertes Attribut.
2. Bestimmen Sie den [REST-API-Endpunkt]({{site.baseurl}}/api/basics#endpoints) für Ihre Braze-Instanz. Wenn Ihre Braze-URL beispielsweise `https://dashboard-03.braze.com` lautet, ist Ihr REST-API-Endpunkt `https://rest.iad-03.braze.com` und Ihre Instanz ist "US-03".
3. Bestimmen Sie eine Liste von [Benutzerprofilfeldern]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields) und [benutzerdefinierten Attributen]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/), die von Amperity an Braze gesendet werden können.

### Schritt 2: Einrichten von Braze als Ziel-DataGrid-Operator

#### Schritt 2a: Erstellen Sie die Tabelle der Kundenprofile

Erstellen Sie eine neue Tabelle mit dem Namen "Braze Kundenattribute" in Ihrer Customer 360 Datenbank in Amperity. Diese Tabelle sollte alle Attribute von Braze enthalten, die Ihre Marke von Amperity aus verwalten möchte, einschließlich der von Braze geforderten Standardfelder für Benutzerprofile und aller benutzerdefinierten Attribute. Verwenden Sie SQL, um die Struktur dieser Tabelle zu definieren, wie in [der Amperity-Dokumentation](https://docs.amperity.com/datagrid/destination_braze.html#customer-profiles-table) beschrieben.

#### Schritt 2b: Benennen, validieren und speichern Sie die Tabelle

Benennen Sie die Tabelle "Braze Kundenattribute" und speichern Sie sie. Vergewissern Sie sich, dass die Tabelle für den **Segment-Editor** und den Editor **Attribute bearbeiten** innerhalb von Kampagnen zugänglich ist.

#### Schritt 2c: Braze als Ziel hinzufügen

Navigieren Sie in der Amperity-Plattform zur Registerkarte **Ziele**. Suchen Sie nach der Option zum Hinzufügen eines neuen Ziels. Wählen Sie unter den verfügbaren Optionen die Option **Hartlöten**.

![Der Abschnitt Neues Ziel mit dem Namen "Braze API", der Beschreibung "Send audience attributes to Braze." und dem Plugin "Braze".][3]{: style="max-width:60%;"}

#### Schritt 2d: Details zum Ziel konfigurieren

Geben Sie unter **Braze-Einstellungen** die Braze-Anmeldedaten und die Zieleinstellungen ein, wie in [der Amperity-Dokumentation](https://docs.amperity.com/datagrid/destination_braze.html#add-destination) beschrieben. Geben Sie die im letzten Schritt gesammelten Konfigurationsdetails ein und definieren Sie den Braze-Identifikator. Verfügbare Identifikatoren für den Abgleich sind:
- `braze_id`: Eine automatisch zugewiesene Braze-Kennung, die nicht geändert werden kann und mit einem bestimmten Benutzer verbunden ist, wenn dieser in Braze erstellt wird.
- `external_id`: Ein vom Kunden zugewiesener Identifikator, in der Regel eine UUID. 

![Der Abschnitt Braze-Einstellungen mit einer Instanz "US-03", der Benutzerkennung "external_id", einem leeren Segmentnamen, dem S3-Bucket "amperity-training-abc123" und dem S3-Ordner "braze-attributes".][4]{: style="max-width:60%;"}

#### Schritt 2e: Eine Datenvorlage hinzufügen

Öffnen Sie auf der Registerkarte **Ziele** das Menü für das Ziel Braze und wählen Sie **Datenvorlage hinzufügen**. Geben Sie einen Namen und eine Beschreibung für die Vorlage ein (z. B. "Braze" und "Benutzerdefinierte Attribute an Braze senden"), überprüfen Sie den Zugriff des Geschäftsbenutzers und kontrollieren Sie alle Konfigurationseinstellungen. 

Wenn die erforderlichen Einstellungen nicht als Teil des Ziels konfiguriert wurden, konfigurieren Sie sie als Teil der Datenvorlage. Speichern Sie die Datenvorlage.

![Der Abschnitt Name der Datenvorlage mit dem Namen "Braze Audience Attributes" und der Beschreibung "Send audience attributes to Braze".][5]{: style="max-width:60%;"}

#### Schritt 2f: Speichern Sie die Konfiguration 

Nachdem Sie die erforderlichen Angaben gemacht haben, speichern Sie die Konfiguration. Jetzt, wo Braze als Ziel konfiguriert ist, können Amp360- und AmpIQ-Benutzer Daten mit Braze synchronisieren.

### Schritt 3: Daten mit Braze synchronisieren

Stellen Sie sicher, dass Braze für Ihren Amperity-Mieter aktiviert ist. Wenn dies nicht der Fall ist, wenden Sie sich bitte an Ihren DataGrid Operator oder einen Vertreter von Amperity.

Befolgen Sie dann die Anweisungen für die Synchronisierung mit Amp360 oder AmpIQ, je nachdem, was für Ihr Unternehmen gilt.

#### Synchronisierungsoption 1: Senden Sie Abfrageergebnisse an Braze über Amp360

Amp360-Benutzer können SQL verwenden, um Freiform-Abfragen zu schreiben und dann einen Zeitplan zu konfigurieren, der die Ergebnisse an Braze sendet.

##### Schritt 1: Erstellen Sie eine Abfrage in Amperity

Navigieren Sie zur Abfragefunktion in Amperity und erstellen Sie eine SQL-Abfrage, die den gewünschten Satz an Kundendaten liefert. Die Ergebnisse sollten die spezifischen Attribute enthalten, die Sie an Braze senden möchten. Sehen Sie sich dieses Beispiel einer Amperity-Abfrage an, mit der Sie eine Liste von Nutzern und deren Kaufhistorie erhalten.

##### Schritt 2: Eine neue Orchestrierung in Amperity hinzufügen

1. Gehen Sie zum Abschnitt **Orchestrierung** und klicken Sie auf die Option zum Hinzufügen einer neuen Orchestrierung. 
2. Geben Sie an, was die Orchestrierung tun soll. Dazu gehört in der Regel die Angabe der SQL-Abfrage, die ausgeführt werden soll und wohin die Ergebnisse gesendet werden sollen. In diesem Fall wählen Sie die SQL-Abfrage, die Sie erstellt haben, um die Liste der aktiven Kunden zu erstellen, und geben Braze als Ziel für die Ergebnisse an.
3. Legen Sie fest, wann und wie oft die Orchestrierung ausgeführt werden soll. Sie können die Orchestrierung zum Beispiel täglich zu einer bestimmten Zeit ausführen.
4. Speichern Sie die Orchestrierung, nachdem Sie sie nach Ihren Wünschen konfiguriert haben. Sie wird zu Ihrer Liste der Orchestrationen in Amperity hinzugefügt.
5. Testen Sie die Orchestrierung, um sicherzustellen, dass sie wie erwartet funktioniert. Sie können dies tun, indem Sie die Orchestrierung manuell auslösen und die Ergebnisse in Braze überprüfen.

##### Schritt 3: Starten Sie die Orchestrierung 

Führen Sie die Orchestrierung aus, um die Abfrage auszuführen und die Ergebnisse an Braze zu senden. Dies kann manuell oder nach dem Zeitplan geschehen, den Sie in den Orchestrierungseinstellungen festgelegt haben.

#### Synchronisierungsoption 2: Senden Sie Audienzen an Braze über AmpIQ

AmpIQ-Benutzer können Segmente in Amperity über eine Nicht-SQL-Schnittstelle erstellen und diese mit nachgelagerten Zielen wie Braze synchronisieren. Benutzer können Ziele auswählen und dann eine Liste von Attributen konfigurieren, die an jedes Ziel gesendet werden sollen.

##### Schritt 1: Erstellen Sie ein Segment in Amperity 

Erstellen Sie in Amperity ein Segment, das eine Liste von Kunden liefert. Dieses Segment sollte mit den benutzerdefinierten Attributen verknüpft sein, die Sie in Braze aktualisieren möchten.

{% alert note %}
In der Dokumentation von Amperity finden Sie Beispiele für verschiedene Segmenttypen, die Sie möglicherweise an Braze senden möchten.
{% endalert %}

##### Schritt 2: Erstellen Sie eine Kampagne in Amperity

1. Gehen Sie zum Abschnitt **Kampagne** und klicken Sie auf die Option zum Erstellen einer neuen Kampagne.
2. Geben Sie Ihrer Kampagne einen beschreibenden und eindeutigen Namen, damit Sie sie später leichter identifizieren können, insbesondere wenn Sie mehrere Kampagnen haben.
3. Wählen Sie das Kundensegment, das Sie mit dieser Kampagne ansprechen möchten. Dies sollte das Segment sein, das Sie zuvor erstellt haben. <br>![Das Dropdown-Feld für Segmente, die von der Zielgruppenansprache ausgeschlossen werden sollen.][6]{: style="max-width:50%;"}<br><br>
4. Wählen Sie die Daten, die Sie im Rahmen der Kampagne versenden möchten. Dies kann eine Reihe von Kundenattributen umfassen. ![Im Modal "Kampagnenattribute bearbeiten" können Sie ein Ziel und Kundenattribute auswählen. ][7]{: style="max-width:90%;"}<br><br>
5. Wählen Sie **Braze** als Ziel, an das die Kampagnendaten gesendet werden sollen.
6. Wählen Sie, wann und wie oft die Kampagne laufen soll. Dies kann ein einmaliges Ereignis oder ein wiederkehrender Zeitplan sein.
7. Speichern Sie Ihre Kampagne und führen Sie einen Test durch, um sicherzustellen, dass sie wie erwartet funktioniert.

##### Schritt 3: Führen Sie die Kampagne durch

Führen Sie die Kampagne aus, um das Segment an Braze zu senden. Dies kann manuell erfolgen oder auf der Grundlage des Zeitplans, den Sie in den Kampagneneinstellungen festgelegt haben.


### Stromstärke mit Lötströmen verwenden
Zum Senden von Braze Currents-Daten an Amperity:
1. [Richten Sie einen Braze Current ein]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/setting_up_currents/), um Daten an einen Amazon S3-Bucket zu senden.
2. Konfigurieren Sie Amperity so, dass es [Apache Avro-Dateien aus diesem Amazon S3-Bucket liest](https://docs.amperity.com/datagrid/source_amazon_s3.html).
3. Konfigurieren Sie Feeds und automatisieren Sie das Laden von Daten mithilfe von Standard-Workflows.

[1]: {% image_buster /assets/img/amperity/custom_attributes_filters.png %}
[2]: {% image_buster /assets/img/amperity/search_custom_attributes_filters.png %}
[3]: {% image_buster /assets/img/amperity/destination_name.png %}
[4]: {% image_buster /assets/img/amperity/braze_settings.png %}
[5]: {% image_buster /assets/img/amperity/data_template_name.png %}
[6]: {% image_buster /assets/img/amperity/select_segments.png %}
[7]: {% image_buster /assets/img/amperity/edit_campaign_attributes.png %}
