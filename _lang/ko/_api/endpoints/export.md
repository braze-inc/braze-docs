---
nav_title: 내보내기
article_title: 엔드포인트 내보내기
search_tag: Endpoint
page_order: 2

layout: dev_guide

#Required
description: "이 랜딩 페이지에서는 Braze 내보내기 엔드포인트를 설명하고 나열합니다."
page_type: landing

guide_top_header: "엔드포인트 내보내기"
guide_top_text: "이 엔드포인트 모음을 사용하면 KPI, 앱 세션, 사용자, 세그먼트, 캠페인 및 캔버스에 대한 다양한 수준의 세부 정보에 액세스하고 내보낼 수 있습니다. <br> <br> 매개변수 및 요청 본문을 작성할 때 <a href='/docs/user_guide/administrative/access_braze/braze_instances/' target='_blank'>Braze 인스턴스</a>, <a href='/docs/api/api_key/' target='_blank'>API 키</a>, <a href='/docs/api/identifier_types/' target='_blank'>API 식별자를</a> 알고 있어야 합니다."

guide_featured_title: "캠페인 엔드포인트 내보내기"
guide_featured_list:
  - name: "GET: 캠페인 분석 "
    link: /docs/api/endpoints/export/campaigns/get_campaign_analytics/
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: "GET: 캠페인 세부 정보"
    link: /docs/api/endpoints/export/campaigns/get_campaign_details/
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: "GET: 캠페인 목록"
    link: /docs/api/endpoints/export/campaigns/get_campaigns/
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: "GET: 애널리틱스 보내기"
    link: /docs/api/endpoints/export/campaigns/get_send_analytics/
    image: /assets/img/braze_icons/bar-chart-01.svg

guide_menu_title: "Export Canvas endpoints"
guide_menu_list:
  - name: "GET: 캔버스 데이터 시리즈 분석"
    link: /docs/api/endpoints/export/canvas/get_canvas_analytics/
    image: /assets/img/braze_icons/dataflow-03.svg
  - name: "GET: 캔버스 애널리틱스 요약"
    link: /docs/api/endpoints/export/canvas/get_canvas_analytics_summary/
    image: /assets/img/braze_icons/dataflow-03.svg
  - name: "GET: 캔버스 세부 정보"
    link: /docs/api/endpoints/export/canvas/get_canvas_details/
    image: /assets/img/braze_icons/dataflow-03.svg
  - name: "GET: 캔버스 목록"
    link: /docs/api/endpoints/export/canvas/get_canvases/
    image: /assets/img/braze_icons/dataflow-03.svg

guide_menu_title2: "Export custom events endpoints"
guide_menu_list2:
  - name: "GET: 사용자 지정 이벤트"
    link: /docs/api/endpoints/export/custom_events/get_custom_events_data/
    image: /assets/img/braze_icons/line-chart-up-01.svg
  - name: "GET: 사용자 지정 이벤트 목록"
    link: /docs/api/endpoints/export/custom_events/get_custom_events/
    image: /assets/img/braze_icons/line-chart-up-01.svg
  - name: "GET: 사용자 지정 이벤트 분석"
    link: /docs/api/endpoints/export/custom_events/get_custom_events_analytics/
    image: /assets/img/braze_icons/line-chart-up-01.svg

guide_menu_title3: "Export KPI endpoints"
guide_menu_list3:
  - name: "GET: 날짜별 일일 신규 사용자 KPI"
    link: /docs/api/endpoints/export/kpi/get_kpi_daily_new_users_date/
    image: /assets/img/braze_icons/target-04.svg
  - name: "GET: 날짜별 일일 활성 사용자 KPI"
    link: /docs/api/endpoints/export/kpi/get_kpi_dau_date/
    image: /assets/img/braze_icons/target-04.svg
  - name: "GET: 지난 30일간 월간 활성 사용자에 대한 KPI"
    link: /docs/api/endpoints/export/kpi/get_kpi_mau_30_days/
    image: /assets/img/braze_icons/target-04.svg
  - name: "GET: 날짜별 제거에 대한 KPI"
    link: /docs/api/endpoints/export/kpi/get_kpi_uninstalls_date/
    image: /assets/img/braze_icons/target-04.svg

guide_menu_title5: "Export purchase endpoints"
guide_menu_list5:
  - name: "GET: 제품 ID 목록"
    link: /docs/api/endpoints/export/purchases/get_list_product_id/
    image: /assets/img/braze_icons/list.svg
  - name: "GET: 구매 횟수"
    link: /docs/api/endpoints/export/purchases/get_number_of_purchases/
    image: /assets/img/braze_icons/list.svg
  - name: "GET: 시간별 수익 데이터"
    link: /docs/api/endpoints/export/purchases/get_revenue_series/
    image: /assets/img/braze_icons/list.svg

guide_menu_title6: "Export segment endpoints"
guide_menu_list6:
  - name: "GET: 세그먼트 목록"
    link: /docs/api/endpoints/export/segments/get_segment/
    image: /assets/img/braze_icons/users-01.svg
  - name: "GET: 세그먼트 분석"
    link: /docs/api/endpoints/export/segments/get_segment_analytics/
    image: /assets/img/braze_icons/users-01.svg
  - name: "GET: 세그먼트 세부 정보"
    link: /docs/api/endpoints/export/segments/get_segment_details/
    image: /assets/img/braze_icons/users-01.svg

guide_menu_title7: "Export sessions endpoint"
guide_menu_list7:
  - name: "GET: 앱 세션 시계열 데이터"
    link: /docs/api/endpoints/export/sessions/get_sessions_analytics/
    image: /assets/img/braze_icons/tablet-01.svg

guide_menu_title8: "Export user data endpoints"
guide_menu_list8:
  - name: "POST: 식별자별 사용자 데이터"
    link: /docs/api/endpoints/export/user_data/post_users_identifier/
    image: /assets/img/braze_icons/users-01.svg
  - name: "POST: 세그먼트별 사용자 데이터"
    link: /docs/api/endpoints/export/user_data/post_users_segment/
    image: /assets/img/braze_icons/users-01.svg
  - name: "POST: 글로벌 제어 그룹별 사용자 데이터"
    link: /docs/api/endpoints/export/user_data/post_users_global_control_group/
    image: /assets/img/braze_icons/users-01.svg

guide_menu_title9: "Export custom attributes endpoints"
guide_menu_list9:
  - name: "GET: 커스텀 속성"
    link: /docs/api/endpoints/export/custom_attributes/get_custom_attributes/
    image: /assets/img/braze_icons/line-chart-up-01.svg
---
