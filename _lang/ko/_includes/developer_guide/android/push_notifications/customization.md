{% multi_lang_include developer_guide/prerequisites/android.md %} [푸시 알림도 설정해야]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android) 합니다.

## 푸시 이벤트에 콜백 사용 {#push-callback}

Braze는 푸시 알림을 수신하거나 열람하거나 해제하는 경우에 대한 [`subscribeToPushNotificationEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/subscribe-to-push-notification-events.html) 콜백을 제공합니다. 애플리케이션이 실행되지 않는 동안 발생하는 이벤트를 놓치지 않도록 `Application.onCreate()`에 이 콜백을 배치하는 것이 좋습니다.

{% alert note %}
이전에 애플리케이션에서 이 기능을 위해 사용자 지정 생방송 수신기를 사용했다면 이 통합 옵션을 위해 해당 수신기를 안전하게 제거할 수 있습니다.
{% endalert %}

{% tabs %}
{% tab 자바 %}

```java
Braze.getInstance(context).subscribeToPushNotificationEvents(event -> {
  final BrazeNotificationPayload parsedData = event.getNotificationPayload();

  //
  // The type of notification itself
  //
  final boolean isPushOpenEvent = event.getEventType() == BrazePushEventType.NOTIFICATION_OPENED;
  final boolean isPushReceivedEvent = event.getEventType() == BrazePushEventType.NOTIFICATION_RECEIVED;
  // Sent when a user has dismissed a notification
  final boolean isPushDeletedEvent = event.getEventType() == BrazePushEventType.NOTIFICATION_DELETED;

  //
  // Notification data
  //
  final String pushTitle = parsedData.getTitleText();
  final Long pushArrivalTimeMs = parsedData.getNotificationReceivedTimestampMillis();
  final String deeplink = parsedData.getDeeplink();

  //
  // Custom KVP data
  //
  final String myCustomKvp1 = parsedData.getBrazeExtras().getString("my first kvp");
  final String myCustomKvp2 = parsedData.getBrazeExtras().getString("my second kvp");
});
```

{% endtab %}
{% tab 코틀린 %}

```kotlin
Braze.getInstance(context).subscribeToPushNotificationEvents { event ->
    val parsedData = event.notificationPayload

    //
    // The type of notification itself
    //
    val isPushOpenEvent = event.eventType == BrazePushEventType.NOTIFICATION_OPENED
    val isPushReceivedEvent = event.eventType == BrazePushEventType.NOTIFICATION_RECEIVED
    // Sent when a user has dismissed a notification
    val isPushDeletedEvent = event.eventType == BrazePushEventType.NOTIFICATION_DELETED

    //
    // Notification data
    //
    val pushTitle = parsedData.titleText
    val pushArrivalTimeMs = parsedData.notificationReceivedTimestampMillis
    val deeplink = parsedData.deeplink

    //
    // Custom KVP data
    //
    val myCustomKvp1 = parsedData.brazeExtras.getString("my first kvp")
    val myCustomKvp2 = parsedData.brazeExtras.getString("my second kvp")
}
```

{% endtab %}
{% endtabs %}

{% alert tip %}
알림 실행 버튼의 경우 `opens app` 또는 `deep link` 동작이 있는 버튼을 클릭하면 `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` 의도가 실행됩니다. 딥링크 및 추가 처리 기능은 동일하게 유지됩니다. `close` 동작이 있는 버튼은 `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` 의도를 실행하지 않으며 알림을 자동으로 해제합니다.
{% endalert %}

{% alert important %}
`Application.onCreate` 에서 푸시 알림 리스너를 생성하여 최종 사용자가 앱이 종료된 상태에서 알림을 탭하면 리스너가 트리거되도록 하세요.
{% endalert %}

## 알림 표시 커스텀하기 {#customization-display}

### 1단계: 사용자 지정 알림 팩토리 만들기

일부 시나리오에서는 서버 측에서 번거롭거나 사용할 수 없는 방식으로 푸시 알림을 사용자 지정하고 싶을 수 있습니다. 알림 표시를 완벽하게 제어할 수 있도록, 사용자가 [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html)를 정의하여 Braze에서 표시할 알림 개체를 생성하는 기능을 추가했습니다.

커스텀 `IBrazeNotificationFactory`를 설정한 경우, 사용자에게 알림이 표시되기 전에 푸시 수신 시 Braze가 팩토리의 `createNotification()` 메서드를 호출합니다. Braze는 Braze 푸시 데이터를 포함하는 `Bundle` 및 대시보드 또는 메시징 API를 통해 전송된 커스텀 키-값 페어를 포함하는 다른 `Bundle`을 전달합니다.

Braze 푸시 알림에 [`BrazeNotificationPayload`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/index.html) 에 Braze 푸시 알림의 데이터가 포함된 파일을 전달합니다.

{% tabs %}
{% tab 자바 %}

```java
// Factory method implemented in your custom IBrazeNotificationFactory
@Override
public Notification createNotification(BrazeNotificationPayload brazeNotificationPayload) {
  // Example of getting notification title
  String title = brazeNotificationPayload.getTitleText();

  // Example of retrieving a custom KVP ("my_key" -> "my_value")
  String customKvp = brazeNotificationPayload.getBrazeExtras().getString("my_key");
}
```

{% endtab %}
{% tab 코틀린 %}

```kotlin
// Factory method implemented in your custom IBrazeNotificationFactory
override fun createNotification(brazeNotificationPayload: BrazeNotificationPayload): Notification {
  // Example of getting notification title
  val title = brazeNotificationPayload.getTitleText()

  // Example of retrieving a custom KVP ("my_key" -> "my_value")
  val customKvp = brazeNotificationPayload.getBrazeExtras().getString("my_key")
}
```

{% endtab %}
{% endtabs %}

알림을 전혀 표시하지 않도록 커스텀 `createNotification()` 메서드에서 `null`을 반환하거나 해당 데이터에 대한 기본 `notification` 오브젝트를 가져와서 표시하기 전에 수정하도록 `BrazeNotificationFactory.getInstance().createNotification()`을 사용하거나 표시하도록 완전히 분리된 `notification` 오브젝트를 생성할 수 있습니다.

{% alert note %}
Braze 푸시 데이터 키에 대한 설명서는 [Android SDK](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-constants/index.html)를 참조하세요.
{% endalert %}

### 2단계: 커스텀 알림 팩토리 설정

커스텀 알림 팩토리를 사용하도록 Braze에 지시하려면 `setCustomBrazeNotificationFactory` 메서드를 사용하여 [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html)를 설정합니다.

{% tabs %}
{% tab 자바 %}


```java
setCustomBrazeNotificationFactory(IBrazeNotificationFactory brazeNotificationFactory);
```

{% endtab %}
{% tab 코틀린 %}

```kotlin
setCustomBrazeNotificationFactory(brazeNotificationFactory: IBrazeNotificationFactory)
```

{% endtab %}
{% endtabs %}

커스텀 `IBrazeNotificationFactory`를 설정하는 권장 위치는 `Application.onCreate()` 애플리케이션 수명 주기 메서드(활동이 아님)입니다. 그러면 앱 프로세스가 활성화될 때마다 알림 팩토리를 올바르게 설정할 수 있습니다.

{% alert important %}
알림을 처음부터 직접 만드는 것은 고급 사용 사례이며, 이때 철저한 테스트와 Braze 푸시 기능에 대한 깊은 이해 기반을 갖추어야 합니다. 예를 들어 알림이 푸시 열람 수를 올바르게 기록하는지 확인해야 합니다.
{% endalert %}

커스텀 [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html)를 해제하고 푸시에 대한 기본 Braze 처리로 돌아가려면 커스텀 알림 팩토리 설정자에게 `null`을 전달합니다.

{% tabs %}
{% tab 자바 %}


```java
setCustomBrazeNotificationFactory(null);
```

{% endtab %}
{% tab 코틀린 %}

```kotlin
setCustomBrazeNotificationFactory(null)
```

{% endtab %}
{% endtabs %}

## 멀티컬러 텍스트 렌더링

Braze 소프트웨어 개발 키트 3.1.1 버전에서는 푸시 알림에 여러 가지 색상의 텍스트를 렌더링하기 위해 기기에 HTML을 전송할 수 있습니다.

![글자가 서로 다른 색상으로 이탤릭체로 표시되고 배경색이 지정된 Android 푸시 메시지 '멀티컬러 푸시 테스트 메시지'입니다.]({% image_buster /assets/img/multicolor_android_push.png %}){: style="max-width:40%;"}

이 예제는 다음 HTML로 렌더링됩니다:

```html
<p><span style="color: #99cc00;">M</span>u<span style="color: #008080;">lti</span>Colo<span style="color: #ff6600;">r</span> <span style="color: #000080;">P</span><span style="color: #00ccff;">u</span><span style="color: #ff0000;">s</span><span style="color: #808080;">h</span></p>

<p><em>test</em> <span style="text-decoration: underline; background-color: #ff6600;"><strong>message</strong></span></p>
```

Android에서는 푸시 알림에 사용할 수 있는 HTML 요소와 태그가 제한되어 있다는 점에 유의하세요. 예를 들어, `marquee`는 허용되지 않습니다.

{% alert important %}
멀티컬러 텍스트 렌더링은 기기별로 다르며 Android 기기 또는 버전에 따라 표시되지 않을 수 있습니다.
{% endalert %}

푸시 알림에 멀티컬러 텍스트를 렌더링하려면 `braze.xml` 또는 `BrazeConfig` 을 업데이트하면 됩니다:

{% tabs local %}
{% tab braze.xml %}
다음 항목을 `braze.xml`에 추가하십시오:

```xml
<bool translatable="false" name="com_braze_push_notification_html_rendering_enabled">true</bool>
```
{% endtab %}

{% tab BrazeConfig %}
에 다음을 추가합니다. [`BrazeConfig`]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/#runtime-configuration):

{% subtabs local %}
{% subtab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
  .setPushHtmlRenderingEnabled(true)
  .build();
Braze.configure(this, brazeConfig);
```
 
{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
    .setPushHtmlRenderingEnabled(true)
    .build()
Braze.configure(this, brazeConfig)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### 지원되는 HTML 태그

현재 Google은 설명서에 Android에 대해 지원되는 HTML 태그를 직접 나열하지 않으며, 이 정보는 [Git 저장소의 `Html.java` 파일에서만](https://android.googlesource.com/platform/frameworks/base/+/master/core/java/android/text/Html.java) 찾을 수 있습니다. 이 정보는 이 파일에서 가져온 것이며 지원되는 HTML 태그는 변경될 수 있으므로 다음 표를 참조할 때 이 점을 염두에 두세요.

<table>
  <thead>
    <tr>
      <th>카테고리</th>
      <th>HTML 태그</th>
      <th>설명</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="7">기본 텍스트 스타일링</td>
      <td><code>&lt;b&gt;</code>, <code>&lt;strong&gt;</code></td>
      <td>굵은 텍스트</td>
    </tr>
    <tr>
      <td><code>&lt;i&gt;</code>, <code>&lt;em&gt;</code></td>
      <td>이탤릭체 텍스트</td>
    </tr>
    <tr>
      <td><code>&lt;u&gt;</code></td>
      <td>텍스트 밑줄</td>
    </tr>
    <tr>
      <td><code>&lt;s&gt;</code>, <code>&lt;strike&gt;</code>, <code>&lt;del&gt;</code></td>
      <td>취소선 텍스트</td>
    </tr>
    <tr>
      <td><code>&lt;sup&gt;</code></td>
      <td>위 첨자 텍스트</td>
    </tr>
    <tr>
      <td><code>&lt;sub&gt;</code></td>
      <td>구독 텍스트</td>
    </tr>
    <tr>
      <td><code>&lt;tt&gt;</code></td>
      <td>모노스페이스 텍스트</td>
    </tr>
    <tr>
      <td rowspan="3">크기/글꼴</td>
      <td><code>&lt;big&gt;</code>, <code>&lt;small&gt;</code></td>
      <td>상대적인 텍스트 크기 변경</td>
    </tr>
    <tr>
      <td><code>&lt;font color="..."&gt;</code></td>
      <td>전경색 설정</td>
    </tr>
    <tr>
      <td><code>&lt;span&gt;</code> (인라인 CSS 사용)</td>
      <td>인라인 스타일(e.g., 색상, 배경)</td>
    </tr>
    <tr>
      <td rowspan="4">단락 및 블록</td>
      <td><code>&lt;p&gt;</code>, <code>&lt;div&gt;</code></td>
      <td>블록 수준 섹션</td>
    </tr>
    <tr>
      <td><code>&lt;br&gt;</code></td>
      <td>줄 바꿈</td>
    </tr>
    <tr>
      <td><code>&lt;blockquote&gt;</code></td>
      <td>따옴표 블록</td>
    </tr>
    <tr>
      <td><code>&lt;ul&gt;</code> + <code>&lt;li&gt;</code></td>
      <td>글머리 기호가 있는 정렬되지 않은 목록</td>
    </tr>
    <tr>
      <td>제목</td>
      <td><code>&lt;h1&gt;</code> - <code>&lt;h6&gt;</code></td>
      <td>제목(다양한 크기)</td>
    </tr>
    <tr>
      <td rowspan="2">링크 및 이미지</td>
      <td><code>&lt;a href="..."&gt;</code></td>
      <td>클릭 가능한 링크</td>
    </tr>
    <tr>
      <td><code>&lt;img src="..."&gt;</code></td>
      <td>인라인 이미지</td>
    </tr>
    <tr>
      <td>기타 인라인</td>
      <td><code>&lt;em&gt;</code>, <code>&lt;strong&gt;</code>, <code>&lt;dfn&gt;</code>, <code>&lt;cite&gt;</code></td>
      <td>이탤릭체 또는 굵게의 동의어</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 인라인 이미지 렌더링

### 작동 방식

인라인 이미지 푸시를 사용하여 Android 푸시 알림에 더 큰 이미지를 표시할 수 있습니다. 이 디자인을 사용하면 사용자가 이미지를 확대하기 위해 수동으로 푸시를 확장할 필요가 없습니다. 일반 Android 푸시 알림과 달리 인라인 이미지 푸시 이미지는 3:2 화면 비율로 제공됩니다.

![]({% image_buster /assets/img/android/push/inline_image_push_android_1.png %}){: style="max-width:50%;"}

### 호환성

모든 기기에 인라인 이미지를 보낼 수 있지만, 최소 버전을 충족하지 않는 기기 및 SDK에는 표준 이미지가 대신 표시됩니다. 인라인 이미지가 제대로 표시되려면 Android 소프트웨어 개발 키트 v10.0.0+와 Android M+를 실행하는 기기가 모두 필요합니다. 이미지를 렌더링하려면 소프트웨어 개발 키트도 인에이블먼트해야 합니다.

{% alert note %}
Android 12를 실행하는 기기는 커스텀 푸시 알림 스타일의 변경으로 인해 다르게 렌더링됩니다.
{% endalert %}

### 인라인 이미지 푸시 보내기

Android 푸시 메시지를 작성할 때 **알림 유형** 드롭다운에서 이 기능을 사용할 수 있습니다.

![푸시 캠페인 에디터에서 '알림 유형' 드롭다운의 위치(표준 푸시 미리보기 위)를 표시합니다.]({% image_buster /assets/img/android/push/android_inline_image_notification_type.png %})

## Settings

Braze 대시보드를 통해 전송되는 Android 푸시 알림에는 다양한 고급 설정을 사용할 수 있습니다. 이 기사에서는 이러한 기능과 성공적으로 사용하는 방법에 대해 설명합니다.

![]({% image_buster /assets/img_archive/android_advanced_settings.png %})

### 알림 ID {#notification-id}

**알림 ID**는 선택한 메시지 카테고리에 대한 고유 식별자로, 메시징 서비스에 해당 ID의 가장 최근 메시지만 고려하도록 알립니다. 알림 ID를 설정하면 오래되고 관련성이 없는 메시지 더미 대신 가장 최근의 관련성 있는 메시지만 보낼 수 있습니다.

### Firebase 메시징 전송 우선순위 {#fcm-priority}

[Firebase 메시징 전송 우선순위](https://firebase.google.com/docs/cloud-messaging/concept-options#setting-the-priority-of-a-message) 필드를 통해 푸시 전송 우선순위를 '일반' 또는 '높음'으로 설정하여 Firebase 클라우드 메시징에 전송할지 여부를 제어할 수 있습니다.

### TTL {#ttl}

TTL( **Time to Live** ) 필드에서는 푸시 메시징 서비스에 메시지를 저장할 사용자 지정 기간을 설정할 수 있습니다. TTL의 기본값은 FCM의 경우 4주, ADM의 경우 31일입니다.

### 요약 텍스트 {#summary-text}

요약 텍스트를 사용하면 확장된 알림 보기에서 추가 텍스트를 설정할 수 있습니다. 알림에 이미지가 포함된 경우 캡션으로도 사용됩니다.

![An Android message with the title "This is the title for the notification." and summary text "This is the summary text for the notification."]({% image_buster /assets/img/android/push/collapsed-android-notification.png %}){: style="max-width:65%;"}

요약 텍스트는 확장된 보기에서 메시지 본문 아래에 표시됩니다. 

![An Android message with the title "This is the title for the notification." and summary text "This is the summary text for the notification."]({% image_buster /assets/img/android/push/expanded-android-notification.png %}){: style="max-width:65%;"}

푸시 알림에 이미지가 포함된 경우, 메시지 텍스트는 축소된 보기에서 표시되며, 요약 텍스트는 알림이 확장될 때 이미지 캡션으로 표시됩니다. 

### 사용자 지정 URI {#custom-uri}

**사용자 지정 URI** 기능을 사용하면 알림을 클릭할 때 이동할 웹 URL 또는 Android 리소스를 지정할 수 있습니다. 사용자 지정 URI가 지정되지 않은 경우 알림을 클릭하면 사용자가 앱으로 이동합니다. 커스텀 URI를 사용하여 앱 내부에 딥링킹하고 사용자를 앱 외부에 존재하는 리소스로 연결할 수 있습니다. 이는 그림과 같이 [메시징 API]({{site.baseurl}}/api/endpoints/messaging/) 또는 푸시 작성기의 **고급 설정** 아래의 대시보드를 통해 지정할 수 있습니다:

![브레이즈 푸시 작성기의 딥링킹 고급 설정]({% image_buster /assets/img_archive/deep_link.png %})

### 알림 표시 우선순위 {#notification-priority}

{% alert important %}
알림 표시 우선순위 설정은 Android O 이상을 실행하는 기기에서는 더 이상 사용되지 않습니다. 최신 장치의 경우 [알림 채널 구성](https://developer.android.com/training/notify-user/channels#importance)을 통해 우선 순위를 설정하십시오.
{% endalert %}

푸시 알림의 우선순위 수준은 다른 알림에 비해 알림 트레이에 표시되는 방식에 영향을 미칩니다. 또한 우선순위가 일반 이하인 메시지는 배터리 수명을 보존하기 위해 지연 시간이 약간 더 길어지거나 일괄 발송되는 반면, 우선순위가 높은 메시지는 항상 즉시 발송되므로 전송 속도와 방식에도 영향을 줄 수 있습니다.

Android O에서는 알림 우선 순위가 알림 채널의 속성이 되었습니다. 채널의 구성 중 우선순위를 정의하려면 개발자와 협력해야 하며, 알림 소리를 보낼 때 적절한 채널을 선택하려면 대시보드를 사용해야 합니다. Android O 이전 버전을 실행하는 기기의 경우, Braze 대시보드 및 메시징 API를 통해 Android 알림의 우선순위를 지정할 수 있습니다. 

전체 사용자 기반에 특정 우선순위를 지정하여 메시지를 보내려면 [알림 채널 구성을](https://developer.android.com/training/notify-user/channels#importance) 통해 간접적으로 우선순위를 *지정하고* (O+ 기기 타겟팅), 대시보드에서 개별 우선순위를 전송하는 것이 좋습니다(<O 기기 타겟팅).

Android 또는 Fire OS 푸시 알림에서 설정할 수 있는 우선 순위 수준은 다음과 같습니다:

| 우선순위 | 설명/용도 | `priority` 값(API 메시지의 경우) |
|----------|--------------------------|-------------------------------------|
| 최대      | 긴급하거나 시간이 촉박한 메시지 | `2` |
| 높음     | 친구의 새 메시지와 같은 중요한 커뮤니케이션 | `1` |
| 기본값  | 대부분의 알림 - 메시지가 다른 우선순위 유형에 명시적으로 속하지 않는 경우에 사용합니다. | `0` |
| 낮음      | 사용자가 알기를 원하지만 즉각적인 조치가 필요하지 않은 정보 | `-1` |
| 최소      | 상황별 또는 배경 정보. | `-2` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

자세한 내용은 Google의 [Android 알림](http://developer.android.com/design/patterns/notifications.html) 설명서를 참조하세요.

### 소리 {#sounds}

Android O에서는 알림 소리가 알림 채널의 속성이 되었습니다. 개발자와 협력하여 채널을 구성하는 동안 채널의 사운드를 정의한 다음 대시보드를 사용하여 알림을 보낼 때 적절한 채널을 선택해야 합니다.

Android O 이전 버전을 실행하는 디바이스의 경우, Braze를 사용하면 대시보드 작성기를 통해 개별 푸시 메시지의 사운드를 설정할 수 있습니다. 기기에서 로컬 사운드 리소스를 지정하면 됩니다(예: `android.resource://com.mycompany.myapp/raw/mysound`). 이 필드에서 '기본값'을 지정하면 기기에서 기본 알림 사운드가 재생됩니다. 이는 [메시징 API]({{site.baseurl}}/api/endpoints/messaging/) 또는 푸시 작성기의 **고급 설정** 아래의 대시보드를 통해 지정할 수 있습니다.

![Braze 푸시 작곡가의 사운드 고급 설정]({% image_buster /assets/img_archive/sound_android.png %})

대시보드 프롬프트에 전체 사운드 리소스 URI(예: `android.resource://com.mycompany.myapp/raw/mysound`)를 입력합니다.

전체 사용자 기반에 특정 사운드로 메시지를 보내려면 [알림 채널 구성을](https://developer.android.com/training/notify-user/channels) 통해 간접적으로 사운드를 지정(O+ 기기 타겟팅) *하고* 대시보드에서 개별 사운드를 전송(<O 기기 타겟팅)하는 것이 좋습니다.
