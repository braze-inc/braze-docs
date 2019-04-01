---
nav_title: Segmentation Filters
page_order: 2
---
# Segmentation Filters

Braze’s SDK provides you with a powerful arsenal of filters to segment and target your users based off of specific features and attributes. You can also retarget your users using [retargeting filters][5].

## Custom Data

Custom data filters allow you to segment your users based on self-defined events and attributes. With them, you can use features specific to your mobile app to more specifically group the users whom you wish to target.


|Filter|Description|
|---|---|
|Custom Attributes|Determines whether or not a user matches a custom recorded attribute value.|
|Custom Event|Determines whether or not a user has performed a specially recorded event.|
|Date of Custom Attribute|Segments your users based upon the calendar date of custom attributes.
|First Did Custom Event|Determines the earliest time that a user has performed a specially recorded event (above).|
|X Custom Event in Y Days|Determines whether or not a user has performed a specially recorded event between 0 and 50 times in the last 1, 3, 7, 14, 21, and 30 days.|
|X Custom Event Property in Y Days| Determines whether or not a user has performed a specially recorded event in relation to a specific property between 0 and 50 times in the last 1, 3, 7, 14, 21, and 30 days. <br> _Please note that Custom Event Properties must be turned on by Braze for specific custom events. Contact your Account Manager or [open a support ticket][3] if you don't see the filters you need._|

## User Activity
User activity filters allow you to segment your users based on their in-app actions and purchases. Among other things, these filters can be used to target active users who have had a history of interacting with your app.

|Filter|Description|
|---|
|First Made Purchase |Segments your users by the earliest recorded time that they have made a purchase in your app.|
|First Purchase for App| Segments your users by the earliest recorded time that they have bought any item from your app. |
|First Purchased Product|Segments your users by the earliest recorded time that they have bought a specific item from your app (special membership, gift certificate, etc…).|
|First Used App|Segments your users by the earliest recorded time that they opened your app. _Note that this will capture the first session they have using a version of your app with the Braze SDK integrated._|
|First Used Specific App|Segments your users by the earliest recorded time that they opened any of your apps within your app group. |
|Last Made Purchase|Segments your users by the most recent time that they have made a purchase in your app.|
|Last Purchase for App| Segments your users by the most recent time that they have bought bought an item from your app. |
|Last Purchased Product| Segments your users by the most recent time that they have bought a specific item from your app (special membership, gift certificate, etc…).|
|Last Used App|Segments your users by the most recent time that they have opened your app.|
|Last Used Specific App| Segments your users by the most recent time that they have opened a specific, designated app. |
|Median Session Duration|Segments your users by the median length of their sessions in your app.|
|Money Spent In-App|Segments your users by the amount of money that they have spent in your app.|
|Most Recent App Version|Segments your users by the latest version of your app that they have used.|
|Most Recent Location|Segments your users by the last recorded location at which they have used your app.|
|Purchased Product|Segments your users by products purchased in your app.|
|Session Count|Segments your users by the number of sessions they have had in any of your apps within your app group.|
|Session Count For App|Segments your users by the number of sessions they have had in a specific, designated app.|
|Total Number of Purchases|Segments your users by how many purchases they have made in your app.|
|Uninstall Date|Segments your users by the date they uninstalled your app.|
|Uninstalled|Segments your users by whether they have uninstalled your app.|
|X Money Spent in Last Y Days|Segments your users by the amount of money that they have spent in your app in the last 1, 3, 7, 14, 21, and 30 days. This amount will only include the sum of the last 50 purchases.|
|X Product Purchased in Last Y Days|Segments your users by the number of times (between 0 and 50) they have bought a specific item from your app in the last 1, 3, 7, 14, 21, and 30 days (special membership, gift certificate, etc…).|
|X Purchase Property in Y Days| Segments your users by the number of times a purchase was made in relation to a certain purchase property in the last 1, 3, 7, 14, 21, and 30 days. |
|X Purchases in Last Y Days|Segments your users by the number of times (between 0 and 50) they have made a purchase in the last 1, 3, 7, 14, 21, and 30 days.|
|X Sessions in Last Y Days|Segments your users by the number of sessions (between 0 and 50) they have had in your app in the last 1, 3, 7, 14, 21, and 30 days.|

## Retargeting
Retargeting filters allow you to segment your users whom you have already attempted to target. These filters are effective for reaching out to your users who have previously responded positively to your marketing campaigns.

|Filter|Description|
|---|---|
|Clicked Card|Segments your users by whether or not they have clicked a specific card or promotion.
|Clicked/Opened Campaign|Segments your users by whether or not they have interacted with a specific campaign.|
|Clicked/Opened Campaign or Canvas With Tag|Segments your users by whether or not they have interacted with a specific campaign or Canvas with a specific tag.|
|Clicked/Opened Step| Segments your users by whether or not they have interacted with a specific Canvas step.|
|Converted from Campaign|Segments your users by whether or not they have converted on a specific campaign.
|Converted from Canvas|Segments your users by whether or not they have converted on a specific Canvas.
|Entered Canvas Variation|Segments your users by whether or not they have entered a variation path of a specific Canvas.
|Has Never Received a Message from a Campaign or Canvas Step| Segments your users by whether or not they have received a designated campaign or canvas step.|
|In Campaign Control Group|Segments your users by whether or not they were in the control group for a specific multivariate campaign.
|In Canvas Control Group|Segments your users by whether or not they were in the control group for a specific Canvas.
|Is Not In Segment| Segments your users by whether or not they are included in an already existing segment.|
|Last Received Message from Campaign or Canvas With Tag|Segments your users by when they received a specific campaign or Canvas with a specific tag.
|Last Received Message from Specific Campaign|Segments your users by when they last received a specific campaign.
|Last Received Message from Specific Canvas Step|Segments your users by selecting those who received a specific, designated Canvas Step.|
|Received Message from Campaign|Segments your users by whether or not they have received a specific campaign.
|Received Campaign Variant|Segments your users by which variant of a multivariate campaign they have received.
|Received Message from Campaign or Canvas with Tag|Segments your users by whether or not they have received a specific campaign or Canvas with a specific tag.
|Received Message from Canvas Step|Segments your users by whether or not they have received a specific Canvas step.|

## Marketing Activity
Marketing filters segment your users based on their previous interactions with your campaigns. These filters are effective for reaching out to large numbers of your users without spamming them.

|Filter|Description|
|---|---|
|Has Marked You As Spam|Segments your users by whether or not they have marked your messages as spam.
|Last Engaged With Message|Segments your users by the last time that they have clicked or opened one of your messaging channels (email, in-app, push).
|Last Enrolled in Any Control Group|Segments your users by the last time that they fell into the control group in a campaign.
|Last In App Message Impression| Segments your users by determining the last in app message impression was received.|
|Last Received Any Message| Segments your users by determining the last message that was received.|
|Last Received Any Campaign|Segments your users by the last time that they have received a campaign on any messaging channel.
|Last Received Email|Segments your users by the last time that they have received one of your email messages.
|Last Received Push|Segments your users by the last time that they received one of your push notifications.
|Last Received Webhook|Segments your users by the last time that Braze sent a webhook for that user.
|Last Viewed News Feed|Segments your users by the last time that they have visited your app's news feed interface.
|News Feed View Count|Segments your users by the number of times that they have viewed your app's news feed interface.

## User Attributes
User attribute filters segment your users by their constant attributes and characteristics. These filters are effective for grouping and targeting large demographical groups (such as specific age groups or foreign language speakers).

|Filter|Description|
|---|---|
|Age|Segments your users by how old they are.
|Amplitude Cohorts| Clients who use Amplitude to supplement their segments may import and choose from those cohorts.|
|Background Push Enabled|Segments your users on whether they have enabled background push or not.
|Birthday|Segments your users by their birthday. Users with a birthday on February 29th will be included in segments including March 1.
|City|Segments your users by their last known city location.
|Country|Segments your users by their last known country location.
|Device Carrier|Segments your users by their device carrier.
|Device Count|Segments your users by how many devices they have used your app on.
|Device Model|Segments your users by their mobile phone's model version.
|Device OS|Segments your users by their mobile phone's operating system.
|Email Available|Segments your users by whether or not they have reported their respective email addresses, and if they are subscribed/opted-in to email.
|Email Opt In Date|Segments your users by the date on which they opted into email.
|Email Subscription Status|Segments your users by their subscription status for email.
|Email Unsubscribed Date|Segments your users by the date on which they unsubscribed from future emails.
|First Name|Segments your users by first name.
|Gender|Segments your users by gender.
|Has App|Segments by whether or not a user has your app.|
|Language|Segments your users by their preferred language.
|Last Name|Segments your users by their last name.
|Location Available|Segments your users by whether or not they have reported their locations. In order to use this filter, your app needs to have [location tracking integrated.][1]|
|Most Recent Watch Model|Segments your users by their most recent smartwatch model.
|Phone Number|Segments your users by their phone number. Only use digits [0-9]. Do not include parenthesis, dashes, etc.
|Push Enabled|Segments your users who have explicitly activated push notifications for any of the apps in your app group. After segmenting with this filter, you will be able to see a breakdown of who is in that segment for Android, iOS, and web in the bottom panel, called _Reachable Users_.
|Push Enabled For App|Segments by whether or not your user has push enabled for your app on their device.|
|Push Opt In Date|Segments your users by the date on which they opted into push.
|Push Subscription Status|Segments your users by their [subscription status][4] for push.
|Push Unsubscribed Date|Segments your users by the date on which they unsubscribed from future push notifications.
|Random Bucket #|Segments your users by a randomly assigned number (0 to 9999 inclusive). Can enable the creation of uniformly distributed segments of truly random users for A/B and multivariate testing.
|Update/Imported from CSV|Segments your users based on whether they were a part of a CSV upload or not.
|Web Browser|Segments your users by the web browser they use to access your website.

## Install Attribution
Braze partners with different install attribution platforms to track the data associated with the following filters. Learn more about these platforms [here.][2]


|Filter|Description|
|---|---|
|Install Attribution Ad|Segments your users by the ad that their install was attributed to.
|Install Attribution Adgroup|Segments your users by the adgroup that their install was attributed to.
|Install Attribution Campaign|Segments your users by the ad campaign that their install was attributed to.
|Install Attribution Source|Segments your users by the source that their install was attributed to.

## Social Activity
Social activity filters segment your users by their social media activity - namely through Facebook and Twitter.

|Filter|Description|
|---|---|
|Connected to Facebook|Segments your users who have granted Facebook account access within your app.
|Connected to Twitter|Segments your users who have granted Twitter account access within your app.
|Number of Facebook Friends Using App|Segments your users by the number of friends that they have on Facebook that are using your app.
|Number of Twitter Followers|Segments your users by the number of followers that they have on Twitter.

## Testing
Testing filter segments allow you to test your campaigns by sending messages to individually designated users only.

|Filter|Description|
|---|---|
|Device IDFA|Allows you to designate your campaign recipients by IDFA for testing.
|Device IDFV|Allows you to designate your campaign recipients by IDFV for testing.
|Email Address|Allows you to designate your campaign recipients by individual email addresses for testing.
|External User ID|Allows you to designate your campaign recipients by individual user IDs for testing.

## Other

|Filter|Description|
|---|---|
|Segment Membership|Allows you to filter based on segment membership anywhere that filters are used (i.e. segments, campaigns, etc) and target multiple different segments within one campaign.|
|Provisionally Authorized on iOS | Allows you to find users who are provisionally authorized on iOS 12 for a given app. |

[1]: {{ site.baseurl }}/search/?query=location%20tracking
[2]: {{ site.baseurl }}/partners/technology_partners/advertising_technologies/attribution/branch_for_attribution/
[3]: {{ site.baseurl }}/support_contact/
[4]: {{ site.baseurl }}/help/best_practices/push/push_subscription_status/#push-subscription-status
[5]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#retargeting-filters
