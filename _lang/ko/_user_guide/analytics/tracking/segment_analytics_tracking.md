---
nav_title: 세그먼트 분석 추적
article_title: 세그먼트 분석 추적
page_order: 8
page_type: reference
description: "이 참조 문서에서는 세그먼트 분석 추적과 시간별 매출 및 구매, 시간별 세션, 시간별 커스텀 이벤트를 보는 방법에 대해 설명합니다."
tool: 
  - Segments
  - Reports
---

# 세그먼트 분석 추적

> 세그먼트에 대해 애널리틱스 추적이 켜져 있으면 해당 세그먼트의 세션, 사용자 지정 이벤트 및 시간 경과에 따른 수익을 볼 수 있습니다.

세그먼트에 대해 애널리틱스 추적을 켜지 않은 경우에도 해당 세그먼트의 [실시간 통계에][11] 액세스하고 해당 사용자를 캠페인으로 타겟팅할 수 있습니다. 유일한 차이점은 이 페이지에 언급된 특정 분석 도구에 액세스할 수 있는지 여부입니다.

## 세그먼트 분석 켜기

세그먼트 페이지의 **세그먼트 세부 정보** 섹션에서 **애널리틱스 추적을** 켭니다.

![세그먼트에 대한 애널리틱스 추적 토글][16]

앱은 최대 25개의 세그먼트에 대해 추적을 설정할 수 있습니다. Braze는 캠페인이 세션, 매출, 구매에 미치는 영향을 파악할 때 분석해야 할 중요한 세그먼트를 추적할 것을 권장합니다.

## 시간 경과에 따른 매출 및 구매 보기

**분석** > **매출 보고서로** 이동하여 [이 세그먼트의 시간별 매출 및 구매][14] 데이터를 확인합니다.

![세그먼트별 매출 데이터][17]

사용자 지정 시간 범위에 대한 세그먼트 데이터를 시각적으로 비교하려면 그래프에서 세그먼트를 추가하거나 제거합니다. **분석** 드롭다운에서 **세그먼트별**을 선택한 다음 **분석 값**에서 세그먼트를 선택합니다.

그래프 위의 세그먼트 이름을 선택하여 해당 세그먼트의 지표에 대한 표시 여부를 설정하거나 해제할 수 있습니다.

![여러 세그먼트에 대한 수익][21]

## 시간별 세션

마찬가지로 **홈** 페이지에서 [이 특정 세그먼트의 시간별 세션에 대한][13] 데이터를 찾을 수 있습니다.

![세그먼트별 세션 데이터][18]

## 시간 경과에 따른 사용자 지정 이벤트 보기

**분석** > **커스텀 이벤트 보고서로** 이동하여 [세그먼트에 대한 시간별 커스텀 이벤트][20]에 대한 데이터를 확인합니다.

## 쿼리 작성기 템플릿 사용

분석 추적이 켜져 있으면 쿼리 빌더 보고서 템플릿을 사용하여 캠페인, 캔버스, 배리언트 및 단계에 대한 성과 지표를 세그먼트별로 세분화할 수 있습니다. 자세히 알아보려면 [세그먼트 데이터를]({{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/#performance-data-by-segment) 확인하세요.

[11]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/#segment-statistics
[13]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_app_usage_data/#exporting-app-usage-data
[14]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/
[16]: {% image_buster /assets/img_archive/A_Tracking_2.png %}
[17]: {% image_buster /assets/img_archive/Revenue.png %}
[18]: {% image_buster /assets/img_archive/events_over_time2.png %}
[20]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#analytics
[21]: {% image_buster /assets/img_archive/segment_revenue_multiple.png %}
