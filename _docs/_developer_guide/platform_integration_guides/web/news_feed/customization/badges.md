---
nav_title: Badges
article_title: News Feed Badges for Web
platform: Web
page_type: reference
description: "This article covers how to request the unread News Feeds card count and use that information to power badges for your web application."
channel: news feed

---

# Badges

> This article covers how to request the unread News Feeds card count and use that information to power badges for your web application.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

## Requesting unread News Feed card counts

You can request the number of unread cards at any time by calling:

``` javascript
braze.getCachedFeed().getUnreadCardCount();
```

This is often used to power badges signifying how many unread News Feed cards there are. See the [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.feed.html) for more information. Note that Braze will not refresh News Feed cards on new page loads (and so this function will return 0) until you show the feed or call `braze.requestFeedRefresh();`

