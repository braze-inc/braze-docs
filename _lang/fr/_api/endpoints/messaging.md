---
nav_title: Messagerie
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
description: "Cette page d’accueil explique et répertorie les endpoints Braze de messagerie."
page_type: landing

guide_top_header: "Endpoints de messagerie"
guide_top_text: "L'API de messagerie Braze vous offre deux options pour envoyer des messages à vos utilisateurs. Vous pouvez fournir le contenu et la configuration du message dans la demande API à l’aide des endpoints <code class='highlighter-rouge'>/messages/send</code> et `/messages/schedule`. Vous pouvez également gérer les détails de votre message avec une campagne de livraison déclenchée par API dans le tableau de bord et contrôler simplement quand et à qui il est envoyé grâce aux endpoints `campaigns/trigger/send` et `campaigns/trigger/schedule`. Les sections suivantes détaillent la spécification de demande pour les deux méthodes. <br> <br> Comme pour les autres campagnes, vous pouvez limiter le nombre de fois qu’un utilisateur particulier peut recevoir une campagne de l’API de messagerie en configurant les [paramètres de rééligibilité](/docs/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/#re-eligibility-with-api-triggered-campaigns) dans le tableau de bord de Braze. Braze ne livrera pas de messages API aux utilisateurs qui ne sont pas rééligibles pour la campagne, quel que soit le nombre de demandes API envoyées. <br> <br> Les endpoints d’envoi vous permettent d’envoyer des messages instantanés et ad hoc aux utilisateurs désignés. Si vous souhaitez cibler un segment, un enregistrement de votre demande sera stocké dans la Developer Console (Console du développeur). Les endpoints de planification vous permettent d’envoyer des messages à un moment donné et de modifier ou d’annuler des messages que vous avez déjà planifiés."

guide_featured_title: "Endpoints de planification des messages"
guide_featured_list:
  - name: "GET : répertorier les campagnes et Canvas planifiés à venir"
    link: /docs/api/endpoints/messaging/schedule_messages/get_messages_scheduled/
    fa_icon: fas fa-calendar
  - name: "POST : supprimer les messages planifiés"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages/
    fa_icon: fas fa-calendar-minus
  - name: "POST : supprimer des campagnes planifiées déclenchées par API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/
    fa_icon: fas fa-calendar-minus
  - name: "POST : supprimer des Canvas planifiés déclenchés par API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases/
    fa_icon: fas fa-calendar-minus
  - name: "POST : planifier les messages"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_messages/
    fa_icon: fas fa-calendar-plus
  - name: "POST : planifier des messages de campagne déclenchés par API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/
    fa_icon: fas fa-calendar-alt
  - name: "POST : planifier des messages Canvas déclenchés par API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/
    fa_icon: fas fa-calendar-alt
  - name: "POST : mettre à jour les messages planifiés"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages/
    fa_icon: fas fa-calendar
  - name: "POST : mettre à jour les messages de campagnes planifiés déclenchés par API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns/
    fa_icon: fas fa-calendar
  - name: "POST : mettre à jour des messages Canvas planifiés déclenchés par API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/
    fa_icon: fas fa-calendar-alt

guide_menu_title: "Endpoints des messages d’envoi"
guide_menu_list:
  - name: "POST : créer des ID d’envoi"
    link: /docs/api/endpoints/messaging/send_messages/post_create_send_ids/
    fa_icon: fas fa-id-card
  - name: "POST : envoyer les messages immédiatement"
    link: /docs/api/endpoints/messaging/send_messages/post_send_messages/
    fa_icon: fas fa-paper-plane
  - name: "POST : envoyer immédiatement les messages de campagnes déclenchés par API"
    link: /docs/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/
    fa_icon: fas fa-inbox
  - name: "POST : envoyer immédiatement les messages Canvas déclenchés par API"
    link: /docs/api/endpoints/messaging/send_messages/post_send_triggered_canvases/
    fa_icon: fas fa-inbox
---
