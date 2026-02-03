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
2. **새 보고서 만들기** 버튼 옆의 **추가 옵션** 화살표를 선택한 다음 **보고서 템플릿 사용을** 선택합니다.<br><br>!['새 보고서 생성' 버튼 드롭다운에는 커스텀 보고서를 만들거나 템플릿을 사용할 수 있는 옵션이 있습니다.]({% image_buster /assets/img/report_builder_2/create_new_report.png %}){: style="max-width:40%;"}<br><br>
3. Braze 템플릿 라이브러리에서 보고서 템플릿 중 하나를 선택합니다.
    - **행 항목** 및 **태그** 드롭다운을 사용하여 사용 사례와 관련된 보고서를 찾을 수 있습니다.<br><br>!["선택할 수 있는 Braze 템플릿 목록이 있는 '보고서 템플릿' 창입니다.]({% image_buster /assets/img/report_builder_2/report_templates.png %}){: style="max-width:90%;"}<br><br>
4. [보고서 만들기의](#creating-a-report) 3단계 이후에 따라 사용 사례에 맞게 보고서를 추가로 사용자 지정할 수 있습니다.

## 보고서 만들기

1. **애널리틱스** > **보고서 작성기(신규)**로 이동합니다.
2. **새 보고서 만들기를** 선택합니다.
3. **행** 드롭다운에서 보고할 항목을 선택합니다:
    - 캠페인
    - 캔버스
    - 캠페인 및 캔버스
    - 채널
    - 태그

    **행을** 선택하면 [볼 수 있는 측정기준에](#metrics-availability) 영향을 미칩니다. 예를 들어, **캔버스** 또는 **배리언트** 드릴다운이 있는 **캠페인에** 대해 보고하는 경우에만 다변량 측정기준을 볼 수 있습니다. 캠페인 및 캔버스에 다변량 테스트가 있는 경우에도 **캠페인 및 캔**버스에 대한 보고 시에는 이러한 측정기준을 볼 수 없습니다. 

![보고서의 행과 그룹을 선택할 수 있는 필드가 있는 '행 및 열' 섹션입니다.]({% image_buster /assets/img/report_builder_2/rows_and_columns.png %}){: style="width:90%;"}

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

![여러 측정기준을 선택할 수 있는 옵션이 있는 '측정기준 커스텀' 섹션입니다.]({% image_buster /assets/img/report_builder_2/customize_metrics.png %}){: style="width:90%;"}

{: start="6"}
6\. 카테고리별로 메트릭을 찾아보고 해당 확인란을 선택하여 보고서에 메트릭을 추가합니다.
    \- 점선 아이콘을 위 또는 아래로 드래그하여 지표와 열의 순서를 변경합니다.
7\. **보고서 내용에서** 보고서에 데이터를 포함할 날짜 범위를 구성합니다.
8\. 그런 다음 3단계에서 선택한 내용에 따라 캠페인, 캔버스 또는 둘 다를 보고서에 수동 또는 자동으로 추가하도록 선택합니다.
    - **수동으로 추가합니다:** **마지막으로 보낸** 날짜와 태그 또는 채널에 대한 필터를 사용하거나 캠페인 또는 캔버스 이름을 검색하여 보고서에 포함할 각 캠페인 또는 캔버스를 선택합니다.<br><br>!['수동으로 캠페인 및 캔버스 추가' 섹션에는 선택할 캠페인 목록이 표시됩니다.]({% image_buster /assets/img/report_builder_2/manually_add.png %}){: style="width:90%;"}<br><br>
    - **자동으로 추가합니다:** 보고서에 포함할 캠페인 또는 캔버스에 대한 규칙을 설정합니다. 이 페이지에서는 하나의 필드만 선택하면 됩니다.
        \- 이 화면에서 설정한 조건을 충족하는 캠페인 또는 캔버스가 추가되면 향후 보고서 실행에 자동으로 추가됩니다.<br><br>!['캠페인 및 캔버스 자동 추가' 섹션에는 보고서에 추가할 캠페인과 캔버스에 대한 규칙을 설정할 수 있는 필드가 있습니다.]({% image_buster /assets/img/report_builder_2/automatically_add.png %}){: style="width:90%;"}<br><br>
9\. **저장 & 실행을** 선택하여 리포트를 실행합니다.

{% alert note %}
보고서는 구성 단계에서 선택한 날짜 범위와 캠페인 또는 캔버스의 수에 따라 실행하는 데 최대 몇 분 정도 걸릴 수 있습니다.
{% endalert %}

## Metrics availability

Your selection for **Rows** affects the metrics you can select.

{% alert tip %}
캔버스 배리언트 또는 단계에 대해 보고하려면 행에 대해 **캔버스를** 선택하고 필드를 비워 두거나 드릴다운으로 **날짜를** 선택합니다. 이렇게 하면 캔버스 **보기** 드롭다운이 생성되어 캔버스에 대한 측정기준만 보거나 배리언트, 단계 또는 메시지별로 측정기준을 그룹화할 수 있습니다. 

![열린 '캔버스 보기' 드롭다운.]({% image_buster /assets/img/report_builder_2/canvas_view_dropdown.png %}){: style="width:40%;"}
{% endalert %}

| Metric | Description |
| --- | --- |
| Conversion metrics | Available for Campaigns, Canvases, Campaigns and Canvases. |
| Entries | Available for Campaigns, Canvases, Campaigns and Canvases, Tags. |
| Last Sent Date | Available for Campaigns, Canvases, Campaigns and Canvases. 예약된 캠페인에 대해서만 표시되며, 액션 기반 또는 API 트리거 캠페인에는 표시되지 않습니다. |
| Sends | Available for each relevant channel. |
| Messages Sent | Available for Campaigns, Canvases, Campaigns and Canvases, Tags. |
| Subject line | Available for email Campaigns with **Variant** drilldown, Canvases, and Canvases with **Variant** drilldown. |
| Total Revenue | Available for Campaigns, Canvases, Campaigns and Canvases, Tags. Unavailable with **Channels** drilldown. |
| Unique Impressions | Available for Campaigns, Canvases, Campaigns and Canvases, Tags. |
| Unique Recipients | Available for Campaigns, Canvases, Campaigns and Canvases, Tags. Unavailable with **Channels** drilldown. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### 삭제된 메시지 배리언트

보고서를 캠페인 또는 캔버스별로 분류할 때 삭제된 메시지 배리언트에 대한 통계는 표시되지 않습니다. 그러나 채널 수준 합계에는 배리언트가 삭제되었는지 여부와 관계없이 모든 통계가 포함됩니다. 예를 들어 이메일 _발송에는_ 모든 이메일 발송이 포함되지만 캠페인별로 통계를 세분화하면 삭제된 메시지 배리언트에 대한 발송이 필터링되므로 수치가 더 낮아질 수 있습니다.

## 보고서 보기

보고서를 실행한 후 보고서 페이지에서 결과를 표 형식으로 볼 수 있습니다. 

![각 캠페인의 측정기준에 대한 보고서 데이터 표입니다.]({% image_buster /assets/img/report_builder_2/report_table.png %}){: style="width:90%;"}

### 보고서 차트 만들기

페이지 하단에서 **차트 유형을** 선택하고 차트 메트릭을 구성하여 데이터 차트를 만들 수 있습니다. 기본적으로 첫 번째 메트릭이 표시됩니다.

![보고서 데이터의 차트로 차트의 X축, Y축, 차트 유형 등을 구성할 수 있는 옵션이 있습니다.]({% image_buster /assets/img/report_builder_2/visualize_table.png %}){: style="max-width:90%;"}

{% alert note %}
꺾은선형 차트를 만들려면 보고서를 구성할 때 드릴다운 옵션으로 **날짜를** 선택합니다. 시간 경과에 따른 추세가 표시됩니다.
{% endalert %}

#### 보고서 차트 다운로드

보고서 차트의 이미지를 다운로드하려면 점선 아이콘을 선택한 다음 다운로드 옵션을 선택합니다.

![다양한 파일 형식에 대한 다운로드 옵션이 있는 메뉴입니다.]({% image_buster /assets/img/report_builder_2/download_options.png %}){: style="max-width:70%;"}

## 보고서 공유

**공유를** 선택하고 다음 옵션 중 하나를 선택하여 보고서에 대한 대시보드 링크를 공유할 수 있습니다:
- **링크를 공유합니다:** 링크를 복사하여 공유합니다.

!["보고서 링크가 있는 '링크 공유' 드롭다운을 클릭합니다.]({% image_buster /assets/img/report_builder_2/share_this_report.png %}){: style="max-width:70%;"}

- **이메일을 보내거나 예약합니다:** 1시간 후에 만료되는 다운로드 링크가 포함된 이메일을 즉시 또는 지정된 시간에 전송합니다. **이메일 수신자** 드롭다운에 나열된 대시보드 사용자 중에서 수신자를 선택하거나 다른 이메일 주소를 입력할 수 있습니다.

!['이메일 예약' 창에서 보고서 형식, 수신 대상, 전송 시기를 선택할 수 있는 필드가 있습니다.]({% image_buster /assets/img/report_builder_2/schedule_an_email.png %}){: style="max-width:70%;"}

- **CSV를 다운로드합니다:** 보고서의 CSV를 다운로드하세요.

## 대시보드에 보고서 추가하기

1. 보고서 표 상단의 점선 아이콘을 선택합니다.
2. **대시보드에 추가를** 선택합니다.
3. 새 대시보드를 만들지 기존 대시보드에 추가할지 선택합니다.<br><br>![새 대시보드 또는 기존 대시보드에 보고서를 추가할지 여부를 선택할 수 있는 옵션이 있는 창입니다.]({% image_buster /assets/img/report_builder_2/add_to_dashboard.png %}){: style="width:90%;"}<br><br>
4. 대시보드 [빌더의]({{site.baseurl}}/user_guide/analytics/reporting/dashboard_builder/) 단계를 따라 대시보드 작성에 대해 자세히 알아보세요.

