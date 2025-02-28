---
nav_title: Newsfeed
article_title: Newsfeed für tvOS
platform: tvOS
page_order: 10
page_type: reference
description: "Diese Seite beschreibt, wie Sie Daten aus dem Newsfeed in Ihrer tvOS-Anwendung abrufen und anzeigen können."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Integration von News Feeds

> Dieser Artikel beschreibt, wie Sie einen Newsfeed für die tvOS-Plattform einrichten.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

## tvOS Integration von Feeds

Unser tvOS SDK unterstützt den Abruf Ihrer News-Feed-Daten, so dass Sie den News-Feed in Ihrer Anwendung mit Ihrer eigenen angepassten UI anzeigen können. Um den Newsfeed abzurufen, rufen Sie die folgenden Methoden auf und analysieren dann jede Karte, indem Sie ihre Klasse inspizieren.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
NSArray *feedCards =  [[Appboy sharedInstance].feedController getNewsFeedCards];
```

{% endtab %}
{% tab schnell %}

```swift
let feedCards = Appboy.sharedInstance()?.feedController.newsFeedCards
```

{% endtab %}
{% endtabs %}
