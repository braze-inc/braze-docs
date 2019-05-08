---
nav_title: Refreshing the Feed
page_order: 3
search_rank: 3
platform: Web
---

# Refreshing Content Cards

 You can queue a manual refresh of the Braze Content Cards at any time by calling:

`requestContentCardsRefresh()`

This will get all currently available cards from the last content cards refresh.

[JS Docs for getCachedContentCards](https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.getCachedContentCards)

The feed will refresh automatically on new session or when the feed is opened and more than 60 seconds have elapsed since the last refresh.
