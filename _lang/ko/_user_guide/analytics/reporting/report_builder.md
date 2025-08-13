---
nav_title: 보고서 빌더
article_title: 보고서 빌더
alias: /report_builder/
page_type: reference
description: "이 참조 문서에서는 보고서 작성기 기능에 대해 설명합니다."
tool:
    - Reports
page_order: 6.2
---

# 보고서 빌더

> 이 페이지에서는 보고서 작성기를 사용하여 Braze 데이터를 사용하여 세분화된 보고서를 만들고 보는 방법과 대시보드에 보고서를 추가하는 방법에 대해 설명합니다.

## 보고서 템플릿 사용

1. **애널리틱스** > **보고서 작성기(신규)**로 이동합니다.
2. **새 보고서 만들기** 버튼 옆의 **추가 옵션** 화살표를 선택한 다음 **보고서 템플릿 사용을** 선택합니다.<br><br>!["Create New Report" button dropdown with options to create a custom report or use a template.]({% image_buster /assets/img/report_builder_2/create_new_report.png %}){: style="max-width:40%;"}<br><br>
3. Braze 템플릿 라이브러리에서 보고서 템플릿 중 하나를 선택합니다.
    - **행 항목** 및 **태그** 드롭다운을 사용하여 사용 사례와 관련된 보고서를 찾을 수 있습니다.<br><br>!["Braze report templates" window with list of Braze templates to select from.]({% image_buster /assets/img/report_builder_2/report_templates.png %}){: style="max-width:90%;"}<br><br>
4. [보고서 만들기의](#creating-a-report) 3단계 이후에 따라 사용 사례에 맞게 보고서를 추가로 사용자 지정할 수 있습니다.

## 보고서 만들기

1. **애널리틱스** > **보고서 작성기(신규)**로 이동합니다.
2. **새 보고서 만들기를** 선택합니다.
3. **행** 드롭다운에서 다음 중 하나를 선택하여 보고서를 만듭니다:
    - 캠페인
    - 캔버스
    - 캠페인 및 캔버스
    - 채널
    - 태그

![The "Rows and columns" section with fields to select the rows and groupings for your report.]({% image_buster /assets/img/report_builder_2/rows_and_columns.png %}){: style="width:90%;"}

{: start="4"}
4\. (선택 사항) **드릴다운 추가를** 선택하여 데이터를 더 세분화된 보기로 분류합니다:
    \- 채널
    \- 날짜
        \- 이 기능을 사용하여 데이터를 더 작은 시간 범위로 분할할 수 있습니다. 예를 들어, 캠페인의 일별 실적을 확인하려면 다음 구성을 선택합니다:
            - **행**: 캠페인
            - **그룹화:** 날짜
            - **간격:** 일
    \- 변형
    \- 캠페인 및 캔버스

{% alert tip %}
Try out different configurations of drilldown options to explore the [many ways you can break down your data](#metrics-availability).
{% endalert %}

{: start="5"}
5\. **열** 섹션에서 **지표 사용자 지정을** 선택합니다.

![The "Customize Metrics" section with options to select multiple metrics.]({% image_buster /assets/img/report_builder_2/customize_metrics.png %}){: style="width:90%;"}

{: start="6"}
6\. 카테고리별로 메트릭을 찾아보고 해당 확인란을 선택하여 보고서에 메트릭을 추가합니다.
    \- 점선 아이콘을 위 또는 아래로 드래그하여 지표와 열의 순서를 변경합니다.
7\. **보고서 내용에서** 보고서에 데이터를 포함할 날짜 범위를 구성합니다.
8\. 그런 다음 3단계에서 선택한 내용에 따라 캠페인, 캔버스 또는 둘 다를 보고서에 수동 또는 자동으로 추가하도록 선택합니다.
    - **수동으로 추가합니다:** **마지막으로 보낸** 날짜와 태그 또는 채널에 대한 필터를 사용하거나 캠페인 또는 캔버스 이름을 검색하여 보고서에 포함할 각 캠페인 또는 캔버스를 선택합니다.<br><br>![The "Manually add campaigns and canvases" section with a list of campaigns to select.]({% image_buster /assets/img/report_builder_2/manually_add.png %}){: style="width:90%;"}<br><br>
    - **자동으로 추가합니다:** 보고서에 포함할 캠페인 또는 캔버스에 대한 규칙을 설정합니다. 이 페이지에서는 하나의 필드만 선택하면 됩니다.
        \- 이 화면에서 설정한 조건을 충족하는 캠페인 또는 캔버스가 추가되면 향후 보고서 실행에 자동으로 추가됩니다.<br><br>![The "Automatically add campaigns and canvases" section with fields to set rules for which campaigns and Canvases should be added to the report.]({% image_buster /assets/img/report_builder_2/automatically_add.png %}){: style="width:90%;"}<br><br>
9\. **저장 후 실행을** 선택하여 보고서를 실행합니다.

{% alert note %}
보고서는 구성 단계에서 선택한 날짜 범위와 캠페인 또는 캔버스의 수에 따라 실행하는 데 최대 몇 분 정도 걸릴 수 있습니다.
{% endalert %}

## Metrics availability

Your selection for **Rows** affects the metrics you can select.

| Metric | Description |
| --- | --- |
| Conversion metrics | Available for Campaigns, Canvases, Campaigns and Canvases. |
| Entries | Available for Campaigns, Canvases, Campaigns and Canvases, Tags. |
| Last Sent Date | Available for Campaigns, Canvases, Campaigns and Canvases. |
| Sends | Available for each relevant channel. |
| Messages Sent | Available for Campaigns, Canvases, Campaigns and Canvases, Tags. |
| Subject line | Available for email Campaigns with **Variant** drilldown, Canvases, and Canvases with **Variant** drilldown. |
| Total Revenue | Available for Campaigns, Canvases, Campaigns and Canvases, Tags. Unavailable with **Channels** drilldown. |
| Unique Impressions | Available for Campaigns, Canvases, Campaigns and Canvases, Tags. |
| Unique Recipients | Available for Campaigns, Canvases, Campaigns and Canvases, Tags. Unavailable with **Channels** drilldown. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## 보고서 보기

보고서를 실행한 후 보고서 페이지에서 결과를 표 형식으로 볼 수 있습니다. 

![A table of the report data for each campaign's metrics.]({% image_buster /assets/img/report_builder_2/report_table.png %}){: style="width:90%;"}

### 보고서 차트 만들기

페이지 하단에서 **차트 유형을** 선택하고 차트 메트릭을 구성하여 데이터 차트를 만들 수 있습니다. 기본적으로 첫 번째 메트릭이 표시됩니다.

![A chart of the report data with options to configure the chart's x-axis, y-axis, chart type, and more.]({% image_buster /assets/img/report_builder_2/visualize_table.png %}){: style="max-width:90%;"}

{% alert note %}
꺾은선형 차트를 만들려면 보고서를 구성할 때 드릴다운 옵션으로 **날짜를** 선택합니다. 시간 경과에 따른 추세가 표시됩니다.
{% endalert %}

#### 보고서 차트 다운로드

보고서 차트의 이미지를 다운로드하려면 점선 아이콘을 선택한 다음 다운로드 옵션을 선택합니다.

![A menu with download options for different file formats.]({% image_buster /assets/img/report_builder_2/download_options.png %}){: style="max-width:30%;"}

## 대시보드에 보고서 추가하기

1. 보고서 표 상단의 점선 아이콘을 선택합니다.
2. **대시보드에 추가를** 선택합니다.
3. 새 대시보드를 만들지 기존 대시보드에 추가할지 선택합니다.<br><br>![Window with options to select if you want to add the report to a new or existing dashboard.]({% image_buster /assets/img/report_builder_2/add_to_dashboard.png %}){: style="width:90%;"}<br><br>
4. 대시보드 [빌더의]({{site.baseurl}}/user_guide/analytics/reporting/dashboard_builder/) 단계를 따라 대시보드 작성에 대해 자세히 알아보세요.

