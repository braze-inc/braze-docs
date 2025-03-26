---
nav_title: Definieren einer Newsfeed-Kategorie
article_title: Definieren einer News Feed Kategorie für Android und FireOS
page_order: 3
platform: 
  - Android
  - FireOS
description: "In diesem Referenzartikel erfahren Sie, wie Sie eine Newsfeed-Kategorie in Ihrer Android- oder FireOS-Anwendung definieren."
channel:
  - news feed
  
---

# Definieren einer Newsfeed-Kategorie

In diesem Referenzartikel erfahren Sie, wie Sie eine Newsfeed-Kategorie in Ihrer Android- oder FireOS-Anwendung definieren.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Instanzen des Braze News Feed können so konfiguriert werden, dass sie nur Karten aus einer bestimmten "Kategorie" empfangen. Dies ermöglicht die effektive Integration mehrerer Newsfeed-Streams in einer einzigen Anwendung. Weitere Informationen zu dieser Funktion finden Sie in unseren [Best Practices für]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/) News Feeds

News Feed-Kategorien können durch den Aufruf der folgenden Methoden beim Laden des News Feeds definiert werden:

```xml
newsFeed.setCategories(CardCategory.ALL_CATEGORIES);
newsFeed.setCategories(CardCategory.ADVERTISING);
newsFeed.setCategories(CardCategory.ANNOUNCEMENTS);
newsFeed.setCategories(CardCategory.NEWS);
newsFeed.setCategories(CardCategory.SOCIAL);
newsFeed.setCategories(CardCategory.NO_CATEGORY);
```

Sie können einen Feed auch wie im folgenden Beispiel mit einer Kombination von Kategorien füllen:

```xml
newsFeed.setCategories:EnumSet.of(CardCategory.ANNOUNCEMENTS, CardCategory.NEWS);
```


