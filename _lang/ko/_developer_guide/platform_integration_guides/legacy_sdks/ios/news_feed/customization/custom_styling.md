---
nav_title: 사용자 지정 스타일
article_title: iOS용 커스텀 뉴스피드 스타일링
platform: iOS
page_order: 0
description: "이 참조 문서는 iOS 애플리케이션에서 커스텀 뉴스피드 스타일을 구현하고 기본값 이미지를 재정의하는 방법을 다룹니다."
channel:
  - news feed

noindex: true
---

{% multi_lang_include 사용 중단/목적-c.md %}

# 사용자 지정 스타일

{% alert note %}
뉴스피드는 사용 중지될 예정입니다. Braze는 뉴스피드 도구를 사용하는 고객이 더 유연하고, 맞춤화 가능하며, 신뢰할 수 있는 콘텐츠 카드 메시징 채널로 이동할 것을 권장합니다. 자세한 내용은 [마이그레이션 가이드]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/)를 확인하세요.
{% endalert %}

iOS 인앱 메시지, 뉴스피드 또는 콘텐츠 카드 내에서 이미지를 표시하기 위해 Braze UI를 사용하려는 경우 `SDWebImage`의 통합이 필요합니다.

## 기본값 이미지를 재정의

Braze는 클라이언트가 기존 기본 이미지를 자신만의 커스텀 이미지로 교체할 수 있도록 합니다. 이를 달성하려면 커스텀 이미지를 사용하여 새 `png` 파일을 만들고 이를 앱의 이미지 번들에 추가하십시오. 그런 다음, 라이브러리의 기본 이미지를 덮어쓰도록 이미지 이름으로 파일 이름을 변경합니다. 또한 다양한 전화기 크기에 맞추기 위해 `@2x` 및 `@3x` 버전의 이미지를 업로드해야 합니다. 콘텐츠 카드에서 재정의할 수 있는 이미지에는 다음이 포함됩니다: 뉴스피드에서 재정의할 수 있는 이미지 포함:

* 아이콘 표시기 읽기: `Icons_Read`
* 입력 안내 이미지: `img-noimage-lrg`

{% alert important %}
Xamarin iOS 통합에서 기본값 이미지를 재정의하는 것은 현재 지원되지 않습니다.
{% endalert %}

