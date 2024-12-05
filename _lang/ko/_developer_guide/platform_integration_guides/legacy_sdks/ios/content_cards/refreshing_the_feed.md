---
nav_title: 피드 새로 고침
article_title: iOS용 콘텐츠 카드 피드 새로 고침
platform: iOS
page_order: 4
description: "이 참조 문서에서는 iOS 애플리케이션에서 콘텐츠 카드 새로 고침을 구현하는 방법에 대해 설명합니다."
channel:
  - content cards

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 피드 새로 고침

## 콘텐츠 카드 새로 고침

`Appboy` 인터페이스에서 `requestContentCardsRefresh:` 방법을 사용하여 사용자의 콘텐츠 카드를 새로 고치도록 Braze에 수동으로 요청할 수 있습니다:
{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] requestContentCardsRefresh];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.requestContentCardsRefresh()
```

{% endtab %}
{% endtabs %}

자세한 내용은 `Appboy.h` [헤더 파일을](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h) 참조하세요.
