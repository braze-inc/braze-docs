---
nav_title: Points de terminaison du noyau
permalink: "/fr/core_endpoints/"
hidden: vrai
---

# Points de terminaison de l'API Braze Core

Les points de terminaison principaux de l'API Braze sont des terminaux spécifiques dans l'API REST de Braze qui ont un temps d'arrêt autorisé conformément à l'accord de niveau de service d'un compte Braze ("SLA"). Pour de plus amples renseignements, veuillez vous référer à votre documentation sur la SLA ou contacter votre responsable de compte.

Les points de terminaison principaux sont les suivants:
- [/fr/users/track][1]
- [/fr/users/delete][2]
- [/email/status][3]
- [/fr/email/blacklist][4]
- [/fr/messages/send][5]
- [/fr/messages/schedule/create][6]
- [/fr/messages/schedule/update][7]
- [/fr/messages/schedule/delete][8]
- [/fr/campaigns/trigger/send][9]
- [/fr/campaigns/trigger/schedule/create][10]
- [/fr/campaigns/trigger/schedule/update][11]
- [/fr/campaigns/trigger/schedule/delete][12]
- [/fr/canvas/trigger/send][13]
- [/fr/canvas/trigger/schedule/create][14]
- [/fr/canvas/trigger/schedule/update][15]
- [/fr/canvas/trigger/schedule/delete][16]
- [/fr/subscription/status/set][17]


[1]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/#user-track
[2]: {{site.baseurl}}/api/endpoints/user_data/post_user_delete
[3]: {{site.baseurl}}/api/endpoints/email/post_email_subscription_status/#change-users-email-subscription-status
[4]: {{site.baseurl}}/api/endpoints/email/post_blacklist/
[5]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/#sending-messages-immediately-via-api-only
[6]: {{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages/#create-scheduled-messages
[7]: {{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages/
[8]: {{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages/
[9]: {{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages/#create-scheduled-messages
[10]: {{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/
[11]: {{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns/
[12]: {{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/
[13]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#sending-canvas-messages-via-api-triggered-delivery
[14]: {{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/#schedule-api-triggered-canvases
[15]: {{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns/
[16]: {{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/
[17]: {{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/#update-users-subscription-group-status