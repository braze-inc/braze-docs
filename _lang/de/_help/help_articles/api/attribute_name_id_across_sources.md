---
nav_title: Unterschiede zwischen Kampagnen- und Canvas-Attributen in Braze
article_title: Unterschiede zwischen Kampagnen- und Canvas-Attributen in Braze
page_order: 1

page_type: reference
description: "Dieser Hilfeartikel vergleicht die Namen und IDs von Kampagnen- und Canvas-Attributen in verschiedenen Quellen in Braze."
platform: API
---

# Wie sich Kampagnen- und Canvas-Attribute zwischen den Quellen in Braze unterscheiden

Die Namen und IDs von Kampagnen, Canvas und Canvas-Schritten sind alle in Liquid, unserer REST-API und Currents verfügbar. Diese Attribute entsprechen in allen drei Quellen demselben Wert, können aber unterschiedlich benannt sein. Diese Seite soll Ihnen helfen, Verbindungen zwischen den drei Bereichen herzustellen.

## Anwendungsfälle

### Liquid

Kampagnen- und Canvas-Attribute sind als Liquid-Tags in unserem Dashboard {% raw %}(wie `{{campaign.${api_id}}}`){% endraw %} verfügbar. Sie können Liquid verwenden, um diese Attribute in der Nachricht selbst, in einem Aufruf von Connected Content oder als Schlüssel-Wert-Paare zu übergeben. Dies geschieht in der Regel zu Nachverfolgungszwecken.

### REST-API

Kampagnen- und Canvas-Attribute sind auch im [Endpunkt Kampagnendetails exportieren]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/) oder im [Endpunkt Canvas-Details exportieren]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/) verfügbar. Sie können unsere REST-API verwenden, um Mappings zu erstellen, d.h. eine Liste aller Canvas-Namen und ihrer entsprechenden IDs.

### Currents

Kampagnen- und Canvas-Attribute sind mit [Ereignissen]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events) aus Currents verknüpft. Dies ist wichtig, damit Sie feststellen können, mit welcher Kampagne oder Canvas-Komponente ein Push-Versand oder eine geöffnete E-Mail verbunden ist.

## Kampagnen-Attribute

| Attribut | Liquid | REST-API | Currents |
| --- | --- | --- | --- |
| Kampagnenname | {% raw %}`{{campaign.${name}}}`{% endraw %} | `name` | `campaign_name` |
| Kampagnen-ID | {% raw %}`{{campaign.${api_id}}}`{% endraw %} | N/A (wird als Eingabe für den API-Aufruf selbst verwendet) | kampagne_id |
| Name der Variante | {% raw %}`{{campaign.${message_name}}}`{% endraw %} | `messages.message_variation_id.name` | N/A (Zuordnung von Variantenname zu Varianten-ID über den Endpunkt Kampagnendetails exportieren) |
| Variante ID | {% raw %}`{{campaign.${message_api_id}}}`{% endraw %} | `messages.message_variation_id` | `message_variation_api_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Leinwand-Attribute

| Attribut | Liquid | REST-API | Currents |
| --- | --- | --- | --- |
| Canvas-Name | {% raw %}`{{canvas.${name}}}`{% endraw %} | `name` | `canvas_name` |
| Canvas-ID | {% raw %}`{{canvas.${api_id}}}`{% endraw %} | N/A (wird als Eingabe für den API-Aufruf selbst verwendet) | Leinwand_id |
| Name der Variante | {% raw %}`{{canvas.${variant_name}}}`{% endraw %} | `variants.name` | `canvas_variation_name` |
| Variante ID | {% raw %}`{{canvas.${variant_api_id}}}`{% endraw %} | `variants.name.id` | `canvas_variation_id` |
| Name des Schritts | {% raw %}`{{campaign.${name}}}`{% endraw %} | `steps.name` | `canvas_step_name` |
| Schritt-ID | {% raw %}`{{campaign.${api_id}}}`{% endraw %} | `steps.id` | `canvas_step_id` |
| Nachrichtenkanal | -- | `steps.messages.message_variation_id.channel` | N/A (vom Ereignistyp abhängig, z. B. Push-Sendung oder Öffnen einer E-Mail) |
| Nachrichten-ID | {% raw %}`{{campaign.${message_api_id}}}`{% endraw %} | `steps.message.message_variation_id` | `canvas_step_message_variation_api_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }