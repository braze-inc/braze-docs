---
nav_title: Link Shortening
article_title: Link Shortening
page_order: 5
description: "This reference article covers how to turn on link shortening in your SMS messages and some frequently asked questions."
page_type: reference
alias: "/link_shortening/"
tool:
  - Campaigns
channel:
  - SMS
---

# Link shortening

> Link shortening and click tracking allow you to automatically shorten URLs contained in SMS messages and collect click-through-rate analytics, providing additional engagement metrics to help understand how your users are engaging with your SMS campaigns. <br><br> This page covers how to turn on link shortening in your SMS messages, test shortened links, use your custom domain in shortened links, and more.

Link shortening and click tracking can be turned on at the [message variant-level]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#step-1-create-your-campaign) in both campaigns and Canvases. 

The length of the URL is determined by the type of tracking that is turned on:
- **Basic tracking** enables campaign-level click tracking. Static URLs will have a length of 20 characters, and dynamic URLs will have a length of 25 characters.
- **Advanced tracking** enables campaign-level and user-level click tracking. Clicks will also generate an [SMS click event]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/) sent through Currents. Static URLs with advanced tracking will have a length of 27–28 characters, allowing you to create segments of users who have clicked on URLs. For dynamic URLs, they will have a length of 32–33 characters.

Links will be shortened using our shared short domain (`brz.ai`). An example URL may look something like this: `https://brz.ai/8jshX` (basic, static) or `https://brz.ai/8jshX/2dj8d` (advanced, dynamic). Refer to [Testing](#testing) for more information.

Any static URLs that start with `http://` or `https://` will be shortened. Static shortened URLs will be valid for one year from the date they were created. Shortened URLs that contain Liquid personalization will be valid for two months.

{% alert note %}
If you plan to use the BrazeAI<sup>TM</sup> [Intelligent Channel filter]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/) and want the SMS channel to be selectable, turn on SMS link shortening with advanced tracking and [click tracking]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/#click-tracking).
{% endalert %}

## Using link shortening

To use link shortening, make sure the link shortening toggle in the message composer is turned on. Then, choose to use either basic or advanced tracking.

![Message composer with a toggle for link shortening.][1]

Braze will only recognize URLs that start with `http://` or `https://`. When a URL is recognized, the **Preview** section updates with a placeholder URL. Braze will estimate the length of the URL after shortening, but a warning will prompt you to select a test user and save the message as a draft for a more accurate estimate.

![Message composer with a long URL in the "Message" box and a generated shortened link in the preview.][3]

### Adding UTM parameters

While link shortening allows you to track your URLs automatically, you can also add UTM parameters to your URLs to track the performance of campaigns in third-party analytics tools, such as Google Analytics.

To add UTM parameters to your URL, do the following:

1. Start with your base URL. This is the URL of the page you want to track (such as `https://www.example.com`).
2. Add a question mark (?) after your base URL.
3. Add each UTM parameter separated by an ampersand (&).

An example is `https://www.example.com?utm_source=newsletter&utm_medium=sms`.

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

We shorten URLs that are rendered by Liquid, even those included in API-trigger properties. For example, if {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} represents a valid URL, we will shorten and track that URL before sending out the SMS message. 

### Shorten URLs in /messages/send endpoint

Link shortening is also turned on for API-only messages through the [`/messages/send` endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/). To also turn on basic or advanced tracking, use the `link_shortening_enabled` or `user_click_tracking_enabled` request parameters.

| Parameter | Required | Data type | Description |
| --------- | ---------| --------- | ----------- |
|`link_shortening_enabled`| Optional | Boolean | Set `link_shortening_enabled` to `true` to turn on link shortening and campaign-level click tracking. To use tracking, a `campaign_id` and `message_variation_id` must be present.|
|`user_click_tracking_enabled`| Optional | Boolean | Set `user_click_tracking_enabled` to `true` to turn on link shortening, and campaign-level and user-level click tracking. You can use the tracked data to create segments of users who clicked URLs.<br><br> To use this parameter, `link_shortening_enabled` must be `true`, and a `campaign_id` and `message_variation_id` must be present. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

For a full list of request parameters, go to [request parameters]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/#request-parameters).

## Testing

Before launching your campaign or Canvas, it's best practice to preview and test your message first. To do so, go to the **Test** tab to preview and send an SMS to [content test groups]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab#content-test-groups) or an individual user. 

This preview will update with relevant personalization and the shortened URL. The number of characters and [billable segments]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/) will also update to reflect the rendered personalization and the shortened URL. 

Make sure to save the campaign or Canvas before sending a test message to receive a representation of the shortened URL that will be dispatched in your message. If the campaign or Canvas isn't saved before a test send, the test send will include a placeholder URL.

{% alert important %}
If a draft is created within an active Canvas, a shortened URL won't be generated. The actual shortened URL generates when the Canvas draft is made active.
{% endalert %}

![Message "Test" tab with fields for selecting test recipients.][2]

{% alert note %}
Liquid personalization and shortened URLs are templated in the **Test** tab after a user has been selected. Make sure a user is selected to receive an accurate character count.
{% endalert %}

## Click tracking

When link shortening is turned on, the SMS and MMS performance table include a column titled **Total Clicks** that shows a count of click events per variant and an associated click rate. For more details on SMS metrics, see [SMS message performance]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_campaign_analytics/#message-performance).

![SMS and MMS performance metrics table.][4]

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
- CAA records **do** exist but have a record for {% raw %}`<any number> issue "letsencrypt.org"`{% endraw %} or {% raw %}`<anynumber> issuewild "letsencrypt.org"`{% endraw %}

2. Create four new A records, one for each IP, and confirm that they are the only A records that exist for the domain link host:
- `151.101.130.133`
- `151.101.194.133`
- `151.101.2.133`
- `151.101.66.133`

### Using custom domains

Once configured, custom domains can be assigned to one or multiple SMS subscription groups. 

![Subscription groups settings that allow you to select a link-shortening domain.][7]

Campaigns sent with link shortening turned on will use the assigned domain associated with your SMS subscription group.

![SMS message composer preview with a shortened link domain that is different from the domain in the "Message" box.][8]

## Frequently asked questions

### Link shortening

#### Are the links I receive when test sending real URLs?

If the campaign has been saved as a draft before test sending, yes. Otherwise, it is a placeholder link. Note that the exact URL sent in a launched campaign may differ from the one sent in a test send.

#### Does the Braze SDK need to be installed in order to shorten links?

No. Link shortening works without any SDK integration.

#### Do I know which individual users are clicking on a URL?

Yes. When **Advanced Tracking** is turned on, you can retarget users who have clicked URLs by leveraging the [SMS retargeting filters]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/) or the SMS click events (`users.messages.sms.ShortLinkClick`) sent by Currents.

#### Can I add UTM parameters to a URL before it is shortened?

Yes. Both static and dynamic parameters can be added. 

#### How long do shortened URLs remain valid?

Static URLs are valid for one year from the time of URL registration, such as first send. Dynamic URLs are valid for two months from the time of URL registration.

#### Does link shortening work with deep links or universal links?

Link shortening doesn't work with deep links. You can shorten universal links from providers such as Branch or Appsflyer, but Braze is unable to troubleshoot issues that may arise in doing so (such as breaking the attribution or causing a redirect).

### Custom domains

#### Can delegated domains be shared across multiple subscription groups?

Yes. A single domain can be used with multiple subscription groups. To do so, select the domain for each subscription group that it should be associated with.

#### Can delegated domains be shared across multiple workspaces?

Yes. Domains can be associated with subscription groups in multiple workspaces, assuming the workspaces are contained within the same company.

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

