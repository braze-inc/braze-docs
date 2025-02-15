---
nav_title: 피드 새로 고침
article_title: iOS용 뉴스피드 새로 고침하기
platform: iOS
page_order: 6
description: "이 참조 문서에서는 iOS 애플리케이션에서 뉴스피드를 새로 고치는 방법을 설명합니다."
channel:
  - news feed

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 뉴스피드 새로 고침

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

`- (void) requestFeedRefresh;`를 사용하여 `Appboy.h`에서 사용자의 뉴스피드를 새로 고치도록 Braze에 수동으로 요청할 수 있습니다. 예를 들어, 다음과 같습니다.

{% tabs %}
{% tab 목표-C %}

```objc
[[Appboy sharedInstance] requestFeedRefresh];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.requestFeedRefresh()
```

{% endtab %}
{% endtabs %}

자세한 내용은 `Appboy.h` [헤더 파일](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h "Appboy.h 헤더 파일을") 참조하세요.


