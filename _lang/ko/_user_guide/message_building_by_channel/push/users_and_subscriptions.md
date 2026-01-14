---
nav_title: "푸시 인에이블먼트 및 구독"
article_title: 푸시 인에이블먼트 및 구독
page_order: 3
page_type: reference
description: "이 참조 문서에서는 iOS, Android 및 웹에서 동작의 근본적인 차이점을 포함하여 Braze의 푸시 인에이블먼트 및 푸시 구독 상태의 개념에 대해 설명합니다."
channel:
  - push

---

# 푸시 인에이블먼트 및 푸시 구독

> 이 참조 문서에서는 iOS, Android 및 웹에서 동작의 근본적인 차이점을 포함하여 Braze의 푸시 인에이블먼트 및 푸시 구독 상태의 개념에 대해 설명합니다.

## 푸시 구독 상태 {#push-sub-states}

Braze의 '푸시 구독 상태'는 푸시 알림 수신을 원하는 **사용자의** 글로벌 선호도를 식별합니다. 구독 상태는 사용자 기반이므로 개별 앱에 한정되지 않습니다. 구독 상태는 푸시 알림을 타겟팅할 사용자를 결정할 때 유용한 플래그가 됩니다.

{% alert note %}
사용자의 푸시 구독 상태는 사용자의 모든 기기를 포함한 전체 고객 프로필에 적용됩니다.
{% endalert %}

푸시 구독 상태 옵션에는 세 가지가 있습니다: `Subscribed`, `Opted-In`, `Unsubscribed` 입니다.

기본적으로 사용자가 푸시를 통해 메시지를 받으려면 푸시 구독 상태가 `Subscribed` 또는 `Opted-In` 이며 [푸시 인에이블먼트가](#foreground-push-enabled) 설정되어 있어야 합니다. 메시지 작성 시 필요한 경우 이 설정을 재정의할 수 있습니다.

|옵트인 상태|설명|
|---|---|
|`Subscribed`| Braze에서 고객 프로필이 생성될 때의 기본값 푸시 구독 상태입니다. |
|`Opted-In`| 사용자가 푸시 알림 수신을 명시적으로 선호한다는 의사를 표시한 경우. 사용자가 OS 수준의 푸시 안내를 수락하면 Braze는 사용자의 옵트인 상태를 `Opted-In` 로 자동 이동합니다.<br><br>Android 12 이하 사용자에게는 적용되지 않습니다.|
|`Unsubscribed`| 사용자가 애플리케이션 또는 브랜드가 제공하는 기타 방법을 통해 푸시 수신을 명시적으로 탈퇴한 경우. 기본값으로 Braze 푸시 캠페인은 `Subscribed` 또는 `Opted-in` 인 사용자만 푸시 타겟팅합니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Braze는 사용자의 푸시 구독 상태를 `Unsubscribed` 로 자동 변경하지 않습니다. 사용자의 푸시 구독 상태가 `Unsubscribed` 인 경우 세분화에서 사용자의 `Foreground Push Enabled` 필터는 `false` 입니다.
{% endalert %}

### 푸시 구독 상태 업데이트하기 {#update-push-subscription-state}

사용자의 푸시 구독 상태를 업데이트하는 방법에는 세 가지가 있습니다:

#### 자동 옵트인(기본값)

사용자가 앱에 대한 푸시 알림을 처음 승인할 때 기본값으로 Braze는 사용자의 푸시 구독 상태를 `Opted-In` 로 설정합니다. 또한 사용자가 이전에 푸시 권한을 비활성화했다가 시스템 설정에서 푸시 권한을 다시 인에이블할 때에도 Braze는 이 작업을 수행합니다.

{% tabs local %}
{% tab android %}
이 기본값을 비활성화하려면 Android Studio 프로젝트의 `braze.xml` 파일에 다음 프로퍼티를 추가하세요:

```xml
<bool name="com_braze_optin_when_push_authorized">false</bool>
```
{% endtab %}

{% tab swift %}
[Braze Swift 소프트웨어 개발 키트 버전 7.5.0부터는](https://github.com/braze-inc/braze-swift-sdk/releases/tag/7.5.0) Xcode 프로젝트의 `AppDelegate.swift` 파일에 `optInWhenPushAuthorized` 구성을 추가하여 이 동작을 비활성화하거나 추가로 커스텀할 수 있습니다:

```swift
configuration.optInWhenPushAuthorized = false // disables the default behavior

let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endtab %}
{% endtabs %}

#### SDK 통합

[웹](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype), [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-push-notification-subscription-type.html) 또는 [iOS에서](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/set(pushnotificationsubscriptionstate:)) `setPushNotificationSubscriptionType` 방법을 사용하여 Braze 소프트웨어 개발 키트로 사용자의 구독 상태를 업데이트할 수 있습니다. 예를 들어 이 방법을 사용하여 앱에서 사용자가 푸시 알림을 수동으로 인에이블먼트하거나 비활성화할 수 있는 설정 페이지를 만들 수 있습니다.

#### REST API

[`/users/track` 엔드포인트를]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) 사용하여 사용자의 구독 상태를 업데이트하려면 Braze REST API를 사용하여 사용자의 구독 상태를 업데이트할 수 있습니다. [`push_subscribe`]({{site.baseurl}}/api/objects_filters/user_attributes_object) 속성을 업데이트할 수 있습니다.

### 푸시 구독 상태 확인하기

!!! 푸시 구독 상태가 가입한 것으로 설정된 신원 미상의 고객 프로필입니다.]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Braze에서 사용자의 푸시 구독 상태를 확인할 수 있는 방법은 두 가지가 있습니다:

1. **고객 프로필** 다음의 Braze 대시보드를 통해 개별 사용자 프로필에 액세스할 수 있습니다. **[사용자 검색]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/)** 페이지의 대시보드를 통해 개별 사용자 프로필에 액세스할 수 있습니다. 이메일 주소, 전화번호 또는 외부 사용자 ID를 통해 사용자 프로필을 찾은 후 **참여** 탭을 선택하여 사용자의 가입 상태를 확인하고 수동으로 조정할 수 있습니다.
2. **REST API 내보내기:** [세그먼트별 사용자]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) 내보내기 또는 [식별자별 사용자]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) 내보내기 엔드포인트를 사용하여 개별 고객 프로필을 JSON 형식으로 내보낼 수 있습니다. Braze는 기기별 푸시 인에이블먼트 정보가 포함된 푸시 토큰 객체를 반환합니다.

## 푸시 권한

iOS, 웹, Android 등 모든 푸시 지원 플랫폼은 아래에 설명된 약간의 차이점을 제외하고 OS 수준의 시스템 프롬프트를 통해 명시적인 옵트인 동의가 필요합니다.

사용자의 결정은 최종적이며 사용자가 거부한 후에는 다시 물어볼 수 없기 때문에 [푸시 프라이머]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) 인앱 메시지를 사용하는 것은 옵트인율을 높이기 위한 중요한 전략입니다.

**기본 OS 푸시 권한 프롬프트**

|플랫폼|스크린샷|설명|
|--|--|--|
|iOS| 메시지 하단에 '허용하지 않음'과 '허용' 버튼이 있는 "내 앱에서 알림을 보내려고 합니다"라는 iOS 기본 푸시 메시지가 표시됩니다.]({% image_buster /assets/img/push_implementation_guide/ios-push-prompt.png %}){: style="max-width:410px;"} | [임시 푸시](#provisional-push) 권한을 요청하는 경우에는 적용되지 않습니다.|
|Android| 메시지 하단에 "허용" 및 "허용 안 함" 버튼이 있는 "Kitchenerie에서 알림을 보내도록 허용하시겠습니까?"라고 묻는 Android 푸시 메시지.]({% image_buster /assets/img/push_implementation_guide/android-push-prompt.png %}){: style="max-width:410px;"} | 이 푸시 권한은 Android 13에 도입되었습니다. Android 13 이전에는 푸시를 보내는 데 권한이 필요하지 않았습니다.|
|웹| 웹 브라우저의 기본 푸시 메시지 하단에 '차단' 및 '허용' 버튼 두 개가 있는 "Braze.com 알림을 표시하려고 합니다"라는 메시지가 표시됩니다.]({% image_buster /assets/img/push_implementation_guide/web-push-prompt.png %}){: style="max-width:410px;"} | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Android

Android 13 이전에는 푸시 알림을 보내는 데 권한이 필요하지 않았습니다. Android 12 이하에서는 모든 사용자가 첫 번째 세션에서 Braze가 자동으로 푸시 토큰을 요청할 때 `Subscribed` 으로 간주됩니다. 이 시점에서 사용자는 해당 기기에 대해 유효한 푸시 토큰과 기본값인 `Subscribed` 으로 **푸시 인에이블먼트됩니다**.

[Android 13부터]({{site.baseurl}}/developer_guide/platforms/android/android_13/) 푸시 권한은 사용자에게 요청하여 부여받아야 합니다. 앱이 적절한 시기에 사용자에게 수동으로 권한을 요청할 수 있지만, 그렇지 않은 경우 앱이 [알림 채널을](https://developer.android.com/reference/android/app/NotificationChannel) 만들 때 사용자에게 자동으로 메시지가 표시됩니다.

### iOS

시스템 알림 센터의 알림 하단에 "Yachtr 앱에서 알림을 계속 수신하시겠습니까?"라는 메시지가 표시되며, 아래 두 개의 버튼으로 "유지" 또는 "끄기"를 선택할 수 있습니다.]({% image_buster /assets/img/push_implementation_guide/ios-provisional-push.png %}){: style="float:right;max-width:430px;width:40%;margin-left:15px;border:0"}

앱에서 임시 푸시 또는 승인된 푸시를 요청할 수 있습니다. 

인증 푸시는 알림을 보내기 전에 사용자의 명시적인 허가를 받아야 하는 반면, [임시 푸시를](https://www.braze.com/resources/articles/mastering-provisional-push) 사용하면 소리나 경고 없이 알림 센터로 바로 __조용히__ 알림을 보낼 수 있습니다.

#### 임시 승인 및 조용한 푸시 {#provisional-push}

iOS 12(2018년 출시) 이전 버전에서는 모든 사용자가 푸시 알림을 받으려면 명시적으로 옵트인해야 합니다.

iOS 12에서 Apple은 브랜드가 명시적으로 옵트인하기 전에 사용자의 알림 센터에 조용한 푸시 알림을 보낼 수 있는 [임시 승인](https://www.braze.com/resources/articles/mastering-provisional-push) 기능을 도입하여 메시지의 가치를 조기에 입증할 수 있는 기회를 제공했습니다. 자세한 내용은 [임시 승인을]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#provisional-push-authentication--quiet-notifications) 참조하세요.

### 웹

웹의 경우 기본 브라우저 권한 대화 상자를 통해 명시적인 사용자 옵트인을 요청해야 합니다.

앱에서 언제든지 권한 프롬프트를 표시할 수 있는 iOS 및 Android와 달리 일부 최신 브라우저에서는 '사용자 제스처'(마우스 클릭 또는 키 입력)에 의해 트리거된 경우에만 프롬프트가 표시됩니다. 사이트에서 페이지 로드 시 푸시 알림 권한을 요청하려고 하면 브라우저에서 무시되거나 무음 처리될 가능성이 높습니다.

따라서 페이지가 로드될 때 무작위로 권한을 요청하는 것이 아니라 사용자가 웹사이트의 어딘가를 클릭할 때만 권한을 요청해야 합니다.

## 푸시 토큰

[푸시 토큰은]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/) 사용자의 기기에서 생성되어 각 수신자의 알림을 보낼 위치를 식별하기 위해 Braze로 전송되는 고유한 익명 식별자입니다.

푸시 알림이 사용자에게 전송되는 방식을 이해하는 데 필수적인 두 가지 방법으로 [푸시 토큰을]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/) 분류할 수 있습니다.

1. **포그라운드 푸시는** 사용자 기기의 포그라운드로 정기적으로 눈에 보이는 푸시 알림을 보내는 기능을 제공합니다.
2. **백그라운드 푸시는** 특정 기기가 해당 브랜드의 푸시 알림을 수신하도록 옵트인했는지 여부와 관계없이 사용할 수 있습니다. 백그라운드 푸시를 사용하면 브랜드가 의도적으로 표시되지 않는 알림인 무음 푸시 알림을 기기에 전송하여 [제거 추적과]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking/) 같은 주요 기능을 지원할 수 있습니다.

고객 프로필에 앱과 연결된 유효한 포그라운드 푸시 토큰이 있는 경우, Braze는 해당 사용자가 해당 앱에 대해 "푸시 등록"된 것으로 간주합니다. 따라서 Braze는 이러한 사용자를 식별할 수 있도록 특정 세그먼트 필터( `Foreground Push Enabled for App,` )를 제공합니다.

{% alert note %}
`Foreground Push Enabled for App` 필터는 지정된 앱에 대해 유효한 포그라운드 및 백그라운드 푸시 토큰이 있는지 여부만 고려합니다. 그러나 보다 일반적인 [`Foreground Push Enabled`](#foreground-push-enabled) 필터는 워크스페이스의 모든 앱에 대해 푸시 알림을 명시적으로 활성화한 사용자를 세그먼트화합니다. 이 수에는 포그라운드 푸시만 포함되며 구독을 탈퇴한 사용자는 포함되지 않습니다. 이러한 필터 및 기타 필터에 대한 자세한 내용은 [세분화 필터에서]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) 확인할 수 있습니다.
{% endalert %}

### 하나의 기기에서 여러 사용자 사용

푸시 토큰은 기기와 앱 모두에 고유하므로 푸시 토큰을 사용하여 동일한 기기를 사용하는 여러 사용자를 구분할 수 없습니다.

예를 들어 사용자가 두 명이라고 가정해 보겠습니다: 찰리와 킴. 찰리가 자신의 휴대폰에서 앱에 대한 푸시 알림을 인에이블먼트한 상태에서 김이 찰리의 휴대폰을 사용하여 찰리의 프로필에서 로그아웃하고 자신의 프로필에 로그인하면 푸시 토큰이 김의 프로필에 다시 할당됩니다. 그러면 푸시 토큰은 김씨가 로그아웃하고 찰리가 다시 로그인할 때까지 해당 기기의 김씨의 프로필에 할당된 상태로 유지됩니다.

앱 또는 웹사이트는 기기당 푸시 구독을 하나만 할 수 있습니다. 따라서 사용자가 기기나 웹사이트에서 로그아웃하고 새 사용자가 로그인하면 푸시 토큰이 새 사용자에게 다시 할당됩니다. 이는 **참여** 탭의 **연락처 설정** 섹션에 있는 사용자 프로필에 반영됩니다:

고객 프로필의 \*\*참여** 탭에 있는 푸시 토큰 체인지로그에는 푸시 토큰이 다른 사용자에게 이동된 시점과 토큰이 무엇인지 나와 있습니다.]({% image_buster /assets/img/push_token_changelog.png %})

푸시 공급자(APN/FCM)가 하나의 기기에 있는 여러 사용자를 구분할 수 있는 방법이 없기 때문에 푸시 토큰을 마지막으로 로그인한 사용자에게 전달하여 푸시할 기기에서 어떤 사용자를 타겟팅할지 결정합니다.

### 여러 기기 및 한 명의 사용자

푸시 구독 상태는 사용자 기반이며 개별 앱에 특정되지 않습니다. 푸시 구독의 상태는 마지막으로 설정한 값입니다. 따라서 사용자가 푸시 알림을 옵트인한 경우 푸시 구독 상태는 해당되는 모든 기기에서 `Opted-in` 입니다. 사용자가 나중에 애플리케이션이나 브랜드에서 제공하는 다른 방법을 통해 푸시 알림을 명시적으로 탈퇴하면 푸시 구독 상태가 `Unsubscribed` 으로 업데이트되며 푸시 등록 기기는 푸시 알림을 수신할 수 없습니다.

## 포 그라운드 푸시 인에이블먼트 필터 {#foreground-push-enabled}

`Foreground Push Enabled` 는 마케터가 Braze에서 푸시 알림을 보내도록 허용한 사용자와 푸시 알림을 받지 않겠다는 의사를 표시하지 않은 사용자를 쉽게 식별할 수 있는 세분화 필터입니다. 

`Foreground Push Enabled` 필터는 다음을 고려합니다:
- Braze가 푸시 알림을 보내는 기능(포그라운드 푸시 토큰)
- 사용자의 전반적인 기기 푸시 수신 선호도(푸시 구독 상태)

사용자가 "푸시 마케팅에 등록됨(iOS)"으로 표시된 대시보드 스크린샷]({% image_buster /assets/img/push_enablement.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

사용자가 워크스페이스 내 앱에 대해 활성 포그라운드 푸시 토큰을 가지고 있는 경우 "푸시 사용" 또는 "푸시 등록"으로 간주되며, 이는 푸시 인에이블먼트 상태가 앱별로 다르다는 의미입니다. 

{% alert note %}
푸시 등록 상태를 확인하는 방법에 대한 자세한 내용은 [푸시 등록 상태를]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#checking-push-registration-status) 참조하세요.
{% endalert %}

## 기타 플랫폼별 시나리오

{% tabs %}
{% tab Android %}

포그라운드 푸시 인에이블먼트 사용자가 OS 설정에서 푸시를 비활성화하면 다음 세션이 시작될 때 푸시가 비활성화됩니다:
- Braze는 이들을 포그라운드 푸시 비활성화로 표시하고 더 이상 푸시 메시지를 보내려고 시도하지 않습니다.
- `Foreground Push Enabled for App (Android)` 필터와 `Foreground Push Enabled` 세분화 필터(고객 프로필에 유효한 포그라운드 푸시 토큰을 가진 다른 앱이 없다고 가정)는 `false` 을 반환합니다.

이 시나리오에서는 백그라운드 푸시 토큰이 계속 존재하므로 세그먼트화 필터를 사용하여 백그라운드(무음) 푸시 알림을 계속 보낼 수 있습니다 `Background or Foreground Push Enabled = true`.

Android의 경우 다음과 같은 경우 Braze는 사용자 푸시를 비활성화한 것으로 간주합니다:

- 사용자가 기기에서 앱을 삭제합니다.
- 반송으로 인해 푸시 메시지가 전달되지 못했습니다. 이는 앱 제거로 인해 발생하는 경우가 많지만 앱 업데이트, 새로운 푸시 토큰 버전 또는 형식으로 인해 발생할 수도 있습니다. 
- 푸시 등록이 Firebase Cloud 메시징에 실패합니다(네트워크 연결 상태가 좋지 않거나 FCM에 연결하여 유효한 토큰을 반환하지 못하여 발생하는 경우도 있음).
- 사용자는 기기 설정에서 앱에 대한 푸시 알림을 차단하고 이후 세션을 기록합니다.

{% alert note %}
앱이 포그라운드 또는 백그라운드에 있지만 아직 실행 중인 경우에만 Android 푸시 알림을 가로챌 수 있습니다. 앱이 종료되거나 완전히 종료된 경우에는 알림을 가로챌 수 없습니다.
{% endalert %}

{% endtab %}
{% tab iOS %}

사용자가 포그라운드 푸시 옵트인 안내를 수락했는지 여부에 관계없이 Xcode에서 원격 알림이 인에이블먼트되어 있고 앱에서 호출 [`registerForRemoteNotifications()`](https://developer.apple.com/documentation/uikit/uiapplication/1623078-registerforremotenotifications).

앱이 잠정적으로 승인되었거나 사용자가 푸시를 옵트인한 경우 포그라운드 푸시 토큰을 수신하여 모든 유형의 푸시를 보낼 수 있습니다. Braze에서는 iOS에서 포그라운드 푸시가 활성화된 사용자를 명시적(앱 수준) 또는 잠정적(기기 수준)으로 푸시 인에이블된 것으로 간주합니다.

사용자가 OS 수준에서 푸시 알림 수신을 거부하는 경우 푸시 구독 상태는 `Subscribed` 이며, 고객 프로필에 포그라운드 푸시 토큰이 등록되었다는 사실이 표시되지 않습니다. 

처음에 OS 수준에서 옵트인한 사용자가 OS 설정에서 푸시 알림을 비활성화하는 경우 다음 세션 시작 시 다음과 같은 일이 발생합니다:
- Braze는 이들을 포그라운드 푸시 비활성화로 표시하고 더 이상 푸시 메시지를 보내려고 시도하지 않습니다.
- `Foreground Push Enabled for App (iOS)` 필터와 `Foreground Push Enabled` 세분화 필터(고객 프로필에 유효한 포그라운드 푸시 토큰을 가진 다른 앱이 없다고 가정)는 `false` 을 반환합니다.

이 시나리오에서는 백그라운드 푸시 토큰이 계속 존재하므로 세그먼트화 필터를 사용하여 백그라운드(무음) 푸시 알림을 계속 보낼 수 있습니다 `Background or Foreground Push Enabled = true`.

{% alert note %}
iOS에서는 푸시 알림이 표시되기 전에 앱이 푸시 알림을 가로채는 것을 허용하지 않습니다. 즉, 앱(및 Braze)은 알림을 표시하거나 숨길 수 있는지 여부를 제어할 수 없습니다. 사용자는 기기 설정에서 앱의 푸시 알림을 옵트아웃할 수 있지만, 이는 운영 체제에 의해 제어됩니다.
{% endalert %}

{% endtab %}
{% tab Web %}

사용자가 기본 푸시 권한 프롬프트를 수락하면 구독 상태가 `opted in` 로 변경됩니다.

구독을 관리하려면 사용자 방법( [`setPushNotificationSubscriptionType`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype) 를 사용하여 사이트에 기본 설정 페이지를 만든 후 대시보드에서 옵트아웃 상태별로 사용자를 필터링할 수 있습니다.

사용자가 브라우저 내에서 알림을 비활성화하면 해당 사용자에게 전송되는 다음 푸시 알림은 반송되며, Braze는 이에 따라 사용자의 푸시 토큰을 업데이트합니다. 푸시 인에이블먼트 필터(`Background or Foreground Push Enabled`, `Foreground Push Enabled` 및 `Foreground Push Enabled for App`)에 대한 자격을 관리하는 데 사용됩니다. 사용자 프로필에 설정된 구독 상태는 사용자 수준 설정이며 푸시가 반송되어도 변경되지 않습니다.

{% alert note %}
웹 플랫폼은 백그라운드 또는 무음 푸시를 허용하지 않습니다.
{% endalert %}
{% endtab %}
{% endtabs %}

## 모범 사례

Braze에서 푸시 사용을 최적화하는 방법에 대한 자세한 안내는 [푸시 모범 사례에]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices) 대한 전용 문서를 참조하세요.

