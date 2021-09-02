---
nav_title: Feature Awareness and New App Version
article_title: Feature Awareness and New App Version
page_order: 7
page_type: reference
description: "This reference article discusses how to keep your users knowledgeable and excited about when you release new features or versions."
tool: Campaigns

---
# Feature Awareness and New App Version

> This reference article addresses how to use the Braze platform to keep your customers up to date on new features and versions of your app. 

You work hard to continually update and improve your app, and you want your users to experience these exciting new features and new app versions.  Learn how to teach users about the new features they have yet to use, and encourage them to explore the app to get the most you have to offer.

## Why Use Feature Awareness Campaigns

Feature awareness campaigns are a great way to encourage users to stay engaged with your app as you continue to improve your app's functionality.  Keeping users up to date is a great way to keep them active, boost ratings and ensure user engagement.

## Filtering by Most Recent App Versions

Braze SDKs automatically track a user's _most recent_ app version. These versions can be used in filters and segments to determine which users should receive a message or campaign.

![App Version Filter][1]

### App Version Number (new)

Use the _App Version Number_ filter to segment users by the app's version/build number. 

This filter supports numerical comparisons to target a range of app versions. For example, you can target users whose app is "below", "above", and "equal to" app version "1.2.3", which might be beneficial to promote a new feature which requires an app upgrade.

This new filter can replace the legacy "App Version Name" filter which would require explicitly listing each older version or using a regular expression.

#### SDK requirements

Values for this filter are collected starting with Braze Android SDK v3.6.0+ and iOS SDK v3.21.0+. Even though this filter has SDK requirements, you will still be able to target users who are on lower (older) versions of your app using this feature!

For Android, this version number is based on the [Package Long Version Code][9] for the app.

For iOS, this version number is based on the [Short Version String][8] for the app.

{% alert tip %}
This filter will populate values once users upgrade their apps to the supported Braze SDK Versions. Until then, the filter won't show any versions when selected.
{% endalert %}

#### Example Scenarios

In the following scenario, let's assume that you first upgraded to the Braze SDKs which supports this filter in version `2.0.0` of your app.

Once Braze receives data from version 2.0.0 of your app, you can target users below or above this version.

| Filter  | User's App Version  | Result |
:------------- | :----------- | :---------|
| _Less than 2.0.0_ | 1.0.0 | User is in the segment, even though their Braze SDK did not support the App Version Number filter |
| _Greater than 2.0.0_ | 2.5.1 | This user, and all future installs will be in the segment |
| _Greater than 2.0.0_ | 1.9.9 | User is not in the segment |
| _Less than or equal to 2.0.0_ | 3.0.1 | User is not in the segment |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### App Version Name

Use the _App Version Name_ filter to segment users by the app's user-facing version name. 

This filter supports matching with "is", "is not", and regular expressions. For example, you can target users who have an app that is not version "1.2.3-test-build".

For Android, this version name is based on the [Package Version Name][7] for the app.

For iOS, this version name is based on the [Short Version String][8] for the app.

### Have Not Used Feature

When you release a new app version and introduce new features, users may not notice new content.  Running a feature awareness campaign is a great way to teach users about new features or features they have never used. To do so you must create a [custom attribute][3] that is assigned to users who have never completed a certain action within your app or use a [custom event][4] to track a particular action.  You can use this attribute (or event) to segment users that you want to send the campaign to.

## Best Practices

### Be Convincing

Persuading a user to update their app or change the way they use your app can be difficult.  Make sure the let them know all the benefits of the new version/features and how it will improve their experience with your app.  Let them know all of the utility they will gain, and the benefits they will miss out on if they choose not to update or engage with new features.

### Send at the Right Time

Convincing your users to update their app can be difficult as they must navigate to the app store to do so.  In general, it is best to ask users to update as soon as the app is updated, however, if they choose not to do not spam them with messages. Rather, wait until they have a positive experience within the app, for instance beating a level, redeeming a coupon, or favoriting a song.

For feature awareness campaigns, timing is also key.  Onboarding should familiarize users with the app, however, users may forget features or not notice new features that are added. When new features are added, be sure to let your users know. Hopefully, users will discover new features easily, however, if users are not engaging with major features within the app it may be best to remind them. Do so when they are engaging with your app and the unused feature would be of use.

### Use Non-intrusive Channels

Because they are relatively intrusive, push notifications and emails that ask users to update can come off as needy if sent too often. Be sure to use a multichannel strategy when making your request, focusing on in-app channels if possible. [In-app messages][5] and [Content Cards][6] cards are less disruptive and easily ignored if the user doesn’t wish to update immediately. Be sure to include deep links to the appropriate app store. Simple in-app messages pointing out new features can be a great way to expose users to new content without getting in their way and cluttering them with messages.


[1]: {% image_buster /assets/img_archive/new_app_version.png %}
[3]: {{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#custom-data
[4]: {{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#custom-data
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/#creating-an-in-app-message
[6]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/
[7]: https://developer.android.com/reference/android/content/pm/PackageInfo#versionName
[8]: https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleshortversionstring
[9]: https://developer.android.com/reference/android/content/pm/PackageInfo.html#getLongVersionCode()
