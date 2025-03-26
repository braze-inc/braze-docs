---
nav_title: Zendesk
article_title: Zendesk Chat
description: "Erfahren Sie, wie Sie Zendesk Chat mit Braze integrieren und eine Zwei-Wege-SMS-Konversation einrichten können."
alias: /partners/zendesk_chat/
page_type: partner
search_tag: Partner

---

# Zendesk Chat

> [Zendesk Chat](https://www.zendesk.com/service/messaging/) verwendet Webhooks von jeder Plattform, um eine zweiseitige SMS-Konversation einzurichten. Wenn ein Benutzer Support anfordert, wird ein Ticket in Zendesk erstellt. Die Antworten der Agenten werden über eine durch die API ausgelöste SMS-Kampagne an Braze weitergeleitet, und die Antworten der Benutzer werden an Zendesk zurückgesendet.

## Voraussetzungen


| Voraussetzung | Beschreibung |
|---|---|
| Ein Zendesk-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Zendesk-Konto.|
| Ein Zendesk Basic Autorisierungs-Token | Ein Zendesk Basic Authorization Token wird verwendet, um eine ausgehende Webhook-Anfrage von Braze an Zendesk zu stellen.|
| Ein Braze REST API Schlüssel  | Ein Braze REST API-Schlüssel mit `campaigns.trigger.send` Berechtigungen. Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden.|

## Anwendungsfälle

Verbessern Sie die Effizienz des Kundensupports, indem Sie die SMS-Funktionen von Braze mit den Antworten von Zendesk-Live-Agenten kombinieren, um Benutzeranfragen umgehend mit menschlichem Support zu beantworten.

## Integration von Zendesk Chat

### Schritt 1: Einen Webhook in Zendesk erstellen

1. Gehen Sie in der Zendesk-Entwicklerkonsole zu Webhooks: {% raw %}`https://{{url}}.zendesk.com/admin/apps-integrations/webhooks/webhooks`{% endraw %}
2. Unter **Webhook erstellen** wählen Sie **Auslöser oder Automatisierung**.
3. Fügen Sie bei **Endpunkt-URL** den Endpunkt **/campaign/trigger/send** hinzu.
4. Wählen Sie unter **Authentifizierung** die Option **Bearer-Token** und fügen Sie den Braze REST API-Schlüssel mit `campaigns.trigger.send` Berechtigungen hinzu.

![Ein Beispiel für einen Zendesk-Webhook.][1]{: style="max-width:70%;"}

### Schritt 2: Erstellen Sie eine ausgehende SMS-Kampagne

Als nächstes erstellen Sie eine SMS-Kampagne, die auf Webhooks von Zendesk wartet und eine individuelle SMS-Antwort an Ihre Kunden sendet.

#### Schritt 2.1: Verfassen Sie Ihre Nachricht

Wenn Zendesk den Inhalt einer Nachricht über die API sendet, hat er das folgende Format:

```
**----------------------------------------------\n\n{Replier Name}, {Replier Date}\n\n{Message}**
```

Wir müssen also die Details, die in der Nachricht angezeigt werden sollen, aus dieser Zeichenkette extrahieren, sonst sieht ein Benutzer alle Details.

![Eine Beispiel-SMS ohne Formatierung.][2]{: style="max-width:40%;"}

Fügen Sie in das Textfeld **Nachricht** den folgenden Liquid-Code und eine Opt-out-Sprache oder andere statische Inhalte ein:

{% raw %}
```liquid
{% assign body = {{api_trigger_properties.${msg_body}}} %}
{% assign msg = body | split: "
" %}
New message from Zendesk: 
{{msg[2]}}
 
Feel free to respond directly to this number!
```
{% endraw %}

![Eine Beispiel-SMS mit Formatierung.][3]{: style="max-width:70%;"}

#### Schritt 2.2: Planen Sie die Lieferung

Wählen Sie als Zustellungsart **API-gesteuerte Zustellung** und kopieren Sie dann die Kampagnen-ID, die in den nächsten Schritten verwendet wird.

![API-ausgelöste Lieferung][4]{: style="max-width:70%;"}

Aktivieren Sie schließlich unter **Zustellungskontrollen** die Wiederzulassung.

![Wiederzulassung aktiviert unter "Lieferkontrollen".][5]

### Schritt 3: Erstellen Sie einen Trigger in Zendesk, um Antworten von Agenten an Braze weiterzuleiten.

Gehen Sie zu **Objekte und Regeln** > **Geschäftsregeln** > **Auslöser**.

1. Erstellen Sie eine neue **Kategorie** (z.B. **Auslösen einer Nachricht**).
2. Erstellen Sie einen neuen **Auslöser** (z.B. **Reagieren über SMS Braze**).
3. Wählen Sie unter **Bedingungen**:
- **Ticket>Kommentar** ist **vorhanden und der Anfragesteller kann den Kommentar sehen**, so dass die Nachricht immer dann ausgelöst wird, wenn ein neuer öffentlicher Kommentar in eine Ticketaktualisierung aufgenommen wird
- **Ticket>Aktualisieren** *ist kein* **Webservice (API)**, so dass, wenn ein Benutzer eine Nachricht von Braze aus sendet, diese nicht an sein Mobiltelefon weitergeleitet wird. Nur Nachrichten, die von Zendesk kommen, werden weitergeleitet.

![Antworten Sie per SMS Braze.][6]{: style="max-width:70%;"}

Wählen Sie unter **Aktionen** die Option **Per Webhook benachrichtigen** und wählen Sie den Endpunkt, den Sie in Schritt 1 erstellt haben. Als nächstes geben Sie den Text des API-Aufrufs an. Geben Sie die `campaign_id` aus [Schritt 2.2](#step-22-schedule-the-delivery) in den Body der Anfrage ein.

![Antworten Sie über SMS Braze JSON body.][7]{: style="max-width:70%;"}

{% raw %}
```liquid
{
    "campaign_id": "{{YOUR_CAMPAIGN_ID}}",
    "recipients": [
        {
            "external_user_id": "{{ticket.requester.custom_fields.braze_external_id}}",
			"trigger_properties": {
    "msg_body": "{{ticket.latest_public_comment_html}}"
		},
		"attributes": {
        "zendesk_ticket" : "{{ticket.id}}",
	"zendesk_ticket_open" : "true"
    }
        }
    ]
}
```
{% endraw %}


### Schritt 4: Erstellen Sie einen Trigger in Zendesk, um einen Benutzer zu aktualisieren, wenn ein Ticket geschlossen wird.

Wenn Sie den Benutzer benachrichtigen möchten, dass das Ticket geschlossen wurde, erstellen Sie in Braze eine neue Kampagne mit der Vorlage für den Antwortkörper.

![Aktualisieren Sie einen Benutzer, wenn ein Ticket geschlossen wird.][8]{: style="max-width:70%;"}

Wählen Sie **API-ausgelöste Zustellung** und kopieren Sie die Kampagnen-ID.

Als nächstes richten Sie einen Auslöser ein, um Braze zu benachrichtigen, wenn das Ticket geschlossen wird:
- Kategorie: **Eine Nachricht auslösen**
- Wählen Sie unter Bedingungen **Ticket>Ticketstatus** und ändern Sie ihn in **Gelöst**

![Gelöstes Ticket in Zendesk eingerichtet.][9]{: style="max-width:70%;"}

Wählen Sie unter **Aktionen** die Option **Per Webhook benachrichtigen** und wählen Sie den zweiten Endpunkt, den Sie gerade erstellt haben. Von dort aus müssen wir den Körper des API-Aufrufs angeben:

![Gelöstes Ticket JSON Körper.][10]{: style="max-width:70%;"}

{% raw %}
```liquid
{
    "campaign_id": "{{YOUR_API_KEY}}",
    "recipients": [
        {
            "external_user_id": "{{ticket.requester.custom_fields.braze_external_id}}",
"trigger_properties": {
    "msg_body": "Your ticket has been closed"
		},
,
			"attributes": {
	"zendesk_ticket_open" : "false"
    }
        }
    ]
}
```
{% endraw %}

### Schritt 5: Hinzufügen eines benutzerdefinierten Benutzerfeldes in Zendesk

Wählen Sie im Admin Center in der Seitenleiste **Personen** und dann **Konfiguration** > **Benutzerfelder**. Fügen Sie das benutzerdefinierte Benutzerfeld `braze_external_id` hinzu.

### Schritt 6: Eingehende SMS-Weiterleitung einrichten

Als nächstes erstellen Sie zwei neue Webhook-Kampagnen in Braze, damit Sie eingehende SMS von Kunden an den Zendesk-Posteingang weiterleiten können.

| Kampagne           | Zweck                                                                              |
|--------------------|--------------------------------------------------------------------------------------|
| Webhook-Kampagne 1 | Erzeugt ein neues Ticket in Zendesk.                                                     |
| Webhook-Kampagne 2 | Leitet alle vom Kunden gesendeten Konversations-SMS-Antworten an Zendesk weiter. |
{: .reset-td-br-1 .reset-td-br-2 }

#### Schritt 6.1: Erstellen Sie eine SMS-Schlüsselwortkategorie

Gehen Sie im Braze Dashboard zu **Zielgruppe**, wählen Sie Ihre **SMS-Abonnementgruppe** und wählen Sie dann **Benutzerdefiniertes Schlüsselwort hinzufügen**. Füllen Sie die folgenden Felder aus, um eine exklusive SMS-Schlüsselwortkategorie für Zendesk zu erstellen.

| Feld            | Beschreibung                                                                                                               |
|------------------|---------------------------------------------------------------------------------------------------------------------------|
| Keyword-Kategorie | Der Name Ihrer Schlüsselwortkategorie, z. B. `ZendeskSMS1`.                                                                 |
| Schlüsselwörter         | Ihre benutzerdefinierten Schlüsselwörter, wie `SUPPORT`.                                                                                  |
| Antwortnachricht    | Die Nachricht, die gesendet wird, wenn ein Schlüsselwort erkannt wird, z. B. "Ein Kundendienstmitarbeiter wird sich in Kürze bei Ihnen melden." |
{: .reset-td-br-1 .reset-td-br-2 }

![Ein Beispiel für eine SMS-Schlüsselwortkategorie in Braze.][11]{: style="max-width:70%;"}

#### Schritt 6.2: Erstellen Sie Ihre erste Webhook-Kampagne

Erstellen Sie im Braze Dashboard Ihre erste Webhook-Kampagne. Diese Nachricht signalisiert Zendesk, dass Support angefordert wird.

Füllen Sie im Webhook Composer die folgenden Felder aus:
- Webhook URL: {% raw %}https://{{url}}.zendesk.com/api/v2/tickets{% endraw %}
- HTTP-Methode: POST
- Kopfzeilen anfordern:
- Inhalt-Typ: application/json
- Autorisierung:  Basic {{Token}}
- Körper der Anfrage: 

{% raw %}
```liquid
{
  "ticket": {
    "subject": "Action Needed",
    "comment": {
      "body": "{{sms.${inbound_message_body}}}"
    },
"requester":{
"name": "{{${first_name}}} {{${last_name}}}",
"user_fields": {
"braze_external_id": "{{${user_id}}}"
}
},
    "priority": "normal",
    "type": "problem"
  }
}
```
{% endraw %}

![Eine Beispielanfrage mit den beiden erforderlichen Kopfzeilen.][12]{: style="max-width:70%;"}


#### Schritt 6.3: Planen Sie die erste Lieferung

Wählen Sie für **Zeitgesteuerte Zustellung** die Option **Aktionsbasierte Zustellung** und wählen Sie dann als Auslösertyp **Ankommende SMS senden**. Fügen Sie auch die SMS-Abonnementgruppe und die Stichwortkategorie hinzu, die Sie zuvor eingerichtet haben.

![Die Seite "Lieferung planen" für die erste Webhook-Kampagne.][13]

Aktivieren Sie unter **Zustellungskontrolle** die Wiederzulassung.

![Wiederzulassung ausgewählt unter "Zustellungssteuerung" für die erste Webhook-Kampagne.][14]

#### Schritt 6.4: Erstellen Sie Ihre zweite Webhook-Kampagne

Richten Sie eine Webhook-Kampagne ein, um verbleibende SMS-Nachrichten des Benutzers an Zendesk weiterzuleiten:

Da Zendesk die Ticket-ID als String sendet, erstellen Sie einen Content Block, um den String in eine ganze Zahl zu konvertieren, damit Sie ihn im Webhook von Zendesk verwenden können.

{% raw %}
```liquid
{% assign var = {{custom_attribute.${zendesk_ticket}}} | to_i %}{{var}}
```
{% endraw %}

Im Webhook-Composer:
- Webhook URL: {% raw %}https://{{url}}.zendesk.com/api/v2/tickets/{{content_blocks.${to_int}}}.json{% endraw %}
- Anfrage: PUT
- KVPs:
    - Inhalt-Typ:Anwendung/JSON
    - Autorisierung: Basic {{Token}}

Beispiel Körper: 

{% raw %}
```liquid
{
  "ticket": {
    "comment": {
      "body": "Inbound message from {{${first_name}}} {{${last_name}}}: {{sms.${inbound_message_body}}}"
    }
}
}
```
{% endraw %}

#### Schritt 6.5: Einrichtung der zweiten Webhook-Kampagne abschließen
- Richten Sie einen aktionsbasierten Auslöser für Benutzer ein, die eine eingehende Nachricht in der Kategorie "Sonstige" senden.
- Legen Sie Kriterien für die Wiederzulassung fest.
- Fügen Sie die entsprechenden Zielgruppen hinzu (in diesem Fall ist das benutzerdefinierte Attribut **zendesk_ticket_open** **wahr**).

[1]: {% image_buster /assets/img/zendesk/instant_chat/chat1.png %}
[2]: {% image_buster /assets/img/zendesk/instant_chat/chat2.png %}
[3]: {% image_buster /assets/img/zendesk/instant_chat/chat3.png %}
[4]: {% image_buster /assets/img/zendesk/instant_chat/chat4.png %}
[5]: {% image_buster /assets/img/zendesk/instant_chat/chat5.png %}
[6]: {% image_buster /assets/img/zendesk/instant_chat/chat6.png %}
[7]: {% image_buster /assets/img/zendesk/instant_chat/chat7.png %}
[8]: {% image_buster /assets/img/zendesk/instant_chat/chat8.png %}
[9]: {% image_buster /assets/img/zendesk/instant_chat/chat9.png %}
[10]: {% image_buster /assets/img/zendesk/instant_chat/chat10.png %}
[11]: {% image_buster /assets/img/zendesk/instant_chat/chat11.png %}
[12]: {% image_buster /assets/img/zendesk/instant_chat/chat12.png %}
[13]: {% image_buster /assets/img/zendesk/instant_chat/chat13.png %}
[14]: {% image_buster /assets/img/zendesk/instant_chat/chat14.png %}
