---
nav_title: 매출 보고서
article_title: 매출 보고서
page_type: reference
description: "이 페이지에서는 매출 보고서 페이지를 사용하여 특정 기간의 매출, 특정 제품 매출 및 앱의 총 매출에 대한 데이터를 보는 방법에 대해 설명합니다."
tool: Reports
---

# 매출 보고서

> 매출 보고서 페이지에서는 특정 기간 동안의 매출, 특정 제품 매출, 앱의 총 매출에 대한 데이터를 확인할 수 있습니다.

대시보드에서 매출 보고서를 보려면 **분석** > **매출 보고서로** 이동합니다. 

## 매출 보고서 커스텀하기

날짜 범위, 보고할 앱, 매개변수를 선택하여 매출 보고서를 커스텀할 수 있습니다.

'매출'을 매개변수로 설정한 '시간 경과에 따른 성능/성과' 그래프를 보여주는 '매출 보고서' 페이지.]({% image_buster /assets/img/revenue_report.png %})

### 날짜 및 앱별로 필터링하기

매출 보고서의 날짜 범위를 선택하고 원하는 경우 특정 앱 또는 일부 앱을 선택할 수 있습니다.

### 매개변수별 필터링

**시간 경과에 따른 성능/성과** 그래프는 **통계 대상** 드롭다운에서 선택할 수 있는 다양한 매개변수에 대한 데이터를 보여줍니다. **분석** 드롭다운에서 특정 매개변수의 데이터를 선택적으로 세분화할 수 있습니다.

**시간 경과에 따른 성능/성과 그래프에서** 다음 데이터를 볼 수 있습니다:
- KPI 공식
- 구매
    - (선택 사항) 제품별 구매
- 매출
    - (선택 사항) 세그먼트별 매출
    - (선택 사항) 제품별 매출
- 시간당 매출
    - (선택 사항) 세그먼트 별 시간당 매출
- 사용자당 매출

## 매출 계산 이해하기

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>측정기준</th>
            <th>정의</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#lifetime-revenue">평생 매출</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Lifetime Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#lifetime-value-per-user">사용자당 생애주기 가치</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Lifetime Value Per User' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#average-daily-revenue">일 평균 매출</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Average Daily Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#daily-purchases">일일 구매</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Daily Purchases' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#daily-revenue-per-user">사용자당 일일 매출</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Daily Revenue Per User' %}</td>
        </tr>
    </tbody>
</table>

## 제품 분석 보기

선택한 기간 동안 구매한 제품 목록, 각 제품의 구매 수량, 각 제품이 창출한 매출은 **제품 분석** 표를 참조하세요.

'제품 이름', '구매', '매출' 열이 표시된 '제품 분석' 표입니다.]({% image_buster /assets/img/revenue_report_product_breakdown.png %})


