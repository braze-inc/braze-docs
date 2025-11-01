---
nav_title: Mensagens
article_title: Endpoints de envio de mensagens
search_tag: Endpoint
page_order: 3
local_redirect: #app-group-rest-api-key #app-identifier #external-user-id #segment-identifier #campaign-identifier #canvas-identifier #trigger-properties #canvas-identifier #server-responses #fatal-errors #responses-for-tracked-send-ids #messaging-queued #canvas-entry-properties
  app-group-rest-api-key: '/docs/api/basics/#rest-api-key'
  app-identifier: '/docs/api/identifier_types/'
  external-user-id: '/docs/api/objects_filters/user_attributes_object/#braze-user-profile-fields'
  segment-identifier: '/docs/api/identifier_types/'
  campaign-identifier: '/docs/api/identifier_types/'
  canvas-identifier: '/docs/api/identifier_types/'
  send-identifier: '/docs/api/identifier_types/'
  trigger-properties: '/docs/api/objects_filters/trigger_properties_object'
  canvas-entry-properties: '/docs/api/objects_filters/canvas_entry_properties_object'
  server-responses: '/docs/api/errors/'
  messaging-queued: '/docs/api/errors/'
  responses-for-tracked-send-ids: '/docs/api/errors/'
  fatal-errors: '/docs/api/errors/'

layout: dev_guide

#Required
description: "Essa landing page lista os endpoints de envio de mensagens da Braze."
page_type: landing

guide_top_header: "Endpoints de envio de mensagens"
guide_top_text: "A API de envio de mensagens da Braze oferece duas opções distintas para o envio de mensagens aos seus usuários. Você pode fornecer o conteúdo e a configuração da mensagem na solicitação da API com os endpoints <code class='highlighter-rouge'>/messages/send</code> e `/messages/schedule`. Como alternativa, você pode gerenciar os detalhes de sua mensagem com uma campanha de mensagens disparada pela API no dashboard da Braze e apenas controlar quando e para quem ela é enviada com os endpoints `/campaigns/trigger/send` e `/campaigns/trigger/schedule`. As seções a seguir detalharão a especificação da solicitação para ambos os métodos. <br> <br> Da mesma forma que outras campanhas, você pode limitar o número de vezes que um determinado usuário pode receber uma campanha de API de mensagens configurando [re-eligibility settings]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/#re-eligibility-with-API-triggered-campaigns) no painel do Braze. A Braze não enviará mensagens API para usuários que não se tornaram elegíveis para a campanha, independentemente de quantas solicitações de API forem enviadas. <br> <br> Os endpoints \"Enviar mensagem\"  permitem enviar mensagens imediatas a usuários designados. Se estiver direcionando a campanha para um segmento, um registro da sua solicitação será armazenado no **Registros de atividades de mensagem**. Use os endpoints \"Agendar mensagem\" para enviar mensagens em um horário designado e modificar ou cancelar mensagens que já foram agendadas."

guide_featured_title: "Programar endpoints de mensagens"
guide_featured_list:
  - name: "OBTER: Listar as próximas campanhas e canvas programadas"
    link: /docs/api/endpoints/messaging/schedule_messages/get_messages_scheduled/
    image: /assets/img/braze_icons/calendar-date.svg
  - name: "POST: Excluir envios de mensagens programadas"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages/
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: "POST: Excluir campanhas programadas disparadas pela API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: "POST: Excluir telas programadas disparadas pela API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases/
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: "POST: Agendar mensagens"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_messages/
    image: /assets/img/braze_icons/calendar-plus-01.svg
  - name: "POST: Agendar envios de mensagens de campanha disparados pela API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: "POST: Agendar mensagens de canvas disparadas pela API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: "POST: Atualizar envios de mensagens programadas"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages/
    image: /assets/img/braze_icons/calendar-date.svg
  - name: "POST: Atualizar mensagens programadas de campanhas de mensagens disparadas pela API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns/
    image: /assets/img/braze_icons/calendar-date.svg
  - name: "POST: Atualizar mensagens de canvas programados disparados pela API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/
    image: /assets/img/braze_icons/calendar-check-02.svg

guide_menu_title: "Send messages endpoints"
guide_menu_list:
  - name: "POST: Criar IDs de envio"
    link: /docs/api/endpoints/messaging/send_messages/post_create_send_ids/
    image: /assets/img/braze_icons/user-square.svg
  - name: "POST: Enviar mensagens imediatamente"
    link: /docs/api/endpoints/messaging/send_messages/post_send_messages/
    image: /assets/img/braze_icons/send-01.svg
  - name: "POST: Enviar mensagens de campanha disparadas por API imediatamente"
    link: /docs/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/
    image: /assets/img/braze_icons/inbox-01.svg
  - name: "POST: Enviar mensagens de canvas disparadas pela API imediatamente"
    link: /docs/api/endpoints/messaging/send_messages/post_send_triggered_canvases/
    image: /assets/img/braze_icons/inbox-01.svg

guide_menu_title2: "Duplicate message endpoints"
guide_menu_list2:
  - name: "POST: Campanhas duplicadas"
    link: /docs/api/endpoints/messaging/duplicate_messages/post_duplicate_campaigns/
    image: /assets/img/braze_icons/copy-04.svg
  - name: "POST: Canvas duplicadas"
    link: /docs/api/endpoints/messaging/duplicate_messages/post_duplicate_canvases/
    image: /assets/img/braze_icons/copy-04.svg

guide_menu_title3: "Live Activity endpoints"
guide_menu_list3:
  - name: "POST: Atividade de atualização em tempo real"
    link: /docs/api/endpoints/messaging/live_activity/update/
    image: /assets/img/braze_icons/tablet-01.svg
---
