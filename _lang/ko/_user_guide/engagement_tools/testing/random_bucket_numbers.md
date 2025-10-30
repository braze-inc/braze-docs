---
nav_title: 무작위 버킷 번호
article_title: 무작위 버킷 번호
page_order: 2
page_type: reference
description: "이 문서에서는 무작위 버킷 번호의 개념과 이를 사용하여 배리언트 및 대조군을 만드는 방법에 대해 설명합니다."
page_type: reference
tool:
  - Campaign
  - Canvas

---

# 무작위 버킷 번호

> 무작위 버킷 번호는 균일하게 분포된 임의의 사용자 세그먼트를 생성하는 데 사용할 수 있는 사용자 속성입니다. 

## 개요

Braze에서 고객 프로필이 생성되면 해당 사용자에게는 0에서 9999 사이의 무작위 버킷 번호가 자동으로 할당됩니다(포함). 이러한 세그먼트를 사용하여 여러 캠페인 또는 캔버스가 시간 경과에 따른 사용자 그룹에 미치는 효과를 테스트할 수 있습니다.

### 글로벌 컨트롤 그룹 사용법

글로벌 컨트롤 그룹(캠페인이나 캔버스를 받지 않는 사용자 그룹)에는 무작위 버킷 번호가 사용됩니다. Braze는 여러 범위의 무작위 버킷 번호를 무작위로 선택하고 선택한 버킷의 사용자를 포함합니다. 무작위 버킷 번호는 가중치를 부여하거나 최근에 할당된 번호를 고려하지 않고 할당됩니다. 

{% alert note %}
사용자가 삭제되었다가 다시 생성되면 새 사용자로 간주되므로 해당 사용자에게는 다른 무작위 버킷 번호가 할당됩니다.
{% endalert %}

글로벌 컨트롤 그룹을 설정한 상태에서 다른 사용 사례에 무작위 버킷 번호를 사용하려는 경우 [주의해야 할 사항을]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#things-to-watch-for) 확인하세요.

### 무작위 버킷 번호를 사용해야 하는 경우

여러 캠페인 또는 캔버스의 효과를 장기간에 걸쳐 테스트하려는 경우 무작위 버킷 번호를 사용하여 사용자를 세분화할 수 있습니다.

### 다른 것을 사용해야 하는 경우

단일 캠페인 또는 단일 캔버스 내에서 테스트 사용자를 세분화하려면 캠페인에 [A/B 테스트를]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/) 사용하세요. 캔버스의 경우 여정 수준 테스트를 위해 다양한 [배리언트를]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#adding-a-variant) 만들거나 단계 수준 테스트를 위해 [실험 경로를]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) 사용할 수 있습니다.

## 무작위 버킷 번호를 사용하여 세그먼트 만들기

[세그먼트를 만들]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) 때 '임의 버킷 #' 필터를 추가합니다. 그런 다음 세그먼트에 포함할 숫자 또는 숫자 범위를 지정합니다.

"3000" 이하의 무작위 버킷 번호에 대한 세그먼트 필터입니다.]({% image_buster /assets/img_archive/random_buckets_filterexample.png %})

세 가지 배리언트에 대한 테스트를 실행하고 대조군도 포함하려는 경우 이러한 유형의 세그먼트를 사용할 수 있습니다. 세 가지 배리언트와 대조군에 대해 동일한 크기의 세그먼트를 만드는 다음 샘플 계획을 고려하세요:

- 버킷 번호 0~2499는 제어 세그먼트에 해당합니다.
- 버킷 번호 2500에서 4999는 배리언트 1을 받을 세그먼트에 해당합니다.
- 버킷 번호 5000~7499는 배리언트 2를 수신할 세그먼트에 해당합니다.
- 버킷 번호 7500~9999는 배리언트 3을 수신할 세그먼트에 해당합니다.

원하는 세그먼트 수와 각 세그먼트 내 사용자 분포에 따라 요금제가 다르게 보일 수 있습니다.

대조군을 포함한 각 무작위 버킷 번호 세그먼트에 대해 [분석 추적을]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/) 켜세요. 대조군과 비교하여 배리언트의 성공 여부를 평가할 때 [커스텀 이벤트]({{site.baseurl}}/user_guide/data/export_braze_data/export_custom_event_data/) 페이지로 이동하여 각 세그먼트가 특정 커스텀 이벤트를 완료한 빈도를 확인할 수 있습니다.

### 무작위 버킷 번호를 사용한 무작위 오디언스 재입장

무작위 오디언스 재입력은 [A/B 테스트]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#what-are-multivariate-and-ab-testing) 또는 캠페인에서 특정 사용자 그룹을 타겟팅하는 데 유용할 수 있습니다. 무작위 버킷 번호로 오디언스 재입력을 수행하려면 다음과 같이 하세요:

1. [세그먼트를 만듭니다]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment).
2. 무작위 버킷을 정의합니다. 캠페인 또는 캔버스에서 무작위 버킷 필터를 사용하여 오디언스를 여러 그룹으로 나눌 수 있습니다. 예를 들어 오디언스를 정확히 두 개의 무작위 버킷으로 분할하도록 지정할 수 있습니다(버킷당 사용자 50%).
3. 캠페인 또는 캔버스의 **타겟 오디언스** 섹션에서 무작위 버킷 설정을 지정합니다. 이를 통해 Braze는 정의된 비율에 따라 사용자를 적절한 버킷에 자동으로 할당할 수 있습니다.
4. 사용자가 세그먼트에 다시 들어갈 수 있는 로직을 설정하세요. 예를 들어, 사용자가 15일 동안 앱에 참여하지 않은 경우 해당 세그먼트에 재참여하도록 허용할 수 있습니다.
5. 캠페인을 시작하고 각 버킷의 성능/성과를 모니터링하세요. 참여율 및 전환율과 같은 측정기준을 분석하여 사용 사례에서 무작위 오디언스 재참여가 얼마나 효과적인지 확인할 수 있습니다.


