---
nav_title: Handling Clicks Manually
article_title: Handling News Feed Clicks Manually for Android and FireOS
page_order: 3
platform: 
  - Android
  - FireOS
description: "This reference article covers how to customize your News Feed in your Android application."
channel:
  - news feed
  
---

# Handling clicks manually

You can handle News Feed clicks manually by setting a custom News Feed click listener. This enables use cases such as selectively using the native web browser to open web links.

## Step 1: Implement a News Feed click listener

Create a class that implements [`IFeedClickActionListener`][37]. Implement the `onFeedCardClicked()` method, which will be called when the user clicks a News Feed card.

## Step 2: Instruct Braze to use your News Feed click listener

Once your `IFeedClickActionListener` is created, call `AppboyFeedManager.getInstance().setFeedCardClickActionListener()` to instruct `AppboyFeedManager` to use your custom `IFeedClickActionListener`.

[37]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/main/java/com/appboy/ui/feed/listeners/IFeedClickActionListener.java
