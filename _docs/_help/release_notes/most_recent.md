---
nav_title: Most Recent
page_order: 0
---

# Most Recent Braze Release Notes

_Braze releases information on it’s product updates on a monthly cadence. For more information on any of the updates listed in this section, reach out to your account manager or to [open a support ticket][support]._

## May 2019

## Content Cards

Content Cards are persistent content that appear within customers’ app and web experiences.

With Content Cards, you can send a highly targeted, dynamic stream of rich content to your customers right within the apps they love, without interrupting their experience. Or, you can pair Content Cards with other channels, like email or push notifications, to enable cohesive marketing strategies.

![Content Cards Feed][CCFeed]

In addition, Content Cards support more personalized features, including card pinning, card dismissal, API-based delivery, custom card expiration times, card analytics.

Use it to create notification centers, homepage feeds, and promotion feeds.

You will need to update to a supported Braze SDK version:
- __iOS__: 3.8.0 or above
- __Android__: 2.6.0 or above
- __Web__: 2.2.0 or above

[Learn more about Content Cards here!]({{ site.baseurl }}/user_guide/message_building_by_channel/content_cards/overview/)

{% alert update %}
Content Cards for Currents, as well as our API documentation for Content Cards, will be launched later this week. Stay tuned!
{% endalert %}

### Roku Platform Addition

Braze has added a new channel to our capabilities! By expanding into new channels, we can enable our customers to enrich their data by understanding viewing behavior or provide meaningful experiences to their consumers across all relevant channels.

You can now retrieve data from Roku devices for data enrichment and custom event tracking.

[Check out the documentation here!]({{ site.baseurl }}/developer_guide/platform_integration_guides/roku/initial_sdk_setup/)

### Notification Preferences for Canvas & Campaign Updates

This new notification will alert you via email when a Campaign/Canvas is activated, updated, reactivated or deactivated. Activate this in Notification Preferences in your Braze account. [Learn more about this preference here.]({{ site.baseurl }}/user_guide/administrative/company_settings/notification_preferences/#notification-preferences)  

### Jampp Technology Partner Documentation

Jampp is a performance marketing platform for acquiring and retargeting mobile customers. It combines behavioral data with predictive and programmatic technology to generate revenue for advertisers by showing personal, relevant ads that inspire consumers to purchase for the first time, or more often.

[Braze customers can integrate with Jampp]({{ site.baseurl }}/partners/technology_partners/advertising_technologies/retargeting/jampp/) by configuring the Braze webhook channel to stream events into Jampp. As a result, customers have the ability to add richer data sets to their retargeting initiatives with Jampp within the mobile advertising ecosystem.

### Platform Picker for In-App Messages

We've made it easier to select where your in-app messages are going and which platforms they're built for with our platform picker, which emphasizes this step in the campaign creation process.

![Platform Picker][plat_p]

### Dispatch ID Currents Field for Email

In the effort to continue enhancing our Currents capabilities, we're adding `dispatch_id` as a field to Currents Email events across all connector types.

The `dispatch_id` is the unique id generated for each transmission – or, dispatch – sent from the Braze platform.

While all customers who are sent a scheduled message get the same `dispatch_id`, customers who receive either action-based or API triggered messages will get a unique `dispatch_id` per message. The `dispatch_id` field enables you to identify which instance of a recurring campaign is responsible for conversion, thus equipping you with more insights and information on which types of campaigns are helping push the needle on your business goals.

### Only Show Mine - Campaign Sorting Feature

When a user checks the `Only Show Mine` checkbox on the Campaign grid, the results will filter down to Campaigns show only created by the logged-in user. Additionally, the user can use the search bar by inputting `created_by_me:true`.

![Created by Me][cbm]

Also, the Campaign grid sidebar is now resizable!

### Delete Users by Alias

You can now use the `users/delete` endpoint to [delete users by alias]({{ site.baseurl }}/api/endpoints/user_data/#user-delete-request)!

### Unique Calculation for Email Clicks and Opens

Unique Clicks and Unique Opens for Email are now captured and displayed on a 7-day time frame per user and increment a count of 1 within that 7 day window, per each `dispatch_id`.

Using `dispatch_id` allows for recurring messages to reflect the true unique open or unique click count of each message. It will be easy for customers to match this data, now that the `dispatch_id` is available in Currents.

Any users also using Mailjet will see a spike in these numbers, since the previous uniqueness timeframe was over 30 days. You should have been made aware of this change three (3) weeks ago.  Sendgrid customers should see no difference.

You can search for these updated terms in our [Report Metrics Glossary]({{site.baseurl }}/user_guide/data_and_analytics/report_metrics/).

### Most Engaged Channel

The Most Engaged Channel filter selects the portion of your audience for whom the selected messaging channel is their “best” channel. In this case, “best” means “has the highest likelihood of engagement, given the user’s history”. You can select Email, Web Push, or Mobile Push (which includes any available mobile OS or device) as a channel.

Check this new filter out in [our Segmentation Filters library]({{site.baseurl }}/user_guide/engagement_tools/segments/segmentation_filters/).

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

[support]: {{ site.baseurl }}/support_contact/
[CCFeed]: {% image_buster /assets/img/cc-feed.png %}
[cbm]: {% image_buster /assets/img/created_by_me2.png %}
[plat_p]: {% image_buster /assets/img/iam_platforms.gif %}
