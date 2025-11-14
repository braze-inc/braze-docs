---
nav_title: 수출 매출 및 총 매출 데이터
article_title: 수출 매출 및 총 매출 데이터
page_order: 4
page_type: reference
description: "이 참고 문서에서는 매출 데이터 및 통계를 내보내는 방법에 대해 설명합니다."
tool: 
  - Reports

---

# 수출 매출 및 총 매출 데이터

> 이 페이지에서는 대시보드의 [매출 보고서]({{site.baseurl}}/user_guide/analytics/reporting/revenue_report/) 페이지에서 특정 기간 동안의 매출, 특정 제품 매출, 앱의 총 매출에 대한 데이터를 확인할 수 있습니다.

**매출 보고서는** **분석에서** 찾을 수 있습니다.

{% alert tip %}
매출 데이터를 얻을 수 있는 더 많은 방법을 찾고 계신가요? 제품 구매뿐만 아니라 구매 행동을 캠페인이나 캔버스에 [전환 이벤트로]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) 추가해 보세요.
{% endalert %}

매출 데이터를 내보내려면 다음을 선택합니다. <i class="fas fa-bars" title="차트 컨텍스트 메뉴"></i> 을 선택하고 내보내기 옵션을 선택합니다.

## 시간 경과에 따른 성능/성과 그래프

**시간 경과에 따른 성능/성과** 그래프에서 다음 데이터를 볼 수 있습니다:

- KPI 공식
- 구매
    - (선택 사항) 제품별 구매
- 매출
    - (선택 사항) 세그먼트별 매출
    - (선택 사항) 제품별 매출
- 시간당 매출
    - (선택 사항) 세그먼트 별 시간당 매출
- 사용자당 매출

\![매출 그래프]({% image_buster /assets/img_archive/Export_revenue_graph.png %})

## 총 매출

[캠페인 분석]({{site.baseurl}}/user_guide/analytics/reporting/campaign_analytics/) 또는 [캔버스 분석]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) 페이지에서 사례별로 매출 통계를 확인할 수 있습니다. 

{% multi_lang_include analytics/metrics.md metric='Total Revenue' %}

{% alert tip %}
API를 통해 매출 보고서를 내보낼 수 없습니다. CSV 내보내기에 대한 도움말은 [내보내기 문제 해결을]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/) 참조하세요.
{% endalert %}

{% comment %}

## 직접 매출

[보고서 빌더를]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/) 사용하여 캠페인 비교 보고서를 생성하면 다음과 같은 추가 매출 측정기준을 확인할 수 있습니다:

- [총 직접 매출]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#total-direct-revenue)
- [총 직접 구매액]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#total-direct-purchases)
- [고유한 직접 구매]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#unique-direct-purchases)
- [수신자당 매출]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#revenue-per-recipient)

이러한 측정기준은 마지막 클릭 속성을 기반으로 하며, 이는 해당 캠페인의 경우 해당 캠페인에 매출이 기여한 것으로 간주됨을 의미합니다:

1. 사용자가 구매하기 전에 마지막으로 클릭한 캠페인입니다.
    <br>**AND**<br>
2. 구매 전 3일 이내에 사용자가 클릭한 경우

{% endcomment %}




