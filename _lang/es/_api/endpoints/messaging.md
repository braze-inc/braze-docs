---
nav_title: Mensajes
article_title: Puntos finales de mensajería
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
description: "Esta página de inicio enumera los puntos finales de mensajería de Braze."
page_type: landing

guide_top_header: "Puntos finales de mensajería"
guide_top_text: "La API de mensajería de Braze te ofrece dos opciones distintas para enviar mensajes a tus usuarios. Puedes proporcionar el contenido y la configuración del mensaje en la solicitud de API con la opción <code class='highlighter-rouge'>/messages/send</code> de puntos finales `/messages/schedule`. También puedes gestionar los detalles de tu mensaje con una campaña desencadenada por API en el panel de Braze y controlar cuándo y a quién se envía con los puntos finales `/campaigns/trigger/send` y `/campaigns/trigger/schedule`. En las secciones siguientes se detallan las especificaciones de las solicitudes de ambos métodos. <br> <br> De forma similar a otras campañas, puedes limitar el número de veces que un usuario concreto puede recibir una campaña de mensajería API configurando [ajustes de re-elegibilidad]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/#re-eligibility-with-api-triggered-campaigns) en el panel de Braze. Braze no enviará mensajes API a usuarios que no hayan vuelto a ser elegibles para la campaña, independientemente del número de solicitudes API que se envíen. <br> <br> Los puntos finales Enviar mensaje permiten enviar mensajes inmediatos a usuarios designados. Si te estás dirigiendo a un segmento específico, se guardará un registro de tu solicitud en el **Registro de actividad de mensajes**. Utiliza los puntos finales Programar mensaje para enviar mensajes a una hora determinada y modificar o cancelar mensajes que ya habías programado."

guide_featured_title: "Puntos finales Programar mensajes"
guide_featured_list:
  - name: "GET: Enumerar próximas campañas y Canvas programados"
    link: /docs/api/endpoints/messaging/schedule_messages/get_messages_scheduled/
    image: /assets/img/braze_icons/calendar-date.svg
  - name: "POST: Borrar mensajes programados"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages/
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: "POST: Eliminar campañas programadas desencadenadas por API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: "POST: Eliminar Canvas programados desencadenados por API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases/
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: "POST: Programar mensajes"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_messages/
    image: /assets/img/braze_icons/calendar-plus-01.svg
  - name: "POST: Programar mensajes de campaña desencadenados por API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: "POST: Programar mensajes de Canvas desencadenados por API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: "POST: Actualizar mensajes programados"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages/
    image: /assets/img/braze_icons/calendar-date.svg
  - name: "POST: Actualizar mensajes de campaña programados desencadenados por API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns/
    image: /assets/img/braze_icons/calendar-date.svg
  - name: "POST: Actualizar mensajes de Canvas programados desencadenados por API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/
    image: /assets/img/braze_icons/calendar-check-02.svg

guide_menu_title: "Send messages endpoints"
guide_menu_list:
  - name: "POST: Crear ID de envío"
    link: /docs/api/endpoints/messaging/send_messages/post_create_send_ids/
    image: /assets/img/braze_icons/user-square.svg
  - name: "POST: Enviar mensajes inmediatamente"
    link: /docs/api/endpoints/messaging/send_messages/post_send_messages/
    image: /assets/img/braze_icons/send-01.svg
  - name: "POST: Enviar inmediatamente mensajes de campaña desencadenados por API"
    link: /docs/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/
    image: /assets/img/braze_icons/inbox-01.svg
  - name: "POST: Enviar inmediatamente mensajes de Canvas desencadenados por API"
    link: /docs/api/endpoints/messaging/send_messages/post_send_triggered_canvases/
    image: /assets/img/braze_icons/inbox-01.svg

guide_menu_title2: "Duplicate message endpoints"
guide_menu_list2:
  - name: "POST: Campañas duplicadas"
    link: /docs/api/endpoints/messaging/duplicate_messages/post_duplicate_campaigns/
    image: /assets/img/braze_icons/copy-04.svg
  - name: "POST: Lienzos duplicados"
    link: /docs/api/endpoints/messaging/duplicate_messages/post_duplicate_canvases/
    image: /assets/img/braze_icons/copy-04.svg

guide_menu_title3: "Live Activity endpoints"
guide_menu_list3:
  - name: "POST: Actualizar actividad en vivo"
    link: /docs/api/endpoints/messaging/live_activity/update/
    image: /assets/img/braze_icons/tablet-01.svg
---
