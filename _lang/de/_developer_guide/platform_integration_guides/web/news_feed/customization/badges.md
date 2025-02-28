---
nav_title: Abzeichen
article_title: News Feed Badges für das Web
platform: Web
page_order: 3
page_type: reference
description: "In diesem Artikel erfahren Sie, wie Sie die Anzahl der ungelesenen News Feeds abfragen und diese Informationen zur Erstellung von Badges für Ihre Webanwendung verwenden können."
channel: news feed

---

# Abzeichen

> In diesem Artikel erfahren Sie, wie Sie die Anzahl der ungelesenen News Feeds abfragen und diese Informationen zur Erstellung von Badges für Ihre Webanwendung verwenden können.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

## Abfrage der Anzahl ungelesener News Feed Karten

Sie können die Anzahl der ungelesenen Karten jederzeit telefonisch erfragen:

``` javascript
braze.getCachedFeed().getUnreadCardCount();
```

Dies wird oft verwendet, um die Anzahl der ungelesenen News Feed-Karten anzuzeigen. In den [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.feed.html) finden Sie weitere Informationen. Beachten Sie, dass Braze die Newsfeed-Cards beim Laden einer neuen Seite nicht aktualisiert (und diese Funktion daher 0 zurückgibt), bis Sie den Feed anzeigen oder `braze.requestFeedRefresh();` aufrufen.

