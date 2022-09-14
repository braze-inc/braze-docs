---
nav_title: Link Shortening
permalink: /user_guide/message_building_by_channel/sms/campaign/link_shortening/
hidden: true
---

# Link Shortening

> Link shortening and click tracking allow you to automatically shorten URLs contained in SMS messages and collect open-rate analytics, providing additional engagement metrics to help understand how your users are engaging with your SMS campaigns. 

{% alert important %}
Link Shortening is currently in early access. Please contact your Braze account manager if you are interested in participating in the early access.
{% endalert %}

## Overview

Link Shortening and click tracking can be enabled at the [message variant-level]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#step-1-create-your-campaign) in both campaigns and Canvases. Links will be shortened using Braze’s shared short domain ([brz.ai](http://brz.ai)) with a length of between 20-21 characters. An example URL may look something like this: `https://brz.ai/8jshX`

Shortened URLs will be valid for one year from the date they were created.

To enable Link Shortening, ensure the Link Shortening toggle in the message composer is enabled.

![][1]

For Braze to recognize URLs, they must start with _http://_ or _https://_. When a URL is recognized, the **Preview** pane will update with a placeholder URL. Note that the character count in the **Compose** tab excludes all personalization of link shortening.

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

When Link Shortening is enabled, the SMS and MMS performance table include a column titled **Total Clicks** that shows a count of click events per variant and an associated click rate. For more details on SMS metrics, see [SMS message performance]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_campaign_analytics/#message-performance).

![][4]

The Historical Performance and SMS Overview chart also includes an option for  **Total Clicks** and shows a daily time series of click events.

## Frequently asked questions

#### How long are the shortened URLs?

Shortened URLs will be between 20 and 21 characters long.

#### Does Link Shortening work with URLs that contain Liquid?

No. Currently, only static URLs are shortened.

#### Are the links I receive when test sending real URLs?

If the campaign has been saved as a draft before test sending, yes! Otherwise, it is a placeholder link. 

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

[1]: {% image_buster /assets/img/link_shortening/shortening1.png %} 
[2]: {% image_buster /assets/img/link_shortening/shortening2.png %} 
[3]: {% image_buster /assets/img/link_shortening/shortening3.png %} 
[4]: {% image_buster /assets/img/link_shortening/shortening4.png %} 
