---
nav_title: Messagerie
article_title: Points de terminaison des messages
search_tag: Endpoint
page_order: 2
local_redirect:  #parameter-definitions #app-group-rest-api-key #app-identifier #external-user-id #segment-identifier #campaign-identifier #canvas-identifier #trigger-properties #canvas-identifier #server-responses #fatal-errors #responses-for-tracked-send-ids #messaging-queued #canvas-entry-properties
  parameter-definitions: '/fr/docs/api/parameters/'
  app-group-rest-api-key: '/fr/docs/api/parameters/'
  app-identifier: '/fr/docs/api/parameters/'
  external-user-id: '/fr/docs/api/parameters/'
  segment-identifier: '/fr/docs/api/parameters/'
  campaign-identifier: '/fr/docs/api/parameters/'
  canvas-identifier: '/fr/docs/api/parameters/'
  send-identifier: '/fr/docs/api/parameters/'
  trigger-properties: '/fr/docs/api/parameters/'
  canvas-entry-properties: '/fr/docs/api/parameters/'
  server-responses: '/fr/docs/api/errors/'
  messaging-queued: '/fr/docs/api/errors/'
  responses-for-tracked-send-ids: '/fr/docs/api/errors/'
  fatal-errors: '/fr/docs/api/errors/'
layout: dev_guide
#Required
description: "Cette page de destination explique et liste les points de terminaison de la messagerie Braze."
page_type: atterrissage
guide_top_header: "Points de terminaison des messages"
guide_top_text: "L'API de messagerie Braze vous offre deux options distinctes pour envoyer des messages à vos utilisateurs. Vous pouvez fournir le contenu et la configuration des messages dans la requête API avec les points de terminaison <code class='highlighter-rouge'>/messages/send</code> et `/messages/schedule`. Autrement, vous pouvez gérer les détails de votre message avec une campagne de distribution déclenchée par l'API dans le tableau de bord et juste contrôler quand et à qui elle est envoyée avec les extrémités `campagnes/trigger/send` et `campaigns/trigger/schedule`. Les sections suivantes détailleront la spécification de la requête pour les deux méthodes. <br> <br> Similairement aux autres campagnes, vous pouvez limiter le nombre de fois qu'un utilisateur peut recevoir une campagne d'API de messagerie en configurant [les paramètres de rééligibilité](/docs/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/api_triggered_delivery/#re-eligibility-with-api-triggered-campaigns) dans le tableau de bord de Braze. Braze n'enverra pas de messages API aux utilisateurs qui ne sont pas rééligibles pour la campagne, quel que soit le nombre de requêtes API envoyées. <br> <br> Les terminaux d'envoi vous permettent d'envoyer des messages immédiats et ad hoc aux utilisateurs désignés. Si vous visez un segment, un enregistrement de votre requête sera stocké dans la Console Développeur. Les points de terminaison du programme vous permettent d'envoyer des messages à une heure désignée et de modifier ou d'annuler les messages que vous avez déjà planifiés."
guide_featured_title: "Planifier les points de terminaison des messages"
guide_featured_list:
  - 
    name: "GET: Lister les prochaines campagnes et toiles planifiées"
    link: /docs/api/endpoints/messaging/schedule_messages/get_messages_scheduled/
    fa_icon: fas fa-calendar
  - 
    name: "POST: Supprimer les messages programmés"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages/
    fa_icon: fas fa-calendar-minus
  - 
    name: "POST: Supprimer les campagnes programmées déclenchées par l'API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/
    fa_icon: fas fa-calendar-minus
  - 
    name: "POST: Supprimer les Canevas programmées déclenchées par l'API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases/
    fa_icon: fas fa-calendar-minus
  - 
    name: "POST: Programmer des messages"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_messages/
    fa_icon: fa-calendar-plus
  - 
    name: "POST: Planifier les messages de campagne déclenchés par l'API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/
    fa_icon: fas fa-calendar-alt
  - 
    name: "POST: Planifier les messages de Canvas déclenchés par l'API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/
    fa_icon: fas fa-calendar-alt
  - 
    name: "POST: Mettre à jour les messages programmés"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages/
    fa_icon: fas fa-calendar
  - 
    name: "POST: Mettre à jour les messages de campagne programmés par l'API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns/
    fa_icon: fas fa-calendar
  - 
    name: "POST: Mettre à jour les messages Canvas déclenchés par l'API"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/
    fa_icon: fas fa-calendar-alt
guide_menu_title: "Envoyer les points de terminaison des messages"
guide_menu_list:
  - 
    name: "POST: Créer des ID d'envoi"
    link: /docs/api/endpoints/messaging/send_messages/post_create_send_ids/
    fa_icon: fas fa-id-card
  - 
    name: "POST: Envoyer des messages immédiatement"
    link: /docs/api/endpoints/messaging/send_messages/post_send_messages/
    fa_icon: fas fa-paper-plane
  - 
    name: "POST: Envoyer des messages de campagne déclenchés par l'API immédiatement"
    link: /docs/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/
    fa_icon: fas fa-inbox
  - 
    name: "POST: Envoyer immédiatement les messages Canvas déclenchés par l'API"
    link: /docs/api/endpoints/messaging/send_messages/post_send_triggered_canvases/
    fa_icon: fas fa-inbox
---

