---
nav_title: Link shortening
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

Link shortening allows you to automatically shorten URLs contained in SMS or RCS messages and collect click-through-rate analytics, providing additional engagement metrics to help understand how your users are engaging with your campaigns.

Link shortening can be turned on at the [message variant-level]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#step-1-create-your-campaign) in both campaigns and Canvases. When link shortening is turned on, clicks will generate an [SMS click event]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) sent through Currents.

Links are shortened using our shared short domain (`brz.ai`) or your custom link shortening domain, and are valid for 9 weeks from the date they were created. An example URL may look something like `https://brz.ai/8jshX2dj`. 

## Using link shortening

To use link shortening, make sure the link shortening checkbox in the message composer is selected.

{% tabs %}
{% tab SMS composer %}

![SMS message composer with a checkbox selected for link shortening.]({% image_buster /assets/img/link_shortening/shortening1.png %})

{% endtab %}
{% tab RCS composer %}

![RCS message composer with a checkbox selected for link shortening.]({% image_buster /assets/img/link_shortening/shortening1_rcs.png %})

{% endtab %}
{% endtabs %}

Braze recognizes only URLs that start with `http://` or `https://`. When a URL is recognized, the **Preview** section updates with a placeholder URL. Braze estimates the length of the message after shortening, but a warning prompts you to select a test user and save the message as a draft for a more accurate estimate.

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

We shorten URLs that are rendered by Liquid, even those included in API-trigger properties. For example, if {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} represents a valid URL, we shorten and track that URL before sending the message. 

### Shorten URLs in `/messages/send` endpoint

Link shortening is also turned on for API-only messages through the [`/messages/send` endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/). For a full list of request parameters, go to [request parameters]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/#request-parameters).

## Testing

Before launching your campaign or Canvas, it's best practice to preview and test your message first. To do so, go to the **Test** tab to preview and send an SMS or RCS message to [content test groups]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab#content-test-groups) or an individual user. 

This preview updates with relevant personalization and the shortened URL. The number of characters and [billable segments]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/) also update to reflect the rendered personalization and the shortened URL.

Make sure to save the campaign or Canvas before sending a test message to receive a representation of the shortened URL that is dispatched in your message. If the campaign or Canvas isn't saved before a test send, the test send includes a placeholder URL.

{% alert important %}
If a draft is created within an active Canvas, a shortened URL won't be generated. The actual shortened URL is generated when the Canvas draft is made active.
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

Yes. You can retarget users who have clicked URLs by using the [SMS retargeting filters]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/) or the SMS click events (`users.messages.sms.ShortLinkClick`) sent by Currents.

### Does link shortening work with deep links or universal links?

Link shortening doesn't work with deep links. Alternatively, you can shorten universal links from third-party providers such as Branch or Appsflyer, but users may experience a brief redirect or "flickering" effect. This occurs because the shortened link routes through the web first before resolving to the universal link that supports app opening. Additionally, Braze is unable to troubleshoot issues that may arise when shortening universal links, such as breaking the attribution or causing unexpected redirects.

{% alert note %}
Test the user experience before implementing link shortening with universal links to confirm it meets your expectations.
{% endalert %}

### Are `send_ids` associated with SMS click events?

No. However, you can generally attribute `send_ids` with click events by using [Query Builder]({{site.baseurl}}/query_builder/) to query Currents data with this query:

```sql
SELECT c.*, s.send_id
FROM USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED AS c
  INNER JOIN USERS_MESSAGES_SMS_SEND_SHARED AS s
    ON s.user_id = c.user_id 
      AND (s.message_variation_id = c.message_variation_id OR s.canvas_step_message_variation_id = c.canvas_step_message_variation_id)
WHERE s.send_id IS NOT NULL; 
```
