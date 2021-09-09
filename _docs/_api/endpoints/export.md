---
nav_title: Export
article_title: Export Endpoints
search_tag: Endpoint
page_order: 1

layout: dev_guide

#Required
description: "This landing page explains and lists the Braze Export Endpoints."
page_type: landing

guide_top_header: "Export Endpoints"
guide_top_text: "With this collection of endpoints, you will be able to access and export various levels of details on your KPIs, News Feed Cards, App Sessions, users, segments, Campaigns, and Canvases. <br> <br> Be sure to consult our <a href='/docs/user_guide/administrative/access_braze/braze_instances/' target='_blank'>Instance</a>, <a href='/docs/api/api_key/' target='_blank'>API Key</a>, and <a href='/docs/api/identifier_types/' target='_blank'>identifier</a> reference documentation when building out your parameters and request bodies."

guide_featured_title: "Campaign, Canvas, News Feed, and SMS Export Endpoints"
guide_featured_list:
  - name: "GET: Campaign Analytics"
    link: /docs/api/endpoints/export/campaigns/get_campaign_analytics/
    fa_icon: far fa-chart-bar
  - name: "GET: Campaign Details"
    link: /docs/api/endpoints/export/campaigns/get_campaign_details/
    fa_icon: far fa-chart-bar
  - name: "GET: Campaigns List"
    link: /docs/api/endpoints/export/campaigns/get_campaigns/
    fa_icon: far fa-chart-bar
  - name: "GET: Send Analytics"
    link: /docs/api/endpoints/export/campaigns/get_send_analytics/
    fa_icon: far fa-chart-bar
  - name: "GET: Canvas Data Series Analytics"
    link: /docs/api/endpoints/export/canvas/get_canvas_analytics/
    fa_icon: fas fa-project-diagram
  - name: "GET: Canvas Analytics Summary"
    link: /docs/api/endpoints/export/canvas/get_canvas_analytics_summary/
    fa_icon: fas fa-project-diagram
  - name: "GET: Canvas Details"
    link: /docs/api/endpoints/export/canvas/get_canvas_details/
    fa_icon: fas fa-project-diagram
  - name: "GET: Canvas List"
    link: /docs/api/endpoints/export/canvas/get_canvases/
    fa_icon: fas fa-project-diagram
  - name: "GET: News Feed Card Engagement Stats"
    link: /docs/api/endpoints/export/news_feed/get_news_feed_card_analytics/
    fa_icon: fas fa-stream
  - name: "GET: News Feed Card Details"
    link: /docs/api/endpoints/export/news_feed/get_news_feed_card_details/
    fa_icon: fas fa-stream
  - name: "GET: News Feed Card List"
    link: /docs/api/endpoints/export/news_feed/get_news_feed_cards/
    fa_icon: fas fa-stream
  - name: "GET: Query Invalid Phone Numbers"
    link: /docs/api/endpoints/export/sms/get_query_invalid_numbers/
    fa_icon: fas fa-phone

guide_menu_title: "Custom Events, KPIs, Segments, Sessions, and User Data Export Endpoints"
guide_menu_list:
  - name: "GET: Custom Events List"
    link: /docs/api/endpoints/export/custom_events/get_custom_events/
    fa_icon: fas fa-chart-line
  - name: "GET: Custom Event Analytics"
    link: /docs/api/endpoints/export/custom_events/get_custom_events_analytics/
    fa_icon: fas fa-chart-line
  - name: "GET: KPIs for Daily New Users by Date"
    link: /docs/api/endpoints/export/kpi/get_kpi_daily_new_users_date/
    fa_icon: fas fa-bullseye
  - name: "GET: KPIs for Daily Active Users by Date"
    link: /docs/api/endpoints/export/kpi/get_kpi_dau_date/
    fa_icon: fas fa-bullseye
  - name: "GET: KPIs for Monthly Active Users Over Last 30 Days"
    link: /docs/api/endpoints/export/kpi/get_kpi_mau_30_days/
    fa_icon: fas fa-bullseye
  - name: "GET: KPIs for Uninstalls by Date"
    link: /docs/api/endpoints/export/kpi/get_kpi_uninstalls_date/
    fa_icon: fas fa-bullseye
  - name: "GET: Segment List"
    link: /docs/api/endpoints/export/segments/get_segment/
    fa_icon: fas fa-users
  - name: "GET: Segment Analytics"
    link: /docs/api/endpoints/export/segments/get_segment_analytics/
    fa_icon: fas fa-users
  - name: "GET: Segment Details"
    link: /docs/api/endpoints/export/segments/get_segment_details/
    fa_icon: fas fa-users
  - name: "GET: App Sessions Time-Series Data"
    link: /docs/api/endpoints/export/sessions/get_sessions_analytics/
    fa_icon: fas fa-tablet-alt
  - name: "POST: User Data by Identifier"
    link: /docs/api/endpoints/export/user_data/post_users_identifier/
    fa_icon: fas fa-user
  - name: "POST: User Data by Segment"
    link: /docs/api/endpoints/export/user_data/post_users_segment/
    fa_icon: fas fa-user
  - name: "POST: User Data by Global Control Group"
    link: /docs/api/endpoints/export/user_data/post_users_global_control_group/
    fa_icon: fas fa-user

---
