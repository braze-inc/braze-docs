---
nav_title: Badges
article_title: News Feed Badges for Web
platform: Web
page_order: 3
page_type: reference
description: "This article covers how to request the unread News Feeds card count for your web applcation."
channel: news feed

---

# Badges

## Requesting unread News Feed card counts

You can request the number of unread cards at any time by calling:

``` javascript
braze.getCachedFeed().getUnreadCardCount();
```

This is often used to power badges signifying how many unread News Feed cards there are. See the [JSDocs][17] for more information. Note that Braze will not refresh News Feed cards on new page loads (and so this function will return 0) until you show the feed or call `braze.requestFeedRefresh();`

[17]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.feed.html
