---
nav_title: Most Recent
page_order: 0
---

# Most Recent Braze Release Notes

_Braze releases information on it’s product updates on a monthly cadence. For more information on any of the updates listed in this section, reach out to your account manager or to [open a support ticket][support]. You can also check out [our SDK Changelogs]({{ site.baseurl }}/developer_guide/platform_integration_guides/sdk_changelogs/) to see more information on our monthly releases, updates, and improvements._

## July 2019

### User Profile Image Removal

We are removing the user profile pictures displayed in Braze User Profiles and User Searches.

### Connected Content in Content Cards

You can now use [Connected Content]({{ site.baseurl }}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content) strings and functionality in [Content Cards]({{ site.baseurl }}/user_guide/message_building_by_channel/content_cards/overview/).

Connected Content calls to external servers will happen when a Card is actually sent, __not__ when the Card is viewed by the User. Similar to Email, dynamic content will be calculated and determined at sending time, rather than when a Card is actually viewed.

### Null 'Reply-To' Address

Customers can now set a `null` value for an email messages's "Reply-To" address from the Email Settings page in Braze or using [the API]({{ site.baseurl }}/api/endpoints/messaging/#email-object-specification).  When used, replies will be sent to the listed "From" address.  You can now personalize the "From" address field as `dan@emailaddress.com` and your customers will have the ability to reply directly back to Dan.

To set a `null` value for an email messages's "Reply-To" address from Braze, go to `Manage App Group` in the navigation, then the `Email Settings` tab. Scroll to the `Outbound Email Settings` section, and select `Exclude “Reply-To” and send replies to “From”` as the default address.

![Email Settings Reply-To]({% image_buster /assets/img/null_reply-to.png %})

### Campaign Comparisons

Look at [multiple campaigns at one time to compare their relative performance]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/testing_and_more/comparing_campaigns/), side-by-side in Braze - in one window!

### Template Dispatch ID into Messages with Liquid

If you want to track the dispatch of a message from within the message (in a URL, for example), you can template in the `dispatch_id`. You can find the formatting for this in our list of Supported Personalization Tags, under [Canvas Attributes]({{ site.baseurl }}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

This behaves just like `api_id`, in that since the `api_id` isn't available at Campaign creation, it is templated in as a placeholder and will preview as `dispatch_id_for_unsent_campaign`. The id is generated before the message is sent, and will be included in as send time.

{% alert warning %}
Liquid templating of `dispatch_id_for_unsent_campaign` does not work with in-app messages, since in-app messages don't have a `dispatch_id`.
{% endalert %}

### "Show Only Mine" Setting Persists

The "Show Only Mine" filter on the Campaign grid will remain "on" any time you visit the Campaigns page.

### A/B Testing Updates

You can send a one-time [A/B test]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/) with up to eight variants (and optional control) to a user-specified percentage of a Campaign's audience, and then send the best variant to the remaining audience at a pre-scheduled time.

## June 2019

### Snowflake Partnership

Braze is proud to announce our partnership with Snowflake!

Snowflake is a purpose-built SQL cloud data warehouse for all of your data and all of your users. With Snowflake's unique and patented architecture it's easy to amass all of your data, enable rapid analytics, and derive data-driven insights for all of your users.

Braze leverages Snowflake’s Data Exchange to build a presence, find new customers, and expand reach through the ever-growing Snowflake customer base.

Learn more about this partnership [here](https://www.braze.com/perspectives/article/snowflake-partner-announcement) or in [our documentation]({{ site.baseurl }}/partners/snowflake/).

## May 2019

## Content Cards

Content Cards are persistent content that appear within customers’ app and web experiences.

With Content Cards, you can send a highly targeted, dynamic stream of rich content to your customers right within the apps they love, without interrupting their experience. Or, you can pair Content Cards with other channels, like email or push notifications, to enable cohesive marketing strategies.

![Content Cards Feed]({% image_buster /assets/img/cc-feed.png %}){: height="50%" width="50%"}

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

![Created by Me][cbm]{: height="50%" width="50%"}

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



[support]: {{ site.baseurl }}/support_contact/
[CCFeed]: {% image_buster /assets/img/cc-feed.png %}
[cbm]: {% image_buster /assets/img/created_by_me2.png %}
[plat_p]: {% image_buster /assets/img/iam_platforms.gif %}
