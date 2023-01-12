---
nav_title: Badges
article_title: News Feed Badges for Android and FireOS
page_order: 3.2
platform: 
  - Android
  - FireOS
description: "This reference article covers how to add News Feed badges to your Android or FireOS application."
channel:
  - news feed
  
---

# Badges

{% alert note %}
News Feed is being deprecated. Braze recommends that customers who use our News Feed tool move over to our Content Cards messaging channel—it's more flexible, customizable, and reliable. Check out the [migration guide]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) for more.
{% endalert %}

## Requesting unread News Feed card counts

You can request the number of unread cards at any time by calling:

```java
getUnreadCardCount()
```

Refer to our [KDoc][17] for more information.

[17]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy.events/-feed-updated-event/get-unread-card-count.html
