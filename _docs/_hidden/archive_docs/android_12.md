---
nav_title: Android 12 upgrade guide
article_title: Android 12 Upgrade Guide
page_order: 9
permalink: "/android_12/"
layout: "dev_guide"
hidden: true
platform: 
  - Android
  - FireOS
description: "This reference article covers the Android 12 SDK update, highlighting changes such as deep linking, SDK compatibility, and more."
---

# Android 12 SDK upgrade guide

This guide describes relevant changes introduced in Android 12 (2021) and the required upgrade steps for your Braze Android SDK integration.

For a full Android 12 migration guide, see the [Android developer documentation](https://developer.android.com/about/versions/12).

## Braze SDK compatibility

If you target Android 12, you must use [Braze Android SDK v13.1.2+](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#1312). If you do not target Android 12 yet, upgrading is still recommended.

**What happens if I don't upgrade my Braze Android SDK?**

* Due to a change in Android's [closing system dialogs](https://developer.android.com/about/versions/12/behavior-changes-all#close-system-dialogs), older versions of the Braze Android SDK will log warnings when receiving push notifications on devices running Android 12. This behavior occurs even if your app does not target Android 12.
* Changes in [component exports](https://developer.android.com/about/versions/12/behavior-changes-12#exported), [pending intents](https://developer.android.com/about/versions/12/behavior-changes-12#pending-intent-mutability), and [notification trampolines](https://developer.android.com/about/versions/12/behavior-changes-12#notification-trampolines) may impact your ability to compile your app or may prevent the Braze SDK from initializing. This behavior occurs only for apps targeting Android 12.
* Changes in [custom push notifications](https://developer.android.com/about/versions/12/behavior-changes-12#custom-notifications) have changed the layout for our new [Android inline image push]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android#android_sending-inline-images) feature. This behavior occurs only for apps targeting Android 12.

