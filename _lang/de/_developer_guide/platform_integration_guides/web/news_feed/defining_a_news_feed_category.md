---
nav_title: Definieren einer Newsfeed-Kategorie
article_title: Definieren einer Newsfeed-Kategorie für das Internet
platform: Web
page_order: 3
page_type: reference
description: "Dieser Artikel beschreibt, wie Sie eine Newsfeed-Kategorie für Ihre Internet-Anwendung definieren."
channel: news feed

---

# Definieren einer Newsfeed-Kategorie

> Dieser Artikel beschreibt, wie Sie eine Newsfeed-Kategorie für das Braze Web SDK definieren.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Instanzen des Braze News Feed können so konfiguriert werden, dass sie nur Karten aus einer bestimmten "Kategorie" empfangen. Dies ermöglicht die effektive Integration mehrerer Newsfeed-Streams in einer einzigen Anwendung.

Newsfeed-Kategorien können definiert werden, indem der dritte `allowedCategories`-Parameter an `toggleFeed` übergeben wird:

``` javascript
braze.toggleFeed(undefined, undefined, [braze.Card.Category.NEWS]);
```

Sie können einen Feed auch mit einer Kombination von Kategorien bestücken, wie im folgenden Beispiel:

``` javascript
braze.toggleFeed(undefined, undefined, [braze.Card.Category.ANNOUNCEMENTS, braze.Card.Category.NEWS]);
```
