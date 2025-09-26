---
nav_title: "푸시 활성화 및 구독"
article_title: 푸시 활성화 및 구독
page_order: 3
page_type: reference
description: "이 참조 문서에서는 Braze에서 푸시 활성화 및 푸시 구독 상태의 개념과 iOS, Android 및 웹에서의 동작의 근본적인 차이점에 대해 설명합니다."
channel:
  - push

---

# 푸시 활성화 및 푸시 구독

> 이 참조 문서에서는 Braze에서 푸시 인에이블먼트 및 푸시 구독 상태의 개념과 iOS, Android 및 웹에서의 동작의 근본적인 차이점에 대해 설명합니다.

## 푸시 구독 상태 {#push-sub-states}

Braze의 '푸시 구독 상태'는 푸시 알림 수신에 대한 **사용자의** 글로벌 선호도를 식별합니다. 구독 상태는 사용자 기반이므로 개별 앱에 한정되지 않습니다. 구독 상태는 푸시 알림을 타겟팅할 사용자를 결정할 때 유용한 플래그가 됩니다.

{% alert note %}
사용자의 푸시 구독 상태는 사용자의 모든 디바이스를 포함한 전체 사용자 프로필에 적용됩니다.
{% endalert %}

푸시 구독 상태 옵션에는 세 가지인 `Subscribed`, `Opted-In`, `Unsubscribed`입니다.

기본적으로 사용자가 푸시를 통해 메시지를 받으려면 푸시 구독 상태가 `Subscribed` 또는 `Opted-In`이어야 하며 [푸시를 사용하도록](#push-enabled) 설정되어 있어야 합니다. 메시지를 작성할 때 필요한 경우 이 설정을 재정의할 수 있습니다.

|옵트인 상태|설명|
|---|---|
|`Subscribed`| Braze에서 사용자 프로필을 생성할 때의 기본 푸시 구독 상태입니다. |
|`Opted-In`| 사용자가 푸시 알림 수신을 명시적으로 선호한다고 밝혔습니다. 사용자가 OS 수준의 푸시 메시지를 수락하면 Braze는 사용자의 옵트인 상태를 `Opted-In`으로 자동 이동합니다.<br><br>Android 12 이하 사용자에게는 적용되지 않습니다.|
|`Unsubscribed`| 사용자가 애플리케이션 또는 브랜드가 제공하는 기타 방법을 통해 푸시 수신을 명시적으로 취소한 경우. 기본값으로 Braze 푸시 캠페인은 `Subscribed` 또는 `Opted-in`인 사용자만 푸시 대상으로 지정합니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Braze는 사용자의 푸시 구독 상태를 `Unsubscribed` 로 자동 변경하지 않습니다. 사용자의 푸시 구독 상태가 `Unsubscribed`인 경우 세분화에서 사용자의 `Push Enabled` 필터는 `false`가 됩니다.
{% endalert %}

### 푸시 구독 상태 업데이트하기 {#update-push-subscription-state}

사용자의 푸시 구독 상태를 업데이트하는 방법에는 세 가지가 있습니다:

#### 자동 옵트인(기본값)

기본적으로 Braze는 사용자가 앱에 대한 푸시 알림을 처음 승인할 때 사용자의 푸시 구독 상태를 `Opted-In`으로 설정합니다. 또한 사용자가 이전에 푸시 권한을 비활성화했다가 시스템 설정에서 다시 활성화하는 경우에도 Braze는 이 작업을 수행합니다.

{% tabs local %}
{% tab Android %}
이 기본 동작을 비활성화하려면 Android Studio 프로젝트의 `braze.xml` 파일에 다음 속성정보를 추가하세요.

```xml
<bool name="com_braze_optin_when_push_authorized">false</bool>
```
{% endtab %}

{% tab swift %}
[Braze Swift SDK 버전 7.5.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/7.5.0)부터는 Xcode 프로젝트의 `AppDelegate.swift` 파일에 `optInWhenPushAuthorized` 구성을 추가하여 이 동작을 비활성화하거나 추가로 사용자 지정할 수 있습니다.

```swift
configuration.optInWhenPushAuthorized = false // disables the default behavior

let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endtab %}
{% endtabs %}

#### SDK 통합

[웹](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype), [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-push-notification-subscription-type.html) 또는 [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/set(pushnotificationsubscriptionstate:))에서 `setPushNotificationSubscriptionType` 방법을 사용하여 Braze SDK로 사용자의 구독 상태를 업데이트할 수 있습니다. 예를 들어, 이 방법을 사용하여 앱에서 사용자가 수동으로 푸시 알림을 사용하거나 사용하지 않도록 설정할 수 있는 설정 페이지를 만들 수 있습니다.

#### REST API

You can update a user's subscription state with the Braze REST API using the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) to update their [`push_subscribe`]({{site.baseurl}}/api/objects_filters/user_attributes_object) attribute.

### 푸시 구독 상태 확인

![User profile for John Doe with their push subscription state set to Subscribed.]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Braze에서 사용자의 푸시 구독 상태를 확인할 수 있는 방법은 두 가지가 있습니다:

1. **사용자 프로필**: You can access individual user profiles through the Braze dashboard on the **[User Search]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/)** page. 이메일 주소, 전화번호 또는 외부 사용자 ID를 통해 사용자의 프로필을 찾은 후 **참여** 탭을 선택하여 사용자의 가입 상태를 확인하고 수동으로 조정할 수 있습니다.
<br><br>
2. **나머지 API 내보내기**: You can export individual user profiles in JSON format using the export [Users by segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) or [Users by identifier]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) endpoints. Braze는 디바이스별 푸시 활성화 정보가 포함된 푸시 토큰 객체를 반환합니다.

## 푸시 권한

iOS, 웹, Android 등 모든 푸시 지원 플랫폼에서는 OS 수준의 시스템 프롬프트를 통해 명시적으로 옵트인해야 하며, 아래에 설명된 몇 가지 차이점이 있습니다.

Because a user's decision is final and you can't ask again after they decline, using [push primer]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) in-app messages is an important strategy for increasing your opt-in rates.

**기본 OS 푸시 권한 프롬프트**

|플랫폼|스크린샷|설명|
|--|--|--|
|iOS| ![An iOS native push prompt asking "My App would like to send you notifications" with two buttons, "Don't Allow" and "Allow" at the bottom of the message.]({% image_buster /assets/img/push_implementation_guide/ios-push-prompt.png %}){: style="max-width:410px;"} | [임시 푸시](#provisional-push) 권한을 요청하는 경우에는 적용되지 않습니다.|
|Android| ![An Android push message asking "Allow Kitchenerie to send you notifications?" with two buttons, "Allow" and "Don't allow" at the bottom of the message.]({% image_buster /assets/img/push_implementation_guide/android-push-prompt.png %}){: style="max-width:410px;"} | 이 푸시 권한은 Android 13에 도입되었습니다. Android 13 이전에는 푸시 전송에 권한이 필요하지 않았습니다.|
|웹| ![A web browser's native push prompt asking "Braze.com wants to show notification" with two buttons, "Block" and "Allow" at the bottom of the message.]({% image_buster /assets/img/push_implementation_guide/web-push-prompt.png %}){: style="max-width:410px;"} | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Android

Android 13 이전에는 푸시 알림을 보내는 데 권한이 필요하지 않았습니다. Android 12 이하에서는 모든 사용자가 첫 번째 세션에서 Braze가 자동으로 푸시 토큰을 요청할 때 `Subscribed`로 간주됩니다. 이 시점에서 사용자는 해당 기기에 대해 유효한 푸시 토큰과 기본 구독 상태인 `Subscribed`로 **푸시가 활성화됩니다**.

Starting with [Android 13]({{site.baseurl}}/developer_guide/platforms/android/android_13/), push permission must be asked of and granted by the user. Your app can manually request permission from the user at opportune times, but if not, users will be prompted automatically when your app creates a [notification channel](https://developer.android.com/reference/android/app/NotificationChannel).

### iOS

![A notification in the system Notification Center with a message at the bottom asking, "Keep receiving notifications from the Yachtr app?" with two buttons below to "Keep" or "Turn Off"]({% image_buster /assets/img/push_implementation_guide/ios-provisional-push.png %}){: style="float:right;max-width:430px;width:40%;margin-left:15px;border:0"}

앱에서 임시 푸시 또는 승인된 푸시를 요청할 수 있습니다. 

Authorized push requires explicit permission from a user before sending any notifications, whereas [provisional push](https://www.braze.com/resources/articles/mastering-provisional-push) lets you send notifications __quietly__, directly to the notification center without any sound or alert.

#### 임시 승인 및 조용한 푸시 {#provisional-push}

iOS 12(2018년 출시) 이전 버전에서는 모든 사용자가 푸시 알림을 받으려면 명시적으로 동의해야 합니다.

In iOS 12, Apple introduced [provisional authorization](https://www.braze.com/resources/articles/mastering-provisional-push), allowing brands to send quiet push notifications to their users' notification center before they explicitly opt-in, giving you a chance to demonstrate the value of your messages early. Refer to [provisional authorization]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#provisional-push-authentication--quiet-notifications) to learn more.

### 웹

웹의 경우 기본 브라우저 권한 대화 상자를 통해 명시적인 사용자 옵트인을 요청해야 합니다.

앱에서 언제든지 권한 프롬프트를 표시할 수 있는 iOS 및 Android와 달리 일부 최신 브라우저에서는 '사용자 제스처'(마우스 클릭 또는 키 입력)에 의해 트리거된 경우에만 프롬프트가 표시됩니다. 사이트에서 페이지 로드 시 푸시 알림 권한을 요청하려고 하면 브라우저에서 무시되거나 무음 처리될 가능성이 높습니다.

따라서 페이지가 로드될 때 무작위로 권한을 요청하는 것이 아니라 사용자가 웹사이트의 어딘가를 클릭할 때만 권한을 요청해야 합니다.

## 푸시 토큰

[Push tokens]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/) are a unique anonymous identifier generated by a user's device and sent to Braze to identify where to send each recipient's notification.

There are two ways a [push token]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/) can be classified that are essential to understanding how a push notification can be sent to your users.

1. **포그라운드 푸시**는 사용자 기기의 포그라운드로 정기적으로 눈에 보이는 푸시 알림을 보내는 기능을 제공합니다.
2. **백그라운드 푸시**는 특정 기기가 해당 브랜드의 푸시 알림을 수신하도록 옵트인했는지 여부와 관계없이 사용할 수 있습니다. Background push allows brands to send silent push notifications - notifications that intentionally aren't displayed - to devices to support key functionalities like [uninstall tracking]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking/).

사용자 프로필에 앱과 연결된 유효한 포그라운드 푸시 토큰이 있는 경우, Braze는 해당 사용자가 해당 앱에 대해 "푸시 등록"된 것으로 간주합니다. 따라서 Braze는 이러한 사용자를 식별하는 데 도움이 되는 특정 세분화 필터(`Push Enabled for App,`)를 제공합니다.

{% alert note %}
`Push Enabled for App` 필터는 지정된 앱에 유효한 포그라운드 및 백그라운드 푸시 토큰이 있는지 여부만 고려합니다. 그러나 보다 일반적인 [`Push Enabled`](#push-enabled) 필터는 워크스페이스의 모든 앱에 대해 명시적으로 푸시 알림을 활성화한 사용자를 세그먼트화합니다. 이 수에는 포그라운드 푸시만 포함되며 구독을 취소한 사용자는 포함되지 않습니다. 이러한 필터 및 기타 필터에 대한 자세한 내용은 [세분화 필터에서]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) 확인할 수 있습니다.
{% endalert %}

### 하나의 기기에서 여러 사용자

푸시 토큰은 디바이스와 앱 모두에 고유하므로 푸시 토큰을 사용하여 동일한 디바이스를 사용하는 여러 사용자를 구분하는 것은 불가능합니다.

예를 들어 사용자가 두 명이라고 가정해 보겠습니다: 바로 찰리와 킴입니다. 찰리가 자신의 휴대폰에서 내 앱의 푸시 알림을 사용 설정한 상태에서 킴이 찰리의 휴대폰을 사용하여 찰리의 프로필에서 로그아웃하고 자신의 프로필에 로그인하면 푸시 토큰이 킴의 프로필에 다시 할당됩니다. 그러면 푸시 토큰은 킴씨가 로그아웃하고 찰리가 다시 로그인할 때까지 해당 기기의 킴씨 프로필에 할당된 상태로 유지됩니다.

앱 또는 웹사이트는 기기당 하나의 푸시 구독만 허용됩니다. 따라서 사용자가 디바이스나 웹사이트에서 로그아웃하고 새 사용자가 로그인하면 푸시 토큰이 새 사용자에게 다시 할당됩니다. 이는 **참여** 탭의 **연락처 설정** 섹션에 있는 사용자 프로필에 반영됩니다:

![Push token changelog on the \*\*Engagement** tab of a user's profile, which lists when the push token was moved to another user, and what the token was.]({% image_buster /assets/img/push_token_changelog.png %})

푸시 공급자(APN/FCM)가 한 기기에 있는 여러 사용자를 구분할 수 있는 방법이 없으므로, 푸시 토큰을 마지막으로 로그인한 사용자에게 전달하여 기기에서 푸시 타겟팅할 사용자를 결정합니다.

### 여러 기기, 한 명의 사용자

푸시 구독 상태는 사용자 기반이며 개별 앱에 특정되지 않습니다. 푸시 구독의 상태는 마지막으로 설정한 값입니다. 따라서 사용자가 푸시 알림을 수신 동의한 경우 해당 사용자의 푸시 구독 상태는 모든 적격 기기에서 `Opted-in`입니다. 사용자가 나중에 애플리케이션이나 브랜드에서 제공하는 다른 방법을 통해 푸시 알림을 명시적으로 수신 거부하면 푸시 구독 상태가 `Unsubscribed`로 업데이트되고 푸시 등록한 기기에서 푸시 알림을 수신할 수 없게 됩니다.

## 푸시 사용 필터 {#push-enabled}

`Push Enabled`는 마케팅 담당자가 Braze에서 푸시 알림 전송을 허용한 사용자와 푸시 알림 수신을 거부하지 않은 사용자를 쉽게 식별할 수 있는 세분화 필터입니다. 

`Push Enabled` 필터는 다음을 고려합니다:
- Braze가 푸시 알림(포그라운드 푸시 토큰)을 보내는 기능
- 사용자의 모든 디바이스에서 푸시 수신에 대한 전반적인 선호도(푸시 구독 상태)

![A screenshot of the dashboard showing a user is "Push Registered for Marketing (iOS)"]({% image_buster /assets/img/push_enablement.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

사용자가 워크스페이스 내 앱에 대해 활성 포그라운드 푸시 토큰을 가지고 있으면 "푸시 사용" 또는 "푸시 등록"으로 간주되며, 이는 푸시 인에이블먼트 상태가 앱별로 다르다는 의미입니다. 

{% alert note %}
푸시 등록 상태를 확인하는 방법에 대한 자세한 내용은 [푸시 등록 상태]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#checking-push-registration-status)를 참조하세요.
{% endalert %}

## 기타 플랫폼별 시나리오

{% tabs %}
{% tab Android %}

포그라운드 푸시를 사용하도록 설정한 사용자가 OS 설정에서 푸시를 비활성화하면 다음 세션이 시작될 때 푸시를 사용할 수 없게 됩니다.
- Braze는 이들에게 포그라운드 푸시 비활성화로 표시하고 더 이상 푸시 메시지를 보내려고 시도하지 않습니다.
- `Push Enabled for App (Android)` 필터와 `Push Enabled` 세분화 필터(고객 프로필에 유효한 포그라운드 푸시 토큰을 가진 다른 앱이 없다고 가정)는 `false`를 반환합니다.

이 시나리오에서는 백그라운드 푸시 토큰이 계속 존재하므로 세그먼테이션 필터 `Background Push Enabled = true`를 사용하여 백그라운드(무음) 푸시 알림을 계속 보낼 수 있습니다.

Android의 경우 Braze는 다음과 같은 경우 사용자 푸시가 비활성화된 것으로 간주합니다:

- 사용자가 기기에서 앱을 삭제합니다.
- 반송으로 인해 푸시 메시지가 전달되지 못했습니다. 이는 앱 제거로 인해 발생하는 경우가 많지만 앱 업데이트, 새로운 푸시 토큰 버전 또는 포맷으로 인해 발생할 수도 있습니다. 
- 푸시 등록에 실패한 경우(네트워크 연결 상태가 좋지 않거나 FCM에 연결하지 못하여 유효한 토큰을 반환하지 못하여 발생하는 경우가 있음) Firebase 클라우드 메시징에 푸시 등록이 실패합니다.
- 사용자는 기기 설정에서 앱에 대한 푸시 알림을 차단하고 이후 세션을 기록합니다.

{% endtab %}
{% tab iOS %}

사용자가 포그라운드 푸시 옵트인 프롬프트에 동의하는지 여부에 관계없이 Xcode에서 원격 알림을 활성화하고 앱에서 [`registerForRemoteNotifications()`](https://developer.apple.com/documentation/uikit/uiapplication/1623078-registerforremotenotifications)을 호출합니다.

앱이 잠정적으로 승인되었거나 사용자가 푸시를 선택하면 포그라운드 푸시 토큰을 수신하여 모든 유형의 푸시를 보낼 수 있습니다. Braze에서는 iOS에서 포그라운드 푸시가 활성화된 사용자를 명시적(앱 수준) 또는 잠정적(기기 수준)으로 푸시가 활성화된 것으로 간주합니다.

사용자가 OS 수준에서 푸시 알림 수신을 거부하면 푸시 구독 상태는 `Subscribed`가 되고 프로필에 포그라운드 푸시 토큰이 등록되었다는 사실이 표시되지 않습니다. 

처음에 OS 수준에서 옵트인한 사용자가 OS 설정에서 푸시 알림을 비활성화하는 경우 다음 세션이 시작될 때 다음과 같은 일이 발생합니다.
- Braze는 이들에게 포그라운드 푸시 비활성화로 표시하고 더 이상 푸시 메시지를 보내려고 시도하지 않습니다.
- `Push Enabled for App (iOS)` 필터와 `Push Enabled` 세분화 필터(고객 프로필에 유효한 포그라운드 푸시 토큰을 가진 다른 앱이 없다고 가정)는 `false`를 반환합니다.

이 시나리오에서는 백그라운드 푸시 토큰이 계속 존재하므로 세그먼테이션 필터 `Background Push Enabled = true`를 사용하여 백그라운드(무음) 푸시 알림을 계속 보낼 수 있습니다.

{% endtab %}
{% tab 웹 %}

사용자가 기본 푸시 권한 프롬프트를 수락하면 구독 상태가 `opted in`으로 변경됩니다.

구독을 관리하려면 사용자 방법([`setPushNotificationSubscriptionType`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype))을 사용하여 사이트에 기본 설정 페이지를 만든 다음 대시보드에서 수신 거부 상태별로 사용자를 필터링할 수 있습니다.

사용자가 브라우저 내에서 알림을 비활성화하면 해당 사용자에게 전송되는 다음 푸시 알림은 반송되며, Braze는 이에 따라 사용자의 푸시 토큰을 업데이트합니다. 푸시 사용 필터(`Background Push Enabled`, `Push Enabled` 및 `Push Enabled for App`)에 대한 자격을 관리하는 데 사용됩니다. 고객 프로필에 설정된 구독 상태는 사용자 수준 설정이며 푸시가 반송되어도 변경되지 않습니다.

{% alert note %}
웹 플랫폼은 백그라운드 또는 자동 푸시를 허용하지 않습니다.
{% endalert %}
{% endtab %}
{% endtabs %}

## 모범 사례

Braze에서 푸시 사용을 최적화하는 방법에 대한 자세한 지침은 [푸시 모범 사례]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices)에 대한 전용 문서를 참조하세요.

