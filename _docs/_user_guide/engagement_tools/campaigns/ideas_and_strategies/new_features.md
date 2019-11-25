---
nav_title: Feature Awareness and New App Version
platform: Campaigns
subplatform: Ideas and Strategies
page_order: 7
---
# Feature Awareness and New App Version

You work hard to continually update and improve your app, and you want your users to experience these exciting new features and new app versions.  Learn how to teach users about the new features they have yet to use, and encourage them to explore the app to get the most you have to offer.

## Why Use Feature Awareness Campaigns

Feature awareness campaigns are a great way to encourage users to stay engaged with your app as you continue to improve your app's functionality.  Keeping users up to date is a great way to keep them active, boost ratings and ensure user engagement.

## Filtering by Most Recent App Versions

Braze SDKs automatically track a user's _most recent_ app version. These versions can be used in filters and segments to determine which users should receive a message or campaign. There are two relevant version filters you can use:

#### Most Recent App Version

_Most Recent App Version_ filters on an app's user-facing version name. This filter supports matching by "is", "is not", and regular expressions.

#### App Version Code

_App Version Code_ filters based on app version numbers. This filter supports numerical comparisons to target a range of app versions. For example, you can filter using "below", "above", and "equal to" certain app versions. Support for this feature is available with the Braze Android SDK v3.6.0+ and iOS SDK v3.21.0+, and can be enabled by your Braze account manager.

![App Version Filter][1]

### Have Not Used Feature

When you release a new app version and introduce new features, users may not notice new content.  Running a feature awareness campaign is a great way to teach users about new features or features they have never used. To do so you must create a [custom attribute][3] that is assigned to users who have never completed a certain action within your app or use a [custom event][4] to track a particular action.  You can use this attribute (or event) to segment users that you want to sent the campaign to.

## Best Practices

### Be Convincing

Persuading a user to update their app or change the way they use your app can be difficult.  Make sure the let them know all the benefits of the new version/features and how it will improve their experience with your app.  Let them know all of the utility they will gain, and the benefits they will miss out on if they choose not to update or engage with new features.

### Send at the Right Time

Convincing your users to update their app can be difficult as they must navigate to the app store to do so.  In general, it is best to ask users to update as soon as the app is updated, however if they choose not to do not spam them with messages. Rather, wait until they have a positive experience within the app, for instance beating a level, redeeming a coupon, or favoriting a song.

For feature awareness campaigns, timing is also key.  Onboarding should familiarize users with the app, however users may forget features or not notice new features that are added. When new features are added, be sure to let your users know. Hopefully users will discover new features easily, however if users are not engaging with major features within the app it may be best to remind them. Do so when they are engaging with your app and the unused feature would be of use.

### Use Non-intrusive Channels

Because they are relatively intrusive, push notifications and emails that ask users to update can come off as needy if sent too often. Be sure to use a multi-channel strategy when making your request, focusing on in-app channels if possible. [In-app messages][5] and [News Feed][6] cards are less disruptive and easily ignored if the user doesn’t wish to update immediately. Be sure to include deep links to the appropriate app store. Simple in-app messages pointing out new features can be a great way to expose users to new content without getting in their way and cluttering them with messages.


[1]: {% image_buster /assets/img_archive/new_app_version.png %}
[2]: {% image_buster /assets/img_archive/update_notification.png %}
[3]: {{ site.baseurl }}/user_guide/engagement_tools/segments/segmentation_filters/#custom-data
[4]: {{ site.baseurl }}/user_guide/engagement_tools/segments/segmentation_filters/#custom-data
[5]: {{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/create/#creating-an-in-app-message
[6]: {{ site.baseurl }}/user_guide/engagement_tools/news_feed/creating_a_news_feed_item/#creating-a-news-feed-item
