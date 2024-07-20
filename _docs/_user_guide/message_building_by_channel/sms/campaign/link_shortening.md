---
nav_title: Link Shortening
article_title: Link Shortening
page_order: 5
description: "This reference article covers how to enable link shortening in your SMS messages and some frequently asked questions."
page_type: reference
alias: "/link_shortening/"
tool:
  - Campaigns
channel:
  - SMS
---

# Link shortening

> Link shortening and click tracking allow you to automatically shorten URLs contained in SMS messages and collect click-through-rate analytics, providing additional engagement metrics to help understand how your users are engaging with your SMS campaigns. 

## Overview

Link shortening and click tracking can be enabled at the [message variant-level]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#step-1-create-your-campaign) in both campaigns and Canvases. 

The length of the URL will be determined by the type of tracking that is enabled:
- **Basic tracking** enables campaign-level click tracking. Static URLs will have a length of 20 characters, and dynamic URLs will have a length of 25 characters.
- **Advanced tracking** enables campaign-level and user-level click tracking. Clicks will also generate an [SMS click event]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/) sent through Currents. Static URLs with advanced tracking will have a length of 27–28 characters, allowing you to create segments of users who have clicked on URLs. For dynamic URLs, they will have a length of 32–33 characters.

Links will be shortened using our shared short domain (`brz.ai`). An example URL may look something like this: `https://brz.ai/8jshX` (basic, static) or `https://brz.ai/8jshX/2dj8d` (advanced, dynamic). Refer to [Testing](#testing) for more information.

Static shortened URLs will be valid for one year from the date they were created. Shortened URLs that contain Liquid personalization will be valid for two months.

{% alert note %}
If you plan to use the Sage AI [Intelligent Channel filter]({{site.baseurl}}/user_guide/sage_ai/intelligence/intelligent_channel/) and want the SMS channel to be selectable, turn on SMS link shortening with advanced tracking and [click tracking]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/#click-tracking).
{% endalert %}

### Enabling link shortening

To enable link shortening, make sure the link shortening toggle in the message composer is enabled. From there, choose whether to use basic or advanced tracking by selecting the respective radial button. 

![]({% image_buster /assets/img/link_shortening/shortening1.png %})

For Braze to recognize URLs, they must start with _http://_ or _https://_. When a URL is recognized, the **Preview** pane will update with a placeholder URL. Braze will estimate the length of the URL after shortening, but a warning will prompt you to select a test user and save the message as a draft for a more accurate estimate.

![]({% image_buster /assets/img/link_shortening/shortening3.png %})

### Liquid personalization in URLs

You can dynamically construct your URL directly within the Braze composer, allowing you to add dynamic UTM parameters to your URLs or send users unique links (such as directing users to their abandoned cart or to a specific product that is back in stock).

#### Create a URL with supported Liquid personalization tags

URLs can be dynamically generated through the use of any [supported Liquid personalization tags]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

{% raw %}
```liquid
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

We also support the shortening of custom-defined Liquid variables. Several examples are shown below:

#### Create a URL using Liquid variables

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

#### Shorten URLs rendered by Liquid variables

We shorten URLs that are rendered by Liquid, even those included in API-trigger properties. For example, if {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} represents a valid URL, we will shorten and track that URL before sending out the SMS message. 

#### Shorten URLs in /messages/send

Link shortening is also enabled for API-only messages through the [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) endpoint. To also enable basic or advanced tracking, use the `link_shortening_enabled` or `user_click_tracking_enabled` request parameters.

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
|`link_shortening_enabled`| Optional | Boolean | Set `link_shortening_enabled` to `true` to turn on link shortening and campaign-level click tracking. To use tracking, a `campaign_id` and `message_variation_id` must be present.|
|`user_click_tracking_enabled`| Optional | Boolean | Set `user_click_tracking_enabled` to `true` to turn on link shortening, and campaign-level and user-level click tracking. You can use the tracked data to create segments of users who clicked URLs. To use tracking, a `campaign_id` and `message_variation_id` must be present. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

For a full list of request parameters, view [request parameters]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/#request-parameters).

## Testing

We always recommend that you preview and test your message before launching a campaign or Canvas. 

Navigate to the **Test** tab to preview and send an SMS to [content test groups]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab#content-test-groups) or an individual user. The preview will update with relevant personalization and the shortened URL. The number of characters and [billable segments]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/) will also update to reflect the rendered personalization and the shortened URL. 

Make sure to save the campaign or Canvas before sending a test message to receive a representation of the shortened URL that will be dispatched in your message. If the campaign or Canvas is not saved before a test send, the test send will contain a placeholder URL.

{% alert important %}
If a draft is created within an active Canvas, a shortened URL will not be generated. The actual shortened URL will be generated when the Canvas draft is made active.
{% endalert %}

![]({% image_buster /assets/img/link_shortening/shortening2.png %})

{% alert note %}
Liquid personalization and shortened URLs are templated in the **Test** tab after a user has been selected. Make sure a user is selected to receive an accurate character count.
{% endalert %}

## Click tracking

When link shortening is enabled, the SMS and MMS performance table include a column titled **Total Clicks** that shows a count of click events per variant and an associated click rate. For more details on SMS metrics, see [SMS message performance]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_campaign_analytics/#message-performance).

![]({% image_buster /assets/img/link_shortening/shortening4.png %})

The **Historical Performance** and **SMS/MMS Performance** charts also include an option for **Total Clicks** and show a daily time series of click events. Clicks are incremented on redirect (such as when a user visits a link), and may be incremented more than once per user.

## Retargeting users

For guidance on retargeting, visit [SMS retargeting]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/#filter-by-advanced-tracking-links).

## Custom domains

Link shortening also allows you to use your own domain to personalize the look and feel of your shortened URLs, helping portray a consistent brand image.

{% alert note %}
Contact your Braze account manager if you're interested in getting started with custom domains.
{% endalert %}

### Domain requirements

- Domains must be procured, owned, and managed by you.
- The domain used for this feature must be unique (that is, different from your website domain), and the domain can't be used to host any web content.
  - You can also use unique subdomains, such as `sms.braze.com`.
- We recommend choosing a domain with as few characters as possible to minimize the length of your URLs.

#### Delegating your custom domain

When you delegate your domain to Braze, we automatically handle the certificate renewal to prevent a lapse in service. 

To delegate your domain to Braze, do the following: 

1. Bring a domain that meets the above requirements to your customer success manager. Braze will then check the existing DNS configuration for the domain and confirm that:
- No CAA records exist OR
- CAA records *do* exist but have a record for {% raw %}`<any number> issue "letsencrypt.org"`{% endraw %} or {% raw %}`<anynumber> issuewild "letsencrypt.org"`{% endraw %}
2. Create four new A records, one for each IP, and confirm that they are the only A records that exist for the domain link host:
- 151.101.130.133
- 151.101.194.133
- 151.101.2.133
- 151.101.66.133

### Using custom domains

Once configured, custom domains can be assigned to one or multiple SMS subscription groups. 

![Subscription groups settings that allow you to select a link-shortening domain.]({% image_buster /assets/img/custom_domain.png %})

Campaigns sent with link shortening enabled will use the assigned domain associated with your SMS subscription group.

![]({% image_buster /assets/img/custom_domain2.png %})

## Frequently asked questions

### Link shortening

#### Are the links I receive when test sending real URLs?

If the campaign has been saved as a draft before test sending, yes. Otherwise, it is a placeholder link. Note that the exact URL sent in a launched campaign may differ from the one sent via a test send.

#### Does the Braze SDK need to be installed in order to shorten links?

No. Link shortening works without any SDK integration.

#### Do I know which individual users are clicking on a URL?

Yes. When Advanced Tracking is turned on, you can retarget users who have clicked URLs by leveraging the [SMS retargeting filters]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/) or the SMS click events (`users.messages.sms.ShortLinkClick`) sent via Currents.

#### Can I add UTM parameters to a URL before it is shortened?

Yes. Both static and dynamic parameters can be added. 

#### How long do shortened URLs remain valid?

Static URLs are valid for one year from the time of URL registration (such as first send).

Dynamic URs are valid for two months from the time of URL registration.

#### Will Link Shortening work with deep links or universal links?

Link shortening will shorten any static URLs that start with _http://_ or _https://_. However, it is not advised to further shorten generated universal links (from providers such as Branch or Appsflyer) as this may break the attribution or redirect of those tools.

### Custom domains

#### Can delegated domains be shared across multiple subscription groups?

Yes, a single domain can be used with multiple subscription groups. To do so, select the domain for each subscription group that it should be associated with.

#### Can delegated domains be shared across multiple workspaces?

Yes, domains can be associated with subscription groups in multiple workspaces, assuming the workspaces are contained within the same company.

[1]: {% image_buster /assets/img/link_shortening/shortening1.png %} 
[2]: {% image_buster /assets/img/link_shortening/shortening2.png %} 
[3]: {% image_buster /assets/img/link_shortening/shortening3.png %} 
[4]: {% image_buster /assets/img/link_shortening/shortening4.png %}
[5]: {% image_buster /assets/img/sms/retargeting5.png %} 
[6]: {% image_buster /assets/img/sms/retargeting4.png %}
[7]: {% image_buster /assets/img/custom_domain.png %} 
[8]: {% image_buster /assets/img/custom_domain2.png %} 
[11]: {% image_buster /assets/img/sms/link_shortening10.png %} 
[13]: {% image_buster /assets/img/link_shortening/shortening3.png %}   

