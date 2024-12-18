---
nav_title: 오디언스 경로 
article_title: 오디언스 경로 
alias: /audience_paths/
page_order: 1
page_type: reference
description: "이 참조 문서에서는 캔버스에서 오디언스 경로를 사용하여 전략적 우선순위 기반 사용자 그룹화를 통해 대규모로 사용자를 직관적으로 필터링하고 세그먼트화하는 방법을 설명합니다."
tool: Canvas

---

# 오디언스 경로 

> 캔버스 오디언스 경로를 사용하면 전략적 우선순위 기반 사용자 그룹화를 통해 대규모로 사용자를 직관적으로 필터링하고 세그먼트할 수 있습니다. 

이 캔버스 구성 요소는 과도한 오디언스 기반 전체 단계를 만들 필요를 대체하여, 여덟 개의 전체 구성 요소가 하나로 결합될 수 있게 합니다. 이것은 불필요한 혼란과 복잡성에서 캔버스를 정리하면서 사용자 타겟팅을 단순화하는 데 도움이 됩니다. 

![][0]{: style="float:right;max-width:13%;margin-left:15px;margin-top:15px;"}

오디언스 경로는 순위 기준이 있는 정렬 깔때기와 유사합니다. 사용자는 우선 순위 순서대로 각 기준에 대해 평가되며 자격을 갖춘 가장 높은 순위의 기준 경로로 보내집니다. 이것은 사용자가 어디로 갈지, 어떤 메시지를 받을지에 대한 모호성을 줄여줍니다. 순위는 출시 후 [편집할 수 없습니다]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/change_your_canvas_after_launch/).

오디언스 경로를 사용하면 다음을 수행할 수 있습니다.

- 오디언스 기준에 따라 사용자를 다른 캔버스 경로로 보냅니다.
- 다른 오디언스 그룹에 우선순위를 할당하여 메시지가 올바른 사용자에게 도달하도록 하세요. 
  - 이전에 사용자가 두 가지 잠재적인 전체 단계의 기준을 충족하면 무작위로 할당되었습니다. 
- 대규모로 사용자를 정확하게 타겟팅하세요.
  - 구성 요소당 최대 여덟 개의 오디언스 그룹(기본값 두 개 및 추가 그룹 여섯 개)을 만들 수 있지만, 여러 오디언스 경로 단계를 연결하여 사용자를 추가로 분류할 수 있습니다. 

## 오디언스 경로 만들기

![][1]{: style="float:right;max-width:20%;margin-left:15px;"}

오디언스 경로 단계를 추가하려면 다음을 수행하세요. 

1. 캔버스에 단계를 추가하세요. 
2. 사이드바에서 구성 요소를 드래그 앤 드롭하거나 단계 하단에서 <i class="fas fa-plus-circle"></i> **추가**를 클릭하고 **오디언스 경로**를 선택합니다.

기본 오디언스 경로 구성 요소에는 두 개의 기본 오디언스 그룹, **Group 1** 및 **Everybody Else**가 포함되어 있습니다. **Everybody Else** 그룹에는 정의된 오디언스 그룹에 속하지 않는 모든 사용자가 포함됩니다. 이 그룹은 항상 마지막에 순위가 매겨집니다.

### 오디언스 그룹 정의

다음 스크린샷은 확장된 오디언스 경로 단계의 레이아웃을 보여줍니다. 여기에서 최대 8개의 오디언스 그룹(하나는 사전 설정된 그룹이고 나머지 일곱 개는 사용자 정의 가능)을 정의할 수 있습니다. 오디언스 그룹을 정의하려면 오디언스 경로 편집기에서 그룹 이름을 선택하십시오. 오디언스 그룹의 이름을 변경하고, 그룹에 적용되는 필터와 세그먼트를 선택하며, 그룹을 추가하거나 삭제할 수 있습니다.

예를 들어, 사용자의 그룹에게 유용한 음식 추천을 보내고 싶다면, 이미 구축한 "아시아 요리를 좋아함", "라틴 요리를 좋아함", "유럽 요리를 좋아함"과 같은 커스텀 속성 필터를 선택할 수 있습니다. 

![][3]{: style="max-width:90%;margin-left:15px;"}

오디언스 경로 단계가 완료되면 각 오디언스 그룹은 별도의 분기를 갖게 됩니다. 오디언스 경로를 계속 사용하여 오디언스를 추가로 필터링하거나 표준 캔버스 단계를 사용하여 캔버스 여정을 계속할 수 있습니다. 

![][4]{: style="max-width:90%;margin-left:15px;"}

### 테스팅 오디언스 그룹

![]({% image_buster /assets/img_archive/user_lookup.png %}){: style="float:right;max-width:40%;margin-left:15px;margin-bottom:15px;"}

세그먼트와 필터를 오디언스에 추가한 후, [사용자를 조회하여]({{site.baseurl}}/user_guide/engagement_tools/segments/user_lookup/) 오디언스 그룹이 예상대로 설정되었는지 확인할 수 있습니다. 

## 오디언스 경로 사용

오디언스 경로의 진정한 힘은 우선순위를 할당하는 능력에 있습니다. 이 기능은 전략적으로 사용할 필요는 없지만, 일부 마케터들은 특별 상품이나 한정판 출시와 같은 특정 제품을 사용자에게 홍보하는 데 사용할 수 있습니다. 

이 그룹에 높은 우선순위를 할당함으로써 특정 필터 및 세그먼트에 속하는 사용자를 타겟팅하면서도 특정 기준에 맞지 않는 사용자를 여전히 타겟팅할 수 있습니다. 모두 단일 캔버스 단계에서 가능합니다.

![][2]{: style="float:right;max-width:40%;margin-left:15px;margin-bottom:15px;"}

예를 들어, 새로운 제품 광고를 사용자 그룹에게 보내고 싶다고 가정해 봅시다. 오디언스 경로에서 해당 제품에 속하는 필터를 높은 순위로 시작할 것입니다. 회사를 위한 마케팅 캠페인을 만들고 있었다면 "Big Brand"와 새 신발 브랜드가 막 출시되었을 때 "Big Brand Shoes를 좋아함" 또는 "Big Brand를 좋아함"과 같은 필터를 선택하고 필터링된 그룹에 따라 다른 이메일 메시지를 보낼 수 있습니다. 

사용자가 이 오디언스 경로 구성 요소에 들어가면 가장 높은 순위의 오디언스 그룹에 속하는지 먼저 평가됩니다: 오디언스 그룹 A "빅 브랜드 신발을 좋아합니다". 그렇다면, 그들은 당신의 캔버스에 정의된 다음 구성 요소로 계속 진행할 것입니다. 만약 "빅 브랜드 신발을 좋아하지 않으면", 다음 오디언스 그룹, 오디언스 그룹 B "빅 브랜드를 좋아함"으로 평가될 것이며, 기준이 충족되면 다음 캔버스 구성 요소로 계속 진행됩니다. 마지막으로, 사용자는 이전 그룹에 속하지 않으면 **기타 모든 사람** 그룹에 속하게 되며 해당 경로에 대해 정의한 다음 캔버스 구성 요소로 계속 진행합니다.

이 단계의 성능도 [캔버스 분석]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/#performance-visualization)을 사용하여 볼 수 있습니다.

### 랜덤 버킷 번호로 오디언스 경로 세분화

캔버스가 [사용량 제한]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/)(예: 캔버스를 받을 총 사용자 수 제한)을 사용하는 경우, Braze는 오디언스 경로를 세그먼트하기 위해 무작위 버킷 번호를 사용하지 않기를 권장합니다. 

[무작위 버킷 번호]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/ab_testing_with_random_buckets/)는 무작위 사용자로 균일하게 분포된 세그먼트를 생성하는 데 사용할 수 있는 사용자 속성입니다. Braze는 세분화 단계에서 무작위 버킷 번호를 사용하여 사용자를 그룹화하고 각 그룹을 별도로 처리합니다. 어떤 그룹이 먼저 처리하느냐에 따라 일부 사용자는 사용량 제한으로 인해 입장이 제한될 수 있으며, 이는 사용자가 오디언스 경로 단계에 도달할 때 고르지 않은 분포를 초래할 수 있습니다.

이 시나리오에서는 대신 [실험 경로]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/)를 사용해 보십시오.

[0]: {% image_buster /assets/img/audience_path/audience_path.png %}
[1]: {% image_buster /assets/img/audience_path/audience_path1.png %}
[2]: {% image_buster /assets/img/audience_path/audience_path2.png %}
[3]: {% image_buster /assets/img/audience_path/audience_path3.png %}
[4]: {% image_buster /assets/img/audience_path/audience_path4.png %}
