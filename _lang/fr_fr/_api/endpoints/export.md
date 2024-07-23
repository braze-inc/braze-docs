---
nav_title: Exporter
article_title: Endpoints d’exportation
search_tag: Endpoint
page_order: 2

layout: dev_guide

#Required
description: "Cette page d’accueil explique et répertorie les endpoints Braze d’exportation."
page_type: landing

guide_top_header: "Endpoints d’exportation"
guide_top_text: "Grâce à cet ensemble d’endpoints, vous pouvez accéder à différents niveaux de détails et les exporter sur vos indicateurs clés de performance, vos cartes de fil d’actualité, vos sessions d’application, vos utilisateurs, vos segments, vos campagnes et vos canvas. <br> <br> Assurez-vous de connaître votre <a href='/docs/user_guide/administrative/access_braze/braze_instances/' target='_blank'>instance Braze</a>, votre <a href='/docs/api/api_key/' target='_blank'>clé API</a> et votre <a href='/docs/api/identifier_types/' target='_blank'>identifiant API</a> lors de la création de vos paramètres et corps de requête."

guide_featured_title: "Exporter les endpoints de campagne"
guide_featured_list:
  - name: "GET: Campaign Analytics"
    link: /docs/api/endpoints/export/campaigns/get_campaign_analytics/
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: "GET: Campaign Details"
    link: /docs/api/endpoints/export/campaigns/get_campaign_details/
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: "GET: Campaigns List"
    link: /docs/api/endpoints/export/campaigns/get_campaigns/
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: "GET: Send Analytics"
    link: /docs/api/endpoints/export/campaigns/get_send_analytics/
    image: /assets/img/braze_icons/bar-chart-01.svg

guide_menu_title: "Export Canvas endpoints"
guide_menu_list:
  - name: "GET: Canvas Data Series Analytics"
    link: /docs/api/endpoints/export/canvas/get_canvas_analytics/
    image: /assets/img/braze_icons/dataflow-03.svg
  - name: "GET: Canvas Analytics Summary"
    link: /docs/api/endpoints/export/canvas/get_canvas_analytics_summary/
    image: /assets/img/braze_icons/dataflow-03.svg
  - name: "GET: Canvas Details"
    link: /docs/api/endpoints/export/canvas/get_canvas_details/
    image: /assets/img/braze_icons/dataflow-03.svg
  - name: "GET: Canvas List"
    link: /docs/api/endpoints/export/canvas/get_canvases/
    image: /assets/img/braze_icons/dataflow-03.svg

guide_menu_title2: "Export custom events endpoints"
guide_menu_list2:
  - name: "GET: Custom Events List"
    link: /docs/api/endpoints/export/custom_events/get_custom_events/
    image: /assets/img/braze_icons/line-chart-up-01.svg
  - name: "GET: Custom Event Analytics"
    link: /docs/api/endpoints/export/custom_events/get_custom_events_analytics/
    image: /assets/img/braze_icons/line-chart-up-01.svg

guide_menu_title3: "Export KPI endpoints"
guide_menu_list3:
  - name: "GET: KPIs for Daily New Users by Date"
    link: /docs/api/endpoints/export/kpi/get_kpi_daily_new_users_date/
    image: /assets/img/braze_icons/target-04.svg
  - name: "GET: KPIs for Daily Active Users by Date"
    link: /docs/api/endpoints/export/kpi/get_kpi_dau_date/
    image: /assets/img/braze_icons/target-04.svg
  - name: "GET: KPIs for Monthly Active Users Over Last 30 Days"
    link: /docs/api/endpoints/export/kpi/get_kpi_mau_30_days/
    image: /assets/img/braze_icons/target-04.svg
  - name: "GET: KPIs for Uninstalls by Date"
    link: /docs/api/endpoints/export/kpi/get_kpi_uninstalls_date/
    image: /assets/img/braze_icons/target-04.svg

guide_menu_title4: "Export News Feed endpoints"
guide_menu_list4:
  - name: "GET: News Feed Card Engagement Stats"
    link: /docs/api/endpoints/export/news_feed/get_news_feed_card_analytics/
    image: /assets/img/braze_icons/download-cloud-01.svg
  - name: "GET: News Feed Card Details"
    link: /docs/api/endpoints/export/news_feed/get_news_feed_card_details/
    image: /assets/img/braze_icons/download-cloud-01.svg
  - name: "GET: News Feed Card List"
    link: /docs/api/endpoints/export/news_feed/get_news_feed_cards/
    image: /assets/img/braze_icons/download-cloud-01.svg

guide_menu_title5: "Export purchase endpoints"
guide_menu_list5:
  - name: "GET: Product IDs List"
    link: /docs/api/endpoints/export/purchases/get_list_product_id/
    image: /assets/img/braze_icons/list.svg
  - name: "GET: Number of Purchases"
    link: /docs/api/endpoints/export/purchases/get_number_of_purchases/
    image: /assets/img/braze_icons/list.svg
  - name: "GET: Revenue Data by Time"
    link: /docs/api/endpoints/export/purchases/get_revenue_series/
    image: /assets/img/braze_icons/list.svg

guide_menu_title6: "Export segment endpoints"
guide_menu_list6:
  - name: "GET: Segment List"
    link: /docs/api/endpoints/export/segments/get_segment/
    image: /assets/img/braze_icons/users-01.svg
  - name: "GET: Segment Analytics"
    link: /docs/api/endpoints/export/segments/get_segment_analytics/
    image: /assets/img/braze_icons/users-01.svg
  - name: "GET: Segment Details"
    link: /docs/api/endpoints/export/segments/get_segment_details/
    image: /assets/img/braze_icons/users-01.svg

guide_menu_title7: "Export sessions endpoint"
guide_menu_list7:
  - name: "GET: App Sessions Time-Series Data"
    link: /docs/api/endpoints/export/sessions/get_sessions_analytics/
    image: /assets/img/braze_icons/tablet-01.svg

guide_menu_title8: "Export user data endpoints"
guide_menu_list8:
  - name: "POST: User Data by Identifier"
    link: /docs/api/endpoints/export/user_data/post_users_identifier/
    image: /assets/img/braze_icons/users-01.svg
  - name: "POST: User Data by Segment"
    link: /docs/api/endpoints/export/user_data/post_users_segment/
    image: /assets/img/braze_icons/users-01.svg
  - name: "POST: User Data by Global Control Group"
    link: /docs/api/endpoints/export/user_data/post_users_global_control_group/
    image: /assets/img/braze_icons/users-01.svg
---
