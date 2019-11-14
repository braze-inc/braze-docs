---
nav_title: Most Recent
page_order: 0
---

# Most Recent Braze Release Notes

_Braze releases information on it’s product updates on a monthly cadence. For more information on any of the updates listed in this section, reach out to your account manager or to [open a support ticket][support]. You can also check out [our SDK Changelogs]({{ site.baseurl }}/developer_guide/platform_integration_guides/sdk_changelogs/) to see more information on our monthly releases, updates, and improvements._

## October 2019

### Improved Canvas Variant Analytics

Canvas has new and improved analytics to view the performance of each of your variants. There are new metrics, especially around conversion events and confidence, and new capabilities like copying cells, API IDs, and downloading a `.csv` of the results. [Learn more here]({{ site.baseurl }}/user_guide/engagement_tools/canvas/get_started/measuring_and_testing_with_canvas_analytics/#performance-breakdown-by-variant).

### SMS

Braze now provides SMS with Campaigns, Canvas, and [Currents]({{ site.baseurl }}/partners/braze_currents/data_storage_events/message_engagement_events/)! Check out our [Set Up Guide]({{ site.baseurl }}/user_guide/onboarding_with_braze/sms_setup/) to get started and our [SMS Sending Guide]({{ site.baseurl }}/user_guide/message_building_by_channel/sms/) to learn more!

### Content Block Improvements

The API ID for a Content Block will now show on the selected Content Block page in the dashboard. Additionally, we will display where Content Blocks are being used.

### Alias-only User creation and Identification via the API

You can now [use an API request]({{ site.baseurl }}/api/endpoints/user_data/#user-attributes-object-specification) with any fields in the Attributes Object will create or update an attribute of that name with the given value on the specified user profile.

## September 2019

{% alert update %}
New September updates!
{% endalert %}

### Braze App within OneLogin

Customers will be able to simply search and select Braze within [OneLogin]({{ site.baseurl }}/user_guide/administrative/access_braze/single_sign_on/onelogin/) for SP or IdP Initiated login. This means that customers will not have to add a custom application within OneLogin. As a result, this should pre-populate certain settings like attributes which we have seen come up since launching SAML SSO.

### Rokt Calendar Partnership

[Rokt Calendar]({{ site.baseurl }}/partners/technology_partners/additional_channels/calendar/rokt_calendar/) provides Braze customers the ability to align their personalized marketing initiatives and extend personalized content to the end user's calendar. Thus, making it a more seamless experience for the end user and further develops stickiness with our customers' services. Customers will be able to...

- Send a calendar invite via Braze platform to 'save the date' and extend our communication
- Update an existing invite if the contents of the event has changed.

### Passkit Partnership

With [Passkit]({{ site.baseurl }}/partners/technology_partners/additional_channels/mobile_wallet/passkit/), Braze customers will be able to expand their customer engagement to mobile wallet. They will be able to personalized wallet campaigns while using Braze's powerful segmentation and orchestrate alongside channels like push, in-app messages, and more.

### Dispatch ID Value Return via Messaging Endpoints

A message's `dispatch_id` will be included in the following Messaging endpoint responses:

- [`/campaigns/trigger/send`]({{ site.baseurl }}/api/endpoints/messaging/#sending-messages-via-api-triggered-delivery)
- [`/campaigns/trigger/schedule`]({{ site.baseurl }}/api/endpoints/messaging/#create-schedule-endpoint)
- [`/messages/send`]({{ site.baseurl }}/api/endpoints/messaging/#sending-messages-immediately-via-api-only)
- [`/messages/schedule`]({{ site.baseurl }}/api/endpoints/messaging/#create-schedule-endpoint)
- [`/canvases/trigger/send`]({{ site.baseurl }}/api/endpoints/messaging/#canvas)
- [`/canvases/trigger/schedule`]({{ site.baseurl }}/api/endpoints/messaging/#api-triggered-canvases)

This way, customers who use transactional messaging can trace the call back through Currents.

### Canvas Changelogs

Did you even wonder more about the details of who is working on a Canvas in your account? Wonder no more! You can now access Canvas Changelogs.

![Canvas Changelogs]({% image_buster /assets/img/canvas-changelogs.gif %})


## August 2019

### Campaign Details in Reports

Your Campaign performance report will now list your campaign's details so you don't have to go back through your campaign to see which Delivery, Audience, or Conversion settings you chose while setting up your report.

![Campaign Details]({% image_buster /assets/img/campaign_details_update.png %})

### New Email Content Block API Endpoints

You can now manage ([create]({{ site.baseurl }}/api/endpoints/email_templates/#create-content-block), [list available]({{ site.baseurl }}/api/endpoints/email_templates/#list-available-content-blocks), [get information]({{ site.baseurl }}/api/endpoints/email_templates/#see-content-block-information)) your Email Content Blocks via API!

{% alert update %}
This feature is temporarily in limited availability. Please reach out to your Braze account manager for more information.
{% endalert %}

### Custom Email Unsubscribe Landing Page Update

The default [custom Email Unsubscribe page]({{ site.baseurl }}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#custom-unsubscribe-landing-page) has been updated with a sleek, more modern look.

### iOS SDK - Notched Phone Support Improvement

Improved support for in-app messages on “notched” devices (for example, iPhone X, Pixel 3XL). Full-screen messages now expand to fill the entire screen of any phone, while covering the status bar.

You won't see many updates in the Docs reflecting this change just yet - but they're on the way!



[support]: {{ site.baseurl }}/support_contact/
[CCFeed]: {% image_buster /assets/img/cc-feed.png %}
[cbm]: {% image_buster /assets/img/created_by_me2.png %}
[plat_p]: {% image_buster /assets/img/iam_platforms.gif %}
