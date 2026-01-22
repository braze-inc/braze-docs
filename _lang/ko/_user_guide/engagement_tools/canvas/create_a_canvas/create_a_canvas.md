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

> 이 참조 문서에서는 캔버스를 만들고, 유지 관리하고, 테스트하는 데 필요한 단계를 다룹니다. 이 가이드를 따르거나 [캔버스 Braze 학습 과정을](https://learning.braze.com/quick-overview-canvas-setup) 확인하세요.

{% details Original Canvas editor %}
더 이상 기존 캔버스 환경을 사용하여 캔버스를 만들거나 복제할 수 없습니다. Braze [커런츠는 캔버스를]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/) 가장 최신 편집기로 [복제할]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/) 것을 권장합니다.
{% enddetails %}

## 캔버스 만들기

### 1단계: 새 캔버스 설정하기 

먼저 **메시징** > **캔버스로** 이동한 다음 **캔버스 만들기를** 선택합니다.

캔버스 빌더는 캔버스 이름 지정부터 전환 이벤트 설정, 적합한 사용자를 고객 여정으로 끌어들이는 것까지 캔버스 설정 과정을 단계별로 안내합니다. 다음 탭을 각각 선택하여 각 빌더 단계에서 조정할 수 있는 설정을 확인합니다.

{% tabs local %}
  {% tab Basics %}
    여기에서 캔버스의 기본 사항을 설정합니다:
    \- 캔버스 이름 지정하기
    \- Teams 추가
    \- 태그 추가
    \- 전환 이벤트를 할당하고 이벤트 유형과 기한을 선택합니다.

    Learn more about the [Basics step](#step-2a-set-up-your-canvas-basics).
  {% endtab %}
  {% tab Entry Schedule %}
    여기에서 사용자가 캔버스에 들어오는 방법과 시기를 결정할 수 있습니다:
    \- 예약됨: 이것은 시간 기반 캔버스 항목입니다.
    \- 액션 기반: 사용자가 정의된 작업을 수행한 후 캔버스에 입장합니다.
    \- API 트리거: API 요청을 사용하여 캔버스에 사용자 입력하기

    Learn more about the [Entry Schedule step](#step-2b-determine-your-canvas-entry-schedule).
  {% endtab %}
  {% tab Target Audience %}
    여기에서 타겟 오디언스를 선택합니다:
    \- 세그먼트와 필터를 추가하여 오디언스 만들기
    \- 캔버스 재진입 및 진입 제한 미세 조정
    \- 타겟팅 오디언스 요약 보기

    Learn more about the [Target Audience step](#step-2c-set-your-target-entry-audience).
  {% endtab %}
  {% tab Send Settings %}
    여기에서 캔버스 보내기 설정을 선택합니다:
    \- 구독 설정 선택
    \- 캔버스 메시징에 대한 전송 속도 제한 설정하기
    \- 방해금지 시간 인에이블먼트 및 설정하기

    Learn more about the [Send Settings step](#step-2d-select-your-send-settings).
  {% endtab %}
  {% tab Build Canvas %}
    여기에서 캔버스를 구축합니다.

    Learn how to [build your Canvas](#step-3-build-your-canvas) using the Canvas builder.
  {% endtab %}
  {% tab Summary %}
    여기에서 캔버스 세부 정보를 요약하여 확인할 수 있습니다. [캔버스 승인 워크플로우가]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) 켜져 있는 경우, 시작하기 전에 나열된 캔버스 세부 정보를 승인할 수 있습니다.

  {% endtab %}
{% endtabs %}

#### 1.1단계: 캔버스 기초부터 시작하기

여기에서 캔버스의 이름을 지정하고, [Teams를]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/#teams) 할당하고, [태그를]({{site.baseurl}}/user_guide/administrative/app_settings/tags/#tags) 만들거나 추가할 수 있습니다. 캔버스에 전환 이벤트를 할당할 수도 있습니다.

{% alert tip %}
캔버스에 태그를 지정하여 쉽게 찾고 보고서를 구축할 수 있도록 하세요. 예를 들어 [보고서 빌더를]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/) 사용할 때 특정 태그를 기준으로 필터링할 수 있습니다.
{% endalert %}

캔버스 이름, 설명, 위치 및 태그 필드가 있는 캔버스 세부 정보 페이지입니다.]({% image_buster /assets/img/canvas_details.png %}){: style="max-width:70%;"}

##### 전환 이벤트 선택하기

전환 이벤트 유형을 선택한 다음 기록할 전환을 선택합니다. 이러한 [전환 이벤트를]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) 통해 캔버스의 효율성을 측정할 수 있습니다. 

주요 전환 이벤트 A 구매하기 전환 이벤트 유형으로 3일의 전환 기한 내에 구매를 한 사용자의 대화를 기록합니다.]({% image_buster /assets/img/add_canvas_conversions.png %})

캔버스에 여러 배리언트 또는 대조군이 있는 경우, Braze는 이 전환 이벤트를 사용하여 이 전환 목표를 달성하는 데 가장 적합한 배리언트를 결정합니다. 동일한 로직을 사용하여 여러 전환 이벤트를 만들 수 있습니다.

#### 1.2단계: 캔버스 입력 일정 결정하기

사용자가 캔버스에 입장할 수 있는 세 가지 방법 중 하나를 선택할 수 있습니다. 

##### 참가 일정 유형

{% tabs local %}
  {% tab Scheduled Delivery %}
    예약 전달을 사용하면 캠페인을 예약하는 방법과 유사하게 사용자가 시간 일정에 따라 입력하게 됩니다. 캔버스가 시작되는 즉시 사용자를 등록하거나, 미래의 특정 시점에 사용자를 여정에 참여시키거나, 매일, 매주 또는 매월 반복적으로 사용자를 등록할 수 있습니다. 

    In this example, based on the time-based options, users will enter this Canvas every Tuesday at 12 pm in their local time zone every week, beginning November 14, 2025 until December 31, 2025.

    ![The "Entry Schedule" page with the type set to "Scheduled". Due to the selection, time-based options are shown, including frequency, start time, recurrence, days, and more.]({% image_buster /assets/img_archive/Canvas_Scheduled_Delivery.png %})
  {% endtab %}
  {% tab Action-Based Delivery %}
    실행 기반 전달을 사용하면 사용자가 앱을 열거나 구매를 하거나 커스텀 이벤트를 트리거하는 등 특정 행동을 할 때 캔버스에 들어가 메시지를 받기 시작합니다.

    You can control other aspects of the Canvas behavior from the **Entry Audience** window, including rules for re-eligibility and frequency capping settings. Note that action-based delivery is unavailable for Canvas components with in-app messages.

    ![An example of action-based delivery. Users will enter the Canvas if they make a purchase with an entry window beginning at 1:30 pm on June 10, 2025.]({% image_buster /assets/img_archive/Canvas_Action_Based_Delivery.png %})

  {% endtab %}
  {% tab API-Triggered Delivery %}
    API 트리거 전달을 사용하면 사용자가 API를 통해 [`/canvas/trigger/send` 엔드포인트를]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) 사용하여 추가한 후 캔버스에 들어가 메시지를 수신하기 시작합니다. 대시보드에서 이 작업을 수행하는 예제 cURL 요청을 찾을 수 있으며, 캔버스 항목 속성 개체를 사용하여 옵션 [`canvas_entry_properties`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) 를 할당할 수 있습니다. 

    ![An example of API-triggered delivery with a Canvas ID and an example of a cURL request.]({% image_buster /assets/img_archive/Canvas_API_Triggered_Delivery.png %})

    You can use the following endpoints for API-triggered delivery:
    - [POST: Send Canvas Messages via API-Triggered Delivery]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)
    - [POST: Schedule API-Triggered Canvases]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/)
    - [POST: Update Scheduled API-Triggered Canvases]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/)

  {% endtab %}
{% endtabs %}

전달 방법을 선택한 후 사용 사례에 맞게 설정을 조정한 다음 타겟팅 오디언스를 계속 설정하세요.

{% details Deduplicate behavior for Canvases using the original editor %}
재자격 기간이 캔버스의 최대 기간보다 짧은 경우, 사용자는 다시 입장하여 두 개 이상의 컴포넌트의 메시지를 수신할 수 있습니다. 사용자의 재진입이 이전 항목과 동일한 컴포넌트에 도달하는 엣지 케이스의 경우, Braze는 해당 컴포넌트의 메시징을 중복 제거합니다. 

사용자가 캔버스에 다시 들어와 이전 항목과 동일한 구성 요소에 도달하고 각 항목에 대한 인앱 메시지를 받을 자격이 있는 경우, 사용자는 세션을 두 번 다시 열면 인앱 메시지 우선순위에 따라 메시지를 두 번 받게 됩니다.
{% enddetails %}

#### 1.3단계: 타겟 오디언스 설정하기

정의된 기준에 부합하는 사용자만 **타겟 오디언스** 단계에서 여정에 진입할 수 있으며, 이는 사용자가 캔버스 여정에 **진입하기 전에** Braze가 먼저 타겟 오디언스의 적격 여부를 평가한다는 의미입니다. 예를 들어 신규 사용자를 타겟팅하려는 경우 앱을 처음 사용한 지 일주일이 되지 않은 사용자 세그먼트를 선택할 수 있습니다.

**항목 제어에서** 캔버스가 실행되도록 예약할 때마다 사용자 수를 제한할 수 있습니다. API 트리거 기반 및 동작 기반 캔버스의 경우, 이 제한은 매 UTC 시간마다 발생합니다. 

{% alert important %}
오디언스 필터와 동일한 트리거(예: 변경된 속성 또는 커스텀 이벤트 수행)로 액션 기반 캠페인 또는 캔버스를 구성하지 마세요. 트리거 이벤트를 수행할 때 사용자가 오디언스에 없는 [경합 조건이]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions) 발생할 수 있으며, 이는 사용자가 캠페인을 수신하지 않거나 캔버스에 입장하지 못한다는 것을 의미합니다.
{% endalert %}

##### 오디언스 테스트하기

타겟 오디언스에 세그먼트와 필터를 추가한 후에는 [사용자를 조회하여]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) 오디언스 기준과 일치하는지 확인하여 오디언스가 예상대로 설정되었는지 테스트할 수 있습니다.

!"사용자 조회" 필드에서 외부 사용자 ID 또는 Braze ID로 검색할 수 있습니다.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:100%;"}{: style="max-width:80%;"}

##### 항목 컨트롤 선택

항목 컨트롤은 사용자가 캔버스에 다시 들어갈 수 있는지 여부를 결정합니다. 또한 선택한 주기(매일, 캔버스 평생 또는 캔버스가 예약될 때마다)에 따라 이 캔버스에 입장할 수 있는 사람의 수를 제한할 수도 있습니다. 

예를 들어, **입력량 제한을** 선택하고 **최대 입력** 수 필드를 5,000명으로 설정하고 제한 주기를 **매일로** 설정하면 캔버스는 하루에 5,000명의 사용자에게만 전송합니다.

'사용자가 캔버스에 다시 입장할 수 있도록 허용' 및 '입장 볼륨 제한' 확인란이 표시된 '입장 컨트롤' 페이지. 후자를 사용하면 최대 항목 수를 설정하고 매일, 캔버스 평생 또는 매번 캔버스를 예약할 때마다 제한할지 여부를 설정할 수 있습니다.]({% image_buster /assets/img_archive/entry_controls.png %})

{% alert tip %}
Braze는 IP 워밍업을 위해 **캔버스를 예약할 때마다** 기능을 사용하면 전송량이 증가할 수 있으므로 사용하지 않는 것이 좋습니다.
{% endalert %}

##### 종료 기준 설정

[종료 기준을]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria) 설정하면 캔버스에서 어떤 사용자를 종료할지 결정할 수 있습니다. 사용자가 예외 이벤트를 수행하거나 메시지 세그먼트 및 필터와 일치하는 경우 더 이상 메시지를 받지 않습니다.

##### 대상 집단 계산하기

**대상 집단** 섹션에서는 선택한 세그먼트 및 추가 필터와 같은 대상 집단에 대한 요약과 메시징 채널별로 도달 가능한 사용자 수에 대한 분석을 볼 수 있습니다. 기본값 대신 타겟 오디언스에서 도달 가능한 정확한 사용자 수를 계산하려면 [정확한 통계 계산을]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#calculating-exact-statistics) 선택합니다.

참고하세요:

- 정확한 통계를 계산하는 데는 몇 분 정도 걸릴 수 있습니다. 이 기능은 필터 또는 필터 그룹 수준이 아닌 세그먼트 수준에서만 정확한 통계를 계산합니다.
- 세그먼트가 큰 경우 정확한 통계를 계산할 때에도 약간의 편차가 발생하는 것이 정상입니다. 이 기능의 정확도는 99.999% 이상일 것으로 예상됩니다.

타겟팅한 사용자의 평균 평생 매출과 같은 추가 통계를 보려면 **추가 통계** 보기를 선택합니다.

정확한 통계를 계산하는 옵션이 포함된 대상 집단 분석.]({% image_buster /assets/img_archive/canvas_exact_stats.png %})

##### 타겟 오디언스 수가 도달 가능한 사용자 수와 다를 수 있는 이유

{% multi_lang_include segments.md section='Differing audience size' %}

#### 1.4단계: 보내기 설정 선택

**전송 설정을** 선택하여 정기구독 설정을 편집하고, 요금 제한을 켜고, 방해금지 시간을 설정할 수 있습니다. [속도 제한]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting-and-canvas-components) 또는 [최대 게재빈도]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting#frequency-capping) 설정을 켜면 사용자에 대한 마케팅 부담을 완화하고 과도한 메시징을 방지할 수 있습니다.

이메일 및 푸시 채널을 타겟팅하는 캔버스의 경우 명시적으로 옵트인한 사용자만 메시지를 받도록 캔버스를 제한할 수 있습니다(가입하거나 탈퇴한 사용자 제외). 예를 들어 옵트인 상태가 서로 다른 세 명의 사용자가 있다고 가정해 보겠습니다:

- **사용자 A는** 이메일에 가입하고 푸시 인에이블먼트가 되어 있습니다. 이 사용자는 이메일을 수신하지 않지만 푸시는 받게 됩니다.
- **사용자 B는** 이메일에 옵트인되어 있지만 푸시 인에이블먼트가 되어 있지 않습니다. 이 사용자는 이메일은 수신하지만 푸시는 받지 않습니다.
- **사용자 C는** 이메일에 옵트인되어 있으며 푸시 인에이블먼트가 설정되어 있습니다. 이 사용자는 이메일과 푸시를 모두 받게 됩니다.

이렇게 하려면 **구독 설정에서** 이 캔버스를 '옵트인한 사용자에게만' 보내도록 설정하세요. 이 옵션을 선택하면 옵트인한 사용자만 이메일을 받게 되며, Braze는 기본값으로 푸시를 인에이블먼트한 사용자에게만 푸시를 보냅니다. 

이러한 구독 설정은 단계별로 적용되므로 진입 오디언스에는 영향을 미치지 않습니다. 따라서 이 설정은 각 캔버스 단계를 받을 수 있는 사용자의 자격을 평가하는 데 사용됩니다.

{% alert important %}
이 구성에서는 오디언스를 단일 채널(예: `Foreground Push Enabled = True` 또는 `Email Subscription = Opted-In`)로 제한하는 필터를 **타겟 오디언스** 단계에 포함하지 마세요.
{% endalert %}

원하는 경우 캔버스에 방해금지 시간(메시징이 전송되지 않는 시간)을 지정할 수 있습니다. **전송 설정에서** **방해금지 시간 인에이블먼트에** 체크합니다. 그런 다음 사용자 현지 시간으로 방해금지 시간을 선택하고 해당 방해금지 시간 내에 메시지가 트리거될 경우 어떤 동작을 수행할지 선택합니다.

'조용한 시간' 페이지에 방해금지 시간을 인에이블먼트할 수 있는 체크박스가 표시됩니다. 인에이블먼트가 활성화되면 시작 시간, 종료 시간 및 대체 동작을 설정할 수 있습니다.]({% image_buster /assets/img/quiet_hours.png %})

### 2단계: 캔버스 구축하기

{% alert tip %}
[Braze 캔버스 템플릿을]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_templates/#available-braze-templates) 사용하여 시간을 저장하고 캔버스 제작을 간소화하세요! 미리 구축된 템플릿 라이브러리를 검색하여 사용 사례에 맞는 템플릿을 찾고 특정 요구사항에 맞게 커스텀하세요.
{% endalert %}

#### 2.1단계: 배리언트 추가하기

'배리언트 추가' 버튼을 선택하면 '배리언트 추가' 옵션이 있는 컨텍스트 메뉴가 표시됩니다.]({% image_buster /assets/img_archive/canvas_add_variant.gif %}){: style="float:right;max-width:40%;margin-left:15px;"}

**배리언트 추가를** 선택한 다음 캔버스에 새 배리언트를 추가합니다. 배리언트는 사용자가 이동하는 여정을 나타내며 여러 단계와 분기를 포함할 수 있습니다.

<i class="fas fa-plus-circle"></i> 더하기 버튼을 선택하여 배리언트를 추가할 수 있습니다. 새로운 배리언트를 추가하면 다양한 참여 전략의 효과를 교차 비교하고 분석할 수 있도록 배리언트 간에 사용자를 배포하는 방법을 조정할 수 있습니다.

Braze 캔버스의 두 가지 배리언트 예시.]({% image_buster /assets/img_archive/Canvas_Multiple_Variants.png %})

{% alert tip %}
기본적으로 캔버스 배리언트 할당은 사용자가 캔버스에 들어갈 때 기본값으로 고정되므로 사용자가 처음 배리언트를 입력하면 캔버스에 다시 들어갈 때마다 해당 배리언트가 그 배리언트가 됩니다. 하지만 이 동작을 우회하는 방법이 있습니다. <br><br>이렇게 하려면 Liquid를 사용하여 난수 생성기를 생성하고 각 사용자의 캔버스 항목이 시작될 때 실행하여 값을 커스텀 속성으로 저장한 다음 해당 속성을 사용하여 사용자를 무작위로 나눌 수 있습니다.

{% details Expand for steps %}

1. 난수를 저장할 커스텀 속성을 생성합니다. "lottery_number" 또는 "random_assignment". 처럼 찾기 쉬운 이름을 지정하세요. [대시보드에서]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data/) 속성을 만들거나 [`/users/track` 엔드포인트에]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) 대한 API 호출을 통해 속성을 만들 수 있습니다.<br><br>
2. 캔버스 시작 부분에 웹훅 캠페인을 만듭니다. 이 캠페인은 난수를 생성하고 커스텀 속성으로 저장하는 매개체가 될 것입니다. 자세한 내용은 [웹훅 만들기를]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#step-1-set-up-a-webhook) 참조하세요. URL을 `/users/track` 엔드포인트로 설정합니다.<br><br>
3. 난수 생성기를 생성합니다. [여기에 설명된](https://community.shopify.com/c/technical-q-a/is-there-any-way-to-generate-random-number-with-liquid-shopify/m-p/1595486) 코드를 사용하면 각 사용자의 고유한 입력 시간을 활용하여 난수를 생성할 수 있습니다. 결과 숫자를 웹훅 캠페인 내에서 Liquid 변수로 설정하세요.<br><br>
4. 웹훅 캠페인에서 `/users/track` 호출의 형식을 지정하여 1단계에서 생성한 커스텀 속성을 현재 사용자 프로필에서 생성한 임의의 번호로 설정합니다. 이 단계가 실행되면 사용자가 캠페인에 참여할 때마다 변경되는 난수를 성공적으로 생성한 것입니다.<br><br>
5. 캔버스의 브랜치를 조정하여 무작위로 선택된 배리언트에 의해 분할되는 대신 오디언스 규칙에 따라 분할되도록 합니다. 각 지점의 오디언스 규칙에서 커스텀 속성에 따라 오디언스 필터를 설정합니다. <br><br>예를 들어 한 지점은 오디언스 필터로 "lottery_number 이 3 미만인 반면, 다른 지점은 "lottery_number 이 3 이상 6 미만인 경우가 있을 수 있습니다.

{% enddetails %}
{% endalert %}

#### 2.2단계: 캔버스 단계 추가하기

**구성 요소** 사이드바에서 구성 요소를 드래그 앤 드롭하여 캔버스 워크플로에 더 많은 단계를 추가할 수 있습니다. 또는 <i class="fas fa-plus-circle"></i> 더하기 버튼을 선택하여 팝업 메뉴로 컴포넌트를 추가합니다.

{% alert tip %}
단계를 더 추가하기 시작하면 확대/축소 수준을 높여 세부 사항에 집중하거나 전체 사용자 여정을 살펴볼 수 있습니다. <kbd>Shift</kbd> + <kbd>+로</kbd> 확대하거나 <kbd>Shift</kbd> + <kbd>-로</kbd> 축소합니다.
{% endalert %}

컴포넌트 검색 창에 Braze 캔버스에 지연 단계가 추가되었습니다.]({% image_buster /assets/img_archive/add_components_flow.png %}){: style="max-width:80%;"}

{% alert important %}
캔버스에는 최대 200개의 단계를 추가할 수 있습니다. 캔버스 단계가 200단계를 초과하면 로드 문제가 발생할 수 있습니다.
{% endalert %}

##### 최대 지속 시간

캔버스 여정이 단계적으로 증가함에 따라 최대 기간은 사용자가 이 캔버스를 완성하는 데 걸리는 최장 시간입니다. 이는 가장 긴 경로의 각 배리언트에 대한 각 단계의 지연 및 트리거 기간을 더하여 계산합니다. 예를 들어 캔버스에 지연 기간이 3일인 지연 단계와 메시지 단계가 있는 경우 캔버스의 최대 기간은 3일이 됩니다.

##### 단계 편집하기

사용자 여정의 단계를 편집하고 싶으신가요? 캔버스 워크플로에 따라 이 작업을 수행하는 방법을 확인하세요!

구성 요소를 선택하여 캔버스 워크플로우의 모든 단계를 편집할 수 있습니다. 예를 들어 워크플로우의 첫 번째 단계인 [지연]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) 컴포넌트를 특정 날짜로 편집하고 싶다고 가정해 보겠습니다. 단계를 선택하여 설정을 확인하고 지연을 3월 1일로 조정합니다. 즉, 3월 1일에 사용자가 캔버스의 다음 단계로 이동하게 됩니다.

지연이 "특정 날짜까지"로 설정된 "지연" 단계의 예입니다.]({% image_buster /assets/img_archive/edit_delay_flow.png %})

또는 [행동 경로]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) 단계의 **행동 설정을** 빠르게 편집하고 조정하여 일정 시간 동안 사용자를 대기시킬 수 있습니다. 이 평가 기간 동안의 행동에 따라 다음 경로의 우선순위를 정합니다.

캔버스의 두 번째 단계인 '작업 설정'에서 평가 기간을 1일로 설정합니다.]({% image_buster /assets/img_archive/action_paths_flow.png %})

캔버스의 가벼운 구성 요소는 간단한 편집 환경을 제공하므로 캔버스의 세세한 디테일을 더 쉽게 조정할 수 있습니다. 

##### 캔버스의 메시지

캔버스 컴포넌트에서 메시지를 편집하여 특정 단계에서 보낼 메시지를 제어할 수 있습니다. 캔버스는 이메일, 모바일, 웹 푸시 메시지를 보낼 수 있으며 웹훅을 통해 다른 시스템과 통합할 수 있습니다. 캠페인과 마찬가지로 특정 [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/) 템플릿을 사용하여 메시지를 개인화할 수 있습니다.

{% alert tip %}
메시지와 링크 템플릿에 캔버스 컴포넌트 이름을 포함할 수 있다는 사실을 알고 계셨나요?<br>
캔버스에서 `campaign.${name}` Liquid 태그를 사용하여 현재 캔버스 컴포넌트 이름을 표시합니다.
{% endalert %}

메시지 구성 요소는 사용자에게 전송되는 메시지를 관리합니다. **메시징 채널을** 선택하고 **전달 설정을** 조정하여 캔버스 메시징을 최적화할 수 있습니다. 이 구성 요소에 대한 자세한 내용은 [메시지를]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) 확인하세요.

'메시지 설정' 단계에서 '메시징 채널'을 선택하면 Android 푸시, 콘텐츠 카드, 이메일 등과 같은 사용 가능한 메시징 채널 목록이 표시됩니다.]({% image_buster /assets/img_archive/message_setup_settings_flow.png %})

캔버스 컴포넌트 구성을 완료한 후 **완료를** 선택합니다.

{% tabs local %}
{% tab Canvas Entry Properties %}

`canvas_entry_properties` 은 캔버스 생성의 엔트리 스케줄 단계에서 구성되며 사용자를 캔버스에 입력하는 트리거를 나타냅니다. 이러한 속성은 API 트리거 캔버스에 있는 항목 페이로드의 속성에도 액세스할 수 있습니다. `canvas_entry_properties` 객체는 최대 50KB까지 가능합니다. 

이러한 항목 속성을 참조할 때 다음 Liquid를 사용하십시오: {% raw %} ``canvas_entry_properties.${property_name}`` {% endraw %}. 이 방법을 사용하려면 이벤트가 커스텀 이벤트 또는 구매 이벤트여야 합니다.

{% raw %}
예를 들어 다음 요청을 고려해 보세요: `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. 이 Liquid ``{{canvas_entry_properties.${product_name}}}`` 를 사용하여 메시징에 "신발"이라는 단어를 추가할 수 있습니다.
{% endraw %}

{% endtab %}

{% tab Event Properties %}
이벤트 속성은 커스텀 이벤트 및 구매에 대해 설정한 속성정보입니다. 이 `event_properties` 는 캔버스뿐만 아니라 실행 기반 전달을 통해 캠페인에 사용할 수 있습니다. 

캔버스에서 커스텀 이벤트 및 구매 이벤트 속성정보는 행동 경로 단계를 따르는 모든 메시지 단계에서 Liquid에서 사용할 수 있습니다. 이 Liquid {% raw %} ``{{event_properties.${property_name}}}`` {% endraw %} 를 참조할 때 `event_properties`. 메시지 구성 요소에서 이러한 방식으로 사용하려면 이러한 이벤트는 커스텀 이벤트 또는 구매 이벤트여야 합니다.

행동 경로 다음의 첫 번째 메시지 단계에서 해당 행동 경로에 참조된 이벤트와 관련된 `event_properties` 을 사용할 수 있습니다. 이 행동 경로 단계와 메시지 단계 사이에 다른 단계(다른 행동 경로나 메시지 단계가 아닌)를 가질 수 있습니다. 메시지 단계가 행동 경로 단계에서 모든 사람이 아닌 경로로 추적할 수 있는 경우에만 `event_properties` 에 액세스할 수 있습니다.

{% endtab %}
{% endtabs %}

#### 2.3단계: 연결 편집

단계 간에 연결을 이동하려면 두 구성 요소를 연결하는 화살표를 선택하고 다른 구성 요소를 선택합니다. 연결을 제거하려면 캔버스 작성기 바닥글에서 화살표와 **연결 취소를** 차례로 선택합니다.

### 3단계: 대조군 추가하기

<i class="fas fa-plus-circle"></i> 더하기 버튼을 선택하여 새 배리언트를 추가하여 캔버스에 대조군을 추가할 수 있습니다. 

Braze는 대조군에 배치된 사용자의 전환을 추적하지만 메시지를 수신하지 않습니다. 정확한 테스트를 유지하기 위해 전환 이벤트 선택 화면에 표시된 것처럼 배리언트와 대조군의 전환 수를 정확히 동일한 시간 동안 추적합니다. 

**배리언트 이름** 헤더를 두 번 클릭하여 메시지 간의 배포를 조정할 수 있습니다.

이 예시에서는 캔버스를 두 가지 배리언트로 나누었습니다. 배리언트 1은 70%의 사용자를 보유하고 있습니다. 두 번째 배리언트는 나머지 30%의 사용자로 구성된 대조군입니다.

70%가 첫 번째 단계에서 하루 동안 지연된 후 두 번째 단계에서 메시지를 보내는 "Variant 1"로 이동하는 Braze 캔버스의 배리언트 예시입니다. 나머지 30%는 후속 단계가 없는 '제어'로 이동합니다.]({% image_buster /assets/img_archive/Canvas_Multivariate_Flow.png %})

#### 캔버스를 위한 지능형 선택

이제 다변량 캔버스에서 지능형 선택 기능을 사용할 수 있습니다. 다변량 캠페인의 [지능형 선택]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/) 기능과 마찬가지로, 캔버스용 지능형 선택은 각 캔버스 배리언트의 성능/성과를 분석하고 각 배리언트를 통해 퍼널링되는 사용자 비율을 조정합니다. 이 분포는 총 예상 전환 수를 최대화하기 위해 각 배리언트의 성능/성과 측정기준을 기반으로 합니다.

다변량 캔버스를 사용하면 카피뿐만 아니라 타이밍과 채널도 테스트할 수 있습니다. 지능형 선택을 통해 캔버스를 보다 효율적으로 테스트하고 사용자에게 최상의 캔버스 여정을 제공할 수 있다는 확신을 가질 수 있습니다.

'배리언트 배포 편집' 페이지에서 '지능형 선택' 옵션이 인에이블먼트됩니다. 캔버스를 분석하고 최적화할 때 페이지 전체에 가로 막대가 표시되며, 이 가로 막대는 각각 색상과 크기가 다른 여러 섹션으로 나뉩니다. 이는 시각적 표현일 뿐이며 특정 분석과 관련이 없습니다.]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

캔버스용 지능형 선택은 각 배리언트로 분류된 사용자 분포를 점진적으로 실시간으로 조정하여 캔버스 결과를 최적화합니다. 통계 알고리즘이 배리언트 중에서 결정적인 승자를 결정하면, 실적이 저조한 배리언트를 배제하고 향후 모든 적격 캔버스 수신자를 우승 배리언트에 배치합니다. 

이러한 이유로 지능형 선택은 새로운 사용자가 자주 들어오는 캔버스에서 가장 잘 작동합니다.

### 4단계: 저장 및 실행

캔버스 생성을 완료한 후 **캔버스 시작을** 선택하여 캔버스를 저장하고 실행합니다. 캔버스를 실행한 후에는 **캔버스 세부 정보** 페이지에서 여정에 대한 분석 결과를 확인할 수 있습니다. 

다시 돌아와야 할 경우 캔버스를 초안으로 저장할 수도 있습니다.

Braze의 캔버스 예시.]({% image_buster /assets/img_archive/Canvas_Analytics.png %})

{% alert tip %}
실행 후 캔버스를 편집해야 하나요? 할 수 있습니다! 자세한 내용은 [출시 후 캔버스 편집하기를]({{site.baseurl}}/post-launch_edits/) 참조하세요.
{% endalert %}

