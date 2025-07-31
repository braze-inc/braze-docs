---
nav_title: 캔버스 기본 사항
article_title: 캔버스 기본 사항
page_order: 1
page_type: reference
description: "이 참조 문서에서는 캔버스의 기본 사항을 다루며, 캔버스를 처음 설정할 때 스스로에게 물어봐야 할 다양한 질문을 다룹니다."
tool: Canvas

---

# 캔버스 기본 사항

> 이 참조 문서에서는 캔버스의 기본 사항을 다루며, 캔버스를 처음 설정할 때 스스로에게 물어봐야 할 다양한 질문을 다룹니다. 또한 시각화의 다섯 가지 W(무엇을, 언제, 누가, 왜, 어디서)와 이를 통해 캔버스를 어떻게 구성하고 정의할 수 있는지 설명합니다.

## 캔버스 구조 이해

[캔버스 설정에]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) 대한 자세한 내용을 시작하기 전에 캔버스를 구성하는 주요 부분을 파악해 보겠습니다.

{% tabs %}
  {% tab 캔버스 %}
  캔버스는 마케터가 여러 메시지로 캠페인을 제작할 수 있는 통합 인터페이스입니다. 시각적 프로그래밍 도구와 비슷하며 일련의 단계를 통해 일관된 사용자 여정을 구축할 수 있습니다.

  ![An example of a Canvas with a Decision Split step into two different user journeys depending if a user is push enabled.]({% image_buster /assets/img/canvas_intro/canvas_intro.gif %})

  {% endtab %}

  {% tab 여정 %}

  여정 또는 일반적으로 사용자 여정이라고 하는 것은 캔버스 내에서 개별 사용자의 경험을 의미합니다.<br><br> ![A chart with the customer journey for a new user. An anonymous user installs an app, Kat creates an account, Kat doesn't open the app for a week, a push notification brings Kat back to the app, then Kat uses the app regularly.]({% image_buster /assets/img_archive/Journey_2.png %}){: style="max-width:90%;"}

  {% endtab %}

  {% tab 캔버스 빌더 %}
  캔버스 빌더는 캔버스를 만들 때 수행해야 할 단계를 매핑합니다. 여기에는 캔버스 이름 지정 및 팀 추가와 같은 기본 사항이 포함됩니다. 기본적으로 캔버스 빌더는 캔버스 제작을 시작하기 전에 필요한 중요한 설정입니다. 여기에서 [응모 일정]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2b-set-your-canvas-entry-schedule), [대상 오디언스]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2c-set-your-target-entry-audience) 및 [전송 설정]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2d-select-your-send-settings)을 편집하는 옵션을 사용하여 사용자가 고객 여정을 시작하고 완료하는 방식을 제어할 수 있습니다.<br><br> ![The Canvas builder on the Basics section for a Canvas named "New Canvas".]({% image_buster /assets/img_archive/canvas_flow_entry_wizard.png %}){: style="max-width:90%;"}

  {% endtab %}

  {% tab 변형 %}
  배리언트는 각 고객이 여정에서 따라가는 경로입니다. 캔버스는 대조군과 함께 최대 8개의 배리언트 상품을 지원합니다. 각 배리언트를 팔로우할 오디언스 세그먼트를 제어할 수 있습니다.<br><br> ![Selecting the "Add Variant" button.]({% image_buster /assets/img/canvas_intro/add_canvas_variant.gif %})

  {% endtab %}

  {% tab 단계 %}
  캔버스의 한 단계는 "이 경우 저걸 한다"라는 마케팅 의사 결정 포인트입니다. [캔버스 구성 요소를]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/#about-canvas-components) 활용하여 사용자 여정의 단계를 구축하세요.<br><br> ![Example of adding a Delay step to a Canvas.]({% image_buster /assets/img/canvas_intro/add_canvas_step.gif %}) <br><br> When a user enters a Canvas, they start at the first step. Each step has conditions that determine whether a user can move to the next step. 한 단계 내에서 트리거를 설정하거나 전송 일정을 예약하고, 필터를 추가하거나 예외 이벤트를 표시하여 타겟팅을 구체화하고, 푸시 알림이나 웹훅 이벤트와 같은 다양한 채널을 지정할 수 있습니다. In Canvas, steps occur in a sequence, meaning the first step occurs before the second step can occur. Let's say we have a Canvas with the following steps: Delay step A with a 24-hour delay, Message step A with a push message, and Message step B with an in-app message. User A is held in a 24-hour delay, then, after 24-hours, they will receive a push message, then an in-app message.

  {% endtab %}
{% endtabs %}

## 고객 여정 구축

시각화의 5가지 W(무엇을, 언제, 누가, 왜, 어디서)를 사용하면 각 사용자를 위한 개인화된 메시지 여정을 만드는 방법에 대한 고객 참여 전략을 파악하는 데 도움이 될 수 있습니다.

### "무엇": 캔버스에 이름 지정

> 사용자가 무엇을 하도록 돕거나 이해하도록 돕고 있나요?

이름이 가진 힘을 절대 과소평가하지 마세요. Braze는 협업을 위해 만들어졌으므로 지금이 팀과 목표를 공유하는 방법에 대해 알아볼 수 있는 좋은 시기입니다.

캔버스에서 태그를 추가하고 단계 및 이형 상품의 이름을 지정할 수 있습니다. 고객 여정에 대한 자세한 내용은 [사용자 라이프사이클 매핑](https://learning.braze.com/mapping-customer-lifecycles)에 대한 Braze 학습 과정을 확인하세요.

### "왜": 전환 이벤트 식별

> '무엇'을 기반으로 이 캔버스를 구축하는 이유는 무엇인가요? 

항상 명확한 목표를 염두에 두는 것이 중요하며, 캔버스는 세션 인게이지먼트, 구매 및 커스텀 이벤트와 같은 KPI에 대한 성과를 파악하는 데 도움이 됩니다.

하나 이상의 [전환 이벤트]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/)를 선택하면 캔버스 내에서 성능을 최적화하는 방법을 이해할 수 있습니다. 또한 캔버스에 여러 변형 또는 대조 그룹이 있는 경우, Braze는 전환 이벤트를 사용하여 이 목표를 달성하는 데 가장 적합한 변형을 결정합니다.

* **세션 시작**: 사용자가 다시 돌아와서 앱에 참여하기를 바랍니다.
* **구매하기**: 사용자가 구매하기를 원합니다.
* **커스텀 이벤트 수행**: 사용자가 커스텀 이벤트로 추적 중인 특정 작업을 수행하도록 하고 싶습니다.
* **앱 업그레이드:** 사용자가 앱 버전을 업그레이드하기를 원합니다.

### "언제": 시작 조건 만들기

> 사용자는 언제 이 경험을 시작하나요?

답변에 따라 캔버스가 고객에게 전달되는 시기와 방법에 대한 세부 정보가 결정됩니다. 사용자는 예약 또는 액션 기반 트리거 중 한 가지 방법으로 캔버스에 입장할 수 있습니다.

{% alert tip %}
더 많은 전략과 일반적인 질문에 대한 답변은 Canvas의 [시간 기반 기능에서]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/delivery_types/) 확인하세요.
{% endalert %}

예약된 전달을 사용하면 오디언스에게 즉시 캔버스를 보낼 수 있습니다. 정기적으로 보내거나 향후 특정 시간으로 예약할 수도 있습니다. 액션 기반 캔버스는 특정 고객 행동이 발생하면 그에 따라 반응합니다. 예를 들어, 액션 기반 트리거에는 앱 열기, 구매, 다른 캠페인과의 상호 작용 또는 커스텀 이벤트 트리거 등이 포함될 수 있습니다. 작업이 발생하는 시점에 캔버스가 사용자에게 전송하도록 할 수 있습니다.

### "누구": 대상 선택

> 누구에게 연락하려는 대상인가요? 

"대상"을 정의하려면 캔버스에서 제공되는 사전 정의된 세그먼트를 사용할 수 있습니다. 필터를 더 추가하여 타겟 오디언스와의 연결에 더욱 집중할 수도 있습니다. 이러한 세그먼트를 구축한 후에는 타겟 고객 기준과 일치하는 사용자만 캔버스 여정에 진입할 수 있으므로 보다 개인화된 경험을 제공할 수 있습니다. 사용 가능한 필터와 사용 사례에 맞게 사용자를 세분화하는 방법은 이 표를 참조하세요.

| 필터              | 설명                                                                                         |
|---------------------|-----------------------------------------------------------------------------------------------------|
| 사용자 지정 데이터         | 정의한 이벤트와 속성을 기반으로 사용자를 세분화하세요. 제품별 기능을 사용할 수 있습니다. |
| 사용자 활동       | 고객의 행동과 구매를 기반으로 고객을 세분화하세요.                                             |
| 리타겟팅         | 이전 캔버스와 주고받거나 상호작용한 적이 있는 고객을 세분화합니다.               |
| 마케팅 활동  | 마지막 참여와 같은 보편적인 행동을 기반으로 고객을 세분화하세요.                         |
| 사용자 속성     | 고객의 지속적인 속성과 특성에 따라 고객을 세분화하세요.                                 |
| 설치 기여도 | 첫 번째 소스, 광고 그룹, 캠페인 또는 광고별로 고객을 세분화합니다.                                 |

### '어디': 내 잠재 고객 찾기

> 잠재 고객에게 가장 잘 도달할 수 있는 곳은 어디인가요? 

이를 통해 사용자 여정에 가장 적합한 메시징 채널을 결정합니다. 이상적으로는 사용자가 가장 접근하기 쉬운 곳에서 사용자에게 도달하는 것이 좋습니다. 이를 염두에 두고 다음 채널 중 하나를 캔버스와 함께 사용할 수 있습니다.
* [이메일]({{site.baseurl}}/user_guide/message_building_by_channel/email/about/)
* [푸시]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/)
* [인앱 메시지]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/)
* [콘텐츠 카드]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/)
* [SMS 또는 MMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/about_sms/)
* [웹훅]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/)

### "방법": 완벽한 경험 구축

> 다섯 가지 W를 파악한 후 캔버스 여정을 어떻게 구축하나요?

'방법'은 캔버스를 만드는 방법과 메시지를 사용자에게 전달하는 방법을 총체적으로 요약한 것입니다. 예를 들어, 메시지의 효과를 높이려면 다양한 사용자의 시간대를 고려하여 메시지의 타이밍을 최적화해야 합니다.

"어떻게"에 대한 답변에 따라 오디언스에게 캔버스를 보내는 주기(예: 주 1회 또는 격주)와 "어디"에 설명된 대로 구축한 각 캔버스에 대해 활용할 메시징 채널도 결정됩니다.

## 사용 사례: 고객 온보딩 흐름

예를 들어 온라인 스트리밍 서비스 회사인 MovieCanon의 마케터로서 앱의 신규 사용자를 위한 온보딩 플로우를 만드는 일을 담당한다고 가정해 보겠습니다. 다섯 가지 W를 참조하여 다음과 같은 방식으로 캔버스를 구축할 수 있습니다.

* **What**: 캔버스 이름은 "새로운 온보딩 여정"이 될 것입니다.
* **Why**: 캔버스의 목표는 사용자를 환영하고 앱에 계속 참여하도록 하는 것입니다.
* **언제**: 사용자가 앱을 처음 열면 환영 이메일을 보내려고 합니다. 
* **Who**: 저희는 앱을 처음 사용하는 신규 사용자를 타겟팅하고 있습니다.
* **Where**: 우리는 과거에 모든 메시지를 전달했던 방식인 이메일을 통해 새로운 사용자에게 도달할 수 있다고 확신합니다.
* **방법**: 신규 사용자에게 알림을 너무 많이 보내지 않도록 하루 지연을 설정하려고 합니다. 이 기간이 지나면 가장 인기 있는 영화와 TV 프로그램 목록이 포함된 이메일을 보내 앱을 계속 사용하도록 유도할 것입니다.

## 일반 팁

### 단계 및 변형 사용 시기 및 방법 결정하기

각 캔버스에는 적어도 하나의 변형과 적어도 하나의 단계가 있어야 합니다. 캔버스의 모양은 어떻게 결정할 수 있을까요? 여기서 목표, 데이터, 가설이 중요한 역할을 합니다. '어떻게'와 '어디에' 브레인스토밍을 하면 캔버스의 올바른 모양과 구조를 구상하는 데 도움이 됩니다.

### 거꾸로 작업

일부 목표에는 더 작은 하위 목표가 있습니다. 예를 들어 무료 사용자를 정기구독으로 전환하려는 경우 정기구독 서비스에 대한 개요가 포함된 페이지가 필요할 수 있습니다. 방문자는 구매하기 전에 옵션을 확인해야 할 수 있습니다. 결제 페이지 전에 이 페이지를 표시하는 데 메시징 노력을 집중할 수 있습니다. 고객이 목표에 도달하기 위해 거쳐야 하는 여정을 역으로 이해하는 것은 고객을 전환으로 유도하는 데 있어 핵심입니다.

### 메시징 혼합

과거에 비슷한 캠페인을 진행한 적이 있나요? 아니면 현재 실행 중이신가요? 이 하나의 메시지를 사용하여 더 많은 개인화 기능을 추가해 보세요. 새 필터를 사용하거나 후속 메시지를 추가하세요. 메시징 기술을 혼합하면서 성능을 모니터링하고 점진적으로 변경하여 계속 최적화하세요.
