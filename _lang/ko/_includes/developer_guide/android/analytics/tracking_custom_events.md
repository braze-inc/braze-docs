# 사용자 지정 이벤트 추적

> Braze에서 커스텀 이벤트를 기록하여 앱의 사용 패턴에 대해 자세히 알아보고 대시보드에서 사용자의 작업에 따라 사용자를 세분화할 수 있습니다. 이 참조 문서에서는 Android 또는 FireOS 애플리케이션에 커스텀 이벤트를 추가하고 추적하는 방법을 다룹니다.

구현하기 전에 [이벤트 명명 규칙]({{site.baseurl}}/user_guide/data/custom_data/event_naming_conventions/)의 참고 사항과 함께 [분석 개요]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection)에서 커스텀 이벤트, 커스텀 속성 및 구매 이벤트가 제공하는 세분화 옵션 예제를 검토하세요.

## 커스텀 이벤트 추가

{% tabs %}
{% tab 자바 %}

```java
Braze.getInstance(context).logCustomEvent(YOUR_EVENT_NAME);
```

{% endtab %}
{% tab 코틀린 %}

```kotlin
Braze.getInstance(context).logCustomEvent(YOUR_EVENT_NAME)
```

{% endtab %}
{% endtabs %}

자세한 내용은 [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-custom-event.html)을 참조하십시오.

### 속성정보 추가

커스텀 이벤트에 대한 메타데이터는 [Braze 속성 객체](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.outgoing/-braze-properties/index.html)를 커스텀 이벤트와 함께 전달하여 추가할 수 있습니다.

속성은 키-값 쌍으로 정의됩니다. 키는 `String` 오브젝트이고 값은 `String`, `int`, `float`, `boolean` 또는 [`Date`](http://developer.android.com/reference/java/util/Date.html) 오브젝트일 수 있습니다.

{% tabs %}
{% tab 자바 %}

```java
Braze.logCustomEvent("YOUR-EVENT-NAME",
    new BrazeProperties(new JSONObject()
        .put("you", "can")
        .put("pass", false)
        .put("orNumbers", 42)
        .put("orDates", new Date())
        .put("or", new JSONArray()
            .put("any")
            .put("array")
            .put("here"))
        .put("andEven", new JSONObject()
            .put("deeply", new JSONArray()
                .put("nested")
                .put("json"))
        )
));
```

{% endtab %}
{% tab 코틀린 %}

```kotlin
Braze.logCustomEvent("YOUR-EVENT-NAME",
    BrazeProperties(JSONObject()
        .put("you", "can")
        .put("pass", false)
        .put("orNumbers", 42)
        .put("orDates", Date())
        .put("or", JSONArray()
            .put("any")
            .put("array")
            .put("here"))
        .put("andEven", JSONObject()
            .put("deeply", JSONArray()
                .put("nested")
                .put("json"))
        )
))
```

{% endtab %}
{% endtabs %}

### 예약 키

다음 키는 예약되어 있으며 커스텀 이벤트 속성으로 사용할 수 없습니다:

- `time`
- `event_name`

자세한 내용은 [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-custom-event.html)을 참조하십시오.

