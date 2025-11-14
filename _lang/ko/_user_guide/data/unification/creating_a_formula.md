---
nav_title: 수식 만들기
article_title: 수식 만들기
page_order: 1.2
page_type: reference
description: "이 참조 문서에서는 데이터에 존재하는 복잡한 관계를 쉽게 이해할 수 있도록 도와주는 수식을 만들고 관리하는 방법에 대해 설명합니다."
tool: Reports

---
# 수식 만들기

> Braze에서 분석을 볼 때 여러 데이터 포인트를 결합하여 사용자 데이터에 대한 귀중한 인사이트를 얻을 수 있습니다. 이를 수식이라고 합니다. 공식을 사용하여 총 월간 활성 사용자 수(MAU) 및 일일 활성 사용자 수(DAU)를 기준으로 시계열 데이터를 정규화할 수 있습니다. 

수식은 데이터에 존재하는 복잡한 관계를 이해하는 데 도움이 됩니다. 예를 들어, 특정 세그먼트에 해당하는 일일 활성 사용자가 완료한 커스텀 이벤트 수를 일반 인구(또는 다른 세그먼트에 대해)와 비교할 수 있습니다.

## 사용 사례

특히 수식을 커스텀 이벤트와 결합하면 앱 내 사용자 행동을 이해하는 데 도움이 될 수 있습니다. 또한, Google Ads나 TV와 같은 유료 미디어를 Braze와 함께 사용하는 경우에도 포뮬러를 통해 세그먼트 구매 패턴에 대한 심층적인 인사이트를 얻을 수 있습니다. 

다음은 수식을 사용하여 감지할 수 있는 행동 패턴의 몇 가지 예입니다:

- **차량 공유 앱:** 사용자가 라이딩을 취소하는 시점에 대한 커스텀 이벤트가 있는 경우, 취소된 라이딩/DAU에 대한 기능을 구성하여 특정 사용자 세그먼트가 다른 사용자보다 라이딩을 더 많이 취소하는 경향이 있는지 확인할 수 있습니다.
- **전자상거래 앱:** 특정 제품 ID/MAU 구매에 대한 기능을 설정하면, Braze를 사용하여 모든 프로모션을 추적할 수 없더라도 최근 프로모션한 제품의 세그먼트 간 인기도를 비교할 수 있습니다.
- **광고를 사용하는 미디어 앱:** 동영상 또는 오디오 클립 사이에 광고로 인해 사용자 경험이 중단되는 경우, 광고 중간 이탈을 커스텀 이벤트로 기록하고 광고 중간 이탈/DAU 비율을 계산하면 광고 없는 프리미엄 구독 캠페인으로 타겟팅할 최적의 세그먼트를 찾는 데 도움이 될 수 있습니다.

## 수식 만들기

공식은 대시보드의 [홈]({{site.baseurl}}/user_guide/analytics/dashboard/home_dashboard/), [매출 보고서]({{site.baseurl}}/user_guide/data/export_braze_data/exporting_revenue_data/) 및 [커스텀 이벤트 보고서]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) 페이지의 통계 패널에서 액세스할 수 있습니다. 이 패널을 보려면 **시간 경과에 따른 성능/성과** 차트로 이동하여 **통계 대상** 드롭다운을 **KPI 공식으로** 변경한 다음 하나 이상의 KPI 공식을 선택하여 차트를 채우세요.

\![Braze 대시보드에서 KPI 공식에 대한 통계 보기]({% image_buster /assets/img_archive/kpi_forms.png %})

새 수식을 만들려면 다음과 같이 하세요:

1. 해당 대시보드**(홈**, **매출 보고서** 또는 **커스텀 이벤트 보고서**)로 이동합니다.
2. **KPI 공식 관리를** 선택합니다.
3. 공식의 이름을 입력합니다.
4. 관련 분자와 분모를 선택합니다.
5. **저장을** 선택합니다.

## 사용 가능한 분자 및 분모

<style>
  div.small_table + table {
    max-width: 50%;
  }
  div.large_table + table {
    max-width: 75%;
  }
table th:nth-child(1),
table th:nth-child(2),
table th:nth-child(3),
table td:nth-child(1),
table td:nth-child(2),
table td:nth-child(3) {
    width:25%;
}
table td {
    word-break: break-word;
}
</style>

<div class="small_table"></div>

### 개요 대시보드

| 숫자 | 분모 |
| --- | --- |
| DAU | MAU |
| 세션 | DAU |
| | 세그먼트 크기 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 매출 대시보드

| 숫자 | 분모 |
| --- | --- |
| 구매(전체) | DAU |
| 구매 선택(예: 기프트 카드 또는 제품 ID) | MAU |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 커스텀 이벤트 대시보드

| 숫자 | 분모 |
| --- | --- |
| 커스텀 이벤트 횟수 | MAU |
|  | DAU |
|  | 세그먼트 크기( [분석 추적이]({{site.baseurl}}/viewing_and_understanding_segment_data/) 활성화된 세그먼트만 사용 가능) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

