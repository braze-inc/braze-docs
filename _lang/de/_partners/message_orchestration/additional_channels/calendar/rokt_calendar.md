---
nav_title: Rokt-Kalender
article_title: Rokt-Kalender
alias: /partners/rokt_calendar/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Rokt Calendar, einer dynamischen Kalendermarketing-Technologie, die es Marken ermöglicht, 1:1-Events und Werbebotschaften in Form von Kalenderereignissen und Benachrichtigungen zu versenden."
page_type: partner
search_tag: Partner

---

# Rokt-Kalender

> [Rokt Calendar](https://www.rokt.com/rokt-calendar/) ist eine dynamische Kalender-Marketingtechnologie, die es Marken ermöglicht, 1:1-Ereignisse und Werbebotschaften in Form von Kalenderereignissen und Benachrichtigungen zu versenden.

Die Integration von Braze und Rokt Calendar ermöglicht es, Ihre Rokt Calendar-Abonnenten und deren Daten über einen Braze-Webhook an Braze zu übertragen. Sie können diese Daten dann in Braze Canvases für das Journey-Targeting und die Zielgruppensegmentierung mit einem der folgenden benutzerdefinierten [Rokt Calendar-Attribute](#audience-segmentation) verwenden. 

## Voraussetzungen

| Anforderung  | Beschreibung |
| ------------ | ----------- |
| Rokt Calendar Konto | Um die Vorteile dieser Partnerschaft zu nutzen, ist ein kundenspezifisches Rokt Calendar-Konto erforderlich. Kontaktieren Sie [sales-calendar@rokt.com](mailto:sales-calendar@rokt.com), um mit einem Kundenbetreuer zu sprechen.  |
| Rokt Kalender einrichten | Ihr Rokt Calendar-Kundenbetreuer wird mit Ihnen zusammenarbeiten, um den Kalender so einzurichten, dass er Ihren Bedürfnissen am besten entspricht, einschließlich Einstellungen wie:<br>\- Flagge verschmelzen<br>\- Fallback-Flag für Abonnenten-ID<br>\- E-Mail-Erfassung, falls erforderlich |
| Rokt Calendar OAuth-Anmeldeinformationen | Mit diesem Schlüssel, den Sie von Ihrem Rokt Calendar Account Manager erhalten, können Sie Ihre Braze- und Rokt Calendar-Konten miteinander verbinden.<br><br>Diese können Sie im Braze Dashboard unter **Einstellungen** > **Verbundene Inhalte** erstellen. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. Diesen Schlüssel müssen Sie Ihrem Rokt Calendar Account Manager mitteilen.<br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| [Braze REST Endpunkt]({{site.baseurl}}/api/basics/#endpoints) | Ihre REST-Endpunkt-URL. Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
| Externe Teilnehmer-ID | Dies ist die Kennung, die vom Rokt Calendar-Abonnementprozess verwendet wird, um den Kalenderabonnenten mit dem Braze-Benutzer abzugleichen. Dies ist etwas, das Sie an Rokt Calendar weitergeben.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Segmentierung des Publikums {#audience-segmentation}

Wenn Rokt Calendar einen neuen Benutzer erstellt oder einen bestehenden Abonnenten mit einem Braze-Benutzer abgleicht, sendet Rokt Calendar die folgenden benutzerdefinierten Abonnementattribute, die Sie in Braze filtern können:

| Angepasstes Attribut  | Definition       | Beispiel          |
| ----------------  | ---------------- | ---------------- |
| `rokt:account_code` | Code des Rokt Calendar-Kontos | `brazetest/f5733866ade2` und `brazetest/ff10919f1078` |
| `rokt:account_id` |ID des Rokt Calendar-Kontos | `d0ce4299-7d6c-4888-bfd8-c7e867a0fa6c/f5733866ade2` |
| `rokt:account_name` | Name des Rokt Calendar-Kontos | `Braze Test/f5733866ade2` |
| `rokt:calendar_code` | Code des Rokt Calendar Kalenders | `test-calendar-1/f5733866ade2` |
| `rokt:calendar_id` | ID des Kalenders Rokt Calendar | `9a9007c7-f5a4-e811-b13c-06424c4f2724/f5733866ade2` |
| `rokt:calendar_title` | Titel des Kalenders Rokt Calendar | `Test Calendar 1/f5733866ade2` |
| `rokt:country_code` | Ländercode für das erstellte Abonnement | `AU/f5733866ade2` |
| `rokt:device_name` | Gerätetyp für das erstellte Abonnement | `Desktop/f5733866ade2` |
| `rokt:geo_country` | Herkunftsland für das erstellte Abonnement | `Australia/f5733866ade2` |
| `rokt:optIn1` | Wenn sich der Benutzer für das erste von 2 Opt-Ins für das erstellte Abonnement entschieden hat | `True/f5733866ade2` |
| `rokt:optIn2` | Wenn sich der Benutzer für das zweite von 2 Opt-Ins für das erstellte Abonnement entschieden hat | `True/f5733866ade2` |
| `rokt:source` | Die Quelle des erstellten Abonnements | `brazetest.Rokt Calendarapp.com/f5733866ade2` |
| `rokt:subscriber_email` | Die E-Mail-Adresse, die der Benutzer während des Anmeldevorgangs eingegeben hat | `test@email.com/f5733866ade2` |
| `rokt:subscription_id` | Die Abonnement-ID, die als eindeutiger Bezeichner für das erstellte Abonnement dient | `06423672-b6ba-4536-aa36-70788a7a0a36` |
| `rokt:subscription_method` | Abo-Methode (webcal/Google) im Zusammenhang mit dem erstellten Abonnement. | `WebCal/f5733866ade2` |
| `rokt:tags` | Verwendete Kalender-Tags im Zusammenhang mit dem erstellten Abonnement. | `Test Calendar 1/All Teams/f5733866ade2 and Test Calendar 1/TeamI//f5733866ade2` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Rokt Calendar löst außerdem ein benutzerdefiniertes Ereignis `subscribe` aus, sobald der Benutzer Ihren Rokt-Kalender abonniert hat, das entweder in der Braze-Segmentierung oder als Auslöser für eine Kampagne oder eine Canvas-Komponente verwendet werden kann.

## Integration

### Schritt 1: Aufbau einer Zielgruppe von Kalender-Abonnenten

Um Kalenderereignisse von Canvas aus zu versenden, müssen Sie zunächst einen Rokt-Kalender mit bereits abonnierten Benutzern einrichten. Dazu müssen Sie Ihre Benutzer darüber informieren, wo und wie sie den Kalender abonnieren können. Rokt Calendar empfiehlt, dass Sie:

#### Integrationspunkte für Abonnements bereitstellen
Um ein Publikum von Kalender-Abonnenten aufzubauen, müssen Sie ein Ziel anbieten, zu dem ein Benutzer navigieren und sich anmelden kann. Einige Beispiele für Abonnement-Integrationspunkte sind:
  - Fügen Sie eine Kalender-Schaltfläche zu Ihrer Website hinzu
  - Hinzufügen eines Kalenderlinks in einer E-Mail oder SMS 
  - Hinzufügen einer Kalender-Schaltfläche zu Ihrer App
  - Fügen Sie einen Kalenderlink in sozialen Medien hinzu

#### Werben Sie für den Kalender
Um ein Publikum von Abonnenten aufzubauen, müssen Sie den Kalender bei Ihrem Publikum bekannt machen, damit es weiß, wie es ihn abonnieren kann. Einige Beispiele für Kalenderwerbung sind:
  - Beiträge in sozialen Medien
  - E-Mail-Newsletter und Updates
  - Blog-Beiträge
  - In-App-Benachrichtigungen

### Schritt 2: Erstellen Sie einen Rokt Calendar Webhook in Braze

In Braze können Sie entweder eine Webhook-Kampagne oder einen Webhook innerhalb eines Canvas einrichten:

- Senden Sie ein neues personalisiertes Ereignis: Erlauben Sie, dass neue Ereignisse zu einem Segment der Kalender von Abonnenten hinzugefügt werden.
- Aktualisieren Sie ein personalisiertes Ereignis: Ermöglichen Sie die Aktualisierung eines bestehenden Termins in den Kalendern der Abonnenten.

Um eine Rokt Calendar Webhook-Vorlage zu erstellen, die Sie in zukünftigen Kampagnen oder Canvases verwenden können, navigieren Sie zu **Vorlagen** > **Webhook-Vorlagen** in der Braze-Plattform. 

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, gehen Sie zu **Engagement** > **Vorlagen & Medien** > **Webhook-Vorlagen**.
{% endalert %}

Wenn Sie eine einmalige Rokt Calendar Webhook-Kampagne erstellen oder eine bestehende Vorlage verwenden möchten, wählen Sie **Webhook** in Braze, wenn Sie eine neue Kampagne erstellen.

{% tabs %}
{% tab Ein neues Ereignis senden %}
Sobald Sie die Rokt Calendar Webhook-Vorlage ausgewählt haben, sollten Sie folgendes sehen:
- **Webhook URL**: {% raw %}`{% assign accountCode = {{custom_attribute.${rokt:account_code}}}[0] | split: '/' | first %}https://api.roktcalendar.com/v1/subscriptionevent/{{accountCode}}`{% endraw %}
- **Anfrage Körper**: Rohtext
{% endtab %}
{% tab Ein bestehendes Ereignis aktualisieren %}
Sobald Sie die Rokt Calendar Webhook-Vorlage ausgewählt haben, sollten Sie folgendes sehen:
- **Webhook URL**: {% raw %}`{% assign accountCode = {{custom_attribute.${rokt:account_code}}}[0] | split: '/' | first %}https://api.roktcalendar.com/v1/subscriptionevent/{{accountCode}}/update`{% endraw %}
- **Anfrage Körper**: Rohtext
{% endtab %}
{% endtabs %}

#### Kopfzeilen der Anfrage und Methode

Rokt Calendar benötigt für die Autorisierung eine `HTTP Header`, die den Namen Ihrer Rokt Calendar Connected Content Zugangsdaten enthält. Die folgenden Angaben sind bereits als Schlüssel-Wert-Paare in der Vorlage enthalten, aber auf der Registerkarte **Einstellungen** müssen Sie `<Rokt-Calendar-API>` durch den Namen der Anmeldedaten ersetzen, den Sie unter `Manage Settings > Connected Content > Credential` finden.

{% raw %}
- **HTTP-Methode**: POST
- **Kopfzeile der Anfrage**:
  - **Autorisierung**: Träger `{% connected_content https://api.roktcalendar.com/oauth2/token :method post :basic_auth <Rokt-Calendar-API> :body grant_type=client_credentials :save token :retry %}{{token.access_token}}`
  - **Inhalt-Typ**: application/json
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
| `eventId` <br>**\*erforderlich** | Eine eindeutige Kennung für das Ereignis, das hinzugefügt oder aktualisiert werden soll | `Event_00001`
| `eventTitle` <br>**\*erforderlich** | Der Titel des Ereignisses, wie er im Kalender erscheinen würde | Sommerschlussverkauf 2019
| `eventDescr` | Die Beschreibung des Ereignisses, wie sie im Kalender erscheinen würde | Der Verkauf läuft drei Tage lang. Klicken Sie auf diesen Link `www.mybusiness.com/sale`, um die Angebote zu sehen. |
| `eventLocation` | Der Ort des Ereignisses, wie er im Kalender erscheinen würde. Beachten Sie, dass dies oft als zweiter Aufruf zum Handeln verwendet wird, der den eventTitle ergänzt. | Öffnen Sie die Veranstaltung, um 50% Rabatt zu erhalten |
| `eventStart` <br>**\*erforderlich**  | Das Startdatum und die Uhrzeit des Ereignisses, wie sie im Kalender erscheinen würden | `2019-02-21T15:00:00` |
| `eventEnd` <br>**\*erforderlich**  | Das Startdatum und die Uhrzeit des Ereignisses, wie sie im Kalender erscheinen würden | `2019-02-21T16:00:00` |
| `eventTz` <br>**\*erforderlich**  | Die Zeitzone des Ereignisses, wie sie im Kalender erscheinen würde. Beachten Sie, dass die Liste der anwendbaren Zeitzonen [hier](https://roktcalendar-api.readme.io/docs/timezones) zu finden ist. | `Eastern Standard Time` |
| `notifyBefore` <br>**\*erforderlich**  | Die Erinnerungszeit des Ereignisses, wie sie im Kalender erscheinen würde. Beachten Sie, dass diese in Minuten angegeben wird. | `15` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}
{% endtabs %}

{% alert tip %}
Eine Liste der gültigen Zeitzonen finden Sie unter [https://roktcalendar-api.readme.io](https://roktcalendar-api.readme.io/reference/timezones)/reference/timezones.
{% endalert %}

### Schritt 3: Vorschau Ihrer Anfrage

Zeigen Sie Ihre Anfrage in der **Vorschau** an oder wechseln Sie zur Registerkarte **Test**, wo Sie einen zufälligen Benutzer, einen vorhandenen Benutzer oder einen eigenen Benutzer auswählen können, um Ihren Webhook zu testen.

{% alert important %}
Denken Sie daran, Ihre Vorlage zu speichern, bevor Sie die Seite verlassen! <br>Aktualisierte Webhook-Vorlagen finden Sie in der Liste **Gespeicherte Webhook-Vorlagen**, wenn Sie eine neue [Webhook-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) erstellen.
{% endalert %}
