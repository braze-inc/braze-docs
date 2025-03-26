---
nav_title: Gelesen &amp; Ungelesen Indikatoren
article_title: Anzeigen für gelesene und ungelesene News Feeds für Android und FireOS
page_order: 3.1
platform: 
  - Android
  - FireOS
description: "Dieser Referenzartikel behandelt die Anzeigen für gelesene und ungelesene News Feeds in Ihrer Android- oder FireOS-Anwendung."
channel:
  - news feed
  
---

# Indikatoren für gelesen und ungelesen

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

> Mit Braze können Sie optional die Anzeigen für ungelesene und gelesene Nachrichten auf den News Feed-Karten einschalten.

![Eine News-Feed-Karte, die ein Bild einer Uhr zusammen mit etwas Text zeigt. In der oberen Ecke des Textes befindet sich ein blaues oder graues Dreieck, das anzeigt, ob eine Karte gelesen wurde oder nicht. Ein blaues Dreieck zeigt an, dass eine Karte gelesen wurde.]({% image_buster /assets/img_archive/UnreadvsReadNewsFeedCard.png %})

## Aktivieren der Indikatoren

Um diese Funktion zu aktivieren, fügen Sie die folgende Zeile in die Datei `braze.xml` ein:

```xml
<bool name="com_braze_newsfeed_unread_visual_indicator_on">true</bool>
```

## Anpassen der Indikatoren

Diese Indikatoren können durch Ändern der Drawables `icon_read` und `icon_unread` angepasst werden.

