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

You can queue a manual refresh of the Braze Content Cards at any time by calling [`requestContentCardsRefresh()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestcontentcardsrefresh). 

You can also call [`getCachedContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getcachedcontentcards) to get all currently available cards from the last Content Cards refresh. 

The feed will refresh automatically on new session or when the feed is opened and more than 60 seconds have elapsed since the last refresh.

{% alert important %}
Usage of `requestContentCardsRefresh` may be rate limited under certain conditions. For more details around this, contact your Customer Success Manager or Account Team.

Please try to limit these calls to 3 calls per 10 minutes. These limits will be imposed on the SDK-side in the future.
{% endalert %}
