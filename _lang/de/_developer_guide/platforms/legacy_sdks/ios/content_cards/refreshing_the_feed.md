---
nav_title: Aktualisieren des Feeds
article_title: Aktualisieren des Content-Card Feeds für iOS
platform: iOS
page_order: 4
description: "Dieser Referenzartikel behandelt die Aktualisierung von Content-Cards in Ihrer iOS-Anwendung."
channel:
  - content cards

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Aktualisieren des Feeds

## Aktualisieren von Inhaltskarten

Sie können Braze manuell anfragen, die Content-Cards des Nutzers mit der Methode `requestContentCardsRefresh:` auf der Schnittstelle `Appboy` zu aktualisieren:
{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] requestContentCardsRefresh];
```

{% endtab %}
{% tab schnell %}

```swift
Appboy.sharedInstance()?.requestContentCardsRefresh()
```

{% endtab %}
{% endtabs %}

Weitere Informationen finden Sie in der [Header-Datei](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h) `Appboy.h`.
