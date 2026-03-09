---
nav_title: Nachrichten senden
article_title: Versenden von Nachrichten über die REST API
page_order: 1
page_type: reference
description: "Dieser Referenzartikel behandelt die beiden Möglichkeiten, Nachrichten mithilfe der Braze-REST-API programmgesteuert zu versenden."
---

# Versenden von Nachrichten über die REST API

> Sie können Nachrichten in Realtime über zwei verschiedene Braze-Endpunkte von Ihrem Backend aus versenden. Jede hat eine unterschiedliche Anforderungsform: Eine erfordert den vollständigen Inhalt der Nachricht in der Anfrage, die andere erfordert eine Kampagnen-ID und sendet den im Dashboard definierten Inhalt.

Dieser Ansatz ist mit jedem von der API unterstützten Messaging-Kanal kompatibel (WhatsApp, E-Mail, SMS, Push-Benachrichtigungen, Content-Cards, Webhooks und mehr).

## Zwei Möglichkeiten zum Versenden

| | [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) | [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) |
| --- | --- | --- |
| **Kampagnen-ID** | Optional. Bitte lassen Sie dieses Feld leer, um ohne Tracking im Dashboard zu senden, oder geben Sie in jeder Nachricht `message_variation_id`eine API-Kampagnen-ID an, um das Tracking im Dashboard zu ermöglichen. | Erforderlich. |
| **Nachrichteninhalt** | Bitte fügen Sie ein`messages`Objekt in die Anfrage ein (zum Beispiel,`messages.whats_app` `messages.email`). | Nicht akzeptiert. Der Inhalt der Nachricht wird in der Kampagne im Braze-Dashboard definiert. |
| **Anwendungsfall** | Bitte senden Sie eine Nachricht, deren Inhalt vollständig in der API-Anfrage angegeben ist. | Triggern Sie eine vorgefertigte Kampagne (Inhalt im Dashboard) an bestimmte Empfänger:innen über die API. |

Ausführliche Informationen zu Anfragen und Antworten finden Sie in den Referenzen [„Nachrichten sofort senden (nur API)]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)“ und [„Kampagnen über API-gesteuerte ]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)Zustellungsendpunkte [senden]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)“.

---

## Option 1: Bitte senden Sie mit dem Inhalt der Nachricht in der Anfrage.`/messages/send`

Verwenden Sie diesen Endpunkt, wenn Sie den vollständigen Inhalt der Nachricht in der API-Anfrage angeben möchten. **Bitte** fügen Sie ein`messages`Objekt ein (zum Beispiel ,`messages.whats_app` `messages.email`, oder `messages.sms`). Sie können das Senden ohne `campaign_id`Kampagnen-Tracking auslassen oder eine API-Kampagnen-ID und`message_variation_id`in jede Nachricht einfügen, um die Sendungen im Dashboard zu verfolgen (weitere Informationen finden Sie in der [Endpunkt-Referenz]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)).

**Erforderlich:** API-Schlüssel mit der entsprechenden`messages.send` Berechtigung.

{% alert important %}
Jeder Empfänger:in in `external_user_ids`Braze muss bereits vorhanden sein. Um Nutzer:innen im Rahmen eines Versands zu erstellen, verwenden Sie bitte zunächst[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) [Option 1](#option-2-trigger-a-campaign-with-content-in-the-dashboard-campaignstriggersend) oder alternativ [Option 2](#option-2-trigger-a-campaign-with-content-in-the-dashboard-campaignstriggersend) (API-gesteuerte Kampagne).
{% endalert %}

### Beispiel: WhatsApp-Template-Nachricht

```
POST YOUR_REST_ENDPOINT/messages/send
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "external_user_ids": ["user123"],
  "messages": {
    "whats_app": {
      "app_id": "YOUR_APP_ID",
      "subscription_group_id": "YOUR_WHATSAPP_SUBSCRIPTION_GROUP_ID",
      "message_type": "template_message",
      "message": {
        "template_name": "new_message_received",
        "template_language_code": "en_US"
      }
    }
  }
}
```

Die vollständige Spezifikation des WhatsApp-Objekts finden Sie unter [WhatsApp-Objekt]({{site.baseurl}}/api/objects_filters/messaging/whats_app_object/).

{% alert note %}
Der`/messages/send`Endpunkt unterstützt ausschließlich WhatsApp-Templates mit TEXT- oder IMAGE-Headern. Für die Header-Typen DOCUMENT, Video oder andere Medien verwenden Sie bitte den [API-gesteuerten Kampagnen-Endpunkt]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) oder das Braze-Dashboard.
{% endalert %}

### Beispiel: E-Mail

```json
{
  "external_user_ids": ["user123"],
  "messages": {
    "email": {
      "app_id": "YOUR_APP_ID",
      "subject": "Your order has shipped",
      "from": "no-reply@example.com",
      "body": "<p>Your order #12345 is on its way.</p>"
    }
  }
}
```

Für andere Kanäle, siehe [Messaging-Objekte]({{site.baseurl}}/api/objects_filters/#messaging-objects).

---

## Option 2: Triggern Sie eine Kampagne mit Inhalten im Dashboard.`/campaigns/trigger/send`

Bitte verwenden Sie diesen Endpunkt, wenn der Nachrichteninhalt im Braze-Dashboard erstellt wird (API-ausgelöste Kampagne). Sie senden ein **erforderliches**`campaign_id`  und Empfänger:innen; Sie senden **kein**  Objekt`messages`.

**Erforderlich:** API-Schlüssel mit der entsprechenden`campaigns.trigger.send` Berechtigung.

### Schritt 1: Erstellen Sie eine API-gesteuerte Kampagne

1. Bitte gehen Sie im Braze-Dashboard zu **„Messaging“** > **„Kampagnen**“.
2. Bitte wählen Sie **„Kampagne erstellen**“ und anschließend **„API-gesteuerte Kampagne“** (nicht „API-Kampagne“).
3. Fügen Sie Ihren Messaging-Kanal hinzu (WhatsApp, E-Mail, SMS usw.) und erstellen Sie den Inhalt der Nachrichten im Dashboard.
4. Bitte notieren Sie sich die **Kampagnen-ID** (und **die Sende-ID,** falls Sie mehrere Nachrichtenvarianten verwenden). Sie werden diese in der API-Anfrage verwenden.

Weitere Informationen zum Erstellen von API-gesteuerten Kampagnen finden Sie unter [API-gesteuerte Zustellung]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/).

### Schritt 2: Die Kampagne über die API triggern

Senden Sie eine POST-Anfrage an`/campaigns/trigger/send`mit`campaign_id`und`recipients`(oder `broadcast`/`audience`). Bitte fügen Sie kein Objekt`messages` ein – der Inhalt stammt aus der Kampagne.

```
POST YOUR_REST_ENDPOINT/campaigns/trigger/send
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "campaign_id": "YOUR_CAMPAIGN_ID",
  "recipients": [
    {
      "external_user_id": "user123"
    }
  ]
}
```

Den vollständigen Anfragetext (einschließlich `trigger_properties`, `send_to_existing_only`, `attributes`, usw.) finden Sie in der Referenz zum Endpunkt [„Kampagnen über API-gesteuerte Zustellung senden]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/#request-body)“.

---

## Bitte überprüfen Sie Ihre Integration.

1. Bitte senden Sie eine Anfrage über eine der oben genannten Optionen und geben Sie Ihre eigene ID als Empfänger:in an.
2. Bitte bestätigen Sie, dass die Nachricht zugestellt wurde.
3. Bei Verwendung von Option 2 überprüfen Sie bitte die Kampagne im Braze-Dashboard, um sicherzustellen, dass der Versand aufgezeichnet wurde.

## Überlegungen

- Nutzen Sie [die Features der Personalisierung]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/) von Braze, um Inhalte anzupassen, sofern dies unterstützt wird.
- Bitte stellen Sie sicher, dass Ihr Messaging den geltenden Vorschriften entspricht und die erforderlichen Abmeldeoptionen sowie Datenschutzhinweise enthält.
- Weitere Endpunkte (Zeitplan, Canvas-Trigger usw.) finden Sie unter [Messaging-Endpunkte]({{site.baseurl}}/api/endpoints/messaging/).
