---
nav_title: Gelesen- und Ungelesen-Anzeigen
article_title: Newsfeed Lese- und Ungelesen-Anzeigen für das Internet
platform: Web
page_order: 2
page_type: reference
description: "Dieser Artikel beschreibt, wie Sie über das Braze SDK Ungelesen-Anzeigen in Ihren Newsfeed-Karten setzen können."
channel: news feed

---

# Indikatoren für gelesen und ungelesen

> Dieser Artikel beschreibt, wie Sie über das Braze SDK Ungelesen-Anzeigen in Ihren Newsfeed-Karten setzen können.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Braze bietet eine Anzeige für ungelesene und gelesene Newsfeed-Karten, wie in der folgenden Abbildung gezeigt:

![Eine News-Feed-Karte, die ein Bild einer Uhr zusammen mit etwas Text zeigt. In der oberen Ecke des Textes befindet sich ein blaues oder graues Dreieck, das anzeigt, ob eine Karte gelesen wurde oder nicht. Ein blaues Dreieck zeigt an, dass eine Karte gelesen wurde.]({% image_buster /assets/img_archive/UnreadvsReadNewsFeedCard.png %})

## Deaktivieren der Indikatoren

Um diese Funktion zu deaktivieren, fügen Sie den folgenden Stil zu Ihrem CSS hinzu:

``` css
.ab-read-dot { display: none; }
.ab-read-indicator { display: none; }
```

