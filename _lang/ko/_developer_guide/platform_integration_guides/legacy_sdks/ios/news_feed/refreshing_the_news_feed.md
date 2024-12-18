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

{% alert note %}
뉴스피드는 사용 중지될 예정입니다. Braze는 뉴스피드 도구를 사용하는 고객에게 보다 유연하고 맞춤 설정이 가능하며 안정적인 콘텐츠 카드 메시징 채널로 전환할 것을 권장합니다. 자세한 내용은 [마이그레이션 가이드를]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) 확인하세요.
{% endalert %}

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


