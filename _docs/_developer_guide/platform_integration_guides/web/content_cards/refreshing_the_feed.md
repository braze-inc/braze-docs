---
nav_title: Refreshing the Feed
article_title: Refreshing the Content Card Feed for Web
page_order: 2
platform: Web
channel: content cards
page_type: reference
description: "This reference article describes how to queue a manual refresh of your Content Cards for your web application."

---

# Refreshing the feed

> This reference article describes how to queue a manual refresh of your Content Cards for your web application.

{% alert tip %}
To dynamically show up-to-date Content Cards without manually refreshing, select **At first impression** during card creation. These cards will be refreshed after they are available.
{% endalert %}

You can queue a manual refresh of the Braze Content Cards at any time by calling [`requestContentCardsRefresh()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestcontentcardsrefresh). 

You can also call [`getCachedContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getcachedcontentcards) to get all currently available cards from the last Content Cards refresh. 

The feed will refresh automatically on new session or when the feed is opened and more than 60 seconds have elapsed since the last refresh.

{% alert important %}
The default rate limit for calling `requestContentCardsRefresh()` is 3 calls per 10 minutes per device to prevent performance degradation and errors.
{% endalert %}