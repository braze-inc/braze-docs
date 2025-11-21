---
nav_title: 캠페인 및 캔버스
article_title: "시작하기: 캠페인 및 캔버스"
page_order: 3
page_type: reference
description: "이 문서에서는 Braze로 메시지를 보낼 수 있는 다양한 방법에 대한 개요를 제공합니다."

---

# 시작하기: 캠페인 및 캔버스

Braze에서는 [캠페인](#campaigns) 또는 [캔버스를](#canvas) 통해 메시지를 보낼 수 있습니다.

- 사용자 그룹에 하나의 타겟팅된 메시지를 보내려면 캠페인을 선택합니다. 캠페인은 다양한 메시징 채널에서 사용자와 소통하기 위한 단일 메시지 단계입니다.
- 중요한 고객 여정에서 일련의 지속적인 메시지를 보내려면 여정 오케스트레이션 도구인 캔버스를 선택하세요. 캠페인은 단순하고 타겟팅된 메시지를 보내는 데 적합하지만, 캔버스는 고객과의 관계를 한 단계 더 발전시킬 수 있는 곳입니다.

## 캠페인

캠페인은 채널에 따라 고유하게 구축할 수 있지만, Braze에서 알아두어야 할 네 가지 주요 캠페인 유형이 있습니다:

| 캠페인 유형        | 설명                                                                                                                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 일반              | 가장 일반적인 캠페인 유형입니다. 메시징 목표에 따라 하나 이상의 채널을 타겟팅할 수 있으며, 비주얼 에디터를 통해 Braze에서 직접 콘텐츠를 디자인, 커스텀 및 테스트할 수 있습니다. [캠페인을 만드는]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign) 방법을 알아보세요. |
| A/B 테스트          | 단일 채널을 타겟팅하는 캠페인의 경우 동일한 캠페인을 두 개 이상의 버전으로 전송하고 어떤 캠페인이 더 높은 순위를 차지하는지 확인할 수 있습니다. [다변량 캠페인을]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) 통해 최대 8가지 버전에 대해 카피, 개인화 등을 테스트할 수 있습니다. |
| API                  | [API 캠페인을]({{site.baseurl}}/api/api_campaigns/) 사용하면 최대한 신속하게 시의적절한 메시지를 보낼 수 있습니다. 다른 캠페인 유형과 달리, 메시지, 수신자 또는 일정을 Braze 대시보드에서 지정하지 않습니다. 대신 API 호출에 이러한 식별자를 전달합니다. 일반적으로 실시간 트랜잭션 메시징이나 뉴스 속보에 사용됩니다.  |
| 트랜잭션 이메일 | Braze [트랜잭션 이메일은]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign/) 판매자와 고객 간의 합의된 트랜잭션을 촉진하기 위해 자동화된 비프로모션 이메일 메시지를 전송하기 위해 특별히 구축된 기능입니다. 속도가 가장 중요한 비즈니스 크리티컬 알림을 단일 사용자에게 전송합니다. *일부 패키지에서 사용할 수 있습니다.* |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
정기 및 A/B 테스트 캠페인을 예약하거나(예: 예정된 이벤트에 대해 사용자 목록에 알리기) 사용자의 행동에 따라 이메일을 보내도록 자동화할 수 있습니다(예: 누군가가 뉴스레터에 가입하면 이메일 보내기). [캠페인 예약에]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types) 대해 자세히 알아보세요.
{% endalert %}

어떤 유형의 캠페인을 만들든 사용자의 요구에 귀 기울이고 사려 깊고 개인화된 응답을 제공할 수 있습니다. 캠페인을 전송한 후에는 [구축된 분석 도구를]({{site.baseurl}}/user_guide/analytics/reporting/) 사용하여 캠페인의 성능/성과와 [전환 이벤트에]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) 따라 전환한 사용자 수를 확인할 수 있습니다.

Braze의 캠페인에 대해 자세히 알아보려면 다음 추가 리소스를 확인하세요:

- Braze 학습: [캠페인 설정](https://learning.braze.com/campaign-setup-delivery-targeting-conversions)
- [캠페인 만들기]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign)
- [아이디어 및 전략]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies)

## 캔버스

캔버스는 여러 캠페인에 걸쳐 산발적으로 메시지를 보내는 대신 사용자와 지속적으로 유동적인 대화를 나눕니다. 캔버스를 통과하는 사용자의 여정은 브랜드에 대한 사용자의 행동(또는 무행동)에 따라 여러 경로로 나뉠 수 있으므로, 실시간으로 특정 흐름을 통해 사용자를 자동으로 진행할 수 있습니다.

\![]({% image_buster /assets/img/getting_started/canvas_flow.png %})

이러한 방식으로 캔버스는 전환 경로에서 이탈한 사용자를 포착하여 가장 효과적인 아웃리치 이니셔티브에 배치할 수 있는 그물을 던지는 데 유용합니다.

캔버스를 만들 때는 전체 오디언스, 참가 조건 및 전송 설정 지정 등 캠페인 설정과 동일한 단계를 많이 따릅니다. 누군가 트리거 조건과 일치하면 캔버스가 시작됩니다. 그런 다음 종료 조건을 충족할 때까지 캔버스의 경로를 따라 이동합니다.

캔버스에는 [메시지]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/), [지연]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/), [실험]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) 등을 자유롭게 조합할 수 있습니다. 지원되는 모든 메시징 채널에서 전송할 수 있으며, Facebook, Google, [TikTok과]({{site.baseurl}}/partners/canvas_audience_sync/overview/) 같은 [소셜 및 광고 플랫폼과 통합할]({{site.baseurl}}/partners/canvas_audience_sync/overview/) 수도 있습니다.

캔버스에 대해 자세히 알아보려면 다음 추가 리소스를 확인하세요:

- Braze 학습: [캔버스 플로우를 사용한 여정 오케스트레이션](https://learning.braze.com/path/journey-orchestration-with-canvas-flow)
- [캔버스 만들기]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)
- [캔버스 윤곽선]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/canvas_outlines/)

## 메시징 채널

메시징 채널은 고객 참여를 유도하고 타겟팅된 메시지를 전달할 수 있는 다양한 커뮤니케이션 채널입니다. 

\![]({% image_buster /assets/img/getting_started/channels.png %})

다음 표에는 지원되는 채널이 간략하게 나와 있습니다.

| 채널                                                                                              | 설명                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [이메일]({{site.baseurl}}/user_guide/message_building_by_channel/email/about/)                        | 사용자의 받은편지함에 개인화된 이메일을 보내세요.                                                                                                       |
| [모바일 푸시]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/)                   | 사용자의 모바일 기기에 알림으로 직접 메시지를 전달하세요.                                                                                   |
| [웹 푸시]({{site.baseurl}}/user_guide/message_building_by_channel/push/web)                         | 사용자가 웹사이트에 접속하지 않을 때에도 사용자의 웹 브라우저에 알림을 전달하세요.                                                         |
| [인앱 메시지]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/)    | 사용자가 모바일 앱을 활발하게 사용하는 동안 모바일 앱 내에 메시지를 표시하세요.                                                                             |
| [SMS, MMS 및 RCS*]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/)                   | 사용자의 휴대폰으로 문자 메시지를 보냅니다.                                                                                                            |
| [WhatsApp*]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/)              | 인기 메시징 플랫폼인 WhatsApp을 통해 메시지를 전송하여 사용자에게 다가가고 참여를 유도하세요.                                                   |
| [배너*]({{site.baseurl}}/user_guide/message_building_by_channel/banners/)       | 앱이나 웹사이트에 직접 메시지를 임베드하세요. |
| [콘텐츠 카드*]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/)       | 앱 또는 웹사이트 내에 사용자가 메시지를 수신하고 상호 작용할 수 있는 받은편지함을 제공하거나 캐러셀, 배너 등으로 메시지를 표시할 수 있습니다. |
| [커넥티드 TV]({{site.baseurl}}/developer_guide/platforms/tv_and_ott/)                           | 커넥티드 TV 플랫폼에서 사용자와 참여하세요.                                                                                                   |
| [웹훅]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/) | 커스텀 HTTP 콜백을 통해 외부 시스템과 실시간 커뮤니케이션 및 통합을 인에이블하세요.                                                    |
| [LINE]({{site.baseurl}}/user_guide/message_building_by_channel/line/) | 일본에서 가장 인기 있는 메시징 앱인 LINE에서 사용자들과 소통하세요.                                                    |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

<sup>\*\*애드온 기능으로 제공\*됩니다.</sup>

{% alert tip %}
대부분의 채널(이메일, SMS, 푸시)을 통해 전달할 수 있는 짧고 긴급한 메시지의 경우 [인텔리전트 채널]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/) 필터를 활용하여 각 사용자에게 가장 적합한 채널을 통해 메시지를 자동으로 전송하세요.
{% endalert %}

