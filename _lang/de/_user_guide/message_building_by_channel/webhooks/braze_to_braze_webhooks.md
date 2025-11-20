---
nav_title: Erstellen eines Braze-to-Braze-Webhooks
article_title: Erstellen eines Braze-to-Braze-Webhooks
page_order: 3
channel:
  - webhooks
description: "Dieser Artikel beschreibt, wie Sie einen Braze-to-Braze-Webhook für wichtige Anwendungsfälle erstellen."

---

# Erstellen eines Braze-to-Braze-Webhooks

> Sie können Webhooks verwenden, um mit der Braze [REST API]({{site.baseurl}}/api/basics/) zu kommunizieren und im Wesentlichen alles zu tun, was unsere API Ihnen erlaubt. Wir referenzieren dies als Braze-to-Braze-Webhook – ein Webhook, der von Braze zu Braze kommuniziert. Die Anwendungsfälle auf dieser Seite setzen voraus, dass Sie mit der [Funktionsweise von Webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/) und der [Erstellung eines Webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) in Braze vertraut sind.

## Voraussetzungen

Um einen Braze-to-Braze-Webhook zu erstellen, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/api_key/) mit Berechtigungen für den Endpunkt, den Sie erreichen möchten.

## Einrichten Ihres Braze-to-Braze Webhooks

Während die Besonderheiten Ihrer Webhook-Anfrage von Anwendungsfall zu Anwendungsfall variieren, bleibt der allgemeine Workflow für die Erstellung eines Braze-to-Braze-Webhooks derselbe.

1. [Erstellen Sie einen Webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) als Kampagne oder Canvas-Komponente. 
2. Wählen Sie **Leere Vorlage**.
3. Geben Sie auf der Registerkarte **Verfassen** die **Webhook-URL** und den **Request Body** wie für Ihren Anwendungsfall angegeben an.
4. Geben Sie auf der Registerkarte **Einstellungen** die **HTTP-Methode** und die **Anfrage-Header** an, wie für Ihren Anwendungsfall vorgesehen.
5. Fahren Sie damit fort, den Rest Ihres Webhooks nach Bedarf einzurichten. Einige Anwendungsfälle erfordern spezielle Einstellungen für die Zustellung, z. B. das Triggern der Kampagne oder des Canvas durch ein angepasstes Event.

## Anwendungsfälle

Es gibt viele Möglichkeiten für Braze-to-Braze-Webhooks, aber hier sind einige Anwendungsfälle, die Ihnen den Einstieg erleichtern:

- Erhöht ein ganzzahliges angepasstes Attribut für einen Zähler, wenn ein:e Nutzer:in eine Nachricht erhält.
- Triggern Sie ein zweites Canvas von einem ersten Canvas aus.

{% alert tip %}
Fügen Sie Ihrem Canvas einen [Schritt zur Benutzeraktualisierung]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) hinzu, um die Attribute, Ereignisse und Käufe eines Benutzers in einem JSON-Composer zu verfolgen. Auf diese Weise werden diese Updates gebündelt, sodass Braze sie effizienter verarbeiten kann als ein Braze-to-Braze-Webhook.
{% endalert %}

### Anwendungsfall: Inkrementieren eines benutzerdefinierten Integer-Attributs für einen Zähler

In diesem Anwendungsfall erstellen Sie ein benutzerdefiniertes Attribut und verwenden Liquid, um zu zählen, wie oft eine bestimmte Aktion stattgefunden hat. 

Sie könnten zum Beispiel zählen, wie oft ein:e Nutzer:in eine aktive In-App-Nachricht-Kampagne gesehen hat, und verhindern, dass die Kampagne erneut an den oder die Nutzer:in gesendet wird, nachdem er oder sie sie dreimal gesehen hat. Weitere Ideen, was Sie mit Liquid-Logik in Braze tun können, finden Sie in unserer [Bibliothek für Liquid-Anwendungsfälle]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases).

Folgen Sie den allgemeinen Schritten zur Erstellung eines Braze-to-Braze-Webhooks und beachten Sie bei der Konfiguration Ihres Webhooks die folgenden Hinweise:

- **Webhook-URL:** Ihre [REST-Endpunkt-URL]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/), gefolgt von `/users/track`. Für die Instanz `US-06` würde die URL beispielsweise `https://rest.iad-06.braze.com/users/track` lauten.
- **Anfragetext:** Rohtext

#### Kopfzeilen der Anfrage und Methode

Braze benötigt für die Autorisierung einen HTTP-Header, der Ihren API-Schlüssel enthält, und einen weiteren, der Ihren `content-type` deklariert.

- **Anfrage-Header:**
  - **Autorisierung:** Bearer {YOUR_API_KEY}
  - **Content-Typ:** application/json
- **HTTP-Methode:** POST

Ersetzen Sie `YOUR_API_KEY` durch einen Braze API-Schlüssel mit `users.track` Berechtigungen. Sie können einen API-Schlüssel innerhalb des Braze-Dashboards unter **Einstellungen** > **API-Schlüssel** erstellen.

![Die Anfrage-Header für den Webhook.]({% image_buster /assets/img_archive/webhook_settings.png %}){: style="max-width:70%;"}

#### Anfragetext

Fügen Sie Ihren Nutzer-Tracking-Anfrage in den Anfragetext und den Liquid ein, um eine Zählervariable zuzuweisen. Weitere Einzelheiten finden Sie unter dem [Endpunkt`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).

Nachfolgend finden Sie ein Beispiel für das erforderliche Liquid und den Request Body für diesen Endpunkt, wobei `your_attribute_count` das Attribut ist, mit dem Sie zählen, wie oft ein Benutzer eine Nachricht gesehen hat:

{% raw %}
```json
{% assign new_number = {{custom_attribute.${your_attribute_count}}} | plus: 1 %}
{
    "attributes": [
        {
        "external_id": "{{${user_id}}}",
        "your_attribute_count": "{{new_number}}"
        }
    ]
}
```
{% endraw %}

{% alert note %}
Jedes Mal, wenn ein benutzerdefinierter Attributzähler aktualisiert (erhöht oder verringert) wird, verbraucht er einen [Datenpunkt]({{site.baseurl}}/user_guide/data/data_points/), der zu Ihrem Gesamtverbrauch zählt.
{% endalert %}

### Anwendungsfall: Triggern Sie ein zweites Canvas von einem ersten Canvas aus

Für diesen Anwendungsfall erstellen Sie zwei Canvases und verwenden einen Webhook, um das zweite Canvas vom ersten Canvas aus anzustoßen. Dies wirkt wie ein Entry-Trigger, wenn ein:e Nutzer:in einem anderen Canvas einen bestimmten Punkt erreicht.

1. Beginnen Sie mit der Erstellung Ihres zweiten Canvas - das Canvas, das durch Ihr erstes Canvas ausgelöst werden soll. 
2. Wählen Sie für den **Canvas-Eingabezeitplan** die Option **API-gesteuert**.
3. Notieren Sie sich Ihre **Canvas-ID**. Sie werden dies in einem späteren Schritt benötigen.
4. Fahren Sie mit dem Aufbau der Schritte Ihres zweiten Canvas fort und speichern Sie das Canvas.
5. Erstellen Sie schließlich Ihr erstes Canvas. Suchen Sie den Schritt, in dem Sie das zweite Canvas auslösen möchten, und erstellen Sie einen neuen Schritt mit einem Webhook. 

Referenzieren Sie bei der Konfiguration Ihres Webhooks auf die folgenden Punkte:

- **Webhook-URL:** Ihre [REST-Endpunkt-URL]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/), gefolgt von `canvas/trigger/send`. Für die US-06-Instanz würde die URL beispielsweise `https://rest.iad-06.braze.com/canvas/trigger/send` lauten.
- **Anfragetext:** Rohtext

#### Kopfzeilen der Anfrage und Methode

Braze benötigt für die Autorisierung einen HTTP-Header, der Ihren API-Schlüssel enthält, und einen weiteren, der Ihren `content-type` deklariert.

- **Anfrage-Header:**
  - **Autorisierung:** Bearer `YOUR_API_KEY`
  - **Content-Typ:** application/json
- **HTTP-Methode:** POST

Ersetzen Sie `YOUR_API_KEY` durch einen Braze API-Schlüssel mit `canvas.trigger.send` Berechtigungen. Sie können einen API-Schlüssel innerhalb des Braze-Dashboards unter **Einstellungen** > **API-Schlüssel** erstellen.

![Die Anfrage-Header für den Webhook.]({% image_buster /assets/img_archive/webhook_settings.png %}){: style="max-width:70%;"}

#### Anfragetext

Fügen Sie Ihre `canvas/trigger/send` Anfrage in das Textfeld ein. Weitere Einzelheiten finden Sie unter [Versenden von Canvas Nachrichten über eine API-getriggerte Zustellung]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/). Nachfolgend sehen Sie ein Beispiel für den Textkörper der Anfrage für diesen Endpunkt, wobei `your_canvas_id` die Canvas-ID Ihres zweiten Canvas ist: 

{% raw %}
```json
{
      "canvas_id": "your_canvas_id",
      "recipients": [
        {
          "external_user_id": "{{${user_id}}}"
         }
      ]
}
```
{% endraw %}

## Was Sie wissen sollten

- Braze-to-Braze-Webhooks unterliegen den [Rate-Limits]({{site.baseurl}}/api/api_limits/) für Endpunkte.
- Updates des Nutzerprofils führen zu zusätzlichen [Datenpunkten]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/#consumption-count), während das Triggern einer weiteren Nachricht über die Messaging-Endpunkte dies nicht tut.
- Wenn Sie [anonyme Nutzer:innen]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#anonymous-user-profiles) als Zielgruppe zusammenstellen möchten, können Sie `braze_id` anstelle von `external_id` im Textkörper der Anfrage Ihres Webhooks verwenden.
- Sie können Ihren Braze-to-Braze-Webhook als [Vorlage]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/webhook_template/) speichern, um ihn erneut zu verwenden.
- Sie können das [Nachrichten-Aktivitätsprotokoll]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) überprüfen, um Webhook-Fehler anzuzeigen und zu beheben.


