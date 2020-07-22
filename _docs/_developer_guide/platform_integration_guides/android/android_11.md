---
nav_title: Android 11 Upgrade Guide
page_order: 10
platform: Android
hidden: true
---

# Android 11 SDK Upgrade Guide

This guide describes relevant changes introduced in Android 11 (API version 30) and necessary upgrade steps required for the Braze Android SDK integration.

For a full migration guide to Android 11 features, see the [Android Developer Documentation](https://developer.android.com/preview/migration).

## Upgrade Requirements

If your Android app does not yet target the new **Android 11** (API Version 30), then no upgrade steps are required yet.

When your Android app targets **Android 11** (API Version 30), please upgrade to [Braze Android SDK v8.1.0][1].

{% alert warning %}
Apps targeting **Android 11** that do not upgrade to Braze Android SDK v8.1.0 will experience issues with deep linking from Braze UI components and will fail to render HTML In-App Messages.
{% endalert %}

## Braze Android 11 Support

Apps targeting **Android 11** (API 30) must upgrade to [Braze Android SDK v8.1.0][1].

Failure to upgrade to [Braze Android SDK v8.1.0][1] for apps targeting **Android 11** will cause the following Braze features to no longer function as expected:
 
### Deep Links

Links to external URLs from a Braze message (In-App Message or Content Cards) will no longer work on **Android 11** Targeted apps until upgrading to [Braze Android SDK v8.1.0][1]. 

Links from push notifications will continue to work.

### HTML In-App Messages

Due to a change in **Android 11**'s WebView settings, HTML In-App Messages will not be displayed on **Android 11** Targeted apps until upgrading to [Braze Android SDK v8.1.0][1]. 
 
For more information on other **Android 11** behavior changes unrelated to your Braze integration please review the official [Android 11 Behavior Changes](https://developer.android.com/preview/behavior-changes-11)

## Braze-related Android 11 Features

Android 11 introduced [several changes](https://developer.android.com/preview/privacy/location#change-details) to how location permissions are granted.
 
### Allow Once Permissions
Users can now grant permissions, such as Location Collection, on a temporary, one-time basis (see the [Android Docs](https://developer.android.com/preview/privacy/location#one-time-access) for more information). Once an app is closed, or in the background for long enough, that permission will be revoked automatically. The app would need to re-request this permission when needed in the future. Apps that already follow recommended patterns of asking for location likely already support one-time permissions.

![Android Allow Once Permission][3]{: height="230px" }

 
### Background Location 
Android 11 will require apps to first request the foreground location permission, and then after the app is backgrounded it may prompt the user again for Background Location permission. 
Customers using Geofences should ensure their app follows Android’s recommendations on collecting Background Location permission. For more information, see the [Android Docs](https://developer.android.com/preview/privacy/location#background-location).

![Android Background Location Permission][2]{: height="230px" }

[1]: https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#810
[2]: {% image_buster /assets/img/android/android-11-background-location-permission.svg %}
[3]: {% image_buster /assets/img/android/android-11-one-time-permission.svg %}
