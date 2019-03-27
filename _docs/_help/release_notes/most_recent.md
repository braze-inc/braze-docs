---
nav_title: Most Recent
page_order: 0
---

# Most Recent Braze Release Notes

_Braze releases information on it’s product updates on a monthly cadence. For more information on any of the updates listed in this section, reach out to your account manager or to [open a support ticket][support]._

## March 2019

### In-App Messages - Generation 3

Braze is proud to announce that we have made improvements to the look and feel of our in-app messages to adhere to the latest UX and UI best practices. In the newest in-app messages, you can expect your users to interact with messages with
- larger font sizes,
- refined spacing,
- a new close `x` asset,
- improved responsive behavior for all message types to better fit viewports of all sizes, and
- button borders to help you create custom contrasts between buttons.

Our [new in-app messages]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/overview/) will take your interactions with your user from good to app-mazing!

![Full-Screen Behavior]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

#### What You Need to Do

We highly recommend updating to the latest versions of the Braze SDKs for [Web]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#upgrading-the-sdk), [iOS]({{ site.baseurl }}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/initial_sdk_setup/), and [Android]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/).

After that, you're good to go!

### Content Blocks Archive Update

You can now archive and unarchive Content Blocks. Learn more in our main [Content Blocks documentation]({{ site.baseurl }}/user_guide/engagement_tools/templates_and_media/content_blocks/#archiving-content-blocks).

### Inkit Partner Addition

You can now use [Inkit]({{ site.baseurl }}/partners/inkit/) as a Predesigned Webhook Template or create a new Webhook Campaign.

### Google Cloud Storage

Google Cloud Storage is no longer in Beta! Braze is proud to announce that Google Cloud Storage is available to interested customers within the Braze platform. Go to __Technology Partners__ in your Braze account and search for Google Cloud Storage and [read more in our documentation]({{ site.baseurl }}/partners/technology_partners/data_and_infrastructure_agility/data_warehouses/google_cloud_storage_for_currents/).

## February 2019

### Email Subscription Groups

[Subscription Groups]({{ site.baseurl }}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups) are segment filters that can further narrow your audience from the [Global Subscription States]({{ site.baseurl }}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) above. These Groups offer the ability to present more granular subscription options to end users.

For example, if you send out multiple categories of email campaigns, you can offer your customers the option to subscribe or unsubscribe from those groups in bulk from a single page, using our [Email Preference Center](#email-preference-center).

Use the [Subscription Group REST APIs]({{ site.baseurl }}/developer_guide/rest_api/subscription_group_api/) to programmatically manage the subscription groups that you have stored on the Braze dashboard to the Subscription Group page.

### Email Preference Center

The [Email Preference Center]({{ site.baseurl }}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#email-preference-center) is an easy way to manage which users receive certain groups of newsletters. Each Subscription Group you create is added to the Preference Center list. Click on the name of the Preference Center to see an interactive preview.

## January 2019

Welcome to a new year!

### Push Time to Live (TTL)

In your account, within __Manage App Group__, click the [Push TTL Settings]({{ site.baseurl }}/user_guide/administrative/app_settings/push_ttl_settings/) tab to manage the time duration for attempted resends in the event that a device is offline.

### Connected Content IP Whitelisting

Braze is pleased to announce that due to a number of infrastructure upgrades made by our internal teams, we can now offer IP whitelisting for Connected Content on all clusters. In the future, we plan to add additional IPs for the non-EU clusters.

### Canvas Delay

We have added the option for any Canvas step to be sent __immediately__.

![Canvas Delay]({% image_buster /assets/img/canvas_delay_immediate.png %})

### Adjust (Technology Partner) REST Endpoint Field Update

With our updated integration with [Adjust]({{ site.baseurl }}/partners/adjust/), Braze customers will only need to add their rest endpoint from the Adjust partner spotlight page.

This will make it easier for customers wanting to pass attribution data into Braze.

[support]: {{ site.baseurl }}/support_contact/
