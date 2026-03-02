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

{% details 기존 캔버스 편집기 세부 정보를 보려면 펼치세요 %}
더 이상 기존 캔버스 환경을 사용하여 캔버스를 만들거나 복제할 수 없습니다. Braze는 [캔버스를]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/) 가장 최신 편집기로 [복제할]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/) 것을 권장합니다.
{% enddetails %}

## 캔버스 만들기

### 1단계: 새 캔버스 설정 

먼저 **메시징** > **캔버스**로 이동한 다음 **캔버스 만들기**를 선택합니다.

캔버스 빌더는 캔버스 설정 과정을 단계별로 안내합니다—이름 지정부터 전환 이벤트 설정 및 적절한 사용자를 고객 여정에 포함시키는 것까지 모든 과정을 포함합니다. 각 빌더 단계에서 조정할 수 있는 설정을 보려면 다음 탭을 각각 선택하세요.

{% tabs local %}
  {% tab Basics %}
    여기에서 캔버스의 기본 사항을 설정합니다:
    - 캔버스 이름 지정
    - Teams 추가
    - 태그 추가
    - 전환 이벤트를 할당하고 이벤트 유형과 마감일 선택

    [기본 단계](#step-2a-set-up-your-canvas-basics)에 대해 자세히 알아보세요.
  {% endtab %}
  {% tab Entry Schedule %}
    여기에서 사용자가 캔버스에 진입하는 방법과 시기를 결정합니다:
    - 예약: 시간 기반 캔버스 진입입니다
    - 실행 기반: 사용자가 정의된 작업을 수행한 후에 캔버스에 진입합니다
    - API 트리거: API 요청을 사용하여 사용자를 캔버스에 진입시킵니다

    [진입 스케줄 단계](#step-2b-determine-your-canvas-entry-schedule)에 대해 자세히 알아보세요.
  {% endtab %}
  {% tab Target Audience %}
    여기에서 타겟 오디언스를 선택합니다:
    - 세그먼트와 필터를 추가하여 오디언스를 만드세요
    - 캔버스 재진입 및 진입 한도를 미세 조정하세요
    - 타겟 오디언스의 요약을 확인하세요

    [타겟 오디언스 단계](#step-2c-set-your-target-entry-audience)에 대해 자세히 알아보세요.
  {% endtab %}
  {% tab Send Settings %}
    여기에서 캔버스 전송 설정을 선택합니다:
    - 구독 설정 선택
    - 캔버스 메시지에 대한 전송 속도 제한 설정
    - 방해금지 시간 활성화 및 설정

    [전송 설정 단계](#step-2d-select-your-send-settings)에 대해 자세히 알아보세요.
  {% endtab %}
  {% tab Build Canvas %}
    여기에서 캔버스를 구축합니다.

    캔버스 빌더를 사용하여 [캔버스를 구축하는 방법](#step-3-build-your-canvas)을 알아보세요.
  {% endtab %}
  {% tab Summary %}
    여기에서 캔버스 세부 정보의 요약을 확인할 수 있습니다. [캔버스 승인 워크플로우]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/)가 켜져 있으면 시작하기 전에 나열된 캔버스 세부 정보를 승인할 수 있습니다.

  {% endtab %}
{% endtabs %}

#### 1.1단계: 캔버스 기본 사항부터 시작하세요

여기에서 캔버스의 이름을 지정하고 [Teams]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/#teams)을 할당하며 [태그]({{site.baseurl}}/user_guide/administrative/app_settings/tags/#tags)를 만들거나 추가합니다. 캔버스에 대한 전환 이벤트를 할당할 수도 있습니다.

{% alert tip %}
캔버스에 태그를 지정하면 쉽게 찾고 보고서를 작성할 수 있습니다. 예를 들어, [보고서 빌더]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/)를 사용할 때 특정 태그로 필터링할 수 있습니다.
{% endalert %}

![캔버스 이름, 설명, 위치 및 태그 필드가 있는 캔버스 세부 정보 페이지입니다.]({% image_buster /assets/img/canvas_details.png %}){: style="max-width:70%;"}

##### 전환 이벤트 선택

전환 이벤트 유형을 선택한 다음 기록할 전환을 선택하세요. 이러한 [전환 이벤트]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/)는 캔버스의 효율성을 측정합니다. 

![구매하기 전환 이벤트 유형의 주요 전환 이벤트 A는 3일의 전환 기한 내에 구매를 한 사용자의 전환을 기록합니다.]({% image_buster /assets/img/add_canvas_conversions.png %})

캔버스에 여러 배리언트 또는 대조군이 있는 경우, Braze는 이 전환 이벤트를 사용하여 이 전환 목표를 달성하기 위한 최적의 배리에이션을 결정합니다. 동일한 논리를 사용하여 여러 전환 이벤트를 생성할 수 있습니다.

#### 1.2단계: 캔버스 진입 스케줄 결정

사용자가 캔버스에 진입할 수 있는 세 가지 방법 중 하나를 선택할 수 있습니다. 

##### 진입 스케줄 유형

{% tabs local %}
  {% tab Scheduled Delivery %}
    예약된 전달을 사용하면 캠페인을 예약하는 방식과 유사하게 사용자가 시간 스케줄에 따라 진입합니다. 캔버스가 시작되자마자 사용자를 등록하거나, 미래의 특정 시점에 여정에 진입시키거나, 반복적으로(매일, 매주 또는 매월) 진입시킬 수 있습니다. 

    이 예에서는 시간 기반 옵션에 따라 사용자가 2025년 11월 14일부터 2025년 12월 31일까지 매주 화요일 오후 12시(현지 시간대 기준)에 이 캔버스에 진입합니다.

    !["진입 스케줄" 페이지에서 유형이 "예약"으로 설정되어 있습니다. 선택에 따라 빈도, 시작 시간, 반복, 요일 등의 시간 기반 옵션이 표시됩니다.]({% image_buster /assets/img_archive/Canvas_Scheduled_Delivery.png %})
  {% endtab %}
  {% tab Action-Based Delivery %}
    실행 기반 전달을 사용하면 사용자가 앱 열기, 구매, 커스텀 이벤트 트리거 등 특정 작업을 수행할 때 캔버스에 진입하여 메시지를 받기 시작합니다.

    **진입 오디언스** 창에서 재자격 규칙 및 최대 게재빈도 설정을 포함하여 캔버스 동작의 다른 측면을 제어할 수 있습니다. 실행 기반 전달은 인앱 메시지가 포함된 캔버스 구성 요소에서는 사용할 수 없습니다.

    ![실행 기반 전달의 예입니다. 사용자가 구매를 하면 2025년 6월 10일 오후 1시 30분에 시작하는 진입 기간으로 캔버스에 진입합니다.]({% image_buster /assets/img_archive/Canvas_Action_Based_Delivery.png %})

  {% endtab %}
  {% tab API-Triggered Delivery %}
    API 트리거 전달을 사용하면 [`/canvas/trigger/send` 엔드포인트]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)를 통해 API로 추가된 후 사용자가 캔버스에 진입하여 메시지를 받기 시작합니다. 대시보드에서 이 작업을 수행하는 예제 cURL 요청을 확인할 수 있으며, [컨텍스트 객체]({{site.baseurl}}/api/objects_filters/context_object/)를 사용하여 선택적으로 [`context`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)를 할당할 수 있습니다. 

    ![캔버스 ID와 cURL 요청 예제가 포함된 API 트리거 전달의 예입니다.]({% image_buster /assets/img_archive/Canvas_API_Triggered_Delivery.png %})

    API 트리거 전달에 다음 엔드포인트를 사용할 수 있습니다:
    - [POST: API 트리거 전달을 통해 캔버스 메시지 보내기]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)
    - [POST: API 트리거 캔버스 예약]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/)
    - [POST: 예약된 API 트리거 캔버스 업데이트]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/)

  {% endtab %}
{% endtabs %}

전달 방법을 선택한 후 사용 사례에 맞게 설정을 조정한 다음 타겟 오디언스 설정으로 진행하세요.

{% details 기존 편집기를 사용하는 캔버스의 중복 제거 동작 %}
재자격 부여 기간이 캔버스의 최대 기간보다 짧을 경우, 사용자는 다시 진입하여 둘 이상의 구성 요소의 메시지를 받을 수 있습니다. 사용자의 재진입이 이전 진입과 동일한 구성 요소에 도달하는 극단적인 경우, Braze는 해당 구성 요소의 메시지를 중복 제거합니다. 

사용자가 캔버스에 다시 진입하여 이전에 진입했던 동일한 구성 요소에 도달하고 각 진입에 대해 인앱 메시지를 받을 자격이 있는 경우, 사용자가 세션을 두 번 다시 열면 인앱 메시지 우선순위에 따라 메시지를 두 번 받게 됩니다.
{% enddetails %}

#### 1.3단계: 타겟 진입 오디언스 설정

정의된 기준에 부합하는 사용자만 **타겟 오디언스** 단계에서 여정에 진입할 수 있습니다. 이는 사용자가 캔버스 여정에 **진입하기 전에** Braze가 먼저 타겟 오디언스의 자격 여부를 평가한다는 의미입니다. 예를 들어, 신규 사용자를 타겟팅하려면 일주일 이내에 처음으로 앱을 사용한 사용자의 세그먼트를 선택할 수 있습니다.

**진입 제어**에서 캔버스가 실행되도록 예약될 때마다 사용자 수를 제한할 수 있습니다. API 트리거 기반 및 실행 기반 캔버스의 경우 이 제한은 매 UTC 시간마다 적용됩니다. 

{% include alerts/warning_alerts.md alert='Canvas race condition audience trigger' %}

##### 오디언스 테스트

타겟 오디언스에 세그먼트와 필터를 추가한 후, [사용자를 조회]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/)하여 오디언스 기준에 부합하는지 확인함으로써 오디언스가 예상대로 설정되었는지 테스트할 수 있습니다.

!['사용자 조회' 필드에서는 외부 사용자 ID 또는 Braze ID로 검색할 수 있습니다.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:80%;"}

##### 진입 제어 선택

진입 제어는 사용자가 캔버스에 다시 진입할 수 있는지 여부를 결정합니다. 또한 진입 스케줄 유형에 따라 선택한 주기에 따라 이 캔버스에 잠재적으로 진입할 수 있는 사람의 수를 제한할 수도 있습니다:

- **예약:** 캔버스의 수명 동안 또는 캔버스가 예약될 때마다
- **실행 기반:** 시간별, 일별 또는 캔버스의 수명 동안
- **API 트리거:** 시간별, 일별 또는 캔버스의 수명 동안

예를 들어, 실행 기반 캔버스에서 **진입량 제한**을 선택하고 **최대 진입** 필드를 5,000명으로 설정하고 **매일**을 제한 주기로 설정하면 캔버스는 하루에 5,000명의 사용자에게만 전송합니다.

!['사용자가 캔버스에 다시 진입할 수 있도록 허용' 및 '진입량 제한' 확인란이 표시된 '진입 제어' 페이지입니다. 후자를 사용하면 최대 진입 수를 설정하고 진입 스케줄 유형에 따라 주기를 선택할 수 있습니다(예: 예약 진입의 경우 캔버스의 수명 동안 또는 캔버스가 예약될 때마다, 실행 기반 및 API 트리거 진입의 경우 시간별, 일별 또는 캔버스의 수명 동안).]({% image_buster /assets/img_archive/entry_controls.png %})

{% alert tip %}
Braze는 IP 워밍을 위해 **캔버스가 예약될 때마다**를 선택하는 것을 권장하지 않습니다. 이는 전송량이 증가할 수 있기 때문입니다.
{% endalert %}

##### 종료 기준 설정

[종료 기준]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria)을 설정하면 캔버스에서 나갈 사용자를 결정할 수 있습니다. 사용자가 예외 이벤트를 수행하거나 세그먼트 및 필터와 일치하는 경우 더 이상 메시지를 받지 않습니다.

##### 대상 집단 계산

**대상 집단** 섹션에서는 선택한 세그먼트 및 추가 필터와 같은 오디언스 요약과 메시징 채널별 도달 가능한 사용자 수 분석을 확인할 수 있습니다. 기본 추정값 대신 타겟 오디언스에서 도달 가능한 정확한 사용자 수를 계산하려면 [정확한 통계 계산]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#calculating-exact-statistics)을 선택합니다.

참고:

- 정확한 통계를 계산하는 데 몇 분이 걸릴 수 있습니다. 이 기능은 필터 또는 필터 그룹 수준이 아닌 세그먼트 수준에서만 정확한 통계를 계산합니다.
- 큰 세그먼트의 경우, 정확한 통계를 계산할 때에도 약간의 변동이 있는 것이 정상입니다. 이 기능의 정확도는 99.999% 이상으로 예상됩니다.

타겟팅된 사용자의 평균 평생 매출과 같은 추가 통계를 보려면 **추가 통계 보기**를 선택합니다.

![정확한 통계를 계산하는 옵션이 있는 대상 집단 분석.]({% image_buster /assets/img_archive/canvas_exact_stats.png %})

##### 타겟 오디언스 수가 도달 가능한 사용자 수와 다를 수 있는 이유

{% multi_lang_include segments.md section='Differing audience size' %}

#### 1.4단계: 전송 설정 선택

**전송 설정**을 선택하여 구독 설정을 편집하고, 속도 제한을 켜고, 방해금지 시간을 켭니다. [속도 제한]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting-and-canvas-components) 또는 [최대 게재빈도 설정]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting#frequency-capping)을 켜면 사용자에게 가해지는 마케팅 부담을 완화하고 과도한 메시지 전송을 방지할 수 있습니다.

캔버스가 이메일 및 푸시 채널을 타겟팅하는 경우, 명시적으로 옵트인한 사용자만 메시지를 받도록 캔버스를 제한할 수 있습니다(구독 또는 구독 취소한 사용자는 제외). 예를 들어, 옵트인 상태가 다른 세 명의 사용자가 있다고 가정해 보겠습니다:

- **사용자 A**는 이메일을 구독하고 푸시가 활성화되어 있습니다. 이 사용자는 이메일을 수신하지 않지만 푸시를 받게 됩니다.
- **사용자 B**는 이메일 수신에 옵트인했지만 푸시가 활성화되어 있지 않습니다. 이 사용자는 이메일을 받지만 푸시는 받지 않습니다.
- **사용자 C**는 이메일 수신에 옵트인하고 푸시가 활성화되어 있습니다. 이 사용자는 이메일과 푸시를 모두 받습니다.

이렇게 하려면 **구독 설정**에서 이 캔버스를 "옵트인한 사용자에게만" 보내도록 설정하세요. 이 옵션은 옵트인한 사용자만 이메일을 받도록 보장하며, Braze는 기본적으로 푸시가 활성화된 사용자에게만 푸시를 보냅니다. 

이 구독 설정은 단계별로 적용되므로 진입 오디언스에는 영향을 미치지 않습니다. 따라서 이 설정은 사용자가 각 캔버스 단계를 받을 자격이 있는지 평가하는 데 사용됩니다.

{% alert important %}
이 구성에서는 **타겟 오디언스** 단계에 오디언스를 단일 채널로 제한하는 필터(예: `Foreground Push Enabled = True` 또는 `Email Subscription = Opted-In`)를 포함하지 마세요.
{% endalert %}

원하는 경우 캔버스에 대한 방해금지 시간(메시지가 전송되지 않는 시간)을 지정하세요. **전송 설정**에서 **방해금지 시간 활성화**를 체크하세요. 그런 다음 사용자의 현지 시간 기준으로 방해금지 시간을 선택하고 메시지가 해당 방해금지 시간 내에 트리거될 경우 수행할 작업을 선택합니다.

![방해금지 시간을 활성화하는 확인란이 표시된 '방해금지 시간' 페이지입니다. 활성화하면 시작 시간, 종료 시간 및 대체 동작을 설정할 수 있습니다.]({% image_buster /assets/img/quiet_hours.png %})

### 2단계: 캔버스 구축

{% alert tip %}
[Braze 캔버스 템플릿]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_templates/#available-braze-templates)을 사용하여 시간을 절약하고 캔버스 제작을 간소화하세요! 미리 구축된 템플릿 라이브러리를 검색하여 사용 사례에 맞는 템플릿을 찾고 특정 요구사항에 맞게 커스터마이즈하세요.
{% endalert %}

#### 2.1단계: 배리언트 추가

!['배리언트 추가' 버튼을 선택하면 '배리언트 추가' 옵션이 있는 컨텍스트 메뉴가 표시됩니다.]({% image_buster /assets/img_archive/canvas_add_variant.gif %}){: style="float:right;max-width:40%;margin-left:15px;"}

**배리언트 추가**를 선택한 다음 캔버스에 새 배리언트를 추가합니다. 배리언트는 사용자가 거치게 될 여정을 나타내며 여러 단계와 분기를 포함할 수 있습니다.

추가 배리언트를 추가하려면 <i class="fas fa-plus-circle"></i> 플러스 버튼을 선택하세요. 새 배리언트를 추가하면 사용자가 배리언트 간에 어떻게 분배될지를 조정할 수 있으므로 다양한 참여 전략의 효과를 비교 분석할 수 있습니다.

![Braze 캔버스의 두 가지 배리언트 예시입니다.]({% image_buster /assets/img_archive/Canvas_Multiple_Variants.png %})

{% alert tip %}
기본적으로, 사용자가 캔버스에 진입할 때 캔버스 배리언트 할당이 고정됩니다. 즉, 사용자가 처음 특정 배리언트에 진입하면, 이후 캔버스에 다시 진입할 때마다 해당 배리언트가 유지됩니다. 하지만 이 동작을 우회할 수 있는 방법이 있습니다. <br><br>이를 위해 Liquid를 사용하여 난수 생성기를 만들고 각 사용자의 캔버스 진입 시 실행하여 값을 커스텀 속성으로 저장한 다음 해당 속성을 사용하여 사용자를 무작위로 나눌 수 있습니다.

{% details 단계를 보려면 펼치세요 %}

1. 난수를 저장할 커스텀 속성을 만드세요. "lottery_number" 또는 "random_assignment"처럼 찾기 쉬운 이름을 지정하세요. [대시보드에서]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data/) 속성을 만들거나 [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)에 대한 API 호출을 통해 만들 수 있습니다.<br><br>
2. 캔버스의 시작 부분에 웹훅 캠페인을 만드세요. 이 캠페인은 난수를 생성하고 이를 커스텀 속성으로 저장하는 매개체가 됩니다. 자세한 내용은 [웹훅 만들기]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#step-1-set-up-a-webhook)를 참조하세요. URL을 `/users/track` 엔드포인트로 설정하세요.<br><br>
3. 난수 생성기를 만드세요. [여기에 설명된](https://community.shopify.com/c/technical-q-a/is-there-any-way-to-generate-random-number-with-liquid-shopify/m-p/1595486) 코드를 사용하면 각 사용자의 고유한 진입 시간을 활용하여 난수를 생성할 수 있습니다. 결과 숫자를 웹훅 캠페인 내에서 Liquid 변수로 설정하세요.<br><br>
4. 웹훅 캠페인에서 `/users/track` 호출을 포맷하여 1단계에서 생성한 커스텀 속성을 현재 사용자의 프로필에 생성한 난수로 설정하세요. 이 단계가 실행되면 사용자가 캠페인에 진입할 때마다 변경되는 난수를 성공적으로 만들 수 있습니다.<br><br>
5. 캔버스의 분기를 무작위로 선택된 배리언트 대신 오디언스 규칙에 따라 나뉘도록 조정하세요. 각 분기의 오디언스 규칙에서 커스텀 속성에 따라 오디언스 필터를 설정하세요. <br><br>예를 들어, 한 분기는 오디언스 필터로 "lottery_number가 3 미만"을, 다른 분기는 "lottery_number가 3 이상 6 미만"을 설정할 수 있습니다.

{% enddetails %}
{% endalert %}

#### 2.2단계: 캔버스 단계 추가

캔버스 워크플로우에 더 많은 단계를 추가하려면 **구성 요소** 사이드바에서 구성 요소를 드래그 앤 드롭하세요. 또는, <i class="fas fa-plus-circle"></i> 플러스 버튼을 선택하여 팝오버 메뉴에서 구성 요소를 추가하세요.

{% alert tip %}
단계를 추가하기 시작하면 세부 사항에 집중하거나 전체 사용자 여정을 파악하기 위해 확대/축소 수준을 변경할 수 있습니다. <kbd>Shift</kbd> + <kbd>+</kbd>로 확대하거나 <kbd>Shift</kbd> + <kbd>-</kbd>로 축소합니다.
{% endalert %}

![구성 요소 검색 창에서 Braze 캔버스에 지연 단계를 추가하는 모습입니다.]({% image_buster /assets/img_archive/add_components_flow.png %}){: style="max-width:80%;"}

{% alert important %}
캔버스에는 최대 200개의 단계를 추가할 수 있습니다. 캔버스가 200단계를 초과하면 로드 문제가 발생할 수 있습니다.
{% endalert %}

##### 최대 지속 시간

캔버스 여정의 단계가 증가함에 따라 최대 지속 시간은 사용자가 이 캔버스를 완료하는 데 걸릴 수 있는 가장 긴 시간입니다. 이는 가장 긴 경로에 대해 각 배리언트의 각 단계에 대한 지연 및 트리거 창을 합산하여 계산됩니다. 예를 들어, 캔버스에 3일의 지연이 있는 지연 단계와 메시지 단계가 있는 경우 캔버스의 최대 지속 시간은 3일입니다.

##### 단계 편집

사용자 여정의 단계를 편집하고 싶으신가요? 캔버스 워크플로우에 따라 편집하는 방법을 확인하세요!

구성 요소를 선택하여 캔버스 워크플로우의 모든 단계를 편집할 수 있습니다. 예를 들어, 워크플로우에서 첫 번째 단계인 [지연]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) 구성 요소를 특정 날짜로 편집하고자 하는 경우, 해당 단계를 선택하여 설정을 확인하고 지연을 3월 1일로 조정하세요. 이렇게 하면 3월 1일에 사용자가 캔버스의 다음 단계로 이동합니다.

![지연이 "특정 날짜까지"로 설정된 "지연" 단계의 예입니다.]({% image_buster /assets/img_archive/edit_delay_flow.png %})

또는 [행동 경로]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) 단계의 **작업 설정**을 빠르게 편집하고 조정하여 사용자를 일정 시간 동안 유지할 수 있습니다. 이 평가 기간 동안의 행동을 기반으로 다음 경로의 우선순위가 결정됩니다.

![캔버스의 두 번째 단계인 '작업 설정'에서 평가 기간이 1일로 설정되어 있습니다.]({% image_buster /assets/img_archive/action_paths_flow.png %})

캔버스의 경량 구성 요소는 간단한 편집 경험을 제공하므로 캔버스의 세부 사항을 더 쉽게 조정할 수 있습니다. 

##### 캔버스의 메시지

캔버스 구성 요소에서 메시지를 편집하여 특정 단계가 보낼 메시지를 제어합니다. 캔버스는 이메일, 모바일 및 웹 푸시 메시지와 웹훅을 보내 다른 시스템과 통합할 수 있습니다. 캠페인과 유사하게, 특정 [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/) 템플릿을 사용하여 메시지를 개인화할 수 있습니다.

{% alert tip %}
알고 계셨나요? 메시지 및 링크 템플릿에 캔버스 구성 요소 이름을 포함할 수 있습니다.<br>
캔버스에서 현재 캔버스 구성 요소 이름을 표시하려면 `campaign.${name}` Liquid 태그를 사용하세요.
{% endalert %}

메시지 구성 요소는 사용자에게 전송되는 메시지를 관리합니다. **메시징 채널**을 선택하고 **전달 설정**을 조정하여 캔버스 메시징을 최적화할 수 있습니다. 이 구성 요소에 대한 자세한 내용은 [메시지]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/)를 확인하세요.

!['메시지 설정' 단계에서 '메시징 채널'을 선택하면 Android 푸시, 콘텐츠 카드, 이메일 등과 같은 사용 가능한 메시징 채널 목록이 표시됩니다.]({% image_buster /assets/img_archive/message_setup_settings_flow.png %})

캔버스 구성 요소 구성을 완료한 후 **완료**를 선택하세요.

{% tabs local %}
{% tab Canvas Entry Properties %}

[`context` 객체]({{site.baseurl}}/api/objects_filters/context_object/)는 캔버스 생성의 **진입 스케줄** 단계에서 구성되며 사용자를 캔버스로 진입시키는 트리거를 나타냅니다. 이러한 속성은 API 트리거 캔버스의 진입 페이로드 속성에도 액세스할 수 있습니다. `context` 객체는 최대 50KB까지 가능합니다. 

캔버스 진입 시 생성된 이러한 속성을 참조할 때는 다음 Liquid를 사용합니다: {% raw %} ``context.${property_name}`` {% endraw %}. 이 방법을 사용하려면 이벤트가 커스텀 이벤트 또는 구매 이벤트여야 합니다.

{% raw %}
예를 들어 다음 요청을 고려해 보세요: `\"context\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. "shoes"라는 단어를 ``{{context.${product_name}}}`` Liquid를 사용하여 메시지에 추가할 수 있습니다.
{% endraw %}

{% endtab %}

{% tab Event Properties %}
이벤트 속성은 커스텀 이벤트 및 구매에 대해 사용자가 설정한 속성입니다. 이 `event_properties`는 캔버스뿐만 아니라 실행 기반 전달이 있는 캠페인에서도 사용할 수 있습니다. 

캔버스에서 커스텀 이벤트 및 구매 이벤트 속성은 행동 경로 단계 다음에 오는 모든 메시지 단계에서 Liquid로 사용할 수 있습니다. 이 `event_properties`를 참조할 때 {% raw %} ``{{event_properties.${property_name}}}`` {% endraw %} Liquid를 사용하세요. 메시지 구성 요소에서 이러한 방식으로 사용하려면 이벤트가 커스텀 이벤트 또는 구매 이벤트여야 합니다.

행동 경로 다음의 첫 번째 메시지 단계에서 해당 행동 경로에 참조된 이벤트와 관련된 `event_properties`를 사용할 수 있습니다. 이 행동 경로 단계와 메시지 단계 사이에 다른 단계(다른 행동 경로 또는 메시지 단계가 아닌)를 배치할 수 있습니다. 메시지 단계가 행동 경로 단계에서 모든 사람 경로가 아닌 경로로 추적될 수 있는 경우에만 `event_properties`에 액세스할 수 있습니다.

{% endtab %}
{% endtabs %}

#### 2.3단계: 연결 편집

단계 간 연결을 이동하려면 두 구성 요소를 연결하는 화살표를 선택하고 다른 구성 요소를 선택합니다. 연결을 제거하려면 화살표를 선택한 다음 캔버스 작성기의 바닥글에서 **연결 취소**를 선택하세요.

### 3단계: 대조군 추가

캔버스에 대조군을 추가하려면 <i class="fas fa-plus-circle"></i> 플러스 버튼을 선택하여 새 배리언트를 추가합니다. 

대조군에 포함된 사용자는 어떤 메시지도 수신하지 않지만, Braze는 해당 사용자의 전환을 추적합니다. 정확한 테스트를 유지하기 위해 전환 이벤트 선택 화면에 표시된 것과 정확히 동일한 기간 동안 배리언트와 대조군의 전환 수를 추적합니다. 

**배리언트 이름** 헤더를 더블 클릭하면 메시지 간 분포를 조정할 수 있습니다.

이 예에서는 캔버스를 두 가지 배리언트로 나누었습니다. 배리언트 1에는 사용자의 70%가 포함됩니다. 두 번째 배리언트는 대조군이며, 나머지 30%의 사용자로 구성됩니다.

![70%가 첫 번째 단계에서 하루 동안 지연된 후 두 번째 단계에서 메시지를 보내는 '배리언트 1'로 이동하는 Braze 캔버스의 배리언트 예시입니다. 나머지 30%는 후속 단계가 없는 '대조군'으로 이동합니다.]({% image_buster /assets/img_archive/Canvas_Multivariate_Flow.png %})

#### 캔버스를 위한 지능형 선택

지능형 선택 기능은 이제 다변량 캔버스 내에서 사용할 수 있습니다. 다변량 캠페인의 [지능형 선택]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/) 기능과 마찬가지로, 캔버스용 지능형 선택은 각 캔버스 배리언트의 성과를 분석하고 각 배리언트를 통해 유입되는 사용자의 비율을 조정합니다. 이 분포는 총 예상 전환 수를 최대화하기 위해 각 배리언트의 성과 측정기준을 기반으로 합니다.

다변량 캔버스를 사용하면 카피뿐만 아니라 타이밍과 채널도 테스트할 수 있다는 점을 기억하세요. 지능형 선택을 통해 캔버스를 더 효율적으로 테스트하고 사용자가 최적의 캔버스 여정을 경험할 수 있다는 확신을 가질 수 있습니다.

!['지능형 선택' 옵션이 '배리언트 분포 편집' 페이지에서 활성화되어 있습니다. 캔버스를 분석하고 최적화할 때 페이지 전체에 가로 막대가 표시되며, 이 가로 막대는 각각 색상과 크기가 다른 여러 섹션으로 나뉘어져 있습니다. 이는 시각적 표현일 뿐이며 특정 분석과 관련이 없습니다.]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

캔버스용 지능형 선택은 각 배리언트로 분류된 사용자 분포를 점진적으로 실시간 조정하여 캔버스 결과를 최적화합니다. 통계 알고리즘이 배리언트 중에서 확실한 승자를 결정하면, 성과가 저조한 배리언트를 배제하고 향후 캔버스의 모든 적격 수신자를 우승 배리언트에 배정합니다. 

이러한 이유로 지능형 선택은 새로운 사용자가 자주 진입하는 캔버스에서 가장 잘 작동합니다.

### 4단계: 저장 및 시작

캔버스 생성을 완료한 후 **캔버스 시작**을 선택하여 캔버스를 저장하고 시작합니다. 캔버스를 시작한 후에는 **캔버스 세부 정보** 페이지에서 여정의 분석을 확인할 수 있습니다. 

나중에 다시 작업해야 할 경우 캔버스를 초안으로 저장할 수도 있습니다.

![Braze의 캔버스 예시.]({% image_buster /assets/img_archive/Canvas_Analytics.png %})

{% alert tip %}
시작한 후 캔버스를 편집해야 하나요? 가능합니다! 자세한 내용은 [시작 후 캔버스 편집]({{site.baseurl}}/post-launch_edits/)을 확인하세요.
{% endalert %}