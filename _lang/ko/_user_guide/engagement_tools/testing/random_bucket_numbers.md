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

> 이 문서에서는 무작위 버킷 번호의 개념과 이를 사용하여 이형 상품 및 대조군을 만드는 방법에 대해 설명합니다.

## 개요

Braze에서 사용자 프로필이 생성되면 해당 사용자에게는 0에서 9999 사이의 임의의 버킷 번호가 자동으로 할당됩니다(포함). 무작위 버킷 번호는 무작위 사용자 세그먼트를 균일하게 분산시키는 데 사용할 수 있는 사용자 속성입니다. 이러한 세그먼트를 활용하여 여러 캠페인 또는 캔버스의 효과를 시간 경과에 따라 사용자 그룹에 테스트할 수 있습니다.

캠페인이나 캔버스를 받지 않는 사용자 그룹인 글로벌 컨트롤 그룹에도 무작위 버킷 번호가 사용됩니다. Braze는 여러 범위의 무작위 버킷 번호를 무작위로 선택하고 선택한 버킷의 사용자를 포함합니다. 글로벌 제어 그룹을 설정한 상태에서 다른 용도로 임의의 버킷 번호를 사용하려는 경우 [주의해야 할 사항을]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#things-to-watch-for) 확인하세요.

### 무작위 버킷 번호를 사용해야 하는 경우

여러 캠페인 또는 캔버스의 효과를 장기간에 걸쳐 테스트하려는 경우 임의의 버킷 번호를 사용하여 사용자를 세분화할 수 있습니다.

### 다른 것을 사용해야 하는 경우

단일 캠페인 또는 단일 캔버스 내에서 테스트할 사용자를 세분화하려면 캠페인에 [A/B 테스트를]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/) 사용하는 것이 좋습니다. 캔버스의 경우, 여정 수준 테스트를 위해 다양한 [변형을]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#adding-a-variant) 만들거나 단계 수준 테스트를 위해 [실험 경로를]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) 사용할 수 있습니다.

## 임의의 버킷 번호를 사용하여 세그먼트 생성

[세그먼트를 만들]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) 때 `Random Bucket #` 필터를 추가합니다. 필터 레이블이 **통계 샘플링 ID로** 변경됩니다. 그런 다음 세그먼트에 포함할 숫자 또는 숫자 범위를 지정할 수 있습니다.

![][1]

![][2]

세 가지 변종에 대한 테스트를 실행하고 대조 그룹도 포함하려는 경우 이러한 유형의 세그먼트를 사용할 수 있습니다. 세 가지 이형 상품과 대조 그룹에 대해 동일한 크기의 세그먼트를 만드는 다음 샘플 계획을 고려하세요:

- 버킷 번호 0~2499는 제어 세그먼트에 해당합니다.
- 버킷 번호 2500~4999는 이형 1을 수신할 세그먼트에 해당합니다.
- 버킷 번호 5000~7499는 이형 2를 수신할 세그먼트에 해당합니다.
- 버킷 번호 7500~9999는 이형 3을 수신할 세그먼트에 해당합니다.

원하는 세그먼트 수와 각 세그먼트 내 사용자 분포에 따라 요금제가 다르게 보일 수 있습니다.

대조 그룹을 포함한 임의의 버킷 번호 세그먼트 각각에 대해 [애널리틱스 추적을]({{site.baseurl}}/user_guide/data_and_analytics/tracking/segment_analytics_tracking) 켭니다. 대조 그룹을 기준으로 이형 상품의 성공 여부를 평가할 때 [사용자 지정 이벤트]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_custom_event_data) 페이지로 이동하여 각 세그먼트가 특정 사용자 지정 이벤트를 완료한 빈도를 확인할 수 있습니다.


[1]: {% image_buster /assets/img_archive/random_buckets_filter.png %}
[2]: {% image_buster /assets/img_archive/random_buckets_filterexample.png %}
