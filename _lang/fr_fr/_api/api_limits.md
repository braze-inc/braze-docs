---
nav_title: Limites de débit
article_title: Limites de débit de l’API
page_order: 4.5
description: "Cet article de référence couvre les limites de débit de l’API pour l’infrastructure API Braze."
page_type: reference

---

# Limites de débit

> L’infrastructure API Braze est conçue pour gérer des volumes élevés de données sur l’ensemble de notre base de clients. À cette fin, nous appliquons des limites de débit à l’API par espace de travail.

Une limite de débit correspond au nombre de demandes que l’API peut recevoir sur une période donnée. De nombreux incidents de déni de service basés sur la charge dans les grands systèmes sont involontaires, causés par des erreurs dans les logiciels ou les configurations, et non par des attaques malveillantes. Les limites de débit permettent de vérifier que de telles erreurs ne privent pas nos clients des ressources de l'API de Braze. Si trop de demandes sont envoyées dans un délai donné, vous risquez de recevoir des réponses d’erreur avec un code de statut de `429`, qui indique que la limite de débit a été atteinte.

{% alert warning %}
Les limites de débit de l’API sont sujettes à modification en fonction de l’utilisation propre à notre système. Nous encourageons des limites raisonnables lors de l’appel d’API afin d’éviter tout dommage ou toute mauvaise utilisation.
{% endalert %}

## Limites de débit par type de demande

Reportez-vous à ce qui suit pour connaître les limites de débit par défaut de l'API pour différents types de demandes. Ces limites par défaut peuvent être augmentées sur demande. Contactez votre gestionnaire du succès des clients pour plus d’informations.

### Demandes avec différentes limites de débit

| Type de demande                                                                                                                                                                                                                                           | Limite de débit par défaut de l’API                                                                                                                                                                                                                                                                                                                                                                    |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`/users/track`][10]                                                                                                                                                                                                                                   | **Demandes :** 3 000 demandes par trois secondes.<br><br>**Traitement par lot :** 75 événements, 75 achats et 75 attributs par requête d'API. Pour en savoir plus, consultez la rubrique [Mise en lot des demandes de suivi des utilisateurs](#batch-user-track).<br><br>**Limites pour les utilisateurs actifs par mois CY 24-25 :** voir [Limites pour les utilisateurs actifs par mois CY 24-25]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#monthly-active-users-cy-24-25) |
| [`/users/export/ids`][11]                                                                                                                                                                                                                              | **Si vous avez embarqué à partir du 22 août 2024 :** 250 demandes par minute. <br><br> **Si vous avez embarqué avant le 22 août 2024 :** 2 500 demandes par minute.                                                                                                                                                                                                                               |
| [`/users/delete`][12]<br>[`/users/alias/new`][13]<br>[`/users/alias/update`][45]<br>[`/users/identify`][14]<br>[`/users/merge`][44]                                                                                                                    | 20 000 demandes par minute, partagées entre les endpoints.                                                                                                                                                                                                                                                                                                                                 |
| [`/users/external_id/rename`][20]                                                                                                                                                                                                                      | 1 000 demandes par minute.                                                                                                                                                                                                                                                                                                                                                                |
| [`/users/external_id/remove`][21]                                                                                                                                                                                                                      | 1 000 demandes par minute.                                                                                                                                                                                                                                                                                                                                                                |
| [`/events/list`][15]                                                                                                                                                                                                                                   | 1 000 demandes par heure, partagées avec l’endpoint `/purchases/product_list`.                                                                                                                                                                                                                                                                                                              |
| [`/purchases/product_list`][16]                                                                                                                                                                                                                        | 1 000 demandes par heure, partagées avec l’endpoint `/events/list`.                                                                                                                                                                                                                                                                                                                         |
| [`/campaigns/data_series`][17.3]                                                                                                                                                                                                                       | 50 000 demandes par minute.                                                                                                                                                                                                                                                                                                                                                               |
| [`/messages/send`][17]<br>[`/campaigns/trigger/send`][17.1]<br>[`/canvas/trigger/send`][17.2]                                                                                                                                                          | 250 requêtes par minute pour les appels de diffusion (lorsque vous ne spécifiez qu'un segment ou une audience connectée). Sinon, 250 000 requêtes par heure réparties entre les endpoints.                                                                                                                                                                                                                    |
| [`/sends/id/create`][18]                                                                                                                                                                                                                               | 100 demandes par jour.                                                                                                                                                                                                                                                                                                                                                                     |
| [`/subscription/status/set`][19]                                                                                                                                                                                                                       | 5 000 demandes par minute.                                                                                                                                                                                                                                                                                                                                                                |
| [`/preference_center/v1/{preferenceCenterExternalId}/url/{userId}`][26]<br>[`/preference_center/v1/list`][27]<br>[`/preference_center/v1/{preferenceCenterExternalId}`][28]                                                                            | 1 000 demandes par minute.                                                                                                                                                                                                                                                                                                                                                 |
| [`/preference_center/v1`][29]<br>[`/preference_center/v1/{preferenceCenterExternalId}`][30]                                                                                                                                                            | 10 demandes par minute.                                                                                                                                                                                                                                                                                                                                                    |
| [`/catalogs/{catalog_name}`][31]<br>[`/catalogs`][32]<br>[`/catalogs`][33]                                                                                                                                                                             | 50 demandes par minute, partagées entre les endpoints.                                                                                                                                                                                                                                                                                                                                      |
| [`/catalogs/{catalog_name}/items`][34]<br>[`/catalogs/{catalog_name}/items`][35]<br>[`/catalogs/{catalog_name}/items`][36]                                                                                                                             | 16 000 requêtes par minute réparties entre les endpoints.                                                                                                                                                                                                                                                                                                                                  |
| [`/catalogs/{catalog_name}/items/{item_id}`][37]<br>[`/catalogs/{catalog_name}/items/{item_id}`][38]<br>[`/catalogs/{catalog_name}/items`][39]<br>[`/catalogs/{catalog_name}/items/{item_id}`][40]<br>[`/catalogs/{catalog_name}/items/{item_id}`][41] | 50 demandes par minute, partagées entre les endpoints.                                                                                                                                                                                                                                                                                                                                      |
| [`/catalogs/{catalog_name}/fields/{field_name}`][51]<br>[`/catalogs/{catalog_name}/fields`][52]<br>[`/catalogs/{catalog_name}/selections/{selection_name}`][49]<br>[`/catalogs/{catalog_name}/selections`][50] | 50 demandes par minute, partagées entre les endpoints. |
| [`/scim/v2/Users/{id}`][22]<br>[`/scim/v2/Users?filter={userName@example.com}`][43]<br>[`/scim/v2/Users/{id}`][25]<br>[`/scim/v2/Users/{id}}`][24]<br>[`/scim/v2/Users/`][23]                                                                          | 5 000 demandes par jour, partagées entre les endpoints.                                                                                                                                                                                                                                                                                                                        |
| [`/cdi/integrations`][46]                                                                                                                                                                                                                              | 50 demandes par minute.                                                                                                                                                                                                                                                                                                                                                                   |
| [`/cdi/integrations/{integration_id}/sync`][47]                                                                                                                                                                                                        | 20 demandes par minute.                                                                                                                                                                                                                                                                                                                                                                   |
| [`/cdi/integrations/{integration_id}/job_sync_status`][48]                                                                                                                                                                                             | 100 demandes par minute.                                                                                                                                                                                                                                                                                                                                                                  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Demandes avec limites de débit partagées

Les demandes suivantes ont une limite de débit de 250 000 demandes par heure, partagée entre elles.

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

## Traitement des demandes d’API par lot

Les API de Braze sont créées pour prendre en charge la mise en lots. Grâce au traitement par lot, Braze peut récupérer autant de données que possible en un seul appel d’API afin de limiter le nombre d’appels d’API à passer. Il est plus efficace pour Braze de traiter les données par lots que de les traiter par appel. Par exemple, la gestion de 1 000 appels d’API par lots nécessite moins de ressources que la gestion de 75 000 appels individuels. L’utilisation du traitement par lot est extrêmement importante pour les applications qui peuvent nécessiter plus de 75 000 appels par heure.

{% alert note %}
Selon les besoins des clients qui utilisent les capacités de traitement par lot de l’API, des augmentations de limite de débit API REST peuvent être envisagées.
{% endalert %}

### Demandes de mise en lots pour le point final de suivi des utilisateurs {#batch-user-track}

Chaque demande `/users/track` peut contenir jusqu’à 75 objets d’événement, 75 objets d’attributs et 75 objets d’achats. Chaque objet (événement, attribut et tableau d’achat) peut mettre à jour un utilisateur chacun. Au total, cela signifie que jusqu'à 225 utilisateurs peuvent être mis à jour en un seul appel. En outre, un profil utilisateur unique peut être mis à jour par plusieurs objets.

Les demandes adressées à cet endpoint commencent généralement à traiter dans cet ordre :

1. Attributs
2. Événements
3. Achats

### Demandes de traitement par lot aux endpoints de messagerie

Une seule demande adressée aux [endpoints de messages][1] peut atteindre l'un des éléments suivants :

- Jusqu’à 50 `external_ids` spécifiques, chacun avec des paramètres de message individuels
- Un segment de toute taille créé dans le tableau de bord de Braze, spécifié par son `segment_id`
- Les utilisateurs qui correspondent à des filtres d'audience supplémentaires de toute taille, définis dans la demande comme un objet d'[audience connecté.][2] 

### Exemple de demande de lot

L’exemple suivant utilise `external_id` pour effectuer un appel API pour les e-mails et SMS.

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

## Surveiller vos limites de débit

Chaque demande API envoyée à Braze renvoie les informations suivantes dans les en-têtes de réponse :

| Nom d’en-tête             | Description                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------- |
| `X-RateLimit-Limit`     | Nombre maximum de demandes que vous pouvez effectuer dans un intervalle spécifié (votre limite de débit). |
| `X-RateLimit-Remaining` | Nombre de demandes restant dans la fenêtre de limite de débit actuelle.                          |
| `X-RateLimit-Reset`     | Heure à laquelle la fenêtre de limite de débit actuelle se réinitialise en secondes d’époque UTC.                |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Ces informations sont intentionnellement incluses dans l’en-tête de la réponse à la demande API plutôt que sur le tableau de bord de Braze. Cela permet à votre système de mieux réagir en temps réel lorsque vous interagissez avec notre API. Par exemple, si la valeur de `X-RateLimit-Remaining` passe en dessous d'un certain seuil, vous pouvez ralentir l'envoi pour vous assurer que tous les e-mails transactionnels sont envoyés. Ou, si elle atteint zéro, vous voudrez peut-être suspendre tous les envois jusqu’à ce que le temps spécifié dans `X-RateLimit-Reset` s’écoule.

{% alert note %}
Les en-têtes HTTP seront retournés en minuscules. Ce comportement est conforme au protocole HTTP/2 qui exige que tous les noms de champs d'en-tête soient en minuscules. Cela diffère de HTTP/1.X où les noms des en-têtes n'étaient pas sensibles à la casse, mais étaient généralement écrits avec différentes majuscules.
{% endalert %}

Si vous avez des questions sur les limites de l'API, contactez votre gestionnaire satisfaction client ou ouvrez un [ticket d'assistance.][support]

{% alert tip %}
Vous pouvez utiliser le [tableau de bord de l'utilisation de l'API]({{site.baseurl}}/user_guide/analytics/dashboard/api_usage_dashboard/) pour afficher et comparer le trafic entrant par rapport à vos limites de débit.
{% endalert %}

### Délai optimal entre les endpoints

{% alert note %}
Nous vous recommandons de laisser un délai de 5 minutes entre des appels d’endpoint consécutifs pour réduire les possibilités d’erreur.
{% endalert %}

Il est crucial de comprendre le délai optimal entre les endpoints lors de la réalisation d’appels consécutifs vers l’API Braze. Des problèmes surviennent lorsque les endpoints dépendent de la réussite du traitement d’autres endpoints, et s’ils sont appelés trop tôt, ils peuvent provoquer des erreurs. Par exemple, si vous attribuez un alias à un utilisateur par l'intermédiaire de notre point d'accès `/user/alias/new`, puis que vous utilisez cet alias pour envoyer un événement personnalisé par l'intermédiaire de notre point d'accès `/users/track`, combien de temps devez-vous attendre ?

Dans des conditions normales, le temps pour que la cohérence éventuelle de nos données se produise est de 10 à 100 ms (1/10 d’une seconde). Toutefois, dans certains cas, il faut plus de temps pour que cette cohérence se produise. Nous vous recommandons donc de prévoir un délai de 5 minutes entre les appels suivants afin de minimiser la probabilité d'une erreur.

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