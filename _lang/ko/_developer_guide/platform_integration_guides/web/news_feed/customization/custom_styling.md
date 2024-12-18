---
nav_title: 사용자 지정 스타일
article_title: 웹용 뉴스피드 사용자 지정 스타일링
platform: Web
page_order: 0
page_type: reference
description: "이 문서에서는 웹 애플리케이션의 사용자 지정 뉴스피드 스타일링 옵션에 대해 설명합니다."
channel: news feed

---

# 사용자 지정 스타일

> 이 문서에서는 웹 애플리케이션의 사용자 지정 뉴스피드 스타일링 옵션에 대해 설명합니다.

{% alert note %}
뉴스피드는 사용 중지될 예정입니다. Braze는 뉴스피드 도구를 사용하는 고객에게 보다 유연하고 맞춤 설정이 가능하며 안정적인 콘텐츠 카드 메시징 채널로 전환할 것을 권장합니다. 자세한 내용은 [마이그레이션 가이드를]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) 확인하세요.
{% endalert %}

Braze UI 요소는 Braze 대시보드 내 작성기와 일치하는 기본 모양과 느낌을 사용하며, 다른 Braze 모바일 플랫폼과의 일관성을 목표로 합니다. 기본 스타일은 Braze SDK 내 CSS에서 정의됩니다. 애플리케이션에서 선택한 스타일을 재정의하여 나만의 배경 이미지, 글꼴 모음, 스타일, 크기, 애니메이션 등으로 표준 피드를 맞춤 설정할 수 있습니다.

예를 들어, 다음은 뉴스피드를 800px 너비로 표시하는 재정의 예제입니다.

``` css
body .ab-feed {
  width: 800px;
}
```