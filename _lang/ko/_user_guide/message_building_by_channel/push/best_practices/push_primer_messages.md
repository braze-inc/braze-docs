---
nav_title: Push primer in-app messages
article_title: 푸시 프라이머 인앱 메시지
page_order: 1
page_type: reference
description: "이 문서에서는 푸시 프라이머 인앱 메시지의 전제 조건과 설정 방법에 대해 설명합니다."
channel: push

---

# 푸시 프라이머 인앱 메시지

![스트리밍 앱용 푸시 프라이머 인앱 메시지. 알림에는 "Movie Cannon에서 푸시 알림을 받으시겠습니까? 알림에는 새 영화, TV 프로그램 또는 기타 알림이 포함될 수 있으며 언제든지 해제할 수 있습니다."라고 적혀 있습니다]({% image_buster /assets/img_archive/push_primer_iam.png %}){: style="float:right;max-width:40%;margin-left:15px;border:none;"}

> 사용자에게 푸시 권한을 요청할 수 있는 기회는 한 번뿐이므로 푸시 등록을 최적화하는 것은 푸시 메시지의 도달 범위를 극대화하는 데 매우 중요합니다. 이를 위해 기본 푸시 메시지를 표시하기 전에 인앱 메시지를 사용하여 사용자가 옵트인할 경우 수신할 수 있는 메시지 유형을 설명할 수 있습니다. 이를 푸시 프라이머라고 합니다.

Braze에서 푸시 프라이머 인앱 메시지를 생성하려면 iOS, Android 또는 웹용 인앱 메시지를 생성할 때 버튼 클릭 동작 "푸시 권한 요청"을 사용하면 됩니다.

## 필수 조건

This feature requires [button on-click behavior](#button-actions), which is supported in the following minimum versions or later:

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

Additionally, note the following platform-specific details:

{% tabs local %}
{% tab android %}
|OS version|Additional information|
\|----------|----------------------|
| **Android 12 and earlier** | Implementing push primers is not recommended because push is opted-in by default. |
| **Android 13+** | If a user denies your push permission prompt twice, Android blocks further prompts—including Braze push primer messages. To grant permission after this, users must manually enable push for your app in their device settings. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}

{% tab swift %}
### General information

- The push prompt can be displayed only once per install, enforced by the operating system.
- 앱의 푸시 설정이 명시적으로 켜져 있거나 꺼져 있는 경우에는 프롬프트가 표시되지 않습니다. [임시 권한이](https://developer.apple.com/documentation/usernotifications/asking_permission_to_use_notifications#3544375) 있는 사용자에게만 표시됩니다.
  - **App's push setting is on:** 사용자가 이미 옵트인했기 때문에 Braze는 인앱 메시지를 표시하지 않습니다.
  - **App's push setting is off:** 기기 설정에서 사용자를 앱의 푸시 알림 설정으로 리디렉션해야 합니다.

### 수동 코드 제거

이 튜토리얼을 사용하여 설정한 인앱 메시지는 사용자가 인앱 메시지 버튼을 클릭하면 기본 푸시 프롬프트 코드를 자동으로 호출합니다. 푸시 알림 권한을 두 번 요청하거나 잘못된 시간에 요청하는 것을 방지하려면 개발자가 구현한 기존 푸시 알림 통합을 수정하여 인앱 메시지가 사용자에게 가장 먼저 표시되는 푸시 알림 프라이머가 되도록 해야 합니다.

개발팀은 앱 또는 사이트에 대한 푸시 알림 구현을 검토하고 푸시 권한을 요청하는 코드를 수동으로 제거해야 합니다. 예를 들어 다음 코드에 대한 참조를 제거합니다:

{% subtabs %}
{% subtab OBJECTIVE-C %}
```objc
requestAuthorizationWithOptions
```
{% endsubtab %}
{% subtab swift %}
```swift
requestAuthorization
```
{% endsubtab %}
{% subtab JavaScript %}
```javascript
braze.requestPushPermission()
// or
appboy.registerAppboyPushMessages()
```
{% endsubtab %}
{% subtab Java %}
```java
android.permission.POST_NOTIFICATIONS
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## 1단계: 인앱 메시지 만들기

First, [create an in-app message]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/), then select your message type and layout.

To ensure you have enough space for both your message and buttons, use a fullscreen or modal message layout. If you choose fullscreen, note that an image is required.

## 2단계: 메시지 작성

이제 사본을 추가할 차례입니다! 푸시 프라이머는 사용자가 푸시 알림을 켜도록 유도하는 역할을 한다는 점을 기억하세요. 메시지 본문에서 사용자가 푸시 알림을 사용 설정해야 하는 이유를 강조하는 것이 좋습니다. 어떤 유형의 알림을 보낼지, 어떤 가치를 제공할 수 있을지 구체적으로 정하세요.

예를 들어 뉴스 앱은 다음과 같은 푸시 프라이머를 사용할 수 있습니다:

```plaintext
Breaking news on the go! Enable push notifications to get alerts for major stories and topics that matter to you.
```

스트리밍 앱은 다음을 사용할 수 있습니다:

```plaintext
Get push notifications from Movie Cannon? Notifications may include new movies, TV shows, or other notices and can be turned off at any time.
```

For best practices and additional resources, refer to [Creating custom opt-in prompts]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).

## 3단계: 버튼 동작 지정 {#button-actions}

인앱 메시지에 버튼을 추가하려면 인앱 메시지의 기본 및 보조 버튼 역할을 하는 두 개의 **버튼** 블록을 메시지로 드래그하면 됩니다. You can also drag a row into your message, and then drag the buttons into the row, so that the buttons are on the same horizontal row (as opposed to stacked on top of each other). 시작 버튼으로 '알림 허용' 및 '지금은 안 함'을 권장하지만, 다양한 버튼 프롬프트를 지정할 수 있습니다.

버튼 복사본을 추가한 후 각 버튼의 클릭 시 동작을 지정합니다:

- **버튼 1:** 이를 '메시지 닫기'로 설정합니다. 이 버튼은 보조 버튼 또는 "지금 안 함" 옵션입니다.
- **버튼 2:** 이를 "푸시 권한 요청"으로 설정합니다. 이 버튼은 기본 버튼 또는 "알림 허용" 옵션입니다.

![In-app message composer with two buttons: "알림 허용" 및 "지금은 안함"을 선택합니다.]({% image_buster /assets/img_archive/push_primer_button_behavior.png %})

## 4단계: 배송 예약

푸시 프라이머가 적절한 시간에 전송되도록 설정하려면 인앱 메시지를 **커스텀 이벤트 수행**을 트리거 동작으로 사용하여 작업 기반 메시지로 예약해야 합니다.

이상적인 시기는 다양하지만, Braze는 사용자가 앱이나 사이트에서 가치를 느끼기 시작했거나 푸시 알림으로 해결할 수 있는 강력한 요구 [사항](https://www.braze.com/resources/videos/mapping-high-value-actions)(예: 주문 후 배송 추적 정보를 제공하려는 경우)이 있을 때까지 기다릴 것을 제안합니다. 이렇게 하면 프롬프트가 브랜드에만 도움이 되는 것이 아니라 고객에게도 도움이 됩니다.

!["관심 목록에 추가"라는 커스텀 이벤트를 수행한 사용자에게 보낼 실행 기반 전달 설정입니다.]({% image_buster /assets/img_archive/push_primer_trigger.png %})

## 5단계: 타겟 사용자

푸시 프라이머 캠페인의 목표는 아직 푸시 권한을 부여하지 않은 모든 기기의 사용자에게 푸시 권한을 부여하라는 메시지를 표시하는 것입니다. 여기에는 처음 사용하는 사용자나 새 기기를 구입하거나 애플리케이션을 다시 설치하는 기존 사용자가 포함될 수 있습니다.

{% alert important %}
**코드가 없는 푸시 프라이머로 자동 억제**: 코드 없는 푸시 프라이머("푸시 권한 요청" 버튼 동작)를 사용하는 경우 세분화에 푸시 구독 필터를 추가할 필요가 없습니다. 소프트웨어 개발 키트는 다른 기기에서 사용자의 푸시 상태와 관계없이 이미 활성 푸시 토큰이 있는 기기의 인앱 메시지를 자동으로 억제합니다. 여러 기기를 가진 사용자를 타겟팅하는 방법에 대한 자세한 내용은 [여러 기기를 가진 사용자 타겟팅하기를](#targeting-users-with-multiple-devices) 참조하세요.
{% endalert %}

코드 없는 푸시 프라이머를 사용하지 않는 경우 `Foreground Push Enabled For App is false` 에 필터를 추가하세요. 이 필터는 포그라운드 푸시 알림에 아직 옵트인하지 않은 개별 앱 설치를 식별합니다.

{% alert important %}
`Push Subscription Status is not Opted In` 같은 사용자 수준 필터를 사용하면 다른 기기에서 이미 옵트인한 사용자는 제외되므로 새 기기에서 안내 메시지를 받지 못합니다.
{% endalert %}

그 외에도 가장 적절하다고 생각되는 추가 세그먼트를 결정할 수 있습니다. 예를 들어, 두 번째 구매를 완료한 사용자, 방금 계정을 만들어 회원이 된 사용자 또는 일주일에 두 번 이상 앱을 방문하는 사용자를 타겟팅할 수 있습니다. 이러한 중요한 세그먼트의 사용자를 타겟팅하면 사용자가 푸시 사용을 허용하고 옵트인할 가능성이 높아집니다.

### 여러 기기를 사용하는 사용자 타겟팅하기

Braze는 기기 수준이 아닌 프로필 수준에서 사용자 데이터를 캡처하기 때문에 여러 대의 기기를 소유한 사용자를 타겟팅하는 것이 어려울 수 있습니다. 세분화된 푸시 구독 필터는 특정 타겟팅된 기기의 구독 상태가 아닌 단일 기기의 구독 상태를 기반으로 사용자를 포함하거나 제외합니다. 또한 iOS의 임시 상태는 기술적으로 이러한 기기에 포그라운드 푸시 토큰이 있지만 사용자가 명시적으로 옵트인하지 않았기 때문에 복잡성을 더합니다.

#### 푸시 구독 필터의 문제점

사용자가 푸시 구독 상태가 다른 여러 대의 기기를 보유하고 있는 경우 세분화의 푸시 구독 필터가 일부 기기를 타겟팅하지 못할 수 있습니다. 다음 시나리오를 고려하세요:

{% details Scenario 1: User has two devices on different platforms %}

**사용자에게 두 개의 기기가 있습니다:**
- 기기 A: Android, 푸시 옵트인됨
- 기기 B: iOS, 푸시 옵트인하지 않음

**작동하지 않는 세그먼트 필터:**
- `Push enabled = false` - 사용자는 Android 기기에서 푸시 인에이블먼트가 활성화되어 있으므로 세그먼트에 포함되지 않습니다. 이 세그먼트에는 iOS 기기가 포함되지 않습니다.
- `Push subscription status is not opted in` - 사용자는 Android 기기에서 푸시 인에이블먼트가 활성화되어 있으므로 세그먼트에 포함되지 않습니다. 이 세그먼트에는 iOS 기기가 포함되지 않습니다.

**작동하는 세그먼트 필터:**
- `Push enabled for iOS = false` - 사용자는 Android 기기에서 푸시 인에이블먼트가 설정되어 있지만 iOS 기기만 타겟팅하고 있으므로 해당 사용자는 세그먼트에 속합니다. 세그먼트에는 iOS 기기가 포함됩니다.

{% enddetails %}

{% details Scenario 2: User has two iOS devices with different states %}

**사용자에게 두 대의 iOS 기기가 있습니다:**
- 기기 A: 푸시 옵트인함
- 기기 B: 잠정적으로 인에이블먼트되었지만 옵트인하지 않음

**작동하지 않는 세그먼트 필터:**
- `Push enabled = false` - 기기 A는 푸시에 옵트인되어 있으므로 사용자가 세그먼트에 포함되지 않습니다. 세그먼트에 기기 B가 포함되지 않습니다.
- `Provisionally opted in = true` - 기기 A는 완전히 옵트인되었으므로 임시 상태가 아닙니다. 사용자가 세그먼트에 속하지 않습니다. 세그먼트에 기기 B가 포함되지 않습니다.
- `Push enabled for app > iOS = false` - 기기 A는 iOS에서 푸시하도록 옵트인되어 있으므로 사용자는 세그먼트에 포함되지 않습니다. 세그먼트에 기기 B가 포함되지 않습니다.
- `Push subscription status is not opted in` - 기기 A는 푸시에 옵트인되어 있으므로 사용자가 세그먼트에 포함되지 않습니다. 세그먼트에 기기 B가 포함되지 않습니다.

**결과:** 이러한 푸시 필터를 조합하여 사용하면 적어도 하나의 기기가 제외되는 세그먼트가 생성됩니다.

{% enddetails %}

{% details Scenario 3: User has three or more devices on the same OS %}

**사용자에게 기기가 3개 있습니다:**
- 기기 A: 푸시 옵트인함
- 기기 B: 푸시 옵트인하지 않음
- 기기 C: 푸시 옵트인하지 않음

**작동하지 않는 세그먼트 필터:**
- `Push enabled = false` - 기기 A는 푸시에 옵트인되어 있으므로 사용자가 세그먼트에 포함되지 않습니다. 이 세그먼트에는 기기 B와 C가 포함되지 않습니다.
- `Push enabled for app > X = false` - 기기 A는 지정된 앱을 푸시하도록 옵트인되어 있으므로 사용자가 세그먼트에 포함되지 않습니다. 이 세그먼트에는 기기 B와 C가 포함되지 않습니다.
- `Push subscription status is not opted in` - 기기 A는 푸시에 옵트인되어 있으므로 사용자가 세그먼트에 포함되지 않습니다. 이 세그먼트에는 기기 B와 C가 포함되지 않습니다.

**결과:** 이러한 푸시 필터를 조합하여 사용하면 적어도 하나의 기기가 타겟팅되지 않은 상태로 남습니다.

{% enddetails %}

#### 솔루션: 코드 없는 푸시 프라이머 사용

권장되는 솔루션은 추가 푸시 상태 세분화 필터 없이 코드 없는 푸시 프라이머("푸시 권한 요청" 버튼 동작)를 사용하는 것입니다.

{% alert important %}
**자동 억제**: 코드 없는 푸시 프라이머는 이미 활성화된 푸시 토큰이 있는 기기에서는 자동으로 억제됩니다. 소프트웨어 개발 키트는 특정 기기의 사용자가 이미 푸시 토큰을 가지고 있는지 확인합니다. 사용자가 이미 옵트인한 경우(예: 이전 요청 또는 기기 설정을 통해) 소프트웨어 개발 키트는 추가 세분화 필터 없이도 자동으로 인앱 메시지를 표시하지 않습니다. 사용자가 잠정적으로 푸시 옵트인한 경우를 포함하여 다른 모든 시나리오에서 프라이머가 표시됩니다.
{% endalert %}

코드가 없는 푸시 프라이머를 사용하면 이 기능이 Braze 소프트웨어 개발 키트에서 지원된다는 이점이 있습니다. 소프트웨어 개발 키트는 메시지를 표시하는 특정 기기의 푸시 토큰 상태를 감지할 수 있으므로 여러 기기를 가진 사용자를 제외할 수 있는 프로필 수준의 세분화 필터에 의존할 필요가 없습니다.

#### 고려 사항

**코드 푸시 프라이머가 필요하지 않습니다**: 자동 억제가 작동하려면 코드가 없는 푸시 프라이머를 사용해야 합니다. "푸시 권한 요청" 버튼 액션을 사용하는 대신 커스텀 로직이나 딥링크를 설정하면 소프트웨어 개발 키트에서 푸시 프라이머를 표시하려고 한다는 사실을 식별할 수 없습니다. 이렇게 하면 해당 기기의 구독 상태와 관계없이 메시징이 표시됩니다.

**옵트아웃한 사용자에게는 표시되지** 않습니다: 네이티브 요청 또는 기기 설정 등을 통해 푸시를 명시적으로 옵트아웃한 사용자에게는 인앱 메시지를 표시하지 않고 별도의 육성 캠페인을 통해 해당 사용자를 리타겟팅할 수 있습니다. 이렇게 하려면 코드가 없는 프라이머와 함께 다음 Liquid 로직을 사용하세요:

{% raw %}
```liquid
{% if targeted_device.${foreground_push_enabled} == false %} 
{% abort_message('user turned off push notifications') %} 
{% endif %}
- message goes here -
```
{% endraw %}

`targeted_device` Liquid 필터는 고객 프로필이 아닌 메시지가 표시되고 있는 기기만 확인합니다. 해당 기기에서 `foreground_push_enabled` 는 활성 포그라운드 푸시 토큰이 있는 경우 `true` 로 설정되고 운영 체제에서 푸시 알림이 비활성화되었다고 보고하면 `false` 로 설정됩니다(예: 사용자가 푸시 알림을 명시적으로 끄는 경우). 아직 푸시 권한 상태에 응답하지 않은 완전히 새로운 기기의 경우 `foreground_push_enabled` 은 설정되지 않은 상태이며 아무런 가치가 없습니다. Liquid 상태는 `{% raw %}``false`{% endraw %} 를 구체적으로 확인하기 때문에 명시적으로 옵트아웃한 기기에 대해서만 프라이머를 억제하고, 알 수 없는 상태의 기기는 여전히 자격이 있으며 푸시 프라이머를 받을 수 있습니다.

## 6단계: 전환 이벤트

Braze는 전환에 대한 기본 설정을 제안하지만, 푸시 프라이머를 둘러싼 [전환 이벤트]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/)를 설정할 수도 있습니다.