---
nav_title: 키-값 쌍
article_title: Android 및 FireOS용 인앱 메시지 키-값 쌍
platform: 
  - Android
  - FireOS
page_order: 6.9
description: "이 참조 문서에서는 Android 또는 FireOS 애플리케이션의 인앱 메시징 키-값 페어를 다룹니다."
channel:
  - in-app messages

---

# 키-값 쌍

> 이 참조 문서에서는 Android 또는 FireOS 애플리케이션의 인앱 메시징 키-값 페어를 다룹니다.

인앱 메시지 오브젝트는 키-값 페어를 `extras`로 전달할 수 있습니다. 인앱 메시지 캠페인을 생성할 때 대시보드의 **설정**에서 지정됩니다. 애플리케이션에서 추가 처리를 위해 인앱 메시지와 함께 데이터를 전송하는 데 사용할 수 있습니다.

인앱 메시지 오브젝트를 가져올 때 다음을 호출하여 추가 항목을 검색합니다.

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

자세한 내용은 이 [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html#1498425856%2FProperties%2F-1725759721)를 참조하세요.

