---
nav_title: 뉴스피드 카테고리 정의하기
article_title: 웹용 뉴스피드 카테고리 정의하기
platform: Web
page_order: 3
page_type: reference
description: "이 문서에서는 웹 애플리케이션의 뉴스피드 카테고리를 정의하는 방법에 대해 설명합니다."
channel: news feed

---

# 뉴스피드 카테고리 정의하기

> 이 문서에서는 Braze 웹 SDK의 뉴스피드 카테고리를 정의하는 방법에 대해 설명합니다.

{% alert note %}
뉴스피드는 사용 중지될 예정입니다. Braze는 뉴스피드 도구를 사용하는 고객에게 보다 유연하고 맞춤 설정이 가능하며 안정적인 콘텐츠 카드 메시징 채널로 전환할 것을 권장합니다. 자세한 내용은 [마이그레이션 가이드를]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) 확인하세요.
{% endalert %}

Braze 뉴스피드의 인스턴스는 특정 '카테고리'의 카드만 수신하도록 구성할 수 있습니다. 이를 통해 단일 애플리케이션 내에서 여러 개의 뉴스피드 스트림을 효과적으로 통합할 수 있습니다.

뉴스피드 카테고리는 `toggleFeed` 에 세 번째 `allowedCategories` 파라미터를 제공하여 정의할 수 있습니다:

``` javascript
braze.toggleFeed(undefined, undefined, [braze.Card.Category.NEWS]);
```

다음 예시와 같이 여러 카테고리의 조합으로 피드를 채울 수도 있습니다:

``` javascript
braze.toggleFeed(undefined, undefined, [braze.Card.Category.ANNOUNCEMENTS, braze.Card.Category.NEWS]);
```
