---
nav_title: "알림 옵션"
article_title: iOS 알림 옵션
page_order: 2
page_layout: reference
description: "이 참고 문서에서는 중요 알림, 조용한 알림, 임시 푸시 알림 등과 같은 iOS 알림 옵션에 대해 설명합니다."

platform: iOS
channel:
  - push

---

# 알림 옵션

> Apple의 iOS 12가 출시됨에 따라 Braze는 [알림 그룹](#notification-groups), [조용한 알림/잠정 승인](#provisional-push-authentication--quiet-notifications), [중요 알림](#critical-alerts) 등 여러 기능을 지원합니다.

## 알림 그룹

메시지를 분류하여 사용자의 알림 트레이에 그룹화하려면 Braze를 통해 iOS의 알림 그룹 기능을 활용할 수 있습니다.

Create your iOS push campaign, then to to the **Settings** tab and open the **Notification group** dropdown.

![The "Settings" tab with a "Notification group" dropdown that selected a value of "Coupons".]({% image_buster /assets/img_archive/notification_group_dropdown.png %}){: style="max-width:50%;" }

드롭다운에서 알림 그룹을 선택합니다. 알림 그룹 설정이 잘못되었거나 드롭다운에서 **없음**을 선택하면 워크스페이스에 정의된 모든 사용자에게 정상적으로 메시지가 자동으로 전송됩니다.

여기에 나열된 알림 그룹이 없는 경우 iOS 스레드 ID를 사용하여 알림 그룹을 추가할 수 있습니다. 추가하려는 모든 알림 그룹에 대해 하나의 iOS 스레드 ID가 필요합니다. 그런 다음 드롭다운에서 **알림 그룹 관리를** 클릭하고 표시되는 **iOS 푸시 알림 그룹 관리** 창에서 필수 입력란을 작성하여 알림 그룹에 추가합니다.

![Window to manage iOS push notification groups.]({% image_buster /assets/img_archive/managenotgroups.png %}){: style="max-width:70%;" }

iOS 푸시 캠페인을 만든 다음 작성기 상단을 확인합니다. **알림 그룹**이라는 레이블이 붙은 드롭다운이 표시됩니다.

### 요약 인수

스레드 ID별로 알림을 그룹화하는 것 외에도 Apple에서는 알림이 그룹화될 때 표시되는 요약을 편집할 수 있습니다. Braze 사용자는 도구를 사용하여 푸시 캠페인을 작성할 때 요약 카테고리, 요약 횟수, 요약 인수를 지정할 수 있습니다.

{% alert tip %}
동일한 스레드 ID를 가진 알림이 알림 트레이에 그룹화되는 방식은 OS의 제어하에 있습니다. iOS는 최적이라고 판단되는 경우에 따라 동일한 스레드 ID를 가진 알림을 개별적으로 또는 그룹으로 표시하도록 선택할 수 있습니다.
{% endalert %}

**푸시 작성기에서** **알림 옵션** 상자를 선택합니다.

그런 다음 `summary-arg` 및 `summary-arg-count` 을 키로 선택하고 해당 열에 해당 값을 입력합니다. `summary-arg`에 값을 설정하지 않으면 기본값은 1이 됩니다.

### 요약 카테고리

요약 카테고리를 사용하면 알림이 그룹화될 때 표시되는 전체 요약을 사용자 지정할 수 있습니다. 여러 카테고리를 생성하고 적용할 수 있습니다.

메시지에서 카테고리를 사용하려면 개발자와 협력하여 다음 예제를 사용하여 구현하세요:

```
UNNotificationCategory *newsCategory = [UNNotificationCategory categoryWithIdentifier:@"news"
                                                      actions:@[likeAction, unlikeAction]
                                                      intentIdentifiers:@[]
                                                      hiddenPreviewsBodyPlaceholder:@""
                                                      categorySummaryFormat:@"%u more news articles from %@"
                                                       Options:0];
```

{% alert important %}
이 경우 SDK 업데이트가 필요하지 않습니다.
{% endalert %}

{% alert tip %}
`%u` 및 `%@`은 각각 요약 개수 및 요약 인수의 서식 지정 문자열입니다. 요약이 표시되면 이러한 입력 안내는 `summary-count` 및 `summary-arg`의 값으로 대체됩니다 .
{% endalert %}

앱에서 설정이 완료되면 **알림 버튼** 상자를 선택하고 **미리 등록된 iOS 카테고리 입력을** 선택하여 요약 카테고리를 사용합니다.

그런 다음 앱에서 설정한 요약 카테고리 식별자를 입력합니다.

### 임시 푸시 인증 및 조용한 알림 {#provisional-push}

Apple은 브랜드가 공식적으로 명시적으로 옵트인하기 전에 사용자의 알림 센터에 조용한 푸시 알림을 보낼 수 있는 옵션을 제공하여 메시지의 가치를 조기에 입증할 수 있는 기회를 제공합니다. 앱에서 [임시 푸시 알림을 설정하기만](#set-up-provisional-push-notifications) 하면 임시 푸시 토큰이 있는 모든 사용자가 메시지를 받게 됩니다.

기존 iOS 푸시 토큰과 달리 임시 푸시 토큰은 브랜드가 신규 사용자가 Apple의 기본 푸시 옵트인 안내를 보고 클릭하기 전에 도달할 수 있는 "체험판" 역할을 합니다. 이 기능을 사용하면 푸시 알림이 새 사용자의 알림 트레이로 바로 전달되며, 향후 알림을 '유지' 또는 '끄기'할 수 있는 옵션이 제공됩니다. 사용자는 '옵트인' 여정을 경험하는 대신 '옵트아웃' 여정에 더 가까운 경험을 하게 됩니다.

{% alert tip %}
임시 인증은 옵트인 비율을 크게 높일 수 있는 잠재력이 있지만, 사용자가 메시지에서 가치를 발견할 경우에만 가능합니다. [사용자 세분화]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/), [위치 타겟팅]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/) 및 [개인화]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) 기능을 사용하여 적절한 사용자가 적시에 '체험판' 알림을 받을 수 있도록 하세요. 그러면 푸시 알림이 사용자의 앱 사용 경험에 가치를 더한다는 사실을 알고 사용자가 푸시 알림을 완전히 옵트인하도록 유도할 수 있습니다.
{% endalert %}

사용자가 어떤 옵션을 선택하든 고객 프로필의 **인게이지먼트** 탭 아래에 있는 [연락처 설정]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab)에 적절한 토큰 또는 [구독 상태]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/)가 추가됩니다.

![Contact settings with a push subscribed status.]({% image_buster /assets/img/profile-push-prov-auth.png %}){: width="50%"}

[세분화 필터]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/)를 사용하여 잠정 승인 여부에 따라 사용자를 타겟팅할 수 있습니다.

![세그먼트 세부 정보 패널에 샘플 세그먼트 필터 "iOS 스톱워치(iOS)에서 잠정적으로 승인됨"을 적용하여 타겟 사용자를 대상으로 합니다.]({% image_buster /assets/img/segment-push-prov-auth.png %})

{% alert tip %}
사용자가 임시 푸시를 "끄기"로 선택하면 더 이상 임시 푸시 메시지가 표시되지 않습니다. 이 기능을 사용하여 보내는 메시지 내용과 문장에 신중을 기하세요!
{% endalert %}

{% alert important %}
추가 푸시 프롬프트 또는 [인앱 푸시 프라이머](https://www.braze.com/resources/glossary/priming-for-push/) (사용자가 푸시 알림을 수신하도록 유도하는 인앱 메시지)를 사용하는 경우, Braze 담당자에게 문의하여 추가 안내를 받으시기 바랍니다.
{% endalert %}

#### 임시 푸시 알림 설정

Braze를 사용하면 다음 스니펫을 예로 들어 Braze iOS SDK 구현 내에서 토큰 등록 스니펫의 코드를 업데이트하여 임시 인증을 등록할 수 있습니다(이를 개발자에게 보내거나 [통합 프로세스 중에 임시 푸시 인증을 구현하도록]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#using-usernotification-framework-ios-10) 하세요).

{% alert warning %}
임시 푸시 인증 구현은 iOS 12 이상만 지원하며 배포 대상이 그 이전인 경우 오류가 발생합니다. 이에 대한 자세한 내용은 [여기에서 자세한 구현 설명서]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#using-usernotification-framework-ios-10)를 참조하세요.
{% endalert %}

{% tabs local %}
  {% tab Swift %}
**Swift**

```
var options: UNAuthorizationOptions = [.alert, .sound, .badge]
if #available(iOS 12.0, *) {
  options = UNAuthorizationOptions(rawValue: options.rawValue | UNAuthorizationOptions.provisional.rawValue)
}
```
  {% endtab %}
  {% tab Objective-C %}

**Objective-C**

```
UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
center.delegate = self;
UNAuthorizationOptions options = UNAuthorizationOptionAlert | UNAuthorizationOptionSound | UNAuthorizationOptionBadge;
if (@available(iOS 12.0, *)) {
    options = options | UNAuthorizationOptionProvisional;
}
```
  {% endtab %}
{% endtabs %}

### 중단 수준(iOS 15+) {#interruption-level}

iOS 15의 새로운 집중 모드를 통해 사용자는 앱 알림이 소리나 진동으로 "방해"할 수 있는 시기를 더 잘 제어할 수 있습니다.

![iOS Notification Settings page that shows notifications enabled for immediate delivery and with time sensitive notifications enabled.]({% image_buster /assets/img/ios/ios15-notification-settings.png %}){: style="max-width:40%"}

이제 앱에서 알림의 긴급성에 따라 알림에 포함할 중단 수준을 지정할 수 있습니다.

iOS 푸시 알림의 중단 수준을 변경하려면 **설정** 탭을 선택하고 **중단 수준** 드롭다운 메뉴에서 원하는 수준을 선택합니다.

![Dropdown for selecting the interruption level.]({% image_buster /assets/img/ios/interruption_level.png %}){: style="max-width:50%"}

이 기능은 최소 SDK 버전 요구 사항이 없으며 iOS 15 이상을 실행하는 기기에만 적용됩니다.

사용자는 궁극적으로 자신의 집중력을 제어할 수 있으며, 시간 민감 알림이 전달되더라도 집중력을 방해할 수 없는 앱을 지정할 수 있다는 점을 명심하세요.

중단 수준과 그 설명은 다음 표를 참조하세요.

|방해 수준|설명|사용 시기|브레이크 스루 포커스 모드|
|--|--|--|--|
|[수동적](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/passive)|소리, 진동 또는 화면 켜기 없이 알림을 보냅니다.|즉각적인 주의가 필요하지 않은 알림입니다.|아니요|
|[활성](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/active) (기본값)|사용자가 포커스 모드에 있지 않은 경우에만 소리와 진동을 내고 화면을 켭니다.|사용자가 포커스 모드를 활성화하지 않은 경우 즉각적인 주의가 필요한 알림입니다.|아니요|
|[시간 민감형](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/timesensitive)|포커스 모드에 있는 동안에도 소리가 나고 진동이 울리며 화면이 켜집니다. 이를 위해서는 Xcode에서 앱에 **시간 민감형 알림**을 추가해야 합니다.|차량 공유 또는 배달 알림과 같이 Focus 모드와 관계없이 사용자에게 방해가 될 수 있는 시기 적절한 알림을 제공합니다.|예|
|[중요](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/critical)|휴대폰의 **방해 금지** 스위치가 활성화되어 있어도 소리가 나고 진동이 울리며 화면이 켜집니다. 이를 위해서는 [Apple의 명시적인 승인이 필요합니다](https://developer.apple.com/contact/request/notifications-critical-alerts-entitlement/).|악천후 또는 안전 경보와 같은 긴급 상황|예|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### 관련성 점수(iOS 15+) {#relevance-score}

![세 개의 알림이 포함된 '저녁 요약'이라는 제목의 iOS용 알림 요약.]({% image_buster /assets/img/ios/ios15-notification-summary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

iOS 15는 또한 사용자가 하루 중 지정된 시간에 여러 알림을 선택적으로 그룹화하여 다이제스트하도록 예약할 수 있는 새로운 방법을 도입했습니다. 이는 즉각적인 주의가 필요하지 않은 알림으로 인해 하루 종일 알림이 계속 중단되는 것을 방지하기 위한 것입니다.

앱은 **관련성 점수**를 설정하여 가장 관련성이 높은 푸시 알림을 지정할 수 있습니다. Apple은 이 점수를 사용하여 예약된 알림 요약에 어떤 알림을 표시할지, 다른 알림은 사용자가 요약을 클릭하면 사용할 수 있도록 할지를 결정합니다. 

모든 알림은 사용자의 알림 센터에서 계속 액세스할 수 있습니다.

iOS 알림의 관련성 점수를 설정하려면 **설정** 탭에서 `0.0` ~ `1.0` 사이의 값을 입력합니다. 예를 들어 가장 중요한 메시지는 `1.0`으로 보내고, 중간 정도의 중요도는 `0.5`로 보내면 됩니다.

![Relevance score of "0.5".]({% image_buster /assets/img/ios/relevance-score.png %}){: style="max-width:80%;"}

이 기능은 최소 SDK 버전 요구 사항이 없으며 iOS 15 이상을 실행하는 기기에만 적용됩니다.

다양한 메시지 유형별 최대 메시지 길이에 대한 자세한 내용은 다음 리소스를 참조하세요.

- [이미지 및 텍스트 사양]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#image-and-text-specifications)
- [iOS 문자 수 가이드라인]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/#character-count)

