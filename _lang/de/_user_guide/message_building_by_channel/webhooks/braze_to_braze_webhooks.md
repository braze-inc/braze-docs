---
nav_title: Erstellen Sie einen Braze-to-Braze-Webhook.
article_title: Erstellen Sie einen Braze-to-Braze-Webhook
page_order: 3
channel:
  - webhooks
description: "Dieser Referenzartikel behandelt, wann User Update und wann Braze-to-Braze-Webhooks verwendet werden sollten und wie ein Braze-to-Braze-Webhook erstellt wird."

---

# Erstellen Sie einen Braze-to-Braze-Webhook.

> Mit Braze-to-Braze-Webhooks können Sie die [Braze-REST-API]({{site.baseurl}}/api/basics/) aus Braze heraus über einen [Webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) in einer [Kampagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/) oder [einem Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/) aufrufen. Verwenden Sie dies für Aufgaben der Orchestrierung wie das Triggern eines [API-gesteuerten Canvases]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/). Um [Benutzerattribute]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/), [angepasste Events]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) oder [Käufe]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/) aus Canvas zu aktualisieren, verwenden Sie bitte [die Benutzeraktualisierung]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/). Es wurde für Änderungen an Nutzerprofilen entwickelt und verarbeitet Updates effizienter.

Um diesen Artikel optimal nutzen zu können, sollten Sie mit [der Funktionsweise von Webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/) vertraut sein und wissen, wie man [einen Webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) in Braze [erstellt]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).

## Verwenden Sie das Benutzer-Update für Änderungen an Nutzerdaten.

Um Benutzerprofile innerhalb eines Canvas zu aktualisieren, einschließlich der Änderung [benutzerdefinierter Attribute]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/), der Aufzeichnung [benutzerdefinierter Ereignisse]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) oder der Aufzeichnung [von Käufen]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/), verwenden Sie [bitte die Benutzeraktualisierung]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) anstelle eines Braze-to-Braze-Webhooks. 

User Update fasst mehrere Änderungen zusammen und sendet sie in Stapeln, wodurch es schneller als Webhooks ist. Die Einrichtung ist einfacher als bei einem Webhook und es unterstützt komplexe Updates durch seinen [erweiterten JSON-Composer]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/#advanced-json-composer). Um beispielsweise zu erfassen, wie oft eine Nutzer:in eine Nachricht gesehen hat, verwenden Sie bitte [das Inkrement- und Dekrement-Feature]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/#increasing-and-decreasing-values) von User Update anstelle eines Braze-to-Braze-Webhooks.

{% alert tip %}
Fügen Sie [„Benutzer-Update“]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) zu Ihrem Canvas hinzu, um die Attribute, Ereignisse und Käufe einer Nutzer:in mithilfe eines JSON-Composers zu aktualisieren.
{% endalert %}

## Wann sollte ein Braze-to-Braze-Webhook verwendet werden?

User Update kann nahezu alle Aufgaben übernehmen, die auch ein Braze-to-Braze-Webhook zur Aktualisierung von Nutzerprofilen ausführt. Für komplexe Updates, die über einfache angepasste Attribute hinausgehen, können Sie den [erweiterten JSON-Composer]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/#advanced-json-composer) verwenden.

Sie können einen Braze-to-Braze-Webhook verwenden, wenn Sie [die REST API]({{site.baseurl}}/api/basics/) von Braze aus Braze heraus für andere Szenarien als direkte Updates der Nutzer:innen aus Canvas-Schritten aufrufen müssen. Häufige Beispiele sind:

- Triggern eines [API-gesteuerten Canvases]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) aus einem anderen Canvas heraus
- Aufruf anderer [Messaging-Endpunkte]({{site.baseurl}}/api/endpoints/messaging/) für Muster der Orchestrierung, bei denen ein Workflow in Braze eine API aufrufen muss, die keine dedizierte Canvas-Komponente hat.

Für Updates für Nutzer:innen innerhalb von Canvas wird die Verwendung von [„User Update“]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) empfohlen.

## Voraussetzungen

Um einen Braze-to-Braze-Webhook zu erstellen, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/api_key/) mit Berechtigungen für den Endpunkt, den Sie erreichen möchten. Um beispielsweise ein API-gesteuertes Canvas zu triggern, benötigen Sie einen API-Schlüssel mit der entsprechenden`canvas.trigger.send` Berechtigung.

## Einrichten Ihres Braze-to-Braze Webhooks

Der allgemeine Arbeitsablauf zum Erstellen eines Braze-to-Braze-Webhooks umfasst die folgenden Schritte:

1. [Erstellen Sie einen Webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) als Kampagne oder Canvas-Komponente. 
2. Wählen Sie **Leere Vorlage**.
3. Geben Sie auf dem Tab **„Erstellen“** die **Webhook-URL** und **den Body der Anfrage** für Ihren API-Anwendungsfall an.
4. Bitte geben Sie auf dem Tab **„Einstellungen“** die **HTTP-Methode** und **die Anfrage-Header** gemäß den Anforderungen des Endpunkts an.
5. Bitte konfigurieren Sie alle zusätzlichen Einstellungen für die Zustellung (z. B. Triggern durch ein angepasstes Event) und erstellen Sie den Rest Ihrer Kampagne oder Ihres Canvas.

## Triggern Sie ein zweites Canvas von einem ersten Canvas aus

In diesem Anwendungsfall erstellen Sie zwei Canvases und verwenden einen Braze-to-Braze-Webhook, um das zweite Canvas aus dem ersten heraus zu triggern. Dies wirkt wie ein Entry-Trigger, wenn ein:e Nutzer:in einem anderen Canvas einen bestimmten Punkt erreicht.

1. Beginnen Sie mit der Erstellung Ihres zweiten Canvas - das Canvas, das durch Ihr erstes Canvas ausgelöst werden soll.
2. Wählen Sie für den **Canvas-Eingabezeitplan** die Option **API-gesteuert**.
3. Notieren Sie sich Ihre **Canvas-ID**. Sie benötigen dies in einem späteren Schritt.
4. Fahren Sie mit dem Aufbau der Schritte Ihres zweiten Canvas fort und speichern Sie das Canvas.
5. Erstellen Sie schließlich Ihr erstes Canvas. Suchen Sie den Schritt, in dem Sie das zweite Canvas auslösen möchten, und erstellen Sie einen neuen Schritt mit einem Webhook.

Referenzieren Sie bei der Konfiguration Ihres Webhooks auf die folgenden Punkte:

- **Webhook-URL:** Ihre [REST-Endpunkt-URL]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/), gefolgt von `/canvas/trigger/send`. Für die Instanz `US-06` würde die URL beispielsweise `https://rest.iad-06.braze.com/canvas/trigger/send` lauten.
- **Anfragetext:** Rohtext

#### Kopfzeilen der Anfrage und Methode

Braze erfordert einen HTTP-Header für die Autorisierung, der Ihren API-Schlüssel enthält, sowie einen weiteren, der Ihren Content-Typ angibt.

- **Anfrage-Header:**
  - **Genehmigung:** `Bearer YOUR_API_KEY`
  - **Content-Typ:** `application/json`
- **HTTP-Methode:** `POST`

Ersetzen Sie `YOUR_API_KEY`dies bitte durch einen Braze-API-Schlüssel, der über`canvas.trigger.send`die erforderlichen Berechtigungen verfügt. Sie können einen API-Schlüssel im Braze-Dashboard erstellen, indem Sie zu **„Einstellungen“** > **„API-Schlüssel“** navigieren.

![Anfrage-Header für den Webhook, die die Felder „Authorization“ und „Content-Typ“ im Braze-Dashboard anzeigen.]({% image_buster /assets/img_archive/webhook_settings.png %}){: style="max-width:70%;"}

#### Anfragetext

Fügen Sie Ihre `/canvas/trigger/send` Anfrage in das Textfeld ein. Weitere Informationen finden Sie unter [Senden von Canvas-Nachrichten über API-gesteuerte Zustellung]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/). Nachfolgend sehen Sie ein Beispiel für den Textkörper der Anfrage für diesen Endpunkt, wobei `your_canvas_id` die Canvas-ID Ihres zweiten Canvas ist:

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

Wenn ein Nutzer diesen Webhook-Schritt im ersten Canvas erreicht, triggert Braze über die API den zweiten Canvas für diesen Nutzer.

## Überlegungen

- **Update für Nutzer:innen:** Für die Aktualisierung von Nutzerprofilen aus Canvas (Attribute, Ereignisse, Käufe) empfehlen wir die Verwendung von [User Update]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) anstelle von Braze-to-Braze-Webhooks, um eine höhere Effizienz und Kosteneffektivität zu erzielen.
- Braze-to-Braze-Webhooks unterliegen Endpunkt[-Rate-Limits]({{site.baseurl}}/api/api_limits/).
- Aktualisierungen des Nutzerprofils verursachen [Datenpunkte]({{site.baseurl}}/user_guide/data/data_points/), die zu Ihrem Gesamtverbrauch zählen, während das Triggern einer weiteren Nachricht über die Messaging-Endpunkte dies nicht tut.
- Um [anonyme Nutzer:innen]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#anonymous-user-profiles) anzusprechen, verwenden Sie bitte`braze_id`  anstelle von`external_id`  im Request-Body Ihres Webhooks.
- Sie können Ihren Braze-to-Braze-Webhook als [Webhook-Template]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/webhook_template/) speichern, um ihn wiederzuverwenden.
- Sie können das [Nachrichten-Aktivitätsprotokoll]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) überprüfen, um Webhook-Fehler anzuzeigen und zu beheben.


