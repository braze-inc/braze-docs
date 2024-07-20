---
nav_title: Refreshing the Feed
article_title: Refreshing the News Feed for Android and FireOS
page_order: 7
platform: 
  - Android
  - FireOS
description: "This reference article shows how to refresh the News Feed in your Android or FireOS application."
channel:
  - news feed

---

# Refreshing the feed

> This reference article shows how to refresh the News Feed in your Android or FireOS application.

{% alert note %}
News Feed is being deprecated. Braze recommends that customers who use our News Feed tool move over to our Content Cards messaging channel—it's more flexible, customizable, and reliable. Check out the [migration guide]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) for more.
{% endalert %}

You can queue a manual refresh of the Braze News Feed at any time by calling:

```java
Braze.requestFeedRefresh()
```

Refer to our [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-feed-refresh.html) for more information.


