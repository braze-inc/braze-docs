---
nav_title: 실행 기반 전달
article_title: 실행 기반 전달
page_order: 1
page_type: reference
description: "이 참조 문서에서는 사용자가 특정 이벤트를 완료한 후 캠페인을 트리거하여 전송하는 방법에 대해 설명합니다."
tool: Campaigns

---

# 액션 기반 전달

> 실행 기반 전달 캠페인 또는 이벤트 트리거 캠페인은 트랜잭션 또는 업적 기반 메시지에 매우 효과적입니다. 특정 날짜에 캠페인을 전송하는 대신 사용자가 특정 이벤트를 완료한 후에 캠페인을 전송하도록 트리거할 수 있습니다. 

## 트리거된 캠페인 설정하기

### 1단계: 트리거 이벤트 선택

트리거 이벤트를 선택합니다. 여기에는 다음 중 어느 것이든 포함될 수 있습니다:
- 구매하기
- 세션 시작하기
- 사용자 지정 이벤트 수행
- 캠페인의 기본 전환 이벤트 수행하기
- 사용자 프로필에 이메일 주소 추가하기
- 사용자 지정 속성 값 변경하기
- 구독 상태 업데이트하기
- 구독 그룹 상태 업데이트하기
- 다른 캠페인과 상호 작용하기
    - 인앱 메시지 보기
    - 인앱 메시지 클릭
    - 인앱 메시지 버튼 클릭
    - 이메일 클릭
    - 이메일에서 별칭 클릭
    - 캠페인 또는 캔버스 단계에서 클릭한 별칭
    - 이메일 열기
    - 이메일 열람(기계 열람)
    - 이메일 열람(기타 열람)
    - 푸시 알림 바로 열기
    - 푸시 알림 버튼 클릭
    - 푸시 스토리 페이지 클릭
    - 전환 이벤트 수행
    - 이메일 수신
    - SMS 수신
    - 단축 SMS 링크 클릭
    - 푸시 알림 받기
    - 웹훅 수신
    - 대조군에 등록됨
    - 콘텐츠 카드 보기
    - 콘텐츠 카드 클릭
    - 콘텐츠 카드 해제
- 뉴스피드 카드와 상호 작용하기([캠페인 커넥터][33] 참고)
- 위치 입력
- 다른 캠페인에 대한 예외 이벤트 수행
- 캔버스 단계와 상호 작용하기
- 지오펜스 트리거
- SMS 인바운드 메시지 보내기
- WhatsApp 인바운드 메시지 보내기

또한 Braze [커스텀 이벤트 속성정보][32]를 통해 트리거 이벤트를 추가로 필터링하여 커스텀 이벤트 및 인앱 구매에 대한 이벤트 속성을 커스텀할 수 있습니다. 이 기능을 사용하면 사용자 지정 이벤트의 특정 속성을 기반으로 메시지를 수신할 사용자를 더욱 맞춤화할 수 있으므로 캠페인 개인화를 강화하고 데이터를 더욱 정교하게 수집할 수 있습니다. 

예를 들어, '장바구니 값' 속성 필터로 추가 타겟팅되는 버려진 장바구니 사용자 지정 이벤트가 있는 캠페인이 있다고 가정해 보겠습니다. 이 캠페인은 장바구니에 100달러에서 200달러 상당의 상품을 남긴 사용자에게만 도달합니다. 

![][34]

{% alert note %}
캠페인의 세그먼트가 신규 사용자에게 적용되는 경우 트리거 이벤트 "세션 시작"은 사용자의 첫 번째 앱 실행이 될 수 있습니다. (예를 들어, 세그먼트가 세션이 없는 사용자로 구성된 경우).
{% endalert %}

특정 사용자 세그먼트에 트리거된 캠페인을 보낼 수 있으므로 해당 세그먼트에 속하지 않은 사용자는 트리거 이벤트를 완료하더라도 캠페인을 받지 못합니다. 세그먼트 자격을 갖추었음에도 불구하고 사용자가 캠페인을 받지 못하는 경우 [사용자가 트리거된 캠페인을 받지 못한 이유][49] 섹션을 참조하세요.

사용자가 프로필에 이메일 주소를 추가할 때의 트리거 이벤트와 관련하여 다음 규칙이 적용됩니다:

- 트리거 이벤트는 사용자 프로필 속성이 업데이트된 후에 발생합니다. 즉, 캠페인의 세그먼트 및 필터에 대한 평가는 속성 업데이트 후에 이루어집니다. "이메일 주소 일치 gmail.com"와 같은 필터를 설정하여 Gmail 사용자에게만 전송하고 이메일 주소를 추가하는 즉시 실행되는 트리거 캠페인을 만들 수 있기 때문에 유용합니다.
- 트리거 이벤트는 이메일 주소가 사용자 프로필에 추가되면 실행됩니다. 동일한 이메일 주소로 생성한 사용자 프로필이 여러 개 있는 경우 각 사용자 프로필에 대해 한 번씩 캠페인이 여러 번 실행될 수 있습니다.

또한 트리거된 인앱 메시지는 여전히 인앱 메시지 전달 규칙을 준수하며 앱 세션이 시작될 때 표시됩니다.

![][17]

### 2단계: 지연 길이 선택

트리거 기준이 충족된 후 캠페인을 보내기 전에 대기할 기간을 선택합니다. 선택한 지연 길이가 메시지 전송 기간보다 길면 캠페인을 수신하는 사용자가 없습니다. 

또한 캠페인이 시작된 후 트리거 이벤트를 완료한 사용자는 지연 시간이 지난 후 가장 먼저 메시지를 받기 시작합니다. 캠페인이 시작되기 전에 트리거 이벤트를 완료한 사용자는 캠페인을 받을 자격이 없습니다.

![][19]

또한 향후 특정 요일("다음날"을 선택한 다음 하루를 선택)이나 특정 일수("다음날"을 선택)에 캠페인을 보내도록 선택할 수도 있습니다. 또는 배달 시간을 수동으로 선택하는 대신 [지능형 타이밍][8] 기능을 사용하여 메시지를 보낼 수도 있습니다.

![][41]
![][50]

### 3단계: 예외 이벤트 선택

사용자가 이 캠페인을 받을 자격을 박탈할 예외 이벤트를 선택합니다. 트리거된 메시지가 시간 지연 후에 전송되는 경우에만 이 작업을 수행할 수 있습니다. [예외 이벤트]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria/#exception-events)는 구매하기, 세션 시작하기, 캠페인의 지정된 [전환 이벤트][18] 수행하기, 또는 커스텀 이벤트 수행하기일 수 있습니다. 사용자가 트리거 이벤트를 완료했지만 시간 지연으로 인해 메시지가 전송되기 전에 예외 이벤트를 완료하면 캠페인을 받지 못합니다. 예외 이벤트로 인해 캠페인을 받지 못한 사용자는 사용자가 [재대상자]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/reeligibility/)로 지정하지 않더라도 다음에 트리거 이벤트를 완료할 때 자동으로 캠페인을 받을 수 있습니다.

![][20]

예외 이벤트를 사용하는 방법에 대한 자세한 내용은 [사용 사례]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/#use-cases) 섹션에서 확인할 수 있습니다.

> 예외 이벤트와 일치하는 트리거 이벤트가 포함된 캠페인을 전송하면 Braze는 캠페인을 취소하고 예외 이벤트의 메시지 전송 시간에 따라 자동으로 새 캠페인을 다시 예약합니다. 예를 들어 첫 번째 트리거 이벤트가 5분에 시작되고 예외 이벤트가 10분에 시작되는 경우 예외 이벤트의 10분을 공식 캠페인의 메시지 전달 시간으로 사용합니다.

{% alert note %}
캠페인의 트리거 이벤트와 예외 이벤트를 모두 "세션 시작"으로 설정할 수 없습니다. 그러나 이 옵션 외에 다른 커스텀 이벤트를 언제든지 선택할 수 있습니다.
{% endalert %}

### 4단계: 기간 지정

시작 시간과 종료 시간(선택 사항)을 지정하여 캠페인 기간을 지정합니다.

![][21]

사용자가 지정된 기간 동안 트리거 이벤트를 완료했지만 예정된 지연으로 인해 해당 기간 외에는 메시지를 받을 자격이 없는 경우 캠페인을 받지 못합니다. 따라서 메시지 시간보다 긴 시간 지연을 설정하면 캠페인을 수신할 사용자가 없습니다. 또한 사용자의 [현지 시간]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/scheduled_delivery/#local-time-zone-campaigns)대로 메시지를 보내도록 선택할 수 있습니다.

### 5단계: 기간 선택

사용자가 하루 중 특정 시간대에 캠페인을 수신할지 여부를 선택합니다. 메시지에 시간 프레임을 지정했는데 사용자가 이 시간 프레임 전에 트리거 이벤트를 완료하거나 메시지 지연으로 인해 시간 프레임을 놓친 경우 기본적으로 사용자는 메시지를 받지 못합니다.

![][27]

사용자가 기간 내에 트리거 이벤트를 완료했지만 메시지 지연으로 인해 사용자가 기간에서 벗어난 경우 다음 확인란을 선택하여 해당 사용자가 캠페인을 계속 받을 수 있도록 할 수 있습니다.

![][31]

사용자가 기간을 놓쳐서 메시지를 받지 못한 경우에는 사용자가 [다시 자격]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/reeligibility/)을 얻도록 선택하지 않았더라도 다음에 트리거 이벤트를 완료할 때 메시지를 받을 수 있는 자격을 얻게 됩니다. 사용자가 다시 자격을 갖추도록 선택한 경우, 지정된 기간 동안 자격을 갖추었다고 가정하여 사용자가 트리거 이벤트를 완료할 때마다 캠페인을 받을 수 있습니다.

캠페인에 특정 기간도 지정한 경우 사용자는 해당 기간과 하루 중 특정 시간대에 자격을 갖추어야 메시지를 받을 수 있습니다.

### 6단계: 재적격 여부 결정

사용자가 캠페인에 [재적격][24]이 될 수 있는지 여부를 결정합니다. 사용자가 다시 캠페인을 받을 수 있도록 허용하는 경우, 사용자가 캠페인을 다시 받을 수 있는 기간을 지정할 수 있습니다. 이렇게 하면 트리거된 캠페인이 "스팸성"이 되는 것을 방지할 수 있습니다.

![][28]

## 사용 사례

트리거 캠페인은 트랜잭션 또는 업적 기반 메시지에 매우 효과적입니다.

거래 캠페인에는 사용자가 구매를 완료하거나 장바구니에 상품을 추가한 후 전송되는 메시지가 포함됩니다. 후자의 경우는 예외 이벤트의 혜택을 받을 수 있는 캠페인의 좋은 예입니다. 사용자가 구매하지 않은 장바구니에 있는 상품을 상기시키는 캠페인이라고 가정해 보겠습니다. 이 경우 예외 이벤트는 사용자가 카트에서 제품을 구매하는 경우입니다. 업적 기반 캠페인의 경우, 사용자가 전환을 완료하거나 게임 레벨을 달성한 후 5분 후에 메시지를 보낼 수 있습니다.

또한 환영 캠페인을 만들 때 사용자가 계정을 등록하거나 설정한 후에 메시지를 보내도록 트리거할 수 있습니다. 등록 후 서로 다른 날짜에 메시지를 보내도록 시차를 두면 철저한 온보딩 프로세스를 만들 수 있습니다.

## 사용자가 트리거된 캠페인을 받지 못한 이유는 무엇인가요?

트리거 이벤트를 완료한 사용자가 캠페인을 수신하지 못하게 됩니다.

- 사용자가 시간 지연이 완전히 경과하기 전에 예외 이벤트를 완료했습니다.
- Liquid [`abort_message` 로직]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages)이 사용되었고 `abort_message` 로직 또는 규칙에 따라 메시지가 중단되었습니다.
- 시간 지연으로 인해 사용자는 기간 종료 후 캠페인을 받을 수 있는 자격을 얻게 됩니다.
- 시간 지연으로 인해 사용자는 지정된 시간 외에는 캠페인을 받을 수 있는 자격을 얻지 못했습니다.
- 사용자가 이미 캠페인을 받았으며 사용자는 다시 캠페인에 참여할 수 없습니다.
- 사용자는 캠페인을 다시 받을 수 있지만, 일정 기간이 지난 후에만 다시 트리거할 수 있으며 해당 기간이 아직 경과하지 않았습니다.

이벤트 발생 시점에 기록된 사용자 데이터로 트리거된 캠페인을 [세그먼트화하면]({{site.baseurl}}/user_guide/engagement_tools/segments/) [경쟁 조건이]({{site.baseurl}}/help/best_practices/race_conditions/#race-conditions) 발생할 수 있습니다. 이는 캠페인이 세분화되는 사용자 속성이 변경되었지만 캠페인이 전송될 때 사용자에 대한 변경 사항이 처리되지 않은 경우에 발생합니다. 캠페인은 가입 시 세그먼트 멤버십을 확인하기 때문에 사용자가 캠페인을 받지 못할 수 있습니다.

예를 들어 방금 등록한 남성 사용자에게 이벤트 트리거 캠페인을 보내고 싶다고 가정해 보겠습니다. 사용자가 등록하면 커스텀 이벤트 `registration`을 기록하는 동시에 사용자의 `gender` 속성을 설정합니다. Braze가 사용자의 성별을 처리하기 전에 이벤트가 트리거되어 캠페인을 받지 못할 수도 있습니다.

모범 사례로, 이벤트 전에 캠페인이 세분화되는 속성이 Braze 서버로 플러시되는지 확인하세요. 이것이 불가능하다면 [사용자 지정 이벤트 속성][48] ]을 사용하여 관련 사용자 속성을 이벤트에 첨부하고 세분화 필터 대신 특정 이벤트 속성에 대한 속성 필터를 적용하는 것이 배달을 보장하는 가장 좋은 방법입니다. 예를 들어, 커스텀 이벤트 `registration`에 `gender` 속성정보를 추가하면 캠페인이 트리거될 때 필요한 데이터를 Braze가 확보할 수 있습니다.

또한 캠페인이 액션 기반이고 지연이 있는 경우, **전송 시 세그먼트 멤버십 재평가** 옵션을 선택하여 메시지를 전송할 때 사용자가 여전히 타겟 오디언스에 속해 있는지 확인할 수 있습니다.

특정 사용자 지정 이벤트에 의해 캠페인이 트리거되고 세그먼트를 대상 그룹으로 선택한 경우, 사용자가 세그먼트에 포함되려면 동일한 사용자 지정 이벤트를 수행해야 합니다. 즉, 실행 기반 캠페인이 트리거되기 전에 사용자가 오디언스의 일부가 되어야 합니다. 트리거된 캠페인의 일반적인 워크플로우는 다음과 같습니다:

1. **오디언스와 함께하기:** 사용자가 사용자 지정 이벤트를 수행하면 캠페인의 타겟 오디언스에 추가됩니다.
2. **이메일 트리거:** 이메일이 전송되기 전에 사용자가 오디언스에 포함되어 있어야 하므로 이메일을 트리거하려면 커스텀 이벤트를 다시 수행해야 합니다.

모든 사용자를 포함하도록 대상 그룹을 변경하거나 이벤트를 수행할 것으로 예상되는 사용자가 이미 캠페인의 대상 그룹에 포함되어 있는지 확인하여 메시지를 트리거하는 것이 좋습니다.

![][51]

[5]: #local-time-zone-campaigns
[8]: {{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/
[17]: {% image_buster /assets/img_archive/schedule_triggered1.png %}
[18]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-events
[19]: {% image_buster /assets/img_archive/schedule_triggered22.png %}
[20]: {% image_buster /assets/img_archive/schedule_triggered32.png %}
[21]: {% image_buster /assets/img_archive/schedule_triggered43.png %}
[22]: \#use-cases-2
[24]: {% image_buster /assets/img_archive/ReEligible.png %}
[27]: {% image_buster /assets/img_archive/schedule_triggered5.png %}
[28]: {% image_buster /assets/img_archive/schedule_triggered6.png %}
[29]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/in-app_message_behavior/#in-app-message-delivery-rules
[31]: {% image_buster /assets/img_archive/schedule_triggered_next_available.png %}
[32]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/
[33]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/campaign_connector/#campaign-connector
[34]: {% image_buster /assets/img_archive/customEventProperties.png %}
[41]: {% image_buster /assets/img_archive/schedule_triggered7.png %}
[47]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/#why-did-a-user-not-receive-my-triggered-campaign
[48]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties
[49]: {{site.baseurl}}/help/help_articles/campaigns_and_canvas/not_triggering/
[50]: {% image_buster /assets/img_archive/schedule_triggered8.png %}
[51]: {% image_buster /assets/img_archive/reevaluate_segment_membership.png %}
