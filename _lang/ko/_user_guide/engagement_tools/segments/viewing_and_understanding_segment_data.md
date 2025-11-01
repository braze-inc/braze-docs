---
nav_title: 세그먼트 데이터
article_title: 세그먼트 데이터 보기 및 이해하기
page_order: 4
page_type: reference
description: "이 페이지에서는 Braze 대시보드의 세그먼트 섹션에 대해 설명하고 제공된 통계에 대한 요약 정보를 제공합니다."
alias: /viewing_and_understanding_segment_data/
tool: 
  - Segments
  - Reports
  
---
# 세그먼트 데이터

> 이 페이지에서는 Braze 대시보드의 세그먼트 섹션에 대해 설명하고 제공된 통계에 대한 요약 정보를 제공합니다.

## 세그먼트 및 멤버십에 대한 데이터에 액세스하기

Braze 대시보드의 **세그먼트** 페이지에는 모든 세그먼트에 대한 요약이 포함되어 있으며 각 세그먼트에 대한 자세한 데이터를 살펴볼 수 있습니다. 이 페이지에서 세그먼트의 이름을 검색하고 선택하여 해당 데이터를 편집하고 확인합니다. 세그먼트를 만드는 방법을 알아보려면 [세그먼트 만들기를]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment) 참조하세요.

\![세그먼트 페이지]({% image_buster /assets/img_archive/segments.png %})

세그먼트 이름을 선택한 후 세그먼트 통계 및 필터를 확인하고 필터를 추가하거나 삭제하여 세그먼트를 편집할 수 있습니다. 변경 사항이 있으면 반드시 저장하세요!

[세그먼트에 대한 분석 추적을]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/) 켜면 이 세그먼트의 시간 경과에 따른 세션, 커스텀 이벤트 및 매출을 볼 수 있습니다.

\![세그먼트에 대한 분석 추적 토글]({% image_buster /assets/img_archive/A_Tracking_2.png %})

### 세그먼트 통계

필터를 추가하거나 삭제하면 실시간으로 업데이트되는 다음 세그먼트 통계를 볼 수 있습니다:

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>통계</th>
            <th>정의</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split">총 사용자 수</td>
            <td class="no-split">앱의 총 사용자 수입니다.</td>
        </tr>
        <tr>
            <td class="no-split">선택한 사용자</td>
            <td class="no-split">세그먼트에 포함된 사용자 수와 전체 사용자 기반에서 차지하는 비율을 확인할 수 있습니다.</td>
        </tr>
        <tr>
            <td class="no-split">LTV(유료 사용자)</td>
            <td class="no-split">이 세그먼트의 사용자당 생애주기 가치(LTV)와 이 세그먼트의 유료 사용자당 생애주기 가치입니다. LTV는 평생 매출을 평생 사용자 수로 나누어 계산합니다.</td>
        </tr>
        <tr>
            <td class="no-split">이메일 수신 가능(옵트인)</td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Emailable' %} <a href="/docs/help/best_practices/spam_regulations/#spam-regulationsspam regulations">스팸 규정으로</a> 인해 사용자가 초기 확인 이메일의 링크를 클릭해야 하는 이중 옵트인 정책을 구현하여 사용자에게 명시적으로 옵트인하도록 요청하는 것이 좋습니다. 더 많은 사용자가 옵트인하도록 유도하려면 <a href="/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/#segmenting-by-user-subscriptions">옵트인하지 않은 사용자를</a> 대상으로 메시지를 타겟팅할 수 있습니다.</td>
        </tr>
        <tr>
            <td class="no-split">푸시 인에이블먼트(옵트인)</td>
            <td class="no-split">푸시 인에이블먼트는 푸시 토큰을 하나 이상 보유한 사용자 수를 의미합니다. 일부 사용자는 여러 개의 푸시 토큰을 가지고 있을 수 있으므로(예: iPhone과 iPad를 소유한 경우) 이 세그먼트에 보내는 푸시 알림의 수가 '푸시 인에이블먼트' 사용자 수보다 많을 수 있습니다. '옵트인'은 푸시 알림을 명시적으로 옵트인한 사용자 수를 의미합니다. 사용자가 푸시를 보내려면 항상 명시적으로 옵트인해야 합니다.</td>
        </tr>
    </tbody>
</table>

### 세그먼트 인사이트

대시보드의 [세그먼트 인사이트]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_insights/) 페이지에서 미리 선택된 일련의 KPI에 대해 한 세그먼트가 다른 세그먼트에 비해 어떤 성능/성과를 보이고 있는지 확인할 수 있습니다.

### 메시징 사용
**메시징 사용** 섹션에는 어떤 세그먼트, 현재 활성화된 캠페인, 현재 활성화된 캔버스가 세그먼트를 타겟팅하고 있는지 표시됩니다.

### 과거 멤버십

**과거 멤버십** 섹션에서는 시간이 지남에 따라 세그먼트의 규모가 어떻게 변했는지 확인할 수 있습니다. 드롭다운을 사용하여 날짜 범위별로 멤버십을 세분화하여 필터링할 수 있습니다.

세그먼트의 멤버십 및 규모를 모니터링하는 방법에 대해 자세히 알아보려면 [세그먼트 규모 측정하기를]({{site.baseurl}}/user_guide/engagement_tools/segments/measuring_segment_size/) 참조하세요.

### 사용자 미리 보기

세그먼트에 대한 자세한 사용자별 정보를 보려면 **사용자 데이터를** 클릭하고 **사용자 미리 보기를** 선택합니다.

이 페이지에서 성별, 연령, 세션 수, 푸시 및 이메일 옵트인 여부 등 다양한 사용자별 속성을 확인할 수 있습니다.

작업 공간 크기에 비해 세그먼트가 매우 작은 경우에는 사용자 미리보기에서 사용자가 0명으로 표시될 수 있습니다. [정확한 통계 계산을]({{site.baseurl}}/user_guide/engagement_tools/segments/measuring_segment_size/#statistics-for-segment-size) 실행하여 세그먼트의 정확한 크기를 확인하려면 [정확한 통계 계산을]({{site.baseurl}}/user_guide/engagement_tools/segments/measuring_segment_size/#statistics-for-segment-size) 실행하세요.

\![사용자 미리보기]({% image_buster /assets/img_archive/user_preview.png %})

## 세그먼트별 성능/성과 데이터 보기

[쿼리 빌더 보고서 템플릿을]({{site.baseurl}}/user_guide/analytics/reporting/data_by_segments/) 사용하여 캠페인, 캔버스, 배리언트 및 세그먼트별 단계에 대한 성능/성과 측정기준을 세분화할 수 있습니다.

## 쿼리 빌더를 사용하여 세그먼트 세분화 보고서 만들기

[쿼리 빌더]({{site.baseurl}}/user_guide/analytics/query_builder/) 템플릿에서 보고서를 만들려면 **쿼리 빌더로** 이동하여 다음과 같이 하세요:

1. **SQL 쿼리 만들기** > **쿼리 템플릿을** 선택합니다.
2. '세그먼트 세분화'를 포함하는 측정기준이 있는 템플릿을 필터링합니다.
3. 사용하려는 템플릿을 선택합니다.
4. [변수](#variables) 탭에서 SQL 템플릿의 변수를 채웁니다.
5. (선택 사항) 템플릿에서 SQL을 직접 편집합니다.
6. **쿼리 실행을** 선택합니다. 결과가 표로 표시됩니다.

## 변수 {#variables}

보고서를 생성하기 전에 **변수** 탭으로 이동하여 보고서에 따라 달라지는 필수 변수를 포함하여 보고서 빌더 템플릿에 대한 정보를 제공하세요. 

변수는 다음과 같습니다:

- **캠페인 또는 캔버스:** 하나 또는 여러 개의 캠페인 또는 캔버스를 포함할 수 있습니다(지정할 수 있는 캠페인 또는 캔버스 수에는 제한이 없습니다). 캠페인이나 캔버스를 지정하지 않으면 선택한 기간의 모든 캠페인이나 캔버스가 보고서에 포함됩니다.
- **배리언트:** 배리언트 수준 분류를 제공하는 템플릿을 사용하는 경우 캠페인 또는 캔버스를 선택한 후 해당 캠페인 또는 캔버스 내에서 배리언트를 선택할 수 있습니다. 여러 배리언트를 선택하면 결과가 배리언트별로 그룹화됩니다.
- **Step:** 캔버스 배리언트를 선택하면 캔버스 단계를 선택할 수 있습니다. 캔버스 배리언트를 먼저 선택하지 않으면 단계를 선택할 수 없습니다. 
- **시간 범위:** 데이터를 가져올 기간을 식별합니다. 시간 범위를 지정하지 않으면 기본값은 지난 30일입니다.
- **제품 이름:** 구매 데이터에 대한 리포트를 실행하는 경우 데이터를 가져올 특정 제품을 식별할 수 있습니다.
- **전환 창:** 매출 및 구매 데이터가 포함된 보고서에는 항상 필요합니다. 이메일 수신 또는 클릭 후 Braze가 구매 또는 매출 기여도를 속성으로 지정해야 하는 일수입니다.
- **세그먼트:** 데이터를 세분화할 세그먼트를 식별합니다. 지정하지 않으면 분석 추적이 켜져 있는 모든 세그먼트에 대해 리포트가 실행됩니다.
- **태그:** **변수에서** 태그를 지정하여 특정 태그가 있는 모든 캠페인 또는 캔버스에 대한 리포트를 실행할 수 있습니다. 여러 태그를 포함할 수 있습니다. 태그와 특정 캠페인 또는 캔버스를 모두 보고서에 추가하는 경우 보고서에 태그와 지정된 캠페인 또는 캔버스의 데이터가 포함됩니다. 

## 데이터 가용성

이 두 가지 조건이 모두 충족되는 기간 동안 데이터를 사용할 수 있습니다:

1. 데이터를 보려는 세그먼트에 대해 세그먼트 [분석 추적이]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/) 켜져 있습니다.
2. 세그먼트별 성능/성과 데이터 기능이 켜져 있습니다.

회사에서 이 기능을 사용 설정하기 이전의 기간의 데이터에는 액세스할 수 없습니다. 예를 들어 10월 1일에 세그먼트 A에 대해 분석 추적이 켜져 있고 10월 2일에 회사에 이 기능이 켜져 있는 경우, 10월 2일 이후에 측정기준을 기록한 캠페인 및 캔버스에 대해 세그먼트 A에 대한 데이터만 볼 수 있습니다. 

회사가 10월 2일에 이 기능을 켜고 10월 3일에 세그먼트 B에 대한 분석 추적을 켜는 경우, 10월 3일 이후에 측정기준을 기록한 캠페인 및 캔버스에 대한 세그먼트 B의 데이터만 볼 수 있습니다.


