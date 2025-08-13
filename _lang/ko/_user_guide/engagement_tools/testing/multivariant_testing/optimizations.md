---
nav_title: 최적화
article_title: 승리한 배리언트 또는 개인화된 배리언트로 A/B 테스트 최적화
page_order: 1
page_type: reference
description: "다변량 및 A/B 테스트를 만들 때 위닝 배리언트 또는 개인화된 변수를 사용하는 방법을 알아보세요."
---

# 승리한 배리언트 또는 개인화된 배리언트로 A/B 테스트 최적화

When [creating an A/B test]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/) for email, push, webhook, SMS, and WhatsApp campaigns scheduled to send once, you can select an optimization. 최적화 옵션은 두 가지가 있습니다: **배리언트 위닝** 및 **개인화된 배리언트**.

![타겟 오디언스를 선택할 때 A/B 테스트 섹션에 나열된 최적화 옵션을 선택합니다. 세 가지 옵션이 나열되어 있습니다: 최적화 없음, 이기는 변형 및 개인화된 변형. 개인화된 배리언트가 선택되었습니다.]({% image_buster /assets/img_archive/ab_personalized_variant.png %})

두 가지 옵션 모두 대상 세그먼트의 일부에 초기 테스트를 보내는 방식으로 작동합니다. 테스트가 끝난 후, 오디언스에 남아 있는 사용자에게는 가장 성과가 좋은 배리언트(위닝 배리언트) 또는 그들이 참여할 가능성이 가장 높은 배리언트(개인화된 배리언트)가 전송됩니다.

{% alert tip %}
최적화는 캠페인 생성의 **대상 오디언스** 단계에서 **A/B 테스트** 아래에 있습니다.
{% endalert %}

## 위닝 배리언트

위닝 배리언트를 보내는 것은 표준 A/B 테스트와 유사합니다. 이 그룹의 사용자는 초기 테스트가 완료되면 배리언트를 받게 됩니다.

1. **배리언트**를 선택한 다음, 캠페인 오디언스 중 몇 퍼센트를 배리언트 그룹에 할당할지 지정하세요.
2. 다음 추가 설정을 구성하십시오.

| 필드 | 설명 |
| --- | --- | 
| 위닝 배리언트 결정 | 최적화할 메트릭입니다. 이메일, 푸시, 또는 모든 채널에 대해 *고유 오픈* 또는 *클릭* 중에서 선택하거나 *오픈*을 선택하거나 *주요 전환율*을 선택하세요. *열람* 또는 *클릭*을 선택하여 위너를 결정하는 것은 캠페인의 [전환 이벤트]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/)에 대해 선택한 항목에 영향을 미치지 않습니다. <br><br>명심하세요, 대조군을 사용하는 경우 대조군의 사용자는 *열람* 또는 *클릭*을 수행할 수 없으므로 대조군의 성능은 `0`으로 보장됩니다. 결과적으로, 대조군은 A/B 테스트에서 이길 수 없습니다. 그러나 메시지를 받지 않는 사용자의 다른 측정기준을 추적하기 위해 여전히 대조군을 사용할 수 있습니다. |
| 위닝 배리언트 발송 시간 | 당첨된 이형 상품이 전송된 날짜와 시간입니다. |
| 위닝 배리언트를 결정할 수 없는 경우 | 통계적으로 유의미한 차이로 배리언트가 승리하지 못하면 어떻게 되나요. 최고 성능의 배리언트를 보내거나 테스트를 종료하고 더 이상 메시지를 보내지 않는 것 중에서 선택하세요. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 개인화된 배리언트

개인화된 배리언트를 사용하여 타겟 세그먼트의 각 사용자에게 가장 참여할 가능성이 높은 배리언트를 보내세요.

각 사용자에게 가장 적합한 배리언트를 결정하기 위해 Braze는 사용자 특성과 메시지 선호도 간의 연관성을 찾기 위해 대상 오디언스의 일부에게 초기 테스트를 보냅니다. 사용자가 초기 테스트에서 각 배리언트에 반응하는 방식에 따라 이러한 특성을 사용하여 나머지 사용자가 각 배리언트를 받을지 여부를 결정합니다. 연관성이 발견되지 않고 개인화할 수 없는 경우, 나머지 사용자에게 자동으로 전송되는 것은 위닝 배리언트입니다. 개인화된 배리언트가 결정되는 방법에 대해 자세히 알아보려면 [다변량 및 A/B 테스트 분석]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/multivariate_analytics/#personalized-variant)을 참조하세요.

1. **개인화된 배리언트**을 선택한 다음 캠페인 오디언스 중 몇 퍼센트를 개인화된 배리언트 그룹에 할당할지 지정합니다.
2. 다음 추가 설정을 구성하십시오.

| 필드 | 설명 |
| --- | --- | 
| 개인화된 배리언트 결정 | 최적화할 메트릭입니다. 이메일, 푸시, 또는 모든 채널에 대해 *고유 오픈* 또는 *클릭* 중에서 선택하거나 *오픈*을 선택하거나 *주요 전환율*을 선택하세요. *열람* 또는 *클릭*을 선택하여 위너를 결정하는 것은 캠페인의 [전환 이벤트]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-events)에 대해 선택한 항목에 영향을 미치지 않습니다. <br><br>명심하세요, 대조군을 사용하는 경우 대조군의 사용자는 *열람* 또는 *클릭*을 수행할 수 없으므로 대조군의 성능은 `0`으로 보장됩니다. 결과적으로, 대조군은 A/B 테스트에서 이길 수 없습니다. 그러나 메시지를 받지 않는 사용자의 다른 측정기준을 추적하기 위해 여전히 대조군을 사용할 수 있습니다. |
| 개인화된 배리언트 발송 시간 | 개인화된 이형 상품이 전송되는 날짜와 시간입니다. |
| 개인화된 변형을 결정할 수 없는 경우 | 개인화된 변형이 발견되지 않으면 어떻게 되나요. 대신에 위닝 배리언트를 보내거나 테스트를 종료하고 더 이상 메시지를 보내지 않는 것 중에서 선택하세요. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 분석

To learn about the results of your A/B test with an optimization, refer to [Multivariate and A/B test analytics]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/multivariate_analytics/).

