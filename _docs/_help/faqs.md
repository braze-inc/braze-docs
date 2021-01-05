---
page_order: 6
nav_title: FAQs
hide_toc: true
---
# Frequently Asked Questions

{% details Is Braze compatible with other SDKs? %}
Yes. We have done internal testing and verified that we are compatible with Urban Airship, Flurry, and Crittercism. That is not to say that we are not compatible with more, but that is what we have tested so far. If you are experiencing any issues you think might be due to incompatibility, feel free to contact your Customer Success Manager.
{% enddetails %}


{% details What is my dashboard URL and REST endpoint? %}
Braze manages a number of different instances for our Dashboard and REST Endpoints. When your account is provisioned you will log in to one of the corresponding URLs mentioned in the [Access Braze article]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/). Use the correct REST Endpoint based on which instance you are provisioned to. If you are unsure, open a support ticket or use the table below to match the URL of the dashboard you use to the correct REST Endpoint.
{% enddetails %}


{% details Which SDK endpoint do I use? %}
If your company was set up with a custom endpoint, please reach out to your Customer Success Manager or [open a support ticket][support]. If not, one of the corresponding endpoints mentioned in the [Access Braze article]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/).
{% enddetails %}


{% details Will Braze affect my app’s performance? %}
Braze should have no negative impact on your app’s performance. The Braze SDKs have a very small footprint. We automatically change the rate that we flush user data depending on the quality of the network, in addition to allowing manual network control. We automatically batch API requests from the SDK to make sure that data is logged quickly while maintaining maximum network efficiency. Lastly, the amount of data sent from the client to Braze within each API call is extremely small.
{% enddetails %}


{% details What is a UserID? %}
A UserID is a unique identifier for a given user. A UserID can have multiple devices associated with it which provides a few benefits:
* Provide a consistent user experience across multiple devices and platforms e.g. not sending lapsing user notifications to a user’s Android tablet when they are a loyal user of the app on the iPhone.
* Improve the accuracy of your analytics by ensuring users aren’t creating a new user profile every time they uninstall and reinstall, or install the app on a different device.
Enable import of user data from sources outside the app using our RESTful User API, and target users with transactional messages using our RESTful Messaging API.
* Search for individual users using our “Testing” filters within the segmenter, and on the “User Search” page.
* We strongly recommend providing a UserID for users who have logged into your application. These should be unchanging and accessible when a user opens the app. Something like a username, or a unique identifier from your database is usually a good reference to use.
If you are unsure if you’ve set a UserID for your users, or are trying to perform a user search and are unaware of how UserIDs have been assigned within your app please contact your developers. Refer them to success@braze.com if they require additional details.
{% enddetails %}


{% details What is the definition of an “active user”? %}
Braze defines an active user for a given time period as any user who has a session in that time period. If a user loses connectivity, we will cache the session data locally and upload it when the user regains a network connection. These sessions will also be applied to the active user count. Additionally, if your app has a registration process, Braze will count all users as active - registered or unregistered.
Additionally, if you set User IDs to identify users when a new user logs in they will be counted as a separate active user. Users who are updated via the API will also be counted as an active user in the time period that they are updated.
{% enddetails %}


{% details What is the definition of a “new user”? %}
Braze considers a new user as anyone who has newly installed your app. Alternatively, a new user can also be defined as a user with a user ID that has not been previously identified within Braze.
{% enddetails %}


{% details What is the definition of “stickiness”? %}
Your app’s “Stickiness” value is a ratio of a given day’s total number of users that visited the app to your Monthly Active Users (MAUs) on that day. MAUs are calculated nightly on a rolling monthly period.
{% enddetails %}


{% details Why is there a difference between the number of unique recipients and the number of sends for a given Campaign or Canvas? %}
One potential explanation for this difference could be due to the campaign or Canvas having re-eligibility turned on. By having this on, users who qualify for the segment and delivery settings will be able to receive the message more than once.
If re-eligibility is not turned on, then the probable explanation for the difference between sends and unique recipients may be due to users having multiple devices, across platforms, associated with their profiles. For example, should you have a Canvas that has both iOS and web push notifications, a given user with both mobile and desktop devices could receive more than one message.
{% enddetails %}

{% details What does Local Time Zone Delivery offer? %}
Local time zone delivery allows you to deliver messaging campaigns to a segment based on a user’s individual time zone. Without local time zone delivery, campaigns will be scheduled based on your company’s time zone settings in Braze. For example, a London-based company sending a campaign at 12pm will reach users on the west coast of America at 4am. If your app is only available in certain countries, this may not be a risk for you, otherwise, we highly recommend avoiding sending early morning push notifications to your user base!
{% enddetails %}

{% details How does Braze recognize a user’s time zone? %}
Braze will automatically determine a user’s time zone from their device. This ensures time zone accuracy and full coverage of your users. Users created through the User API or otherwise without a timezone will have your company’s time zone as their default time zone until they are recognized in your app by the SDK. To check your company’s timezone, look at your company settings on the dashboard. Click on your name in the top toolbar and then click on “Company Settings.”
{% enddetails %}

{% details How does local time zone delivery work? %}
Braze will begin delivering a campaign when the first time zone in the world reaches the specified time. After delivery begins, we will continue delivering the campaign throughout the day as additional time zones reach the campaign delivery time. Please allow for sufficient time to view full campaign results from a local time zone campaign. In addition, to the typical time lag seen for email results, full campaign analytics will be available shortly after the campaign completes a full 24-hour cycle.
{% enddetails %}

{% details How do I schedule a local time zone campaign? %}
When scheduling a campaign, you need to choose to send it at a designated time, and then check the box next to “Send campaign to users in their local time zone.”
Braze highly recommends that all local time zone campaigns are scheduled 24 hours in advance. Since such a campaign needs to send over the course of an entire day, scheduling them 24 hours in advance ensures that your message will reach your entire segment. However, you do have the ability to schedule these campaigns less than 24 hours in advance if necessary. Keep in mind that Braze will not send messages to any users that has missed the send time by more than 1 hour. For example, if it is 1pm and you schedule a local time zone campaign for 3pm, then the campaign will immediately send to all users whose local time is 3-4pm, but not to users whose local time is 5pm. In addition, the send time you choose for your campaign needs to have not yet occurred in your company’s time zone.
Editing a local time zone campaign that is scheduled less than 24 hours in advance will alter the message’s schedule for certain users. If you decide to edit a local time zone campaign to send at a later time (for instance, 7pm instead of 6pm), users who were in the targeted segment when the original send time was chosen will still receive the message at the original time (6pm). If you edit a local time zone to send at an earlier time (for instance, 4pm instead of 5pm), then the campaign will send to all segment members at the earlier time (4pm). If you have allowed users to become re-eligible for the campaign, then they will receive it again at the original time (5pm). For all subsequent occurrences of your campaign, however, your messages only send at your updated time.
{% enddetails %}

{% details When do changes to local time zone campaigns take effect? %}
Target segments for local time zone campaigns should include at least a 48-hour window for any time-based filters to guarantee delivery to the entire segment. For example, consider a segment targeting users on their second day with the filters:
* First used app more than 1 day ago
* First used app less than 2 days ago
* Local time zone delivery may miss users in this segment based on the delivery time and the users’ local time zone. This is because a user can leave the segment by the time their time zone triggers delivery.
{% enddetails %}

{% details What changes can I make to scheduled campaigns ahead of launch? %}
When the campaign is scheduled, edits to anything other than the message composition need to be made before we enqueue the messages to send.
As per all campaigns, you can’t edit conversion events after it is launched.<br>
For Canvas entries, refer to above.<br>

For Canvas steps: <br>- Scheduled changes will only apply to users who are not already waiting to receive the step. <br>- Audience changes default to apply to everyone unless you’ve selected Evaluate At Enqueue Time, in which case it’s similar behavior to above.
{% enddetails %}

{% details What is the “safe zone” before messages on a scheduled campaign are enqueued? %}
__One-time scheduled campaigns__ - can be edited up until the scheduled send time.<br>
__Recurring scheduled campaigns__ - can be edited up until the scheduled send time.<br>
__Local Send Time campaigns__ - can be edited up to 24 hours prior to the scheduled send time.<br>
__Optimal Send Time campaigns__ - can be edited up to 24 hours prior to the day the campaign is scheduled to send on.

What if I make an edit within the “safe zone?”

Changing the send time on campaigns within this time can lead to undesired behavior, for example:<br>- Braze will not send messages to any users that have missed the send time by more than 1 hour.<br>- Pre-enqueued messages may still send at the originally enqueued time, rather than the adjusted time.
{% enddetails %}

{% details What should I do if the “safe zone” has already passed? %}
To ensure campaigns operate as desired, we recommend stopping the current campaign (this will abort any enqueued messages). You can then duplicate the campaign, making the changes as necessary and launch the new campaign. You may need to exclude users from this campaign who have already received the first campaign.
Please ensure you re-adjust campaign schedule times to allow for timezone sending.
{% enddetails %}

{% details Can I create single-user segments? %}
Yes. You can create single user segments (or segments of a handful of users) using unique attributes that identify users, like a user name or a user ID. The segmentation stats or preview may not show this individual user though because segment stats are calculated based on a random sample with a 95% confidence interval that the result is within +/- 1%. The larger your user base is, the more likely it is that the size of your segment is a rough estimate. To ensure that your segment contains the single user you are targeting, click on “Calculate Exact Statistics” on the segment page. This will calculate the exact number of users in your segment, without any rounding.
Braze has testing filters to target specific users by user ID or email address.
{% enddetails %}

{% details Can I send myself test messages? %}
Yes. Check out our section on sending test messages here within the troubleshooting section.
{% enddetails %}

{% details What’s the default APNs expiration date? %}
Braze sets the default expiration date for push notifications sent through APNs to 30 days.
{% enddetails %}

{% details When does the client download new content? %}
Braze sends data to the SDK at the beginning of a session based on which segments the user falls into at the time of the session. The news feed or new in-app messages will not be updated during the session. However, user data during the session will be continually processed as it is sent from the client. For example, a lapsed user (last used the app more than 7 days ago) will still receive content targeted at lapsed users on their first session back in the app.
{% enddetails %}

{% details When is segment membership calculated? %}
Braze updates the user’s segment membership as data is sent back to our servers and processed, typically instantaneously. A user’s segment membership will not change until that session has been processed. For example, a user who falls into a lapsed user segment when the session first starts will be immediately moved out of the lapsed user segment when the session is processed.
{% enddetails %}

{% details When does Braze upload data? %}
The Braze SDK caches data (sessions, custom events, etc) and uploads it periodically. Only after the data has been uploaded will the values be updated on the dashboard. The upload interval takes into account the state of the device and is governed by the quality of the network connection:

|Network Connection Quality |    Data Flush Interval|
|---|---|
|Great    |10 Seconds|
|Good    |30 Seconds|
|Poor    |60 Seconds|

If there is no network connection, data is cached locally on the device until the network connection is re-established. When the connection is re-established, the data will be uploaded to Braze.
No data is uploaded after a session is closed.
{% enddetails %}

{% details What does it actually mean to “warm up” an IP address? %}
IP warming is designed to ensure that you establish a positive email reputation with ISPs (Internet Service Providers) so that your messages are not filtered to spam. If you send email from a new or “cold” IP address, ISPs closely monitor the amount of email you are sending and how often your users are labeling your email as SPAM. They use that data to create an email reputation that will eventually determine whether or not your emails are filtered to SPAM automatically.
Abrupt, high volume email campaigns are regarded with the most skepticism by ISPs. Given that, you should begin by sending small amounts of email and scale gradually towards the volume of email you ultimately intend to send. Regardless of volume, we suggest warming up your IP to be safe.
This process doesn’t guarantee that your emails won’t be filtered to spam. It is also important that you send engaging content, and send emails consistently to users who want to receive it.
{% enddetails %}

{% details Why don’t I see “Braze Is Working” anymore with a debug API key? %}
Braze deprecated the Debug API keys in August 2014. As a result, you will no longer see “Braze is Working” when using any legacy debug API keys you may have. You should migrate your application to the API key on your “App Settings” page in order to test messaging and recording functionality.
The production key should be used with production provisioning profiles and apps that are live in the app store.
{% enddetails %}

{% details How does rate-limiting work? %}
Braze affords you control over marketing pressure by allowing you to limit the rate at which your users are messaged both globally and on a per-channel basis using the following filters.
* Last Received Any Message
* Last Received Email Campaign
* Last Received Push Campaign
If your push campaign fails to reach the intended user we still mark that user has having received a push campaign on that day. We record the campaign receipt at the time of delivery because push token invalidation notifications from iOS and FCM are not synchronous.
{% enddetails %}

{% details Can I target users who have downloaded but not opened my app? %}
No, Braze does not generate profiles for users until they have used the app for the first time.
{% enddetails %}

{% details Is Braze compatible with RubyMotion? %}
Yes. The Braze iOS SDK fully supports RubyMotion Apps.
{% enddetails %}

{% details When can FCM Registration IDs change? %}
FCM Registration IDs are created when the app is installed and registers for push notifications. Google will not change this registration ID except in the following cases:
* Client App Update
* Backup and Restore
Braze automatically handles the deletion of the old token, and the addition of the new token to a user’s profile so long as our SDK is instrumented properly as outlined in our Android Push Documentation.
{% enddetails %}

{% details What is Deep Linking? %}
“Deep Linking” is a way of launching a native app and providing additional information telling it do some specific action or show specific content. It also allows Google to crawl your app content and allows users to enter your app from search results.
There are three parts to this:
* Identify which app to launch
* Instruct the app which action to perform
* Provide the action with any additional data it will need
“Deep Links” contain all of these things. The key is defining a custom scheme. “http:” is the scheme with which almost everyone is familiar but schemes can begin with any word. A scheme must start with a letter, but can then contain letters, numbers, plus-signs, minus-signs, and dots. Practically speaking, there is no central registry to prevent conflicts, so it is a Best Current Practice to include your domain name in the scheme.
Everything after the colon within a “Deep Link” is free-form text. It is up to you to define its structure and interpretation, however, a common convention is to model it after “http:” URLs, including a leading “//” (or “///”, leaving a null string where the hostname would normally appear) and query parameters (e.g. ?foo=1&bar=2). Following this approach, the action would be specified by the path and the additional data would be either in the path or in a query string. e.g. “/user/johndoe” or “/show?user=johndoe”.
These “Deep Links” are a powerful tool when used in tandem with the Braze News Feed. “Providing “Deep Links” as the URL within News Feed items allows you to utilize the News Feed as an individualized navigation tool to direct users to content inside or outside of your app.
With iOS, it’s also possible to deep-link into your application’s settings within the iOS Settings App where a user can define their preferences for Location, Notifications, Background App Refresh, etc. This can be useful if trying to re-prime users for push who have denied your initial prompt. Type “app-settings://” for your deep-link within your campaign to achieve this.
{% enddetails %}

{% details When should I put multiple apps in the same app group? %}
The draw to have multiple apps under one App group can be enticing as it can lead to the ability to rate limit messaging across your entire app portfolio. However, as a best practice, we suggest only putting different versions of the same or very similar apps together under one app group. For example, your iOS and Android versions of the same app or your free and premium versions of the same app.
Whichever apps you choose to have in one app group will have their data aggregated which will have a notable impact on filters in Braze:
* Last Used App
* First Used App
* Session Count
* Money Spent In-App
* Push subscription (this becomes an all or none situation, in other words, if your users unsubscribe from one app they will be unsubscribed from all of your apps under the app group)
* Email subscription (this becomes an all or none situation - and can leave you open to compliance issues)
This is not an exhaustive list. The aggregation of the data across dissimilar apps in filters like those listed above is why we do not recommend housing substantially different apps within the same app group.
{% enddetails %}

{% details If I’m relaunching a new version of my app, should I make a new app group? %}
If users will simply have to update the app and it’s not a new app being released to the app store, you should not create a new app group if you plan to still message users on the older version.
By creating a new app group, all of the historical data and profiles from the older version of your app will not exist in this new app group. So, once existing users upgrade to the new app version, they’ll have a new profile created that does not contain any of the behavioral data from the old app. Additionally, this user will exist on both the old app group and the new app group and can potentially have the same push token. If this happens, it can lead to users receiving an “upgrade now” marketing message intended for only old app group users, even if they’ve already upgraded.
The best way to go about this if you want to separate the old vs. new app would be to create a new app within the same app group. This way, you can effectively target only users on the new version by selecting that app as you create your segments. If you did want to message users who are still on the old version, you can select the old app and filter the previous app version.
{% enddetails %}

{% details When does Braze collect location? %}
Braze only collects location when the application is in the foreground. As a result, our last known location filters target users based upon where they last opened the application.
{% enddetails %}

{% details Does Braze allow me to add UTM parameters to deep links for Google Analytics tracking? %}
Yes, this is possible as long as your client code is programmed to parse the UTM parameters that are sent with the deep link and send them to Google Analytics. You should ensure that you have the appropriate Google Analytics method integrated to do this.
{% enddetails %}

{% details Why has one of my users been blocked? %}
Braze will ban or block users ("dummy users") with over 5 million sessions and no longer ingest their SDK events because they are usually the result of misintegration. If you find that this has happened for a legitimate user, please reach out to your Braze account manager.
{% enddetails %}

{% details What are Braze Firebrands? %}
Braze Firebrands is our customer engagement community. We're building a community of movers and shakers using Braze to modernize their customer experience and marketing. Interested in learning more? <a href='https://brazefirebrands.splashthat.com/'>Join now</a>.
{% enddetails %}


[support]: {{site.baseurl}}/support_contact/
