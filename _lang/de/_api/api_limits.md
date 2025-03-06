---
nav_title: Raten-Grenzwerte
article_title: API-Raten-Grenzwerte
page_order: 4.5
description: "Dieser Referenzartikel befasst sich mit den API-Grenzwerten für die Braze API-Infrastruktur."
page_type: reference

---

# Preisgrenzen

> Die API-Infrastruktur von Braze ist so konzipiert, dass sie große Datenmengen für unseren Kundenstamm verarbeiten kann. Zu diesem Zweck setzen wir API-Ratenlimits pro Arbeitsbereich durch.

Ein Ratenlimit ist die Anzahl der Anfragen, die die API in einer bestimmten Zeitspanne erhalten kann. Viele Last-basierte Denial-of-Service-Vorfälle in großen Systemen sind unbeabsichtigt - verursacht durch Fehler in der Software oder den Konfigurationen - und nicht durch böswillige Angriffe. Ratenbeschränkungen sorgen dafür, dass unseren Kunden durch solche Fehler keine Braze API-Ressourcen vorenthalten werden. Wenn in einem bestimmten Zeitrahmen zu viele Anfragen gesendet werden, erhalten Sie möglicherweise Fehlerantworten mit dem Statuscode `429`, was bedeutet, dass das Ratenlimit erreicht wurde.

{% alert warning %}
Die API-Raten können sich je nach ordnungsgemäßer Nutzung unseres Systems ändern. Wir raten zu vernünftigen Beschränkungen bei der Durchführung eines API-Aufrufs, um Schäden oder Missbrauch zu vermeiden.
{% endalert %}

## Tarifgrenzen nach Art der Anfrage

In der folgenden Tabelle sind die Standard-API-Ratenlimits für verschiedene Anfragearten aufgeführt. Diese Standardlimits können auf Anfrage erhöht werden. Wenden Sie sich für weitere Informationen an Ihren Kundenbetreuer.

{% alert note %}
Für Anfragen, die nicht in dieser Tabelle aufgeführt sind, gilt ein Standard-Limit von insgesamt 250.000 Anfragen pro Stunde.
{% endalert %}

| Anfrage Typ                                                                                                                                                                                                                                           | Standard API Rate Limit                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [`/users/track`][10]                                                                                                                                                                                                                                   | **Anfragen:** 3.000 Anfragen pro drei Sekunden.<br><br>**Batching:** 75 Ereignisse, 75 Käufe und 75 Attribute pro API-Anfrage. Weitere Informationen finden Sie unter [Stapeln von User Track-Anfragen](#batch-user-track).<br><br>**Grenzwerte für monatlich aktive Nutzer CY 24-25:** siehe [Grenzwerte für monatlich aktive Nutzer CY 24-25]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#monthly-active-users-cy-24-25) |
| [`/users/export/ids`][11]                                                                                                                                                                                                                              | **Wenn Sie am oder nach dem 22\. August 2024 an Bord gegangen sind:** 250 Anfragen pro Minute. <br><br> **Wenn Sie vor dem 22\. August 2024 an Bord gegangen sind:** 2.500 Anfragen pro Minute.                                                                                                                                                                   |
| [`/users/delete`][12]<br>[`/users/alias/new`][13]<br>[`/users/alias/update`][45]<br>[`/users/identify`][14]<br>[`/users/merge`][44]                                                                                                                    | 20.000 Anfragen pro Minute, verteilt auf die Endpunkte.                                                                                                                                  |
| [`/users/external_id/rename`][20]                                                                                                                                                                                                                      | 1.000 Anfragen pro Minute.                                                                                                                                                                 |
| [`/users/external_id/remove`][21]                                                                                                                                                                                                                      | 1.000 Anfragen pro Minute.                                                                                                                                                                 |
| [`/events/list`][15]                                                                                                                                                                                                                                   | 1.000 Anfragen pro Stunde, gemeinsam mit dem Endpunkt `/purchases/product_list`.                                                                                                               |
| [`/purchases/product_list`][16]                                                                                                                                                                                                                        | 1.000 Anfragen pro Stunde, gemeinsam mit dem Endpunkt `/events/list`.                                                                                                                          |
| [`/campaigns/data_series`][17.3]                                                                                                                                                                                                                       | 50.000 Anfragen pro Minute.                                                                                                                                                                |
| [`/messages/send`][17]<br>[`/campaigns/trigger/send`][17.1]<br>[`/canvas/trigger/send`][17.2]                                                                                                                                                          | 250 Anfragen pro Minute für Rundrufe (wenn Sie nur ein Segment oder Connected Audience angeben). Ansonsten 250.000 Anfragen pro Stunde, die auf die Endpunkte verteilt werden.                     |
| [`/sends/id/create`][18]                                                                                                                                                                                                                               | 100 Anfragen pro Tag.                                                                                                                                                                      |
| [`/subscription/status/set`][19]                                                                                                                                                                                                                       | 5.000 Anfragen pro Minute.                                                                                                                                                                 |
| [`/preference_center/v1/{preferenceCenterExternalId}/url/{userId}`][26]<br>[`/preference_center/v1/list`][27]<br>[`/preference_center/v1/{preferenceCenterExternalId}`][28]                                                                            | 1.000 Anfragen pro Minute, pro Arbeitsbereich.                                                                                                                                                  |
| [`/preference_center/v1`][29]<br>[`/preference_center/v1/{preferenceCenterExternalId}`][30]                                                                                                                                                            | 10 Anfragen pro Minute, pro Arbeitsbereich.                                                                                                                                                     |
| [`/catalogs/{catalog_name}`][31]<br>[`/catalogs`][32]<br>[`/catalogs`][33]                                                                                                                                                                             | 50 Anfragen pro Minute zwischen den Endpunkten.                                                                                                                                       |
| [`/catalogs/{catalog_name}/items`][34]<br>[`/catalogs/{catalog_name}/items`][35]<br>[`/catalogs/{catalog_name}/items`][36]                                                                                                                             | 16.000 Anfragen pro Minute, verteilt auf die Endpunkte.                                                                                                                                   |
| [`/catalogs/{catalog_name}/items/{item_id}`][37]<br>[`/catalogs/{catalog_name}/items/{item_id}`][38]<br>[`/catalogs/{catalog_name}/items`][39]<br>[`/catalogs/{catalog_name}/items/{item_id}`][40]<br>[`/catalogs/{catalog_name}/items/{item_id}`][41] | 50 Anfragen pro Minute zwischen den Endpunkten.                                                                                                                                       |
| [`/scim/v2/Users/{id}`][22]<br>[`/scim/v2/Users?filter={userName@example.com}`][43]<br>[`/scim/v2/Users/{id}`][25]<br>[`/scim/v2/Users/{id}}`][24]<br>[`/scim/v2/Users/`][23]                                                                          | 5.000 Anfragen pro Tag, pro Unternehmen, verteilt auf die Endpunkte.                                                                                                                         |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

<!-- Add during CDI endpoints GA
| [`/cdi/integrations`][46] | 50 requests per minute. |
| [`/cdi/integrations/{integration_id}/sync`][47] | 20 requests per minute. |
| [`/cdi/integrations/{integration_id}/job_sync_status`][48] | 100 requests per minute. |
-->

## Batching von API-Anfragen

Die Braze-APIs sind für die Unterstützung von Batching ausgelegt. Mit Batching kann Braze so viele Daten wie möglich in einem einzigen API-Aufruf aufnehmen, so dass Sie nicht viele API-Aufrufe tätigen müssen. Für Braze ist es effizienter, Daten in Stapeln zu verarbeiten, als sie einzeln aufzurufen. Die Bearbeitung von 1.000 gebündelten API-Aufrufen erfordert zum Beispiel weniger Ressourcen als die Bearbeitung von 75.000 einzelnen Aufrufen. Batching ist extrem wichtig für jede Anwendung, die mehr als 75.000 Anrufe pro Stunde erfordert.

{% alert note %}
Erhöhungen der REST-API-Raten werden je nach Bedarf für Kunden, die die API-Batching-Funktionen nutzen, in Betracht gezogen.
{% endalert %}

### Stapeln von User Track-Anfragen {#batch-user-track}

Jede `/users/track` Anfrage kann bis zu 75 Ereignisobjekte, 75 Attributobjekte und 75 Kaufobjekte enthalten. Jedes Objekt (Ereignis-, Attribut- und Kauf-Arrays) kann jeweils einen Benutzer aktualisieren. Insgesamt bedeutet dies, dass maximal 225 Benutzer in einem einzigen Anruf aktualisiert werden können. Darüber hinaus kann ein einzelnes Benutzerprofil durch mehrere Objekte aktualisiert werden.

Anfragen, die an diesen Endpunkt gerichtet werden, werden in der Regel in dieser Reihenfolge bearbeitet:

1. Attribute
2. Ereignisse
3. Käufe

### Batching von Messaging-Endpunktanfragen

Eine einzelne Anfrage an die [Messaging-Endpunkte][1] kann einen der folgenden Punkte erreichen:

- Bis zu 50 spezifische `external_ids`, jeweils mit individuellen Nachrichtenparametern
- Ein im Braze Dashboard erstelltes Segment beliebiger Größe, das durch seine `segment_id`
- Benutzer, die zusätzlichen Publikumsfiltern beliebiger Größe entsprechen, die in der Anfrage als [verbundenes Publikumsobjekt][2] definiert sind

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

## Überwachung Ihrer Tarifgrenzen

Jede einzelne API-Anfrage, die an Braze gesendet wird, gibt die folgenden Informationen in den Antwort-Headern zurück:

| Kopfzeile Name             | Beschreibung                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------- |
| `X-RateLimit-Limit`     | Die maximale Anzahl von Anfragen, die Sie in einem bestimmten Intervall stellen können (Ihr Ratenlimit). |
| `X-RateLimit-Remaining` | Die Anzahl der verbleibenden Anfragen im aktuellen Ratenlimitfenster.                          |
| `X-RateLimit-Reset`     | Die Zeit, zu der das aktuelle Ratenbegrenzungsfenster zurückgesetzt wird, in UTC-Epochen-Sekunden.                |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Diese Informationen sind absichtlich in der Kopfzeile der Antwort auf die API-Anfrage enthalten und nicht im Braze Dashboard. Dadurch kann Ihr System besser in Echtzeit reagieren, während Sie mit unserer API interagieren. Wenn zum Beispiel der Wert von `X-RateLimit-Remaining` unter einen bestimmten Schwellenwert fällt, sollten Sie den Versand verlangsamen, um sicherzustellen, dass alle Transaktions-E-Mails verschickt werden. Oder, wenn sie Null erreicht, möchten Sie vielleicht alle Sendungen unterbrechen, bis die in `X-RateLimit-Reset` angegebene Zeit abgelaufen ist.

{% alert note %}
Die HTTP-Header werden in Kleinbuchstaben zurückgegeben. Dieses Verhalten steht im Einklang mit dem HTTP/2-Protokoll, das vorschreibt, dass alle Header-Feldnamen klein geschrieben werden müssen. Dies unterscheidet sich von HTTP/1.X, wo bei den Headernamen die Groß- und Kleinschreibung nicht beachtet wurde, diese aber üblicherweise in verschiedenen Großbuchstaben geschrieben wurden.
{% endalert %}

Wenn Sie Fragen zu API-Limits haben, wenden Sie sich an Ihren Customer Success Manager oder eröffnen Sie ein [Support-Ticket][support].

### Optimale Verzögerung zwischen Endpunkten

{% alert note %}
Wir empfehlen Ihnen, eine 5-minütige Verzögerung zwischen aufeinanderfolgenden Endpunktaufrufen einzuplanen, um Fehler zu vermeiden.
{% endalert %}

Das Verständnis der optimalen Verzögerung zwischen den Endpunkten ist entscheidend, wenn Sie die Braze-API nacheinander aufrufen. Probleme entstehen, wenn Endpunkte von der erfolgreichen Verarbeitung anderer Endpunkte abhängen und bei einem zu frühen Aufruf Fehler auftreten können. Wenn Sie zum Beispiel Benutzern über unseren `/user/alias/new` Endpunkt einen Alias zuweisen und dann diesen Alias anklicken, um ein benutzerdefiniertes Ereignis über unseren `/users/track` Endpunkt zu senden, wie lange sollten Sie dann warten?

Unter normalen Bedingungen beträgt die Zeit, in der unsere Daten konsistent sind, 10-100ms (1/10 einer Sekunde). Es kann jedoch vorkommen, dass es länger dauert, bis diese Konsistenz eintritt. Daher empfehlen wir Ihnen, eine 5-minütige Verzögerung zwischen den folgenden Aufrufen einzuplanen, um die Fehlerwahrscheinlichkeit zu minimieren.

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
[47]: {{site.baseurl}}/api/endpoints/cdi/job_sync/
[48]: {{site.baseurl}}/api/endpoints/cdi/job_sync_status/
