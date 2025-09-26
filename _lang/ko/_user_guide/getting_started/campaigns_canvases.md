---
nav_title: 캠페인 및 캔버스
article_title: "시작하기: 캠페인 및 캔버스"
page_order: 3
page_type: reference
description: "이 문서는 Braze를 사용하여 메시지를 보낼 수 있는 다양한 방법에 대한 개요를 제공합니다."

---

# 시작하기: 캠페인 및 캔버스

Braze에서 메시지는 [캠페인](#campaigns) 또는 [캔버스](#canvas-flow)를 통해 보낼 수 있습니다.

- 단일 타겟 메시지를 사용자 그룹에 보내려면 캠페인을 선택하세요. 캠페인은 다양한 메시징 채널에서 사용자와 연결하기 위한 단일 메시지 단계입니다.
- 지속적인 메시지 시리즈를 전체적인 고객 여정에서 보내려면 캔버스 플로우를 선택하세요. 캔버스 플로우는 여정 오케스트레이션 도구입니다. 캠페인은 간단하고 타겟팅된 메시지를 보내는 데 좋지만, 캔버스는 고객과의 관계를 한 단계 끌어올리는 곳입니다.

## 캠페인

캠페인은 채널에 따라 고유하게 구축될 수 있지만, Braze에서 알아야 할 주요 캠페인 유형은 네 가지입니다:

| 캠페인 유형        | 설명                                                                                                                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 정규              | 이것은 가장 일반적인 유형의 캠페인입니다. 메시징 목표에 따라 하나 이상의 채널을 타겟팅하고, Braze에서 시각적 편집기를 사용하여 콘텐츠를 직접 설계, 맞춤화 및 테스트할 수 있습니다. [캠페인을 만드는 방법을 배우세요]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign). |
| A/B 테스트          | 단일 채널을 타겟팅하는 캠페인의 경우, 동일한 캠페인의 여러 버전을 보내고 어떤 버전이 가장 좋은지 확인할 수 있습니다. 최대 8개의 다른 버전으로 [다변량 캠페인]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/)을 통해 카피, 개인화 등을 테스트할 수 있습니다. |
| API                  | [API 캠페인]({{site.baseurl}}/api/api_campaigns/)을 통해 가능한 한 빨리 시기적절한 메시지를 보낼 수 있습니다. 다른 캠페인 유형과 달리, Braze 대시보드에서 메시지, 수신자 또는 일정을 지정하지 않습니다. 대신 이러한 식별자를 API 호출에 전달합니다. 이들은 일반적으로 실시간 거래 메시징 또는 속보에 사용됩니다.  |
| 트랜잭션 이메일 | Braze [트랜잭션 이메일]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign/)은 귀하와 고객 간의 합의된 거래를 촉진하기 위해 자동화된 비프로모션 이메일 메시지를 보내도록 목적에 맞게 설계되었습니다. 속도가 가장 중요한 단일 사용자에게 비즈니스에 중요한 알림을 보냅니다. *선택한 패키지에 사용할 수 있습니다.* |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
정기 및 A/B 테스트 캠페인은 예정된 일정에 따라 (예: 다가오는 이벤트에 대해 사용자 목록에게 알림) 또는 사용자의 행동에 대한 응답으로 자동으로 발송될 수 있습니다 (예: 누군가가 뉴스레터를 구독할 때 이메일을 보내는 경우). [캠페인 일정]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types)에 대해 자세히 알아보세요.
{% endalert %}

캠페인의 유형에 관계없이, 캠페인은 사용자의 요구를 듣고 사려 깊고 개인화된 응답을 제공할 수 있습니다. After you've sent your campaign, use our [built-in analytics tools]({{site.baseurl}}/user_guide/analytics/reporting/) to see how it performed and how many users converted based on your [conversion events]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/).

Braze에서 캠페인에 대해 자세히 알아보려면 다음 추가 리소스를 확인하세요:

- Braze 학습센터: [캠페인 설정](https://learning.braze.com/campaign-setup-delivery-targeting-conversions)
- [캠페인을 생성하세요]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign)
- [아이디어와 전략]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies)

## 캔버스 플로우

여러 캠페인에 걸쳐 산발적인 메시지를 보내는 대신, 캔버스는 사용자와 지속적인 유동적인 대화를 만듭니다. 이것은 사용자가 캔버스를 통해 이동하는 과정이 브랜드와의 상호작용(또는 비상호작용)에 따라 다른 경로로 나뉠 수 있기 때문에, 실시간으로 특정 흐름을 통해 사용자를 자동으로 진행시킬 수 있게 해줍니다.

![]({% image_buster /assets/img/getting_started/canvas_flow.png %})

이와 같이, 캔버스는 전환 경로에서 이탈한 사용자를 포착하여 가장 효과적인 아웃리치 이니셔티브에 배치하는 데 훌륭합니다.

캔버스를 만들 때 캠페인을 설정하는 것과 동일한 단계를 따릅니다: 전체 오디언스, 진입 조건 및 전송 설정을 지정합니다. 사용자의 캔버스는 누군가가 트리거 조건과 일치할 때 시작됩니다. 그런 다음 그들은 캔버스의 경로를 따라 이동하여 종료 조건을 충족할 때까지 이동합니다.

캔버스는 [메시지]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/), [지연]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/), [실험]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) 등 다양한 조합을 가질 수 있습니다. You can send on any supported messaging channel, and even [integrate with social and ad platforms]({{site.baseurl}}/partners/canvas_audience_sync/overview/) such as Facebook, Google, or TikTok.

캔버스 플로우에 대해 더 알아보려면 추가 리소스를 확인하세요.

- Braze 학습센터: [여정 오케스트레이션과 캔버스 흐름](https://learning.braze.com/path/journey-orchestration-with-canvas-flow)
- [캔버스를 만들기]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)
- [캔버스 윤곽]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/canvas_outlines/)

## 메시징 채널

메시징 채널은 고객과 소통하고 타겟 메시지를 전달할 수 있는 다양한 커뮤니케이션 채널입니다. 

![]({% image_buster /assets/img/getting_started/channels.png %})

다음 표는 지원되는 채널을 설명합니다.

| 채널                                                                                              | 설명                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [이메일]({{site.baseurl}}/user_guide/message_building_by_channel/email/about/)                        | 사용자의 받은 편지함으로 개인화된 이메일을 보내세요.                                                                                                       |
| [모바일 푸시]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/)                   | 사용자의 모바일 장치로 알림을 직접 전달합니다.                                                                                   |
| [웹 푸시]({{site.baseurl}}/user_guide/message_building_by_channel/push/web)                         | 사용자가 귀하의 웹사이트에 적극적으로 접속하지 않아도 웹 브라우저에 알림을 전달합니다.                                                         |
| [인앱 메시지]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/)    | 사용자가 앱을 적극적으로 사용하는 동안 모바일 앱 내에 메시지를 표시합니다.                                                                             |
| [SMS, MMS, and RCS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/)*                   | 사용자의 휴대폰으로 문자 메시지를 보내세요.                                                                                                            |
| [WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/)*              | 인기 있는 메시징 플랫폼인 WhatsApp을 통해 메시지를 보내고 사용자와 소통하세요.                                                   |
| [Banners]({{site.baseurl}}/user_guide/message_building_by_channel/banners/)*       | Embed messages directly in your app or website. |
| [콘텐츠 카드]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/)*       | 앱 또는 웹사이트 내에서 사용자가 메시지를 수신하고 상호작용할 수 있는 받은편지함을 제공하거나, 메시지를 캐러셀, 배너 등으로 표시합니다. |
| [Connected TV]({{site.baseurl}}/developer_guide/platforms/tv_and_ott/)                           | 연결된 텔레비전 플랫폼에서 사용자와 소통하세요.                                                                                                   |
| [웹훅]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/) | 외부 시스템과의 실시간 통신 및 통합을 커스텀 HTTP 콜백을 통해 활성화합니다.                                                    |
| [LINE]({{site.baseurl}}/user_guide/message_building_by_channel/line/) | Engage with users on LINE, the most popular messaging app in Japan.                                                    |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

<sup>\*\*추가 기능으로 제공됩니다.*</sup>

{% alert tip %}
짧고 긴급한 메시지를 대부분의 채널(이메일, SMS, 푸시)을 통해 전달할 수 있는 경우, [인텔리전트 채널]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/) 필터를 활용하여 각 사용자에게 가장 적합한 채널을 통해 메시지를 자동으로 전송하세요.
{% endalert %}

