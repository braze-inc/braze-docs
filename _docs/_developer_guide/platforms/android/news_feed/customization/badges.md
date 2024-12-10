---
nav_title: Badges
article_title: News Feed Badges for Android and FireOS
page_order: 3.2
platform: 
  - Android
  - FireOS
description: "This reference article covers how to add News Feed badges and request unread News Feed card counts to your Android or FireOS application."
channel:
  - news feed
  
---

# Badges

> This reference article covers how to add News Feed badges and request unread News Feed card counts to your Android or FireOS application.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

## Requesting unread News Feed card counts

You can request the number of unread cards at any time by calling:

```java
getUnreadCardCount()
```

Refer to our [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.events/-feed-updated-event/get-unread-card-count.html) for more information.

