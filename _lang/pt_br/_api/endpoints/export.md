---
nav_title: Exportar
article_title: Exportar pontos de extremidade
search_tag: Endpoint
page_order: 2

layout: dev_guide

#Required
description: "Esta landing page explica e lista os endpoints de exportação do Braze."
page_type: landing

guide_top_header: "Exportar pontos de extremidade"
guide_top_text: "Com esta coleção de endpoints, você pode acessar e exportar vários níveis de detalhes sobre seus KPIs, sessões de app, usuários, segmentos, campanhas e canvas. <br> <br> Certifique-se de conhecer sua <a href='/docs/user_guide/administrative/access_braze/braze_instances/' target='_blank'>instância do Braze</a>, <a href='/docs/api/api_key/' target='_blank'>a chave de API</a> e <a href='/docs/api/identifier_types/' target='_blank'>o identificador de API</a> ao criar seus parâmetros e corpos de solicitação."

guide_featured_title: "Exportar endpoints de campanha"
guide_featured_list:
  - name: "OBTER: Análises de dados da campanha"
    link: /docs/api/endpoints/export/campaigns/get_campaign_analytics/
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: "OBTER: Informações da campanha"
    link: /docs/api/endpoints/export/campaigns/get_campaign_details/
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: "OBTER: Lista de campanhas"
    link: /docs/api/endpoints/export/campaigns/get_campaigns/
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: "OBTER: Enviar análises de dados"
    link: /docs/api/endpoints/export/campaigns/get_send_analytics/
    image: /assets/img/braze_icons/bar-chart-01.svg

guide_menu_title: "Export Canvas endpoints"
guide_menu_list:
  - name: "OBTER: Análise de séries de dados do Canva"
    link: /docs/api/endpoints/export/canvas/get_canvas_analytics/
    image: /assets/img/braze_icons/dataflow-03.svg
  - name: "OBTER: Resumo da análise de dados do Canva"
    link: /docs/api/endpoints/export/canvas/get_canvas_analytics_summary/
    image: /assets/img/braze_icons/dataflow-03.svg
  - name: "OBTER: Informações do canva"
    link: /docs/api/endpoints/export/canvas/get_canvas_details/
    image: /assets/img/braze_icons/dataflow-03.svg
  - name: "OBTER: Lista de telas"
    link: /docs/api/endpoints/export/canvas/get_canvases/
    image: /assets/img/braze_icons/dataflow-03.svg

guide_menu_title2: "Export custom events endpoints"
guide_menu_list2:
  - name: "OBTER: Eventos personalizados"
    link: /docs/api/endpoints/export/custom_events/get_custom_events_data/
    image: /assets/img/braze_icons/line-chart-up-01.svg
  - name: "OBTER: Lista de eventos personalizados"
    link: /docs/api/endpoints/export/custom_events/get_custom_events/
    image: /assets/img/braze_icons/line-chart-up-01.svg
  - name: "OBTER: Análise de dados de eventos personalizados"
    link: /docs/api/endpoints/export/custom_events/get_custom_events_analytics/
    image: /assets/img/braze_icons/line-chart-up-01.svg

guide_menu_title3: "Export KPI endpoints"
guide_menu_list3:
  - name: "OBTER: KPIs para novos usuários diários por data"
    link: /docs/api/endpoints/export/kpi/get_kpi_daily_new_users_date/
    image: /assets/img/braze_icons/target-04.svg
  - name: "OBTER: KPIs para usuários ativos diários por data"
    link: /docs/api/endpoints/export/kpi/get_kpi_dau_date/
    image: /assets/img/braze_icons/target-04.svg
  - name: "OBTER: KPIs para usuários ativos mensais nos últimos 30 dias"
    link: /docs/api/endpoints/export/kpi/get_kpi_mau_30_days/
    image: /assets/img/braze_icons/target-04.svg
  - name: "OBTER: KPIs para desinstalações por data"
    link: /docs/api/endpoints/export/kpi/get_kpi_uninstalls_date/
    image: /assets/img/braze_icons/target-04.svg

guide_menu_title5: "Export purchase endpoints"
guide_menu_list5:
  - name: "OBTER: Lista de IDs de produtos"
    link: /docs/api/endpoints/export/purchases/get_list_product_id/
    image: /assets/img/braze_icons/list.svg
  - name: "OBTER: Número de compras"
    link: /docs/api/endpoints/export/purchases/get_number_of_purchases/
    image: /assets/img/braze_icons/list.svg
  - name: "OBTER: Dados de receita por tempo"
    link: /docs/api/endpoints/export/purchases/get_revenue_series/
    image: /assets/img/braze_icons/list.svg

guide_menu_title6: "Export segment endpoints"
guide_menu_list6:
  - name: "OBTER: Lista de segmentos"
    link: /docs/api/endpoints/export/segments/get_segment/
    image: /assets/img/braze_icons/users-01.svg
  - name: "OBTER: Análise de dados do segmento"
    link: /docs/api/endpoints/export/segments/get_segment_analytics/
    image: /assets/img/braze_icons/users-01.svg
  - name: "OBTER: Informações do segmento"
    link: /docs/api/endpoints/export/segments/get_segment_details/
    image: /assets/img/braze_icons/users-01.svg

guide_menu_title7: "Export sessions endpoint"
guide_menu_list7:
  - name: "OBTER: Dados de séries temporais de sessões de aplicativos"
    link: /docs/api/endpoints/export/sessions/get_sessions_analytics/
    image: /assets/img/braze_icons/tablet-01.svg

guide_menu_title8: "Export user data endpoints"
guide_menu_list8:
  - name: "POST: Dados de usuários por identificador"
    link: /docs/api/endpoints/export/user_data/post_users_identifier/
    image: /assets/img/braze_icons/users-01.svg
  - name: "POST: Dados de usuários por segmento"
    link: /docs/api/endpoints/export/user_data/post_users_segment/
    image: /assets/img/braze_icons/users-01.svg
  - name: "POST: Dados de usuários do grupo de controle global"
    link: /docs/api/endpoints/export/user_data/post_users_global_control_group/
    image: /assets/img/braze_icons/users-01.svg

guide_menu_title9: "Export custom attributes endpoints"
guide_menu_list9:
  - name: "OBTER: Atributos personalizados"
    link: /docs/api/endpoints/export/custom_attributes/get_custom_attributes/
    image: /assets/img/braze_icons/line-chart-up-01.svg
---
