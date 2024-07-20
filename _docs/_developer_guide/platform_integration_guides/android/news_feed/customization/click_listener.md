---
nav_title: Handling Clicks Manually
article_title: Handling News Feed Clicks Manually for Android and FireOS
page_order: 3
platform: 
  - Android
  - FireOS
description: "This reference article covers how to manually handle News Feed clicks in your Android or FireOS application."
channel:
  - news feed
  
---

# Handling clicks manually

> This reference article covers how to manually handle News Feed clicks in your Android or FireOS application.

{% alert note %}
News Feed is being deprecated. Braze recommends that customers who use our News Feed tool move over to our Content Cards messaging channel—it's more flexible, customizable, and reliable. Check out the [migration guide]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) for more.
{% endalert %}

You can handle News Feed clicks manually by setting a custom News Feed click listener. This enables use cases such as selectively using the native web browser to open web links.

## Step 1: Implement a News Feed click listener

Create a class that implements [`IFeedClickActionListener`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/feed/listeners/IFeedClickActionListener.java). Implement the `onFeedCardClicked()` method, which will be called when the user clicks a News Feed card.

## Step 2: Instruct Braze to use your News Feed click listener

Once your `IFeedClickActionListener` is created, call `BrazeFeedManager.getInstance().setFeedCardClickActionListener()` to instruct `BrazeFeedManager` to use your custom `IFeedClickActionListener`.

[37]: https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/feed/listeners/IFeedClickActionListener.java
