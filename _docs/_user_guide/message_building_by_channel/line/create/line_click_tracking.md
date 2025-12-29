---
nav_title: LINE click tracking
article_title: LINE Click Tracking
page_order: 2
description: "This page covers how to turn on click tracking in your LINE messages, test shortened links, use your custom domain in tracked links, and more."
page_type: reference
alias: /line/click_tracking/
channel:
 - LINE
---

# LINE click tracking

> This page covers how to turn on click tracking in your LINE messages, test shortened links, use your custom domain in tracked links, and more.


When LINE click tracking is turned on, Braze automatically shortens your URLs, adds tracking mechanisms, and records clicks in real time. While LINE offers you aggregate click data, Braze provides granular user information that is timely and actionable. This data empowers you to create more targeted segmentation and retargeting strategies, such as segmenting users based on click behavior and triggering messages in response to specific clicks.

LINE click tracking can be used for text, rich, and card-based messages. It supports links within buttons and image-mapped areas that have a URL as an on-click action. You can also personalize URLs using Liquid and custom domains.

## How it works

You can manage LINE click tracking settings in the **Settings** tab while composing a message. When turned on, URLs will be shortened using the default Braze domain (`https://brz.ai`) or the custom domain specified for the subscription group, and personalized for the user.

Any URLs that start with `http://` or `https://` will be shortened. You can have up to 25 URLs in a message. Shortened URLs that contain Liquid personalization (such as user-level tracking or UTM parameters) will be valid for two months.

## Setting up click tracking

### Text messages

To set up click tracking for a text message:

1. Drag a **Text** message into the composer and add a URL to the text field.

![LINE message composer with a Text message containing a long URL: https://braze.com/docs/user_guide/message_building_by_channel/line/create/]({% image_buster /assets/img/line/click_tracking_text_message.png %})

{: start="2"}
2. Go to the **Settings** tab and confirm **Click Tracking** is turned on. Click tracking is turned on by default for all new messages.

{% alert note %}
You can view previews of the shortened link while in the **Settings** or **Preview & Test** tab. The full link will display in the composer while you build your message.
{% endalert %}

![LINE message composer "Settings" tab with " with "Click Tracking" toggled on and a preview Text message containing a shortened URL: https://olaf.brz.ai/p/9rcfdqdD]({% image_buster /assets/img/line/click_tracking_settings.png %})

### Rich messages

To set up click tracking for a rich message:

1. Drag a **Rich message** into the composer and select a template.
2. Select **URI** for the **On-click behavior** for the applicable tappable area.
3. Enter a URL into the **Open URL** field.

![LINE message composer with a Rich message with two tappable areas that each have a URL.]({% image_buster /assets/img/line/rich_message_click_tracking.png %})

{: start="4"}
4. Go to the **Settings** tab and confirm **Click Tracking** is turned on. Click tracking is turned on by default for all new messages.

### Card-based messages

To set up click tracking for a card-based message:

1. Drag a **Card-based message** into the composer.
2. Select **URI** for the **On-click behavior** for the applicable card or button areas.

![LINE message composer with a card-based message with two buttons that each have a URL.]({% image_buster /assets/img/line/card_based_message_click_tracking.png %})

{: start="3"}
3. Go to the **Settings** tab and confirm **Click Tracking** is turned on. Click tracking is turned on by default for all new messages.

{% alert note %}
URLs in the **Title** or **Description** fields will not be shortened because these fields aren't clickable within LINE.
{% endalert %}

## Custom domains

LINE click tracking allows you to use your own domain to personalize the look and feel of your shortened URLs, helping portray a consistent brand image. For more information, refer to [Custom domains]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/custom_domains).

## Liquid personalization in URLs

You can dynamically construct your URL directly within the Braze composer, allowing you to add dynamic UTM parameters to your URLs or send users unique links (such as directing users to their abandoned cart or to a specific product that is back in stock).
URLs can be dynamically generated through the use of any supported Liquid personalization tags.

{% raw %}
```
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

You can also shorten custom-defined Liquid variables, as shown in the following example:

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

## Shorten URLs rendered by Liquid variables

Braze shortens URLs that are rendered by Liquid, even those included in API-trigger properties. For example, if {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} represents a valid URL, we will shorten and track that URL before sending the LINE message.

## Testing

Before launching your campaign or Canvas, it’s best practice to preview and test your message first. To do so, go to the **Test** tab to preview and send a LINE message to content test groups or an individual user.

This preview will update with relevant personalization and the shortened URL. 

{% alert important %}
If a draft is created within an active Canvas, a shortened URL won’t be generated. The actual shortened URL is generated when the Canvas draft is made active.
{% endalert %}

## Reporting

The LINE performance table includes the column **Total Clicks** that shows a count of click events per variant and an associated click rate. For more details on LINE metrics, refer to [LINE message performance]({{site.baseurl}}/user_guide/message_building_by_channel/line/reporting).

![Performance for a LINE Canvas step.]({% image_buster /assets/img/line/line_step_performance.png %}){: style="max-width:30%;"}

Click data will be automatically reported in the analytics dashboard. 

![LINE performance analytics dashboard.]({% image_buster /assets/img/line/line_performance.png %})

## Retargeting users

You can retarget users who have clicked a URL in a LINE message by using the following segmentation filters and triggers:

- Action-based triggers
    - Interact with Campaign
    - Interact with Step

![LINE action-based delivery trigger.]({% image_buster /assets/img/line/line_action_based.png %})

- Segmentation filters
    - Clicked/Opened Campaign
    - Clicked/Opened Campaign or Canvas with Tag 
    - Clicked/Opened Step

![Filter group displaying all three segmentation filters: "Clicked/Opened Campaign", "Clicked/Opened Campaign or Canvas with Tag", and "Clicked/Opened Step".]({% image_buster /assets/img/line/line_segmentation_filters.png %})

## Frequently asked questions

### Are the links I receive when test sending real URLs?

Yes, real URLs will be generated when test sending. However, the exact URL sent in a launched campaign may differ from the one sent in a test send.

### Can I add UTM parameters to a URL before it is shortened?

Yes, both static and dynamic parameters can be added.

### How long do shortened URLs remain valid?

Personalized URLs are valid for two months from the time of URL registration.

### Does the Braze SDK need to be installed in order to shorten URLs?

No, click tracking works without any SDK integration.

### Do I know which individual users are clicking on a URL?

Yes. When click tracking is turned on, you can retarget users who have clicked URLs by using the [LINE retargeting filters](#retargeting-users).

### Does click tracking work with deep links or universal links?

Click tracking doesn’t work with deep links. You can shorten universal links from providers such as Branch or Appsflyer, but Braze is unable to troubleshoot issues that may arise in doing so (such as breaking the attribution or failing to redirect).

### Do previews on the LINE app count as clicks?

No, they do not contribute to the click rate for LINE messages.