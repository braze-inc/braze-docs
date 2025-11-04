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
guide_top_text: "L’API de messagerie Braze vous offre deux options pour envoyer des messages à vos utilisateurs. Vous pouvez fournir le contenu et la configuration du message dans la demande d'API à l'aide de l'attribut <code class='highlighter-rouge'>/messages/send</code> et les endpoints `/messages/schedule`. Vous pouvez également gérer les détails de votre message avec une campagne déclenchée par l'API dans le tableau de bord de Braze et contrôler simplement quand et à qui il est envoyé avec les endpoints `/campaigns/trigger/send` et `/campaigns/trigger/schedule`. Les sections suivantes détaillent la spécification de demande pour les deux méthodes. <br> <br> De la même manière que pour les autres campagnes, vous pouvez limiter le nombre de fois qu'un utilisateur donné peut recevoir une campagne API de messages en configurant les [paramètres de rééligibilité]({{site.baseurl}}/user_guide/engagement_tools/campagnes/building_campaigns/delivery_types/api_triggered_delivery/#re-eligibility-with-api-triggered-campaigns) dans le tableau de bord de Braze. Braze ne livrera pas de messages API aux utilisateurs qui ne sont pas rééligibles pour la campagne, quel que soit le nombre de demandes API envoyées. <br> <br> Les endpoints d'envoi de messages vous permettent d'envoyer des messages immédiats à des utilisateurs désignés. Si vous ciblez un segmentation, un enregistrement de votre demande sera stocké dans le **Journal d'activité des messages**. Utilisez les endpoints Schedule Message pour envoyer des messages à une heure donnée, et pour modifier ou annuler des messages que vous avez déjà planifiés."

guide_featured_title: "Points d'extrémité des messages de planification"
guide_featured_list:
  - name: "GET : Répertorier les campagnes et Canvas planifiés à venir"
    link: /docs/api/endpoints/messaging/schedule_messages/get_messages_scheduled/
    image: /assets/img/braze_icons/calendar-date.svg
  - name: "POST : Supprimer les messages planifiés"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages/
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: "POST : Supprimer des campagnes planifiées déclenchées par API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: "POST : Supprimer des Canvas planifiés déclenchés par API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases/
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: "POST : Planifier les messages"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_messages/
    image: /assets/img/braze_icons/calendar-plus-01.svg
  - name: "POST : Planifier des messages de campagne déclenchés par API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: "POST : Planifier des messages Canvas déclenchés par API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: "POST : Mettre à jour les messages planifiés"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages/
    image: /assets/img/braze_icons/calendar-date.svg
  - name: "POST : Mettre à jour les messages de campagnes planifiés déclenchés par API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns/
    image: /assets/img/braze_icons/calendar-date.svg
  - name: "POST : Mettre à jour des messages Canvas planifiés déclenchés par API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/
    image: /assets/img/braze_icons/calendar-check-02.svg

guide_menu_title: "Send messages endpoints"
guide_menu_list:
  - name: "POST : Créer des ID d’envoi"
    link: /docs/api/endpoints/messaging/send_messages/post_create_send_ids/
    image: /assets/img/braze_icons/user-square.svg
  - name: "POST : Envoyer les messages immédiatement"
    link: /docs/api/endpoints/messaging/send_messages/post_send_messages/
    image: /assets/img/braze_icons/send-01.svg
  - name: "POST : Envoyer immédiatement les messages de campagnes déclenchés par API"
    link: /docs/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/
    image: /assets/img/braze_icons/inbox-01.svg
  - name: "POST : Envoyer immédiatement les messages Canvas déclenchés par API"
    link: /docs/api/endpoints/messaging/send_messages/post_send_triggered_canvases/
    image: /assets/img/braze_icons/inbox-01.svg

guide_menu_title2: "Duplicate message endpoints"
guide_menu_list2:
  - name: "POST : Campagnes en double"
    link: /docs/api/endpoints/messaging/duplicate_messages/post_duplicate_campaigns/
    image: /assets/img/braze_icons/copy-04.svg
  - name: "POST : Dupliquer les canvas"
    link: /docs/api/endpoints/messaging/duplicate_messages/post_duplicate_canvases/
    image: /assets/img/braze_icons/copy-04.svg

guide_menu_title3: "Live Activity endpoints"
guide_menu_list3:
  - name: "POST : Mettre à jour l’activité en direct"
    link: /docs/api/endpoints/messaging/live_activity/update/
    image: /assets/img/braze_icons/tablet-01.svg
---
