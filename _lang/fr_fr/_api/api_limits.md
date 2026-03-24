---
nav_title: Limites de débit
article_title: Limites de débit de l'API
page_order: 4.5
description: "Cet article de référence couvre les limites de débit de l'API pour l'infrastructure API de Braze."
page_type: reference

---

# Limites de débit

> L'infrastructure API de Braze est conçue pour gérer des volumes élevés de données sur l'ensemble de notre base de clients. C'est pourquoi nous appliquons des limites de débit à l'API par espace de travail.

Une limite de débit correspond au nombre de requêtes que l'API peut recevoir sur une période donnée. De nombreux incidents de déni de service liés à la charge dans les grands systèmes sont involontaires — causés par des erreurs dans les logiciels ou les configurations — et non par des attaques malveillantes. Les limites de débit garantissent que de telles erreurs ne privent pas nos clients des ressources de l'API de Braze. Si trop de requêtes sont envoyées dans un délai donné, vous risquez de recevoir des réponses d'erreur avec un code d'état `429`, indiquant que la limite de débit a été atteinte.

{% alert warning %}
Les limites de débit de l'API sont susceptibles d'évoluer en fonction de l'utilisation appropriée de notre système. Nous vous encourageons à définir des limites raisonnables lors de vos appels API afin d'éviter tout dommage ou toute mauvaise utilisation.
{% endalert %}

## Limites de débit par type de requête

Consultez les informations ci-dessous pour connaître les limites de débit par défaut de l'API selon les différents types de requêtes. Ces limites par défaut peuvent être augmentées sur demande. Contactez votre Customer Success Manager pour plus d'informations.

### Requêtes avec différentes limites de débit

| Type de requête                                                                                                                                                                                                                                           | Limite de débit par défaut de l'API                                                                                                                                                                                                                                                                                                                                                                    |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)                                                                                                                                                                                                                                   | **Requêtes :** 3 000 requêtes par trois secondes.<br><br>**Traitement par lot :** jusqu'à 75 objets au total, combinés entre `attributes`, `events` et `purchases` par requête API. Les clients bénéficiant d'anciennes limites de débit peuvent inclure jusqu'à 75 objets par tableau de manière indépendante. Pour en savoir plus, consultez la rubrique [Mise en lot des requêtes de suivi des utilisateurs](#batch-user-track).<br><br>**Limites pour les utilisateurs actifs par mois CY 24-25, MAU universels, MAU Web et MAU mobiles :** consultez [les directives relatives aux limites ici]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#monthly-active-users-cy-24-25). |
| [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)                                                                                                                                                                                                                              | **Si votre intégration date du 22 août 2024 ou après :** 250 requêtes par minute. <br><br> **Si votre intégration date d'avant le 22 août 2024 :** 2 500 requêtes par minute.                                                                                                                                                                                                                               |
| [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/)<br>[`/users/alias/new`]({{site.baseurl}}/api/endpoints/user_data/post_user_alias/)<br>[`/users/alias/update`]({{site.baseurl}}/api/endpoints/user_data/post_users_alias_update/)<br>[`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)<br>[`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)                                                                                                                    | 20 000 requêtes par minute, partagées entre les endpoints.                                                                                                                                                                                                                                                                                                                                 |
| [`/users/external_id/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/)                                                                                                                                                                                                                      | 1 000 requêtes par minute.                                                                                                                                                                                                                                                                                                                                                                |
| [`/users/external_id/remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove/)                                                                                                                                                                                                                      | 1 000 requêtes par minute.                                                                                                                                                                                                                                                                                                                                                                |
| [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events/)                                                                                                                                                                                                                                   | 1 000 requêtes par heure, partagées avec l'endpoint `/purchases/product_list`.                                                                                                                                                                                                                                                                                                              |
| [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/)                                                                                                                                                                                                                        | 1 000 requêtes par heure, partagées avec l'endpoint `/events/list`.                                                                                                                                                                                                                                                                                                                         |
| [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/)                                                                                                                                                                                                                       | 50 000 requêtes par minute.                                                                                                                                                                                                                                                                                                                                                               |
| [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)<br>[`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)<br>[`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)                                                                                                                                                          | Pour les appels de diffusion (ciblage large de segments, de filtres ou d'une audience connectée) : 250 requêtes par minute toutes audiences confondues, **et** 10 requêtes par minute par [audience unique]({{site.baseurl}}/api/api_limits/#what-counts-as-the-same-unique-audience) (c'est la première limite atteinte qui s'applique).<br><br>Pour le ciblage de destinataires individuels, la requête est comptabilisée dans la [limite de débit partagée]({{site.baseurl}}/api/api_limits/#requests-with-shared-rate-limits) de 250 000 requêtes par heure.                                                                                                                                                                                                                    |
| [`/sends/id/create`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/)                                                                                                                                                                                                                               | 100 requêtes par jour.                                                                                                                                                                                                                                                                                                                                                                     |
| [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)                                                                                                                                                                                                                       | 5 000 requêtes par minute.                                                                                                                                                                                                                                                                                                                                                                |
| [`/preference_center/v1/{preferenceCenterExternalId}/url/{userId}`]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center/)<br>[`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center/)<br>[`/preference_center/v1/{preferenceCenterExternalId}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/)                                                                            | 1 000 requêtes par minute.                                                                                                                                                                                                                                                                                                                                                 |
| [`/preference_center/v1`]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center/)<br>[`/preference_center/v1/{preferenceCenterExternalId}`]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center/)                                                                                                                                                            | 10 requêtes par minute.                                                                                                                                                                                                                                                                                                                                                    |
| [`/catalogs/{catalog_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog/)<br>[`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/)<br>[`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/)                                                                                                                                                                             | 50 requêtes par minute, partagées entre les endpoints.                                                                                                                                                                                                                                                                                                                                      |
| [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk/)<br>[`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk/)<br>[`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk/)                                                                                                                             | 16 000 requêtes par minute, partagées entre les endpoints.                                                                                                                                                                                                                                                                                                                                  |
| [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item/)<br>[`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/)<br>[`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/)<br>[`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/)<br>[`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item/) | 50 requêtes par minute, partagées entre les endpoints.                                                                                                                                                                                                                                                                                                                                      |
| [`/catalogs/{catalog_name}/fields/{field_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field)<br>[`/catalogs/{catalog_name}/fields`]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields)<br>[`/catalogs/{catalog_name}/selections/{selection_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection)<br>[`/catalogs/{catalog_name}/selections`]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections) | 50 requêtes par minute, partagées entre les endpoints. |
| [`/scim/v2/Users/{id}`]({{site.baseurl}}/get_see_user_account_information/)<br>[`/scim/v2/Users?filter={userName@example.com}`]({{site.baseurl}}/get_search_existing_dashboard_user_email/)<br>[`/scim/v2/Users/{id}`]({{site.baseurl}}/post_update_existing_user_account/)<br>[`/scim/v2/Users/{id}}`]({{site.baseurl}}/delete_existing_dashboard_user/)<br>[`/scim/v2/Users/`]({{site.baseurl}}/post_create_user_account/)                                                                          | 5 000 requêtes par jour, par société, partagées entre les endpoints.                                                                                                                                                                                                                                                                                                                        |
| [`/cdi/integrations`]({{site.baseurl}}/api/endpoints/cdi/get_integration_list/)                                                                                                                                                                                                                              | 50 requêtes par minute.                                                                                                                                                                                                                                                                                                                                                                   |
| [`/cdi/integrations/{integration_id}/sync`]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status/)                                                                                                                                                                                                        | 20 requêtes par minute.                                                                                                                                                                                                                                                                                                                                                                   |
| [`/cdi/integrations/{integration_id}/job_sync_status`]({{site.baseurl}}/api/endpoints/cdi/post_job_sync/)                                                                                                                                                                                             | 100 requêtes par minute.                                                                                                                                                                                                                                                                                                                                                                  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Requêtes avec limites de débit partagées

Les requêtes suivantes partagent une limite de débit commune de 250 000 requêtes par heure.

- [`/app_group/sdk_authentication/create`]({{site.baseurl}}/api/endpoints/sdk_authentication/post_create_sdk_authentication_key/)
- [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys/)
- [`/app_group/sdk_authentication/delete`]({{site.baseurl}}/api/endpoints/sdk_authentication/delete_sdk_authentication_key)
- [`/app_group/sdk_authentication/primary`]({{site.baseurl}}/api/endpoints/sdk_authentication/delete_sdk_authentication_key/)
- [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details)
- [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns)
- [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) (uniquement pour les appels non diffusés, c'est-à-dire ceux qui spécifient `external_user_ids` ou `aliases`)
- [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/)
- [`/campaigns/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/)
- [`/campaigns/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns/)
- [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/)
- [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary/)
- [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/)
- [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/)
- [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) (uniquement pour les appels non diffusés)
- [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/)
- [`/canvas/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases/)
- [`/canvas/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/)
- [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/)
- [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/)
- [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/)
- [`/content_blocks/update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/)
- [`/email/blocklist`]({{site.baseurl}}/api/endpoints/email/post_blocklist/)
- [`/email/blacklist`]({{site.baseurl}}/api/endpoints/email/post_blacklist/)
- [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces/)
- [`/email/hard_bounces`]({{site.baseurl}}/api/endpoints/email/get_list_hard_bounces/)
- [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam/)
- [`/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status/)
- [`/email/unsubscribes`]({{site.baseurl}}/api/endpoints/email/get_query_unsubscribed_email_addresses/)
- [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics/)
- [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date/)
- [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days/)
- [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date/)
- [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date/)
- [`/messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start)
- [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update/)
- [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) (uniquement pour les appels non diffusés)
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

### Qu'est-ce qui est considéré comme la même audience unique ? {#what-counts-as-the-same-unique-audience}

Cela s'applique aux trois endpoints suivants : [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/), [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) et [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/).

Pour ces endpoints, les requêtes de diffusion sont considérées comme ciblant la même audience unique lorsque tous les éléments suivants correspondent :

- La campagne ou le canvas déclenché (le `campaign_id` ou `canvas_id` dans votre requête API, si spécifié)
- L'audience ciblée (les segments ou filtres, ou pour les campagnes API, le `segment_id` dans votre requête API)
- Les filtres d'audience connectés (l'objet `audience` dans votre requête API, s'il est spécifié)

Chaque combinaison unique de ces attributs est considérée comme une audience distincte. La limite de débit supplémentaire pour chaque audience unique s'applique donc indépendamment à chaque combinaison.

## Traitement des requêtes API par lot

Les API de Braze sont conçues pour prendre en charge le traitement par lot. Grâce à cette fonctionnalité, Braze peut ingérer un maximum de données en un seul appel API, ce qui vous évite de multiplier les appels. Il est bien plus efficace pour Braze de traiter les données par lots que de les traiter appel par appel. Par exemple, la gestion de 1 000 appels API par lots nécessite moins de ressources que la gestion de 75 000 appels individuels. Le traitement par lot est essentiel pour toute application susceptible de nécessiter plus de 75 000 appels par heure.

{% alert note %}
Des augmentations de la limite de débit de l'API REST peuvent être envisagées en fonction des besoins des clients qui utilisent les capacités de traitement par lot de l'API.
{% endalert %}

### Mise en lot des requêtes pour l'endpoint de suivi des utilisateurs {#batch-user-track}

Chaque requête `/users/track` peut contenir jusqu'à 75 objets au total, combinés entre `attributes`, `events` et `purchases`. Chaque objet peut mettre à jour un utilisateur. Un même profil utilisateur peut être mis à jour par plusieurs objets.

{% details Anciennes limites de débit %}
Pour les clients bénéficiant d'anciennes limites de débit, chaque tableau (`attributes`, `events` et `purchases`) peut contenir jusqu'à 75 objets de manière indépendante, pour un maximum combiné de 225 objets par requête.
{% enddetails %}

Pour en savoir plus sur les limites de débit de `/users/track`, consultez [POST : Créer et mettre à jour des utilisateurs]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).

Les requêtes adressées à cet endpoint commencent généralement à être traitées dans l'ordre suivant :

1. Attributs
2. Événements
3. Achats

### Mise en lot des requêtes aux endpoints de messagerie

Une seule requête adressée aux [endpoints de messagerie]({{site.baseurl}}/api/endpoints/messaging/) peut cibler l'un des éléments suivants :

- Jusqu'à 50 `external_ids` spécifiques, chacun avec des paramètres de message individuels
- Un segment de toute taille créé dans le tableau de bord de Braze, spécifié par son `segment_id`
- Les utilisateurs correspondant à des filtres d'audience supplémentaires de toute taille, définis dans la requête sous forme d'objet d'[audience connectée]({{site.baseurl}}/api/objects_filters/connected_audience/)

### Exemple de requête par lot

L'exemple suivant utilise `external_id` pour effectuer un seul appel API couvrant les e-mails et les SMS.

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

Chaque requête API envoyée à Braze renvoie les informations suivantes dans les en-têtes de réponse :

| Nom de l'en-tête             | Description                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------- |
| `X-RateLimit-Limit`     | Le nombre maximum de requêtes que vous pouvez effectuer dans un intervalle donné (votre limite de débit). |
| `X-RateLimit-Remaining` | Le nombre de requêtes restantes dans la fenêtre de limite de débit en cours.                          |
| `X-RateLimit-Reset`     | L'heure de réinitialisation de la fenêtre de limite de débit en cours, exprimée en secondes epoch UTC.                |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Ces informations sont volontairement incluses dans l'en-tête de la réponse API plutôt que dans le tableau de bord de Braze. Votre système peut ainsi réagir en temps réel lors de ses interactions avec notre API. Par exemple, si la valeur de `X-RateLimit-Remaining` passe en dessous d'un certain seuil, vous pouvez ralentir les envois pour vous assurer que tous les e-mails transactionnels sont bien transmis. Si elle atteint zéro, vous pouvez suspendre tous les envois jusqu'à ce que le délai indiqué dans `X-RateLimit-Reset` soit écoulé.

{% alert note %}
Les en-têtes HTTP sont renvoyés entièrement en minuscules. Ce comportement est conforme au protocole HTTP/2, qui impose que tous les noms de champs d'en-tête soient en minuscules. Cela diffère de HTTP/1.X, où les noms d'en-tête n'étaient pas sensibles à la casse mais étaient couramment écrits avec différentes capitalisations.
{% endalert %}

Si vous avez des questions sur les limites de l'API, contactez votre Customer Success Manager ou ouvrez un [ticket d'assistance]({{site.baseurl}}/braze_support/).

{% alert tip %}
Vous pouvez utiliser le [tableau de bord d'utilisation de l'API]({{site.baseurl}}/user_guide/analytics/dashboard/api_usage_dashboard/) pour visualiser et comparer le trafic entrant par rapport à vos limites de débit.
{% endalert %}

### Délai optimal entre les endpoints

{% alert note %}
Nous vous recommandons de prévoir un délai de 5 minutes entre des appels d'endpoint consécutifs afin de minimiser les erreurs.
{% endalert %}

Comprendre le délai optimal entre les endpoints est essentiel lorsque vous effectuez des appels consécutifs vers l'API de Braze. Des problèmes surviennent lorsqu'un endpoint dépend du traitement réussi d'un autre endpoint : s'il est appelé trop tôt, cela peut provoquer des erreurs. Par exemple, si vous attribuez un alias à un utilisateur via l'endpoint `/user/alias/new`, puis que vous utilisez cet alias pour envoyer un événement personnalisé via l'endpoint `/users/track`, combien de temps devez-vous attendre ?

Dans des conditions normales, la cohérence à terme de nos données s'établit en 10 à 100 ms (1/10 de seconde). Toutefois, dans certains cas, ce délai peut être plus long. Nous vous recommandons donc de prévoir un délai de 5 minutes entre les appels successifs afin de minimiser la probabilité d'erreur.

### Réinitialisation des limites de débit

Les limites de débit se réinitialisent à chaque heure pleine, et non sur une fenêtre glissante. Par exemple, si la limite est de 250 000 requêtes par heure, vous pouvez effectuer 50 000 requêtes entre 22 h 00 et 22 h 59, puis 250 000 requêtes supplémentaires entre 23 h 00 et 23 h 59, car le compteur se réinitialise au début de chaque heure.