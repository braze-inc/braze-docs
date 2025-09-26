---
nav_title: "고급 푸시 캠페인 설정"
article_title: 고급 푸시 캠페인 설정
page_order: 5
page_layout: reference
description: "이 참조 문서에서는 우선 순위, 커스텀 URL, 전달 옵션 등과 같은 고급 푸시 캠페인 설정에 대해 다룹니다."
platform: Android
channel:
  - push
tool:
  - Campaigns

---

# 고급 푸시 캠페인 설정

> Android 및 Fire OS 푸시 알림을 Braze 대시보드를 통해 보낼 때 사용할 수 있는 고급 설정이 많이 있습니다. 이 기사에서는 이러한 기능과 성공적으로 사용하는 방법에 대해 설명합니다.

## 알림 ID {#notification-id}

알림 ID는 메시징 서비스가 해당 ID의 최신 메시지만 존중하도록 알리는 메시지 범주의 고유 식별자입니다. 알림 ID를 설정하면 오래되고 관련 없는 메시지 더미가 아닌 최신의 관련 메시지만 보낼 수 있습니다.

알림 ID를 할당하려면 ID를 추가하려는 푸시의 작성 페이지로 이동하여 **설정** 탭을 선택하세요. **알림 ID** 섹션에 정수를 입력하세요. 이 알림을 발행한 후 업데이트하려면 이전에 사용한 동일한 ID로 다른 알림을 보내세요.

![Notification ID field.]({% image_buster /assets/img_archive/notification_ids.png %}){: style="max-width:60%;" }

## Time to live (TTL) {#ttl}

The **Time to Live** field allows you to set a custom length of time to store messages with the push messaging service. If the device remains offline beyond the TTL, the message will expire and not be delivered.

To edit the time to live for your Android push, go to the composer and select the **Settings** tab. Find the **Time to Live** field and enter a value in days, hours, or seconds.

The default values for time to live are defined by your admin on the [Push Settings]({{site.baseurl}}/user_guide/administrative/app_settings/push_settings/) page. By default, Braze sets Push TTL to the maximum value for each push messaging service. While default TTL settings apply globally, you can override them at the message level during campaign creation. This is helpful when different campaigns require varying urgency or delivery windows.

For example, let's say your app hosts a weekly trivia contest. You send a push notification an hour before it starts. By setting the TTL to 1 hour, you make sure that users who open the app after the contest starts won’t receive a notification about an event that has already begun.

{% details Best practices %}

#### When to use shorter TTL

Shorter TTLs make sure users receive timely notifications for events or promotions that quickly lose relevance. For example:

- **Retail:** Sending a push for a flash sale that ends in 2 hours (TTL: 1–2 hours)
- **Food delivery:** Notifying users when their order is nearby (TTL: 10–15 minutes)
- **Transportation apps:** Sharing ride arrival updates (TTL: a few minutes)
- **Event reminders:** Notifying users when a webinar is starting soon (TTL: under 1 hour)

#### When to avoid shorter TTL

- If your campaign’s message remains relevant for several days or weeks, such as subscription renewal reminders or ongoing promotions.
- When maximizing reach is more important than urgency, like with app update announcements or feature promotions.

{% enddetails %}

## Firebase 메시징 전달 우선순위 {#fcm-priority}

**Firebase 메시징 전송 우선순위** 필드를 통해 푸시 전송 우선순위를 "일반" 또는 "높음"으로 설정하여 Firebase 클라우드 메시징에 전송할지 여부를 제어할 수 있습니다. This setting determines how quickly messages are delivered and how they affect device battery life.

| 우선순위 | 설명 | Best for |
|---------|-------------|----------|
| Normal | Battery-optimized delivery that may be delayed to conserve battery | Non-urgent content, promotional offers, news updates |
| 높음 | Immediate delivery with higher battery consumption | Time-sensitive notifications, critical alerts, live event updates, account alerts, breaking news, or urgent reminders |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Considerations

- **Default setting**: You can set a default FCM priority for all Android campaigns in your [Push Settings]({{site.baseurl}}/user_guide/administrative/app_settings/push_settings/). This campaign-level setting will override the default if needed.
- **Deprioritization**: If FCM detects that your app frequently sends high-priority messages that don't result in user-visible notifications or user engagement, those messages may be automatically deprioritized to normal priority.
- **Battery impact**: High-priority messages wake sleeping devices more aggressively and consume more battery. Use this priority judiciously.

For more detailed information on message handling and deprioritization, see [FCM documentation](https://firebase.google.com/docs/cloud-messaging/concept-options#setting-the-priority-of-a-message) and [Message handling and deprioritization on Android](https://firebase.google.com/docs/cloud-messaging/android/message-priority#deprioritize).

## 요약 텍스트

The summary text allows you to set additional text in the expanded notification view. 알림에 이미지가 포함된 경우 캡션으로도 사용됩니다.

![An Android message with the title "This is the title for the notification." and summary text "This is the summary text for the notification."]({% image_buster /assets/img/android/push/collapsed-android-notification.png %}){: style="max-width:65%;"}

요약 텍스트는 확장된 보기에서 메시지 본문 아래에 표시됩니다. 

![An Android message with the title "This is the title for the notification." and summary text "This is the summary text for the notification."]({% image_buster /assets/img/android/push/expanded-android-notification.png %}){: style="max-width:65%;"}

푸시 알림에 이미지가 포함된 경우, 메시지 텍스트는 축소된 보기에서 표시되며, 요약 텍스트는 알림이 확장될 때 이미지 캡션으로 표시됩니다. 

## 커스텀 URI

**커스텀 URI** 기능을 사용하면 알림을 클릭할 때 이동할 웹 URL 또는 Android 리소스를 지정할 수 있습니다. 커스텀 URI가 지정되지 않은 경우 알림을 클릭하면 사용자가 앱으로 이동합니다. 커스텀 URI를 사용하여 앱 내부에서 딥 링크를 만들 수 있을 뿐만 아니라 앱 외부에 존재하는 리소스로 사용자를 직접 안내할 수도 있습니다. This can be specified via our [Messaging API]({{site.baseurl}}/api/endpoints/messaging/) or in the **Compose** tab of the the push composer.

![Custom URI field.]({% image_buster /assets/img_archive/deep_link.png %}){: style="max-width:60%;"}

## 알림 표시 우선순위

{% alert important %}
알림 표시 우선순위 설정은 Android O 이상을 실행하는 기기에서는 더 이상 사용되지 않습니다. 최신 장치의 경우 [알림 채널 구성](https://developer.android.com/training/notify-user/channels#importance)을 통해 우선 순위를 설정하십시오.
{% endalert %}

푸시 알림의 우선순위 수준은 다른 알림에 비해 알림 트레이에 표시되는 방식에 영향을 미칩니다. 또한 우선순위가 일반 이하인 메시지는 배터리 수명을 보존하기 위해 지연 시간이 약간 더 길어지거나 일괄 발송되는 반면, 우선순위가 높은 메시지는 항상 즉시 발송되므로 전송 속도와 방식에도 영향을 줄 수 있습니다.

이 기능은 메시지의 중요도나 긴급성에 따라 메시지를 구분하는 데 유용합니다. 예를 들어, 위험한 도로 상태에 대한 알림은 높은 우선순위를 받을 좋은 후보가 될 수 있지만, 진행 중인 세일에 대한 알림은 낮은 우선순위를 받아야 합니다. 사용자가 받은편지함에서 항상 최상위 자리를 차지하거나 다른 활동을 방해하는 것은 부정적인 영향을 미칠 수 있으므로, 방해 우선순위를 사용하는 것이 실제로 필요한지 여부를 고려해야 합니다.

Android O에서 알림 우선순위는 알림 채널의 속성이 되었습니다. 채널의 구성 중 우선순위를 정의하려면 개발자와 협력해야 하며, 알림 소리를 보낼 때 적절한 채널을 선택하려면 대시보드를 사용해야 합니다. O 이전의 Android 버전을 실행하는 기기의 경우, Braze 대시보드 및 메시징 API를 통해 Android 및 FireOS 알림의 우선순위를 지정할 수 있습니다.

To message your full user base with a specific priority, we recommend that you indirectly specify the priority through [notification channel configuration](https://developer.android.com/training/notify-user/channels#importance) (to target O+ devices) and send the individual priority from the dashboard (to target <O devices).

Android 또는 Fire OS 푸시 알림에 설정할 수 있는 우선 순위 수준에 대한 다음 표를 참조하십시오:

| 우선순위 | 설명| `priority` 값 (API 메시지용) |
|------|-----------|----------------------------|
| 최대 | 긴급하거나 시간에 민감한 메시지. | `2` |
| 높음 | 친구의 새 메시지와 같은 중요한 커뮤니케이션. | `1` |
| 기본값 | 대부분의 알림. 다른 우선순위 유형 중 어느 것에도 명시적으로 해당되지 않는 경우 메시지를 사용하세요. | `0` |
| 낮음 | 사용자가 알고 싶어하는 정보이지만 즉각적인 조치가 필요하지는 않습니다. | `-1`|
| 최소 | 상황별 또는 배경 정보. | `-2`|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

For more information, refer to Google's documentation on [Android notifications](http://developer.android.com/design/patterns/notifications.html).

## 푸시 카테고리

Android 푸시 알림은 알림이 미리 정의된 범주에 속하는지 여부를 지정할 수 있는 옵션을 제공합니다. Android 시스템 UI는 이 범주를 사용하여 사용자 알림 트레이에서 알림을 배치할 위치에 대한 순위 지정 또는 필터링 결정을 내릴 수 있습니다.

![Settings tab with the Category set to None, which is the default setting.]({% image_buster /assets/img_archive/braze_category.png %}){: style="max-width:60%;"}

| 카테고리 | 설명 |
|---|-------|
| 없음 | 기본값 옵션. |
| 경보 | 알람 또는 타이머. |
| 호출 | 수신 전화(음성 또는 비디오) 또는 유사한 동기식 통신 요청. |
| 이메일 | 비동기 대량 메시지 (이메일). |
| 오류 | 백그라운드 작업 또는 인증 상태에 오류가 발생했습니다. |
| 이벤트 | 캘린더 이벤트. |
| 메시지 | 수신된 직접 메시지 (SMS, 인스턴트 메시지 등). |
| 진행률 | 오래 실행되는 백그라운드 작업의 진행 상황. |
| 프로모션 | 홍보 또는 광고. |
| 추천 | 특정하고 시기적절한 단일 항목에 대한 추천. |
| 리마인더 | 사용자 예약 알림. |
| 서비스 | 백그라운드 서비스 실행 표시. |
| 소셜 | 소셜 네트워크 또는 공유 업데이트. |
| 상태 | 기기 또는 상황별 상태에 대한 진행 중인 정보. |
| 시스템 | 시스템 또는 기기 상태 업데이트. 시스템 사용을 위해 예약됨. |
| 이동 | 재생을 위한 미디어 전송 제어. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 푸시 가시성

Android 푸시 알림은 사용자의 잠금 화면에 알림이 어떻게 나타나는지 결정하는 선택적 필드를 제공합니다. 다음 표에서 가시성 옵션 및 설명을 참조하십시오.

| 가시성 | 설명 |
|---|-----|
| 공개 | 잠금 화면에 알림이 나타납니다 |
| 비공개 | 알림이 "내용 숨김" 메시지로 표시됩니다 |
| 비밀 | 알림이 잠금 화면에 표시되지 않습니다 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

또한, Android 사용자는 기기의 알림 개인 정보 설정을 변경하여 잠금 화면에 푸시 알림이 나타나는 방식을 재정의할 수 있습니다. 이 설정은 푸시 알림의 가시성을 무시합니다.

![Dashboard push priority location with Set Visibility enabled and set to Private.]({% image_buster /assets/img_archive/braze_visibility.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

표시 여부와 관계없이 기기의 알림 개인 정보 설정이 **모든 콘텐츠 표시**(기본값)로 설정된 경우 모든 알림이 사용자의 잠금 화면에 표시됩니다. 마찬가지로, 알림 개인 정보가 **알림 표시 안 함**으로 설정된 경우 잠금 화면에 알림이 표시되지 않습니다. 가시성은 알림 개인 정보 보호 설정이 **민감한 콘텐츠 숨기기**로 설정된 경우에만 영향을 미칩니다.

가시성은 Android Lollipop 5.0.0 이전 장치에는 영향을 미치지 않으며, 이 기기에서는 모든 알림이 표시됩니다.

Refer to our [Android documentation](https://developer.android.com/guide/topics/ui/notifiers/notifications) for more information.

## 알림음

Android O에서 알림 소리는 알림 채널의 속성이 되었습니다. 채널의 구성 중에 소리를 정의하기 위해 개발자와 협력해야 하며, 알림을 보낼 때 적절한 채널을 선택하기 위해 대시보드를 사용해야 합니다.

Android O 이전 버전의 Android를 실행하는 기기에서는 Braze가 대시보드 컴포저를 통해 개별 푸시 메시지의 소리를 설정할 수 있도록 합니다. 기기에서 로컬 사운드 리소스를 지정하면 됩니다(예: `android.resource://com.mycompany.myapp/raw/mysound`). 

이 필드에서 **기본값**을 선택하면 기기에서 기본 알림 소리가 재생됩니다. This can be specified via our [Messaging API]({{site.baseurl}}/api/endpoints/messaging/) or in the **Settings** in the push composer.

![The "Sound" field.]({% image_buster /assets/img_archive/sound_android.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

다음으로, 전체 사운드 리소스 URI(예: `android.resource://com.mycompany.myapp/raw/mysound`)를 대시보드 프롬프트에 입력하세요.

To message your full user base with a specific sound, we recommend that you indirectly specify the sound through [notification channel configuration](https://developer.android.com/training/notify-user/channels) (to target O+ devices) and send the individual sound from the dashboard (to target <O devices).

