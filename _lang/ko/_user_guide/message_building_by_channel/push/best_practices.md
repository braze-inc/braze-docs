---
page_order: 20
nav_title: 모범 사례
article_title: 푸시 모범 사례
description: "이 페이지에는 푸시 모범 사례와 사용 사례를 통해 푸시 메시지가 성가신 것이 아니라 참여를 유도할 수 있도록 하는 방법이 나와 있습니다."
channel: push
---

# 푸시 모범 사례

푸시 알림은 앱 사용자와 소통할 수 있는 강력한 도구이지만, 적시에 관련성 있는 메시지를 전달할 수 있도록 신중하게 사용해야 합니다. 푸시 메시지를 보내기 전에 다음 모범 사례를 참조하여 알아야 할 사항과 확인해야 할 사항을 확인하세요.

{% alert important %}
푸시 메시지는 광고, 스팸, 프로모션 등으로 푸시 메시지를 사용하는 것과 관련된 Apple App Store 및 Google Play 스토어 정책의 가이드라인을 준수해야 합니다. [모바일 푸시 규정]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#mobile-push-regulations-for-apps)에 대해 자세히 알아보세요.
{% endalert %}

## 푸시 메시지 작성

모범 사례로, Braze는 모바일 푸시 알림에서 선택 사항인 제목과 메시지 본문의 각 텍스트 줄을 약 30~40자로 유지하는 것을 권장합니다. 작곡기의 문자 카운터는 Liquid 문자를 계산하지 않는다는 점에 유의하세요. 즉, 메시지의 최종 글자 수는 각 사용자에 대해 Liquid가 렌더링하는 방식에 따라 달라집니다. 확실하지 않은 경우 짧고 간결하게 작성하세요.

## 타겟팅 최적화

### 관련 사용자 데이터 수집

푸시 알림은 적시에 관련성 있는 알림으로 사용자를 타겟팅할 수 있도록 신중하게 처리해야 합니다. Braze는 관련 세그먼트를 타겟팅하는 데 사용할 수 있는 유용한 기기 및 사용 정보를 수집합니다. 이 정보는 앱에 특정한 커스텀 이벤트 및 속성으로 보완해야 합니다. 이 데이터를 사용하면 메시지를 신중하게 타겟팅하여 열람율을 높이고 푸시를 비활성화하는 사용자의 사례를 줄일 수 있습니다.

### 알림 설정 페이지 만들기

앱에서 설정 페이지를 만들어 사용자가 수신할 알림을 지정할 수 있도록 할 수 있습니다. 일반적인 접근 방식은 앱 설정 상태에 해당하는 부울 커스텀 속성을 Braze에 생성하는 것입니다. 예를 들어 뉴스 앱에는 속보, 스포츠 뉴스 또는 정치에 대한 구독 설정이 있을 수 있습니다.

뉴스 앱에서 정치에 관심 있는 사용자만 타겟팅하는 캠페인을 만들고자 하는 경우 세그먼트에 `Subscribes to Politics` 속성 필터를 추가합니다. true로 설정하면 알림을 구독하는 사용자만 알림을 받게 됩니다.

커스텀 속성 설정에 대한 자세한 내용은 [iOS][6], [Android][7] 또는 [REST API][8]에 대한 문서를 참조하세요.

## 옵트인 및 관련성 향상

### 사용자 권한 얻기

푸시 사용 여부에 대한 일반적인 통계는 사용자가 운영 체제에서 알림을 승인했는지 여부와 관련이 있습니다. 사용자가 iOS에서 알림을 끄면 Apple에서 푸시 토큰 전송을 허용하지 않으므로 시스템에서 자동으로 제거됩니다.

Android 13 이상에서는 푸시 알림을 표시하려면 먼저 권한을 얻어야 합니다. 이전 버전의 Android는 기본적으로 사용자에게 알림을 구독하도록 설정합니다.

### 푸시용 주요 사용자

사용자에게 푸시 권한을 요청할 수 있는 기회는 단 한 번뿐이며, 사용자가 이를 거부하면 디바이스 설정에서 푸시를 다시 사용하도록 설득하기가 매우 어렵습니다. 따라서 시스템 프롬프트를 표시하기 전에 인앱 메시지를 사용하여 사용자에게 푸시를 유도해야 합니다. 옵트인을 늘리는 방법에 대해 자세히 알아보려면 [푸시 프라이머 인앱 메시지를][2] 참조하세요.

### 푸시 구독 컨트롤 추가

사용자가 기기 수준에서 알림을 끄면 포그라운드 푸시 토큰이 완전히 제거되는 것을 방지하려면 사용자가 앱 내에서 직접 푸시 구독을 제어할 수 있도록 하세요. 자세한 내용은 [푸시 구독 상태 업데이트하기][10]를 참조하세요.

### 푸시 구독 상태 이해하기

푸시 구독 상태는 푸시 전송을 보장하지 않으며, 알림을 받으려면 사용자가 푸시를 사용하도록 설정되어 있어야 합니다. 이는 고객 프로필에 포그라운드 푸시 권한이 서로 다른 여러 기기가 있지만 푸시 구독 상태는 하나만 있을 수 있기 때문입니다.

사용자가 앱에 유효한 포그라운드 푸시 토큰이 없는 경우(즉, 설정을 통해 기기 수준에서 푸시 토큰을 끄고 알림을 받지 않기로 선택한 경우) 구독 상태는 여전히 `subscribed`로 간주되어 푸시할 수 있습니다. 그러나 이 사용자는 포그라운드 푸시 토큰이 유효하지 않으므로 Braze에서 `Push Enabled for App`이 아닙니다.

또한 고객 프로필에 다른 앱에 대해 유효하거나 등록된 푸시 토큰이 없는 경우 세분화의 `Push Enabled` 필터도 거짓이 됩니다.

## 응답이 없는 사용자에 대한 일몰 정책 구현하기

시의적절하고 관련성 있는 푸시 알림만 보내도 일부 사용자는 푸시 알림에 응답하지 않거나 스팸으로 간주할 수 있습니다. 사용자가 푸시 알림을 반복적으로 무시한 이력을 보인다고 가정해 보겠습니다. 이 경우 앱의 커뮤니케이션에 짜증이 나기 전에 푸시 전송을 중단하거나 아예 앱을 삭제하는 것이 좋습니다. 

이렇게 하려면 [일몰 정책][9]을 만들어 오랫동안 직접 또는 영향력을 행사한 적이 없는 사용자에게 푸시 알림을 보내지 않도록 합니다.

1. 직접 또는 영향을 받은 열기를 기반으로 응답하지 않는 사용자를 식별합니다.
2. 해당 사용자에게 푸시 알림 전송을 점진적으로 중단합니다.
3. 푸시 알림을 완전히 제거하기 전에 푸시 알림을 더 이상 받지 않게 되는 이유를 설명하는 마지막 알림을 한 번 더 전달하세요. 이렇게 하면 사용자가 해당 알림을 열어 지속적인 푸시에 대한 관심을 표시할 수 있습니다.
4. 일몰 정책이 시행된 후에는 [인앱 메시지][13]를 사용하여 이러한 사용자에게 더 이상 푸시를 받지 못하지만 인앱 메시징 채널에서 흥미롭고 유용한 정보를 계속 전달할 것임을 알려주세요.

원래 푸시를 옵트인한 사용자에게 푸시 전송을 중단하는 것이 꺼려질 수 있지만, 특히 이전에 푸시를 무시했던 사용자라면 다른 메시징 채널이 이러한 사용자에게 더 효과적으로 도달할 수 있다는 점을 기억하세요. 사용자가 이메일을 열면 이메일 캠페인은 앱 외부에서 사용자에게 도달할 수 있는 좋은 방법입니다. 그렇지 않은 경우 인앱 메시지는 사용자가 앱을 삭제할 위험 없이 콘텐츠를 전달할 수 있는 가장 좋은 방법입니다.

## 앱 실행에 대한 전환 이벤트 설정

푸시 캠페인에 [전환 이벤트][11]를 할당할 때, 캠페인이 수신된 후 일정 기간 동안 앱 실행을 추적할 수 있습니다. 앱 실행에 대한 전환 이벤트를 설정하면 푸시 캠페인 후 일반적으로 받는 결과 통계와는 다른 인사이트를 얻을 수 있습니다.

모든 푸시 캠페인 결과는 메시지의 직접 오픈과 오픈(직접 오픈과 [영향받은 오픈][12] 모두 포함)으로 분류되지만, 전환 추적은 직접 오픈이든 영향받은 오픈이든 모든 유형의 오픈을 추적합니다.

또한 전환 이벤트 "앱 열기"를 사용하면 해당 전환 마감일(예: 3일) 이전에 발생한 앱 열기를 추적할 수 있습니다. 이는 사용자가 영향력 있는 열람을 등록해야 하는 시간이 각 사용자의 과거 인게이지먼트 행동에 따라 사람마다 다를 수 있다는 점에서 영향력 있는 오픈과 다릅니다.

## 관련 문서

원하는 정보를 찾지 못하셨나요? 이 추가 모범 사례 문서를 확인하세요:

- [푸시 메시지 및 이미지 형식][1]
- [푸시 프라이머 인앱 메시지][2]
- [중국 Android 기기용 전달 가능성][3]
- [보내기 전에 알아두어야 할 사항: 채널][4]

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/message_format/
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/chinese_push_deliverability/
[4]: {{site.baseurl}}/help/help_articles/campaigns_and_canvas/know_before_send/

[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_custom_attributes/
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/#setting-custom-attributes
[8]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-attributes-object-specification
[9]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sunset_policies
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions#update-push-subscription-state
[11]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/
[12]: {{site.baseurl}}/user_guide/data_and_analytics/tracking/influenced_opens
[13]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/