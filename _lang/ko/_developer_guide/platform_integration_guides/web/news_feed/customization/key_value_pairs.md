---
nav_title: 키-값 쌍
article_title: 웹용 뉴스 피드 키-값 쌍
platform: Web
page_order: 1
page_type: reference
description: "이 문서에서는 Braze SDK를 통해 뉴스피드 카드에서 키-값 페어를 사용하는 방법을 다룹니다."
channel: news feed

---

# 키-값 쌍

> 이 문서에서는 Braze SDK를 통해 뉴스피드 카드에서 키-값 페어를 사용하는 방법을 다룹니다.

{% alert note %}
뉴스피드는 사용 중지될 예정입니다. Braze는 뉴스피드 도구를 사용하는 고객에게 보다 유연하고 맞춤 설정이 가능하며 안정적인 콘텐츠 카드 메시징 채널로 전환할 것을 권장합니다. 자세한 내용은 [마이그레이션 가이드를]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) 확인하세요.
{% endalert %}

`Card` 오브젝트는 선택적으로 키-값 페어를 `extras`와 같이 전달할 수 있습니다. 애플리케이션에서 추가 처리를 위해 카드와 함께 데이터를 전송하는 데 사용할 수 있습니다. `card.extras`를 호출하여 이러한 값에 액세스합니다.

[ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html), [ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html), [CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html)에 대한 자세한 내용은 JSDocs를 참조하세요.

