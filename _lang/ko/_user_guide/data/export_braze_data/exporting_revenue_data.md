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

> 이 페이지에서는 대시보드의 [수익 보고서]({{site.baseurl}}/user_guide/analytics/reporting/revenue_report/) 페이지에서 특정 기간의 수익, 특정 제품 수익 및 앱의 총 수익에 대한 데이터를 확인할 수 있습니다.

**애널리틱스에서** **수익 보고서를** 찾을 수 있습니다.

{% alert tip %}
매출 데이터를 확보하는 더 많은 방법을 찾고 계신가요? 캠페인이나 캔버스에 제품 구매뿐만 아니라 구매 행동을 [전환 이벤트로]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) 추가해 보세요.
{% endalert %}

수익 데이터를 내보내려면 다음을 선택합니다. **시간 경과에 따른 실적** 그래프에서 <i class="fas fa-bars" title="차트 컨텍스트 메뉴"></i> 을 선택하고 내보내기 옵션을 선택합니다.

## 시간 경과에 따른 성능 그래프

**시간 경과에 따른 성능** 그래프에서 다음 데이터를 볼 수 있습니다:

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

[캠페인 분석]({{site.baseurl}}/user_guide/analytics/reporting/campaign_analytics/) 또는 [캔버스 분석]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) 페이지에서 사례별로 수익 통계를 확인할 수 있습니다. 

{% multi_lang_include metrics.md metric='Total Revenue' %}

{% alert tip %}
수익 보고서는 API를 통해 내보낼 수 없습니다. CSV 내보내기에 대한 도움말은 [내보내기 문제 해결]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/)을 참조하세요.
{% endalert %}

{% comment %}

## 직접 수익

[보고서 작성기를][1] 사용하여 캠페인 비교 보고서를 생성하면 다음과 같은 추가 수익 지표를 확인할 수 있습니다:

- [총 직접 수익][2]
- [총 직접 구매 수][3]
- [고유 직접 구매 수][4]
- [수신자 당 수익][5]

이러한 지표는 최종 클릭 어트리뷰션을 기반으로 하며, 이는 해당 캠페인의 경우 수익이 해당 캠페인에 어트리뷰션된다는 의미입니다:

1. 사용자가 구매하기 전에 마지막으로 클릭한 캠페인입니다.
    <br>**AND**<br>
2. 사용자가 구매 전 3일 이내에 클릭한 경우

{% endcomment %}

[1]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/
[2]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#total-direct-revenue
[3]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#total-direct-purchases
[4]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#unique-direct-purchases
[5]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#revenue-per-recipient



[9]: {% image_buster /assets/img_archive/Export_revenue_graph.png %}
