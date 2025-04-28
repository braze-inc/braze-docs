---
nav_title: Rate-Limits
article_title: API Rate-Limits
page_order: 4.5
description: "Dieser Artikel referenziert die API Rate-Limits für die Braze API Infrastruktur."
page_type: reference

---

# Rate-Limits

> Die API-Infrastruktur von Braze ist darauf ausgelegt, große Datenmengen für unsere Kund:innen zu verarbeiten. Zu diesem Zweck setzen wir Rate-Limits für APIs pro Workspace durch.

Ein Rate-Limit ist die Anzahl der Anfragen, die die API in einem bestimmten Zeitraum erhalten kann. Viele auf Last basierende Denial-of-Service-Vorfälle in großen Systemen sind unbeabsichtigt - sie werden durch Fehler in der Software oder den Konfigurationen verursacht und nicht durch böswillige Angriffe. Rate-Limits sorgen dafür, dass unseren Kund:innen durch solche Fehler keine Ressourcen der Braze APIs vorenthalten werden. Wenn in einem bestimmten Zeitrahmen zu viele Anfragen gesendet werden, erhalten Sie möglicherweise Fehlerantworten mit einem Fehlercode von `429`, der anzeigt, dass das Rate-Limit erreicht wurde.

{% alert warning %}
Die Rate-Limits für APIs können sich je nach Nutzung unseres Systems ändern. Wir raten zu vernünftigen Grenzen bei API-Aufrufen, um Schäden oder Missbrauch zu vermeiden.
{% endalert %}

## Rate-Limits nach Art der Anfrage

Im Folgenden finden Sie die Standard API Rate-Limits für verschiedene Arten von Anfragen. Diese Standard-Limits können auf Anfrage erhöht werden. Wenden Sie sich an Ihren Customer-Success-Manager:in für weitere Informationen.

### Anfragen mit unterschiedlichen Rate-Limits

| Anfrage Typ                                                                                                                                                                                                                                           | Standard API Rate-Limiting                                                                                                                                                                                                                                                                                                                                                                    |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`/users/track`][10]                                                                                                                                                                                                                                   | **Anfragen:** 3.000 Anfragen pro drei Sekunden.<br><br>**Batching:** 75 Ereignisse, 75 Käufe und 75 Attribute pro API-Anfrage. Weitere Informationen finden Sie unter [Batching von Nutzer:innen Tracking Anfragen](#batch-user-track).<br><br>**Grenzwerte für monatlich aktive Nutzer:innen CY 24-25:** siehe [Grenzwerte für monatlich aktive Nutzer:innen CY 24-25]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#monthly-active-users-cy-24-25) |
| [`/users/export/ids`][11]                                                                                                                                                                                                                              | **Wenn Sie am oder nach dem 22\. August 2024 onboarding waren:** 250 Anfragen pro Minute. <br><br> **Wenn Sie vor dem 22\. August 2024 onboarding waren:** 2.500 Anfragen pro Minute.                                                                                                                                                                                                                               |
| [`/users/delete`][12]<br>[`/users/alias/new`][13]<br>[`/users/alias/update`][45]<br>[`/users/identify`][14]<br>[`/users/merge`][44]                                                                                                                    | 20.000 Anfragen pro Minute, verteilt auf die Endpunkte.                                                                                                                                                                                                                                                                                                                                 |
| [`/users/external_id/rename`][20]                                                                                                                                                                                                                      | 1.000 Anfragen pro Minute.                                                                                                                                                                                                                                                                                                                                                                |
| [`/users/external_id/remove`][21]                                                                                                                                                                                                                      | 1.000 Anfragen pro Minute.                                                                                                                                                                                                                                                                                                                                                                |
| [`/events/list`][15]                                                                                                                                                                                                                                   | 1.000 Anfragen pro Stunde, gemeinsam mit dem Endpunkt `/purchases/product_list`.                                                                                                                                                                                                                                                                                                              |
| [`/purchases/product_list`][16]                                                                                                                                                                                                                        | 1.000 Anfragen pro Stunde, gemeinsam mit dem Endpunkt `/events/list`.                                                                                                                                                                                                                                                                                                                         |
| [`/campaigns/data_series`][17.3]                                                                                                                                                                                                                       | 50.000 Anfragen pro Minute.                                                                                                                                                                                                                                                                                                                                                               |
| [`/messages/send`][17]<br>[`/campaigns/trigger/send`][17.1]<br>[`/canvas/trigger/send`][17.2]                                                                                                                                                          | 250 Anfragen pro Minute für Broadcast-Anrufe (wenn nur ein Segment oder eine Connected Audience angegeben wird). Andernfalls werden 250.000 Anfragen pro Stunde auf die Endpunkte verteilt.                                                                                                                                                                                                                    |
| [`/sends/id/create`][18]                                                                                                                                                                                                                               | 100 Anfragen pro Tag.                                                                                                                                                                                                                                                                                                                                                                     |
| [`/subscription/status/set`][19]                                                                                                                                                                                                                       | 5.000 Anfragen pro Minute.                                                                                                                                                                                                                                                                                                                                                                |
| [`/preference_center/v1/{preferenceCenterExternalId}/url/{userId}`][26]<br>[`/preference_center/v1/list`][27]<br>[`/preference_center/v1/{preferenceCenterExternalId}`][28]                                                                            | 1.000 Anfragen pro Minute.                                                                                                                                                                                                                                                                                                                                                 |
| [`/preference_center/v1`][29]<br>[`/preference_center/v1/{preferenceCenterExternalId}`][30]                                                                                                                                                            | 10 Anfragen pro Minute.                                                                                                                                                                                                                                                                                                                                                    |
| [`/catalogs/{catalog_name}`][31]<br>[`/catalogs`][32]<br>[`/catalogs`][33]                                                                                                                                                                             | 50 Anfragen pro Minute, die von den Endpunkten gemeinsam genutzt werden.                                                                                                                                                                                                                                                                                                                                      |
| [`/catalogs/{catalog_name}/items`][34]<br>[`/catalogs/{catalog_name}/items`][35]<br>[`/catalogs/{catalog_name}/items`][36]                                                                                                                             | 16.000 Anfragen pro Minute, verteilt auf die Endpunkte.                                                                                                                                                                                                                                                                                                                                  |
| [`/catalogs/{catalog_name}/items/{item_id}`][37]<br>[`/catalogs/{catalog_name}/items/{item_id}`][38]<br>[`/catalogs/{catalog_name}/items`][39]<br>[`/catalogs/{catalog_name}/items/{item_id}`][40]<br>[`/catalogs/{catalog_name}/items/{item_id}`][41] | 50 Anfragen pro Minute, die von den Endpunkten gemeinsam genutzt werden.                                                                                                                                                                                                                                                                                                                                      |
| [`/catalogs/{catalog_name}/fields/{field_name}`][51]<br>[`/catalogs/{catalog_name}/fields`][52]<br>[`/catalogs/{catalog_name}/selections/{selection_name}`][49]<br>[`/catalogs/{catalog_name}/selections`][50] | 50 Anfragen pro Minute, die von den Endpunkten gemeinsam genutzt werden. |
| [`/scim/v2/Users/{id}`][22]<br>[`/scim/v2/Users?filter={userName@example.com}`][43]<br>[`/scim/v2/Users/{id}`][25]<br>[`/scim/v2/Users/{id}}`][24]<br>[`/scim/v2/Users/`][23]                                                                          | 5.000 Anfragen pro Tag, pro Unternehmen, aufgeteilt auf die Endpunkte.                                                                                                                                                                                                                                                                                                                        |
| [`/cdi/integrations`][46]                                                                                                                                                                                                                              | 50 Anfragen pro Minute.                                                                                                                                                                                                                                                                                                                                                                   |
| [`/cdi/integrations/{integration_id}/sync`][47]                                                                                                                                                                                                        | 20 Anfragen pro Minute.                                                                                                                                                                                                                                                                                                                                                                   |
| [`/cdi/integrations/{integration_id}/job_sync_status`][48]                                                                                                                                                                                             | 100 Anfragen pro Minute.                                                                                                                                                                                                                                                                                                                                                                  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Anfragen mit gemeinsamen Rate-Limits

Für die folgenden Anfragen gilt ein Rate-Limits von 250.000 Anfragen pro Stunde, das sie sich teilen.

- [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details)
- [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns)
- [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/)
- [`/campaigns/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/)
- [`/campaigns/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns/)
- [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/)
- [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary/)
- [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/)
- [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/)
- [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/)
- [`/canvas/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases/)
- [`/canvas/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/)
- [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/)
- [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/)
- [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/)
- [`/content_blocks/update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/)
- [`/email/blocklist`]({{site.baseurl}}/api/endpoints/email/post_blocklist/)
- [`/email/blacklist`]({{site.baseurl}}/api/endpoints/email/post_blacklist/)
- [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/bounce/remove)
- [`/email/hard_bounces`]({{site.baseurl}}/api/endpoints/email/get_list_hard_bounces/)
- [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam/)
- [`/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status/)
- [`/email/unsubscribes`]({{site.baseurl}}/api/endpoints/email/get_query_unsubscribed_email_addresses/)
- [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics/)
- [`/feed/data_series`]({{site.baseurl}}/api/endpoints/export/news_feed/get_news_feed_card_analytics/)
- [`/feed/details`]({{site.baseurl}}/api/endpoints/export/news_feed/get_news_feed_card_details/)
- [`/feed/list`]({{site.baseurl}}/api/endpoints/export/news_feed/get_news_feed_cards/)
- [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date/)
- [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days/)
- [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date/)
- [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date/)
- [`/messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start)
- [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update/)
- [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages/)
- [`/messages/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages/)
- [`/messages/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages/)
- [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled/)
- [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics/)
- [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/)
- [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment/)
- [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/)
- [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics/)
- [`/sms/invalid_phone_numbers`]({{site.baseurl}}/api/endpoints/sms/get_query_invalid_numbers/)
- [`/sms/invalid_phone_numbers/remove`]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers/)
- [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/)
- [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/)
- [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/)
- [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information/)
- [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/)
- [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/)
- [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/)
- [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)

## Batching von API-Anfragen

Die Braze APIs unterstützen die Stapelverarbeitung. Mit Batching kann Braze so viele Daten wie möglich in einem einzigen API-Aufruf aufnehmen, so dass Sie nicht viele API-Aufrufe tätigen müssen. Für Braze ist es effizienter, Daten in Stapeln zu verarbeiten, als Daten in einem Aufruf zu verarbeiten. Die Verarbeitung von 1.000 gebündelten API-Aufrufen erfordert zum Beispiel weniger Ressourcen als die Verarbeitung von 75.000 einzelnen Aufrufen. Batching ist extrem wichtig für jede Anwendung, die mehr als 75.000 Anrufe pro Stunde erfordert.

{% alert note %}
REST API Rate-Limits werden je nach Bedarf für Kund:inen, die die API-Batching-Funktionen nutzen, angehoben.
{% endalert %}

### Batching von Anfragen für den Endpunkt Tracking Nutzer:innen {#batch-user-track}

Jede `/users/track` Anfrage kann bis zu 75 Event-Objekte, 75 Attribut-Objekte und 75 Kauf-Objekte enthalten. Jedes Objekt (Ereignis-, Attribut- und Kauf-Arrays) kann jeweils eine:n Nutzer:in aktualisieren. Insgesamt können so bis zu 225 Nutzer:innen mit einem einzigen Aufruf aktualisiert werden. Darüber hinaus kann ein einzelnes Nutzerprofil durch mehrere Objekte aktualisiert werden.

Anfragen, die an diesen Endpunkt gerichtet werden, werden in der Regel in dieser Reihenfolge bearbeitet:

1. Attribute
2. Events
3. Käufe

### Batching von Messaging Endpunkt Anfragen

Eine einzelne Anfrage an die [Messaging Endpunkte][1] kann einen der folgenden Punkte erreichen:

- Bis zu 50 spezifische `external_ids`, jeweils mit individuellen Nachrichtenparametern
- Ein im Braze-Dashboard erstelltes Segment beliebiger Größe, das durch seine `segment_id` angegeben wird
- Nutzer:innen, die zusätzlichen Zielgruppen-Filtern beliebiger Größe entsprechen, die in der Anfrage als [verbundenes Zielgruppen-Objekt][2] definiert sind

### Beispiel einer Batch-Anfrage

Das folgende Beispiel verwendet `external_id`, um einen API-Aufruf für E-Mail und SMS zu tätigen.

```
curl --location --request POST 'https://rest.iad-01.braze.com/v2/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_groups":[
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "external_ids":["example-user","example1@email.com"]
    },
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "external_ids":["example-user","example1@email.com"]
    }
  ]
}
```

## Überwachung Ihrer Rate-Limits

Jede einzelne API-Anfrage, die an Braze gesendet wird, gibt die folgenden Informationen in den Antwort-Headern zurück:

| Kopfzeile Name             | Beschreibung                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------- |
| `X-RateLimit-Limit`     | Die maximale Anzahl der Anfragen, die Sie in einem bestimmten Intervall stellen können (Ihr Rate-Limit). |
| `X-RateLimit-Remaining` | Die Anzahl der verbleibenden Anfragen im aktuellen Rate-Limits-Fenster.                          |
| `X-RateLimit-Reset`     | Die Zeit, zu der das aktuelle Rate-Limits-Fenster zurückgesetzt wird, in UTC-Epochen-Sekunden.                |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Diese Informationen sind absichtlich in der Kopfzeile der Antwort auf die API-Anfrage und nicht im Braze-Dashboard enthalten. Dies erlaubt es Ihrem System, besser in Echtzeit zu reagieren, während Sie mit unserer API interagieren. Wenn zum Beispiel der Wert `X-RateLimit-Remaining` unter einen bestimmten Schwellenwert fällt, sollten Sie den Versand verlangsamen, um sicherzustellen, dass alle Transaktions-E-Mails versendet werden. Oder, wenn sie Null erreicht, möchten Sie vielleicht alle Sendungen unterbrechen, bis die in `X-RateLimit-Reset` angegebene Zeit abgelaufen ist.

{% alert note %}
Die HTTP-Header werden in Kleinbuchstaben zurückgegeben. Dieses Verhalten steht im Einklang mit dem HTTP/2-Protokoll, das vorschreibt, dass alle Header-Feldnamen klein geschrieben werden müssen. Dies unterscheidet sich von HTTP/1.X, wo bei den Headernamen die Groß- und Kleinschreibung nicht beachtet wurde, diese aber üblicherweise in verschiedenen Großbuchstaben geschrieben wurden.
{% endalert %}

Wenn Sie Fragen zu API-Limits haben, wenden Sie sich an Ihren Customer-Success-Manager oder öffnen Sie ein [Support-Ticket][support].

{% alert tip %}
Sie können das [Dashboard zur API-Nutzung]({{site.baseurl}}/user_guide/analytics/dashboard/api_usage_dashboard/) verwenden, um den eingehenden Datenverkehr mit Ihren Rate-Limits zu vergleichen.
{% endalert %}

### Optimale Verzögerung zwischen Endpunkten

{% alert note %}
Wir empfehlen Ihnen, eine 5-minütige Verzögerung zwischen aufeinanderfolgenden Aufrufen des Endpunkts zuzulassen, um Fehler zu minimieren.
{% endalert %}

Das Verständnis für die optimale Verzögerung zwischen den Endpunkten ist entscheidend, wenn Sie die Braze APIs nacheinander aufrufen. Probleme entstehen, wenn Endpunkte von der erfolgreichen Verarbeitung anderer Endpunkte abhängen und bei einem zu frühen Aufruf Fehler auftreten können. Wenn Sie zum Beispiel Nutzern:innen über unseren Endpunkt `/user/alias/new` einen Alias zuweisen und dann diesen Alias verwenden, um ein angepasstes Event über unseren Endpunkt `/users/track` zu senden, wie lange sollten Sie dann warten?

Unter normalen Bedingungen beträgt die Zeit, in der unsere Daten konsistent sind, 10-100ms (1/10 einer Sekunde). Es kann jedoch vorkommen, dass es länger dauert, bis diese Konsistenz eintritt. Daher empfehlen wir Ihnen, eine 5-minütige Verzögerung zwischen den nachfolgenden Aufrufen zuzulassen, um die Fehlerwahrscheinlichkeit zu minimieren.

[1]: {{site.baseurl}}/api/endpoints/messaging/
[2]: {{site.baseurl}}/api/objects_filters/connected_audience/
[support]: {{site.baseurl}}/braze_support/
[10]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[11]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/
[12]: {{site.baseurl}}/api/endpoints/user_data/post_user_delete/
[13]: {{site.baseurl}}/api/endpoints/user_data/post_user_alias/
[14]: {{site.baseurl}}/api/endpoints/user_data/post_user_identify/
[15]: {{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events/
[16]: {{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/
[17]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/
[17.1]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/
[17.2]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/
[17.3]: {{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/
[18]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/
[19]: {{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/
[20]: {{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/
[21]: {{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove/
[22]: {{site.baseurl}}/get_see_user_account_information/
[23]: {{site.baseurl}}/post_create_user_account/
[24]: {{site.baseurl}}/delete_existing_dashboard_user/
[25]: {{site.baseurl}}/post_update_existing_user_account/
[26]: {{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center/
[27]: {{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center/
[28]: {{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/
[29]: {{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center/
[30]: {{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center/
[31]: {{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog/
[32]: {{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/
[33]: {{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/
[34]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk/
[35]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk/
[36]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk/
[37]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item/
[38]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/
[39]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/
[40]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/
[41]: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item/
[43]: {{site.baseurl}}/get_search_existing_dashboard_user_email/
[44]: {{site.baseurl}}/api/endpoints/user_data/post_users_merge/
[45]: {{site.baseurl}}/api/endpoints/user_data/post_users_alias_update/
[46]: {{site.baseurl}}/api/endpoints/cdi/get_integration_list/
[47]: {{site.baseurl}}/api/endpoints/cdi/get_job_sync_status/
[48]: {{site.baseurl}}/api/endpoints/cdi/post_job_sync/
[49]: {{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection
[50]: {{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections
[51]: {{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field
[52]: {{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields