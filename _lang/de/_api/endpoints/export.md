---
nav_title: Exportieren
article_title: Endpunkte exportieren
search_tag: Endpoint
page_order: 2

layout: dev_guide

#Required
description: "Auf dieser Landing Page werden die Export-Endpunkte von Braze erklärt und aufgelistet."
page_type: landing

guide_top_header: "Endpunkte exportieren"
guide_top_text: "Mit dieser Sammlung von Endpunkten können Sie auf verschiedene Ebenen von Details zu Ihren KPIs, News Feed-Karten, App-Sitzungen, Benutzern, Segmenten, Kampagnen und Canvases zugreifen und diese exportieren. <br> <br> Vergewissern Sie sich, dass Sie Ihre <a href='/docs/user_guide/administrative/access_braze/braze_instances/' target='_blank'>Braze-Instanz</a>, den <a href='/docs/api/api_key/' target='_blank'>API-Schlüssel</a> und die <a href='/docs/api/identifier_types/' target='_blank'>API-Kennung</a> kennen, wenn Sie Ihre Parameter und Anfragekörper erstellen."

guide_featured_title: "Endpunkte der Kampagne exportieren"
guide_featured_list:
  - name: "GET: Kampagnen-Analytik"
    link: /docs/api/endpoints/export/campaigns/get_campaign_analytics/
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: "GET: Details zur Kampagne"
    link: /docs/api/endpoints/export/campaigns/get_campaign_details/
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: "GET: Kampagnen Liste"
    link: /docs/api/endpoints/export/campaigns/get_campaigns/
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: "GET: Analytik senden"
    link: /docs/api/endpoints/export/campaigns/get_send_analytics/
    image: /assets/img/braze_icons/bar-chart-01.svg

guide_menu_title: "Export Canvas endpoints"
guide_menu_list:
  - name: "GET: Canvas Datenreihen Analytik"
    link: /docs/api/endpoints/export/canvas/get_canvas_analytics/
    image: /assets/img/braze_icons/dataflow-03.svg
  - name: "GET: Canvas Analytics Zusammenfassung"
    link: /docs/api/endpoints/export/canvas/get_canvas_analytics_summary/
    image: /assets/img/braze_icons/dataflow-03.svg
  - name: "GET: Segeltuch Details"
    link: /docs/api/endpoints/export/canvas/get_canvas_details/
    image: /assets/img/braze_icons/dataflow-03.svg
  - name: "GET: Leinwand Liste"
    link: /docs/api/endpoints/export/canvas/get_canvases/
    image: /assets/img/braze_icons/dataflow-03.svg

guide_menu_title2: "Export custom events endpoints"
guide_menu_list2:
  - name: "GET: Benutzerdefinierte Ereignisse"
    link: /docs/api/endpoints/export/custom_events/get_custom_events_data/
    image: /assets/img/braze_icons/line-chart-up-01.svg
  - name: "GET: Benutzerdefinierte Ereignisliste"
    link: /docs/api/endpoints/export/custom_events/get_custom_events/
    image: /assets/img/braze_icons/line-chart-up-01.svg
  - name: "GET: Benutzerdefinierte Ereignisanalyse"
    link: /docs/api/endpoints/export/custom_events/get_custom_events_analytics/
    image: /assets/img/braze_icons/line-chart-up-01.svg

guide_menu_title3: "Export KPI endpoints"
guide_menu_list3:
  - name: "GET: KPIs für täglich neue Benutzer nach Datum"
    link: /docs/api/endpoints/export/kpi/get_kpi_daily_new_users_date/
    image: /assets/img/braze_icons/target-04.svg
  - name: "GET: KPIs für täglich aktive Benutzer nach Datum"
    link: /docs/api/endpoints/export/kpi/get_kpi_dau_date/
    image: /assets/img/braze_icons/target-04.svg
  - name: "GET: KPIs für monatlich aktive Benutzer in den letzten 30 Tagen"
    link: /docs/api/endpoints/export/kpi/get_kpi_mau_30_days/
    image: /assets/img/braze_icons/target-04.svg
  - name: "GET: KPIs für Deinstallationen nach Datum"
    link: /docs/api/endpoints/export/kpi/get_kpi_uninstalls_date/
    image: /assets/img/braze_icons/target-04.svg

guide_menu_title4: "Export News Feed endpoints"
guide_menu_list4:
  - name: "GET: Engagement-Statistiken für News Feed-Karten"
    link: /docs/api/endpoints/export/news_feed/get_news_feed_card_analytics/
    image: /assets/img/braze_icons/download-cloud-01.svg
  - name: "GET: Details zur News Feed Karte"
    link: /docs/api/endpoints/export/news_feed/get_news_feed_card_details/
    image: /assets/img/braze_icons/download-cloud-01.svg
  - name: "GET: News Feed Kartenliste"
    link: /docs/api/endpoints/export/news_feed/get_news_feed_cards/
    image: /assets/img/braze_icons/download-cloud-01.svg

guide_menu_title5: "Export purchase endpoints"
guide_menu_list5:
  - name: "GET: Liste der Produkt-IDs"
    link: /docs/api/endpoints/export/purchases/get_list_product_id/
    image: /assets/img/braze_icons/list.svg
  - name: "GET: Anzahl der Käufe"
    link: /docs/api/endpoints/export/purchases/get_number_of_purchases/
    image: /assets/img/braze_icons/list.svg
  - name: "GET: Einkommensdaten nach Zeit"
    link: /docs/api/endpoints/export/purchases/get_revenue_series/
    image: /assets/img/braze_icons/list.svg

guide_menu_title6: "Export segment endpoints"
guide_menu_list6:
  - name: "GET: Segment-Liste"
    link: /docs/api/endpoints/export/segments/get_segment/
    image: /assets/img/braze_icons/users-01.svg
  - name: "GET: Segment Analytik"
    link: /docs/api/endpoints/export/segments/get_segment_analytics/
    image: /assets/img/braze_icons/users-01.svg
  - name: "GET: Segment Details"
    link: /docs/api/endpoints/export/segments/get_segment_details/
    image: /assets/img/braze_icons/users-01.svg

guide_menu_title7: "Export sessions endpoint"
guide_menu_list7:
  - name: "GET: App-Sitzungen Zeitreihendaten"
    link: /docs/api/endpoints/export/sessions/get_sessions_analytics/
    image: /assets/img/braze_icons/tablet-01.svg

guide_menu_title8: "Export user data endpoints"
guide_menu_list8:
  - name: "POST: Benutzerdaten nach Kennung"
    link: /docs/api/endpoints/export/user_data/post_users_identifier/
    image: /assets/img/braze_icons/users-01.svg
  - name: "POST: Benutzerdaten nach Segment"
    link: /docs/api/endpoints/export/user_data/post_users_segment/
    image: /assets/img/braze_icons/users-01.svg
  - name: "POST: Benutzerdaten nach Global Control Group"
    link: /docs/api/endpoints/export/user_data/post_users_global_control_group/
    image: /assets/img/braze_icons/users-01.svg

guide_menu_title9: "Export custom attributes endpoints"
guide_menu_list9:
  - name: "GET: Benutzerdefinierte Attribute"
    link: /docs/api/endpoints/export/custom_attributes/get_custom_attributes/
    image: /assets/img/braze_icons/line-chart-up-01.svg
---
