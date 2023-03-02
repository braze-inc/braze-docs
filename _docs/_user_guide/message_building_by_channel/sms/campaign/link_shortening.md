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

# Link Shortening

> Link shortening and click tracking allow you to automatically shorten URLs contained in SMS messages and collect click-through-rate analytics, providing additional engagement metrics to help understand how your users are engaging with your SMS campaigns. 

## Overview

Link shortening and click tracking can be enabled at the [message variant-level]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#step-1-create-your-campaign) in both campaigns and Canvases. 

{% alert important %}
Shortened links with advanced tracking are currently in early access. Contact your Braze customer success manager if you're interested in participating in the early access.
{% endalert %}

The length of the URL will be determined by the type of tracking that is enabled:
- **Basic tracking** enables campaign-level click tracking. Basic links will have a length of between 20-21 characters.
- **Advanced tracking** enables campaign-level and user-level click tracking. Links with advanced tracking are longer by up to 7 characters and allow you to create segments of users who have clicked on URLs. Advanced links will have a length of between 27-28 characters.

Links will be shortened using Braze's shared short domain ([brz.ai](http://brz.ai)). An example URL may look something like this: `https://brz.ai/8jshX` (basic) or `https://brz.ai/8jshX/2dj8d` (advanced). Refer to the [Testing](#testing) for more information.

Shortened URLs will be valid for one year from the date they were created.

### Enabling link shortening

To enable link shortening, ensure the link shortening toggle in the message composer is enabled. From there, choose whether to use Basic or Advanced by selecting the respective radial button. 

![][1]

For Braze to recognize URLs, they must start with _http://_ or _https://_. When a URL is recognized, the **Preview** pane will update with a placeholder URL. Braze will estimate the length of the URL after shortening, but a warning will prompt you to select a test user and save the message as a draft for a more accurate estimate.

![][3]

## Testing

We always recommend that you preview and test your message before launching a campaign or Canvas. 

Navigate to the **Test** tab to preview and send an SMS to [content test groups]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab#content-test-groups) or an individual user. The preview will update with relevant personalization and the shortened URL. The number of characters and [billable segments]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/) will also update to reflect the rendered personalization and the shortened URL. 

Make sure to save the campaign or Canvas before sending a test message to receive the shortened URL that will be dispatched in your message. If the campaign or Canvas is not saved before a test send, the test send will contain a placeholder URL.

![][2]

{% alert note %}
Liquid personalization and shortened URLs are templated on the **Test** tab after a user has been selected. Ensure a user is selected to receive an accurate character count!
{% endalert %}

## Click tracking

When link shortening is enabled, the SMS and MMS performance table include a column titled **Total Clicks** that shows a count of click events per variant and an associated click rate. For more details on SMS metrics, see [SMS message performance]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_campaign_analytics/#message-performance).

![][4]

The Historical Performance and SMS Overview chart also includes an option for  **Total Clicks** and shows a daily time series of click events.

## Retargeting Users

Retarget users who have clicked campaigns with advanced tracking links.
Only campaigns that have advanced tracking enabled will appear in the following dropdowns:

##### Retarget users who have clicked a specific SMS Campaign:
1. Create a segment using the **Clicked/Opened Campaign** filter.
2. Select **clicked sms**.
3. Choose the desired campaign.

![][5]

##### Retarget users who have clicked a specific Canvas Step:
1. Create a segment using the **Clicked/Opened Step** filter.
2. Select **clicked sms**.
3. Choose the desired Canvas and Canvas step.

![][6]

## Custom domains

Link shortening also allows you to use your own domain to personalize the look and feel of your shortened URLs, helping portray a consistent brand image.

{% alert note %}
Contact your Braze account manager if you are interested in getting started with Custom Domains.
{% endalert %}

Once configured, custom domains can be assigned to one or multiple SMS subscription groups. 

![Subscription groups settings that allow you to select a link-shortening domain.][7]

Campaigns sent with Link Shortening enabled will use the assigned domain associated with your SMS subscription group.

![][8]

## Frequently asked questions

### Link shortening

#### How long are the shortened URLs?

Shortened URLs will be between 20 and 21 characters long.

#### Does Link Shortening work with URLs that contain Liquid?

No. Currently, only static URLs are shortened.

#### Are the links I receive when test sending real URLs?

If the campaign has been saved as a draft before test sending, yes! Otherwise, it is a placeholder link. Note that the exact URL sent in a launched campaign may differ from the one sent via a test send.

#### Does the Braze SDK need to be installed in order to shorten links?

No, Link Shortening will work without any SDK integration.

#### Can I specify my own custom Link Shortening domain?

Not yet, though we plan to provide more customization options in the future.

#### Do I know which individual users are clicking on a URL?

Not yet. This will be part of a future user-level click tracking release.

#### Can I add UTM parameters to a URL before it is shortened?

Yes! Any static URL parameters can be added. 

#### How long do shortened URLs remain valid?

One year.

#### Will Link Shortening work with deep links or universal links?

Link shortening will shorten any static URLs that start with _http://_ or _https://_. However, it is not advised to further shorten generated universal links (from providers such as Branch or Appsflyer) as this may break the attribution or redirect of those tools.

### Custom domains

#### Can delegated domains be shared across multiple subscription groups?
Yes, a single domain can be used with multiple subscription groups. To do so, select the domain for each subscription group that it should be associated with.

#### Can delegated domains be shared across multiple app groups?
Yes, domains can be associated with subscription groups in multiple app groups, assuming the app groups are contained within the same company.

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

