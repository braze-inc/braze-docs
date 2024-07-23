---
nav_title: Messages
article_title: Endpoints de messagerie
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
description: "Cette page d’accueil liste les endpoints Braze d’envoi de messages."
page_type: landing

guide_top_header: "Endpoints de messagerie"
guide_top_text: "L’API de messagerie Braze vous offre deux options pour envoyer des messages à vos utilisateurs. Tu peux fournir le contenu des messages et la configuration dans la demande API avec les points de terminaison <code class='highlighter-rouge'>/messages/send</code> et `/messages/schedule`. Sinon, tu peux gérer les détails de ton message avec une campagne déclenchée par l'API dans le tableau de bord de Braze et simplement contrôler quand et à qui il est envoyé avec les points de terminaison `/campaigns/trigger/send` et `/campaigns/trigger/schedule`. Les sections suivantes détailleront la spécification de la demande pour les deux méthodes. <br> <br>De la même manière que pour les autres campagnes, tu peux limiter le nombre de fois qu'un utilisateur donné peut recevoir une campagne API de messagerie en configurant les [paramètres de rééligibilité](/docs/guide_utilisateur/engagement_tools/campagnes/construction_campagnes/delivery_types/api_triggered_delivery/#re-eligibility-with-api-triggered-campaigns) dans le tableau de bord de Braze. Braze ne délivrera pas de messages API aux utilisateurs qui ne sont pas redevenus éligibles pour la campagne, quel que soit le nombre de demandes API envoyées. <br> <br>Les points d'extrémité Envoyer un message te permettent d'envoyer des messages immédiats aux utilisateurs désignés. Si tu cibles un segment, un enregistrement de ta demande sera stocké dans le **Journal d'activité des messages**. Utilise les points de terminaison Programmer un message pour envoyer des messages à une heure désignée, et modifier ou annuler les messages que tu as déjà programmés."

guide_featured_title: "Endpoints de planification des messages"
guide_featured_list:
  - name: "GET: List Upcoming Scheduled Campaigns and Canvases"
    link: /docs/api/endpoints/messaging/schedule_messages/get_messages_scheduled/
    image: /assets/img/braze_icons/calendar-date.svg
  - name: "POST: Delete Scheduled Messages"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages/
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: "POST: Delete Scheduled API-Triggered Campaigns"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: "POST: Delete Scheduled API-Triggered Canvases"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases/
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: "POST: Schedule Messages"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_messages/
    image: /assets/img/braze_icons/calendar-plus-01.svg
  - name: "POST: Schedule API-Triggered Campaign Messages"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: "POST: Schedule API-Triggered Canvas Messages"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: "POST: Update Scheduled Messages"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages/
    image: /assets/img/braze_icons/calendar-date.svg
  - name: "POST: Update Scheduled API-Triggered Campaign Messages"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns/
    image: /assets/img/braze_icons/calendar-date.svg
  - name: "POST: Update Scheduled API-Triggered Canvas Messages"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/
    image: /assets/img/braze_icons/calendar-check-02.svg

guide_menu_title: "Send messages endpoints"
guide_menu_list:
  - name: "POST: Create Send IDs"
    link: /docs/api/endpoints/messaging/send_messages/post_create_send_ids/
    image: /assets/img/braze_icons/user-square.svg
  - name: "POST: Send Messages Immediately"
    link: /docs/api/endpoints/messaging/send_messages/post_send_messages/
    image: /assets/img/braze_icons/send-01.svg
  - name: "POST: Send API-Triggered Campaign Messages Immediately"
    link: /docs/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/
    image: /assets/img/braze_icons/inbox-01.svg
  - name: "POST: Send API-Triggered Canvas Messages Immediately"
    link: /docs/api/endpoints/messaging/send_messages/post_send_triggered_canvases/
    image: /assets/img/braze_icons/inbox-01.svg

guide_menu_title2: "Live Activity endpoints"
guide_menu_list2:
  - name: "POST: Update Live Activity"
    link: /docs/api/endpoints/messaging/live_activity/update/
    image: /assets/img/braze_icons/tablet-01.svg
---
