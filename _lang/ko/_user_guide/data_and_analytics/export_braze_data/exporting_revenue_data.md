---
nav_title: 수출 수익 및 총 수익 데이터
article_title: 수출 수익 및 총 수익 데이터
page_order: 4
page_type: reference
description: "이 참고 문서에서는 매출 데이터 및 통계를 내보내는 방법에 대해 설명합니다."
tool: 
  - Reports

---

# 수익 및 총 수익 데이터 내보내기

> 이 페이지는 대시보드의 [매출 보고서]({{site.baseurl}}/user_guide/data_and_analytics/reporting/revenue_report/) 페이지를 다루며, 특정 기간 동안의 매출 데이터, 특정 제품의 매출 및 귀하의 앱의 총 매출을 볼 수 있습니다.

**애널리틱스에서** **수익 보고서를** 찾을 수 있습니다.

{% alert note %}
[이전 탐색을]({{site.baseurl}}/navigation) 사용하는 경우 **데이터에서** **매출**을 찾을 수 있습니다.
{% endalert %}

{% alert tip %}
매출 데이터를 확보하는 더 많은 방법을 찾고 계신가요? 캠페인이나 캔버스에 제품 구매뿐만 아니라 구매 행동을 [전환 이벤트로]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/) 추가해 보세요.
{% endalert %}

수익 데이터를 내보내려면 <i class="fas fa-bars" title="차트 컨텍스트 메뉴"></i>에서 **성능 시간 경과** 그래프를 선택하고 내보내기 옵션을 선택하세요.

## 시간 경과에 따른 성능 그래프

다음 데이터는 **성능/성과** 그래프에서 볼 수 있습니다:

- KPI 산출식
- 구매
    - (선택 사항) 제품별 구매
- 매출
    - (선택 사항) 세그먼트별 수익
    - (선택 사항) 제품별 수익
- 시간별 수익
    - (선택 사항) 세그먼트별 시간당 매출
- 사용자당 수익

![수익 그래프][9]

## 총 매출

[캠페인 분석]({{site.baseurl}}/user_guide/data_and_analytics/reporting/campaign_analytics/) 또는 [캔버스 분석]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) 페이지에서 사례별로 수익 통계를 확인할 수 있습니다. 

{% multi_lang_include metrics.md metric='총 매출' %}

{% alert tip %}
매출 보고서는 API를 통해 내보낼 수 없습니다. CSV 내보내기에 대한 도움말은 [내보내기 문제 해결]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/)을 참조하세요.
{% endalert %}

{% comment %}

## 직접 수익

[보고서 작성기를][1] 사용하여 캠페인 비교 보고서를 생성하면 다음과 같은 추가 수익 지표를 확인할 수 있습니다:

- [총 직접 수익][2]
- [총 직접 구매 수][3]
- [고유 직접 구매 수][4]
- [수신자 당 수익][5]

이 측정기준은 마지막 클릭 기여도에 기반하며, 이는 매출이 캠페인에 귀속된다는 것을 의미합니다. 만약 그 캠페인이:

1. 사용자가 구매하기 전에 클릭한 마지막 캠페인인가요?
    <br>**AND**<br>
2. 사용자가 구매하기 3일 이내에 클릭했습니다.

{% endcomment %}

[1]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/
[2]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#total-direct-revenue
[3]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#total-direct-purchases
[4]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#unique-direct-purchases
[5]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#revenue-per-recipient



[9]: {% image_buster /assets/img_archive/Export_revenue_graph.png %}
