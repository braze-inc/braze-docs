---
nav_title: Most Recent
page_order: 0
---

# Most Recent Braze Release Notes

_Braze releases information on it’s product updates on a monthly cadence. For more information on any of the updates listed in this section, reach out to your account manager or to [open a support ticket][support]._

## April 2019

### New Currents Events & Fields

In addition to some corrections to the section, a new [Subscription Event]({{ site.baseurl}}/partners/braze_currents/data_storage_events/message_engagement_events/#subscription-events) has been added to the Message Engagement Events page. You can now export Subscription Group State Change data from Braze to [Segment]({{ site.baseurl}}/partners/technology_partners/data_and_infrastructure_agility/customer_data_platform/segment_for_currents/#integration-details) and [mParticle]({{ site.baseurl}}/partners/technology_partners/data_and_infrastructure_agility/customer_data_platform/mparticle_for_currents/#integration-details), as well as that and Install Attribution Events in [Mixpanel]({{ site.baseurl}}/partners/technology_partners/insights/behavioral_analytics/mixpanel_for_currents).

Additionally, the property `canvas_step_id` has been added to available [Conversion Events]({{ site.baseurl}}/partners/braze_currents/data_storage_events/message_engagement_events/#conversion-events).

{% alert important %}
To take advantage of these updates, you will need to edit your Currents connector settings and enable the events you want to use. Reach out to your account manager if you have any questions.
{% endalert %}

### Subscription Groups Archiving

You can now [archive Subscription Groups]({{ site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#archiving-groups)! Archived Subscription Groups cannot be edited and will no longer appear in Segment Filters.  If you attempt to archive a group which is being used as a Segment Filter in any email, campaign, or canvas, you will receive an error message that will prevent you from archiving the Group until you remove all usages of it.

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

[support]: {{ site.baseurl }}/support_contact/
