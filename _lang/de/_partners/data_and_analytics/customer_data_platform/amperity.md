---
nav_title: Amperity
article_title: Amperity
alias: /partners/amperity/
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Amperity, einer umfassenden Plattform für Kundendaten von Unternehmen, die es Ihnen erlaubt, Nutzer:innen von Amperity zu synchronisieren, Daten zu vereinheitlichen, Daten über AWS S3-Buckets an Braze zu senden und mehr."
page_type: partner
search_tag: Partner

---

# Amperity

> [Amperity](https://amperity.com/) ist eine umfassende Customer Data Platform (CDP) für Unternehmen, die Marken dabei hilft, ihre Kunden kennenzulernen, strategische Entscheidungen zu treffen und konsequent die richtigen Maßnahmen zu ergreifen, um ihre Verbraucher:in besser zu bedienen. Amperity bietet intelligente Funktionen für die Vereinheitlichung der Datenverwaltung, Analytics, Insights und Aktivierung.

_Diese Integration wird von Amperity gepflegt._

{% multi_lang_include video.html id="06G0lxaSjgk" align="right" %}

Die Integration von Braze und Amperity bietet eine einheitliche Sicht auf Ihre Kund:in auf beiden Plattformen. Diese Integration lässt Sie zu:
- **Synchronisieren Sie Kundenprofile**: Bilden Sie Nutzerdaten und angepasste Attribute von Amperity auf Braze ab. 
- **Zielgruppen erstellen und versenden**: Erstellen Sie Segmente, die Listen aktiver Kund:innen und die dazugehörigen angepassten Attribute an Braze zurücksenden, und senden Sie diese an Braze.
- **Verwalten Sie Daten-Updates**: Steuern Sie die Häufigkeit, mit der Updates für angepasste Attribute an Braze gesendet werden.
- **Daten vereinheitlichen**: Vereinheitlichen Sie Daten über verschiedene von Amperity unterstützte Plattformen und Braze.
- **Synchronisieren Sie Braze Daten mit Amazon S3**: Verwenden Sie Braze-Currents zur Integration von Engagement-Daten aus Braze-Kampagnen, was eine Synchronisierung der Daten mit Amazon S3 im Apache Avro-Format zulässig macht.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Amperity Konto | Sie benötigen ein [Amperity Konto](https://amperity.com/request-a-demo), um die Vorteile dieser Partnerschaft zu nutzen. |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br> Dieser kann im Braze-Dashboard erstellt werden, indem Sie zu **Entwicklungskonsole** > **REST-API-Schlüssel** > **Neuen API-Schlüssel erstellen** navigieren. |
| Braze-Instanz | Ihre Braze-Instanz erhalten Sie von Ihrem Braze Onboarding Manager oder auf der [Übersichtsseite über die APIs]({{site.baseurl}}/api/basics#endpoints). |
| Braze REST Endpunkt | Ihre Braze Endpunkt-URL. Ihr Endpunkt hängt von Ihrer Braze-Instanz ab. |
| Currents Konnektor (optional) | Der S3 Currents Konnektor. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Abbildung der Daten

Sowohl Standard- als auch angepasste Attribute können von Amperity an Braze gesendet werden, was es Ihnen erlaubt, Kundenprofile in Braze mit Daten aus verschiedenen Quellen über Amperity anzureichern. Die spezifischen Attribute, die Sie senden können, hängen von den Daten in Ihrem Amperity-System und den Attributen ab, die Sie in Braze eingerichtet haben.

Lesen Sie unten, um mehr über diese Attribute zu erfahren.

### Standard-Attribute 

[Profil-Attribute]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields) beschreiben, wer Ihre Kund:innen sind. Sie sind oft mit der Identität der Kund:in verbunden, wie z.B.:
- Namen
- Geburtsdaten
- E-Mail-Adressen
- Telefonnummern

### Angepasste Attribute 

[Angepasste Attribute]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) in Braze sind Felder, die von Ihrer Marke bestimmt werden. Wenn Sie möchten, dass Amperity angepasste Attribute verwaltet, die bereits in Braze vorhanden sind, passen Sie die von Amperity gesendete Ausgabe an die Namen an, die sich bereits in Ihrem Braze Workspace befinden. Dies kann Folgendes beinhalten:
- Kauf Verläufe
- Loyalitätsstatus
- Wertstufen
- Aktuelle Daten zum Engagement

Überprüfen Sie die Namen der angepassten Attribute, die von Amperity an Braze gesendet werden. Amperity fügt ein angepasstes Attribut hinzu, wenn es keinen passenden Namen gibt.

Angepasste Attribute werden nur für diejenigen Nutzer:innen aktualisiert, die über eine passende `external_id` oder `braze_id` in Braze verfügen.

### Amperity Zielgruppen

Zielgruppen, die von Amperity mit Braze synchronisiert wurden, werden als angepasste Attribute in Nutzerprofilen gespeichert. Diese können dann verwendet werden, um diese Nutzer:innen in Braze zu targetieren.

![Dropdown-Liste der Filter mit angepassten Attributen, die in der Kategorie Benutzerdefinierte Daten angezeigt werden.]({% image_buster /assets/img/amperity/custom_attributes_filters.png %}){: style="max-width:60%;"}

![Dropdown-Liste mit angepassten Attributen wie "l12m_frequency" und "l12m_monetary".]({% image_buster /assets/img/amperity/search_custom_attributes_filters.png %}){: style="max-width:40%;"}

### Daten-Typen

Folgende Datentypen werden unterstützt:
- Boolesch
- Datum
- Datetime
- Dezimalzahlen (decimal)
- Gleitkommazahl
- Integer
- String
- Varchar

Der verwendete Datentyp hängt von der Art des Attributs ab. Eine E-Mail Adresse wäre zum Beispiel ein String, während das Alter einer Kund:in eine ganze Zahl sein könnte.

### Duplizierung von Attributen

Vermeiden Sie das Senden angepasster Attribute, die die Felder des Standard Nutzerprofils duplizieren. Das Geburtsdatum sollte beispielsweise als Nutzerprofil-Feld mit dem Namen "dob" an Braze gesendet werden, damit es mit dem Standardattribut von Braze übereinstimmt. Wenn sie als "Geburtstag", "Geburtsdatum" oder ein anderer String gesendet werden, wird ein angepasstes Attribut erstellt, und die Werte im Feld "dob" werden nicht aktualisiert.

### Datenpunkte

Amperity verfolgt, was sich zwischen den Synchronisierungen mit Braze ändert und wie der Status der Sendungen insgesamt ist. Amperity sendet Braze nur die Listenmitgliedschaft und andere ausgewählte Attribute, die sich seit der letzten Synchronisierung geändert haben.  

## Integration

### Schritt 1: Erfassen Sie Konfigurationsdetails für Braze

1. Erstellen Sie einen Braze REST API-Schlüssel für Ihren Braze Workspace mit den `users.track` Berechtigungen unter **Nutzerdaten**. Der Endpunkt `users.track` synchronisiert die Amperity Zielgruppe mit Braze als angepasstes Attribut.
2. Ermitteln Sie den [REST API Endpunkt]({{site.baseurl}}/api/basics#endpoints) für Ihre Braze-Instanz. Wenn Ihre Braze-URL beispielsweise `https://dashboard-03.braze.com` lautet, ist Ihr REST API-Endpunkt `https://rest.iad-03.braze.com` und Ihre Instanz ist "US-03".
3. Bestimmen Sie eine Liste von [Nutzerprofilfeldern]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields) und [angepassten Attributen]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/), die von Amperity an Braze gesendet werden können.

### Schritt 2: Einrichten von Braze als Ziel-DataGrid Operator

#### Schritt 2a: Erstellen Sie die Tabelle mit den Kundenprofilen

Erstellen Sie eine neue Tabelle mit dem Namen "Braze Customer Attributes" in Ihrer Customer 360 Datenbank in Amperity. Diese Tabelle sollte alle Attribute von Braze enthalten, die Ihre Marke von Amperity aus verwalten möchte, einschließlich der von Braze geforderten Standardfelder des Nutzerprofils und aller angepassten Attribute. Verwenden Sie SQL, um die Struktur dieser Tabelle zu definieren, wie in [der Amperity Dokumentation](https://docs.amperity.com/datagrid/destination_braze.html#customer-profiles-table) beschrieben.

#### Schritt 2b: Benennen, validieren und speichern Sie die Tabelle

Benennen Sie die Tabelle "Braze Customer Attributes" und speichern Sie sie. Überprüfen Sie, ob die Tabelle für den **Segment Editor** und den Editor **Attribute bearbeiten** innerhalb von Kampagnen zugänglich ist.

#### Schritt 2c: Braze als Reiseziel hinzufügen

Navigieren Sie in der Amperity Plattform zum Tab **Ziele**. Suchen Sie nach der Option, ein neues Ziel hinzuzufügen. Wählen Sie aus den verfügbaren Optionen **Braze** aus.

![Der Abschnitt "Neues Ziel" mit dem Namen "Braze API", der Beschreibung "Senden Sie Attribute der Zielgruppe an Braze." und dem Plugin "Braze".]({% image_buster /assets/img/amperity/destination_name.png %}){: style="max-width:60%;"}

#### Schritt 2d: Ziel-Details konfigurieren

Geben Sie unter **Braze-Einstellungen** die Zugangsdaten zu Braze und die Zieleinstellungen an, wie in [der Dokumentation von Amperity](https://docs.amperity.com/datagrid/destination_braze.html#add-destination) beschrieben. Geben Sie die im letzten Schritt gesammelten Konfigurationsdetails ein und definieren Sie den Bezeichner für Braze. Verfügbare Bezeichner für den Abgleich sind:
- `braze_id`: Ein automatisch zugewiesener Bezeichner von Braze, der nicht geändert werden kann und mit einem bestimmten Nutzer:innen verbunden ist, wenn diese in Braze erstellt werden.
- `external_id`: Ein von Kund:in zugewiesener Bezeichner, normalerweise eine UUID. 

![Der Abschnitt Braze-Einstellungen mit der Instanz "US-03", dem Bezeichner "external_id", dem leeren Segmentenamen, dem S3-Bucket "amperity-training-abc123" und dem S3-Ordner "braze-attributes".]({% image_buster /assets/img/amperity/braze_settings.png %}){: style="max-width:60%;"}

#### Schritt 2e: Eine Daten-Template hinzufügen

Öffnen Sie auf dem Tab **Ziele** das Menü für das Ziel Braze und wählen Sie **Daten Template hinzufügen**. Geben Sie einen Namen und eine Beschreibung für das Template ein (z.B. "Braze" und "Angepasste Attribute an Braze senden"), überprüfen Sie den Zugriff der geschäftlichen Nutzer:innen und kontrollieren Sie alle Konfigurationseinstellungen. 

Wenn die erforderlichen Einstellungen nicht als Teil des Ziels konfiguriert wurden, konfigurieren Sie sie als Teil der Daten-Templates. Speichern Sie das Template für die Daten.

![Der Abschnitt Daten Template Name mit dem Namen "Braze Audience Attributes" und der Beschreibung "Send audience attributes to Braze".]({% image_buster /assets/img/amperity/data_template_name.png %}){: style="max-width:60%;"}

#### Schritt 2f: Speichern Sie die Konfiguration 

Nachdem Sie die erforderlichen Angaben gemacht haben, speichern Sie die Konfiguration. Jetzt, da Braze als Ziel konfiguriert ist, können Nutzer:innen von Amp360 und AmpIQ Daten mit Braze synchronisieren.

### Schritt 3: Daten mit Braze synchronisieren

Stellen Sie sicher, dass Braze für Ihren Amperity-Mieter aktiviert ist. Wenn dies nicht der Fall ist, wenden Sie sich an Ihren DataGrid Operator oder die Vertretung von Amperity.

Befolgen Sie dann die Anweisungen für die Synchronisierung mit Amp360 oder AmpIQ, je nachdem, was für Ihr Unternehmen gilt.

#### Synchronisierungsoption 1: Senden Sie Abfrageergebnisse an Braze über Amp360

Nutzer:innen von Amp360 können mit SQL-Abfragen in freier Form schreiben und dann einen Zeitplan konfigurieren, der die Ergebnisse an Braze sendet.

##### Schritt 1: Erstellen Sie eine Abfrage in Amperity

Navigieren Sie zur Abfragefunktion in Amperity und erstellen Sie eine SQL-Abfrage, die den gewünschten Datensatz mit Kundendaten liefert. Die Ergebnisse sollten die spezifischen Attribute enthalten, die Sie an Braze senden möchten. Sehen Sie sich dieses Beispiel einer Amperity-Abfrage an, mit der Sie eine Liste von Nutzer:innen mit ihren Kaufverläufen erhalten.

##### Schritt 2: Hinzufügen einer neuen Orchestrierung in Amperity

1. Gehen Sie zum Bereich **Orchestrierung** und klicken Sie auf die Option zum Hinzufügen einer neuen Orchestrierung. 
2. Geben Sie an, was die Orchestrierung tun soll. Dazu gehört in der Regel die Angabe der SQL-Abfrage, die ausgeführt werden soll und wohin die Ergebnisse gesendet werden sollen. Wählen Sie in diesem Fall die SQL-Abfrage aus, die Sie erstellt haben, um die Liste der aktiven Kund:in zu erstellen, und geben Sie Braze als Ziel für die Ergebnisse an.
3. Legen Sie fest, wann und wie oft die Orchestrierung ausgeführt werden soll. Sie können die Orchestrierung zum Beispiel täglich zu einer bestimmten Zeit ausführen.
4. Speichern Sie die Orchestrierung, nachdem Sie sie nach Ihren Wünschen konfiguriert haben. Sie wird zu Ihrer Liste der Orchestrierung in Amperity hinzugefügt.
5. Testen Sie die Orchestrierung, um sicherzustellen, dass sie wie erwartet funktioniert. Sie können dies tun, indem Sie die Orchestrierung manuell triggern und die Ergebnisse in Braze überprüfen.

##### Schritt 3: Führen Sie die Orchestrierung aus 

Führen Sie die Orchestrierung aus, um die Abfrage auszuführen und die Ergebnisse an Braze zu senden. Dies kann manuell geschehen oder nach dem Zeitplan, den Sie in den Einstellungen für die Orchestrierung festgelegt haben.

#### Synchronisierungsoption 2: Senden Sie Zielgruppen an Braze über AmpIQ

Nutzer:innen von AmpIQ können Segmente in Amperity über eine Nicht-SQL-Schnittstelle erstellen und diese mit nachgelagerten Zielen wie Braze synchronisieren. Nutzer:innen können Ziele auswählen und dann eine Liste von Attributen konfigurieren, die an jedes Ziel gesendet werden sollen.

##### Schritt 1: Erstellen Sie ein Segment in Amperity 

Erstellen Sie ein Segment in Amperity, das eine Liste von Kund:in liefert. Dieses Segment sollte mit den angepassten Attributen verknüpft sein, die Sie in Braze aktualisieren möchten.

{% alert note %}
In der Dokumentation von Amperity finden Sie Beispiele für verschiedene Segmente, die Sie möglicherweise an Braze senden möchten.
{% endalert %}

##### Schritt 2: Erstellen Sie eine Kampagne in Amperity

1. Gehen Sie in den Bereich **Kampagne** und klicken Sie auf die Option zum Erstellen einer neuen Kampagne.
2. Geben Sie Ihrer Kampagne einen beschreibenden und eindeutigen Namen, mit dem Sie sie später leichter identifizieren können, insbesondere wenn Sie mehrere Kampagnen haben.
3. Wählen Sie das Segment der Kund:in aus, das Sie mit dieser Kampagne ansprechen möchten. Dies sollte das Segment sein, das Sie zuvor erstellt haben. <br>![Das Dropdown-Feld für Segmente, die von der Targetierung ausgeschlossen werden sollen.]({% image_buster /assets/img/amperity/select_segments.png %}){: style="max-width:50%;"}<br><br>
4. Wählen Sie die Daten, die Sie im Rahmen der Kampagne versenden möchten. Dies kann eine Reihe von Kund:in-Attributen umfassen. ![Im Modal Kampagnen-Attribute bearbeiten können Sie ein Ziel und die Attribute der Kund:in auswählen. ]({% image_buster /assets/img/amperity/edit_campaign_attributes.png %}){: style="max-width:90%;"}<br><br>
5. Wählen Sie **Braze** als das Ziel aus, an das die Daten der Kampagne gesendet werden sollen.
6. Wählen Sie, wann und wie oft die Kampagne laufen soll. Dies kann ein einmaliges Ereignis oder ein wiederkehrender Zeitplan sein.
7. Speichern Sie Ihre Kampagne und führen Sie einen Test durch, um sicherzustellen, dass sie wie erwartet funktioniert.

##### Schritt 3: Führen Sie die Kampagne durch

Führen Sie die Kampagne aus, um das Segment an Braze zu senden. Dies kann manuell geschehen oder auf der Grundlage des Zeitplans, den Sie in den Einstellungen der Kampagne eingerichtet haben.


### Verwendung von Amperity mit Braze-Currents
So senden Sie Braze-Currents-Daten an Amperity:
1. [Richten Sie einen Braze-Currents ein]({{site.baseurl}}/user_guide/data/braze_currents/setting_up_currents/), um Daten an ein Amazon S3-Bucket zu senden.
2. Konfigurieren Sie Amperity so, dass es [Apache Avro-Dateien aus diesem Amazon S3 Bucket liest](https://docs.amperity.com/datagrid/source_amazon_s3.html).
3. Konfigurieren Sie Feeds und automatisieren Sie das Laden von Daten mit Hilfe von Standard-Workflows.


