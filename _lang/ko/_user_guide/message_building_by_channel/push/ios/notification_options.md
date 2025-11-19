---
nav_title: "알림 옵션"
article_title: iOS 알림 옵션
page_order: 2
page_layout: reference
description: "이 참조 문서에서는 중요한 알림, 조용한 알림, 임시 푸시 알림 등과 같은 iOS 알림 옵션을 다룹니다."

platform: iOS
channel:
  - push

---

# 알림 옵션

> Apple의 iOS 12 출시와 함께 Braze는 [알림 그룹](#notification-groups), [조용한 알림/임시 승인](#provisional-push-authentication--quiet-notifications), [중요 알림](#critical-alerts) 등 여러 기능을 지원합니다.

## 알림 그룹

메시지를 분류하고 사용자의 알림 트레이에 그룹화하려면 Braze를 통해 iOS의 알림 그룹 기능을 활용할 수 있습니다.

iOS 푸시 캠페인을 생성한 후 **설정** 탭으로 이동하여 **알림 그룹** 드롭다운을 엽니다.

\!["설정" 탭과 "알림 그룹" 드롭다운이 있으며, "쿠폰" 값을 선택했습니다.]({% image_buster /assets/img_archive/notification_group_dropdown.png %}){: style="max-width:50%;" }

드롭다운에서 알림 그룹을 선택하세요. 알림 그룹 설정이 잘못되었거나 드롭다운에서 **없음**을 선택하면 메시지는 자동으로 모든 정의된 사용자에게 정상적으로 전송됩니다.

여기에 나열된 알림 그룹이 없으면 iOS 스레드 ID를 사용하여 하나를 추가할 수 있습니다. 추가하려는 각 알림 그룹에 대해 하나의 iOS 스레드 ID가 필요합니다. 그런 다음 드롭다운에서 **알림 그룹 관리**를 클릭하고 나타나는 **iOS 푸시 알림 그룹 관리** 창에서 필수 필드를 작성하여 알림 그룹에 추가합니다.

\![iOS 푸시 알림 그룹을 관리하는 창.]({% image_buster /assets/img_archive/managenotgroups.png %}){: style="max-width:70%;" }

iOS 푸시 캠페인을 생성한 후 작성기 상단을 확인하세요. 거기에서 **알림 그룹**이라는 레이블이 붙은 드롭다운을 볼 수 있습니다.

### 요약 인수

Apple은 스레드 ID로 알림을 그룹화하는 것 외에도 알림이 그룹화될 때 나타나는 요약을 편집할 수 있도록 허용합니다. Braze 사용자는 도구를 사용하여 푸시 캠페인을 작성할 때 요약 카테고리, 요약 수 및 요약 인수를 지정할 수 있습니다.

{% alert tip %}
알림이 동일한 스레드 ID로 그룹화되는 방식은 OS의 제어를 받습니다. iOS는 최적이라고 판단되는 방식에 따라 동일한 스레드 ID를 가진 알림을 개별적으로 또는 그룹으로 표시할 수 있습니다.
{% endalert %}

**알림 옵션** 상자를 **푸시 작성기**에서 체크하세요.

그런 다음 `summary-arg`과 `summary-arg-count`를 키로 선택하고 해당 값을 해당 열에 입력하세요. `summary-arg`에 대한 값을 설정하지 않으면 기본값은 1이 됩니다.

### 요약 카테고리

요약 카테고리를 사용하면 알림이 그룹화될 때 나타나는 전체 요약을 사용자 정의할 수 있습니다. 여러 카테고리를 생성하고 적용할 수 있습니다.

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
이것은 SDK 업데이트를 필요로 하지 않습니다.
{% endalert %}

{% alert tip %}
`%u`와 `%@`은 각각 요약 카운트와 요약 인수에 대한 형식 문자열입니다. 요약이 표시될 때 이러한 자리 표시자는 `summary-count`와 `summary-arg`의 값으로 대체됩니다.
{% endalert %}

앱에서 이 설정이 완료되면 **알림 버튼** 상자를 체크하고 **사전 등록된 iOS 카테고리 입력**를 선택하여 요약 카테고리를 사용하세요.

그런 다음 앱에서 설정한 요약 카테고리 식별자를 입력하세요.

### 임시 푸시 인증 및 조용한 알림 {#provisional-push}

Apple은 브랜드가 공식적으로 명시적으로 옵트인하기 전에 사용자들의 알림 센터에 조용한 푸시 알림을 보낼 수 있는 옵션을 허용하여 메시지의 가치를 조기에 보여줄 수 있는 기회를 제공합니다. 앱에서 [임시 푸시 알림 설정](#set-up-provisional-push-notifications)만 하면, 임시 푸시 토큰을 가진 모든 사용자가 귀하의 메시지를 받을 수 있습니다.

전통적인 iOS 푸시 토큰과 달리, 임시 푸시 토큰은 브랜드가 Apple의 기본 푸시 옵트인 프롬프트를 보기 전에 새로운 사용자에게 다가갈 수 있도록 하는 "시험 패스" 역할을 합니다. 이 기능을 사용하면 푸시 알림이 새로운 사용자의 알림 트레이에 직접 전달되며, 향후 알림을 "유지"하거나 "끄기" 옵션이 제공됩니다. "옵트인" 여정을 경험하는 대신, 사용자들은 "옵트아웃" 여정에 더 가까운 것을 경험하게 될 것입니다.

{% alert tip %}
임시 인증은 귀하의 옵트인 비율을 극적으로 증가시킬 잠재력이 있지만, 사용자가 귀하의 메시지에서 가치를 느낄 때만 가능합니다. 적절한 사용자들이 이러한 "시험" 알림을 적시에 받을 수 있도록 [사용자 세분화]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/), [위치 타겟팅]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/), 및 [개인화]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) 기능을 반드시 사용하세요. 그런 다음, 사용자가 귀하의 푸시 알림에 완전히 옵트인하도록 유도할 수 있으며, 이는 사용자에게 귀하의 앱에서 가치를 더합니다.
{% endalert %}

사용자가 선택한 옵션에 따라 적절한 토큰 또는 [구독 상태]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/)가 사용자 프로필의 [연락처 설정]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab)의 **참여** 탭에 추가됩니다.

\![푸시 구독 상태가 있는 연락처 설정.]({% image_buster /assets/img/profile-push-prov-auth.png %}){: width="50%"}

사용자가 임시 인증을 받았는지 여부에 따라 사용자를 타겟팅할 수 있으며, 이를 위해 [세분화 필터]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/)를 사용합니다.

\![샘플 세그먼트 필터 "iOS 스톱워치에서 임시 인증이 true인 사용자 타겟팅"이 있는 세그먼트 세부정보 패널.]({% image_buster /assets/img/segment-push-prov-auth.png %})

{% alert tip %}
사용자가 귀하의 임시 푸시를 "끄기"로 선택하면, 더 이상 귀하로부터 임시 푸시 메시지를 보지 않게 됩니다. 이 기능을 사용하여 전송되는 메시지 내용과 주기에 대해 신중하게 생각하세요!
{% endalert %}

{% alert important %}
추가 푸시 프롬프트 또는 [앱 내 푸시 프라이머](https://www.braze.com/resources/glossary/priming-for-push/) (사용자가 푸시 알림에 옵트인하도록 유도하는 앱 내 메시지)를 사용하는 경우, 추가 지침을 위해 Braze 담당자에게 문의하세요.
{% endalert %}

#### 임시 푸시 알림 설정하기

Braze는 귀하의 Braze iOS SDK 구현 내 토큰 등록 스니펫에서 코드를 업데이트하여 임시 인증에 등록할 수 있도록 하며, 다음 스니펫을 예로 사용하여 개발자에게 전달하거나 [통합 과정에서 임시 푸시 인증을 구현하도록 하세요]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#using-usernotification-framework-ios-10).

{% alert warning %}
임시 푸시 인증의 구현은 iOS 12+만 지원하며, 배포 대상이 그 이전일 경우 오류가 발생합니다. 자세한 구현 문서에서 이 [자세히 알아보세요]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#using-usernotification-framework-ios-10).
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

### 중단 수준 (iOS 15+) {#interruption-level}

iOS 15의 새로운 집중 모드 덕분에 사용자는 앱 알림이 소리나 진동으로 "방해"할 수 있는 시점을 더 잘 제어할 수 있습니다.

\![즉시 전달 및 시간 민감 알림이 활성화된 알림이 표시된 iOS 알림 설정 페이지.]({% image_buster /assets/img/ios/ios15-notification-settings.png %}){: style="max-width:40%"}

앱은 이제 알림의 긴급성에 따라 알림이 포함해야 할 방해 수준을 지정할 수 있습니다.

iOS 푸시 알림의 방해 수준을 변경하려면 **설정** 탭을 선택하고 **방해 수준** 드롭다운 메뉴에서 원하는 수준을 선택하십시오.

\![방해 수준을 선택하기 위한 드롭다운.]({% image_buster /assets/img/ios/interruption_level.png %}){: style="max-width:50%"}

이 기능은 최소 SDK 버전 요구 사항이 없지만 iOS 15 이상을 실행하는 장치에만 적용됩니다.

사용자가 궁극적으로 집중을 제어한다는 점을 명심하십시오. 시간 민감 알림이 전달되더라도 어떤 앱이 집중을 방해할 수 없는지 지정할 수 있습니다.

방해 수준 및 설명에 대한 다음 표를 참조하십시오.

|방해 수준|설명|사용 시기|집중 모드에서 방해하기|
|--|--|--|--|
|[수동](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/passive)|소리, 진동 또는 화면을 켜지 않고 알림을 보냅니다.|즉각적인 주의가 필요하지 않은 알림입니다.|아니요|
|[활성](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/active) (기본값)|사용자가 집중 모드에 있지 않은 경우에만 소리, 진동 및 화면을 켭니다.|사용자가 집중 모드를 활성화하지 않는 한 즉각적인 주의가 필요한 알림입니다.|아니요|
|[시간 민감](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/timesensitive)|소리가 나고 진동하며 포커스 모드에서도 화면이 켜집니다. 이것은 **시간 민감 알림 기능**이 Xcode에서 앱에 추가되어야 합니다.|사용자의 포커스 모드와 관계없이 방해해야 하는 적시 알림, 예를 들어 차량 공유 또는 배달 알림입니다.|예|
|[중요](https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel/critical)|전화의 **방해 금지** 스위치가 활성화되어 있어도 소리가 나고 진동하며 화면이 켜집니다. 이 [애플의 명시적 승인이 필요합니다](https://developer.apple.com/contact/request/notifications-critical-alerts-entitlement/).|심각한 날씨나 안전 경고와 같은 비상 상황|예|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### 관련성 점수 (iOS 15+) {#relevance-score}

\!["당신의 저녁 요약"이라는 제목의 iOS 알림 요약으로 세 개의 알림이 포함되어 있습니다.]({% image_buster /assets/img/ios/ios15-notification-summary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

iOS 15는 사용자가 하루 중 지정된 시간에 여러 알림을 그룹화하여 선택적으로 예약할 수 있는 새로운 방법을 도입합니다. 이는 즉각적인 주의가 필요하지 않은 알림으로 인해 하루 종일 지속적인 방해를 방지하기 위해 수행됩니다.

앱은 **관련성 점수**를 설정하여 가장 관련성이 높은 푸시 알림을 지정할 수 있습니다. 애플은 이 점수를 사용하여 예약된 알림 요약에서 어떤 알림을 보여줄지 결정하고, 다른 알림은 사용자가 요약을 클릭할 때 사용할 수 있도록 합니다. 

모든 알림은 여전히 사용자의 알림 센터에서 접근할 수 있습니다.

iOS 알림의 관련성 점수를 설정하려면 **설정** 탭 내에서 `0.0`과 `1.0` 사이의 값을 입력하세요. 예를 들어, 가장 중요한 메시지는 `1.0`로 전송해야 하며, 중간 중요도의 메시지는 `0.5`로 전송할 수 있습니다.

\!["0.5"의 관련성 점수.]({% image_buster /assets/img/ios/relevance-score.png %}){: style="max-width:80%;"}

이 기능은 최소 SDK 버전 요구 사항이 없지만 iOS 15 이상을 실행하는 장치에만 적용됩니다.

다양한 메시지 유형에 대한 최대 메시지 길이에 대한 자세한 정보는 다음 리소스를 참조하세요:

- [이미지 및 텍스트 사양]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#image-and-text-specifications)
- [iOS 문자 수 가이드라인]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/#character-count)

