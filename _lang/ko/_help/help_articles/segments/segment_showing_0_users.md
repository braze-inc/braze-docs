---
nav_title: 세그먼트에서 사용자 누락
article_title: 세그먼트에서 사용자 누락
page_order: 1

page_type: solution
description: "이 도움말 문서는 세그먼트에 사용자가 표시되지 않지만 더 많은 사용자가 예상되는 경우 문제 해결 단계를 안내합니다."
tool: Segments
---

# 세그먼트에 사용자 누락

`0` 사용자를 보고 있지만 더 많은 사용자를 예상했을 때 가능한 두 가지 솔루션이 있습니다.
* [상세 통계 계산](#calculate-exact-statistics)
* [데이터 전송 확인](#verify-data-transfer)

## 정확한 통계를 계산하하세요

세그먼트 통계는 추정치를 제공할 수 있습니다. 추정치는 95%의 신뢰구간을 가지는 무작위 샘플을 기반으로 계산되며, 그 결과는 `+/- 1%` 이내입니다. 사용자 기반이 작을수록 세그먼트의 규모가 대략적인 추정치에 그칠 가능성이 높아집니다. **세그먼트 세부정보** 패널에서 **정확한 통계 계산**을 클릭하세요. 이것은 귀하의 세그먼트에 있는 정확한 사용자 수를 계산할 것입니다.

![정확한 통계 계산 옵션을 표시하는 세그먼트 세부 정보 패널]({% image_buster /assets/img_archive/trouble8.png %})

## 데이터 전송 확인

데이터를 필터링할 때 Braze로 전송되지 않을 수 있습니다. 어떤 커스텀 이벤트가 Braze로 전송되고 있는지 확인하려면 [커스텀 이벤트 보고서]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-analytics)를 참조하세요.

커스텀 이벤트와 특정 날짜 및 앱을 선택하여 실제로 Braze로 전송되는 데이터가 무엇인지 확인합니다. 만약 `0` 데이터가 Braze로 전송되고 있음을 알게 된다면, 다음 단계는 이벤트를 Braze로 전송하는 방법을 평가하는 것입니다.

![사용자 지정 이벤트 수를 0으로 표시하는 그래프]({% image_buster /assets/img_archive/trouble9.png %})

{% alert important %}
Braze 대시보드에서 보는 데이터는 Braze로 보내는 것과 동일한 구문이 아닐 수 있습니다. Ensure that these two match exactly.
{% endalert %}

아직도 도움이 필요하신가요? [지원 티켓]({{site.baseurl}}/braze_support/)을 여세요.

_마지막 업데이트 날짜: 2021년 1월 5일_

