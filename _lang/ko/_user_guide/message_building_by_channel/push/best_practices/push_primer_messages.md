---
nav_title: 푸시 프라이머 인앱 메시지 보내기
article_title: 푸시 프라이머 인앱 메시지 보내기
page_order: 1
page_type: reference
description: "이 문서에서는 푸시 프라이머 인앱 메시지의 전제 조건과 설정 방법에 대해 설명합니다."
channel: push

---

# 푸시 프라이머 인앱 메시지 보내기

스트리밍 앱용 푸시 프라이머 인앱 메시지. 알림에는 "Movie Cannon에서 푸시 알림을 받으시겠습니까? 알림에는 새 영화, TV 프로그램 또는 기타 알림이 포함될 수 있으며 언제든지 해제할 수 있습니다."]({% image_buster /assets/img_archive/push_primer_iam.png %}){: style="float:right;max-width:40%;margin-left:15px;border:none;"}

> 사용자에게 푸시 권한을 요청할 수 있는 기회는 한 번뿐이므로 푸시 등록을 최적화하여 푸시 메시지의 도달 범위를 극대화하는 것이 중요합니다. 이를 위해 인앱 메시지를 사용하여 사용자에게 기본 푸시 안내 메시지를 표시하기 전에 옵트인을 선택하면 어떤 유형의 메시지를 받을 수 있는지 설명할 수 있습니다. 이를 푸시 프라이머라고 합니다.

Braze에서 푸시 프라이머 인앱 메시지를 만들려면 iOS, Android 또는 웹용 인앱 메시지를 만들 때 '푸시 권한 요청' 버튼 클릭 동작을 사용하면 됩니다.

## 전제 조건

이 기능을 사용하려면 다음 최소 버전 이상에서 지원되는 [버튼 클릭 동작이](#button-actions) 필요합니다:

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

또한 다음 플랫폼별 세부 정보를 참고하세요:

{% tabs local %}
{% tab android %}
|OS 버전|추가 정보|
\|----------|----------------------|
| **Android 12 및 이전** 버전 | 푸시는 기본값으로 옵트인되어 있으므로 푸시 프라이머를 구현하는 것은 권장되지 않습니다. |
| **Android 13+** | 사용자가 푸시 권한 프롬프트를 두 번 거부하면 Android는 Braze 푸시 프라이머 메시지를 포함한 추가 프롬프트를 차단합니다. 이 후 권한을 부여하려면 사용자가 기기 설정에서 앱에 푸시를 수동으로 인에이블먼트해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}

{% tab swift %}
### 일반 정보

- 푸시 프롬프트는 운영 체제에 따라 설치당 한 번만 표시될 수 있습니다.
- 앱의 푸시 설정이 명시적으로 켜져 있거나 꺼져 있는 경우에는 메시지가 표시되지 않으며, [임시 권한이](https://developer.apple.com/documentation/usernotifications/asking_permission_to_use_notifications#3544375) 있는 사용자에게만 메시지가 표시됩니다.
  - **앱의 푸시 설정이 켜져 있습니다:** 사용자가 이미 옵트인했으므로 Braze는 인앱 메시지를 표시하지 않습니다.
  - **앱의 푸시 설정이 꺼져 있습니다:** 기기 설정에서 사용자를 앱의 푸시 알림 설정으로 리디렉션해야 합니다.

### 수동 코드 제거

이 튜토리얼을 사용하여 설정한 인앱 메시지는 사용자가 인앱 메시지 버튼을 클릭할 때 자동으로 네이티브 푸시 프롬프트 코드를 호출합니다. 푸시 알림 권한을 두 번 요청하거나 잘못된 시간에 요청하는 것을 방지하려면 개발자가 구현한 기존 푸시 알림 통합을 수정하여 인앱 메시지가 사용자에게 가장 먼저 표시되는 푸시 알림 프라이머가 되도록 해야 합니다.

개발팀은 앱 또는 사이트에 대한 푸시 알림 구현을 검토하고 푸시 권한을 요청하는 코드를 수동으로 제거해야 합니다. 예를 들어 다음 코드에 대한 참조를 제거할 수 있습니다:

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

먼저 [인앱 메시지를 만든]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/) 다음 메시지 유형과 레이아웃을 선택합니다.

메시지와 버튼 모두에 충분한 공간을 확보하려면 전체 화면 또는 모달 메시지 레이아웃을 사용하세요. 전체 화면을 선택하는 경우 이미지가 필요하다는 점에 유의하세요.

## 2단계: 메시지 구축하기

이제 사본을 추가할 차례입니다! 푸시 프라이머는 사용자가 푸시 알림을 켜도록 준비시키는 역할을 한다는 점을 기억하세요. 메시지 본문에는 사용자가 푸시 알림을 사용 설정해야 하는 이유를 강조하는 것이 좋습니다. 어떤 유형의 알림을 보낼지, 어떤 가치를 제공할 수 있을지 구체적으로 정하세요.

예를 들어 뉴스 앱은 다음과 같은 푸시 프라이머를 사용할 수 있습니다:

```plaintext
Breaking news on the go! Enable push notifications to get alerts for major stories and topics that matter to you.
```

스트리밍 앱은 다음을 사용할 수 있습니다:

```plaintext
Get push notifications from Movie Cannon? Notifications may include new movies, TV shows, or other notices and can be turned off at any time.
```

모범 사례 및 추가 리소스는 [커스텀 옵트인 안내 메시지 만들기를]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) 참조하세요.

## 3단계: 버튼 동작 지정 {#button-actions}

인앱 메시지에 버튼을 추가하려면 두 개의 **버튼** 블록을 메시지로 드래그하면 인앱 메시지의 기본 및 보조 버튼 역할을 하는 버튼이 추가됩니다. 행을 메시지로 드래그한 다음 버튼을 행으로 드래그하여 버튼이 서로 겹치지 않고 같은 가로 행에 위치하도록 할 수도 있습니다. 시작 버튼으로 '알림 허용' 및 '지금은 안 함'을 권장하지만, 다양한 버튼 프롬프트를 지정할 수 있습니다.

버튼 복사본을 추가한 후 각 버튼의 클릭 시 동작을 지정합니다:

- **버튼 1:** 이를 "메시지 닫기"로 설정합니다. 이 버튼은 보조 버튼 또는 '지금 안 함' 옵션입니다.
- **버튼 2:** 이를 '푸시 권한 요청'으로 설정합니다. 이 버튼은 기본 버튼 또는 '알림 허용' 옵션입니다.

버튼이 두 개 있는 인앱 메시지 작성기: "알림 허용" 및 "지금은 안함"을 선택합니다.]({% image_buster /assets/img_archive/push_primer_button_behavior.png %})

## 4단계: 전달 예약

푸시 프라이머가 적절한 시간에 전송되도록 설정하려면 인앱 메시지를 액션 기반 메시지로 예약하고 **커스텀 이벤트 수행을** 트리거 동작으로 설정해야 합니다.

이상적인 시기는 다양하지만, Braze는 사용자가 앱이나 사이트에서 가치를 느끼기 시작했거나 푸시 알림으로 해결할 수 있는 강력한 요구가 있을 때(예: 주문 후 배송 추적 정보를 제공하려는 경우) 사용자가 어떤 종류의 [가치 높은 작업을](https://www.braze.com/resources/videos/mapping-high-value-actions) 완료할 때까지 기다릴 것을 제안합니다. 이렇게 하면 프롬프트가 브랜드에만 도움이 되는 것이 아니라 고객에게도 도움이 됩니다.

!"관심 목록에 추가"라는 커스텀 이벤트를 수행한 사용자에게 보낼 실행 기반 전달 설정입니다.]({% image_buster /assets/img_archive/push_primer_trigger.png %})

## 5단계: 타겟팅 사용자

푸시 프라이머 캠페인의 목표는 아직 푸시 권한을 부여하지 않은 모든 기기의 사용자에게 푸시 권한을 부여하라는 메시지를 표시하는 것입니다. 여기에는 처음 사용하는 사용자나 새 기기를 구입하거나 애플리케이션을 다시 설치하는 기존 사용자가 포함될 수 있습니다. 푸시 프라이머 캠페인을 올바르게 타겟팅하려면 `Foreground Push Enabled For App is false` 에 필터를 추가하세요. 이 필터는 포그라운드 푸시 알림에 아직 옵트인하지 않은 개별 앱 설치를 식별합니다.

{% alert important %}
`Push Subscription Status is not Opted In` 같은 사용자 수준 필터를 사용하면 다른 기기에서 이미 옵트인한 사용자가 제외되어 새 기기에서 안내 메시지를 받지 못합니다.
{% endalert %}

그 외에도 가장 적절하다고 생각되는 추가 세그먼트를 결정할 수 있습니다. 예를 들어 두 번째 구매를 완료한 사용자, 방금 계정을 만들어 회원으로 가입한 사용자 또는 일주일에 두 번 이상 앱을 방문하는 사용자를 타겟팅할 수 있습니다. 이러한 중요한 세그먼트에 대해 사용자를 타겟팅하면 사용자가 옵트인하고 푸시 인에이블먼트가 될 확률이 높아집니다.

## 6단계: 전환 이벤트

Braze는 전환에 대한 기본값 설정을 제안하지만 푸시 프라이머를 둘러싼 [전환 이벤트를]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) 설정할 수 있습니다.

