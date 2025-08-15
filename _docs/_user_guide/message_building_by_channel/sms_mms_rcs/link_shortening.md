---
nav_title: Link Shortening
article_title: Link Shortening
page_order: 3
description: "This reference article covers how to turn on link shortening in your SMS messages and some frequently asked questions."
page_type: reference
alias: "/link_shortening/"
tool:
  - Campaigns
channel:
  - SMS
  - MMS
  - RCS
---

# Link shortening

> This page covers how to turn on link shortening in your SMS and RCS messages, test shortened links, use your custom domain in shortened links, and more.

Link shortening and click tracking allow you to automatically shorten URLs contained in SMS or RCS messages and collect click-through-rate analytics, providing additional engagement metrics to help understand how your users are engaging with your campaigns.

Link shortening and click tracking can be turned on at the [message variant-level]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#step-1-create-your-campaign) in both campaigns and Canvases. 

The length of the URL is determined by the type of tracking that is turned on:
- **Basic tracking** enables campaign-level click tracking. Static URLs will have a length of 20 characters, and personalized URLs will have a length of 25 characters.
- **Advanced tracking** enables campaign-level and user-level click tracking, and enables use of segmentation and retargeting capabilities which rely on clicks. Clicks will also generate an [SMS click event]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) sent through Currents. Static URLs with advanced tracking will have a length of 27–28 characters, allowing you to create segments of users who have clicked on URLs. For personalized URLs, they will have a length of 32–33 characters.

Links will be shortened using our shared short domain (`brz.ai`). An example URL may look something like this: `https://brz.ai/8jshX` (basic, static) or `https://brz.ai/p/8jshX/2dj8d` (advanced, personalized). Refer to [Testing](#testing) for more information.

Any static URLs that start with `http://` or `https://` will be shortened. Static shortened URLs will be valid for one year from the date they were created. Shortened URLs that contain Liquid personalization will be valid for two months.

{% alert note %}
If you plan to use the BrazeAI<sup>TM</sup> [Intelligent Channel filter]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/) and want the SMS and RCS channels to be selectable, turn on link shortening with advanced tracking.
{% endalert %}

## Using link shortening

To use link shortening, make sure the link shortening toggle in the message composer is turned on. Then, choose to use either basic or advanced tracking.

![Message composer with a toggle for link shortening.]({% image_buster /assets/img/link_shortening/shortening1.png %})

Braze will only recognize URLs that start with `http://` or `https://`. When a URL is recognized, the **Preview** section updates with a placeholder URL. Braze will estimate the length of the URL after shortening, but a warning will prompt you to select a test user and save the message as a draft for a more accurate estimate.

![Message composer with a long URL in the "Message" box and a generated shortened link in the preview.]({% image_buster /assets/img/link_shortening/shortening3.png %})

### Adding UTM parameters

{% multi_lang_include analytics/click_tracking.md section='UTM parameters' %}

## Liquid personalization in URLs

You can dynamically construct your URL directly within the Braze composer, allowing you to add dynamic UTM parameters to your URLs or send users unique links (such as directing users to their abandoned cart or to a specific product that is back in stock).

### Create a URL with supported Liquid personalization tags

URLs can be dynamically generated through the use of any [supported Liquid personalization tags]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

{% raw %}
```liquid
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

We also support the shortening of custom-defined Liquid variables. Several examples are shown below:

### Create a URL using Liquid variables

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

### Shorten URLs rendered by Liquid variables

We shorten URLs that are rendered by Liquid, even those included in API-trigger properties. For example, if {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} represents a valid URL, we will shorten and track that URL before sending out the message. 

### Shorten URLs in /messages/send endpoint

Link shortening is also turned on for API-only messages through the [`/messages/send` endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/). To also turn on basic or advanced tracking, use the `link_shortening_enabled` or `user_click_tracking_enabled` request parameters.

| Parameter | Required | Data type | Description |
| --------- | ---------| --------- | ----------- |
|`link_shortening_enabled`| Optional | Boolean | Set `link_shortening_enabled` to `true` to turn on link shortening and campaign-level click tracking. To use tracking, a `campaign_id` and `message_variation_id` must be present.|
|`user_click_tracking_enabled`| Optional | Boolean | Set `user_click_tracking_enabled` to `true` to turn on link shortening, and campaign-level and user-level click tracking. You can use the tracked data to create segments of users who clicked URLs.<br><br> To use this parameter, `link_shortening_enabled` must be `true`, and a `campaign_id` and `message_variation_id` must be present. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

For a full list of request parameters, go to [request parameters]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/#request-parameters).

## Testing

Before launching your campaign or Canvas, it's best practice to preview and test your message first. To do so, go to the **Test** tab to preview and send an SMS or RCS message to [content test groups]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab#content-test-groups) or an individual user. 

This preview will update with relevant personalization and the shortened URL. The number of characters and [billable segments]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/) will also update to reflect the rendered personalization and the shortened URL. 

Make sure to save the campaign or Canvas before sending a test message to receive a representation of the shortened URL that will be dispatched in your message. If the campaign or Canvas isn't saved before a test send, the test send will include a placeholder URL.

{% alert important %}
If a draft is created within an active Canvas, a shortened URL won't be generated. The actual shortened URL generates when the Canvas draft is made active.
{% endalert %}

![Message "Test" tab with fields for selecting test recipients.]({% image_buster /assets/img/link_shortening/shortening2.png %})

{% alert note %}
Liquid personalization and shortened URLs are templated in the **Test** tab after a user has been selected. Make sure a user is selected to receive an accurate character count.
{% endalert %}

## Click tracking

When link shortening is turned on, the **SMS/MMS/RCS Performance** table includes a column titled **Total Clicks** that shows a count of click events per variant and an associated click rate. For more details on metrics, see [Message performance]({{site.baseurl}}/sms_mms_rcs_reporting/).

![SMS and MMS performance metrics table.]({% image_buster /assets/img/link_shortening/shortening4.png %})

The **Historical Performance** and **SMS/MMS/RCS Performance** tables also include an option for **Total Clicks** and show a daily time series of click events. Clicks are incremented on redirect (such as when a user visits a link), and may be incremented more than once per user.

## Retargeting users

For guidance on retargeting, visit [Retargeting]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/#filter-by-advanced-tracking-links).

{% multi_lang_include analytics/click_tracking.md section='Custom Domains' %}

{% multi_lang_include analytics/click_tracking.md section='Frequently Asked Questions' %}

### Do I know which individual users are clicking on a URL?

Yes. When **Advanced Tracking** is turned on, you can retarget users who have clicked URLs by leveraging the [SMS retargeting filters]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/) or the SMS click events (`users.messages.sms.ShortLinkClick`) sent by Currents.

{% alert note %}
At this time, RCS Click events are not available through Currents.
{% endalert %}

### Does link shortening work with deep links or universal links?

Link shortening doesn't work with deep links. Alternatively, you can shorten universal links from third-party providers such as Branch or Appsflyer, but users may experience a brief redirect or "flickering" effect. This occurs because the shortened link routes through the web first before resolving to the universal link that supports app opening. Additionally, Braze is unable to troubleshoot issues that may arise when shortening universal links, such as breaking the attribution or causing unexpected redirects.

{% alert note %}
Test the user experience before implementing link shortening with universal links to confirm it meets your expectations.
{% endalert %}

### Are `send_ids` associated with SMS click events?

No. However, if you have advanced tracking enabled, you can generally attribute `send_ids` with click events by using [Query Builder]({{site.baseurl}}/query_builder/) to query Currents data with this query:

```sql
SELECT c.*, s.send_id
FROM USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED AS c
  INNER JOIN USERS_MESSAGES_SMS_SEND_SHARED AS s
    ON s.user_id = c.user_id 
      AND (s.message_variation_id = c.message_variation_id OR s.canvas_step_message_variation_id = c.canvas_step_message_variation_id)
WHERE s.send_id IS NOT NULL; 
```