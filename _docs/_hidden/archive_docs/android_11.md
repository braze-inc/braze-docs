---
nav_title: Android 11 upgrade guide
article_title: Android 11 Upgrade Guide
page_order: 9
platform: 
  - Android
  - FireOS
description: "This reference article covers the Android 11 SDK update, highlighting changes such as deep linking, SDK compatibility, and more."
hidden: true
---

# Android 11 SDK upgrade guide

This guide describes relevant changes introduced in Android 11 (released September 8, 2020) and the required upgrade steps for your Braze Android SDK integration.

For a full migration guide of Android 11, see the [Android developer documentation](https://developer.android.com/preview/migration).

## Braze SDK compatibility

All apps that _target_ Android 11 (API 30) must upgrade to [Braze Android SDK v8.1.0+](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#810) to continue using Braze messaging features.

{% alert important %}
Due to changes in Android 11's APIs, apps targeting Android 11 that do not upgrade to Braze Android SDK v8.1.0+ will experience issues with deep linking from Braze UI components and will not properly display custom HTML in-app messages.
{% endalert %}

### Deep links

Apps targeting Android 11 or later (API Version 30+) must upgrade to [Braze Android SDK v8.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#810) to continue using deep links within Braze messages. Due to a change in Android 11 APIs, apps that do not upgrade to at least Android SDK v8.1.0 will experience issues with deep links within Braze messages (in-app messages or Content Cards).

### HTML in-app messages

Apps targeting Android 11 or later (API Version 30+) must upgrade to Braze Android SDK v8.1.0 to continue using custom HTML in-app messages. Due to a change in Android 11 WebView settings, HTML in-app messages will not properly display on Android 11 targeted apps until upgrading to [Braze Android SDK v8.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#810). 

### Location permissions

Apps using location permissions should follow Android's [best practices](https://developer.android.com/preview/privacy/location#change-details) when requesting location access. No changes to your Braze integration are necessary for these location updates.

## Android 11 behavior changes

### Allow once permissions

Users can now grant permissions, such as location collection, on a one-time basis (see the [Android Docs](https://developer.android.com/preview/privacy/location#one-time-access) for more information). After an app is closed or in the background for long enough, that permission will be revoked automatically. The app would need to re-request this permission when needed in the future. Apps that already follow the recommended flow for requesting location permissions will support one-time permissions.

![]({% image_buster /assets/img/android/android-11-one-time-permission.svg %}){: height="230px" }

### Background location permission

Android 11 will require apps to first request the foreground location permission, and then after the app is in the background, it may prompt the user again for background location permission. 
Customers using Geofences should ensure their app follows Android's recommendations on collecting background location permission. For more information, see the [Android Docs](https://developer.android.com/preview/privacy/location#background-location).

