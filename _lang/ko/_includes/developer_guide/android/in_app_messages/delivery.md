{% multi_lang_include developer_guide/prerequisites/android.md %}

## 메시지 트리거된 메시지

### 트리거 유형

인앱 메시지는 소프트웨어 개발 키트에서 다음 커스텀 이벤트 유형 중 하나를 기록하면 자동으로 트리거됩니다: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event`, `Push Click`. `Specific Purchase` 및 `Custom Event` 트리거에는 강력한 속성 필터도 포함되어 있습니다.

{% alert note %}
인앱 메시지는 API 또는 API 이벤트를 통해 트리거할 수 없으며, SDK에서 로깅한 사용자 지정 이벤트만 트리거할 수 있습니다. 로깅에 대해 자세히 알아보려면 [사용자 지정 이벤트 로깅을]({{site.baseurl}}/developer_guide/analytics/logging_events/) 참조하세요.
{% endalert %}

### 전달 의미 체계

모든 적격 인앱 메시지는 세션이 시작될 때 사용자의 기기에 전달됩니다. 소프트웨어 개발 키트가 제공되면 자산을 미리 가져와 트리거 시점에 사용할 수 있으므로 디스플레이 대기 시간을 최소화할 수 있습니다. 트리거 이벤트에 적격 인앱 메시지가 두 개 이상 있는 경우 우선순위가 가장 높은 메시지만 전달됩니다.

소프트웨어 개발 키트의 세션 시작 시맨틱에 대한 자세한 내용은 세션[수명주기를]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=android) 참조하세요.

### 사용량 제한

기본적으로, 원활한 사용자 경험을 지원하기 위해 인앱 메시지를 30초에 한 번으로 제한합니다.

이 값을 재정의하려면 다음을 통해 `braze.xml`에서 `com_braze_trigger_action_minimum_time_interval_seconds`를 설정합니다.

```xml
  <integer name="com_braze_trigger_action_minimum_time_interval_seconds">5</integer>
```

## 키-값 쌍

Braze에서 캠페인을 생성할 때 키-값 쌍을 `extras` 으로 설정하면 인앱 메시징 개체가 앱에 데이터를 전송하는 데 사용할 수 있습니다. For example:

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

{% alert note %}
자세한 내용은 [KDoc을](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html#1498425856%2FProperties%2F-1725759721) 참조하세요.
{% endalert %}

## 자동 트리거 비활성화하기

인앱 메시지가 자동으로 트리거되는 것을 방지합니다:

1. 버전 `2.2.0`부터 기본적으로 활성화되는 자동 통합 초기화 프로그램을 사용하고 있는지 확인합니다.
2. `braze.xml` 파일에 다음 줄을 추가하여 인앱 메시지 작업의 기본값을 `DISCARD`로 설정합니다.

```xml
<string name="com_braze_flutter_automatic_integration_iam_operation">DISCARD</string>
```

## 수동으로 메시지 트리거하기

기본적으로 인앱 메시지는 SDK가 사용자 지정 이벤트를 기록할 때 자동으로 트리거됩니다. 그러나 다음 방법을 사용하여 수동으로 메시지를 트리거할 수 있습니다.

### 서버 측 이벤트 사용

서버에서 전송한 이벤트를 사용하여 인앱 메시지를 트리거하려면 디바이스에 무음 푸시 알림을 보내면 사용자 지정 푸시 콜백이 SDK 기반 이벤트를 기록할 수 있습니다. 그러면 이 이벤트가 사용자에게 표시되는 인앱 메시지를 트리거합니다.

#### 1단계: 무음 푸시 수신을 위한 푸시 콜백 만들기

[커스텀 푸시 콜백을]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android#push-callback) 등록하여 특정 무음 푸시 알림을 수신할 수 있습니다.

다음 예시에서는 인앱 메시지 전달을 위해 서버에서 발생하는 이벤트와 커스텀 푸시 콜백 내에서 발생하는 이벤트 두 개가 기록됩니다. 동일한 이벤트가 중복되지 않도록 하려면 푸시 콜백 내에서 기록된 이벤트는 일번적인 명명 규칙을 따라야 하고(예: '인앱 메시지 트리거 이벤트'), 서버에서 보낸 이벤트와 같은 이름이 아니어야 합니다. 이를 준수하지 않으면 단일 사용자 작업에 대해 기록된 중복 이벤트가 세분화 및 사용자 데이터에 영향을 미칠 수 있습니다.

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

#### 2단계: 푸시 캠페인 만들기

서버 전송 이벤트를 통해 트리거되는 [무음 푸시 캠페인을]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android) 만듭니다.

![]({% image_buster /assets/img_archive/serverSentPush.png %})

푸시 캠페인에는 이 푸시 캠페인이 SDK 커스텀 이벤트를 기록하기 위해 전송되었음을 나타내는 키-값 페어 추가 항목이 포함되어야 합니다. 이 이벤트는 인앱 메시지를 트리거하는 데 사용됩니다.

![두 가지 키-값 페어: IS_SERVER_EVENT 을 "true"로 설정하고 CAMPAIGN_NAME 을 "예시 캠페인 이름"으로 설정합니다.]({% image_buster /assets/img_archive/kvpConfiguration.png %}){: style="max-width:70%;" }

앞의 푸시 콜백 샘플 코드는 키-값 페어를 인식하고 적절한 SDK 커스텀 이벤트를 기록합니다.

'인앱 메시지 트리거' 이벤트에 첨부할 이벤트 속성정보를 포함하려면 푸시 페이로드의 키-값 페어에서 이벤트 속성정보를 전달하면 됩니다. 이 예시에서는 후속 인앱 메시지의 캠페인 이름이 포함되었습니다. 그러면 커스텀 푸시 콜백은 커스텀 이벤트를 기록할 때 이벤트 속성정보의 매개변수로 값을 전달할 수 있습니다.

#### 3단계: 인앱 메시지 캠페인 만들기

Braze 대시보드에서 사용자가 볼 수 있는 인앱 메시지 캠페인을 생성하세요. 이 캠페인에는 액션 기반 전달이 있어야 하며 사용자 지정 푸시 콜백 내에서 로깅된 사용자 지정 이벤트에서 트리거되어야 합니다.

다음 예제에서는 초기 무음 푸시의 일부로 이벤트 속성정보를 전송하여 트리거할 특정 인앱 메시지를 구성합니다.

!["campaign_name" 이 "IAM 캠페인 이름 예시"와 같을 때 인앱 메시지가 트리거되는 실행 기반 전달 캠페인입니다.]({% image_buster /assets/img_archive/iam_event_trigger.png %})

앱이 포그라운드에 있지 않은 상태에서 서버에서 전송된 이벤트가 기록되면 이벤트는 기록되지만 인앱 메시지는 표시되지 않습니다. 애플리케이션이 포그라운드에 표시될 때까지 이벤트를 지연시키려면 앱이 포그라운드에 표시될 때까지 이벤트를 해제하거나 지연시키도록 커스텀 푸시 수신기에 확인을 포함해야 합니다.

### 미리 정의된 메시지 표시

미리 정의된 인앱 메시지를 수동으로 표시하려면 다음 방법을 사용하세요:

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

### 실시간 메시지 표시 

대시보드에서 사용할 수 있는 동일한 사용자 지정 옵션을 사용하여 로컬 인앱 메시지를 실시간으로 생성하고 표시할 수도 있습니다. 그렇게 하려면

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
