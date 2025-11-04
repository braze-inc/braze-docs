---
nav_title: 보고
article_title: LINE 보고
page_order: 4
description: "이 참고 문서에서는 Braze에서 사용하는 LINE 지표와 LINE 캠페인에서 이를 확인하는 방법에 대해 설명합니다."
page_type: reference
channel:
 - LINE
alias: /line/reporting/
---

# LINE 보고

> 캠페인 또는 캔버스를 시작한 후 캠페인 세부 정보 페이지 또는 캔버스 분석에서 주요 측정기준을 확인할 수 있습니다. 이 문서에서는 이러한 메트릭을 찾을 수 있는 위치와 해당 메트릭이 나타내는 내용에 대해 설명합니다.

{% alert tip %}
보고서의 용어 및 지표에 대한 정의를 찾고 계신가요? Refer to [Report metrics glossary]({{site.baseurl}}/user_guide/data/report_metrics/).
{% endalert %}

## 캠페인 분석

**캠페인 분석** 탭에서는 일련의 패널에서 보고서를 볼 수 있습니다. 아래 섹션에 나열된 항목보다 많거나 적은 항목이 표시될 수 있지만 각 항목에는 고유한 목적이 있습니다.

{% alert note %}
LINE의 오픈 및 클릭 관련 통계는 특정 날짜에 20명 이상의 사용자가 이벤트를 수행한 경우에만 계산됩니다.
{% endalert %}

### 캠페인 세부 정보

**캠페인 세부정보** 패널에는 LINE 메시지 실적에 대한 간략한 개요가 표시됩니다.

이 패널을 검토하여 수신자 수에 전송된 메시지 수, 주요 전환율 및 이 메시지로 인해 발생한 총 매출 등의 전반적인 측정기준을 확인할 수 있습니다. 이 페이지에서 전달, 오디언스 및 전환 설정을 검토할 수도 있습니다.

#### 대조군

To measure the impact of an individual LINE message, you can add a [control group]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) to an A/B test. 최상위 **캠페인 세부 정보** 패널에는 컨트롤 그룹 변형의 지표가 포함되지 않습니다.

### LINE 성과

**LINE 성과** 패널에는 다양한 측면에서 메시지의 성과가 얼마나 잘 나타났는지 요약되어 있습니다. 이 패널의 측정기준은 선택한 메시징 채널과 다변량 테스트를 실행하는지 여부에 따라 달라집니다. <i class="fa fa-eye preview-icon"></i> **미리보기** 아이콘을 클릭하여 각 이형 상품 또는 채널에 대한 메시지를 확인할 수 있습니다.

![The "LINE Performance" panel show metrics for two variants.]({% image_buster /assets/img/line/line_performance.png %})

보기를 단순화하려면 **\+ 열 추가/제거**를 선택하고 원하는 대로 측정기준을 지우세요. 기본적으로 모든 메트릭이 표시됩니다.

#### LINE 지표

다음은 분석에서 확인할 수 있는 몇 가지 주요 LINE 지표입니다. To see the definitions of all LINE metrics used in Braze, refer to [Report metrics glossary]({{site.baseurl}}/user_guide/data/report_metrics/).

| 기간 | 정의 |
| --- | --- |
| 발송 수 | Braze와 LINE 간에 성공적으로 통신한 총 전송 횟수입니다. 이는 사용자가 메시지를 수신했다는 것을 의미하지는 않습니다. |
| 고유 열람 | 하루 최소 기준인 20개 메시지에 도달한 후 사용자가 열어본 LINE 메시지의 총 개수입니다. |
| 총 열람 수 | 하루 최소 기준인 20개 메시지에 도달한 후 사용자가 보낸 LINE 메시지를 열어본 총 횟수입니다. |
| 고유 클릭 수 | 하루 최소 기준인 20개 메시지에 도달한 후 사용자가 클릭한 총 LINE 메시지 수입니다. |
| 총 클릭 수 | 하루 최소 기준인 20개 메시지에 도달한 후 사용자가 보낸 LINE 메시지를 클릭한 총 횟수입니다. |
{: .reset-td-br-1 .reset-td-br-2 }

### 과거 성과

**과거 실적** 패널에서는 **메시지 실적** 패널의 메트릭을 시간 경과에 따른 그래프로 볼 수 있습니다. 패널 상단의 필터를 사용하여 그래프에 표시된 통계와 채널을 수정할 수 있습니다. 이 그래프의 시간 범위는 항상 페이지 상단에 지정된 시간 범위를 반영합니다.

일별 분석을 보려면 <i class="fas fa-bars"></i> 햄버거 메뉴를 선택하고 **CSV 다운로드를** 선택하면 보고서의 CSV 내보내기를 받을 수 있습니다.

### 전환 이벤트 세부 정보
 
**전환 이벤트 세부 정보** 패널에는 캠페인에 대한 전환 이벤트의 성과가 표시됩니다. 자세한 내용은 [전환 이벤트를]({{site.baseurl}}/user_guide/engagement_tools/testing/conversion_correlation) 참조하세요.

### 전환 상관관계

**전환 상관관계** 패널은 어떤 사용자 속성과 행동이 캠페인에 대해 설정한 결과에 도움이 되거나 해가 되는지에 대한 인사이트를 제공합니다. 자세한 내용은 [전환 상관관계]({{site.baseurl}}/user_guide/engagement_tools/testing/conversion_correlation)를 참조하세요.


