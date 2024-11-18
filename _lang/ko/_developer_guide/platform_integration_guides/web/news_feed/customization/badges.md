---
nav_title: 배지
article_title: 웹용 뉴스피드 배지
platform: Web
page_order: 3
page_type: reference
description: "이 문서에서는 미열람 뉴스피드 카드 수를 요청하고 해당 정보를 사용하여 웹 애플리케이션의 배지를 강화하는 방법을 다룹니다."
channel: news feed

---

# 배지

> 이 문서에서는 미열람 뉴스피드 카드 수를 요청하고 해당 정보를 사용하여 웹 애플리케이션의 배지를 강화하는 방법을 다룹니다.

{% alert note %}
뉴스피드는 사용 중지될 예정입니다. Braze는 뉴스피드 도구를 사용하는 고객에게 보다 유연하고 맞춤 설정이 가능하며 안정적인 콘텐츠 카드 메시징 채널로 전환할 것을 권장합니다. 자세한 내용은 [마이그레이션 가이드를]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) 확인하세요.
{% endalert %}

## 미열람 뉴스피드 카드 수 요청

언제든지 전화로 읽지 않은 카드의 수를 요청할 수 있습니다:

``` javascript
braze.getCachedFeed().getUnreadCardCount();
```

종종 미열람 뉴스피드 카드 개수를 나타내는 배지를 구동하는 데 사용됩니다. 자세한 내용은 [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.feed.html)를 참조하세요. Braze는 피드를 표시하거나 `braze.requestFeedRefresh();`를 호출할 때까지 새 페이지를 로드할 때 뉴스피드 카드를 새로 고치지 않으며, 이 함수는 0을 반환합니다.

