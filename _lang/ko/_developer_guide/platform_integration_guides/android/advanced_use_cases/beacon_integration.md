---
nav_title: 비콘 통합
article_title: Android 및 FireOS용 비콘 통합
platform: 
  - Android
  - FireOS
page_order: 2
description: "이 참조 문서에서는 Android 또는 FireOS용 Gimbal 비콘을 사용하여 커스텀 이벤트를 기록하는 방법을 다룹니다."

---

# 비콘 통합

> 이 문서에서는 특정 종류의 비콘을 Braze와 통합하여 세분화 및 메시징을 허용하는 방법을 안내합니다.

## Gimbal 비콘

Gimbal 비콘이 설정되어 있고 앱에 통합되어 있으면 방문 시작 또는 방문 종료, 비콘 확인과 같은 커스텀 이벤트를 기록할 수 있습니다. 장소 이름이나 체류 시간과 같은 이벤트의 속성을 기록할 수도 있습니다.

사용자가 장소에 입장할 때 사용자 지정 이벤트를 기록하려면 `onVisitStart` 메서드에 이 코드를 포함하세요:

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).logCustomEvent("Entered " + visit.getPlace());
Braze.getInstance(context).requestImmediateDataFlush();
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).logCustomEvent("Entered " + visit.getPlace())
Braze.getInstance(context).requestImmediateDataFlush()
```

{% endtab %}
{% endtabs %}

`requestImmediateDataFlush`를 사용하면 앱이 백그라운드 상태에 있더라도 이벤트가 기록되며, 장소를 떠나는 경우에 대해서도 동일한 프로세스를 구현할 수 있습니다. 사용 중인 활동 및 컨텍스트에 따라 `logCustomEvent` 및 `requestImmediateDataFlush` 라인의 정확한 통합 방법이 달라질 수 있습니다. 또한 이 코드에서는 사용자가 들어서는 각각의 새 장소에 대해 고유한 커스텀 이벤트가 생성되고 증가됩니다. 따라서 50개가 넘는 장소를 생성할 것으로 예상한다면, 한 개의 일반 '방문 장소' 사용자 지정 이벤트를 생성하고 장소명을 이벤트 등록정보로 포함하는 것이 좋습니다.
