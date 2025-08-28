---
nav_title: エクスポート
article_title: エクスポートエンドポイント
search_tag: Endpoint
page_order: 2

layout: dev_guide

#Required
description: "このランディングページでは、Brazeエクスポートエンドポイントについて説明し、一覧表示しています。"
page_type: landing

guide_top_header: "エクスポートエンドポイント"
guide_top_text: "このエンドポイントのコレクションで、KPI、アプリセッション、ユーザー、セグメンテーション、キャンペーン、キャンバスに関する様々なレベルの詳細にアクセスし、エクスポートすることができます。<br> <br> パラメータとリクエストボディを作成する際には、<a href='/docs/user_guide/administrative/access_braze/braze_instances/' target='_blank'>Brazeインスタンス</a>、<a href='/docs/api/api_key/' target='_blank'>API キー</a>、および<a href='/docs/api/identifier_types/' target='_blank'>API 識別子</a>を確認してください。"

guide_featured_title: "エクスポートキャンペーンエンドポイント"
guide_featured_list:
  - name: "取得:キャンペーン分析"
    link: /docs/api/endpoints/export/campaigns/get_campaign_analytics/
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: "取得:キャンペーンの詳細"
    link: /docs/api/endpoints/export/campaigns/get_campaign_details/
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: "取得:キャンペーン一覧"
    link: /docs/api/endpoints/export/campaigns/get_campaigns/
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: "取得:分析を送信"
    link: /docs/api/endpoints/export/campaigns/get_send_analytics/
    image: /assets/img/braze_icons/bar-chart-01.svg

guide_menu_title: "Export Canvas endpoints"
guide_menu_list:
  - name: "取得:キャンバス データ シリーズ 分析"
    link: /docs/api/endpoints/export/canvas/get_canvas_analytics/
    image: /assets/img/braze_icons/dataflow-03.svg
  - name: "取得:キャンバス分析の要約"
    link: /docs/api/endpoints/export/canvas/get_canvas_analytics_summary/
    image: /assets/img/braze_icons/dataflow-03.svg
  - name: "取得:キャンバスの詳細"
    link: /docs/api/endpoints/export/canvas/get_canvas_details/
    image: /assets/img/braze_icons/dataflow-03.svg
  - name: "取得:キャンバスリスト"
    link: /docs/api/endpoints/export/canvas/get_canvases/
    image: /assets/img/braze_icons/dataflow-03.svg

guide_menu_title2: "Export custom events endpoints"
guide_menu_list2:
  - name: "取得:カスタムイベント"
    link: /docs/api/endpoints/export/custom_events/get_custom_events_data/
    image: /assets/img/braze_icons/line-chart-up-01.svg
  - name: "取得:カスタムイベントリスト"
    link: /docs/api/endpoints/export/custom_events/get_custom_events/
    image: /assets/img/braze_icons/line-chart-up-01.svg
  - name: "取得:カスタムイベント分析"
    link: /docs/api/endpoints/export/custom_events/get_custom_events_analytics/
    image: /assets/img/braze_icons/line-chart-up-01.svg

guide_menu_title3: "Export KPI endpoints"
guide_menu_list3:
  - name: "取得:日別の新規ユーザーの日次 KPI"
    link: /docs/api/endpoints/export/kpi/get_kpi_daily_new_users_date/
    image: /assets/img/braze_icons/target-04.svg
  - name: "取得:日付ごとのデイリーアクティブユーザーのKPI"
    link: /docs/api/endpoints/export/kpi/get_kpi_dau_date/
    image: /assets/img/braze_icons/target-04.svg
  - name: "取得:過去30日間の月間アクティブユーザーのKPI"
    link: /docs/api/endpoints/export/kpi/get_kpi_mau_30_days/
    image: /assets/img/braze_icons/target-04.svg
  - name: "取得:日付ごとのアンインストールのKPI"
    link: /docs/api/endpoints/export/kpi/get_kpi_uninstalls_date/
    image: /assets/img/braze_icons/target-04.svg

guide_menu_title5: "Export purchase endpoints"
guide_menu_list5:
  - name: "取得:製品IDリスト"
    link: /docs/api/endpoints/export/purchases/get_list_product_id/
    image: /assets/img/braze_icons/list.svg
  - name: "取得:購入数"
    link: /docs/api/endpoints/export/purchases/get_number_of_purchases/
    image: /assets/img/braze_icons/list.svg
  - name: "取得:時間別収益データ"
    link: /docs/api/endpoints/export/purchases/get_revenue_series/
    image: /assets/img/braze_icons/list.svg

guide_menu_title6: "Export segment endpoints"
guide_menu_list6:
  - name: "取得:セグメントリスト"
    link: /docs/api/endpoints/export/segments/get_segment/
    image: /assets/img/braze_icons/users-01.svg
  - name: "取得:セグメント分析"
    link: /docs/api/endpoints/export/segments/get_segment_analytics/
    image: /assets/img/braze_icons/users-01.svg
  - name: "取得:Segment 詳細"
    link: /docs/api/endpoints/export/segments/get_segment_details/
    image: /assets/img/braze_icons/users-01.svg

guide_menu_title7: "Export sessions endpoint"
guide_menu_list7:
  - name: "取得:アプリセッションの時系列データ"
    link: /docs/api/endpoints/export/sessions/get_sessions_analytics/
    image: /assets/img/braze_icons/tablet-01.svg

guide_menu_title8: "Export user data endpoints"
guide_menu_list8:
  - name: "POST:識別子によるユーザーデータ"
    link: /docs/api/endpoints/export/user_data/post_users_identifier/
    image: /assets/img/braze_icons/users-01.svg
  - name: "POST:Segmentによるユーザーデータ"
    link: /docs/api/endpoints/export/user_data/post_users_segment/
    image: /assets/img/braze_icons/users-01.svg
  - name: "POST:グローバルコントロールグループによるユーザーデータ"
    link: /docs/api/endpoints/export/user_data/post_users_global_control_group/
    image: /assets/img/braze_icons/users-01.svg

guide_menu_title9: "Export custom attributes endpoints"
guide_menu_list9:
  - name: "取得:カスタム属性"
    link: /docs/api/endpoints/export/custom_attributes/get_custom_attributes/
    image: /assets/img/braze_icons/line-chart-up-01.svg
---
