# Handling clicks manually

> This reference article covers how to manually handle News Feed clicks in your Android or FireOS application.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

You can handle News Feed clicks manually by setting a custom News Feed click listener. This enables use cases such as selectively using the native web browser to open web links.

## Step 1: Implement a News Feed click listener

Create a class that implements [`IFeedClickActionListener`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/feed/listeners/IFeedClickActionListener.java). Implement the `onFeedCardClicked()` method, which will be called when the user clicks a News Feed card.

## Step 2: Instruct Braze to use your News Feed click listener

Once your `IFeedClickActionListener` is created, call `BrazeFeedManager.getInstance().setFeedCardClickActionListener()` to instruct `BrazeFeedManager` to use your custom `IFeedClickActionListener`.

