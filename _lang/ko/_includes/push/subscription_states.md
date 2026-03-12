## 푸시 구독 상태 {#push-sub-states}

Braze의 '푸시 구독 상태'는 푸시 알림 수신에 대한 **사용자의** 글로벌 선호도를 식별합니다. 구독 상태는 사용자 기반이므로 개별 앱에 한정되지 않습니다. 구독 상태는 푸시 알림을 타겟팅할 사용자를 결정할 때 유용한 플래그가 됩니다.

{% alert note %}
사용자의 푸시 구독 상태는 사용자의 모든 디바이스를 포함한 전체 사용자 프로필에 적용됩니다.
{% endalert %}

다음 구독 상태 옵션이 있습니다: `Subscribed`, `Opted-In`, 및 `Unsubscribed`.

기본적으로 사용자가 푸시를 통해 메시지를 받으려면 푸시 구독 상태가 `Subscribed` 또는 `Opted-In`이어야 하며, 포그라운드 푸시가 활성화되어 있어야 합니다. 메시지를 작성할 때 필요한 경우 이 설정을 재정의할 수 있습니다.

|옵트인 상태|설명|
|---|---|
|`Subscribed`| Braze에서 사용자 프로필을 생성할 때의 기본 푸시 구독 상태입니다. |
|`Opted-In`| 사용자가 푸시 알림 수신을 명시적으로 선호한다고 밝혔습니다. Braze는 사용자가 OS 수준의 푸시 프롬프트를 수락하면 사용자의 옵트인 상태를 자동으로 `Opted-In`로 이동합니다.<br><br>Android 12 이하 사용자에게는 적용되지 않습니다.|
|`Unsubscribed`| 사용자가 애플리케이션 또는 브랜드가 제공하는 기타 방법을 통해 푸시 수신을 명시적으로 취소한 경우. 기본적으로 Braze 푸시 캠페인은 푸시에 대해 `Subscribed` 또는 `Opted-in`인 사용자만을 대상으로 합니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Braze는 사용자의 푸시 구독 상태를 `Unsubscribed` 로 자동 변경하지 않습니다. 사용자의 푸시 구독 상태가 `Unsubscribed`인 경우 사용자의 `Foreground Push Enabled` 세분화 필터는 `false`임을 기억하세요.
{% endalert %}

### 푸시 구독 상태 업데이트하기 {#update-push-subscription-state}

사용자의 푸시 구독 상태를 업데이트하는 다음 방법을 검토하세요:

#### 자동 옵트인(기본값)

기본적으로 Braze는 사용자가 앱에 대한 푸시 알림을 처음 승인할 때 사용자의 푸시 구독 상태를 `Opted-In`으로 설정합니다. 또한 사용자가 이전에 푸시 권한을 비활성화했다가 시스템 설정에서 다시 활성화하는 경우에도 Braze는 이 작업을 수행합니다.

{% tabs local %}
{% tab android %}
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

![푸시 구독 상태가 구독됨으로 설정된 신원 미상의 고객 프로필입니다.]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Braze를 사용하여 사용자의 푸시 구독 상태를 확인할 수 있는 방법은 다음과 같습니다:

* **사용자 프로필:** You can access individual user profiles through the Braze dashboard on the **[User Search]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/)** page. 이메일 주소, 전화번호 또는 외부 사용자 ID를 통해 사용자의 프로필을 찾은 후 **참여** 탭을 선택하여 사용자의 가입 상태를 확인하고 수동으로 조정할 수 있습니다.
* **REST API 내보내기:** You can export individual user profiles in JSON format using the export [Users by segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) or [Users by identifier]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) endpoints. Braze는 각 기기에 대한 푸시 활성화 정보를 포함하는 푸시 토큰 객체를 반환합니다.