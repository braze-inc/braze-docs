---
nav_title: Integration Overview
article_title: News Feed Integration Overview for Android and FireOS
page_order: 1
platform: 
  - Android
  - FireOS
description: "This article covers an overview of how to integrate the News Feed into your Android application."
channel:
  - news feed
  
---

# News Feed integration overview

In Android, the News Feed is implemented as a [fragment][2] available in the Braze Android UI project. Refer to Google's documentation on [Fragments][3] for information on adding a fragment to an activity.

The `AppboyFeedFragment` class will automatically refresh and display the contents of the News Feed and log usage analytics. The cards that can appear in a user's News Feed are set on the Braze dashboard.

## Session analytics

The Android UI fragments do not automatically track session analytics. To ensure that sessions are [tracked correctly][4], call `IAppboy.openSession()` when your app is opened.

## Linking

Linking to the News Feed from an in-app message must be enabled by registering the `AppboyFeedActivity` within your `AndroidManifest.xml`.


[2]: http://developer.android.com/guide/components/fragments.html
[3]: http://developer.android.com/guide/components/fragments.html#Adding "Android Documentation: Fragments"
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/
