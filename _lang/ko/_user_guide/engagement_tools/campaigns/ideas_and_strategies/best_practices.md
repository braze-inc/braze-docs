---
nav_title: 모범 사례
article_title: 캠페인 모범 사례
page_order: 0
description: "이 기사는 캠페인을 생성하고 사용자 정의하는 데 대한 모범 사례를 제공합니다."
tool: Campaign

---

# 캠페인 모범 사례

## 브레이즈의 네 가지 T

브레이즈는 브레이즈 플랫폼에서 활용할 의도가 있는 고객 데이터만 전송할 것을 권장합니다. 브레이즈의 "네 가지 T" 철학을 고려하여 사용할 데이터를 전송하도록 하십시오:

- **대상** [청중 세그먼트]({{site.baseurl}}/user_guide/engagement_tools/segments/)를 구축하여 귀하의 청중을 타겟팅하십시오.
- **메시지 트리거** [행동 기반]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery#action-based-delivery) 또는 [API 트리거]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) 전송으로 귀하의 메시지를 트리거하십시오.
- **템플릿**을 만들고 [Liquid 조건 논리]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid)로 메시지를 개인화하십시오.
- **추적** [전환 추적]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/)으로 캠페인의 효율성을 추적하십시오.

이것은 브레이즈에 전송하는 데이터를 최적화할 수 있게 해주며, 팀이 장기적으로 유용하지 않다고 생각할 수 있는 데이터 포인트를 추적하는 것을 보장하면서 사용자에게 메시지를 전송하는 능력을 간소화합니다. 

## 사용자 타겟팅

시간이 지남에 따라 캠페인을 구축하면서 청중의 공백을 발견할 수 있습니다. 이 중요한 시점에서, 세분화를 사용하여 [공백 사용자]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/)를 전문화된 캠페인으로 타겟팅할 수 있습니다. 

### 청중 식별

세그먼트와 필터를 활용하여 청중을 정의함으로써 귀하에게 유리하게 활용하십시오. 귀하의 캠페인과 메시지가 누구를 타겟팅하고 있는지 고려하십시오. 이 중요한 정보를 통해 귀하는 청중의 알림 선호도에 맞춰 다양한 채널에서 메시지를 구축할 수 있는 유연성을 제공하는 [다채널 캠페인]({{site.baseurl}}/user_guide/engagement_tools/campaigns/faq/#how-do-you-create-a-multichannel-campaign)을 생성할 수 있습니다.

또한, 일관된 사용자에게 감사를 표하기 위해 [활성 사용자]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/active_user_campaigns/)를 이해하는 것이 중요합니다.

## 멀티채널 캠페인

### 기능 인식

사용자를 새로운 기능이나 앱 버전으로 유도하는 것이 목표라면, 인앱 채널에 중점을 둔 멀티채널 전략을 사용하세요. [인앱 메시지]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/)와 [콘텐츠 카드]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/)는 사용자가 즉시 업데이트를 원하지 않을 경우 일반적으로 덜 방해가 됩니다. 

적절한 앱 스토어에 대한 [딥 링크]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/)를 포함하는 것을 잊지 마세요.

사용자가 앱을 업데이트하거나 앱 사용 방식을 변경하도록 설득하는 것은 어려울 수 있으므로, 새로운 버전이나 기능의 모든 이점과 그것이 사용자 경험을 어떻게 개선할 것인지 알려주세요. 

### 전송 타이밍

타이밍이 핵심입니다! 사용자를 앱 업데이트로 설득하는 것이 목표라면, 사용자가 앱 내에서 긍정적인 경험을 할 때까지 기다렸다가 요청하세요. 청중의 참여를 유지하려면 침해로 보일 수 있는 반복적인 메시지를 피하세요.

시간이 지나면 사용자는 특정 기능을 잊거나 새로운 기능을 인식하지 못할 수 있습니다. 새로운 기능이 추가되면 [인앱 메시지]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/)로 사용자에게 알려주세요. 사용자가 앱 내 주요 기능에 참여하지 않는 경우, 사용자가 앱에 참여할 때와 이 새로운 기능이 유용할 때 상기시켜주는 것이 좋습니다. [데이터 옵트인]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/)에 대한 우리의 기사에는 요청이 사용자의 작업 흐름 기대에 부합하는지 확인하는 방법에 대한 더 많은 정보가 있습니다. 

## 높은 평가

앱 스토어에서 별 5개 평가를 받는 것은 모든 모바일 마케터의 소원 목록에 있습니다. 긍정적인 리뷰를 얻는 것은 쉽지 않은 작업입니다. 왜냐하면 사용자의 추가 작업이 필요하기 때문입니다. 우리의 기능을 기발한 방식으로 적용함으로써 고객 참여를 증가시킬 수 있도록 도와드릴 수 있습니다.

### 파워 사용자 타겟팅

파워 사용자는 귀하의 앱을 홍보할 수 있는 지지자가 될 수 있습니다. 종종 그들은 귀하의 앱과 일관되게 상호작용하며 귀하의 앱을 개선하기 위한 피드백을 제공할 수 있습니다. 앱마다 다르지만, 파워 유저는 다음과 같은 경향이 있습니다:

- 많은 세션을 기록했습니다.
- 최근에 앱을 사용했습니다.
- 돈을 쓰고 구매했습니다.

더 높은 평가를 보장하기 위해, 파워 유저에게 앱 스토어에서 귀하의 앱을 리뷰해 달라고 요청하세요. 그들은 좋은 말을 할 가능성이 더 높습니다. 예를 들어, 다음 필터를 사용하여 "파워 유저"라는 세그먼트를 만들 수 있습니다:
- 지난 14일 동안 이 앱을 10회 이상 사용했습니다.
- 50달러 이상을 지출했습니다.

\![앱의 파워 유저를 타겟으로 하는 세그먼트의 예.]({% image_buster /assets/img_archive/ratings_power_users.png %})

앱 스토어를 방문하는 것은 사용자에게 시간이 걸립니다. 그들이 추가 노력을 기울일 가능성을 극대화하기 위해, 귀하의 앱에서 긍정적인 경험을 한 후에 평가나 리뷰를 요청하세요. 예를 들어, 게임 레벨을 클리어하거나 할인 코드를 사용하여 구매한 후에 요청하세요. [데이터 옵트인]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states)에 대한 우리의 기사에는 귀하의 요청이 사용자 작업 흐름 기대에 부합하도록 보장하는 방법에 대한 더 많은 정보가 있습니다.

## 캠페인 일정 예약하기

캠페인 일정이나 대상을 편집할 때 다음의 모범 사례를 참고하세요:

- **일회성 일정 캠페인:** 예정된 발송 시간까지 캠페인을 편집할 수 있습니다.
- **정기적으로 예약된 캠페인:** 예정된 발송 시간까지 캠페인을 편집할 수 있습니다.
- **지역 발송 시간 캠페인:** 예정된 발송 시간 24시간 전에는 수정하지 마십시오.
- **최적 발송 시간 캠페인:** 캠페인이 발송될 날 자정 24시간 전에는 수정하지 마십시오.

{% alert note %}
실시간 캠페인을 편집하고 배달을 **지역 발송 시간**으로 변경하면 새로운 메시지 배치가 대기열에 추가되어 사용자가 메시지를 두 번 받게 됩니다. 이를 방지하려면 먼저 원래 캠페인을 중지한 다음 일정을 업데이트한 후 복제본을 시작하십시오.
{% endalert %}

