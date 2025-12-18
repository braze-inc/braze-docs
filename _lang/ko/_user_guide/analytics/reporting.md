---
nav_title: 보고서
article_title: 보고서
page_order: 7
layout: dev_guide
guide_top_header: "보고서"
guide_top_text: "데이터는 사용자에게 중요한 의미를 갖기 때문에, 저희는 Braze 내에서 여러 가지 보고 옵션을 제공합니다( <a href='/docs/user_guide/data/distribution/braze_currents/'>커런츠</a> 제외). 어디서부터 시작해야 할지 잘 모르겠다면 <a href='/docs/user_guide/analytics/reporting/#reports-overview'>보고서 개요를</a> 확인하여 일반적인 마케팅 전략 질문에 답하는 데 사용할 수 있는 보고서와 분석에 대한 지침을 얻으세요."

page_type: landing
description: "이 랜딩 페이지에는 세그먼트 보고, 참여 보고서, 보고서 빌더 등 Braze 내에서 사용할 수 있는 보고 옵션(커런츠 제외)에 대한 문서가 있습니다."
tool: Reports
search_rank: 2
guide_featured_title: "섹션 기사"
guide_featured_list:
  - name: 보고서 측정기준 용어집
    link: /docs/user_guide/analytics/reporting/report_metrics/
    image: /assets/img/braze_icons/book-closed.svg
  - name: 세그먼트 데이터
    link: /docs/viewing_and_understanding_segment_data/
    image: /assets/img/braze_icons/pie-chart-01.svg
  - name: 참여 보고서
    link: /docs/user_guide/analytics/reporting/engagement_reports/
    image: /assets/img/braze_icons/line-chart-up-01.svg
  - name: 보고서 빌더
    link: /docs/user_guide/analytics/reporting/report_builder/
    image: /assets/img/braze_icons/tool-01.svg
  - name: 대시보드 빌더
    link: /docs/user_guide/analytics/reporting/dashboard_builder/
    image: /assets/img/braze_icons/tool-01.svg

guide_menu_title: "More articles"
guide_menu_list:
  - name: 보고 구성
    link: /docs/user_guide/analytics/reporting/configuring_reporting/
    image: /assets/img/braze_icons/settings-01.svg
  - name: 캠페인 분석
    link: /docs/user_guide/analytics/
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: 캔버스 분석
    link: /docs/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/
    image: /assets/img/braze_icons/line-chart-down-01.svg
  - name: 커스텀 이벤트
    link: /docs/user_guide/data/custom_data/custom_events/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 퍼널 보고서
    link: /docs/user_guide/analytics/reporting/funnel_reports/
    image: /assets/img/braze_icons/flag-02.svg
  - name: 글로벌 컨트롤 보고서
    link: /docs/user_guide/engagement_tools/testing/global_control_group/
    image: /assets/img/braze_icons/globe-04.svg
  - name: 리텐션 보고서
    link: /docs/user_guide/analytics/reporting/retention_reports/
    image: /assets/img/braze_icons/user-check-01.svg
  - name: 매출 데이터
    link: /docs/user_guide/data/export_braze_data/exporting_revenue_data/
    image: /assets/img/braze_icons/piggy-bank-02.svg
  - name: 매출 보고서
    link: /docs/user_guide/analytics/reporting/revenue_report/
    image: /assets/img/braze_icons/piggy-bank-02.svg
  - name: 세그먼트 인사이트
    link: /docs/user_guide/engagement_tools/segments/segment_insights/#segment-insights
    image: /assets/img/braze_icons/pie-chart-01.svg
  - name: 글로벌 컨트롤 그룹 보고서
    link: /docs/user_guide/analytics/reporting/global_control_group_reporting/
    image: /assets/img/braze_icons/globe-slated-02.svg
---

# 보고서 개요

## 어떤 배리언트가 이겼나요?

{% tabs local %}
{% tab Campaign Analytics %}
**캠페인 분석**

[캠페인 분석을]({{site.baseurl}}/user_guide/analytics/reporting/campaign_analytics/) 사용하여 각 캠페인 및 해당 캠페인 내 배리언트의 상위 결과와 메시지 수준 세부 정보를 실시간으로 업데이트할 수 있습니다. 날짜 범위를 조정하여 시간 경과에 따른 캠페인 성능/성과를 파악하고 메시지를 미리 보고 테스트한 내용을 기억할 수 있습니다.

{% endtab %}

{% tab Canvas Analytics %}
**캔버스 분석**

캔버스 [분석을]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) 사용하여 캔버스에 대한 주요 통계를 통해 메시징 전략의 성능/성과를 확인할 수 있습니다. 라이브 캔버스를 열어 다음과 같은 주요 성능/성과 통계를 확인하세요:

- 캔버스 내에서 전송된 메시지 수
- 고객이 캔버스에 입장한 총 횟수
- 전환한 고객 수
- 캔버스에서 생성된 매출
- 예상 총 오디언스 수

<br>

**배리언트별 성능/성과**

라이브 캔버스에서 [배리언트를 분석하여]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/measuring_and_testing_with_canvas_analytics/#performance-breakdown-by-variant) 모든 전환 이벤트에 대해 자동으로 계산된 전환율을 확인할 수 있습니다. 또한 각 배리언트 및 전환 이벤트에 대한 상승도 및 신뢰도 계산을 비교하기 쉬운 표 형식으로 볼 수 있습니다.

이 보고서를 통해 더 많은 질문에 답할 수 있습니다:

- 통계적으로 유의미한 신뢰도가 있었나요?
- 배리언트 1과 배리언트 2의 성능/성과는 어땠나요?

{% endtab %}

{% tab Report Builder %}
**보고서 빌더**

[보고서 빌더를]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/) 사용하여 여러 캠페인 또는 캔버스의 결과를 단일 보기에서 비교하고 어떤 참여 전략이 주요 측정기준에 가장 큰 영향을 미쳤는지 빠르게 확인할 수 있습니다.

이 페이지를 확인하세요:

- 지난 주 또는 지난 달의 캠페인과 캔버스에 대한 보고서를 작성하고, 중요한 측정기준을 계산하고, 팀원들과 공유하세요.
- 다변량 테스트와 캔버스 모두에 대해 배리언트 간의 성능/성과를 비교하세요.
- 특정 캠페인 또는 캔버스에서 가장 많은 전환 또는 참여를 유도한 메시징 채널을 확인할 수 있습니다.
- 캠페인 그룹 또는 캔버스('뉴스레터' 태그와 관련된 모든 메시지 등)의 일반적인 성능/성과 추세를 추적할 수 있습니다.

이 기능으로 더 많은 질문에 답변할 수 있습니다:

- 환영 이메일의 첫 번째 버전은 두 번째 버전과 비교했을 때 성능/성과가 어땠나요?
- 특정 태그에 대해 지난달 대비 이번 달의 평균 푸시 열람율은 얼마입니까?
- 전환이 가장 많았던 달의 뉴스레터는 무엇인가요?

{% endtab %}
{% endtabs %}

## 리텐션에 가장 큰 영향을 미치는 배리언트는 무엇인가요?

{% tabs local %}
{% tab Retention Reports %}
**리텐션 보고서**

[캠페인]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/) 또는 [캔버스에]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/) 대한 리텐션 보고서를 사용하여 특정 캠페인에서 선택한 이벤트를 수행한 사용자의 리텐션을 측정할 수 있습니다.

이 보고서를 확인하세요:

- 캠페인 수신 후 최대 1개월까지 다양한 이벤트 발생을 분석하여 메시지가 장기적으로 사용자의 재참여를 유도하는 데 얼마나 효과적인지 파악할 수 있습니다.
- [A/B 테스트의]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) 배리언트에서 서로 다른 이벤트 발생을 비교합니다.

이 보고서를 통해 더 많은 질문에 답할 수 있습니다:

- 리텐션에 가장 큰 영향을 미치는 배리언트는 무엇인가요?
- 이 캠페인을 받은 고객은 이후에도 얼마 동안 앱을 계속 사용하나요?
- 이 캠페인은 하루 후 리텐션에 어떤 영향을 미쳤나요? 30일 후?

{% alert note %} SMS 및 API 트리거 캠페인에는 리텐션 리포트를 사용할 수 없습니다. {% endalert %}

{% endtab %}
{% tab Funnel Report %}

[캠페인]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) 또는 [캔버스용]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) 퍼널 보고서를 사용하여 고객이 캠페인을 수신한 후 이동하는 여정을 분석하세요. 각 퍼널 분석에 포함할 네이티브 또는 커스텀 이벤트를 선택한 다음, 선택한 전환 퍼널에 대한 각 배리언트의 성능/성과를 자세히 살펴볼 수 있습니다.

이 보고서를 확인하세요:

- 전환 퍼널에서 사용자가 이탈한 위치를 파악하고 재참여 메시징의 기회를 식별합니다.
- 캠페인 설정 시 원래 전환 이벤트로 포함되지 않은 이벤트의 전환을 확인합니다.
- "이메일을 수신하고 세션을 시작하고 장바구니에 아이템을 추가한 후 구매한 고객은 몇 퍼센트인가요?" 등의 일련의 작업을 사용하여 구매 퍼널을 분석하세요.

이 보고서를 통해 더 많은 질문에 답할 수 있습니다:

- 전환 경로에서 고객이 이탈하는 단계는 어디인가요?
- 마케팅 전략을 개선하려면 어떻게 해야 하나요?

{% endtab %}
{% endtabs%}

## 사용자의 참여도는 어느 정도인가요?

{% tabs local %}
{% tab Report Builder %}

[보고서 빌더를]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/) 사용하여 여러 캠페인 또는 캔버스의 결과를 단일 보기에서 비교하고 어떤 참여 전략이 주요 측정기준에 가장 큰 영향을 미쳤는지 빠르게 확인할 수 있습니다.

이 페이지를 확인하세요:

- 지난 주 또는 지난 달의 캠페인과 캔버스에 대한 보고서를 작성하고, 중요한 측정기준을 계산하고, 팀원들과 공유하세요.
- 특정 캠페인 또는 캔버스에서 가장 많은 전환 또는 참여를 유도한 메시징 채널을 확인할 수 있습니다.
- 캠페인 그룹 또는 캔버스('뉴스레터' 태그와 관련된 모든 메시지 등)의 일반적인 성능/성과 추세를 추적할 수 있습니다.

이 기능으로 더 많은 질문에 답변할 수 있습니다:

- 환영 이메일의 첫 번째 버전은 두 번째 버전과 비교했을 때 성능/성과가 어땠나요?
- 특정 태그에 대해 지난달 대비 이번 달의 평균 푸시 열람율은 얼마입니까?
- 전환이 가장 많았던 달의 뉴스레터는 무엇인가요?

{% endtab %}
{% tab Overview Data %}
**개요 데이터**

[개요]({{site.baseurl}}/user_guide/analytics/dashboard/home_dashboard/) 페이지에서 앱의 성능/성과에 관한 주요 측정기준에 대한 개략적인 요약과 앱 사용자 기반에 대한 인사이트를 얻을 수 있습니다.

이러한 통계는 이 페이지에서 확인하세요:

- 평생 사용자
- 평생 세션
- 월간 활성 사용자(MAU)
- 일일 활성 사용자(DAU)
- 신규 사용자
- 사용자 고착도
- 일일 세션
- MAU당 일일 세션 수

이 대시보드를 통해 더 많은 질문에 답할 수 있습니다:

- 사용자 고착도가 전월 대비 개선되나요?
- iOS 또는 Android 앱의 전반적인 성장세를 볼 수 있나요?
- 이번 달 전체 이메일 볼륨은 어떻게 되나요?

{% endtab %}
{% tab Engagement Reports %}
**참여 보고서**

[참여 보고서를]({{site.baseurl}}/user_guide/analytics/reporting/engagement_reports/) 사용하여 선택한 캠페인 및 캔버스에 대한 참여 통계의 반복 이메일 내보내기를 설정할 수 있습니다. 이 보고서는 대시보드에서 사용할 수 있는 가장 사용자 지정 가능하고 세분화된 보고서입니다.

메시징 채널에 따라 다음과 같은 통계를 내보낼 수 있습니다:

| 채널| 사용 가능한 통계|
| ------| --------------|
| 이메일 | 전송, 열람, 고유 열람, 클릭, 고유 클릭, 클릭하여 열람, 탈퇴, 반송, 전달, 신고된 스팸 |
| 푸시  | 전송, 열기, 영향받은 열기, 바운스, 본문 클릭 |
| 웹 푸시 | 보내기, 열기, 반송, 본문 클릭 |
| 인앱 메시지 | 노출 횟수, 클릭 수, 첫 번째 버튼 클릭 수, 두 번째 버튼 클릭 수 |
| 웹훅  |  전송, 오류 |
| SMS | 전송, 배송업체로 전송, 배송 확인, 배송 실패, 거부 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

이 보고서를 통해 더 많은 질문에 답할 수 있습니다:

- 모든 "윈백" 메시징의 성능/성과는 어떻습니까?
- 내 이메일 캠페인의 총 전달률은 얼마인가요?
- 6월의 모든 Braze 캠페인은 어떻게 진행되었나요? 2021년부터 현재까지?
- 다변량 테스트에서 어떤 추세를 볼 수 있나요?

{% endtab %}
{% endtabs %}

## 세그먼트별로 사용자 행동은 어떻게 다를까요?

{% tabs local %}
{% tab Segment Data %}
**세그먼트 데이터**

세그먼트에 대한 [분석 추적을]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/) 인에이블한 경우 해당 세그먼트를 열어 [세그먼트 데이터를]({{site.baseurl}}/viewing_and_understanding_segment_data/) 확인합니다. 세그먼트 데이터는 해당 사용자의 시간 경과에 따른 세션, 커스텀 이벤트 및 매출을 추적합니다.

이러한 통계는 이 페이지에서 확인하세요:

- 총 개수입니다:
  - 세그먼트의 사용자 수 및 전체 사용자 기반에서 차지하는 비율
  - 이메일 수신에 명시적으로 옵트인한 이메일 수신 가능 사용자
  - 푸시 알림을 명시적으로 옵트인한 푸시 인에이블먼트 사용자
- 이 세그먼트에 속한 사용자의 평균 생애주기 가치(LTV)
- 이 세그먼트를 타겟팅한 참여 툴 목록
- 세그먼트 인사이트

{% endtab %}
{% tab Segment Insights %}
**세그먼트 인사이트**

[세그먼트 인사이트를]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_insights/) 사용하면 세그먼트를 서로 비교하여 다음 측정기준이 수명 주기 길이 및 세션 빈도와 같은 항목에 어떤 영향을 미치는지 파악할 수 있습니다:

- 인구 통계
- 플랫폼
- 옵트인 상태
- 카테고리 기본 설정
- 캠페인 영수증

이 보고서를 통해 더 많은 질문에 답할 수 있습니다:

- 온보딩 캔버스를 받은 사용자와 대조군의 세션 빈도는 어느 정도였나요?
- 푸시에 옵트인한 사용자와 이메일에 옵트인한 사용자, 그리고 두 가지 모두에 옵트인한 사용자의 라이프사이클 길이에는 어떤 차이가 있나요?

{% endtab %}
{% tab Custom Events %}
**커스텀 이벤트**

[커스텀]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-analytics) 이벤트 페이지를 사용하여 커스텀 이벤트의 발생 빈도와 각 사용자가 마지막으로 수행한 시간을 모니터링하여 세그먼트를 세분화할 수 있습니다.

이 페이지를 확인하세요:

- 커스텀 이벤트 빈도 모니터링
- 세그먼트별 커스텀 이벤트 모니터링
- 캠페인이 커스텀 이벤트 활동에 미치는 영향 분석하기
- [KPI 공식]({{site.baseurl}}/user_guide/data/creating_a_formula/) 생성 및 모니터링
- 커스텀 이벤트 추적 문제 해결하기

{% endtab %}
{% endtabs %}

## 내 캠페인이 투자수익률을 제공했나요?

{% tabs local %}
{% tab Revenue Data %}
**매출 데이터**

[수익]({{site.baseurl}}/user_guide/data/export_braze_data/exporting_revenue_data/) 페이지를 사용하여 특정 기간 동안의 매출 및 구매 또는 앱의 총 매출 또는 구매를 추적할 수 있습니다.

이러한 통계는 이 페이지에서 확인하세요:

- KPI 공식 결과
- 제품 구매 횟수
- 다양한 세그먼트별 매출
- 다양한 제품에 대한 매출
- 시간당 매출
- 세그먼트별 시간당 매출
- 사용자당 매출

{% endtab %}
{% tab Global Control Group Report %}
**글로벌 컨트롤 그룹 보고서**

[글로벌 컨트롤 그룹을]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/) 설정한 후에는 [글로벌 컨트롤 보고서를]({{site.baseurl}}/user_guide/analytics/reporting/global_control_group_reporting/) 사용하여 전체적으로 Braze 마케팅의 영향을 평가하세요. 이 보고서를 통해 메시징을 수신한 사용자의 행동과 그렇지 않은 사용자의 행동을 비교하여 캠페인과 캔버스가 비즈니스 목표에 어떻게 기여하고 있는지 더 잘 이해할 수 있습니다.

이 페이지를 확인하세요:

- 캠페인과 캔버스가 세션과 커스텀 이벤트에 미치는 영향과 점진적인 상승 효과를 쉽게 측정할 수 있습니다.
- 대조군 구성원을 자동으로 무작위로 지정하여 메시지 수신에서 제외합니다.
- 추가 분석을 위해 대조군 구성원을 내보냅니다.

보고서로 답변할 수 있는 질문이 더 있습니다:

- Braze 메시지 전송이 고객 행동에 미치는 전반적인 영향은 어떤가요?
- (리뉴얼 또는 이해관계자 논의를 위한) 플랫폼으로서 Braze의 ROI는 무엇인가요?

{% endtab %}
{% endtabs %}

## 다음에 어떤 캠페인을 실행해야 하나요?

{% tabs local %}
{% tab Funnel Report %}

[캠페인]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) 또는 [캔버스용]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) 퍼널 보고서를 사용하여 고객이 캠페인을 수신한 후 이동하는 여정을 분석하세요. 각 퍼널 분석에 포함할 네이티브 또는 커스텀 이벤트를 선택한 다음, 선택한 전환 퍼널에 대한 각 배리언트의 성능/성과를 자세히 살펴볼 수 있습니다.

이 보고서를 확인하세요:

- 전환 퍼널에서 사용자가 이탈한 위치를 파악하고 재참여 메시징의 기회를 식별합니다.
- 캠페인 설정 시 원래 전환 이벤트로 포함되지 않은 이벤트의 전환을 확인합니다.
- "이메일을 수신하고 세션을 시작하고 장바구니에 아이템을 추가한 후 구매한 고객은 몇 퍼센트인가요?" 등의 일련의 작업을 사용하여 구매 퍼널을 분석하세요.

이 보고서를 통해 더 많은 질문에 답할 수 있습니다:

- 전환 경로에서 고객이 이탈하는 단계는 어디인가요?
- 마케팅 전략을 개선하려면 어떻게 해야 하나요?

{% endtab %}
{% tab Predictive Churn %}
**예측 이탈률**

[예측 이탈은]({{site.baseurl}}/user_guide/brazeai/predictive_churn/) [Braze Predictive Suite의]({{site.baseurl}}/user_guide/brazeai/) 첫 번째 모델입니다. 예측 이탈을 사용하여 예측을 정의하고 생성하여 향후 고객 이탈을 최소화하기 위한 사전 예방적 접근 방식을 제공합니다.

비즈니스마다 고객이탈과 리텐션의 정의가 다르기 때문에, 예측 이탈에 정의를 입력하기만 하면 나머지는 Braze가 알아서 처리합니다. 또한 캠페인이나 캔버스를 만들어 예측에 따라 행동하거나 추가 분석을 위한 세그먼트를 구축할 수도 있습니다.

이 기능으로 더 많은 질문에 답변할 수 있습니다:

- 내 이상적인 사용자 중 얼마나 많은 사용자가 이탈할 위험이 있나요?
- 위험에 처한 사용자들은 어떤 행동이나 속성을 공통적으로 가지고 있나요?

{% endtab %}
{% tab Report Builder %}
**보고서 빌더**

[보고서 빌더를]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/) 사용하여 여러 캠페인 또는 캔버스의 결과를 단일 보기에서 비교하고 어떤 참여 전략이 주요 측정기준에 가장 큰 영향을 미쳤는지 빠르게 확인할 수 있습니다.

이 페이지를 확인하세요:

- 지난 주 또는 지난 달의 캠페인과 캔버스에 대한 보고서를 작성하고, 중요한 측정기준을 계산하고, 팀원들과 공유하세요.
- 다변량 테스트와 캔버스 모두에 대해 배리언트 간의 성능/성과를 비교하세요.
- 특정 캠페인 또는 캔버스에서 가장 많은 전환 또는 참여를 유도한 메시징 채널을 확인할 수 있습니다.
- 캠페인 그룹 또는 캔버스('뉴스레터' 태그와 관련된 모든 메시지 등)의 일반적인 성능/성과 추세를 추적할 수 있습니다.

이 기능으로 더 많은 질문에 답변할 수 있습니다:

- 환영 이메일의 첫 번째 버전은 두 번째 버전과 비교했을 때 성능/성과가 어땠나요?
- 특정 태그에 대해 지난달 대비 이번 달의 평균 푸시 열람율은 얼마입니까?
- 전환이 가장 많았던 달의 뉴스레터는 무엇인가요?

{% endtab %}
{% endtabs %}
