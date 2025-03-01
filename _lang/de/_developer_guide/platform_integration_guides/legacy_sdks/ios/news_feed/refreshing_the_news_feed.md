---
nav_title: Aktualisieren des Feeds
article_title: Aktualisieren des Newsfeeds für iOS
platform: iOS
page_order: 6
description: "Dieser Referenzartikel zeigt, wie Sie den Newsfeed in Ihrer iOS-Anwendung aktualisieren können."
channel:
  - news feed

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Aktualisieren des Newsfeeds

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Sie können Braze manuell auffordern, den Newsfeed des Benutzers in `Appboy.h` zu aktualisieren, indem Sie `- (void) requestFeedRefresh;` verwenden. Zum Beispiel:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] requestFeedRefresh];
```

{% endtab %}
{% tab schnell %}

```swift
Appboy.sharedInstance()?.requestFeedRefresh()
```

{% endtab %}
{% endtabs %}

Weitere Informationen finden Sie in der `Appboy.h` [Header-Datei](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h "Appboy.h Header File").


