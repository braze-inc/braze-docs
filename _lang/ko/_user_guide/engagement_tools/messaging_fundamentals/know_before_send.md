---
nav_title: 보내기 전에 알아두세요
article_title: 보내기 전에 알아두세요
description: "사전 출시 가이드를 방문한 후, 콘텐츠 카드, 이메일, 앱 내 메시지, 푸시 및 SMS에 대한 최종 점검 목록 또는 '주의 사항'을 참조하세요."
alias: /know_before_send/
page_order: 10.2
tool:
    - Campaigns
    - Canvas
---

# 보내기 전에 알아두세요: 채널

자신감을 가지고 캠페인과 캔버스를 시작하세요! 콘텐츠 카드, 이메일, 앱 내 메시지, 푸시 및 SMS에 대한 최종 점검 목록 또는 "주의 사항"을 참조하세요.

{% alert note %}
우리는 보내기 전에 참조할 수 있는 방대한 자원 목록을 제공하지만, 각 채널은 제품이 발전함에 따라 계속해서 성장하는 개별적인 뉘앙스가 있습니다. 아래에 나열된 점검 사항은 유용한 제안이며, 보내기 전에 캠페인과 대규모 발송을 철저히 테스트할 것을 권장합니다.
{% endalert %}

## 일반

#### 확인할 사항
- [**API 속도 제한**](https://braze.com/resources/articles/whats-rate-limiting): 오류가 발생하지 않도록 작업 공간에 대한 Braze API [속도 제한]({{site.baseurl}}/api/api_limits/)를 검토하세요. 속도 제한을 늘리려는 경우(이미 요청을 배치하고 있는 경우), 고객 성공 관리자에게 문의하세요. 이 프로세스에는 시간이 필요하므로 계획을 세우세요.
- [**필요한 빈도 제한 오버라이드**]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping): 거래 메시지와 같은 일부 캠페인은 사용자의 빈도 제한에 도달했더라도 항상 사용자에게 도달해야 합니다(예: 배송 알림). 특정 캠페인이 빈도 제한 규칙을 오버라이드하도록 하려면, 해당 캠페인의 배달을 예약할 때 Braze 대시보드에서 빈도 제한을 끄도록 설정할 수 있습니다.

#### 알아야 할 사항
- [**글로벌 제어 그룹**]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group#global-control-group): 글로벌 제어 그룹을 사용하는 경우, 일부 사용자에게는 캠페인이나 캔버스가 제공되지 않습니다. (예외를 만들 수 있습니다 [제외 설정]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#step-3-assign-exclusion-settings)). 이 사용자 목록을 보려면 CSV로 내보내거나 [API]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/)를 통해 내보내십시오.
- [**캔버스 비율 제한**]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting): 캔버스에서는 비율 제한이 전체 캔버스에 적용되며, 개별 단계에는 적용되지 않습니다. 예를 들어, 여러 단계가 있는 캔버스에서 분당 10,000 메시지 비율 제한을 설정하면, 첫 번째 단계에서 제한이 도달했기 때문에 여전히 10,000 메시지로 제한됩니다.
- **빈도 제한**: 
  - 빈도 제한 규칙은 푸시, 이메일, SMS 및 웹훅에 적용되지만, 앱 내 메시지 및 콘텐츠 카드에는 적용되지 않습니다.
  - 글로벌 빈도 제한은 사용자의 시간대에 따라 예약되며, 24시간 주기가 아닌 달력 일수로 계산됩니다. 예를 들어, 하루에 캠페인을 한 번 이상 보내지 않도록 빈도 제한 규칙을 설정하면, 사용자는 현지 시간대에서 오후 11시에 메시지를 받을 수 있으며, 한 시간 후에 또 다른 메시지를 받을 수 있습니다.

{% alert tip %}
캔버스 및 캠페인 문제 해결에 대한 추가 지원이 필요하면, 문제 발생 후 30일 이내에 Braze 지원팀에 문의하십시오. 진단 로그는 마지막 30일만 보유하고 있습니다.
{% endalert %}

## 이메일

#### 확인할 사항
- **고객 동의**: 초기 이메일을 보내기 전에 고객의 허가를 받는 것이 중요합니다. 자세한 내용은 [동의 및 주소 수집]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/consent_and_address_collection/) 및 [Braze 허용 사용 정책](https://www.braze.com/company/legal/aup)을 참조하십시오.
- **예상 볼륨**: 단일 IP에 대해 하루에 200만 이메일이 일반 권장 사항입니다. 이 볼륨이 [적절히 준비되었을 경우]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/ip_warming#ip-warming)입니다. 
  - 이보다 더 높은 볼륨을 지속적으로 보내려는 경우, 제공자가 이메일 수신을 제한하여 많은 소프트 바운스, 낮은 배달률 및 감소된 IP 평판을 초래하지 않도록 여러 IP 주소를 IP 풀로 묶어 사용하는 것을 고려하십시오. 
  - 짧은 시간 내에만 보내고자 하는 경우, 다양한 제공자가 메일을 얼마나 빨리 수락하는지 확인하여 보낼 IP 수를 평가하는 것을 권장합니다. 

#### 알아야 할 사항
- **전송 볼륨 요소**: IP의 전송 가능한 볼륨을 결정하는 몇 가지 요소는 다음과 같습니다:
  - 메일박스: 대형 이메일 제공업체는 단일 IP에서 하루에 수백만 개를 처리할 수 있지만, 더 작은 지역 메일박스 제공업체나 인프라가 작은 업체는 그 정도의 양을 처리할 수 없을 수 있습니다.
  - 발신자 평판: 발신자가 해당 볼륨으로 증가하고 각 메일박스나 도메인에서의 발신자 평판이 충분히 강하다면 단일 IP에서 하루에 더 많은 볼륨을 보낼 수 있습니다.
- **모범 사례**: Braze [이메일 모범 사례]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices)를 검토하고 배달 가능성 서비스에 대해 더 알고 싶다면 Braze 계정 팀에 문의하세요.

## 푸시

#### 확인할 사항
- [**가입/구독 및 푸시 활성화**]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/): 사용자가 Braze로부터 푸시 메시지를 받으려면, 그들의 구독 상태가 iOS의 경우 가입(Opted-in) 또는 Android의 경우 구독(Subscribed)이어야 하며 `Push Enabled = True`입니다. Android 13은 푸시 알림을 보내는 앱을 관리하는 방식에 큰 변화를 도입합니다. Braze [Android 13 SDK 업그레이드 가이드]({{site.baseurl}}/developer_guide/platforms/android/android_13/)는 새로운 Android 13 베타 버전이 출시됨에 따라 계속 업데이트될 것입니다.

#### 알아야 할 사항
- **웹 푸시**: Braze [웹 SDK 설정]({{site.baseurl}}/user_guide/message_building_by_channel/push/web)이 있다면, 사용자를 참여시키기 위해 웹 푸시를 활용하는 것을 고려하세요. 웹 푸시는 앱 푸시 알림이 휴대폰에서 작동하는 방식과 동일하게 작동합니다. 웹 푸시 작성에 대한 자세한 정보는 [푸시 알림 만들기]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message)를 확인하세요.
- **단일 앱 타겟팅**: 단일 앱과 그 사용자를 타겟팅하기 위해 [세분화의 차이점]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#targeting-a-singular-app)를 검토하세요.

## SMS

#### 확인할 사항
- **할당량 및 처리량**: 현재 귀하의 계정에 연결된 SMS 할당량(단기 코드, 장기 코드 및 유사한 것)이 무엇인지 이해하고 [그것이 제공하는 처리량이 얼마인지]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/short_and_long_codes/) 확인하여 원하는 시간에 전송할 수 있는 충분한 처리량이 있는지 확인하십시오.
- **SMS 복사에서 세그먼트 추정**: [SMS 세그먼트 계산기]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#things-to-keep-in-mind-as-you-create-your-copy)에서 SMS 복사를 테스트하십시오. SMS 세그먼트 수는 처리량 능력과 함께 고려해야 한다는 점을 명심하십시오. (청중 * SMS 세그먼트 = 필요한 처리량). [초과 요금 방지]({{site.baseurl}}/sms_faq/)에 대한 SMS FAQ를 참조하십시오.
- **SMS 법률 및 규정**: [SMS 법률, 규정 및 남용 방지]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/)를 검토하여 모든 관련 법률을 준수하여 SMS 서비스를 사용하고 있는지 확인하십시오. 전송하기 전에 법률 자문을 구해야 한다는 점을 확실히 하십시오.

#### 알아야 할 사항
- **SMS 메시지 기본 설정**: SMS 메시지는 일반적으로 발신자 풀의 단기 코드에서 전송되도록 기본 설정됩니다.
- **영숫자 발신자 ID**: 영숫자 발신자 ID를 사용하면 양방향 메시징이 더 이상 작동하지 않으며, 이제는 단방향만 가능합니다.
- **미국의 업데이트된 처리량**: 미국의 처리량은 미국 [A2P 10DLC 등록](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US)으로 변경되었습니다. 트래픽 혼잡 및 실제 배송 속도에 영향을 미칠 수 있는 통신사 문제와 같은 여러 요인으로 인해 우리는 계약상 어떤 전송 속도 SLA도 약속하지 않음을 유의하십시오.
- **구독 그룹**: Braze를 통해 SMS 캠페인을 시작하려면 구독 그룹을 선택해야 합니다. 또한 국제 [통신 준수 및 지침]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/)를 준수하기 위해 Braze는 선택된 구독 그룹에 [구독하지 않은 사용자]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#how-to-check-a-users-sms-subscription-group)에게 SMS를 절대 전송하지 않습니다.

## 왓츠앱

#### 알아야 할 사항

- [**모범 사례**]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_best_practices/): 추천하는 왓츠앱 모범 사례를 검토하세요.

## 배너

#### 확인할 사항
- **배너 크기:** 고정 크기 요소를 사용하여 배너를 만들고 편집기에서 테스트하세요.
- **우선순위:** 여러 배너를 출시하는 경우 각 배너가 표시되는 우선순위를 수동으로 설정할 수 있습니다.

#### 알아야 할 사항
- **액체 개인화:** 액체 개인화는 매번 새로 고침 요청 시 새로 고쳐집니다.
- **배치 및 배너 비율:** 각 배너 배치는 작업 공간에서 최대 10개의 캠페인에 사용할 수 있습니다.  
- **클릭 및 노출:** 배너의 클릭 및 노출은 SDK를 통해 자동으로 추적됩니다.
- **제한 사항:**  현재 다음 기능은 지원되지 않습니다: 캔버스 통합, API 트리거 및 작업 기반 캠페인, 연결된 콘텐츠, 프로모션 코드, 사용자 제어 해제 및 `catalog_items` [`:rerender` 태그]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/#using-liquid) 사용.
- **테스트:** 테스트 배너를 표시하려면 사용 중인 장치가 포그라운드 푸시 알림을 받을 수 있어야 합니다.
- **사용자 정의 HTML:** 사용자 정의 HTML을 사용하여 클릭 작업(링크 및 버튼 등)을 정의할 때 클릭을 기록하기 위해 [JS bridge]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages/#javascript-bridge)를 활용하십시오. 클릭 작업은 드래그 앤 드롭 편집기에서 미리 구축된 구성 요소를 사용할 때만 자동으로 기록됩니다.
- **배치 요청:** 한 번의 새로 고침 요청으로 SDK에 최대 10개의 배치를 반환할 수 있습니다. 각 배치는 사용자가 자격이 있는 가장 높은 우선 순위의 배너를 포함합니다.

## 콘텐츠 카드

#### 확인할 사항
- **콘텐츠 카드 크기**: 콘텐츠 카드 메시지 필드는 제목, 메시지, 이미지 URL, 링크 텍스트, 링크 URL 및 키-값 쌍의 바이트 크기 길이를 더하여 계산된 압축 전 크기가 2 KB로 제한됩니다. 이 크기를 초과하는 메시지는 전송되지 않습니다. 이는 이미지 크기를 포함하지 않고 이미지 URL의 길이를 포함합니다.
- **전송 후 복사 업데이트**: 카드가 전송된 후에는 동일한 카드에서 복사를 업데이트할 수 없습니다. 이 시나리오에 접근하는 방법을 이해하려면 [전송된 카드 업데이트]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/#updating-sent-cards)를 참조하십시오.

#### 알아야 할 사항
- **활성 콘텐츠 카드 캠페인 한도**: 최대 500개의 활성 콘텐츠 카드 캠페인을 가질 수 있습니다. 이 수치는 [카드 생성]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/) 옵션으로 전송된 콘텐츠 카드를 포함합니다.  
- [**보고 용어**]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/reporting/): 총 노출 수, 고유 노출 수 및 고유 수신자와 같은 용어를 검토하십시오. 정의가 때때로 혼란을 초래할 수 있습니다.
- **콘텐츠 카드 새로 고침**: 기본적으로 Braze는 세션 시작 시, 피드 아래로 스와이프(모바일) 시, 마지막 새로 고침이 1분 이상 경과한 경우 카드 보기가 열릴 때 콘텐츠 카드 요청을 새로 고칩니다.
- **콘텐츠 카드 캐싱**: 콘텐츠 카드 캐싱 옵션은 [안드로이드/파이어OS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/customization/custom_styling/#customizing-card-rendering-for-android) 및 [웹](https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#getcachedcontentcards) 문서에서 찾을 수 있습니다. 
- **빈도 제한**: 빈도 제한은 콘텐츠 카드에 적용되지 않습니다.
- **노출**: 노출은 일반적으로 카드가 보일 때 기록됩니다. 예를 들어, 콘텐츠 카드로 가득 찬 받은 편지함이 있는 경우, 사용자가 특정 콘텐츠 카드로 스크롤할 때까지 노출이 기록되지 않습니다. 웹, 안드로이드 및 iOS 플랫폼 간에는 몇 가지 뉘앙스가 있습니다.  

## 앱 내 메시지

#### 알아야 할 사항
- **앱 내 메시지 트리거**: 세션 시작 시, SDK는 모든 적격 앱 내 메시지가 장치로 전송되도록 요청하며, 이와 함께 트리거도 전송됩니다. 따라서 세션 중 이벤트를 수행하면 앱 내 메시지를 빠르고 신뢰성 있게 받을 수 있습니다.
- **전송 대 노출**: 앱 내 메시지의 경우, "전송됨"의 개념은 다른 사용 가능한 채널과 다릅니다. 앱 내 메시지를 보려면 사용자가 세션을 시작하고, 적격 청중에 속하며, 트리거를 수행해야 합니다. 이로 인해 우리는 "노출"을 추적합니다. 이는 더 명확하기 때문입니다.
- **트리거**: 기본적으로 앱 내 메시지는 SDK에 의해 기록된 이벤트로 트리거됩니다. 서버 전송 이벤트로 앱 내 메시지를 트리거하려면 [iOS]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=swift) 및 [안드로이드]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android)에 대한 가이드를 통해 이를 달성할 수 있습니다.
- [캔버스 앱 내 메시지]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas/#advancement-behavior-options): 이 메시지는 사용자가 캔버스 구성 요소에서 예약된 메시지를 받은 후 앱을 처음 열 때(세션 시작으로 트리거됨) 나타납니다.
- **연결된 콘텐츠 호출**: 연결된 콘텐츠를 사용하면 메시지에 동적 콘텐츠를 보낼 수 있습니다. 인앱 메시지와 같은 채널을 통해 메시지를 보낼 때, 이는 사용자 장치에 더 많은 동시 연결을 생성할 수 있습니다(메시지는 일괄 처리 대신 하나씩 전송됩니다). 이를 관리하기 위해, 우리는 메시지를 [비율 제한]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting)할 것을 권장합니다.
