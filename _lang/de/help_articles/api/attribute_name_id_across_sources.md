---
nav_title: Unterschiede zwischen Kampagnen- und Canvas-Attributen in Braze
article_title: Unterschiede zwischen Kampagnen- und Canvas-Attributen in Braze
page_order: 1

page_type: reference
description: "Dieser Hilfeartikel vergleicht die Namen und IDs von Kampagnen und Canvas-Attributen in verschiedenen Quellen in Braze."
platform: API
---

# Wie sich Kampagnen- und Canvas-Attribute zwischen den Quellen in Braze unterscheiden

Die Namen und IDs von Kampagnen, Canvas und Canvas-Schritten sind alle in Liquid, unserer REST API und Currents verfügbar. Diese Attribute werden in allen drei Quellen auf denselben Wert abgebildet, können aber unterschiedlich benannt sein. Diese Seite soll Ihnen helfen, Verbindungen zwischen den drei Bereichen herzustellen.

## Anwendungsfälle

### Liquid

Kampagnen- und Canvas-Attribute sind als Liquid-Tags in unserem Dashboard {% raw %}(wie `{{campaign.${api_id}}}`){% endraw %} verfügbar. Sie können Liquid verwenden, um diese Attribute in der Nachricht selbst, in einem Connected-Content-Aufruf oder als Schlüssel-Wert-Paare zu übergeben. Dies geschieht in der Regel zu Tracking-Zwecken.

### REST API

Kampagnen- und Canvas-Attribute sind auch im [Endpunkt Kampagnendetails exportieren]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/) oder im [Endpunkt Canvas-Details exportieren]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/) verfügbar. Sie können unsere REST API verwenden, um Abbildungen zu erstellen, d.h. eine Liste aller Canvas-Namen und ihrer entsprechenden IDs.

### Currents

Kampagnen- und Canvas-Attribute sind mit [Nachrichten-Engagement-Ereignissen]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) von Currents verknüpft. Dies ist wichtig, damit Sie feststellen können, welcher Kampagne oder Canvas-Komponente eine Push-Sendung oder eine Öffnung einer E-Mail zuzuordnen ist.

## Attribute der Kampagne

| Attribut | Liquid | REST API | Currents |
| --- | --- | --- | --- |
| Kampagnenname | {% raw %}`{{campaign.${name}}}`{% endraw %} | `name` | `campaign_name` |
| Kampagnen-ID | {% raw %}`{{campaign.${api_id}}}`{% endraw %} | N/A (wird als Eingabe für den API-Aufruf selbst verwendet) | campaign_id |
| Variantenname | {% raw %}`{{campaign.${message_name}}}`{% endraw %} | `messages.message_variation_id.name` | N/A (Abbildung des Namens der Variante auf die ID der Variante mit Hilfe des Endpunkts Details der Kampagne exportieren) |
| Varianten-ID | {% raw %}`{{campaign.${message_api_id}}}`{% endraw %} | `messages.message_variation_id` | `message_variation_api_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Canvas Attribute

| Attribut | Liquid | REST API | Currents |
| --- | --- | --- | --- |
| Canvas-Name | {% raw %}`{{canvas.${name}}}`{% endraw %} | `name` | `canvas_name` |
| Canvas-ID | {% raw %}`{{canvas.${api_id}}}`{% endraw %} | N/A (wird als Eingabe für den API-Aufruf selbst verwendet) | canvas_id |
| Variantenname | {% raw %}`{{canvas.${variant_name}}}`{% endraw %} | `variants.name` | `canvas_variation_name` |
| Varianten-ID | {% raw %}`{{canvas.${variant_api_id}}}`{% endraw %} | `variants.name.id` | `canvas_variation_id` |
| Schrittname | {% raw %}`{{campaign.${name}}}`{% endraw %} | `steps.name` | `canvas_step_name` |
| Schritt-ID | {% raw %}`{{campaign.${api_id}}}`{% endraw %} | `steps.id` | `canvas_step_id` |
| Messaging-Kanal | -- | `steps.messages.message_variation_id.channel` | N/A (abhängig vom Ereignistyp, z. B. Push-Senden oder Öffnen einer E-Mail) |
| Nachrichten-ID | {% raw %}`{{campaign.${message_api_id}}}`{% endraw %} | `steps.message.message_variation_id` | `canvas_step_message_variation_api_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }