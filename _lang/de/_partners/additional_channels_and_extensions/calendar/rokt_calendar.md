---
nav_title: Rokt-Kalender
article_title: Rokt-Kalender
alias: /partners/rokt_calendar/
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Rokt Calendar, einer dynamischen Kalender Marketingtechnologie, die es Marken ermöglicht, 1:1 Ereignisse und Werbebotschaften in Form von Kalenderereignissen und -benachrichtigungen zu pushen."
page_type: partner
search_tag: Partner
---

# Rokt-Kalender

> [Rokt Calendar](https://www.rokt.com/rokt-calendar/) ist eine dynamische Kalender Marketingtechnologie, die es Marken ermöglicht, 1:1-Ereignisse und Werbebotschaften in Form von Kalenderereignissen und -benachrichtigungen zu pushen.

_Diese Integration wird von Rokt Calendar gepflegt._

## Über die Integration

Die Integration von Braze und Rokt Calendar lässt es zu, dass Ihre Abonnenten von Rokt Calendar und deren Daten über einen Braze-Webhook an Braze gepusht werden. Sie können diese Daten dann in Braze Canvase für das Journey-Targeting und die Segmentierung der Zielgruppe mit einem der folgenden angepassten [Attribute von Rokt Calendar](#audience-segmentation) verwenden. 

## Voraussetzungen

| Anforderung  | Beschreibung |
| ------------ | ----------- |
| Rokt Calendar Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein kundenspezifisches Rokt Calendar Konto. Kontaktieren Sie [sales-calendar@rokt.com](mailto:sales-calendar@rokt.com), um mit einem Account Manager zu sprechen.  |
| Rokt Calendar einrichten | Ihr Account Manager von Rokt Calendar wird mit Ihnen zusammenarbeiten, um den Kalender so einzurichten, dass er Ihren Bedürfnissen am besten entspricht, einschließlich Einstellungen wie:<br>\- Flagge verschmelzen<br>\- Fallback-Flag für Abonnenten-ID<br>\- E-Mail-Erfassung, falls erforderlich |
| Rokt Calendar OAuth-Zugangsdaten | Mit diesem Schlüssel, den Ihnen Ihr Account Manager von Rokt Calendar zur Verfügung stellt, können Sie Ihre Braze- und Rokt Calendar-Kontos miteinander verbinden.<br><br>Diese können im Braze-Dashboard unter **Einstellungen** > **Connected-Content** erstellt werden. |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. Diesen Schlüssel müssen Sie Ihrem Rokt Calendar Account Manager:in mitteilen.<br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| [Braze REST Endpunkt]({{site.baseurl}}/api/basics/#endpoints) | Ihre REST Endpunkt URL. Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
| Externe ID des Abonnenten:innen | Dies ist der Bezeichner, der vom Rokt Calendar Abo-Prozess verwendet wird, um den Kalender Abonnent:in mit dem Braze Nutzer:in abzugleichen. Dies ist etwas, das Sie an Rokt Calendar weitergeben.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Segmentierung der Zielgruppe {#audience-segmentation}

Wenn Rokt Calendar einen neuen Nutzer erstellt oder einen bestehenden Nutzer mit einem Braze-Benutzer abgleicht, sendet Rokt Calendar die folgenden angepassten Attribute für Abonnenten, die Sie in Braze filtern können:

| Angepasstes Attribut  | Definition       | Beispiel          |
| ----------------  | ---------------- | ---------------- |
| `rokt:account_code` | Code des Rokt Calendar Kontos | `brazetest/f5733866ade2` und `brazetest/ff10919f1078` |
| `rokt:account_id` |ID des Rokt Calendar Kontos | `d0ce4299-7d6c-4888-bfd8-c7e867a0fa6c/f5733866ade2` |
| `rokt:account_name` | Name des Rokt Calendar Kontos | `Braze Test/f5733866ade2` |
| `rokt:calendar_code` | Code des Rokt Calendar Kalenders | `test-calendar-1/f5733866ade2` |
| `rokt:calendar_id` | ID des Rokt Calendar Kalenders | `9a9007c7-f5a4-e811-b13c-06424c4f2724/f5733866ade2` |
| `rokt:calendar_title` | Titel des Rokt Calendar Kalenders | `Test Calendar 1/f5733866ade2` |
| `rokt:country_code` | Ländercode für das erstellte Abo | `AU/f5733866ade2` |
| `rokt:device_name` | Gerätetyp in Bezug auf das erstellte Abo | `Desktop/f5733866ade2` |
| `rokt:geo_country` | Herkunftsland in Bezug auf das erstellte Abo | `Australia/f5733866ade2` |
| `rokt:optIn1` | Wenn der Nutzer:innen sich für das erste von 2 Opt-ins in Bezug auf das erstellte Abo entschieden hat | `True/f5733866ade2` |
| `rokt:optIn2` | Wenn der Nutzer:innen sich für das zweite von 2 Opt-ins in Bezug auf das erstellte Abo entschieden hat | `True/f5733866ade2` |
| `rokt:source` | Die Quelle des erstellten Abos | `brazetest.Rokt Calendarapp.com/f5733866ade2` |
| `rokt:subscriber_email` | Die E-Mail Adresse, die der Nutzer:innen während des Abo-Vorgangs eingegeben hat | `test@email.com/f5733866ade2` |
| `rokt:subscription_id` | Die ID des Abonnements, die als eindeutiger Bezeichner für das erstellte Abonnement dient | `06423672-b6ba-4536-aa36-70788a7a0a36` |
| `rokt:subscription_method` | Abo-Methode (webcal/Google), die sich auf das erstellte Abo bezieht. | `WebCal/f5733866ade2` |
| `rokt:tags` | Verwendete Tags des Kalenders im Zusammenhang mit dem erstellten Abo. | `Test Calendar 1/All Teams/f5733866ade2 and Test Calendar 1/TeamI//f5733866ade2` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Rokt Calendar triggert außerdem ein angepasstes Event `subscribe`, sobald der Benutzer Ihren Rokt Kalender abonniert hat. Dieses Event kann entweder in der Segmentierung von Braze verwendet werden oder als Trigger für eine Kampagne oder eine Canvas-Komponente dienen.

## Integration

### Schritt 1: Aufbau einer Zielgruppe von Abonnent:innen des Kalenders

Um Kalender-Ereignisse von Canvas aus zu versenden, müssen Sie zunächst einen Rokt-Kalender mit bereits abonnierten Nutzer:in einrichten. Dazu müssen Sie Ihren Nutzer:innen mitteilen, wo und wie sie den Kalender abonnieren können. Rokt Calendar empfiehlt, dass Sie:

#### Bereitstellung von Abo-Integrationspunkten
Um eine Zielgruppe von Kalender-Abonnenten aufzubauen, müssen Sie ein Ziel anbieten, zu dem ein Nutzer:in navigieren und es abonnieren kann. Einige Beispiele für Abo-Integrationspunkte sind:
  - Fügen Sie einen Kalender Button zu Ihrer Website hinzu
  - Hinzufügen eines Kalender-Links in einer E-Mail oder SMS 
  - Fügen Sie einen Kalender Button zu Ihrer App hinzu
  - Fügen Sie einen Kalender-Link auf Social Media hinzu

#### Bewerben Sie den Kalender
Um eine Zielgruppe von Abonnenten aufzubauen, müssen Sie den Kalender bei Ihrer Zielgruppe bekannt machen, damit diese weiß, wie sie ihn abonnieren kann. Einige Beispiele für Kalender-Aktionen sind:
  - Beiträge in Social Media
  - E-Mail-Newsletter und Updates
  - Blog-Beiträge
  - In-App-Benachrichtigungen

### Schritt 2: Erstellen Sie einen Rokt Calendar-Webhook in Braze

Innerhalb von Braze können Sie entweder eine Kampagne mit Webhook oder einen Webhook innerhalb eines Canvas einrichten:

- Senden Sie ein neues personalisiertes Ereignis: Zulassen, dass einem Segment der Kalender von Abonnenten neue Ereignisse hinzugefügt werden.
- Aktualisieren Sie ein personalisiertes Ereignis: Erlaubt das Update eines bestehenden Termins in den Kalendern von Abonnenten:in.

Um eine Rokt Calendar Webhook-Vorlage zu erstellen, die Sie in zukünftigen Kampagnen oder Canvase verwenden können, navigieren Sie auf der Braze-Plattform zu **Vorlagen** > **Webhook-Vorlagen**. 

Wenn Sie eine einmalige Rokt Calendar Webhook-Kampagne erstellen oder eine bestehende Vorlage verwenden möchten, wählen Sie bei der Erstellung einer neuen Kampagne **Webhook** in Braze aus.

{% tabs %}
{% tab Ein neues Ereignis senden %}
Sobald Sie die Webhook-Vorlage Rokt Calendar ausgewählt haben, sollten Sie folgendes sehen:
- **Webhook URL**: {% raw %}`{% assign accountCode = {{custom_attribute.${rokt:account_code}}}[0] | split: '/' | first %}https://api.roktcalendar.com/v1/subscriptionevent/{{accountCode}}`{% endraw %}
- **Anfrage Körper**: Rohtext
{% endtab %}
{% tab Ein bestehendes Ereignis aktualisieren %}
Sobald Sie die Webhook-Vorlage Rokt Calendar ausgewählt haben, sollten Sie folgendes sehen:
- **Webhook URL**: {% raw %}`{% assign accountCode = {{custom_attribute.${rokt:account_code}}}[0] | split: '/' | first %}https://api.roktcalendar.com/v1/subscriptionevent/{{accountCode}}/update`{% endraw %}
- **Anfrage Körper**: Rohtext
{% endtab %}
{% endtabs %}

#### Kopfzeilen der Anfrage und Methode

Rokt Calendar benötigt zur Autorisierung eine `HTTP Header`, die den Namen Ihrer Connected-Content-Zugangsdaten für Rokt Calendar enthält. Die folgenden Angaben sind bereits als Schlüssel-Wert-Paare in der Vorlage enthalten, aber auf dem Tab **Einstellungen** müssen Sie `<Rokt-Calendar-API>` durch den Namen der Zugangsdaten ersetzen, den Sie unter `Manage Settings > Connected Content > Credential` finden.

{% raw %}
- **HTTP-Methode**: POST
- **Anfrage-Header**:
  - **Autorisierung**: Bearer `{% connected_content https://api.roktcalendar.com/oauth2/token :method post :basic_auth <Rokt-Calendar-API> :body grant_type=client_credentials :save token :retry %}{{token.access_token}}`
  - **Content-Typ**: application/json
{% endraw %}

#### Anfragetext

{% tabs local %}
{% tab Ein neues Ereignis senden %}
{% raw %}
```javascript
{% capture eventId %}Event_0001{% endcapture %}
{% capture eventTitle %}Event Title{% endcapture %}
{% capture eventDescr %}Event Description{% endcapture %}
{% capture eventLocation %}Event Location{% endcapture %}
{% capture eventStart %}2019-02-21T15:00:00{% endcapture %}
{% capture eventEnd %}2019-02-21T15:00:00{% endcapture %}
{% capture notifyBefore %}15{% endcapture %}
{% capture eventTZ %}Eastern Standard Time{% endcapture %}

{
  "event": {
    "eventId": "{{eventId}}_{{${user_id}}}",
    "title": "{{eventTitle}}",
    "description": "{{eventDescr}}",
    "location": "{{eventLocation}}",
    "start": "{{eventStart}}",
    "end": "{{eventEnd}}",
    "timezone": "{{eventTZ}}",
    "notifyBefore": "{{notifyBefore}}"
  },
  "subscriptionIds": ["{{custom_attribute.${rokt:subscription_id}| join: '","'  }}"]
}
```
{% endraw %}
{% endtab %}
{% tab Ein bestehendes Ereignis aktualisieren %}
{% raw %}
```javascript
{% capture eventId %}Event_0001{% endcapture %}
{% capture eventTitle %}Event Title{% endcapture %}
{% capture eventDescr %}Event Description{% endcapture %}
{% capture eventLocation %}Event Location{% endcapture %}
{% capture eventStart %}2019-02-21T15:00:00{% endcapture %}
{% capture eventEnd %}2019-02-21T15:00:00{% endcapture %}
{% capture notifyBefore %}15{% endcapture %}
{% capture eventTZ %}Eastern Standard Time{% endcapture %}

{
  "event": {
    "eventId": "{{eventId}}_{{${user_id}}}",
    "title": "{{eventTitle}}",
    "description": "{{eventDescr}}",
    "location": "{{eventLocation}}",
    "start": "{{eventStart}}",
    "end": "{{eventEnd}}",
    "timezone": "{{eventTZ}}",
    "notifyBefore": "{{notifyBefore}}"
  }
}
```
{% endraw %}
{% endtab %}
{% tab Details zur Veranstaltung %}
Die folgenden Felder enthalten Informationen, die auf der Ebene des Ereignisses angepasst werden können.

| Feld             | Definition       | Beispiel          |
| ----------------  | ---------------- | ---------------- |
| `eventId` <br>**\*erforderlich** | Ein eindeutiger Bezeichner für das Ereignis, das hinzugefügt oder aktualisiert werden soll | `Event_00001`
| `eventTitle` <br>**\*erforderlich** | Der Titel des Ereignisses, wie er im Kalender erscheinen würde | Sommerschlussverkauf 2019
| `eventDescr` | Die Beschreibung des Ereignisses, wie sie im Kalender erscheinen würde | Der Verkauf läuft drei Tage lang. Klicken Sie auf diesen Link `www.mybusiness.com/sale`, um die Angebote zu sehen. |
| `eventLocation` | Der Standort des Ereignisses, wie er im Kalender erscheinen würde. Beachten Sie, dass dies oft als zweite Aufforderung zum Handeln verwendet wird, die den eventTitle ergänzt. | Öffnen Sie die Veranstaltung und erhalten Sie 50% Rabatt |
| `eventStart` <br>**\*erforderlich**  | Das Datum und die Uhrzeit des Beginns des Ereignisses, wie es im Kalender erscheinen würde | `2019-02-21T15:00:00` |
| `eventEnd` <br>**\*erforderlich**  | Das Datum und die Uhrzeit des Beginns des Ereignisses, wie es im Kalender erscheinen würde | `2019-02-21T16:00:00` |
| `eventTz` <br>**\*erforderlich**  | Die Zeitzone des Ereignisses, wie sie im Kalender erscheinen würde. Beachten Sie, dass die Liste der anwendbaren Zeitzonen [hier](https://roktcalendar-api.readme.io/docs/timezones) zu finden ist. | `Eastern Standard Time` |
| `notifyBefore` <br>**\*erforderlich**  | Die Erinnerungszeit des Ereignisses, wie sie im Kalender erscheinen würde. Beachten Sie, dass diese in Minuten ausgedrückt wird. | `15` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}
{% endtabs %}

{% alert tip %}
Eine Liste der gültigen Zeitzonen finden Sie unter [https://roktcalendar-api.readme.io](https://roktcalendar-api.readme.io/reference/timezones)/reference/timezones.
{% endalert %}

### Schritt 3: Vorschau auf Ihre Anfrage

Eine Vorschau Ihrer Anfrage finden Sie im Panel **Vorschau** oder auf dem Tab **Test**, wo Sie einen zufälligen Nutzer, einen bestehenden Nutzer:innen auswählen oder Ihren eigenen anpassen können, um Ihren Webhook zu testen.

{% alert important %}
Denken Sie daran, Ihr Template zu speichern, bevor Sie die Seite verlassen! <br>Aktualisierte Webhook-Templates finden Sie in der Liste **Gespeicherte Webhook-Templates**, wenn Sie eine neue [Webhook-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) erstellen.
{% endalert %}

