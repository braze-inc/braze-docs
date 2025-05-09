---
nav_title: 다변량 및 A/B 테스트
article_title: 다변량 및 A/B 테스트
page_order: 2
page_type: reference
description: "이 참조 문서에서는 다변량 및 A/B 테스트와 그 이점에 대해 설명합니다."
search_rank: 2
---

# 다변량 및 A/B 테스트

> 이 페이지에서는 다변량 및 A/B 테스트의 정의와 이점에 대해 설명합니다. 다변량 또는 A/B 테스트를 만드는 방법에 대한 단계는 [Braze로 다변량 및 A/B 테스트 만들기]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/)를 참조하세요. 

[지능형 선택]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/)을 사용하여 다변량 및 A/B 테스트를 사용할 수 있습니다.

## 다변량 및 A/B 테스트란 무엇인가요?

### A/B 테스트

A/B 테스트는 동일한 마케팅 캠페인의 여러 버전에 대한 사용자의 반응을 비교하는 실험입니다. 이 버전은 비슷한 마케팅 목표를 공유하지만 문구와 스타일이 다릅니다.

목표는 마케팅 목표를 가장 잘 달성할 수 있는 캠페인 버전을 식별하는 것입니다. 이 섹션에서는 콘텐츠 차이의 효과를 테스트하는 방법을 살펴봅니다.

{% alert note %}
메시지 예약 또는 타이밍의 차이를 평가하려면(예: 1시간 동안 활동이 없는 경우와 하루 동안 활동이 없는 경우의 유기한 장바구니 메시지 보내기) [캔버스 설정]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) 섹션을 참조하세요.
{% endalert %}

푸시 알림에 대한 두 가지 옵션이 있다고 가정해 보겠습니다:

- "이 거래는 내일 만료됩니다!"
- "이 거래는 24시간 후에 만료됩니다!"

A/B 테스트를 통해 어떤 문구가 더 높은 전환율을 가져오는지 확인할 수 있습니다. 다음에 거래에 대한 푸시 알림을 보낼 때 어떤 유형의 문구가 더 효과적인지 알 수 있습니다. 그러나 이 테스트는 푸시 알림의 복사본이라는 한 가지 변수의 효과만 검사합니다.

### 다변량 테스트

다변량 테스트는 두 개 이상의 변수의 효과를 테스트한다는 점을 제외하면 A/B 테스트와 유사합니다. 푸시 알림 예시로 돌아가 보겠습니다. 테스트할 수 있는 또 다른 변수는 메시지 끝에 이모티콘을 포함할지 여부입니다. 이제 두 개의 변수(또는 변량, 배리언트와 혼동하지 말 것)를 테스트하게 되므로 "다변량"이라는 용어를 사용하게 됩니다. 이렇게 하려면 복사본에 대한 두 가지 옵션과 이모티콘에 대한 두 가지 옵션(있음 또는 없음)을 곱한 총 네 가지 버전의 메시지를 테스트해야 하며, 이는 총 네 가지 메시지 배리언트가 됩니다.

Braze 설명서에서 "다변량 테스트"는 설정 과정이 동일하므로 "A/B 테스트"와 혼용하여 사용합니다.

## 다변량 및 A/B 테스트의 이점 {#the-benefits-of}

다변량 및 A/B 테스트를 통해 오디언스에 대해 쉽고 명확하게 파악할 수 있습니다. 더 이상 사용자가 어떤 반응을 보일지 추측할 필요가 없습니다. 모든 캠페인은 다양한 메시지 변형을 시도하고 잠재고객의 반응을 측정할 수 있는 기회가 됩니다.

다변량 및 A/B 테스트가 유용할 수 있는 구체적인 시나리오는 다음과 같습니다:

- **메시징 유형을 처음 시도하는 경우:** 인앱 메시징을 처음 사용할 때 제대로 사용할 수 있을지 걱정되시나요? 다변량 테스트를 통해 무엇이 사용자의 공감을 불러일으키는지 실험하고 배울 수 있습니다.
- **온보딩 캠페인 및 지속적으로 발송되는 기타 캠페인을 만들 때:** 대부분의 사용자가 이 캠페인을 접하게 될 것이므로 최대한 효과적인 캠페인이 되도록 하는 것은 어떨까요?
- **보낼 메시지에 대한 아이디어가 여러 개 있는 경우:** 어떤 것을 선택해야 할지 잘 모르겠다면 테스트를 실행한 다음 데이터 중심 결정을 내리세요.
- **사용자가 "검증된" 마케팅 기법에 반응하는지 여부를 조사할 때:** 마케터는 사용자 참여를 유도하기 위해 기존의 전략을 고수하는 경우가 많지만, 모든 제품의 사용자 기반은 다릅니다. 때로는 클릭 유도 문안을 반복하고 소셜 증거를 사용해도 원하는 결과를 얻지 못할 수도 있습니다. 다변량 및 A/B 테스트를 통해 틀에서 벗어나 특정 오디언스에게 효과적인 색다른 전략을 발견할 수 있습니다.

### 배리언트 배포

배리언트 상품 간의 분포가 항상 균일한 것은 아닙니다. 배리언트 상품 배포 방식은 다음과 같습니다.

다변량 캠페인에서 메시지를 보낼 때마다 시스템은 사용자가 설정한 비율에 따라 무작위 옵션을 독립적으로 선택하고 그 결과에 따라 변형을 할당합니다. 동전 던지기와 같이 예외적인 상황이 발생할 수 있습니다. 동전을 100번 던져본 적이 있다면, 선택지가 두 개뿐인데도 매번 앞면과 뒷면이 정확히 50대 50으로 나뉘지 않는다는 것을 알고 있을 것입니다. 52개의 머리와 48개의 꼬리를 얻을 수 있습니다.

균등하게 분할하려는 이형 상품이 여러 개 있는 경우 이형 상품의 수가 100의 배수인지도 확인해야 합니다. 그렇지 않으면 일부 이형 상품은 다른 이형 상품에 비해 해당 이형 상품에 배포되는 사용자 비율이 더 높아집니다. 예를 들어 캠페인에 7개의 배리언트 상품이 있는 경우 7이 정수로 100으로 균등하게 나뉘지 않으므로 배리언트 상품 분포가 짝수일 수 없습니다. 이 경우 15%의 배리언트 상품 2개와 14%의 배리언트 상품 5개를 보유하게 됩니다.

#### 인앱 메시지 관련 참고 사항

인앱 메시지에 대해 A/B 테스트를 실행할 때, 분석 결과 한 이형 상품과 다른 이형 상품 간의 비율이 균등하더라도 이형 상품 분포가 더 높은 것처럼 보일 수 있습니다. 예를 들어, 배리언트 A와 배리언트 C에 대한 다음 *고유 수신자* 그래프를 생각해 보겠습니다.

![배리언트 A와 배리언트 C의 모양이 비슷한 두 가지 배리언트에 대한 고유 수신자 그래프(여기서 배리언트 A의 일일 고유 수신자 수가 더 높음)]({% image_buster /assets/img/variant_distribution_iam.png %})

이는 배리언트 분포 때문이 아니라 인앱 메시지의 *고유 수신자* 수가 계산되는 방식 때문이며, 배리언트 A가 배리언트 C보다 *고유 수신자* 수가 지속적으로 더 많습니다. 인앱 메시지의 경우, *고유 수신자*는 실제로 인앱 메시지를 수신하고 본 총 사용자 수인 *고유 노출* 횟수입니다. 즉, 사용자가 어떤 이유로든 메시지를 받지 못하거나 보지 않기로 결정한 경우 *고유 수신자* 수에 포함되지 않으며 변형 분포가 왜곡되어 나타날 수 있습니다.

## Tips for multivariate and A/B testing

다변량 및 A/B 테스트를 통해 사용자에 대한 강력한 인사이트를 발견할 수 있습니다. To receive test results that are truly reflective of your users' behaviors, follow these guidelines.

#### 많은 수의 사용자를 대상으로 테스트 실행

샘플이 많으면 평균 사용자의 선호도를 반영하는 결과가 도출되고 이상값에 의해 흔들릴 가능성이 줄어듭니다. 또한 표본 크기가 클수록 승률 차이가 적은 우승 배리언트를 식별할 수 있습니다.

#### 사용자를 무작위로 다른 테스트 그룹으로 분류

다변량 테스트를 통해 무작위로 선택된 테스트 그룹을 최대 8개까지 만들 수 있습니다. 무작위 추출은 테스트 세트의 편향을 제거하고 테스트 그룹의 구성이 유사할 확률을 높이기 위해 고안되었습니다. 이렇게 하면 응답률의 차이가 샘플의 차이가 아니라 메시지의 차이로 인한 것임을 확인할 수 있습니다.

#### 테스트하려는 요소 파악

다변량 및 A/B 테스트를 통해 여러 버전의 메시지 간의 차이를 테스트할 수 있습니다. 변경 사항을 분리하면 응답에 가장 큰 영향을 미친 요소를 식별할 수 있으므로 경우에 따라 간단한 테스트가 가장 효과적일 수 있습니다. 다른 경우에는 변형 간에 더 많은 차이를 표시하면 이상값을 조사하고 다양한 요소 집합을 비교할 수 있습니다. 처음부터 테스트하려는 대상을 명확히 한다면 두 방법 모두 반드시 틀린 것은 아닙니다.

#### 테스트 실행 시간을 결정하고 테스트를 일찍 종료하지 마세요.

테스트를 시작하기 전에 테스트를 실행할 기간을 정하고 그 기간을 지키세요. 마케터들은 종종 마음에 드는 결과가 나오면 테스트를 중단하여 결과를 편향적으로 해석하려는 유혹을 받습니다. 엿보고 싶은 유혹을 뿌리치고 시험을 일찍 끝내지 마세요!

#### Add your test to campaigns before they launch, not after

If you add your test to a campaign after it has launched, the test won't run properly and you may receive incorrect or misleading statistics. For example, if you add a test to a launched campaign that allows re-entry, users who re-enter the campaign will always go through the same path to prevent data inaccuracies with the test. Additionally, if you change any of the variants while the test is running, the change will invalidate your test and restart it.

For accurate test results:
1. Clone the launched campaign.
2. Stop the original campaign.
3. Then, add the test to the cloned campaign. 

#### 가능하면 대조 그룹을 포함하세요.

[대조 그룹을]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/#including-a-control-group) 포함하면 메시지를 전혀 보내지 않는 것보다 메시지를 보내는 것이 사용자 전환에 더 큰 영향을 미치는지 알 수 있습니다.


[2]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-events
[70]: #tips-different-channels
[80]: #choosing-a-segment
[160]: {% image_buster /assets/img/ab_create_1.png %}
[170]: {% image_buster /assets/img/ab_create_2.png %}
[175]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/
[180]: {% image_buster /assets/img/ab_create_4.png %}
[210]: {% image_buster /assets/img/ab_create_8.png %}
[10]: {% image_buster /assets/img/ab_send_winning_variant.png %}
[272]: #intelligent-selection
[273]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/message_format/
[인텔셀렉션]: {{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/
[confidence]: {{site.baseurl}}/user_guide/intelligence/multivariate_testing/#understanding-confidence
