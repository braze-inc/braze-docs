---
nav_title: Zendesk
article_title: Zendesk Chat
description: "Erfahren Sie, wie Sie Zendesk Chat mit Braze integrieren und eine beidseitige SMS-Konversation einrichten können."
alias: /partners/zendesk_chat/
page_type: partner
search_tag: Partner

---

# Zendesk Chat

> [Zendesk Chat](https://www.zendesk.com/service/messaging/) verwendet Webhooks von jeder Plattform, um eine wechselseitige SMS-Konversation einzurichten. Wenn ein Nutzer:innen eine Anfrage an den Support stellt, wird ein Ticket in Zendesk erstellt. Die Antworten der Agenten werden über eine API-getriggerte SMS-Kampagne an Braze weitergeleitet, und die Antworten der Nutzer:innen werden an Zendesk zurückgesendet.

## Voraussetzungen


| Voraussetzung | Beschreibung |
|---|---|
| Ein Zendesk-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Zendesk-Konto.|
| Ein Zendesk Basic Authorization Token | Ein Zendesk Basic Authorization Token wird verwendet, um eine ausgehende Webhook-Anfrage von Braze an Zendesk zu stellen.|
| Ein Braze REST API-Schlüssel  | Ein Braze REST API-Schlüssel mit `campaigns.trigger.send` Berechtigungen. Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden.|

## Anwendungsfälle

Verbessern Sie die Effizienz des Kund:innen-Supports, indem Sie die SMS-Funktionen von Braze mit den Antworten von Zendesk-Live-Agenten kombinieren, um Nutzer:innen bei Anfragen umgehend zu unterstützen.

## Integration von Zendesk Chat

### Schritt 1: Erstellen Sie einen Webhook in Zendesk

1. Gehen Sie in der Entwicklungskonsole von Zendesk zu Webhooks: {% raw %}`https://{{url}}.zendesk.com/admin/apps-integrations/webhooks/webhooks`{% endraw %}
2. Wählen Sie unter **Webhook erstellen** den Punkt **Triggern oder Automatisierung** aus.
3. Fügen Sie für **Endpunkt-URL** den Endpunkt **/campaign/trigger/send** hinzu.
4. Wählen Sie unter **Authentifizierung** das **Token Bearer** aus und fügen Sie den REST API-Schlüssel von Braze mit den Berechtigungen `campaigns.trigger.send` hinzu.

![Ein Beispiel für einen Webhook von Zendesk.]({% image_buster /assets/img/zendesk/instant_chat/chat1.png %}){: style="max-width:70%;"}

### Schritt 2: Erstellen Sie eine ausgehende SMS-Kampagne

Als nächstes erstellen Sie eine SMS-Kampagne, die auf Webhooks von Zendesk wartet und eine angepasste SMS-Antwort an Ihre Kund:innen sendet.

#### Schritt 2.1: Verfassen Sie Ihre Nachricht

Wenn Zendesk den Inhalt einer Nachricht über die API sendet, hat er das folgende Format:

```
**----------------------------------------------\n\n{Replier Name}, {Replier Date}\n\n{Message}**
```

Wir müssen also die Details, die in der Nachricht angezeigt werden sollen, aus diesem String extrahieren, sonst sieht ein Nutzer:innen alle Details.

![Eine Beispiel-SMS ohne Formatierung.]({% image_buster /assets/img/zendesk/instant_chat/chat2.png %}){: style="max-width:40%;"}

Fügen Sie in das Textfeld **Nachricht** den folgenden Liquid Code und eine Opt-out-Sprache oder andere statische Inhalte ein:

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

![Eine Beispiel-SMS mit Formatierung.]({% image_buster /assets/img/zendesk/instant_chat/chat3.png %}){: style="max-width:70%;"}

#### Schritt 2.2: Zeitplan für die Zustellung

Wählen Sie für die Art der Zustellung die **API-getriggerte Zustellung** aus und kopieren Sie dann die ID der Kampagne, die in den nächsten Schritten verwendet werden soll.

![API Ausgelöste Zustellung]({% image_buster /assets/img/zendesk/instant_chat/chat4.png %}){: style="max-width:70%;"}

Schalten Sie schließlich unter **Zustellungssteuerung** die Wiederzulassung ein.

![Die Wiederzulassung wurde unter "Zustellungskontrollen" aktiviert.]({% image_buster /assets/img/zendesk/instant_chat/chat5.png %})

### Schritt 3: Erstellen Sie einen Trigger in Zendesk, um Antworten von Agenten an Braze weiterzuleiten.

Gehen Sie zu **Objekte und Regeln** > **Geschäftsregeln** > **Triggers** (Auslöser).

1. Erstellen Sie eine neue **Kategorie** (z.B. **Eine Nachricht triggern**).
2. Erstellen Sie einen neuen **Trigger** (z.B. **Reagieren per SMS Braze**).
3. Wählen Sie unter **Bedingungen**:
- **Ticket>Kommentar** ist **vorhanden und der Anfragende kann den Kommentar sehen**, so dass die Nachricht immer dann getriggert wird, wenn ein neuer öffentlicher Kommentar in ein Ticket Update aufgenommen wird
- **Ticket>Update** *ist kein* **Internet Dienst (API)**, so dass eine Nachricht, die ein Nutzer:innen von Braze aus sendet, nicht an sein Mobiltelefon weitergeleitet wird. Nur Nachrichten, die von Zendesk kommen, werden weitergeleitet.

![Antworten Sie per SMS Braze.]({% image_buster /assets/img/zendesk/instant_chat/chat6.png %}){: style="max-width:70%;"}

Wählen Sie unter **Aktionen** die Option **Über Webhook benachrichtigen** aus und wählen Sie den Endpunkt, den Sie in Schritt 1 erstellt haben. Als nächstes geben Sie den Körper des API-Aufrufs an. Geben Sie die `campaign_id` aus [Schritt 2.2](#step-22-schedule-the-delivery) in den Körper der Anfrage ein.

![Antworten Sie per SMS Braze JSON body.]({% image_buster /assets/img/zendesk/instant_chat/chat7.png %}){: style="max-width:70%;"}

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


### Schritt 4: Erstellen Sie einen Trigger in Zendesk, um einen Nutzer:innen zu aktualisieren, wenn ein Ticket geschlossen wird.

Wenn Sie den Nutzer:innen benachrichtigen möchten, dass das Ticket geschlossen wurde, erstellen Sie in Braze eine neue Kampagne mit dem Template für den Antwortkörper.

![Update eines Nutzers:innen, wenn ein Ticket geschlossen wird.]({% image_buster /assets/img/zendesk/instant_chat/chat8.png %}){: style="max-width:70%;"}

Wählen Sie **API-getriggerte Zustellung** und kopieren Sie die ID der Kampagne.

Als nächstes richten Sie einen Trigger ein, der Braze benachrichtigt, wenn das Ticket geschlossen wird:
- Kategorie: **Eine Nachricht triggern**
- Wählen Sie unter Bedingungen **Ticket>Ticketstatus** und ändern Sie ihn in **Gelöst**

![Gelöstes Ticket in Zendesk einrichten.]({% image_buster /assets/img/zendesk/instant_chat/chat9.png %}){: style="max-width:70%;"}

Wählen Sie unter **Aktionen** die Option **Über Webhook benachrichtigen** aus und wählen Sie den zweiten Endpunkt, den Sie gerade erstellt haben. Von dort aus müssen wir den Körper des API-Aufrufs angeben:

![Gelöstes Ticket JSON Körper.]({% image_buster /assets/img/zendesk/instant_chat/chat10.png %}){: style="max-width:70%;"}

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

### Schritt 5: Hinzufügen eines angepassten Nutzer:innen-Feldes in Zendesk

Wählen Sie im Admin Center in der Seitenleiste **Personen** und dann **Konfiguration** > **Nutzer:innen**. Fügen Sie das angepasste Nutzer:innen-Feld `braze_external_id` hinzu.

### Schritt 6: Eingehende SMS-Weiterleitung einrichten

Als nächstes erstellen Sie zwei neue Webhook-Kampagnen in Braze, damit Sie eingehende SMS von Kunden an den Posteingang von Zendesk weiterleiten können.

| Kampagne           | Zweck                                                                              |
|--------------------|--------------------------------------------------------------------------------------|
| Webhook Kampagne 1 | Erzeugt ein neues Ticket in Zendesk.                                                     |
| Webhook Kampagne 2 | Leitet alle konversationellen SMS-Antworten weiter, die eingehend vom Kunden an Zendesk gesendet werden. |
{: .reset-td-br-1 .reset-td-br-2 }

#### Schritt 6.1: Erstellen Sie eine SMS-Schlüsselwortkategorie

Gehen Sie im Braze-Dashboard auf **Zielgruppe**, wählen Sie Ihre **SMS-Abo-Gruppe** und wählen Sie dann **Benutzerdefiniertes Schlüsselwort hinzufügen**. Füllen Sie die folgenden Felder aus, um eine exklusive SMS-Schlüsselwortkategorie für Zendesk zu erstellen.

| Feld            | Beschreibung                                                                                                               |
|------------------|---------------------------------------------------------------------------------------------------------------------------|
| Keyword-Kategorie | Der Name Ihrer Schlüsselwortkategorie, z. B. `ZendeskSMS1`.                                                                 |
| Keyword         | Ihre angepassten Schlüsselwörter, wie z.B. `SUPPORT`.                                                                                  |
| Antwortnachricht    | Die Nachricht, die gesendet wird, wenn ein Schlüsselwort erkannt wird, z.B. "Ein Mitarbeiter des Kundendienstes wird sich in Kürze bei Ihnen melden." |
{: .reset-td-br-1 .reset-td-br-2 }

![Ein Beispiel für eine SMS-Schlüsselwortkategorie in Braze.]({% image_buster /assets/img/zendesk/instant_chat/chat11.png %}){: style="max-width:70%;"}

#### Schritt 6.2: Erstellen Sie Ihre erste Webhook-Kampagne

Erstellen Sie im Braze-Dashboard Ihre erste Webhook-Kampagne. Diese Nachricht signalisiert Zendesk, dass Support angefragt wird.

Füllen Sie im Webhook Composer die folgenden Felder aus:
- Webhook URL: {% raw %}https://{{url}}.zendesk.com/api/v2/tickets{% endraw %}
- HTTP-Methode: POST
- Anfrage-Header:
- Content-Typ: application/json
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

![Eine Beispielanfrage mit den beiden erforderlichen Headern.]({% image_buster /assets/img/zendesk/instant_chat/chat12.png %}){: style="max-width:70%;"}


#### Schritt 6.3: Zeitplan für die erste Zustellung

Wählen Sie für die **Zeitplan-Zustellung** die **aktionsbasierte Zustellung** aus und wählen Sie dann für Ihren Auslösertyp **Eingehende SMS-Nachrichten senden**. Fügen Sie auch die SMS Abo-Gruppe und die Stichwortkategorie hinzu, die Sie zuvor eingerichtet haben.

![Die Seite "Zeitplan für die Zustellung" für die erste Webhook-Kampagne.]({% image_buster /assets/img/zendesk/instant_chat/chat13.png %})

Schalten Sie unter **Zustellungssteuerung** die Wiederzulassung ein.

![Wiederzulassung ausgewählt unter "Zustellungskontrollen" für die erste Webhook Kampagne.]({% image_buster /assets/img/zendesk/instant_chat/chat14.png %})

#### Schritt 6.4: Erstellen Sie Ihre zweite Webhook-Kampagne

Richten Sie eine Webhook-Kampagne ein, um verbleibende SMS-Nachrichten des Nutzers:innen an Zendesk weiterzuleiten:

Da Zendesk die Ticket ID als String sendet, erstellen Sie einen Content-Block, um den String in eine ganze Zahl umzuwandeln, damit Sie ihn im Webhook von Zendesk verwenden können.

{% raw %}
```liquid
{% assign var = {{custom_attribute.${zendesk_ticket}}} | to_i %}{{var}}
```
{% endraw %}

Im Webhook Composer:
- Webhook URL: {% raw %}https://{{url}}.zendesk.com/api/v2/tickets/{{content_blocks.${to_int}}}.json{% endraw %}
- Anfrage: PUT
- KVPs:
    - Content-Typ:application/JSON
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
- Richten Sie einen aktionsbasierten Trigger für Nutzer:in ein, die eine eingehende Nachricht in der Kategorie "Andere" senden.
- Legen Sie Kriterien für die Wiederzulassung fest.
- Fügen Sie anwendbare Zielgruppen hinzu (in diesem Fall ist das angepasste Attribut **zendesk_ticket_open** **wahr**).

[2]: {% image_buster /assets/img/zendesk/instant_chat/chat2.png %}
