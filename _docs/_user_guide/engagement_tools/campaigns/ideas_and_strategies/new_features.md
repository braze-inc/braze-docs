---
nav_title: Feature Awareness and New App Version
article_title: Feature Awareness and New App Version
page_order: 9
page_type: reference
description: "This reference article discusses how to keep your users knowledgeable and excited about when you release new features or versions."
tool: Campaigns

---

# Feature awareness and new app version

> This reference article addresses how to use the Braze platform to keep your customers up to date on new features and versions of your app. 

You work hard to continually update and improve your app, and you want your users to experience these exciting new features and new app versions. Learn how to teach your users about the new features they have yet to use, and encourage them to explore the app to get the most you have to offer.

Feature awareness campaigns are a great way to encourage users to stay engaged with your app as you continue to improve your app's functionality.  Keeping users up to date is a great way to keep them active, boost ratings, and ensure user engagement.

## Filtering by most recent app versions

Braze SDKs automatically track a user's most recent app version. These versions can be used in filters and segments to determine which users should receive a message or campaign.

![The Targeting Options panel in the Target Users step in the campaign building workflow. The Additional Filters section includes the following filter "Most Recent App Version Number for Android Stopwatch (Android) is below 3.7.0 (134.0.0.0)".]({% image_buster /assets/img_archive/new_app_version.png %}){: style="max-width:90%;"}

{% alert note %}
It may take time for the current app versions to populate. The app version on the user profile updates when the information is captured by the SDK, which relies on when users open their apps. If the user doesn't open the app, the current version won't be updated. <br><br> These filters also won't apply retroactively. It's good to use "greater than" or "equal" to current and future versions, but using past version filters may cause unexpected behaviors.
{% endalert %}

### App version number

Use the **App Version Number** filter to segment users by the app's version and build number. 

This filter supports numerical comparisons to target a range of app versions. For example, you can target users whose app is "below", "above", and "equal to" app version "1.2.3", which might be beneficial to promote a new feature which requires an app upgrade.

This new filter can replace the legacy "App Version Name" filter which would require explicitly listing each older version or using a regular expression.

**How it works**

* Each part of the `major.minor.patch` version sent in your app's app version are compared as integers
* If the major numbers are equal, the minor numbers are compared, etc.

**Important**

* Android apps have both a human readable [`versionName`](https://developer.android.com/reference/android/content/pm/PackageInfo#versionName) and an internal [`versionCode`](https://developer.android.com/reference/android/content/pm/PackageInfo.html#getLongVersionCode()). The App Version Number filter uses `versionCode` because it is guaranteed to be incremented with each app store release.
* This can cause confusion when your app's `versionName` and `versionCode` get out of sync, especially since both fields can be viewed from the Braze dashboard. As a best practice, check that your app's `versionName` and `versionCode` are incremented together.
* If you need to filter by the human readable `versionName` field instead (uncommon), use the App Version Name filter.

#### SDK requirements

Values for this filter are collected starting with Braze Android SDK v3.6.0+ and iOS SDK v3.21.0+. Even though this filter has SDK requirements, you will still be able to target users who are on lower (older) versions of your app using this feature!

For Android, this version number is based on the [Package Long Version Code](https://developer.android.com/reference/android/content/pm/PackageInfo.html#getLongVersionCode()) for the app.

For iOS, this version number is based on the [Short Version String](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleshortversionstring) for the app.

{% alert tip %}
This filter will populate values after users upgrade their apps to the supported Braze SDK Versions. Until then, the filter won't show any versions when selected.
{% endalert %}

#### Use case

In the following scenario, let's assume that you first upgraded to the Braze SDKs which supports this filter in version `2.0.0` of your app.

Once Braze receives data from version 2.0.0 of your app, you can target users with earlier or later versions.

| Filter  | User's App Version  | Result |
:------------- | :----------- | :---------|
| Less than 2.0.0 | 1.0.0 | The user is in the segment, even though their Braze SDK did not support the "App Version Number" filter. |
| Greater than 2.0.0 | 2.5.1 | The user and all future installs will be in the segment. |
| Greater than 2.0.0 | 1.9.9 | The user is not in the segment. |
| Less than or equal to 2.0.0 | 3.0.1 | The user is not in the segment. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### App version name

Use the "App Version Name" filter to segment users by the app's user-facing "build name". 

This filter supports matching with "is", "is not", and regular expressions. For example, you can target users who have an app that is not version "1.2.3-test-build".

For Android, this version name is based on the [Package Version Name](https://developer.android.com/reference/android/content/pm/PackageInfo#versionName) for the app. For iOS, this version name is based on the [Short Version String](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleshortversionstring) for the app.

### Have not used feature

When you release a new app version and introduce new features, users may not notice new content. Running a feature awareness campaign is a great way to teach users about new features or features they have never used. To do so, you must create a [custom attribute]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#custom-data) that is assigned to users who have never completed a certain action within your app or use a [custom event]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#custom-data) to track a particular action. You can use this attribute (or event) to segment the users you want to send the campaign to.

{% alert tip %}
Looking to retarget a specific portion of your audience? Check out [Retargeting Campaigns]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/) to learn how to retarget campaigns by leveraging your user's previous actions.
{% endalert %}


