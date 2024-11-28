---
nav_title: 캔버스 만들기
article_title: 캔버스 만들기
page_order: 0
page_type: reference
description: "이 참조 문서에서는 캔버스를 만들고, 유지 관리하고, 테스트하는 데 필요한 단계를 다룹니다."
tool: Canvas
search_rank: 1
---

# 캔버스 만들기

> 이 참조 문서에서는 캔버스를 만들고, 유지 관리하고, 테스트하는 데 필요한 단계를 다룹니다. 이 가이드를 따르거나 [캔버스 Braze 학습 과정](https://learning.braze.com/quick-overview-canvas-setup)을 확인하세요.

{% alert important %}
2023년 2월 28일부터는 더 이상 기존 캔버스 환경을 사용하여 캔버스를 만들거나 복제할 수 없습니다. Braze는 기존 캔버스 환경을 사용하는 고객은 캔버스 흐름으로 전환할 것을 권장합니다. 향상된 편집 경험을 통해 캔버스를 더 잘 구축하고 관리할 수 있습니다. [캔버스를 캔버스 플로우에 복제하는 방법]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/)에 대해 자세히 알아보세요.
{% endalert %}

## 1단계: 새 캔버스 만들기 

**메시징** > **캔버스**로 이동한 다음 **캔버스 만들기**를 선택합니다.

{% alert note %}
[이전 탐색]({{site.baseurl}}/navigation)을 사용하는 경우 **캔버스**를 **인게이지먼트** 아래에서 찾을 수 있습니다.
{% endalert %}

## 2단계: 캔버스를 설정하세요

캔버스 빌더는 캔버스 설정 과정을 단계별로 안내합니다—이름 지정부터 전환 이벤트 설정 및 적절한 사용자를 고객 여정에 포함시키는 모든 것을 포함합니다. 각 빌더 단계에서 조정할 수 있는 설정을 보려면 다음 탭을 각각 선택하세요.

{% tabs local %}
  {% tab 기본 %}
    여기에서 캔버스의 기본을 설정합니다:
    \- 캔버스 이름 지정
    \- 팀 추가
    \- 태그 추가
    \- 전환 이벤트를 할당하고 이벤트 유형과 마감일 선택

    Learn more about the [Basics step](#step-2a-set-up-your-canvas-basics).
  {% endtab %}
  {% tab 진입 스케줄 %}
    여기에서 사용자가 캔버스에 어떻게 들어갈지 결정합니다:
    \- 스케줄: 이것은 시간 기반 캔버스 항목입니다
    \- 액션 기반: 사용자가 정의된 작업을 수행한 후에 캔버스에 들어갑니다
    \- API 트리거됨: API 요청을 사용하여 사용자를 캔버스에 입력하십시오

    Learn more about the [Entry Schedule step](#step-2b-determine-your-canvas-entry-schedule).
  {% endtab %}
  {% tab 타겟 오디언스 %}
    여기에서 대상 오디언스를 선택합니다:
    \- 세그먼트와 필터를 추가하여 오디언스를 만드세요
    \- 캔버스 재진입 및 진입 한도를 미세 조정
    \- 타겟 오디언스의 요약을 확인하세요

    Learn more about the [Target Audience step](#step-2c-set-your-target-entry-audience).
  {% endtab %}
  {% tab 설정 보내기 %}
    여기에서 캔버스 전송 설정을 선택합니다.
    \- 구독 설정 선택
    \- 캔버스 메시지에 대한 사용량 제한 설정
    \- 방해금지 시간을 활성화하고 설정합니다

    Learn more about the [Send Settings step](#step-2d-select-your-send-settings).
  {% endtab %}
  {% tab 캔버스 구축 %}
    여기에서 캔버스를 구축합니다.

    Learn how to [build your Canvas](#step-3-build-your-canvas) using the Canvas builder.
  {% endtab %}
  {% tab 요약 %}
    여기에서 캔버스 세부 정보를 요약한 내용을 찾을 수 있습니다. [캔버스 승인 워크플로우]({{site.baseurl}}/canvas_approval/)가 켜져 있으면 시작하기 전에 나열된 캔버스 세부 정보를 승인할 수 있습니다.

  {% endtab %}
{% endtabs %}

### 2a 단계: 캔버스 기본 사항부터 시작하세요

여기에서 캔버스의 이름을 지정하고 [Teams]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/#teams)을(를) 할당하며 [태그]({{site.baseurl}}/user_guide/administrative/app_settings/tags/#tags)를 만들거나 추가합니다. 캔버스에 대한 전환 이벤트를 할당할 수도 있습니다.

{% alert tip %}
캔버스에 태그를 지정하여 쉽게 찾고 이를 이용하여 보고서를 작성할 수 있습니다. 예를 들어, [보고서 빌더]({{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/)를 사용할 때 특정 태그로 필터링할 수 있습니다.
{% endalert %}

![][53]

#### 전환 이벤트 선택

전환 이벤트 유형을 선택한 다음 기록할 전환을 선택하세요. 이 [전환 이벤트]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/)는 귀하의 캔버스 효율성을 측정할 것입니다. 

![구매하기 전환 이벤트 유형의 주요 전환 이벤트 A는 3일의 전환 기한 내에 구매를 한 사용자의 대화를 기록합니다.][52]

캔버스에 여러 변형 또는 대조군이 있는 경우, Braze는 이 전환 이벤트를 사용하여 이 전환 목표를 달성하기 위한 최상의 변형을 결정합니다. 동일한 논리를 사용하여 여러 전환 이벤트를 생성할 수 있습니다.

### 2b 단계: 캔버스 진입 스케줄 결정

사용자가 캔버스에 들어갈 수 있는 세 가지 방법 중 하나를 선택할 수 있습니다. 

#### 진입 스케줄 유형

{% tabs local %}
  {% tab 예정된 전달 %}
    예약된 전달을 통해 사용자는 캠페인을 예약하는 방식과 유사하게 시간 스케줄에 따라 입력하게 됩니다. 캔버스가 출시되자마자 사용자를 등록하거나, 나중에 여정에 등록하거나, 매일, 매주 또는 매월 반복적으로 등록할 수 있습니다. 

    In this example, based on the time-based options, users will enter this Canvas every Tuesday at 12 pm in their local time zone every week, beginning November 14, 2023 until December 31, 2023.

    ![]({% image_buster /assets/img_archive/Canvas_Scheduled_Delivery.png %})
  {% endtab %}
  {% tab 실행 기반 전달 %}
    실행 기반 전달을 통해 사용자는 특정 작업을 수행할 때 캔버스에 들어가 메시지를 받기 시작합니다. 예를 들어, 앱을 열거나 구매를 하거나 커스텀 이벤트를 트리거하는 경우입니다.

    You can control other aspects of the Canvas behavior from the **Entry Audience** window, including rules for re-eligibility and frequency capping settings. Note that action-based delivery is unavailable for Canvas components with in-app messages.

    ![An example of action-based delivery. Users will enter the Canvas if they make a purchase with an entry window beginning at 1:30 pm on June 10, 2023.]({% image_buster /assets/img_archive/Canvas_Action_Based_Delivery.png %})

  {% endtab %}
  {% tab API 트리거 전달 %}
    API로 트리거된 전달을 통해 사용자는 캔버스에 들어가 [`/canvas/trigger/send` 엔드포인트]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)를 통해 API를 사용하여 추가된 후 메시지를 받기 시작합니다. 대시보드에서 이 작업을 수행하는 예제 cURL 요청을 찾을 수 있으며 [캔버스 항목 속성 개체]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/)를 사용하여 [`canvas_entry_properties`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)를 선택적으로 할당할 수 있습니다. 

    ![An example of API-triggered delivery with a Canvas ID and an example of a cURL request.]({% image_buster /assets/img_archive/Canvas_API_Triggered_Delivery.png %})

    You can use the following endpoints for API-triggered delivery:
    - [POST: Send Canvas Messages via API-Triggered Delivery]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)
    - [POST: Schedule API-Triggered Canvases]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/)
    - [POST: Update Scheduled API-Triggered Canvases]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/)

  {% endtab %}
{% endtabs %}

전달 방법을 선택한 후 설정을 사용 사례에 맞게 조정한 다음 대상 오디언스를 설정하세요.

{% details 원래 편집기를 사용하여 캔버스의 동작 중복 제거 %}
재자격 부여 기간이 캔버스의 최대 기간보다 짧을 경우, 사용자는 다시 들어가서 둘 이상의 구성 요소의 메시지를 받을 수 있습니다. 사용자의 재진입이 과거 진입과 동일한 구성 요소인 극단적인 경우, Braze는 해당 구성 요소의 메시지를 중복 제거합니다. 

사용자가 캔버스에 다시 들어가 이전에 들어갔던 동일한 구성 요소에 도달하고 각 항목에 대해 인앱 메시지를 받을 자격이 있는 경우, 사용자가 세션을 두 번 다시 열면 인앱 메시지 우선 순위에 따라 메시지를 두 번 받게 됩니다.
{% enddetails %}

### 2c 단계: 타겟 진입 오디언스를 설정하세요

캔버스의 대상 오디언스를 **대상 오디언스** 단계에서 설정할 수 있습니다. 정의된 기준에 맞는 사용자만 여정을 시작할 수 있으며, 이는 Braze가 사용자가 캔버스 여정에 들어가기 전에 타겟 오디언스의 적격성을 먼저 평가함을 의미합니다. 예를 들어, 새로운 사용자를 타겟으로 하고 싶다면, 일주일 이내에 처음으로 세그먼트를 사용한 사용자를 선택할 수 있습니다.

**진입 제어**에서 캔버스가 실행될 때마다 사용자의 수를 제한할 수 있습니다. API 트리거 기반 및 작업 기반 캔버스의 경우 이 제한은 매 UTC 시간마다 발생합니다. 

{% alert warning %}
행동 기반 캠페인 또는 캔버스를 오디언스 필터(예: 변경된 속성 또는 커스텀 이벤트 수행)와 동일한 트리거로 구성하지 마세요. 경합 조건이 발생할 수 있으며, 사용자가 트리거 이벤트를 수행할 때 오디언스에 속하지 않으면 캠페인을 받거나 캔버스에 들어가지 못하게 됩니다.  
{% endalert %}

#### 오디언스를 테스트 중

세그먼트와 필터를 타겟 오디언스에 추가한 후, [사용자를 조회하여]({{site.baseurl}}/user_guide/engagement_tools/segments/user_lookup/) 오디언스 기준에 맞는지 확인함으로써 오디언스가 예상대로 설정되었는지 테스트할 수 있습니다.

![]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:50%;"}

#### 항목 컨트롤 선택

진입 제어는 사용자가 캔버스에 다시 입장할 수 있는지 여부를 결정합니다. 또한 이 캔버스에 들어올 수 있는 사람의 수를 제한할 수 있습니다. 예를 들어, **이 캔버스에 잠재적으로 들어갈 수 있는 최대 사용자 수** 필드를 1,000명으로 설정하고 **캔버스가 예약될 때마다 제한** 체크박스를 선택하면, 캔버스는 하루에 1,000명의 사용자에게 전송됩니다.

![]({% image_buster /assets/img_archive/entry_controls.png %}){: style="max-width:50%;"}

Braze는 IP 워밍을 위해 **캔버스가 예약될 때마다 제한 기능**을 사용하는 것을 권장하지 않습니다. 이는 발송량 증가로 이어질 수 있습니다.

#### 종료 기준 설정

[종료 기준]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria)을 설정하면 캔버스에서 나가고자 하는 사용자를 결정할 수 있습니다. 사용자가 예외 이벤트를 수행하거나 세그먼트 및 필터와 일치하는 경우 더 이상 메시지를 받지 않습니다.

#### 대상 인구 계산

**타겟 인구** 섹션에서는 선택한 세그먼트 및 추가 필터 등 오디언스에 대한 요약과 메시징 채널당 도달 가능한 사용자 수에 대한 분석을 볼 수 있습니다. 기본 추정치 대신 타겟 오디언스에서 도달 가능한 정확한 사용자 수를 계산하려면 [정확한 통계 계산을]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#calculating-exact-statistics) 선택합니다.

참고:

- 정확한 통계를 계산하는 데 몇 분이 걸릴 수 있습니다. 이 함수는 필터 또는 필터 그룹 수준이 아닌 세그먼트 수준에서만 정확한 통계를 계산합니다.
- 큰 세그먼트의 경우, 정확한 통계를 계산할 때에도 약간의 변동이 있는 것이 정상입니다. 이 기능의 정확도는 99.999% 이상일 것으로 예상됩니다.

타겟 사용자의 평균 평생 수익과 같은 추가 통계를 보려면 **추가 통계** 보기를 선택합니다.

![정확한 통계를 집계하는 옵션이 있는 타겟 인구 분석.][2]

### 2d 단계: 전송 설정을 선택하세요

**전송 설정**을 선택하여 구독 설정을 편집하고, 사용량 제한조치를 켜고, 방해금지 시간을 켭니다. [rate limiting][6b] 또는 [최대 게재빈도 설정][6c]을 켜면 사용자에게 가해지는 마케팅 압력을 완화하고 과도한 메시징을 방지할 수 있습니다.

캔버스가 이메일 및 푸시 채널을 타겟팅하는 경우, 명시적으로 옵트인한 사용자만 메시지를 받도록 캔버스를 제한하는 것이 좋습니다(구독 또는 구독 취소한 사용자는 제외). 예를 들어, 옵트인 상태가 다른 세 명의 사용자가 있다고 가정해 보겠습니다:

- **User A**는 이메일을 구독하고 푸시를 활성화했습니다. 이 사용자는 이메일을 수신하지 않지만 푸시를 받게 됩니다.
- **사용자 B**는 이메일 수신에 옵트인했지만 푸시를 사용하도록 설정되어 있지 않습니다. 이 사용자는 이메일을 받지만 푸시는 받지 않습니다.
- **사용자 C는** 이메일 수신에 동의하고 푸시를 사용하도록 설정되어 있습니다. 이 사용자는 이메일과 푸시를 모두 받을 것입니다.

이렇게 하려면 **구독 설정**을 설정하여 이 캔버스를 "옵트인한 사용자에게만" 보내도록 하세요. 이 옵션은 옵트인한 사용자만 이메일을 받도록 보장하며, Braze는 기본값으로 푸시가 활성화된 사용자에게만 푸시를 보냅니다. 

이 구독 설정은 단계별로 적용되므로 항목 오디언스에는 영향을 미치지 않습니다. 따라서 이 설정은 사용자가 각 캔버스 단계를 받을 자격이 있는지 평가하는 데 사용됩니다.

{% alert important %}
이 구성에서는 **대상 사용자** 단계에서 오디언스를 단일 채널(예: `Push Enabled = True` 또는 `Email Subscription = Opted-In`)로 제한하는 필터를 포함하지 마십시오.
{% endalert %}

원하는 경우 캔버스에 대한 방해금지 시간(메시지가 전송되지 않는 시간)을 지정하세요. **방해금지 시간 활성화**을(를) **보내기 설정**에서 확인하세요. 그런 다음 사용자의 로컬 시간에 방해금지 시간을 선택하고 메시지가 해당 방해금지 시간 내에 트리거될 경우 수행할 작업을 선택합니다.

![][50]

## 3단계: 캔버스 비드

{% alert tip %}
[브레이즈 캔버스 템플릿을]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_templates/#available-braze-templates) 사용하여 시간을 절약하고 캔버스 제작을 간소화하세요! 사전 구축된 템플릿 라이브러리를 검색하여 사용 사례에 맞는 템플릿을 찾고 특정 요구 사항에 맞게 사용자 지정하세요.
{% endalert %}

### 배리언트 추가

![][11]{: style="float:right;max-width:35%;margin-left:15px;"}

**배리언트 추가**를 선택한 다음 캔버스에 새 배리언트를 추가합니다. 변형은 사용자가 거칠 여정을 나타내며 여러 단계와 분기를 포함할 수 있습니다.

추가 변형을 추가하려면 <i class="fas fa-plus-circle"></i> 플러스 버튼을 선택하십시오. 새 변형을 추가하면 사용자가 그들 사이에 어떻게 분배될지를 조정할 수 있으므로 다양한 참여 전략의 효율성을 비교 분석할 수 있습니다.

![][12]

{% alert tip %}
기본값으로, 사용자가 캔버스에 들어갈 때 캔버스 배리언트 할당이 잠기게 됩니다. 즉, 사용자가 처음으로 배리언트에 들어가면, 그 후로 캔버스에 다시 들어갈 때마다 그 배리언트가 유지됩니다. 하지만 이러한 행동을 피할 수 있는 방법들이 있습니다. <br><br>이를 위해 Liquid을 사용하여 난수 생성기를 만들고 각 사용자의 캔버스 항목 시작 시 실행하여 값을 커스텀 속성으로 저장한 다음 해당 속성을 사용하여 사용자를 무작위로 나눌 수 있습니다.

{% details 단계를 보려면 확장하세요 %}

1. 랜덤 숫자를 저장할 커스텀 속성을 만드세요. 쉽게 찾을 수 있는 "lottery_number" 또는 "random_assignment"와 같은 이름을 지정하세요. 속성을 [대시보드]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/managing_custom_data/)에서 생성하거나 API 호출을 통해 [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)에서 생성할 수 있습니다.<br><br>
2. 캔버스의 시작 부분에서 웹훅 캠페인을 만드세요. 이 캠페인은 사용자가 무작위 숫자를 생성하고 이를 커스텀 속성으로 저장하는 매개체가 될 것입니다. [웹훅 생성]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#step-1-set-up-a-webhook)을 참조하십시오. URL을 우리 `/users/track` 엔드포인트로 설정하십시오.<br><br>
3. 무작위 숫자 생성기를 만드세요. 사용자의 고유한 입장 시간을 활용하여 무작위 숫자를 생성하는 [여기에 설명된](https://community.shopify.com/c/technical-q-a/is-there-any-way-to-generate-random-number-with-liquid-shopify/m-p/1595486) 코드를 사용할 수 있습니다. 결과 숫자를 Liquid 변수로 설정하여 웹훅 캠페인 내에서 사용하세요.<br><br>
4. 웹훅 캠페인에서 `/users/track` 호출을 포맷하여 1단계에서 생성한 커스텀 속성을 현재 사용자의 프로필에 생성한 임의의 숫자로 설정하세요. 이 단계가 실행되면 사용자가 캠페인에 들어올 때마다 변경되는 무작위 숫자를 성공적으로 만들 수 있습니다.<br><br>
5. 캔버스의 가지를 임의로 선택된 변형에 의해 나뉘는 대신 오디언스 규칙에 따라 나뉘도록 조정하십시오. 각 브랜치의 오디언스 규칙에서 커스텀 속성에 따라 오디언스 필터를 설정하세요. <br><br>예를 들어, 한 브랜치는 "lottery_number가 3보다 작음"을 오디언스 필터로 가질 수 있고, 다른 분기는 "lottery_number가 3보다 크고 6보다 작음"을 오디언스 필터로 가질 수 있습니다.

{% enddetails %}
{% endalert %}

### 단계 추가

캔버스 워크플로우에 더 많은 단계를 추가하려면 **구성 요소** 사이드바에서 구성 요소를 드래그 앤 드롭하세요. 또는, 팝오버 메뉴로 구성 요소를 추가하려면 <i class="fas fa-plus-circle"></i> 플러스 버튼을 선택하세요.

{% alert tip %}
단계를 추가하기 시작하면 세부 사항에 집중하거나 전체 사용자 여정을 파악하기 위해 확대/축소 수준을 변경할 수 있습니다. <kbd>Shift</kbd> + <kbd>+</kbd>를 사용하여 확대하거나 <kbd>Shift</kbd> + <kbd>-</kbd>를 사용하여 축소합니다
{% endalert %}

![]({% image_buster /assets/img_archive/add_components_flow.png %})

{% alert warning %}
캔버스 흐름을 사용하여 만든 캔버스는 최대 200단계를 포함할 수 있습니다. 캔버스가 200 단계를 초과하면 로딩 문제가 발생합니다.
{% endalert %}

#### 최대 지속 시간

캔버스 여정이 단계별로 증가함에 따라 사용자가 이 캔버스를 완료하는 데 걸릴 수 있는 최대 기간은 가장 긴 시간입니다. 이는 가장 긴 경로에 대해 각 배리언트의 각 단계에 대한 지연 및 트리거 창을 추가하여 계산됩니다. 예를 들어, 캔버스에 3일의 지연이 있는 지연 단계와 메시지 단계가 있는 경우 캔버스의 최대 시간은 3일입니다.

### 단계 편집

사용자 여정의 단계를 편집하시겠습니까? 캔버스 워크플로에 따라 이를 수행하는 방법을 확인하세요!

캔버스 플로우 워크플로우의 모든 단계를 편집하려면 구성 요소를 선택하면 됩니다. 예를 들어, 워크플로우에서 첫 번째 단계인 [Delay]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) 구성 요소를 특정 날짜로 편집하고자 하는 경우입니다. 단계를 선택하여 설정을 보고 지연 시간을 3월 1일로 조정하십시오. 이는 3월 1일에 사용자가 캔버스의 다음 단계로 이동함을 의미합니다.

![]({% image_buster /assets/img_archive/edit_delay_flow.png %})

또는 **작업 설정**을(를) 빠르게 편집하고 조정하여 [작업 경로]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) 단계에서 사용자를 일정 시간 동안 유지할 수 있습니다. 이 평가 기간 동안의 행동을 기반으로 다음 경로를 우선시합니다.

![]({% image_buster /assets/img_archive/action_paths_flow.png %})

캔버스의 가벼운 구성 요소는 간단한 편집 경험을 제공하므로 캔버스의 세부 사항을 조정하는 것이 더 쉬워집니다. 

#### 캔버스의 메시지

캔버스 구성 요소에서 메시지를 편집하여 특정 단계가 보낼 메시지를 제어합니다. 캔버스는 이메일, 모바일 및 웹 푸시 메시지와 웹훅을 보내 다른 시스템과 통합할 수 있습니다. 캠페인과 유사하게, 특정 [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/) 템플릿을 사용하여 메시지를 개인화할 수 있습니다.

{% alert tip %}
알고 계셨나요? 메시지 및 링크 템플릿에 캔버스 구성 요소 이름을 포함할 수 있습니다?<br>
캔버스에서 현재 캔버스스 구성 요소 이름을 표시하려면 `campaign.${name}` Liquid 태그를 사용하세요.
{% endalert %}

메시지 구성 요소는 사용자에게 전송된 메시지를 관리합니다. **메시징 채널**을 선택하고 **전달 설정**을 조정하여 캔버스 메시징을 최적화할 수 있습니다. 자세한 내용은 [메시지]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/)를 확인하세요.

![]({% image_buster /assets/img_archive/message_setup_settings_flow.png %})

구성 요소 구성을 완료한 후 **완료**을(를) 선택하십시오.

{% tabs local %}
{% tab 캔버스 진입 등록 정보 %}

`canvas_entry_properties`은(는) 캔버스를 생성하는 입력 일정 단계에서 구성되며 사용자를 캔버스로 진입시키는 트리거를 나타냅니다. 이러한 속성은 API 트리거 캔버스에 있는 항목 페이로드의 속성에도 액세스할 수 있습니다. `canvas_entry_properties` 객체의 최대 크기는 50KB입니다. 

캔버스 흐름의 경우 Liquid에서 모든 메시지 단계에서 항목 속성을 사용할 수 있습니다. 이러한 항목 속성을 참조할 때는 {% raw %} ``canvas_entry_properties${property_name}`` {% endraw %} Liquid를 사용합니다. 이 방법으로 사용하려면 이벤트가 사용자 지정 이벤트 또는 구매 이벤트여야 합니다.

이러한 항목 속성을 참조할 때는 {% raw %} ``canvas_entry_properties${property_name}`` {% endraw %} Liquid를 사용합니다. 이 방법을 사용하려면 이벤트가 사용자 지정 이벤트 또는 구매 이벤트여야 합니다.

{% raw %}
예를 들어 다음 요청을 고려해 보세요: `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. "shoes"라는 단어를 ``{{canvas_entry_properties.${product_name}}}`` Liquid을 사용하여 메시지에 추가할 수 있습니다.
{% endraw %}

{% endtab %}

{% tab 이벤트 속성 %}
이벤트 속성은 커스텀 이벤트 및 구매 시 사용자가 설정한 속성입니다. 이 `event_properties`는 캔버스뿐만 아니라 실행 기반 전달이 있는 캠페인에서도 사용할 수 있습니다. 

캔버스 플로우에서 커스텀 이벤트 및 구매 이벤트 속성정보는 행동 경로 단계에 이어지는 메시지 단계에서 Liquid에서 사용할 수 있습니다. 이 {% raw %} ``{{event_properties.${property_name}}}`` {% endraw %} Liquid를 이 `event_properties`를 참조할 때 사용하세요. 이러한 이벤트는 메시지 구성 요소에서 이러한 방식으로 사용하려면 사용자 지정 이벤트 또는 구매 이벤트여야 합니다.

행동 경로 다음의 첫 번째 메시지 단계에서 해당 작업 경로에 참조된 이벤트와 관련된 `event_properties`를 사용할 수 있습니다. 이 행동 경로 단계와 메시지 단계 사이에 다른 단계(다른 작업 경로 또는 메시지 단계가 아닌)를 배치할 수 있습니다. 메시지 단계가 행동 경로 단계에서 모든 사람 경로가 아닌 경로로 추적될 수 있는 경우에만 `event_properties`에 액세스할 수 있습니다.

{% endtab %}
{% endtabs %}

### 연결 편집

단계 간 연결을 이동하려면 두 구성 요소를 연결하는 화살표를 선택하고 다른 구성 요소를 선택합니다. 연결을 제거하려면 캔버스 작성기의 바닥글에서 화살표를 선택한 다음 **연결 취소**를 선택하세요.

## 4단계: 캔버스로 다변량 테스트 실시

캔버스에 대조군을 추가하려면 <i class="fas fa-plus-circle"></i> 플러스 버튼을 선택하여 새 배리언트를 추가할 수 있습니다. 

대조군에 포함된 사용자는 어떤 메시지도 수신하지 않지만, Braze에서는 해당 사용자의 전환 이벤트를 추적합니다. 테스트 정확도를 유지하기 위해 전환 이벤트 선택 화면에 표시된 시간과 정확하게 일치하는 시간 동안 배리언트와 대조군의 전환 수를 추적합니다. 

**배리언트 명칭(Variant Name)** 헤더를 두 번 클릭하면 메시지 간 분포를 조정할 수 있습니다.

이 예에서는 캔버스를 두 가지 배리언트로 나누었습니다. 배리언트 1에는 사용자의 70%가 포함되어 있습니다. 두 번째 배리언트는 대조군이며, 나머지 30%의 사용자로 구성되어 있습니다.

![]({% image_buster /assets/img_archive/Canvas_Multivariate_Flow.png %})

### 캔버스를 위한 지능형 선택

지능형 선택 기능은 이제 다변량 캔버스 내에서 사용할 수 있습니다. 다변량 캠페인을 위한 지능형 선택][18a] 기능과 유사하게, 캔버스를 위한 지능형 선택은 각 캔버스 배리언트의 성능을 분석하고 각 배리언트를 통해 유입되는 사용자 비율을 조정합니다. 이 분포는 총 예상 전환 수를 극대화하기 위해 각 배리언트의 성능/성과 측정기준을 기반으로 합니다.

다변량 캔버스를 사용하면 카피뿐만 아니라 타이밍과 채널도 테스트할 수 있다는 점을 명심하세요. 지능형 선택을 통해 캔버스를 더 효율적으로 테스트하고 사용자가 최상의 캔버스 여정을 경험할 수 있도록 자신감을 가질 수 있습니다.

![][18b]

캔버스용 지능형 선택은 각 배리언트로 분류된 사용자 분포를 점차 실시간으로 조정하여 캔버스 결과를 최적화합니다. 통계 알고리즘이 귀하의 변형들 중에서 결정적인 승자를 결정하면 성과가 저조한 변형들을 배제하고 향후 모든 적격 수신자를 캔버스의 승리 변형에 배정합니다. 

이러한 이유로 지능형 선택은 새로운 사용자가 자주 들어오는 캔버스에서 가장 잘 작동합니다.

## 5단계: 캔버스 저장 및 실행

캔버스 생성을 완료하면 **캔버스 실행**을 선택하여 캔버스를 저장하고 실행하세요. 캔버스를 시작한 후에는 **캔버스 세부 정보** 페이지에서 여정의 분석을 확인할 수 있습니다. 

나중에 다시 작업해야 할 경우 캔버스를 초안으로 저장할 수도 있습니다.

![][19]

{% alert tip %}
이미 실행한 캔버스를 편집해야 한다고요? 당연히 가능합니다! [출시 후 캔버스 편집]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/change_your_canvas_after_launch/)에 대한 자세한 내용을 확인하세요.
{% endalert %}


[1]: {% image_buster /assets/img_archive/canvas_dropdown.png %}
[2]: {% image_buster /assets/img_archive/canvas_exact_stats.png %}
[3]: {% image_buster /assets/img_archive/choose_canvas_experience.png %}
[6b]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting-and-canvas-components
[6c]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting#frequency-capping
[11]:{% image_buster /assets/img_archive/canvas_add_variant.gif %}
[12]:{% image_buster /assets/img_archive/Canvas_Multiple_Variants.png %}
[13]:{% image_buster /assets/img_archive/Canvas_One_Day.png %}
[14]:{% image_buster /assets/img_archive/Canvas_Exception_Events.png %}
[15]:{% image_buster /assets/img_archive/Canvas_Additional_Engagement.png %}
[17]:{% image_buster /assets/img_archive/Canvas_More_Step.png %}
[18a]: {{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/
[18b]: {% image_buster /assets/img_archive/canvas_intelligent_selection.png %}
[19]:{% image_buster /assets/img_archive/Canvas_Analytics.png %}
[50]: {% image_buster /assets/img/quiet_hours.png %}
[52]: {% image_buster /assets/img/add_canvas_conversions.png %}
[53]: {% image_buster /assets/img/canvas_details.png %}
