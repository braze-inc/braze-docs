---
nav_title: 뉴스피드
article_title: tvOS용 뉴스 피드
platform: tvOS
page_order: 10
page_type: reference
description: "이 페이지에서는 tvOS 애플리케이션에서 뉴스피드 데이터를 가져오고 표시하는 방법에 대해 설명합니다."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 뉴스피드 통합

> 이 도움말 문서에서는 tvOS 플랫폼용 뉴스피드를 설정하는 방법에 대해 설명합니다.

{% alert note %}
뉴스피드는 사용 중지될 예정입니다. Braze는 뉴스피드 도구를 사용하는 고객에게 보다 유연하고 맞춤 설정이 가능하며 안정적인 콘텐츠 카드 메시징 채널로 전환할 것을 권장합니다. 자세한 내용은 [마이그레이션 가이드를]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) 확인하세요.
{% endalert %}

## tvOS 피드 통합

tvOS SDK는 뉴스피드 데이터 가져오기를 지원하므로 커스텀 UI로 애플리케이션에 뉴스피드를 표시할 수 있습니다. 뉴스피드를 가져오려면 다음 메서드를 호출한 다음, 해당 클래스를 검사하여 각 카드를 구문 분석합니다.

{% tabs %}
{% tab 목표-C %}

```objc
NSArray *feedCards =  [[Appboy sharedInstance].feedController getNewsFeedCards];
```

{% endtab %}
{% tab swift %}

```swift
let feedCards = Appboy.sharedInstance()?.feedController.newsFeedCards
```

{% endtab %}
{% endtabs %}
