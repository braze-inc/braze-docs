---
nav_title: Core Endpoints
permalink: "/core_endpoints/"
hidden: true
---

# Braze Core API Endpoints

Braze's API core endpoints are specific endpoints in Braze's REST API that have an allowed downtime in accordance with a Braze account's Service Level Agreement ("SLA"). For more information, please refer to your SLA documentation or reach out to your account manager. 

The core endpoints are as follows:
- [/users/track][1]
- [/users/delete][2]
- [/email/status][3]
- [/email/blacklist][4]
- [/messages/send][5]
- [/messages/schedule/create][6]
- [/messages/schedule/update][7]
- [/messages/schedule/delete][8]
- [/campaigns/trigger/send][9]
- [/campaigns/trigger/schedule/create][10]
- [/campaigns/trigger/schedule/update][11]
- [/campaigns/trigger/schedule/delete][12]
- [/canvas/trigger/send][13]
- [/canvas/trigger/schedule/create][14]
- [/canvas/trigger/schedule/update][15]
- [/canvas/trigger/schedule/delete][16]
- [/subscription/status/set][17]


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