---
nav_title: Sisu Data
article_title: Sisu Data
description: "이 참조 문서에서는 모든 캠페인 또는 캠페인 수준에서 측정기준이 변경되는 이유와 가장 최적의 결과를 이끄는 요인을 이해할 수 있도록 지원하는 클라우드 의사 결정 인텔리전스의 선두주자인 Sisu Data와 Braze 간의 파트너십을 간략히 설명합니다."
alias: /partners/sisudata
page_type: partner
search_tag: Partner
---

# Sisu Data

> [Sisu Data][2]는 머신 러닝을 사용하여 측정기준 성능을 자동으로 분해하고 빠르고 포괄적이며 유용한 인사이트를 제공하는 클라우드 의사 결정 인텔리전스의 선두주자입니다.

Sisu 데이터와 Braze 통합을 통해 모든 캠페인 또는 캠페인 수준에서 측정기준(예: 열람율, 클릭률, 전환율 등)이 왜 변하는지, 그리고 가장 최적의 결과를 이끄는 요인이 무엇인지 이해할 수 있습니다. 이러한 세그먼트가 식별되면 Braze 사용자는 데이터 웨어하우스에서 결과물을 구체화하거나 Sisu에서 Braze로 직접 전송하여 사용자를 리타겟팅하고 재참여시킬 수 있습니다.

## 전제 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Sisu 계정 | 이 파트너십을 활용하려면 [Sisu][3] 계정이 필요합니다. |
| 클라우드 창고 | 이 통합은 Braze 데이터가 클라우드 웨어하우스(예: Snowflake, BigQuery)에 저장되어 있다고 가정합니다. To streamline this integration process, we recommend utilizing Braze native functionality via [Currents][4]. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

### 1단계: 데이터셋을 준비하세요

데이터셋은 Sisu가 분석하기를 원하는 KPI를 나타내야 합니다. 예를 들어, 전환율이 주간 대비 하락한 이유를 더 잘 이해하고 싶다면, 도달 레코드에서 주간 전환을 나타내야 합니다. 데이터 세트의 열은 전환율이 떨어질 수 있는 잠재적 이유여야 합니다.

### 2단계: 메트릭 만들기  

데이터 세트가 준비되면 집계된 열을 참조하는 측정기준을 생성해야 합니다. 데이터 세트는 여러 측정기준을 지원할 수 있으므로 사용자는 기본적으로 모든 분석에 포함해야 할 차원과 포함하지 않아야 할 차원의 세트를 큐레이트할 수도 있습니다. 사용자는 항상 분석 수준에서 큐레이션을 계속할 수 있습니다.

![][6]

### 3단계: 분석을 생성  

사용자가 사용 사례에 따라 Sisu에서 만들 수 있는 다양한 분석이 있습니다. 가장 일반적인 분석 중 하나는 어떤 세그먼트가 가장 많이 변경되었는지 이해하기 위한 기간별 분석입니다. 사용자는 상대적인 기간을 선택하여 일별, 주별, 월별 또는 커스텀 기간을 분석할지 여부를 결정할 수 있습니다.

예를 들어, 사용자는 특정 광고 그룹 및 인게이지먼트 채널에 대한 월별 전환율 분석을 생성하고 주요 긍정적 요인과 부정적 요인을 이해할 수 있습니다.

{% tabs %}
{% tab 주요 긍정적 요인 %}

![]({% image_buster /assets/img/sisudata/kda_result_positive.png %})

{% endtab %}
{% tab 상위 부정적 요인 %}

![]({% image_buster /assets/img/sisudata/kda_result_negative.png %})

{% endtab %}
{% endtabs %}

여기에서 참여하거나 캠페인을 수정하려는 코호트에 집중할 수 있습니다. 예를 들어, Sisu는 화요일에 발송된 푸시 알림과 대량으로 발송된 이메일이 전환율에 심각한 영향을 미친다는 점을 자동으로 식별했습니다.

![][9]

### 4단계: 결과를 데이터 웨어하우스에 다시 작성하십시오

사용자는 [Sisu의 API][10]를 사용하여 Sisu에서 결과를 추출하고 데이터 웨어하우스에 세그먼트를 실현할 수 있습니다. Snowflake 고객은 [Cloud Data Ingestion][5]을 통해 Braze에서 이러한 세그먼트를 활성화할 수 있습니다.

다른 데이터 웨어하우스의 경우 사용자는 기존 활성화 솔루션을 활용하거나 추가 지원을 위해 Sisu에 문의할 수 있습니다.

## 고객지원

이 통합에 대한 질문이 있으면 partners@sisudata.com에서 Sisu에 문의하십시오.

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://sisudata.com/
[3]: https://sisudata.com/
[4]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/setting_up_currents/
[5]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/cloud_ingestion/overview/
[6]: {% image_buster /assets/img/sisudata/metric_creation.png %}
[9]: {% image_buster /assets/img/sisudata/segment.png %}
[10]:https://docs.sisudata.com/docs/api/#tag/AnalysesService/operation/AnalysesService_AnalysisRunResults
