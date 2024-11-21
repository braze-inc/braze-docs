---
nav_title: 인앱 메시지 전달
article_title: Android 및 FireOS용 인앱 메시지 전송
page_order: 3
platform: 
  - Android
  - FireOS
description: "이 참조 문서에서는 Android 및 FireOS 인앱 메시지 전달, 다양한 트리거 유형 표시, 전달 의미 체계 및 이벤트 트리거 단계를 다룹니다."
channel:
  - in-app messages

---

# 인앱 메시지 전달

> 이 참조 문서에서는 Android 및 FireOS 인앱 메시지 전달, 다양한 트리거 유형 표시, 전달 의미 체계 및 이벤트 트리거 단계를 다룹니다.

## 트리거 유형

인앱 메시지 제품을 사용하면 여러 가지 이벤트 유형(`Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event`, `Push Click`)으로 인앱 메시지 표시를 트리거할 수 있습니다. 게다가, `Specific Purchase` 및 `Custom Event` 트리거는 강력한 속성정보 필터를 포함할 수 있습니다.

{% alert note %}
트리거된 인앱 메시지는 Braze SDK를 통해 기록된 커스텀 이벤트에서만 작동합니다. 인앱 메시지는 API 또는 API 이벤트(예: 구매 이벤트)를 통해 트리거할 수 없습니다. [사용자 지정 이벤트를 기록하는]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/) 방법을 확인하세요.
{% endalert %}

## 전달 의미 체계

사용자가 받을 수 있는 모든 인앱 메시지는 [세션이 시작될]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/#session-lifecycle) 때 사용자의 디바이스로 전달됩니다. 제공되면 SDK가 트리거 시점에 즉시 사용할 수 있도록 자산을 미리 가져와 표시 지연 시간을 최소화합니다.

트리거 이벤트에 적격한 인앱 메시지가 두 개 이상 연결된 경우 우선순위가 가장 높은 인앱 메시지만 전달됩니다.

전달 즉시 표시되는 인앱 메시지(예: 세션 시작, 푸시 클릭)의 경우 자산을 미리 가져오지 않아 약간의 지연 시간이 발생할 수 있습니다.

## 트리거 간 최소 시간 간격

기본적으로, 원활한 사용자 경험을 지원하기 위해 인앱 메시지를 30초에 한 번으로 제한합니다.

이 값을 재정의하려면 다음을 통해 `braze.xml`에서 `com_braze_trigger_action_minimum_time_interval_seconds`를 설정합니다.

```xml
  <integer name="com_braze_trigger_action_minimum_time_interval_seconds">5</integer>
```

## 서버 측 이벤트 트리거링

기본적으로, 인앱 메시지는 SDK에 의해 기록된 커스텀 이벤트로 트리거됩니다. 서버에서 보낸 이벤트로 인앱 메시지를 트리거하려는 경우에도 이를 수행할 수 있습니다.

이 기능을 활성화하기 위해 무음 푸시가 기기로 전송되어 커스텀 푸시 콜백이 SDK 기반 이벤트를 기록할 수 있습니다. 이 SDK 이벤트는 이후 사용자 대상 인앱 메시지를 트리거합니다.

### 1단계: 무음 푸시 수신을 위한 푸시 콜백 만들기

커스텀 푸시 콜백을 등록하여 특정 무음 푸시 알림을 수신 대기합니다. 자세한 내용은 [표준 Android 푸시 통합을]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#android-push-listener-callback) 참조하세요.

인앱 메시지를 전달하기 위해 두 개의 이벤트가 기록됩니다. 하나는 서버에서, 다른 하나는 커스텀 푸시 콜백에서 기록됩니다. 동일한 이벤트가 중복되지 않도록 하려면 푸시 콜백 내에서 기록된 이벤트는 일번적인 명명 규칙을 따라야 하고(예: '인앱 메시지 트리거 이벤트'), 서버에서 보낸 이벤트와 같은 이름이 아니어야 합니다. 이를 준수하지 않으면 단일 사용자 작업에 대해 기록된 중복 이벤트가 세분화 및 사용자 데이터에 영향을 미칠 수 있습니다.

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).subscribeToPushNotificationEvents(event -> {
  final Bundle kvps = event.getNotificationPayload().getBrazeExtras();
  if (kvps.containsKey("IS_SERVER_EVENT")) {
    BrazeProperties eventProperties = new BrazeProperties();

    // The campaign name is a string extra that clients can include in the push
    String campaignName = kvps.getString("CAMPAIGN_NAME");
    eventProperties.addProperty("campaign_name", campaignName);
    Braze.getInstance(context).logCustomEvent("IAM Trigger", eventProperties);
  }
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(applicationContext).subscribeToPushNotificationEvents { event ->
    val kvps = event.notificationPayload.brazeExtras
    if (kvps.containsKey("IS_SERVER_EVENT")) {
        val eventProperties = BrazeProperties()

        // The campaign name is a string extra that clients can include in the push
        val campaignName = kvps.getString("CAMPAIGN_NAME")
        eventProperties.addProperty("campaign_name", campaignName)
        Braze.getInstance(applicationContext).logCustomEvent("IAM Trigger", eventProperties)
    }
}
```

{% endtab %}
{% endtabs %}

### 2단계: 푸시 캠페인 만들기

서버 전송 이벤트를 통해 트리거되는 [무음 푸시 캠페인을]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/silent_push_notifications/) 만듭니다.

![]({% image_buster /assets/img_archive/serverSentPush.png %})

푸시 캠페인에는 이 푸시 캠페인이 SDK 커스텀 이벤트를 기록하기 위해 전송되었음을 나타내는 키-값 페어 추가 항목이 포함되어야 합니다. 이 이벤트는 인앱 메시지를 트리거하는 데 사용됩니다.

![두 세트의 키-값 페어: IS_SERVER_EVENT를 "true"로 설정하고 CAMPAIGN_NAME을 "예시 캠페인 이름"으로 설정합니다.]({% image_buster /assets/img_archive/kvpConfiguration.png %}){: style="max-width:70%;" }

앞의 푸시 콜백 샘플 코드는 키-값 페어를 인식하고 적절한 SDK 커스텀 이벤트를 기록합니다.

'인앱 메시지 트리거' 이벤트에 첨부할 이벤트 속성정보를 포함하려면 푸시 페이로드의 키-값 페어에서 이벤트 속성정보를 전달하면 됩니다. 이 예시에서는 후속 인앱 메시지의 캠페인 이름이 포함되었습니다. 그러면 커스텀 푸시 콜백은 커스텀 이벤트를 기록할 때 이벤트 속성정보의 매개변수로 값을 전달할 수 있습니다.

### 3단계: 인앱 메시지 캠페인 만들기

Braze 대시보드에서 사용자가 볼 수 있는 인앱 메시지 캠페인을 생성하세요. 이 캠페인에는 액션 기반 전달이 있어야 하며 사용자 지정 푸시 콜백 내에서 로깅된 사용자 지정 이벤트에서 트리거되어야 합니다.

다음 예제에서는 초기 무음 푸시의 일부로 이벤트 속성정보를 전송하여 트리거할 특정 인앱 메시지를 구성합니다.

!["캠페인_이름"이 "IAM 캠페인 이름 예시"와 같을 때 인앱 메시지가 트리거되는 액션 기반 전달 캠페인입니다.]({% image_buster /assets/img_archive/iam_event_trigger.png %})

앱이 포그라운드에 있지 않은 상태에서 서버에서 전송된 이벤트가 기록되면 이벤트는 기록되지만 인앱 메시지는 표시되지 않습니다. 애플리케이션이 포그라운드에 표시될 때까지 이벤트를 지연시키려면 앱이 포그라운드에 표시될 때까지 이벤트를 해제하거나 지연시키도록 커스텀 푸시 수신기에 확인을 포함해야 합니다.

## 로컬 인앱 메시지

앱 내에서 인앱 메시지를 생성하여 실시간으로 로컬에 표시할 수 있습니다. 대시보드에서 사용할 수 있는 모든 사용자 지정 옵션은 로컬에서도 사용할 수 있습니다. 이 기능은 앱 내에서 트리거하려는 메시지를 실시간으로 표시할 때 특히 유용합니다.

{% tabs %}
{% tab JAVA %}

```java
// Initializes a new slideup type in-app message and specifies its message.
InAppMessageSlideup inAppMessage = new InAppMessageSlideup();
inAppMessage.setMessage("Welcome to Braze! This is a slideup in-app message.");
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
// Initializes a new slideup type in-app message and specifies its message.
val inAppMessage = InAppMessageSlideup()
inAppMessage.message = "Welcome to Braze! This is a slideup in-app message."
```

{% endtab %}
{% endtabs %}

{% alert important %}
이 상황에서는 렌더링이 정의되지 않으므로 소프트 키보드가 화면에 표시될 때 인앱 메시지를 표시하지 않습니다.
{% endalert %}

### 인앱 메시지 표시 수동 트리거하기

다음 방법은 인앱 메시지를 수동으로 표시하는 방법입니다:

{% tabs %}
{% tab JAVA %}

```java
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage)
```

{% endtab %}
{% endtabs %}

