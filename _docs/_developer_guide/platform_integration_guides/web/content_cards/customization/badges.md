---
nav_title: Badges
article_title: Requesting Unviewed Content Card for Badges for Web
page_order: 4
platform: Web
channel: content cards
page_type: reference
description: "This reference article describes how to request the number of unread Content Cards for your web application."

---

# Badges

## Requesting unread Content Card counts

You can request the number of unread cards at any time by calling:

``` javascript
braze.getCachedContentCards().getUnviewedCardCount();
```

This is often used to power badges signifying how many unread Content Cards there are. See the [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.contentcards.html)for more information.

{% comment %}
Braze will not refresh Content Cards on new page loads (and so this function will return 0) until you show the feed or call `braze.requestContentCardsRefresh();`.
{% endcomment %}
