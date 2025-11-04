---
nav_title: Exportieren
article_title: Endpunkte exportieren
search_tag: Endpoint
page_order: 2

layout: dev_guide

#Required
description: "Auf dieser Landing Page werden die Endpunkte für den Export von Braze erklärt und aufgelistet."
page_type: landing

guide_top_header: "Endpunkte exportieren"
guide_top_text: "Mit dieser Sammlung von Endpunkten können Sie auf verschiedene Ebenen von Details zu Ihren KPIs, App-Sitzungen, Nutzer:innen, Segmenten, Kampagnen und Canvase zugreifen und diese exportieren. <br> <br> Stellen Sie sicher, dass Sie Ihre <a href='/docs/user_guide/administrative/access_braze/braze_instances/' target='_blank'>Braze-Instanz</a>, Ihren <a href='/docs/api/api_key/' target='_blank'>API-Schlüssel</a> und Ihren <a href='/docs/api/identifier_types/' target='_blank'>API-Bezeichner</a> kennen, wenn Sie Ihre Parameter und Anfragen erstellen."

guide_featured_title: "Endpunkte der Kampagne exportieren"
guide_featured_list:
  - name: "GET: Kampagnen-Analytics"
    link: /docs/api/endpoints/export/campaigns/get_campaign_analytics/
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: "GET: Kampagnendetails"
    link: /docs/api/endpoints/export/campaigns/get_campaign_details/
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: "GET: Kampagnen Liste"
    link: /docs/api/endpoints/export/campaigns/get_campaigns/
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: "GET: Analytics senden"
    link: /docs/api/endpoints/export/campaigns/get_send_analytics/
    image: /assets/img/braze_icons/bar-chart-01.svg

guide_menu_title: "Export Canvas endpoints"
guide_menu_list:
  - name: "GET: Canvas Daten Serien Analytics"
    link: /docs/api/endpoints/export/canvas/get_canvas_analytics/
    image: /assets/img/braze_icons/dataflow-03.svg
  - name: "GET: Canvas Analytics Zusammenfassung"
    link: /docs/api/endpoints/export/canvas/get_canvas_analytics_summary/
    image: /assets/img/braze_icons/dataflow-03.svg
  - name: "GET: Canvas-Details"
    link: /docs/api/endpoints/export/canvas/get_canvas_details/
    image: /assets/img/braze_icons/dataflow-03.svg
  - name: "GET: Canvas Liste"
    link: /docs/api/endpoints/export/canvas/get_canvases/
    image: /assets/img/braze_icons/dataflow-03.svg

guide_menu_title2: "Export custom events endpoints"
guide_menu_list2:
  - name: "GET: Angepasste Events"
    link: /docs/api/endpoints/export/custom_events/get_custom_events_data/
    image: /assets/img/braze_icons/line-chart-up-01.svg
  - name: "GET: Angepasste Events Liste"
    link: /docs/api/endpoints/export/custom_events/get_custom_events/
    image: /assets/img/braze_icons/line-chart-up-01.svg
  - name: "GET: Angepasste Event Analytics"
    link: /docs/api/endpoints/export/custom_events/get_custom_events_analytics/
    image: /assets/img/braze_icons/line-chart-up-01.svg

guide_menu_title3: "Export KPI endpoints"
guide_menu_list3:
  - name: "GET: KPIs für täglich neue Nutzer:innen nach Datum"
    link: /docs/api/endpoints/export/kpi/get_kpi_daily_new_users_date/
    image: /assets/img/braze_icons/target-04.svg
  - name: "GET: KPIs für täglich aktive Nutzer:innen nach Datum"
    link: /docs/api/endpoints/export/kpi/get_kpi_dau_date/
    image: /assets/img/braze_icons/target-04.svg
  - name: "GET: KPIs für monatlich aktive Nutzer:innen in den letzten 30 Tagen"
    link: /docs/api/endpoints/export/kpi/get_kpi_mau_30_days/
    image: /assets/img/braze_icons/target-04.svg
  - name: "GET: KPIs für Deinstallationen nach Datum"
    link: /docs/api/endpoints/export/kpi/get_kpi_uninstalls_date/
    image: /assets/img/braze_icons/target-04.svg

guide_menu_title5: "Export purchase endpoints"
guide_menu_list5:
  - name: "GET: Produkt IDs Liste"
    link: /docs/api/endpoints/export/purchases/get_list_product_id/
    image: /assets/img/braze_icons/list.svg
  - name: "GET: Anzahl der Käufe"
    link: /docs/api/endpoints/export/purchases/get_number_of_purchases/
    image: /assets/img/braze_icons/list.svg
  - name: "GET: Umsatzdaten nach Zeit"
    link: /docs/api/endpoints/export/purchases/get_revenue_series/
    image: /assets/img/braze_icons/list.svg

guide_menu_title6: "Export segment endpoints"
guide_menu_list6:
  - name: "GET: Segmente Liste"
    link: /docs/api/endpoints/export/segments/get_segment/
    image: /assets/img/braze_icons/users-01.svg
  - name: "GET: Segment Analytics"
    link: /docs/api/endpoints/export/segments/get_segment_analytics/
    image: /assets/img/braze_icons/users-01.svg
  - name: "GET: Details zum Segment"
    link: /docs/api/endpoints/export/segments/get_segment_details/
    image: /assets/img/braze_icons/users-01.svg

guide_menu_title7: "Export sessions endpoint"
guide_menu_list7:
  - name: "GET: App-Sitzungen Zeitreihendaten"
    link: /docs/api/endpoints/export/sessions/get_sessions_analytics/
    image: /assets/img/braze_icons/tablet-01.svg

guide_menu_title8: "Export user data endpoints"
guide_menu_list8:
  - name: "POST: Nutzerdaten nach Bezeichner"
    link: /docs/api/endpoints/export/user_data/post_users_identifier/
    image: /assets/img/braze_icons/users-01.svg
  - name: "POST: Nutzerdaten nach Segmenten"
    link: /docs/api/endpoints/export/user_data/post_users_segment/
    image: /assets/img/braze_icons/users-01.svg
  - name: "POST: Nutzerdaten nach globaler Kontrollgruppe"
    link: /docs/api/endpoints/export/user_data/post_users_global_control_group/
    image: /assets/img/braze_icons/users-01.svg

guide_menu_title9: "Export custom attributes endpoints"
guide_menu_list9:
  - name: "GET: Angepasste Attribute"
    link: /docs/api/endpoints/export/custom_attributes/get_custom_attributes/
    image: /assets/img/braze_icons/line-chart-up-01.svg
---
