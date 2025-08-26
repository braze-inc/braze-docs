---
nav_title: 보내기 전에 알아두어야 할 사항
article_title: 보내기 전에 알아두어야 할 사항
description: "사전 출시 가이드를 방문한 후, 콘텐츠 카드, 이메일, 인앱 메시지, 푸시 및 SMS에 대한 최종 확인 목록 또는 '주의 사항'을 참조하세요."
alias: /know_before_send/

---

# 보내기 전에 알아두세요: 채널

자신감을 가지고 캠페인과 캔버스를 시작하세요! 콘텐츠 카드, 이메일, 인앱 메시지, 푸시 및 SMS에 대한 최종 확인 또는 "주의 사항" 목록을 참조하세요.

{% alert note %}
저희는 발송 전 참조할 수 있는 방대한 자료 목록을 제공하지만, 각 채널은 저희 제품이 발전함에 따라 계속해서 성장하는 개별적인 특성을 가지고 있습니다. 아래 나열된 검사는 유용한 제안이며, 발송하기 전에 캠페인과 대량 발송을 철저히 테스트할 것을 권장합니다.
{% endalert %}

## 일반

#### 확인할 사항
- [**API 속도 제한**](https://braze.com/resources/articles/whats-rate-limiting): 워크스페이스에서 오류가 발생하지 않도록 Braze API [사용량 제한]({{site.baseurl}}/api/api_limits/)을 검토하세요. 요청을 일괄 처리하고 있는 경우 사용량 제한을 늘리고 싶다면 고객 성공 매니저에게 문의하세요. 이 과정에는 리드 타임이 필요하므로 이에 따라 계획을 세우십시오.
- [**필요한 최대 게재빈도 설정 재정의**]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping): 일부 캠페인, 예를 들어 트랜잭션 메시지와 같은 경우, 사용자의 빈도 제한에 도달했더라도 항상 사용자에게 도달하기를 원할 것입니다(예: 전달 알림). 특정 캠페인이 최대 게재빈도 설정 규칙을 무시하도록 하려면, 해당 캠페인의 전달을 예약할 때 Braze 대시보드에서 최대 게재빈도 설정을 끔으로 설정할 수 있습니다.

#### 알아야 할 사항
- [**글로벌 컨트롤 그룹**]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group#global-control-group): 글로벌 컨트롤 그룹을 사용하는 경우, 일부 사용자는 캠페인이나 캔버스를 받지 않습니다. (제외 설정[을 사용하여 예외를 만들 수 있습니다]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#step-3-assign-exclusion-settings)). 이 사용자 목록을 보려면 CSV 또는 [API]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/)를 통해 내보내십시오.
- [**캔버스 사용량 제한**]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting): 캔버스에서 사용량 제한은 개별 단계가 아닌 전체 캔버스에 적용됩니다. 예를 들어, 여러 단계가 있는 캔버스에 분당 10,000 메시지의 사용량 제한을 설정하면 첫 번째 단계에서 제한에 도달했기 때문에 여전히 10,000 메시지로 제한됩니다.
- **최대 게재빈도 설정**: 
  - 최대 게재빈도 설정 규칙은 푸시, 이메일, SMS 및 웹훅에 적용되지만, 인앱 메시지 및 콘텐츠 카드에는 적용되지 않습니다.
  - 전역 최대 게재빈도 설정은 사용자의 시간대를 기준으로 예약되며 24시간이 아닌 캘린더 일 기준으로 계산됩니다. 예를 들어, 하루에 한 개의 캠페인만 보내도록 최대 게재빈도 설정 규칙을 설정한 경우, 사용자는 현지 시간대로 오후 11시에 메시지를 받을 수 있으며 한 시간 후에 또 다른 메시지를 받을 자격이 주어집니다.

{% alert tip %}
캔버스 및 캠페인 문제 해결에 대한 추가 지원이 필요하시면 문제 발생 후 30일 이내에 Braze 지원팀에 문의하세요. 진단 로그는 최근 30일 동안만 보관됩니다.
{% endalert %}

## 이메일

#### 확인할 사항
- **고객 consent**: 초기 이메일을 보내기 전에 고객의 허락을 먼저 받는 것이 중요합니다. [동의 및 주소 수집]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/consent_and_address_collection/) 및 자세한 내용은 당사의 [Braze 허용 사용 정책](https://www.braze.com/company/legal/aup)을 참조하십시오.
- **예상 볼륨**: 일일 200만 개의 이메일을 단일 IP로 보내는 것은 해당 볼륨이 [적절히 준비된]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/ip_warming#ip-warming) 경우 일반적인 권장 사항입니다. 
  - 만약 이보다 더 많은 양을 지속적으로 보내려는 계획이 있다면, 제공업체가 이메일 수신을 제한하여 많은 소프트 바운스, 낮은 전달 가능성 비율, 그리고 IP 평판 저하를 초래하는 것을 피하기 위해, IP 풀에 묶인 여러 IP 주소를 사용하는 것을 고려하세요. 
  - 짧은 시간 내에만 보내고자 한다면, 다양한 제공업체가 메일을 수락하는 속도를 조사하여 적절한 IP 수를 파악하는 것을 권장합니다. 

#### 알아야 할 사항
- **발송량 요소**: IP의 유능한 발송량을 결정하는 몇 가지 요인에는 다음이 포함됩니다.
  - 우편함: 대형 이메일 제공업체는 단일 IP에서 하루에 수백만 건을 처리할 수 있는 반면, 소규모 지역 받은편지함 제공업체나 인프라가 작은 제공업체는 그 양을 처리하지 못할 수 있습니다.
  - 발송자 평판: 발송자가 해당 볼륨으로 증가되고 각 받은편지함 또는 도메인에서 발송자 평판이 충분히 강한 경우 단일 IP에서 하루에 더 많은 양을 보낼 수 있습니다.
- **모범 사례**: Braze [이메일 모범 사례]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices)를 검토하고 전달 가능성 서비스에 대해 더 알고 싶다면 Braze 계정 팀에 문의하세요.

## 푸시

#### 확인할 사항
- [**옵트인/구독 및 푸시 사용**]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/): 사용자가 Braze로부터 푸시 메시지를 받으려면 구독 상태가 옵트인(iOS) 또는 구독(Android) 및 `Push Enabled = True`여야 합니다. Android 13은 푸시 알림을 보내는 앱을 관리하는 방식에 큰 변화를 도입했습니다. Braze [Android 13 소프트웨어 개발 키트 업그레이드 가이드]({{site.baseurl}}/developer_guide/platforms/android/android_13/)는 새로운 Android 13 베타 버전이 출시될 때마다 계속 업데이트될 것입니다.

#### 알아야 할 사항
- **웹 푸시**: Braze [웹 SDK 설정]({{site.baseurl}}/user_guide/message_building_by_channel/push/web)이 있는 경우 웹 푸시를 사용하여 사용자를 참여시키는 것을 고려하세요. 웹 푸시는 앱 푸시 알림이 휴대폰에서 작동하는 방식과 동일하게 작동합니다. 웹 푸시 작성에 대한 자세한 내용은 [푸시 알림 만들기]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message)을 참조하세요.
- **Singular 앱 타겟팅**: [세분화의 차이점]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#targeting-a-singular-app)을 검토하여 단일 앱과 그 사용자를 타겟팅합니다.

## SMS

#### 확인할 사항
- **할당량 및 처리량**: 현재 귀하의 계정에 할당된 SMS 할당량(짧은 코드, 긴 코드 등)과 [이를 통해 제공되는 처리량]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_setup/short_and_long_codes/)을 이해하여 원하는 시간에 보낼 수 있는 충분한 처리량이 있는지 확인하십시오.
- **SMS 복사본에서 세그먼트 추정**: SMS 복사본을 [SMS 세그먼트 계산기]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#things-to-keep-in-mind-as-you-create-your-copy)에서 테스트하세요. SMS 세그먼트 수를 처리량 능력과 함께 고려해야 합니다. (오디언스 * SMS segments = Throughput needed). SMS FAQ를 참조하여 [초과 사용을 피하는 방법]({{site.baseurl}}/user_guide/message_building_by_channel/sms/faqs/#how-can-i-avoid-overages)에 대해 알아보세요.
- **SMS 법률 및 규정**: [SMS 법률, 규정 및 남용 방지]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/)를 검토하여 모든 관련 법률을 준수하여 SMS 서비스를 사용하고 있는지 확인하십시오. 보내기 전에 법률 자문을 구해야 합니다.

#### 알아야 할 사항
- **SMS 메시지 기본값**: SMS 메시지는 일반적으로 발신자 풀의 짧은 코드에서 보내도록 기본 설정됩니다.
- **영숫자 발신자 ID**: 알파벳과 숫자가 혼합된 발신자 ID를 사용하면 양방향 메시징이 더 이상 작동하지 않습니다. 이제 이러한 ID는 단방향으로만 작동합니다.
- **미국에서 업데이트된 처리량**: 미국에서 [A2P 10DLC 등록](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US)으로 처리량이 변경되었습니다. 여러 가지 요인(예: 트래픽 혼잡 및 운송업체 문제)으로 인해 실제 전달 속도에 영향을 미칠 수 있으므로, 우리는 계약상 어떠한 전송 속도 SLA에도 동의하지 않습니다.
- **구독 그룹**: Braze를 통해 SMS 캠페인을 시작하려면 구독 그룹을 선택해야 합니다. 또한 국제 [통신 규정 및 지침]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/)을 준수하기 위해 Braze는 [선택한 구독 그룹에 가입하지 않은]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#how-to-check-a-users-sms-subscription-group) 사용자에게 SMS를 보내지 않습니다.

## WhatsApp

#### 알아야 할 사항

- [**모범 사례**]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_best_practices/): 제안된 WhatsApp 모범 사례를 검토하십시오.

## 콘텐츠 카드

#### 확인할 사항
- **콘텐츠 카드 크기**: 콘텐츠 카드 메시지 필드는 압축 전 크기가 2KB로 제한되며 제목, 메시지, 이미지 URL, 링크 텍스트, 링크 URL 및 키-값 페어 필드의 바이트 크기를 합산하여 계산됩니다. 이 크기를 초과하는 메시지는 전송되지 않습니다. 이것은 이미지의 크기가 아니라 이미지 URL의 길이를 포함한다는 점에 유의하십시오.
- **전송 후 복사본 업데이트**: 카드를 보낸 후에는 동일한 카드의 복사본을 업데이트할 수 없습니다. [보낸 카드 업데이트]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/#updating-sent-cards)를 참조하여 이 시나리오에 접근하는 방법을 이해하십시오.

#### 알아야 할 사항
- **활성 콘텐츠 카드 캠페인 제한**: 최대 500개의 활성 콘텐츠 카드 캠페인을 가질 수 있습니다. 이 수에는 [카드 생성]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/) 옵션으로 전송된 콘텐츠 카드가 포함됩니다.  
- [**보고 용어**]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/reporting/): 총 노출 횟수, 고유 노출 횟수, 고유 수신자와 같은 용어를 검토하세요. 정의가 때때로 혼란을 일으킬 수 있습니다.
- **콘텐츠 카드 새로고침**: 기본값으로, Braze는 콘텐츠 카드 요청을 세션 시작 시, 피드 아래로 스와이프할 때(모바일), 그리고 마지막 새로고침이 1분 이상 지났을 때 카드 보기를 열 때 동기화합니다.
- **캐싱 콘텐츠 카드**: 콘텐츠 카드 캐싱 옵션은 저희 [Android/FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/customization/custom_styling/#customizing-card-rendering-for-android) 및 [웹](https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#getcachedcontentcards) 문서에서 찾을 수 있습니다. 
- **최대 게재빈도 설정**: 최대 게재빈도 설정은 콘텐츠 카드에 적용되지 않습니다.
- **노출 횟수**: 노출 횟수는 일반적으로 카드가 보일 때 기록됩니다. 예를 들어, 받은편지함에 콘텐츠 카드가 가득 차 있는 경우 사용자가 특정 콘텐츠 카드로 스크롤할 때까지 노출 횟수가 기록되지 않습니다. 웹, Android 및 iOS 플랫폼 간에는 몇 가지 미묘한 차이가 있습니다.  

## 인앱 메시지

#### 알아야 할 사항
- **인앱 메시지 트리거링**: 세션 시작 시, SDK는 모든 적격 인앱 메시지가 트리거와 함께 기기로 전송되도록 요청하므로, 세션 중에 이벤트를 수행하면 인앱 메시지를 빠르고 신뢰성 있게 받을 수 있습니다. 이로 인해 캔버스 내에서 인앱 메시지는 커스텀 이벤트로 트리거될 수 없습니다.
- **전송 대 노출 횟수**: 인앱 메시지의 경우, "발송됨"의 개념은 다른 사용 가능한 채널과 다릅니다. 인앱 메시지를 보려면 사용자가 세션을 시작하고, 해당 오디언스에 속하며, 트리거를 수행해야 합니다. 이 때문에 우리는 "노출 횟수"를 더 명확하게 추적합니다.
- **트리거**: 기본값으로, 인앱 메시지는 SDK에 의해 기록된 이벤트에 의해 트리거됩니다. 서버에서 보낸 이벤트로 인해 인앱 메시지를 트리거하려면 [iOS]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=swift) 및 [Android]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android)에 대한 이러한 가이드를 통해서도 이를 달성할 수 있습니다.
- [캔버스 인앱 메시지]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas/#advancement-behavior-options): 이 메시지는 사용자가 앱을 처음 열 때(세션 시작 시 트리거됨) 캔버스 구성 요소에서 예약된 메시지가 전송된 후에 나타납니다.
- **연결된 콘텐츠 호출**: 커넥티드 콘텐츠를 사용하면 메시지에서 동적 콘텐츠를 보낼 수 있습니다. 인앱 메시지와 같은 채널을 통해 메시지를 보내면 사용자의 디바이스에 더 많은 동시 접속자가 생길 수 있습니다(메시지는 일괄적으로 전송되지 않고 하나씩 전송됨). 이를 관리하려면 메시지 [속도 제한을]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting) 사용하는 것이 좋습니다.