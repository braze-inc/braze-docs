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

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

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
