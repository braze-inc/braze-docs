---
nav_title: Limites de débit
article_title: Limites de débit de l’API
page_order: 4.5
description: "Cet article de référence couvre les limites de débit de l’API pour l’infrastructure API Braze."
page_type: reference

---

# Limites de débit de l’API

L’infrastructure API Braze est conçue pour gérer des volumes élevés de données sur l’ensemble de notre base de clients. À cette fin, nous appliquons des limites de débit à l’API par groupe d’apps. Une limite de débit correspond au nombre de demandes que l’API peut recevoir dans une période donnée. De nombreux incidents de déni de service basés sur la charge dans les grands systèmes sont involontaires, causés par des erreurs dans les logiciels ou les configurations, et non par des attaques malveillantes. Les limites tarifaires garantissent que ces erreurs ne privent pas nos clients des ressources de l’API Braze. Si trop de demandes sont envoyées dans un délai donné, vous pouvez voir les réponses d’erreur avec un code de statut de `429`, qui indique que la limite de débit a été atteinte.

{% alert warning %}
Les limites de débit de l’API sont sujettes à modification en fonction de l’utilisation propre à notre système. Nous encourageons des limites raisonnables lors de l’appel d’API afin d’éviter tout dommage ou toute mauvaise utilisation.
{% endalert %}

## Limites de débit par type de demande

Le tableau suivant répertorie les limites de débit d’API par défaut pour différents types de demandes. Toutes les autres demandes non répertoriées dans ce tableau ont une limite de débit par défaut de 250 000 demandes par heure. 

Ces limites par défaut peuvent être augmentées sur demande. Contactez votre gestionnaire du succès des clients pour plus d’informations.

| Type de demande | Limite de débit de l’API par défaut |
| --- | --- |
| [`/users/track`][10] | **Demandes :** 50 000 demandes par minute.<br><br>**Traitement par lot :** 75 événements, 75 achats et 75 attributs par demande API. Voir [Demandes de suivi utilisateur du traitement par lots](#batch-user-track) pour en savoir plus. |
| [`/users/export/ids`][11] | 2 500 demandes par minute. |
| [`/users/delete`][12]<br>[`/users/alias/new`][13]<br>[`/users/alias/update`][45]<br>[`/users/identify`][14]<br>[`/users/merge`][44] | 2020 000 demandes par minute, partagées entre les endpoints. |
| [`/users/external_id/rename`][20] | 1 000 demandes par minute. |
| [`/users/external_id/remove`][21] | 1 000 demandes par minute. |
| [`/events/list`][15] | 1 000 demandes par heure, partagées avec l’endpoint `/purchases/product_list`. |
| [`/purchases/product_list`][16] | 1 000 demandes par heure, partagées avec l’endpoint `/events/list`. |
| [`/messages/send`][17] | 250 demandes par minute lors de la spécification d’un segment ou d’une audience connecté(e). Sinon, 250 000 demandes par heure. |
| [`/campaigns/trigger/send`][17.1] | 250 demandes par minute lors de la spécification d’un segment ou d’une audience connecté(e). Sinon, 250 000 demandes par heure. |
| [`/canvas/trigger/send`][17.2] | 250 demandes par minute lors de la spécification d’un segment ou d’une audience connecté(e). Sinon, 250 000 demandes par heure. |
| [`/sends/id/create`][18] | 100 demandes par jour. |
| [`/subscription/status/set`][19] | 5 000 demandes par minute. |
| [`/preference_center/v1/{preferenceCenterExternalId}/url/{userId}`][26]<br>[`/preference_center/v1/list`][27]<br>[`/preference_center/v1/{preferenceCenterExternalId}`][28] | 1 000 demandes par minute par groupe d’apps. |
| [`/preference_center/v1`][29]<br>[`/preference_center/v1/{preferenceCenterExternalId}`][30] | 10 demandes par minute par groupe d’apps. |
| [`/catalogs/catalog_name`][31]<br>[`/catalogs`][32]<br>[`/catalogs`][33] | 5 demandes par minute, partagées entre les endpoints. |
| [`/catalogs/catalog_name/items`][34]<br>[`/catalogs/catalog_name/items`][35]<br>[`/catalogs/catalog_name/items`][36] | 100 demandes par minute, partagées entre les endpoints. |
| [`/catalogs/catalog_name/items/item_id`][37]<br>[`/catalogs/catalog_name/items/item_id`][38]<br>[`/catalogs/catalog_name/items`][39]<br>[`/catalogs/catalog_name/items/item_id`][40]<br>[`/catalogs/catalog_name/items/item_id`][41] | 50 demandes par minute, partagées entre les endpoints. |
| [`GET: /scim/v2/Users/YOUR_ID_HERE`][22]<br>[`GET: /scim/v2/Users?filter=userName eq “user@test.com”`][43]<br>[`PUT: /scim/v2/Users/YOUR_ID_HERE`][25]<br>[`DELETE: /scim/v2/Users/YOUR_ID_HERE`][24]<br>[`POST: /scim/v2/Users/`][23] | 5 000 demandes par jour, partagées entre les endpoints. |
{: .reset-td-br-1 .reset-td-br-2}

## Traitement des demandes d’API par lot

Les API de Braze sont conçues pour prendre en charge le traitement par lot. Grâce au traitement par lot, Braze peut prendre autant de données que possible dans un seul appel d’API afin que vous n’ayez pas besoin de passer beaucoup d’appels d’API. Il est plus efficace pour Braze de traiter les données par lots que de les traiter par appel. Par exemple, la gestion de 1 000 appels d’API par lots nécessite moins de ressources que la gestion de 75 000 appels individuels. L’utilisation du traitement par lot est extrêmement importante pour les applications qui peuvent nécessiter plus de 75 000 appels par heure.

{% alert note %}
Les augmentations de limite de débit API REST sont envisagées en fonction du besoin des clients qui utilisent les capacités de traitement par lot de l’API.
{% endalert %}

### Requêtes User Track (Suivi Utilisateur) en lot {#batch-user-track}

Chaque demande `/users/track` peut contenir jusqu’à 75 objets d’événement, 75 objets d’attributs et 75 objets d’achats. Chaque objet (événement, attribut et tableau d’achat) peut mettre à jour un utilisateur chacun. Au total, cela signifie qu’un maximum de 225 utilisateurs peuvent être mis à jour en un seul appel. En outre, un profil utilisateur unique peut être mis à jour par plusieurs objets.

Les demandes adressées à cet endpoint commencent généralement à traiter dans cet ordre : 

1. Attributs
2. Événements
3. Achats

### Demandes de traitement par lot aux endpoints de messagerie

Une seule demande aux [endpoints de messagerie][1] peut atteindre l’un des éléments suivants :

- Jusqu’à 50 `external_ids` spécifiques, chacun avec des paramètres de message individuels
- Un segment de toute taille créée dans le tableau de bord de Braze, spécifié par son `segment_id`
- Un segment public ad hoc de toute taille, défini dans la demande en tant qu’objet [Audience connectée][2]

## Surveiller vos limites de débit

Chaque demande API envoyée à Braze renvoie les informations suivantes dans les en-têtes de réponse :

Nom d’en-tête             | Description
----------------------- | -----------------------
`X-RateLimit-Limit`     | Nombre maximum de demandes que vous pouvez effectuer dans un intervalle spécifié (votre limite de débit).
`X-RateLimit-Remaining` | Nombre de demandes restant dans la fenêtre de limite de débit actuelle.
`X-RateLimit-Reset`     | Heure à laquelle la fenêtre de limite de débit actuelle se réinitialise en secondes d’époque UTC.
{: .reset-td-br-1 .reset-td-br-2}

Ces informations sont intentionnellement incluses dans l’en-tête de la réponse à la demande API plutôt que sur le tableau de bord de Braze. Cela permet à votre système de mieux réagir en temps réel lorsque vous interagissez avec notre API. Par exemple, si la valeur `X-RateLimit-Remaining` chute en dessous d’un certain seuil, vous voudrez peut-être ralentir l’envoi pour vous assurer que tous les e-mails transactionnels partent. Ou, si elle atteint zéro, vous voudrez peut-être suspendre tous les envois jusqu’à ce que le temps spécifié dans `X-RateLimit-Reset` s’écoule.

Si vous avez des questions sur les limites d’API, contactez votre gestionnaire du succès des clients ou ouvrez un [ticket de support][support].

### Délai optimal entre les endpoints

{% alert note %}
Nous vous recommandons de laisser un délai de 5 minutes entre des appels d’endpoints multiples consécutifs pour réduire les possibilités d’erreur.
{% endalert %}

Il est crucial de comprendre le délai optimal entre les endpoints lors de la réalisation d’appels consécutifs vers l’API Braze. Des problèmes surviennent lorsque les endpoints dépendent du traitement réussi d’autres endpoints, et s’ils sont appelés trop tôt, ils peuvent provoquer des erreurs. Par exemple, si vous assignez un alias à un utilisateur via notre endpoint `/user/alias/new`, puis que vous appuyez sur cet alias pour envoyer un événement personnalisé via notre endpoint `/users/track`, combien de temps devrez-vous attendre ?

Dans des conditions normales, le temps pour que la cohérence éventuelle de nos données se produise est de 10 à 100 ms (1/10 d’une seconde). Cependant, il peut y avoir des cas où il faut plus longtemps pour que cette cohérence se produise. Par conséquent, nous vous recommandons de prévoir un délai de 5 minutes avant d’appeler des endpoints multiples afin de minimiser la probabilité d’erreur. Cette recommandation ne s’applique pas pour des appels d’endpoint consécutifs vers le même endpoint.

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
[31]: {{site.baseurl}}/api/endpoints/catalogs/synchronous_catalogs/delete_catalog/
[32]: {{site.baseurl}}/api/endpoints/catalogs/synchronous_catalogs/get_list_catalogs/
[33]: {{site.baseurl}}/api/endpoints/catalogs/synchronous_catalogs/post_create_catalog/
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
