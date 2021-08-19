---
nav_title: Android 12 Upgrade Guide
page_order: 9
platform: Android
description: "This reference article covers the Android 12 SDK update, highlighting changes such as deep linking, SDK compatibility, and more."
---

# Android 12 SDK Upgrade Guide

This guide describes relevant changes introduced in Android 12 (2021) and the required upgrade steps for your Braze Android SDK integration.

For a full migration guide of Android 12, see the [Android Developer Documentation](https://developer.android.com/about/versions/12).

## Braze SDK Compatibility

If you are targeting Android 12, you must use [Braze Android SDK v13.1.2+][1]. If you do not target Android 12 yet, upgrading is still recommended.

**What happens if I don’t upgrade my Braze Android SDK?**

* Due to a change in Android’s [Closing System Dialogs](https://developer.android.com/about/versions/12/behavior-changes-all#close-system-dialogs), older versions of the Braze Android SDK will log warnings when receiving push notifications on devices running Android 12. This behavior occurs even if your app does not target Android 12.
* Changes in [component exports](https://developer.android.com/about/versions/12/behavior-changes-12#exported), [pending intents](https://developer.android.com/about/versions/12/behavior-changes-12#pending-intent-mutability), [notification trampolines](https://developer.android.com/about/versions/12/behavior-changes-12#notification-trampolines) may impact your ability to compile your app, or may prevent the Braze SDK from initializing. This behavior occurs only for apps targeting Android 12.
* Changes in [custom push notifications](https://developer.android.com/about/versions/12/behavior-changes-12#custom-notifications) have changed the layout for our new [Android Inline Image Push](https://www.braze.com/docs/developer_guide/platform_integration_guides/android/push_notifications/inline_image_push/) feature. This behavior occurs only for apps targeting Android 12.

[1]: https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#1312
