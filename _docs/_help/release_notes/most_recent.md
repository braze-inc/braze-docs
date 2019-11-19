---
nav_title: Most Recent
page_order: 0
---

# Most Recent Braze Release Notes

_Braze releases information on it’s product updates on a monthly cadence. For more information on any of the updates listed in this section, reach out to your account manager or to [open a support ticket][support]. You can also check out [our SDK Changelogs]({{ site.baseurl }}/developer_guide/platform_integration_guides/sdk_changelogs/) to see more information on our monthly releases, updates, and improvements._


## November 2019

More to come! Check back later this month for more updates!

### Intelligence Suite

Braze's [Intelligence Suite]({{ site.baseurl }}/user_guide/intelligence/) helps you automate decision-making with data-based insights. From delivery time to multivariate testing, brands can use these tools and features to create dynamic, cross-channel experiences that optimize at scale. <br> <br> The Intelligence Suite comprises of three main features: [Intelligent Timing]({{ site.baseurl }}/user_guide/intelligence/intelligent_timing/), [Intelligent Channel]({{ site.baseurl }}/user_guide/intelligence/intelligent_channel/), and [Intelligent Selection]({{ site.baseurl }}/user_guide/intelligence/intelligent_selection/).

{% alert note %}
The "Intelligence Suite" is a revision and grouping of features previously known as "Most Engaged Channel", "Intelligent Delivery", and "multivariate and A/B testing".
{% endalert %}

### Dark Mode Themes for In-App Messages

iOS 13 and Android 10 both introduced settings that allowed mobile phones to change their color themes to a "Dark Mode". Aligning with this feature, Braze has introduced [Dark Mode for in-app messages]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/dark-mode/)! This feature allows you to create in-app messages with a "light" and a "dark theme". If a device you send to has "Dark Mode" activated, the message will display your selected Dark Mode Theme.

<img src="{% image_buster /assets/img_archive/iam-dark-mode.gif %}" style="width:100%;max-width:800px;" />

### SMS Metrics in Engagement Reports

SMS Metrics are now available in [Engagement Reports]({{ site.baseurl }}/user_guide/data_and_analytics/your_reports/engagement_reports/)!

### Delete a Braze User's Teams

You can now delete a team from a Braze User's account!

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


[support]: {{ site.baseurl }}/support_contact/
[CCFeed]: {% image_buster /assets/img/cc-feed.png %}
[cbm]: {% image_buster /assets/img/created_by_me2.png %}
[plat_p]: {% image_buster /assets/img/iam_platforms.gif %}
