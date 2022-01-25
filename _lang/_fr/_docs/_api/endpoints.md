---
nav_title: Points de terminaison
article_title: Indice de terminaison de l'API
page_order: 1
description: "Cette page répertorie les points de terminaison Braze disponibles."
page_type: reference
---

<style>
table th:nth-child(1),
table th:nth-child(2),
table td:nth-child(1),
table td:nth-child(2) {
    max-width:150px;
}
table td {
    word-break: break-word;
}
</style>

# Indice de terminaison de l'API

## Données utilisateur

| Méthode | Points de terminaison                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| POSTER  | [/users/alias/new][/users/alias/new]<br>[/users/delete][/users/delete]<br>[/users/export/global_control_group][/users/export/global_control_group]<br>[/users/export/ids][/users/export/ids]<br>[/users/export/segment][/users/export/segment]<br>[/users/external_ids/rename][/users/external_ids/rename]<br>[/users/external_ids/remove][/users/external_ids/remove]<br>[/users/identify][/users/identify]<br>[/users/track][/users/track] |
{: .reset-td-br-1 .reset-td-br-2}

## Envoyer des messages

| Méthode | Points de terminaison                                                                                                                                                                                                                                                                                          |
| ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| POSTER  | [/campaigns/trigger/send][/campaigns/trigger/send]<br>[/canvas/trigger/send][/canvas/trigger/send]<br>[/messages/send][/messages/send]<br>[/sends/id/create][/sends/id/create]<br>[/transactional/v1/campaigns/{{CAMPAIGN_ID}}/send][/transactional/v1/campaigns/{{CAMPAIGN_ID}}/send] |
{: .reset-td-br-1 .reset-td-br-2}

## Programmer les messages

| Méthode | Points de terminaison                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| POSTER  | [/campaigns/trigger/schedule/create][/campaigns/trigger/schedule/create]<br>[/campaigns/trigger/schedule/delete][/campaigns/trigger/schedule/delete]<br>[/campaigns/trigger/scheduger/update][/campaigns/trigger/schedule/update]<br>[/canvas/trigger/schedule/create][/canvas/trigger/schedule/create]<br>[/canvas/trigger/schedule/delete][/canvas/trigger/schedule/delete]<br>[/canvas/trigger/trigger/schedule/update][/canvas/trigger/schedule/update]<br>[/messages/schedule/create][/messages/schedule/create]<br>[/messages/schedule/delete][/messages/schedule/delete]<br>[/messages/schedule/update][/messages/schedule/update] |
| OBTENIR | [/fr/messages/scheduled_broadcasts][/messages/scheduled_broadcasts]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
{: .reset-td-br-1 .reset-td-br-2}

## Groupes d'abonnement

| Méthode | Points de terminaison                                                                                                |
| ------- | -------------------------------------------------------------------------------------------------------------------- |
| POSTER  | [/fr/subscription/status/set][/subscription/status/set]                                                              |
| OBTENIR | [/subscription/status/get][/subscription/status/get]<br>[/subscription/user/status][/subscription/user/status] |
{: .reset-td-br-1 .reset-td-br-2}

## Modèles d'e-mail et d'e-mail

| Méthode | Points de terminaison                                                                                                                                                                                                                                                                                        |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| POSTER  | [/email/blacklist][/email/blacklist]<br>[/email/bounce/remove][/email/bounce/remove]<br>[/email/spam/remove][/email/spam/remove]<br>[/email/status][/email/status]<br>[/templates/email/create][/templates/email/create]<br>[/templates/email/update][/templates/email/update] |
| OBTENIR | [/email/hard_bounces][/email/hard_bounces]<br>[/email/unsubscribes][/email/unsubscribes]<br>[/templates/email/info][/templates/email/info]<br>[/templates/email/list][/templates/email/list]                                                                                               |
{: .reset-td-br-1 .reset-td-br-2}

## Campagnes

| Méthode | Points de terminaison                                                                                                                                                                            |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| OBTENIR | [/campaigns/data_series][/campaigns/data_series]<br>[/campaigns/details][/campaigns/details]<br>[/campaigns/list][/campaigns/list]<br>[/sends/data_series][/sends/data_series] |
{: .reset-td-br-1 .reset-td-br-2}

## Toile

| Méthode | Points de terminaison                                                                                                                                                               |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OBTENIR | [/canvas/data_series][/canvas/data_series]<br>[/canvas/data_summary][/canvas/data_summary]<br>[/canvas/details][/canvas/details]<br>[/canvas/liste][/canvas/list] |
{: .reset-td-br-1 .reset-td-br-2}

## Segments

| Méthode | Points de terminaison                                                                                                                                                                            |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| OBTENIR | [/segments/data_series][/segments/data_series]<br>[/segments/details][/segments/details]<br>[/segments/list][/segments/list]<br>[/sessions/data_series][/sessions/data_series] |
{: .reset-td-br-1 .reset-td-br-2}

## Événements personnalisés

| Méthode | Points de terminaison                                                            |
| ------- | -------------------------------------------------------------------------------- |
| OBTENIR | [/events/data_series][/events/data_series]<br>[/events/list][/events/list] |
{: .reset-td-br-1 .reset-td-br-2}

## Blocs de contenu

| Méthode | Points de terminaison                                                                                      |
| ------- | ---------------------------------------------------------------------------------------------------------- |
| POSTER  | [/content_blocks/create][/content_blocks/create]<br>[/content_blocks/update][/content_blocks/update] |
| OBTENIR | [/content_blocks/info][/content_blocks/info]<br>[/content_blocks/liste][/content_blocks/list]        |
{: .reset-td-br-1 .reset-td-br-2}

## KPI

| Méthode | Points de terminaison                                                                                                                                                                                                                      |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| OBTENIR | [/kpi/dau/data_series][/kpi/dau/data_series]<br>[/kpi/mau/data_series][/kpi/mau/data_series]<br>[/kpi/new_users/data_series][/kpi/new_users/data_series]<br>[/kpi/uninstalls/data_series][/kpi/uninstalls/data_series] |
{: .reset-td-br-1 .reset-td-br-2}

## Flux d'actualité

| Méthode | Points de terminaison                                                                                            |
| ------- | ---------------------------------------------------------------------------------------------------------------- |
| OBTENIR | [/feed/data_series][/feed/data_series]<br>[/feed/details][/feed/details]<br>[/feed/list][/feed/list] |
{: .reset-td-br-1 .reset-td-br-2}

## SMS

| Méthode | Points de terminaison                                                       |
| ------- | --------------------------------------------------------------------------- |
| POSTER  | [/fr/sms/invalid_phone_numbers/remove][/sms/invalid_phone_numbers/remove] |
| OBTENIR | [/sms/invalid_phone_number][/sms/invalid_phone_numbers]                   |
{: .reset-td-br-1 .reset-td-br-2}

## Achats

| Méthode | Points de terminaison                                 |
| ------- | ----------------------------------------------------- |
| OBTENIR | [/fr/purchases/product_list][/purchases/product_list] |
{: .reset-td-br-1 .reset-td-br-2}


<!--- Links for user data --->


<!--- Links for send messages --->


<!--- Links for scheduled messages --->


<!--- Links for subscription groups --->


<!--- Links for email and email templates ---->


<!--- Links for campaigns --->


<!--- Links for Canvas --->


<!--- Links for segments --->


<!--- Links for custom events --->


<!--- Links for Content Blocks --->


<!--- Links for KPIs --->


<!--- Links for News Feed --->


<!--- Links for SMS --->


<!--- Links for purchases --->
[/users/alias/new]: {{site.baseurl}}/api/endpoints/user_data/post_user_alias/
[/users/delete]: {{site.baseurl}}/api/endpoints/user_data/post_user_delete/
[/users/identify]: {{site.baseurl}}/api/endpoints/user_data/post_user_identify/
[/users/track]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[/users/external_ids/rename]: {{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/
[/users/external_ids/remove]: {{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove/
[/users/export/ids]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/
[/users/export/segment]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/
[/users/export/global_control_group]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/
[/sends/id/create]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/
[/messages/send]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/
[/transactional/v1/campaigns/{{CAMPAIGN_ID}}/send]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message/
[/campaigns/trigger/send]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/
[/canvas/trigger/send]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/
[/campaigns/trigger/schedule/create]: {{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/
[/campaigns/trigger/schedule/delete]: {{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/
[/campaigns/trigger/schedule/update]: {{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns/
[/canvas/trigger/schedule/create]: {{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/
[/canvas/trigger/schedule/delete]: {{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases/
[/canvas/trigger/schedule/update]: {{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/
[/messages/schedule/create]: {{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages/
[/messages/schedule/delete]: {{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages/
[/messages/schedule/update]: {{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages/
[/messages/scheduled_broadcasts]: {{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled/
[/subscription/status/set]: {{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/
[/subscription/status/get]: {{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/
[/subscription/user/status]: {{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/
[/email/blacklist]: {{site.baseurl}}/api/endpoints/email/post_blacklist/
[/email/bounce/remove]: {{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces/
[/email/spam/remove]: {{site.baseurl}}/api/endpoints/email/post_remove_spam/
[/email/status]: {{site.baseurl}}/api/endpoints/email/post_email_subscription_status/
[/templates/email/create]: {{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/
[/templates/email/update]: {{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/
[/email/hard_bounces]: {{site.baseurl}}/api/endpoints/email/get_list_hard_bounces/
[/email/unsubscribes]: {{site.baseurl}}/api/endpoints/email/get_query_unsubscribed_email_addresses/
[/templates/email/info]: {{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information/
[/templates/email/list]: {{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/
[/campaigns/data_series]: {{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/
[/campaigns/details]: {{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/
[/campaigns/list]: {{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/
[/sends/data_series]: {{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/
[/canvas/data_series]: {{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/
[/canvas/data_summary]: {{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary/
[/canvas/details]: {{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/
[/canvas/list]: {{site.baseurl}}/api/endpoints/export/canvas/get_canvases/
[/segments/data_series]: {{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics/
[/segments/details]: {{site.baseurl}}/api/endpoints/export/segments/get_segment_details/
[/segments/list]: {{site.baseurl}}/api/endpoints/export/segments/get_segment/
[/sessions/data_series]: {{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics/
[/events/data_series]: {{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics/
[/events/list]: {{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events/
[/content_blocks/create]: {{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/
[/content_blocks/update]: {{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/
[/content_blocks/info]: {{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/
[/content_blocks/list]: {{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/
[/kpi/dau/data_series]: {{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date/
[/kpi/mau/data_series]: {{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days/
[/kpi/new_users/data_series]: {{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date/
[/kpi/uninstalls/data_series]: {{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date/
[/feed/data_series]: {{site.baseurl}}/api/endpoints/export/news_feed/get_news_feed_card_analytics/
[/feed/details]: {{site.baseurl}}/api/endpoints/export/news_feed/get_news_feed_card_details/
[/feed/list]: {{site.baseurl}}/api/endpoints/export/news_feed/get_news_feed_cards/
[/sms/invalid_phone_numbers/remove]: {{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers/
[/sms/invalid_phone_numbers]: {{site.baseurl}}/api/endpoints/sms/get_query_invalid_numbers/
[/purchases/product_list]: {{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/