---
nav_title: 표준 통합
article_title: Android용 표준 푸시 알림 통합
platform: Android
page_order: 0
description: "이 문서에서는 Android 애플리케이션에서 푸시 알림을 통합하는 방법에 대해 설명합니다."
channel:
  - push
search_rank: 3
---

# 표준 Android 푸시 통합

> Android 앱에서 푸시 알림을 통합하는 방법을 알아보세요.

푸시 알림을 사용하면 앱이 종료된 상태에서도 시간에 민감한 관련 콘텐츠를 기기 화면으로 바로 전송하여 앱 사용자의 재참여를 유도할 수 있습니다. 앱에 푸시 통합을 완료했다면 [푸시 모범 사례를]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/) 확인하세요.

{% alert important %}
Android 푸시 연동이 이미 설정되어 있고 더 이상 사용되지 않는 Google의 클라우드 메시징 API에서 마이그레이션하려는 경우 [Firebase 클라우드 메시징 API로 마이그레이션하기를]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/migrating_to_firebase_cloud_messaging) 참조하세요.
{% endalert %}

## 사용량 제한

Firebase 클라우드 메시징(FCM) API의 기본 속도 제한은 분당 600,000건의 요청입니다. 이 제한에 도달하면 몇 분 후에 자동으로 다시 시도합니다. 증액을 요청하려면 [Firebase 지원팀에](https://firebase.google.com/support) 문의하세요.

## 푸시 등록하기

이 섹션에서는 Google의 FCM(파이어베이스 클라우드 메시징) API를 사용하여 푸시를 등록하는 방법에 대해 알아봅니다. Braze Android SDK에서 FCM을 사용하는 샘플 앱을 보려면 [Braze를 참조하세요: Firebase 푸시 샘플 앱](https://github.com/braze-inc/braze-android-sdk/tree/master/samples/firebase-push).

### 1단계: 프로젝트에 Firebase 추가

먼저, Android 프로젝트에 Firebase를 추가합니다. 단계별 지침은 Google의 \[Firebase 설정 가이드][49] 를 참조하세요.

### 2단계: 종속성에 클라우드 메시징 추가

다음으로 프로젝트 종속성에 클라우드 메시징 라이브러리를 추가합니다. Android 프로젝트에서 `build.gradle` 을 열고 `dependencies` 블록에 다음 줄을 추가합니다.

```gradle
implementation "google.firebase:firebase-messaging:+"
```

종속성은 다음과 비슷하게 보일 것입니다:

```gradle
dependencies {
  implementation project(':android-sdk-ui')
  implementation "com.google.firebase:firebase-messaging:+"
}
```

### 3단계: Firebase 클라우드 메시징 API 활성화

Google Cloud에서 Android 앱이 사용 중인 프로젝트를 선택한 다음 [Firebase 클라우드 메시징 API를](https://console.cloud.google.com/apis/library/fcm.googleapis.com) 활성화합니다.

![Firebase 클라우드 메시징 API 사용]({% image_buster /assets/img/android/push_integration/create_a_service_account/firebase-cloud-messaging-api-enabled.png %}){: style="max-width:80%;"}

### 4단계: 서비스 계정 만들기

다음으로 새 서비스 계정을 생성하여 Braze가 FCM 토큰을 등록할 때 승인된 API 호출을 할 수 있도록 합니다. Google Cloud에서 **서비스 계정으로** 이동한 다음 프로젝트를 선택합니다. **서비스 계정** 페이지에서 **서비스 계정 만들기를** 선택합니다.

!["서비스 계정 만들기"가 강조 표시된 프로젝트의 서비스 계정 홈 페이지.]({% image_buster /assets/img/android/push_integration/create_a_service_account/select-create-service-account.png %})

서비스 계정 이름, ID, 설명을 입력한 다음 **만들기를** 선택하고 **계속합니다**.

!['서비스 계정 세부 정보' 양식]({% image_buster /assets/img/android/push_integration/create_a_service_account/enter-service-account-details.png %})

**역할** 필드의 역할 목록에서 **Firebase Cloud 메시징 API 관리자를** 찾아 선택합니다. 보다 제한적인 액세스를 원하면 `cloudmessaging.messages.create` 권한으로 [사용자 지정 역할을](https://cloud.google.com/iam/docs/creating-custom-roles) 만든 다음 목록에서 해당 [역할을](https://cloud.google.com/iam/docs/creating-custom-roles) 선택하세요. 완료했으면 **완료를** 선택합니다.

{% alert warning %}
**Firebase 클라우드 메시징** **관리자가** 아닌 **Firebase 클라우드 메시징 _API_ 관리자를** 선택해야 합니다.
{% endalert %}

!["이 서비스 계정에 프로젝트 액세스 권한 부여"를 위한 양식에 "Firebase Cloud 메시징 API 관리자"를 역할로 선택합니다.]({% image_buster /assets/img/android/push_integration/create_a_service_account/add-fcm-api-admin.png %})

### 5단계: JSON 자격 증명 생성

다음으로 FCM 서비스 계정에 대한 JSON 자격 증명을 생성합니다. Google Cloud IAM 및 관리자에서 **서비스 계정으로** 이동한 다음 프로젝트를 선택합니다. [이전에 만든](#step-3-create-a-service-account) FCM 서비스 계정을 찾은 다음 <i class="fa-solid fa-ellipsis-vertical"></i> **작업** > **키 관리를** 선택합니다.

![프로젝트의 서비스 계정 홈페이지에서 '작업' 메뉴가 열려 있습니다.]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-manage-keys.png %})

**키 추가** > **새 키 만들기를** 선택합니다.

!["키 추가" 메뉴가 열려 있는 선택한 서비스 계정]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-create-new-key.png %})

**JSON을** 선택한 다음 **생성을** 선택합니다. FCM 프로젝트 ID와 다른 Google Cloud 프로젝트 ID를 사용하여 서비스 계정을 만든 경우, JSON 파일에서 `project_id` 에 할당된 값을 수동으로 업데이트해야 합니다.

다음 단계에서 키를 다운로드한 위치를 기억해 두세요.

!["JSON"을 선택한 상태에서 개인 키를 생성하는 양식입니다.]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-create.png %}){: style="max-width:65%;"}

{% alert warning %}
개인 키는 유출될 경우 보안 위험을 초래할 수 있습니다. 지금은 JSON 자격 증명을 안전한 위치에 보관하세요. Braze에 업로드한 후 키를 삭제할 수 있습니다.
{% endalert %}

### 6단계: Braze에 JSON 자격 증명 업로드하기

다음으로, Braze 대시보드에 JSON 자격 증명을 업로드합니다. Braze에서 <i class="fa-solid fa-gear"></i> **설정** > **앱 설정을** 선택합니다.

!["앱 설정"이 강조 표시된 상태로 Braze에서 "설정" 메뉴가 열립니다.]({% image_buster /assets/img/android/push_integration/upload_json_credentials/select-app-settings.png %})

Android 앱의 **푸시 알림 설정에서** **Firebase를** 선택한 다음 **JSON 파일 업로드를** 선택하고 [앞서 생성한](#step-4-generate-json-credentials) 자격 증명을 업로드합니다. 완료했으면 **저장을** 선택합니다.

![푸시 제공업체로 'Firebase'를 선택한 '푸시 알림 설정' 양식]({% image_buster /assets/img/android/push_integration/upload_json_credentials/upload-json-file.png %})

{% alert warning %}
개인 키는 유출될 경우 보안 위험을 초래할 수 있습니다. 이제 키가 Braze에 업로드되었으므로 [이전에 생성한](#step-4-generate-json-credentials) 파일을 삭제합니다.
{% endalert %}

### 7단계: 자동 토큰 등록 설정

사용자 중 한 명이 푸시 알림을 옵트인하면 앱에서 해당 사용자의 디바이스에서 FCM 토큰을 생성해야 푸시 알림을 보낼 수 있습니다. Braze SDK를 사용하면 프로젝트의 Braze 구성 파일에서 각 사용자의 디바이스에 대한 FCM 토큰을 자동으로 등록할 수 있습니다.

먼저 Firebase 콘솔로 이동하여 프로젝트를 연 다음 <i class="fa-solid fa-gear"></i> **설정** > **프로젝트 설정을** 선택합니다.

!["설정" 메뉴가 열려 있는 Firebase 프로젝트]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

**클라우드 메시징을** 선택한 다음 **Firebase 클라우드 메시징 API(V1)**에서 **발신자 ID** 필드에 번호를 복사합니다.

!['발신자 ID'가 강조 표시된 Firebase 프로젝트의 '클라우드 메시징' 페이지.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/copy-sender-id.png %})

그런 다음, 안드로이드 스튜디오 프로젝트를 열고 Firebase 발신자 ID를 사용하여 `braze.xml` 또는 `BrazeConfig` 에서 FCM 토큰 자동 등록을 활성화합니다.

{% tabs local %}
{% tab braze.xml %}
FCM 토큰 자동 등록을 구성하려면 `braze.xml` 파일에 다음 줄을 추가합니다:

```xml
<bool translatable="false" name="com_braze_firebase_cloud_messaging_registration_enabled">true</bool>
<string translatable="false" name="com_braze_firebase_cloud_messaging_sender_id">FIREBASE_SENDER_ID</string>
```

`FIREBASE_SENDER_ID` 을 Firebase 프로젝트 설정에서 복사한 값으로 바꿉니다. `braze.xml` 은 다음과 비슷하게 표시되어야 합니다:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">12345ABC-6789-DEFG-0123-HIJK456789LM</string>
  <bool translatable="false" name="com_braze_firebase_cloud_messaging_registration_enabled">true</bool>
<string translatable="false" name="com_braze_firebase_cloud_messaging_sender_id">603679405392</string>
</resources>
```
{% endtab %}
{% tab BrazeConfig %}
FCM 토큰 자동 등록을 구성하려면 `BrazeConfig` 에 다음 줄을 추가합니다:

{% subtabs global %}
{% subtab JAVA %}
```java
.setIsFirebaseCloudMessagingRegistrationEnabled(true)
.setFirebaseCloudMessagingSenderIdKey("FIREBASE_SENDER_ID")
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
.setIsFirebaseCloudMessagingRegistrationEnabled(true)
.setFirebaseCloudMessagingSenderIdKey("FIREBASE_SENDER_ID")
```
{% endsubtab %}
{% endsubtabs %}

`FIREBASE_SENDER_ID` 을 Firebase 프로젝트 설정에서 복사한 값으로 바꿉니다. `BrazeConfig` 은 다음과 비슷하게 표시되어야 합니다:

{% subtabs global %}
{% subtab JAVA %}
```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
  .setApiKey("12345ABC-6789-DEFG-0123-HIJK456789LM")
  .setCustomEndpoint("sdk.iad-01.braze.com")
  .setSessionTimeout(60)
  .setHandlePushDeepLinksAutomatically(true)
  .setGreatNetworkDataFlushInterval(10)
  .setIsFirebaseCloudMessagingRegistrationEnabled(true)
  .setFirebaseCloudMessagingSenderIdKey("603679405392")
  .build();
Braze.configure(this, brazeConfig);
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
val brazeConfig = BrazeConfig.Builder()
  .setApiKey("12345ABC-6789-DEFG-0123-HIJK456789LM")
  .setCustomEndpoint("sdk.iad-01.braze.com")
  .setSessionTimeout(60)
  .setHandlePushDeepLinksAutomatically(true)
  .setGreatNetworkDataFlushInterval(10)
  .setIsFirebaseCloudMessagingRegistrationEnabled(true)
  .setFirebaseCloudMessagingSenderIdKey("603679405392")
  .build()
Braze.configure(this, brazeConfig)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert tip %}
대신 FCM 토큰을 수동으로 등록하려면 앱 내에서 [`Braze.setRegisteredPushToken()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/registered-push-token.html) 앱의 [`onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) 메서드를 호출하면 됩니다.
{% endalert %}

### 8단계: 애플리케이션 클래스에서 자동 요청 제거

무음 푸시 알림을 보낼 때마다 Braze가 불필요한 네트워크 요청을 트리거하지 않도록 하려면 `Application` 클래스의 `onCreate()` 메서드에 구성된 모든 자동 네트워크 요청을 제거하세요. 자세한 내용은 [Android 개발자 참조를 참조하세요: 신청](https://developer.android.com/reference/android/app/Application).

## 푸시 수신 및 표시 {#displaying-push}

이 섹션을 완료하면 Braze에서 보낸 푸시 알림을 수신하고 표시할 수 있어야 합니다.

### 1단계: Braze 파이어베이스 메시징 서비스 등록

{% alert warning %}
이미 Firebase 메시징 서비스를 등록한 경우에는 이 단계를 완료하지 마세요. 대신 [자체 Firebase 메시징 서비스 사용으로](#using-your-own-firebase-messaging-service) 이동하여 여기에 나열된 단계를 완료하세요.
{% endalert %}

Braze에는 푸시 수신 및 공개 의도를 처리하는 서비스가 포함되어 있습니다. `BrazeFirebaseMessagingService` 클래스는 `AndroidManifest.xml` 에 등록해야 합니다:

```xml
<service android:name="com.braze.push.BrazeFirebaseMessagingService"
  android:exported="false">
  <intent-filter>
    <action android:name="com.google.firebase.MESSAGING_EVENT" />
  </intent-filter>
</service>
```

또한 알림 코드는 `BrazeFirebaseMessagingService` 를 사용하여 열기 및 클릭 동작 추적을 처리합니다. 이 서비스가 제대로 작동하려면 `AndroidManifest.xml` 에 등록해야 합니다. 또한 Braze는 시스템에서 보낸 알림만 렌더링하도록 시스템에서 보낸 알림에 고유 키를 접두사로 붙인다는 점을 기억하세요. 추가 서비스를 별도로 등록하여 다른 FCM 서비스에서 전송되는 알림을 표시할 수 있습니다. Firebase 푸시 샘플 앱에서 \[`AndroidManifest.xml`][70] ]를 참조하세요.

{% alert important %}
Braze SDK 3.1.1 이전에는 `AppboyFcmReceiver` 을 사용하여 FCM 푸시를 처리했습니다. `AppboyFcmReceiver` 클래스는 매니페스트에서 제거하고 이전 통합으로 대체해야 합니다.
{% endalert %}

#### 대체 파이어베이스 메시징 서비스 사용

또한 사용하려는 다른 Firebase 메시징 서비스가 있는 경우, 애플리케이션이 Braze가 아닌 다른 푸시를 수신할 경우 호출할 폴백 Firebase 메시징 서비스를 지정할 수도 있습니다.

`braze.xml` 에 지정합니다:

```xml
<bool name="com_braze_fallback_firebase_cloud_messaging_service_enabled">true</bool>
<string name="com_braze_fallback_firebase_cloud_messaging_service_classpath">com.company.OurFirebaseMessagingService</string>
```

또는 \[런타임 구성]을 통해 설정합니다:][65]

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
        .setFallbackFirebaseMessagingServiceEnabled(true)
        .setFallbackFirebaseMessagingServiceClasspath("com.company.OurFirebaseMessagingService")
        .build();
Braze.configure(this, brazeConfig);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
        .setFallbackFirebaseMessagingServiceEnabled(true)
        .setFallbackFirebaseMessagingServiceClasspath("com.company.OurFirebaseMessagingService")
        .build()
Braze.configure(this, brazeConfig)
```

{% endtab %}
{% endtabs %}

#### 자체 Firebase 메시징 서비스 사용

이미 Firebase 메시징 서비스를 등록한 경우, \[`RemoteMessage`][75] 객체를 \[`BrazeFirebaseMessagingService.handleBrazeRemoteMessage()`][74] 을 통해 Braze에 전달할 수 있습니다. 이 메서드는 \[`RemoteMessage`][75] ] 오브젝트가 Braze에서 발생한 경우에만 알림을 표시하고 그렇지 않은 경우 안전하게 무시합니다.

{% tabs %}
{% tab JAVA %}

```java
public class MyFirebaseMessagingService extends FirebaseMessagingService {
  @Override
  public void onMessageReceived(RemoteMessage remoteMessage) {
    super.onMessageReceived(remoteMessage);
    if (BrazeFirebaseMessagingService.handleBrazeRemoteMessage(this, remoteMessage)) {
      // This Remote Message originated from Braze and a push notification was displayed.
      // No further action is needed.
    } else {
      // This Remote Message did not originate from Braze.
      // No action was taken and you can safely pass this Remote Message to other handlers.
    }
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class MyFirebaseMessagingService : FirebaseMessagingService() {
  override fun onMessageReceived(remoteMessage: RemoteMessage?) {
    super.onMessageReceived(remoteMessage)
    if (BrazeFirebaseMessagingService.handleBrazeRemoteMessage(this, remoteMessage)) {
      // This Remote Message originated from Braze and a push notification was displayed.
      // No further action is needed.
    } else {
      // This Remote Message did not originate from Braze.
      // No action was taken and you can safely pass this Remote Message to other handlers.
    }
  }
}
```

{% endtab %}
{% endtabs %}

### 2단계: 작은 아이콘을 디자인 가이드라인에 따르기

Android 알림 아이콘에 대한 일반적인 정보는 \[알림 개요][37]]를 참조하세요.

Android N부터는 색상이 포함된 작은 알림 아이콘 에셋을 업데이트하거나 제거해야 합니다. Android 시스템(Braze SDK가 아님)은 액션 아이콘과 알림 작은 아이콘에서 알파 및 투명도가 아닌 모든 채널을 무시합니다. 즉, Android는 투명한 영역을 제외한 알림 작은 아이콘의 모든 부분을 흑백으로 변환합니다.

알림 작은 아이콘 에셋을 올바르게 만들려면 다음과 같이 하세요:
- 이미지에서 흰색을 제외한 모든 색상을 제거합니다.
- 자산의 흰색이 아닌 다른 모든 영역은 투명해야 합니다.

{% alert note %}
부적절한 자산의 일반적인 증상은 작은 알림 아이콘이 단색 사각형으로 렌더링되는 것입니다. 이는 Android 시스템에서 알림 작은 아이콘 에셋에서 투명한 영역을 찾을 수 없기 때문입니다.
{% endalert %}

다음 크고 작은 아이콘은 적절하게 디자인된 아이콘의 예시입니다:

!["바에 가는 중이지만..."이라는 메시지 옆의 큰 아이콘 하단 모서리에 작은 아이콘이 나타납니다.][38]

### 3단계: 알림 아이콘 구성

#### 에서 아이콘 지정 braze.xml

Braze를 사용하면 `braze.xml` 에서 그리기 가능한 리소스를 지정하여 알림 아이콘을 구성할 수 있습니다:

```xml
<drawable name="com_braze_push_small_notification_icon">REPLACE_WITH_YOUR_ICON</drawable>
<drawable name="com_braze_push_large_notification_icon">REPLACE_WITH_YOUR_ICON</drawable>
```

작은 알림 아이콘을 설정해야 합니다. **설정하지 않으면 Braze는 기본적으로 애플리케이션 아이콘을 작은 알림 아이콘으로 사용하게 되며, 이는 최선이 아닌 것처럼 보일 수 있습니다.**

큰 알림 아이콘을 설정하는 것은 선택 사항이지만 권장됩니다.

#### 아이콘 강조 색상 지정

알림 아이콘 강조 색상은 `braze.xml` 에서 재정의할 수 있습니다. 색상을 지정하지 않으면 기본 색상은 롤리팝이 시스템 알림에 사용하는 것과 동일한 회색이 됩니다.

```xml
<integer name="com_braze_default_notification_accent_color">0xFFf33e3e</integer>
```

선택적으로 색상 참조를 사용할 수도 있습니다:

```xml
<color name="com_braze_default_notification_accent_color">@color/my_color_here</color>
```

### 4단계: 딥링크 추가

#### 자동 딥링크 열기 활성화

푸시 알림을 클릭하면 Braze가 앱과 딥링크를 자동으로 열도록 설정하려면 `braze.xml` 에서 `com_braze_handle_push_deep_links_automatically` 를 `true` 로 설정하세요:

```xml
<bool name="com_braze_handle_push_deep_links_automatically">true</bool>
```

이 플래그는 \[런타임 구성][65]]을 통해서도 설정할 수 있습니다:

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
        .setHandlePushDeepLinksAutomatically(true)
        .build();
Braze.configure(this, brazeConfig);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
        .setHandlePushDeepLinksAutomatically(true)
        .build()
Braze.configure(this, brazeConfig)
```

{% endtab %}
{% endtabs %}

딥링크를 맞춤 처리하려면 Braze에서 푸시 수신 및 오픈 인텐트를 수신 대기하는 푸시 콜백을 만들어야 합니다. 자세한 내용은 \[푸시 영수증 사용자 지정 처리 및 열기][52] ] 문서를 참조하세요.

#### 사용자 지정 딥링크 만들기

아직 앱에 딥링크를 추가하지 않은 경우 \[안드로이드 개발자 문서][40] 딥링크에 대한 설명]에 있는 지침을 따르세요. 딥링크가 무엇인지 자세히 알아보려면 \[FAQ 문서][42] 를 참조하세요.

#### 딥링크 추가하기

Braze 대시보드는 푸시 알림 캠페인과 캔버스에서 알림을 클릭하면 열릴 딥링크 또는 웹 URL을 설정할 수 있습니다.

![][41]

#### 백 스택 동작 사용자 지정

기본적으로 Android SDK는 푸시 딥링크를 따라갈 때 호스트 앱의 메인 런처 활동을 백 스택에 배치합니다. Braze를 사용하면 기본 런처 활동 대신 백 스택에서 열리도록 사용자 지정 활동을 설정하거나 백 스택을 완전히 비활성화할 수 있습니다.

예를 들어 \[런타임 구성][65]]을 사용하여 `YourMainActivity` 이라는 활동을 백스택 활동으로 설정합니다:

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
        .setPushDeepLinkBackStackActivityEnabled(true)
        .setPushDeepLinkBackStackActivityClass(YourMainActivity.class)
        .build();
Braze.configure(this, brazeConfig);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
        .setPushDeepLinkBackStackActivityEnabled(true)
        .setPushDeepLinkBackStackActivityClass(YourMainActivity.class)
        .build()
Braze.configure(this, brazeConfig)
```

{% endtab %}
{% endtabs %}

`braze.xml` 에 해당하는 구성을 참조하세요. 클래스 이름은 `Class.forName()` 에서 반환한 것과 동일해야 합니다.

```xml
<bool name="com_braze_push_deep_link_back_stack_activity_enabled">true</bool>
<string name="com_braze_push_deep_link_back_stack_activity_class_name">your.package.name.YourMainActivity</string>
```

### 5단계: 알림 채널 정의

Braze 안드로이드 SDK는 \[안드로이드 알림 채널][62]]을 지원합니다. Braze 알림에 알림 채널의 ID가 포함되어 있지 않거나 Braze 알림에 잘못된 채널 ID가 포함되어 있는 경우, Braze는 SDK에 정의된 기본 알림 채널로 알림을 표시합니다. Braze 사용자는 플랫폼 내에서 \[Android 알림 채널][61] ]을 사용하여 알림을 그룹화할 수 있습니다.

기본 Braze 알림 채널의 사용자 대면 이름을 설정하려면 \[`BrazeConfig.setDefaultNotificationChannelName()`][72].

기본 Braze 알림 채널의 사용자 대면 설명을 설정하려면 \[`BrazeConfig.setDefaultNotificationChannelDescription()`][73].

`notification_channel` 필드를 포함하도록 [Android 푸시 개체][63] ] 파라미터를 사용하여 API 캠페인을 업데이트합니다. 이 필드가 지정되지 않은 경우, Braze는 \[대시보드 폴백][64] 채널 ID]로 알림 페이로드를 전송합니다.

기본 알림 채널 외에는 Braze에서 어떠한 채널도 생성하지 않습니다. 다른 모든 채널은 호스트 앱에서 프로그래밍 방식으로 정의한 다음 Braze 대시보드에 입력해야 합니다.

기본 채널 이름과 설명은 `braze.xml` 에서도 구성할 수 있습니다.

```xml
<string name="com_braze_default_notification_channel_name">Your channel name</string>
<string name="com_braze_default_notification_channel_description">Your channel description</string>
```

### 6단계: 테스트 알림 표시 및 분석

#### 디스플레이 테스트

이 시점에서 Braze에서 보낸 알림을 볼 수 있을 것입니다. 이를 테스트하려면 Braze 대시보드의 **캠페인** 페이지로 이동하여 **푸시 알림** 캠페인을 생성하세요. **Android 푸시를** 선택하고 메시지를 디자인합니다. 그런 다음 작성기에서 눈 아이콘을 클릭하여 테스트 발신자를 가져옵니다. 현재 사용자의 사용자 ID 또는 이메일 주소를 입력하고 **테스트 보내기를** 클릭합니다. 디바이스에 푸시가 표시되는 것을 확인할 수 있습니다.

![][55]

푸시 표시와 관련된 문제는 \[문제 해결 가이드][57] 를 참조하세요.

#### 분석 테스트

이 시점에서 푸시 알림 열기에 대한 분석 로깅도 있어야 합니다. 알림이 도착했을 때 클릭하면 캠페인 결과 페이지의 **직접 열기** 수가 1씩 증가합니다. [푸시]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_reporting/) 분석에 대한 자세한 내용은 푸시 [보고]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_reporting/) 문서를 참조하세요.

푸시 애널리틱스와 관련된 문제는 \[문제 해결 가이드][57] 를 참조하세요.

#### 명령줄에서 테스트

명령줄 인터페이스를 통해 인앱 및 푸시 알림을 테스트하려면 터미널을 통해 cURL과 \[메시징 API][22]]를 통해 단일 알림을 보낼 수 있습니다. 다음 필드를 테스트 케이스에 맞는 올바른 값으로 바꿔야 합니다:

- `YOUR_API_KEY` ( **설정** > **API 키로** 이동합니다.)
- `YOUR_EXTERNAL_USER_ID` ( **사용자 검색** 페이지에서 프로필을 검색합니다.)
- `YOUR_KEY1` (선택 사항)
- `YOUR_VALUE1` (선택 사항)

{% alert note %}
[이전 탐색을]({{site.baseurl}}/navigation) 사용하는 경우 이러한 페이지는 다른 위치에 있습니다: <br>- **API 키는** **개발자 콘솔** > **API 설정에서** 찾을 수 있습니다. <br>- **사용자** **검색은** **사용자** > **사용자 검색에** 있습니다.
{% endalert %}

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {YOUR_API_KEY}" -d '{
  "external_user_ids":["YOUR_EXTERNAL_USER_ID"],
  "messages": {
    "android_push": {
      "title":"Test push title",
      "alert":"Test push",
      "extra": {
        "YOUR_KEY1":"YOUR_VALUE1"
      }
    }  
  }
}' https://rest.iad-01.braze.com/messages/send
```

이 예에서는 `US-01` 인스턴스를 사용합니다. 이 인스턴스를 사용하지 않는 경우 `US-01` 엔드포인트를 [사용자 엔드포인트][66]]로 바꾸세요.

## 알림 표시 사용자 지정하기

### 1단계: 사용자 지정 알림 팩토리 만들기

일부 시나리오에서는 서버 측에서 번거롭거나 사용할 수 없는 방식으로 푸시 알림을 사용자 지정하고 싶을 수 있습니다. 알림 표시를 완벽하게 제어할 수 있도록, 사용자가 직접 정의할 수 있는 기능을 추가했습니다. [`IBrazeNotificationFactory`][6] 를 정의하여 Braze에서 표시할 알림 개체를 생성할 수 있는 기능을 추가했습니다.

사용자 지정 `IBrazeNotificationFactory` 을 설정한 경우, 사용자에게 알림이 표시되기 전에 푸시 수신 시 Braze가 공장의 `createNotification()` 메소드를 호출합니다. Braze는 대시보드 또는 메시징 API를 통해 전송된 사용자 지정 키-값 쌍이 포함된 `Bundle` 및 또 다른 `Bundle` 을 전달합니다:

Braze 푸시 알림의 데이터가 포함된 \[`BrazeNotificationPayload`][77] ]을 전달합니다.

{% tabs %}
{% tab JAVA %}

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
{% tab KOTLIN %}

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

사용자 지정 `createNotification()` 메서드에서 `null` 을 반환하여 알림을 전혀 표시하지 않거나, `BrazeNotificationFactory.getInstance().createNotification()` 을 사용하여 해당 데이터에 대한 기본 `notification` 개체를 가져와서 표시하기 전에 수정하거나, 완전히 별도의 `notification` 개체를 생성하여 표시할 수 있습니다.

{% alert note %}
Braze 푸시 데이터 키에 대한 설명서는 [Android SDK를](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-constants/index.html) 참조하세요.
{% endalert %}

### 2단계: 사용자 지정 알림 팩토리 설정

사용자 지정 알림 팩토리를 사용하도록 Braze에 지시하려면 `setCustomBrazeNotificationFactory` 메서드를 사용하여 [`IBrazeNotificationFactory`][6]:

{% tabs %}
{% tab JAVA %}


```java
setCustomBrazeNotificationFactory(IBrazeNotificationFactory brazeNotificationFactory);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
setCustomBrazeNotificationFactory(brazeNotificationFactory: IBrazeNotificationFactory)
```

{% endtab %}
{% endtabs %}

사용자 지정 `IBrazeNotificationFactory` 을 설정하는 권장 위치는 `Application.onCreate()` 애플리케이션 수명 주기 메서드(활동이 아닌)입니다. 이렇게 하면 앱 프로세스가 활성화될 때마다 알림 팩토리를 올바르게 설정할 수 있습니다.

{% alert important %}
나만의 알림을 처음부터 직접 만드는 것은 고급 사용 사례이며, 철저한 테스트와 Braze 푸시 기능에 대한 깊은 이해가 있어야만 수행할 수 있습니다. 예를 들어 알림 로그에 푸시가 올바르게 열리는지 확인해야 합니다.
{% endalert %}

사용자 지정 설정을 해제하고 [`IBrazeNotificationFactory`][6] 을 해제하고 푸시에 대한 기본 Braze 처리로 돌아가려면 사용자 지정 알림 팩토리 설정자에게 `null` 을 전달하세요:

{% tabs %}
{% tab JAVA %}


```java
setCustomBrazeNotificationFactory(null);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
setCustomBrazeNotificationFactory(null)
```

{% endtab %}
{% endtabs %}

## 푸시 프라이머

푸시 프라이머 캠페인은 사용자가 기기에서 앱에 대한 푸시 알림을 사용하도록 설정하도록 유도합니다. [노코드 푸시 프라이머를]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) 사용하면 SDK 커스터마이징 없이도 이 작업을 수행할 수 있습니다.

[6]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html
[8]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/
[16]: {% image_buster /assets/img_archive/fcm_api_insert.png %} "FCMKey"
[22]: {{site.baseurl}}/api/endpoints/messaging/
[28]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/fireos/integration/
[37]:https://developer.android.com/guide/topics/ui/notifiers/notifications
[38]: {% image_buster /assets/img_archive/large_and_small_notification_icon.png %} "크고 작은 알림 아이콘"
[40]: http://developer.android.com/training/app-indexing/deep-linking.html "Google 딥링킹 문서"
[41]: {% image_buster /assets/img_archive/deep_link_click_action.png %} "딥링크 클릭 액션"
[42]: {{site.baseurl}}/user_guide/개인화_및_동적_content/deep_linking_to_in-app_content/#what-is-deep-linking
[45]:https://firebase.google.com/docs/cloud-messaging/
[48]:https://developers.google.com/cloud-messaging/android/android-migrate-fcm
[49]:https://firebase.google.com/docs/android/setup
[52]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#android-push-listener-callback
[55]: {% image_buster /assets/img_archive/android_push_test.png %} "안드로이드 푸시 테스트"
[56]: {{site.baseurl}}/user_guide/메시지_건물_별channel/push/creating_a_push_message/#creating-a-push-message
[57]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/troubleshooting/
[58]:https://console.firebase.google.com/
[59]: {% image_buster /assets/img_archive/finding_firebase_server_key.png %} "파이어베이스서버키"
[61]: {{site.baseurl}}/user_guide/메시지_건물_별channel/push/android/notification_channels/
[62]:https://developer.android.com/preview/features/notification-channels.html
[63]: {{site.baseurl}}/api/objects_filters/messaging/android_object/
[64]: {{site.baseurl}}/user_guide/메시지_건물_별channel/push/android/notification_channels/#dashboard-fallback-channel
[65]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/
[66]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/
[67]:https://developer.android.com/reference/android/app/Application.html#onCreate()
[68]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/#runtime-configuration
[70]: https://github.com/braze-inc/braze-android-sdk/blob/master/samples/firebase-push/src/main/AndroidManifest.xml "AndroidManifest.xml"
[72]:https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-default-notification-channel-name.html
[73]:https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-default-notification-channel-description.html
[74]:https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.push/-braze-firebase-messaging-service/-companion/handle-braze-remote-message.html
[75]:https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage
[76]:https://developer.android.com/reference/android/app/Application
[77]:https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/index.html
[78]:https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-constants/index.html
[79]: {% image_buster /assets/img_archive/cloud_messaging_legacy_disabled.png %} "파이어베이스 레거시 사용 안 함"
[80]: {% image_buster /assets/img_archive/cloud_messaging_legacy_enabled.png %} "파이어베이스 서버 키"
