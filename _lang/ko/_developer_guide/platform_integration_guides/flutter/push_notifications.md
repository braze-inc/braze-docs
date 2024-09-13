---
nav_title: 푸시 알림
article_title: Flutter용 푸시 알림
platform: Flutter
page_order: 2
description: "이 문서에서는 Flutter에서 푸시 알림을 구현하고 테스트하는 방법에 대해 설명합니다."
channel: push

---

# 푸시 알림 통합

> 이 참조 문서에서는 Flutter의 푸시 알림을 설정하는 방법에 대해 설명합니다. 푸시 알림을 통합하려면 각 기본 플랫폼을 개별적으로 설정해야 합니다. 나열된 각 가이드에 따라 설치를 완료합니다.

## 1단계: 초기 설정 완료

{% tabs %}
{% tab Android %}
### 1.1단계: 푸시 등록하기

Google의 Firebase 클라우드 메시징(FCM) API를 사용하여 푸시 등록을 하세요. 전체 안내는 [네이티브 Android 푸시 연동 가이드의]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/) 다음 단계를 참조하세요:

1. [프로젝트에 Firebase를 추가합니다]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-1-add-firebase-to-your-project).
2. [종속 항목에 클라우드 메시징을 추가하세요]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-2-add-cloud-messaging-to-your-dependencies).
3. [서비스 계정을 만듭니다]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-3-create-a-service-account).
4. [JSON 자격 증명을 생성합니다]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-4-generate-json-credentials).
5. [브레이즈에 JSON 자격 증명을 업로드합니다]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-5-upload-your-json-credentials-to-braze).

### 1.2단계: Google 발신자 ID 받기

먼저 Firebase 콘솔로 이동하여 프로젝트를 연 다음 <i class="fa-solid fa-gear"></i> **설정** > **프로젝트 설정을** 선택합니다.

!["설정" 메뉴가 열려 있는 Firebase 프로젝트]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

**클라우드 메시징을** 선택한 다음 **Firebase 클라우드 메시징 API(V1)**에서 **발신자 ID를** 클립보드에 복사합니다.

!['발신자 ID'가 강조 표시된 Firebase 프로젝트의 '클라우드 메시징' 페이지.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/copy-sender-id.png %})

### 1.3단계: 업데이트 `braze.xml`

`braze.xml` 파일에 다음을 추가합니다. `FIREBASE_SENDER_ID` 을 이전에 복사한 발신자 ID로 바꿉니다.

```xml
<bool translatable="false" name="com_braze_firebase_cloud_messaging_registration_enabled">true</bool>
<string translatable="false" name="com_braze_firebase_cloud_messaging_sender_id">FIREBASE_SENDER_ID</string>
```

{% endtab %}

{% tab iOS %}
### 1.1단계: APN 인증서 업로드

Apple 푸시 알림 서비스(APNs) 인증서를 생성하고 이를 Braze 대시보드에 업로드합니다. 전체 안내는 [APN 인증서 업로드를]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-1-upload-your-apns-certificate) 참조하세요.

### 1.2단계: 앱에 푸시 알림 지원 추가

[기본 iOS 통합 가이드를]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/?tab=objective-c#automatic-push-integration) 따르세요.

{% endtab %}
{% endtabs %}

## 2단계: 푸시 알림 이벤트 수신(선택 사항)

Braze가 감지하고 처리한 푸시 알림 이벤트를 수신하려면 `subscribeToPushNotificationEvents()` 으로 전화하여 실행할 인수를 전달하세요.

{% alert note %}
Braze 푸시 알림 이벤트는 Android와 iOS 모두에서 사용할 수 있습니다. 플랫폼의 차이로 인해 iOS에서는 사용자가 알림과 상호작용한 경우에만 Braze 푸시 이벤트가 감지됩니다.
{% endalert %}

```dart
// Create stream subscription
StreamSubscription pushEventsStreamSubscription;

pushEventsStreamSubscription = braze.subscribeToPushNotificationEvents((BrazePushEvent pushEvent) {
  print("Push Notification event of type ${pushEvent.payloadType} seen. Title ${pushEvent.title}\n and deeplink ${pushEvent.url}");
  // Handle push notification events
});

// Cancel stream subscription
pushEventsStreamSubscription.cancel();
```

#### 푸시 알림 이벤트 필드

{% alert note %}
iOS의 플랫폼 제한으로 인해 Braze SDK는 앱이 포그라운드에 있는 동안에만 푸시 페이로드를 처리할 수 있습니다. 리스너는 사용자가 푸시와 상호 작용한 후에만 iOS에서 `push_opened` 이벤트 유형에 대해 트리거됩니다.
{% endalert %}

푸시 알림 필드의 전체 목록은 아래 표를 참조하세요:

| 필드 이름         | 유형      | 설명 |
| ------------------ | --------- | ----------- |
| `payloadType`     | 문자열    | 알림 페이로드 유형을 지정합니다. Braze Flutter SDK에서 전송되는 두 개의 값은 `push_opened` 와 `push_received` 입니다.  iOS에서는 `push_opened` 이벤트만 지원됩니다. |
| `url`              | 문자열    | 알림에 의해 열린 URL을 지정합니다. |
| `useWebview`      | 부울   | `true`, URL은 모달 웹뷰에서 인앱으로 열립니다. `false`, 디바이스 브라우저에서 URL이 열립니다. |
| `title`            | 문자열    | 알림의 제목을 나타냅니다. |
| `body`             | 문자열    | 알림의 본문 또는 콘텐츠 텍스트를 나타냅니다. |
| `summaryText`     | 문자열    | 알림의 요약 텍스트를 표시합니다. 이는 iOS의 `subtitle` 에서 매핑됩니다. |
| `badgeCount`      | 숫자   | 알림의 배지 개수를 나타냅니다. |
| `timestamp`        | 숫자 | 애플리케이션이 페이로드를 수신한 시간을 나타냅니다. |
| `isSilent`        | 부울   | `true`, 페이로드가 자동으로 수신됩니다. Android 무음 푸시 알림을 보내는 방법에 대한 자세한 내용은 [Android에서 무음 푸시 알림을]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/silent_push_notifications) 참조하세요. iOS 무음 푸시 알림을 보내는 방법에 대한 자세한 내용은 [iOS에서 무음 푸시 알림을]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/) 참조하세요. |
| `isBrazeInternal`| 부울   | 지오펜스 동기화, 기능 플래그 동기화 또는 제거 추적과 같은 내부 SDK 기능에 대한 알림 페이로드가 전송된 경우 이 주소는 `true` 입니다. 페이로드는 사용자를 위해 자동으로 수신됩니다. |
| `imageUrl`        | 문자열    | 알림 이미지와 연결된 URL을 지정합니다. |
| `brazeProperties` | 객체    | 캠페인과 관련된 Braze 속성(키-값 쌍)을 나타냅니다. |
| `ios`              | 객체    | iOS 관련 필드를 나타냅니다. |
| `android`          | 객체    | Android 전용 필드를 나타냅니다. |
{: .reset-td-br-1 .reset-td-br-2}

## 3단계: 푸시 알림 표시 테스트

네이티브 레이어에서 푸시 알림을 구성한 후 통합을 테스트합니다:

1. Flutter 애플리케이션에서 활성 사용자를 설정합니다. 이렇게 하려면 `braze.changeUser('your-user-id')` 을 호출하여 플러그인을 초기화합니다.
2. **캠페인으로** 이동하여 새 푸시 알림 캠페인을 만듭니다. 테스트할 플랫폼을 선택합니다.
3. 테스트 알림을 작성하고 **테스트** 탭으로 이동합니다. 테스트 사용자와 동일한 `user-id` 을 추가하고 **테스트 보내기를** 클릭합니다.
4. 곧 장치에서 알림을 받게 될 것입니다. 알림 센터에서 확인하거나 표시되지 않는 경우 설정을 업데이트해야 할 수 있습니다.

{% alert tip %}
Xcode 14부터는 iOS 시뮬레이터에서 원격 푸시 알림을 테스트할 수 있습니다.
{% endalert %}
