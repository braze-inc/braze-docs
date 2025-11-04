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
guide_top_text: "Avec cette collection d'endpoints, vous pouvez accéder et exporter différents niveaux de détails sur vos KPI, sessions d'app, utilisateurs, segments, campagnes et Canvases. <br> <br> Assurez-vous de connaître votre <a href='/docs/user_guide/administrative/access_braze/braze_instances/' target='_blank'>instance Braze</a>, <a href='/docs/api/api_key/' target='_blank'>clé API</a> et <a href='/docs/api/identifier_types/' target='_blank'>identifiant d’API</a> lors de l’élaboration de vos paramètres et corps de requête."

guide_featured_title: "Exporter les points de terminaison de la campagne"
guide_featured_list:
  - name: "GET : Analyse de campagne"
    link: /docs/api/endpoints/export/campaigns/get_campaign_analytics/
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: "GET : Détails de la campagne"
    link: /docs/api/endpoints/export/campaigns/get_campaign_details/
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: "GET : Liste des campagnes"
    link: /docs/api/endpoints/export/campaigns/get_campaigns/
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: "GET : Envoyer des analyses"
    link: /docs/api/endpoints/export/campaigns/get_send_analytics/
    image: /assets/img/braze_icons/bar-chart-01.svg

guide_menu_title: "Export Canvas endpoints"
guide_menu_list:
  - name: "GET : Analyse des séries de données de Canvas"
    link: /docs/api/endpoints/export/canvas/get_canvas_analytics/
    image: /assets/img/braze_icons/dataflow-03.svg
  - name: "GET : Résumé de l’analyse des Canvas"
    link: /docs/api/endpoints/export/canvas/get_canvas_analytics_summary/
    image: /assets/img/braze_icons/dataflow-03.svg
  - name: "GET : Informations relatives au canvas"
    link: /docs/api/endpoints/export/canvas/get_canvas_details/
    image: /assets/img/braze_icons/dataflow-03.svg
  - name: "GET : Liste des Canvas"
    link: /docs/api/endpoints/export/canvas/get_canvases/
    image: /assets/img/braze_icons/dataflow-03.svg

guide_menu_title2: "Export custom events endpoints"
guide_menu_list2:
  - name: "GET : Événements personnalisés"
    link: /docs/api/endpoints/export/custom_events/get_custom_events_data/
    image: /assets/img/braze_icons/line-chart-up-01.svg
  - name: "GET : Liste des événements personnalisés"
    link: /docs/api/endpoints/export/custom_events/get_custom_events/
    image: /assets/img/braze_icons/line-chart-up-01.svg
  - name: "GET : Analyse d’événements personnalisés"
    link: /docs/api/endpoints/export/custom_events/get_custom_events_analytics/
    image: /assets/img/braze_icons/line-chart-up-01.svg

guide_menu_title3: "Export KPI endpoints"
guide_menu_list3:
  - name: "GET : Indicateurs clé de performance pour les nouveaux utilisateurs quotidiens par date"
    link: /docs/api/endpoints/export/kpi/get_kpi_daily_new_users_date/
    image: /assets/img/braze_icons/target-04.svg
  - name: "GET : Indicateurs clé de performance pour les utilisateurs actifs quotidiens par date"
    link: /docs/api/endpoints/export/kpi/get_kpi_dau_date/
    image: /assets/img/braze_icons/target-04.svg
  - name: "GET : Indicateurs clé de performance pour les utilisateurs actifs mensuels au cours des 30 derniers jours"
    link: /docs/api/endpoints/export/kpi/get_kpi_mau_30_days/
    image: /assets/img/braze_icons/target-04.svg
  - name: "GET : Indicateurs clé de performance pour les désinstallations par date"
    link: /docs/api/endpoints/export/kpi/get_kpi_uninstalls_date/
    image: /assets/img/braze_icons/target-04.svg

guide_menu_title5: "Export purchase endpoints"
guide_menu_list5:
  - name: "GET : Liste des identifiants de produit"
    link: /docs/api/endpoints/export/purchases/get_list_product_id/
    image: /assets/img/braze_icons/list.svg
  - name: "GET : Nombre d'achats"
    link: /docs/api/endpoints/export/purchases/get_number_of_purchases/
    image: /assets/img/braze_icons/list.svg
  - name: "GET : Données de revenus par temps"
    link: /docs/api/endpoints/export/purchases/get_revenue_series/
    image: /assets/img/braze_icons/list.svg

guide_menu_title6: "Export segment endpoints"
guide_menu_list6:
  - name: "GET : Liste des segments"
    link: /docs/api/endpoints/export/segments/get_segment/
    image: /assets/img/braze_icons/users-01.svg
  - name: "GET : Analyses des segments"
    link: /docs/api/endpoints/export/segments/get_segment_analytics/
    image: /assets/img/braze_icons/users-01.svg
  - name: "GET : Informations relatives au segment"
    link: /docs/api/endpoints/export/segments/get_segment_details/
    image: /assets/img/braze_icons/users-01.svg

guide_menu_title7: "Export sessions endpoint"
guide_menu_list7:
  - name: "GET : Données de la série temporelle des sessions App"
    link: /docs/api/endpoints/export/sessions/get_sessions_analytics/
    image: /assets/img/braze_icons/tablet-01.svg

guide_menu_title8: "Export user data endpoints"
guide_menu_list8:
  - name: "POST : Données utilisateur par identifiant"
    link: /docs/api/endpoints/export/user_data/post_users_identifier/
    image: /assets/img/braze_icons/users-01.svg
  - name: "POST : Données utilisateur par segment"
    link: /docs/api/endpoints/export/user_data/post_users_segment/
    image: /assets/img/braze_icons/users-01.svg
  - name: "POST : Données utilisateur par groupe de contrôle global"
    link: /docs/api/endpoints/export/user_data/post_users_global_control_group/
    image: /assets/img/braze_icons/users-01.svg

guide_menu_title9: "Export custom attributes endpoints"
guide_menu_list9:
  - name: "GET : Attributs personnalisés"
    link: /docs/api/endpoints/export/custom_attributes/get_custom_attributes/
    image: /assets/img/braze_icons/line-chart-up-01.svg
---
