---
nav_title: Angepasste Stile
article_title: Newsfeed Angepasster Stile für das Internet
platform: Web
page_order: 0
page_type: reference
description: "Dieser Artikel behandelt die angepassten Stile von Newsfeeds für Ihre Internet-Anwendung."
channel: news feed

---

# Angepasste Stile

> Dieser Artikel behandelt die angepassten Stile von Newsfeeds für Ihre Internet-Anwendung.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Die UI-Elemente von Braze sind standardmäßig an die Editoren im Braze-Dashboard angepasst und auf Konsistenz mit anderen Mobilgeräte-Plattformen von Braze ausgelegt. Die Standardstile von Braze sind im Braze SDK in CSS definiert. Indem Sie ausgewählte Stile in Ihrer Anwendung außer Kraft setzen, können Sie unseren Standard-Feed mit Ihren eigenen Hintergrundbildern, Schriftfamilien, Stilen, Größen, Animationen und vielem mehr anpassen.

Im Folgenden finden Sie ein Beispiel für eine Überschreibung, die bewirkt, dass der News Feed 800 px breit erscheint:

``` css
body .ab-feed {
  width: 800px;
}
```