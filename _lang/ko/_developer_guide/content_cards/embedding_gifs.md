---
nav_title: GIF 삽입하기
article_title: 콘텐츠 카드에 GIF 삽입하기
page_order: 5
description: "Braze SDK를 사용하여 콘텐츠 카드에 GIF를 삽입하는 방법을 알아보세요."
channel:
  - content cards
platform:
  - Android
  - Swift
  - Web
  - FireOS
---

# 콘텐츠 카드에 GIF 삽입하기

> Braze SDK를 사용하여 콘텐츠 카드에 GIF를 삽입하는 방법을 알아보세요.

{% alert note %}
목록에 없는 래퍼 SDK의 경우 관련 네이티브 Android 또는 Swift 메서드를 대신 사용하세요. Android 및 Swift Braze SDK는 기본적으로 애니메이션 GIF를 지원하지 않으므로 대신 타사 도구를 사용하여 콘텐츠 카드 GIF를 구현해야 합니다.
{% endalert %}

{% sdktabs %}
{% sdktab android %}
{% multi_lang_include developer_guide/android/_global/gifs.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/gifs.md %}
{% endsdktab %}

{% sdktab web %}
현재 웹브레이즈 SDK에서는 콘텐츠 카드 GIF가 지원되지 않습니다.
{% endsdktab %}
{% endsdktabs %}
