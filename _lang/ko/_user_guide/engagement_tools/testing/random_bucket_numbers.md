---
nav_title: 무작위 버킷 번호
article_title: 무작위 버킷 번호
page_order: 2
page_type: reference
description: "이 문서에서는 무작위 버킷 번호의 개념과 이를 사용하여 이형 상품 및 대조군을 만드는 방법에 대해 설명합니다."
page_type: reference
tool:
  - Campaign
  - Canvas

---

# 무작위 버킷 번호

> 무작위 버킷 번호는 무작위 사용자 세그먼트를 균일하게 분산시키는 데 사용할 수 있는 사용자 속성입니다. 

## Overview

Braze에서 고객 프로필이 생성되면 해당 사용자에게는 0에서 9999 사이의 무작위 버킷 번호가 자동으로 할당됩니다(포함). 이 세그먼트를 사용하여 여러 캠페인 또는 캔버스의 효과를 시간에 따라 사용자 그룹에서 테스트할 수 있습니다.

### 글로벌 컨트롤 그룹 사용

무작위 버킷 번호는 캠페인이나 캔버스를 받지 않는 사용자 그룹인 글로벌 컨트롤 그룹에서 사용됩니다. Braze는 여러 범위의 무작위 버킷 번호를 무작위로 선택하고 선택한 버킷의 사용자를 포함합니다. 무작위 버킷 번호는 가중치나 최근 할당된 번호에 대한 고려 없이 할당됩니다. 

{% alert note %}
사용자가 삭제되고 다시 생성되면, 사용자는 새로운 사용자로 간주되기 때문에 다른 무작위 버킷 번호가 할당됩니다.
{% endalert %}

글로벌 컨트롤 그룹이 설정되어 있고 다른 사용 사례에 대해 무작위 버킷 번호를 사용하려면 [주의할 사항]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#things-to-watch-for)을 확인하세요.

### 무작위 버킷 번호를 사용해야 하는 경우

여러 캠페인이나 캔버스의 효과에 대한 장기 테스트를 수행하려면 무작위 버킷 번호를 사용하여 사용자를 세분화할 수 있습니다.

### 다른 것을 사용해야 하는 경우

단일 캠페인이나 단일 캔버스 내에서 테스트를 위해 사용자를 세분화하려면 캠페인에 대해 [A/B 테스트]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/)를 사용하세요. 캔버스의 경우, 여정 수준 테스트를 위해 다양한 [배리언트]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#adding-a-variant)를 만들거나 단계 수준 테스트를 위해 [실험 경로]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/)를 사용할 수 있습니다.

## 임의의 버킷 번호를 사용하여 세그먼트 생성

[세그먼트 생성]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) 시 "무작위 버킷 #" 필터를 추가하세요. 그런 다음, 세그먼트에 포함할 숫자 또는 숫자 범위를 지정하세요.

무작위 버킷 번호에 대한 세그먼트 필터는 "3000" 이하입니다.

세 가지 배리언트에 대한 테스트를 실행하고 대조군도 포함하려는 경우 이러한 유형의 세그먼트를 사용할 수 있습니다. 세 가지 이형 상품과 대조 그룹에 대해 동일한 크기의 세그먼트를 만드는 다음 샘플 계획을 고려하세요:

- 버킷 번호 0~2499는 제어 세그먼트에 해당합니다.
- 버킷 번호 2500~4999는 이형 1을 수신할 세그먼트에 해당합니다.
- 버킷 번호 5000~7499는 배리언트 2를 수신할 세그먼트에 해당합니다.
- 버킷 번호 7500~9999는 이형 3을 수신할 세그먼트에 해당합니다.

원하는 세그먼트 수와 각 세그먼트 내 사용자 분포에 따라 요금제가 다르게 보일 수 있습니다.

각 무작위 버킷 번호 세그먼트, 대조군 포함, 에 대해 [분석 추적]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/)을 켜세요. 대조군에 대한 변형의 성공을 평가할 때, [커스텀 이벤트]({{site.baseurl}}/user_guide/data/export_braze_data/export_custom_event_data/) 페이지로 가서 각 세그먼트가 특정 커스텀 이벤트를 완료한 빈도를 확인할 수 있습니다.

{% alert tip %}
캔버스에서 무작위 버킷 번호 세그먼트를 사용할 때, 예를 들어 [결정 분할]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split/) 단계의 필터로 사용할 때, 캔버스의 [종료 기준]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria/), 오디언스 필터 및 상류 단계가 버킷 범위 중 하나와 겹치는 세그먼트를 타겟팅하지 않도록 하세요. 그렇지 않으면, 해당 범위의 사용자가 분할에 도달하기 전에 불균형적으로 제거되어 경로 간의 분포가 고르지 않을 수 있습니다.
{% endalert %}

### 무작위 버킷 번호를 사용한 무작위 오디언스 재진입

무작위 오디언스 재진입은 [A/B 테스트]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#what-are-multivariate-and-ab-testing) 또는 캠페인에서 특정 사용자 그룹을 타겟팅하는 데 유용할 수 있습니다. 무작위 버킷 번호로 무작위 오디언스 재진입을 수행하려면 다음을 수행하세요:

1. [세그먼트 생성]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment)하세요.
2. 무작위 버킷을 정의하세요. 캠페인이나 캔버스에서 무작위 버킷 필터를 사용하여 오디언스를 서로 다른 그룹으로 나누세요. 예를 들어, 오디언스를 두 개의 무작위 버킷으로 나누도록 정확히 지정할 수 있습니다(버킷당 50%의 사용자).
3. 캠페인이나 캔버스의 **타겟 오디언스** 섹션에서 무작위 버킷 설정을 지정하세요. 이렇게 하면 Braze가 정의된 비율에 따라 사용자를 적절한 버킷에 자동으로 할당할 수 있습니다.
4. 사용자가 세그먼트에 다시 들어갈 수 있도록 하는 로직을 설정하세요. 예를 들어, 사용자가 앱과 15일 동안 참여하지 않은 경우 세그먼트에 다시 들어갈 수 있도록 허용할 수 있습니다.
5. 캠페인을 시작하고 각 버킷의 성능을 모니터링하세요. 참여율 및 전환율과 같은 측정기준을 분석하여 무작위 오디언스 재진입이 사용 사례에 얼마나 효과적인지 판단할 수 있습니다.


