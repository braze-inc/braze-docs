---
nav_title: Differences between campaign and Canvas attributes in Braze
article_title: Differences between Campaign and Canvas Attributes in Braze
page_order: 1

page_type: reference
description: "This help article compares campaign and Canvas attribute name and IDs across sources in Braze."
platform: API
---

# How campaign and Canvas attributes differ across sources in Braze

Campaign, Canvas, and Canvas Step names and IDs are all available in Liquid, our REST API, and Currents. These attributes map to the same value across all three sources, but may be named differently. This page is meant to help you draw connections between the three.

## Use cases

### Liquid

Campaign and Canvas attributes are available as Liquid tags in our dashboard {% raw %}(such as `{{campaign.${api_id}}}`){% endraw %}. You can use Liquid to pass these attributes in the message itself, in a Connected Content call, or as key-value pairs. This is usually done for tracking purposes.

### REST API

Campaign and Canvas attributes are also available in the [Export campaign details endpoint]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/) or [Export Canvas details endpoint]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/). You can use our REST API to build mappings—that is, a list of all the Canvas names and their corresponding IDs.

### Currents

Campaign and Canvas attributes are tied to [message engagement events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) from Currents. This is important so that you can determine what campaign or Canvas component a push send or email open is associated with.

## Campaign attributes

| Attribute | Liquid | REST API | Currents |
| --- | --- | --- | --- |
| Campaign name | {% raw %}`{{campaign.${name}}}`{% endraw %} | `name` | `campaign_name` |
| Campaign ID | {% raw %}`{{campaign.${api_id}}}`{% endraw %} | N/A (used as an input for the API call itself) | campaign_id |
| Variant name | {% raw %}`{{campaign.${message_name}}}`{% endraw %} | `messages.message_variation_id.name` | N/A (map variant name to variant ID using the Export campaign details endpoint) |
| Variant ID | {% raw %}`{{campaign.${message_api_id}}}`{% endraw %} | `messages.message_variation_id` | `message_variation_api_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Canvas attributes

| Attribute | Liquid | REST API | Currents |
| --- | --- | --- | --- |
| Canvas name | {% raw %}`{{canvas.${name}}}`{% endraw %} | `name` | `canvas_name` |
| Canvas ID | {% raw %}`{{canvas.${api_id}}}`{% endraw %} | N/A (used as an input for the API call itself) | canvas_id |
| Variant name | {% raw %}`{{canvas.${variant_name}}}`{% endraw %} | `variants.name` | `canvas_variation_name` |
| Variant ID | {% raw %}`{{canvas.${variant_api_id}}}`{% endraw %} | `variants.name.id` | `canvas_variation_id` |
| Step name | {% raw %}`{{campaign.${name}}}`{% endraw %} | `steps.name` | `canvas_step_name` |
| Step ID | {% raw %}`{{campaign.${api_id}}}`{% endraw %} | `steps.id` | `canvas_step_id` |
| Message channel | N/A | `steps.messages.message_variation_id.channel` | N/A (inherent from event type, such as push send or email open) |
| Message ID | {% raw %}`{{campaign.${message_api_id}}}`{% endraw %} | `steps.message.message_variation_id` | `canvas_step_message_variation_api_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }