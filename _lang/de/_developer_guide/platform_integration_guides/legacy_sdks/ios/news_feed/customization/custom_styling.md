---
nav_title: Angepasste Stile
article_title: Angepasstes Newsfeed-Styling für iOS
platform: iOS
page_order: 0
description: "In diesem referenzierten Artikel erfahren Sie, wie Sie angepasste Stile für den Newsfeed implementieren und die Standard-Bilder in Ihrer iOS-Anwendung außer Kraft setzen."
channel:
  - news feed

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Angepasste Stile

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Die Integration von `SDWebImage` ist erforderlich, wenn Sie unser Braze UI für die Anzeige von Bildern in In-App-Nachrichten, News Feed oder Content-Cards verwenden möchten.

## Überschreiben der Standardbilder

Braze ermöglicht es Kunden, vorhandene Standardbilder durch eigene angepasste Bilder zu ersetzen. Erstellen Sie dazu eine neue `png`-Datei mit dem angepassten Bild und fügen Sie sie dem Bild-Bundle der App hinzu. Benennen Sie dann die Datei in den Namen des Bildes um, um das Standardbild in unserer Bibliothek zu überschreiben. Stellen Sie außerdem sicher, dass Sie die Versionen `@2x` und `@3x` der Bilder hochladen, damit sie für verschiedene Handygrößen geeignet sind. Folgende Bilder können in Content-Cards überschrieben werden: Zu den Bildern, die für eine Überschreibung im Newsfeed zur Verfügung stehen, gehören:

* Gelesen-Anzeigesymbole: `Icons_Read`
* Platzhalterbild: `img-noimage-lrg`

{% alert important %}
Das Überschreiben von Standardbildern wird in unserer Xamarin iOS-Integration derzeit nicht unterstützt.
{% endalert %}

