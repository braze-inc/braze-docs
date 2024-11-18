---
nav_title: 키-값 쌍
article_title: Android 및 FireOS용 뉴스 피드 키-값 쌍
page_order: 3
platform: 
  - Android
  - FireOS
description: "이 참조 문서에서는 Android 또는 FireOS 애플리케이션에서 뉴스피드 키-값 페어를 사용하는 방법을 다룹니다."
channel:
  - news feed

---

# 키-값 쌍

> 이 참조 문서에서는 Android 또는 FireOS 애플리케이션에서 뉴스피드 키-값 페어를 사용하는 방법을 다룹니다.

{% alert note %}
뉴스피드는 사용 중지될 예정입니다. Braze는 뉴스피드 도구를 사용하는 고객에게 보다 유연하고 맞춤 설정이 가능하며 안정적인 콘텐츠 카드 메시징 채널로 전환할 것을 권장합니다. 자세한 내용은 [마이그레이션 가이드를]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) 확인하세요.
{% endalert %}

`Card` 오브젝트는 선택적으로 키-값 페어를 `extras`와 같이 전달할 수 있습니다. 애플리케이션에서 추가 처리를 위해 `Card`로 데이터를 전송하는 데 사용할 수 있습니다.

`Card` 오브젝트에서 다음을 호출하여 추가 항목을 검색합니다.

{% tabs %}
{% tab JAVA %}

```java
Map<String, String> getExtras()
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
extras: Map<String, String>
```

{% endtab %}
{% endtabs %}
