---
nav_title: 사용자 지정 스타일
article_title: iOS용 커스텀 뉴스피드 스타일링
platform: iOS
page_order: 0
description: "이 참조 문서에서는 iOS 애플리케이션에서 커스텀 뉴스피드 스타일을 구현하고 기본 이미지를 재정의하는 방법을 다룹니다."
channel:
  - news feed

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 사용자 지정 스타일

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

iOS 인앱 메시지, 뉴스피드 또는 콘텐츠 카드에서 이미지를 표시하기 위해 Braze UI를 사용하려는 경우 `SDWebImage`의 통합이 필요합니다.

## 기본 이미지 재정의

Braze에서 클라이언트는 기존 기본 이미지를 고유한 커스텀 이미지로 교체할 수 있습니다. 이를 위해 커스텀 이미지를 사용하여 새 `png` 파일을 만들고 앱의 이미지 번들에 추가합니다. 그런 다음, 라이브러리의 기본 이미지를 덮어쓰도록 파일 이름을 이미지 이름으로 변경합니다. 또한 다양한 휴대폰 크기에 맞추기 위해 `@2x` 및 `@3x` 버전의 이미지를 업로드해야 합니다. 다음은 콘텐츠 카드에서 재정의할 수 있는 이미지입니다. 다음은 뉴스피드에서 재정의할 수 있는 이미지입니다.

* 아이콘 표시기 읽기: `Icons_Read`
* 입력 안내 이미지: `img-noimage-lrg`

{% alert important %}
현재 Xamarin iOS 통합에서 기본 이미지 재정의는 지원되지 않습니다.
{% endalert %}

