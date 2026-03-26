<!---DEFAULT RATE LIMIT-->

{% if include.endpoint == "default" %}
La limite de débit par défaut de Braze de 250 000 requêtes par heure s'applique à cet endpoint, comme documenté dans [Limites de débit de l'API]({{site.baseurl}}/api/api_limits/).

<!---PUT /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "update dashboard user" %}
Cet endpoint a une limite de débit de 5 000 requêtes par jour et par société. Cette limite de débit est partagée avec les endpoints GET, DELETE et POST `/scim/v2/Users/`, comme documenté dans [Limites de débit de l'API]({{site.baseurl}}/api/api_limits/).

<!---GET /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "look up dashboard user" %}
Cet endpoint a une limite de débit de 5 000 requêtes par jour et par société. Cette limite de débit est partagée avec les endpoints PUT, GET, DELETE et POST `/scim/v2/Users/`, comme documenté dans [Limites de débit de l'API]({{site.baseurl}}/api/api_limits/).

<!---DELETE /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "delete dashboard user" %}
Cet endpoint a une limite de débit de 5 000 requêtes par jour et par société. Cette limite de débit est partagée avec les endpoints PUT, GET et POST `/scim/v2/Users/`, comme documenté dans [Limites de débit de l'API]({{site.baseurl}}/api/api_limits/).

<!---POST /scim/v2/Users--->
{% elsif include.endpoint == "create dashboard user" %}
Cet endpoint a une limite de débit de 5 000 requêtes par jour et par société. Cette limite de débit est partagée avec les endpoints PUT, GET et DELETE `/scim/v2/Users/`, comme documenté dans [Limites de débit de l'API]({{site.baseurl}}/api/api_limits/).

<!---GET /scim/v2/Users--->
{% elsif include.endpoint == "look up dashboard user email" %}
Cet endpoint a une limite de débit de 5 000 requêtes par jour et par société. Cette limite de débit est partagée avec les endpoints PUT, GET, DELETE et POST `/scim/v2/Users/`, comme documenté dans [Limites de débit de l'API]({{site.baseurl}}/api/api_limits/).

<!---/users/external_id/rename-->
<!---/users/external_id/remove-->

{% elsif include.endpoint == "external id migration" %}
Nous appliquons une limite de débit de 1 000 requêtes par minute à cet endpoint, comme documenté dans [Limites de débit de l'API]({{site.baseurl}}/api/api_limits/).

<!---/users/track-->

{% elsif include.endpoint == "users track" %}
Braze applique une limite de vitesse de base de 3 000 requêtes toutes les trois secondes à cet endpoint. Chaque requête `/users/track` peut contenir jusqu'à 75 objets au total, répartis entre `attributes`, `events` et `purchases`. Chaque objet peut mettre à jour un utilisateur. Un même profil utilisateur peut être mis à jour par plusieurs objets.

Pour les clients ayant acheté le forfait Monthly Active Users CY 24-25, Universal MAU, Web MAU ou Mobile MAU, des limites de débit supplémentaires s'appliquent. Pour plus d'informations, consultez [Limites Monthly Active Users CY 24-25]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#monthly-active-users-cy-24-25-universal-mau-web-mau-and-mobile-mau).

{% details Anciennes limites de débit %}
Pour les clients soumis aux anciennes limites de débit, chaque requête `/users/track` peut contenir jusqu'à 75 objets d'attributs, 75 objets d'événements et 75 objets d'achats. Chaque objet peut mettre à jour un utilisateur, pour un maximum combiné de 225 objets par requête. Un même profil utilisateur peut être mis à jour par plusieurs objets.
{% enddetails %}

Pour plus d'informations, consultez [Limites de débit de l'API]({{site.baseurl}}/api/api_limits/). Contactez votre Customer Success Manager pour demander une augmentation.

<!---/users/export/ids-->

{% elsif include.endpoint == "users export ids" %}
Si vous avez réalisé l'onboarding avec Braze le 22 août 2024 ou après, cet endpoint présente une limite de débit de 250 requêtes par minute, comme documenté dans [Limites de débit de l'API]({{site.baseurl}}/api/api_limits/).

Vous pouvez également augmenter la limite de débit de cet endpoint à 40 requêtes par seconde en respectant les conditions suivantes :

- Votre espace de travail dispose de la limite de débit par défaut (250 requêtes par minute) activée. Contactez votre Account Manager Braze pour obtenir de l'aide afin de supprimer toute limite de débit préexistante dont vous pourriez disposer.
- Votre requête inclut le paramètre `fields_to_export` pour lister tous les champs que vous souhaitez recevoir.

{% alert important %}
Si vous incluez `canvases_received` ou `campaigns_received` dans le paramètre `fields_to_export`, votre requête ne sera pas éligible à la limite de débit plus élevée. Nous vous recommandons de ne les inclure dans votre requête que si vous avez un cas d'utilisation spécifique.
{% endalert %}

<!---/users/delete-->

{% elsif include.endpoint == "users delete" %}
Nous appliquons une limite de débit partagée de 20 000 requêtes par minute à cet endpoint. Cette limite de débit est partagée avec les endpoints `/users/alias/new`, `/users/identify`, `/users/merge` et `/users/alias/update`, comme documenté dans [Limites de débit de l'API]({{site.baseurl}}/api/api_limits/).

<!---/users/alias/new-->

{% elsif include.endpoint == "users alias new" %}
Nous appliquons une limite de débit partagée de 20 000 requêtes par minute à cet endpoint. Cette limite de débit est partagée avec les endpoints `/users/delete`, `/users/identify`, `/users/merge` et `/users/alias/update`, comme documenté dans [Limites de débit de l'API]({{site.baseurl}}/api/api_limits/).

<!---/users/alias/update-->

{% elsif include.endpoint == "users alias update" %}
Nous appliquons une limite de débit partagée de 20 000 requêtes par minute à cet endpoint. Cette limite de débit est partagée avec les endpoints `/users/delete`, `/users/alias/new`, `/users/identify` et `/users/merge`, comme documenté dans [Limites de débit de l'API]({{site.baseurl}}/api/api_limits/).

<!---/users/identify-->

{% elsif include.endpoint == "users identify" %}
Nous appliquons une limite de débit partagée de 20 000 requêtes par minute à cet endpoint. Cette limite de débit est partagée avec les endpoints `/users/delete`, `/users/alias/new`, `/users/merge` et `/users/alias/update`, comme documenté dans [Limites de débit de l'API]({{site.baseurl}}/api/api_limits/).

<!---/users/merge-->

{% elsif include.endpoint == "users merge" %}
Nous appliquons une limite de débit partagée de 20 000 requêtes par minute à cet endpoint. Cette limite de débit est partagée avec les endpoints `/users/delete`, `/users/alias/new`, `/users/identify` et `/users/alias/update`, comme documenté dans [Limites de débit de l'API]({{site.baseurl}}/api/api_limits/).

<!---/custom_attributes-->

{% elsif include.endpoint == "custom_attributes" %}
Nous appliquons une limite de débit partagée de 1 000 requêtes par heure à cet endpoint. Cette limite de débit est partagée avec les endpoints `/events`, `/events/list` et `/purchases/product_list`, comme documenté dans [Limites de débit de l'API]({{site.baseurl}}/api/api_limits/).

<!---/events-->

{% elsif include.endpoint == "events" %}
Nous appliquons une limite de débit partagée de 1 000 requêtes par heure à cet endpoint. Cette limite de débit est partagée avec les endpoints `/custom_attributes`, `/events/list` et `/purchases/product_list`, comme documenté dans [Limites de débit de l'API]({{site.baseurl}}/api/api_limits/).

<!---/events/list-->

{% elsif include.endpoint == "events list" %}
Nous appliquons une limite de débit partagée de 1 000 requêtes par heure à cet endpoint. Cette limite de débit est partagée avec les endpoints `/custom_attributes`, `/events` et `/purchases/product_list`, comme documenté dans [Limites de débit de l'API]({{site.baseurl}}/api/api_limits/).

<!---/purchases/product_list-->

{% elsif include.endpoint == "purchases product list" %}
Nous appliquons une limite de débit partagée de 1 000 requêtes par heure à cet endpoint. Cette limite de débit est partagée avec les endpoints `/custom_attributes`, `/events` et `/events/list`, comme documenté dans [Limites de débit de l'API]({{site.baseurl}}/api/api_limits/).

<!---/messages/send-->
<!---/campaigns/trigger/send-->
<!---/canvas/trigger/send-->

{% elsif include.endpoint == "send endpoints" %}
Lorsque vous utilisez des filtres d'audience connectée dans votre requête, nous appliquons une limite de débit de 250 requêtes par minute à cet endpoint. Sinon, si vous spécifiez un `external_id`, cet endpoint présente une limite de débit par défaut de 250 000 requêtes par heure, partagée entre `/messages/send`, `/campaigns/trigger/send` et `/canvas/trigger/send`, comme documenté dans [Limites de débit de l'API]({{site.baseurl}}/api/api_limits/).

Les endpoints Braze prennent en charge le traitement par lots des requêtes API. Une seule requête aux endpoints d'envoi de messages peut atteindre n'importe lequel des éléments suivants :

- Jusqu'à 50 `external_ids` spécifiques, chacun avec des paramètres de message individuels
- Un segment d'audience de toute taille, défini dans la requête comme un objet Connected Audience

<!---/transactional/v1/campaigns/{campaign_id}/send -->

{% elsif include.endpoint == "transactional email" %}
L'endpoint `/transactional/v1/campaigns/{campaign_id}/send` est un endpoint payant facturé en unités par heure (par exemple, 50 000 par heure selon votre forfait). Il n'existe pas de limite de débit distincte par endpoint : vous pouvez envoyer au-delà du volume qui vous est alloué, mais seul le volume alloué est couvert par le SLA. Les requêtes adressées à cet endpoint sont prises en compte dans votre [limite de débit globale de l'API externe]({{site.baseurl}}/api/api_limits/). Si vous dépassez cette limite (par exemple, 250 000 requêtes par heure sur tous les endpoints), Braze renvoie une erreur 429 et les requêtes sont limitées. Le compteur de volume transactionnel est réinitialisé toutes les heures, de sorte qu'après une heure, un nouveau contingent est disponible. Dans le cadre du volume couvert par le SLA, 99,9 % des e-mails seront envoyés en moins d'une minute.

<!---POST /preference_center/v1 and PUT /preference_center/v1/{preferenceCenterExternalID}-->
{% elsif include.endpoint == "post or put preference center" %}
Cet endpoint a une limite de débit de 10 requêtes par minute et par espace de travail, comme documenté dans [Limites de débit de l'API]({{site.baseurl}}/api/api_limits/).

<!---GET /preference_center/v1-->
{% elsif include.endpoint == "get preference center" %}
Cet endpoint a une limite de débit de 1 000 requêtes par minute et par espace de travail, comme documenté dans [Limites de débit de l'API]({{site.baseurl}}/api/api_limits/).

<!---/sends/id/create-->

{% elsif include.endpoint == "sends id create" %}
Vous pouvez créer jusqu'à 100 identifiants d'envoi personnalisés par jour à l'aide de cet endpoint pour un espace de travail donné. Chaque combinaison de `send_id` et `campaign_id` que vous créez est prise en compte dans votre limite quotidienne. Les en-têtes de réponse pour toute requête valide incluent l'état actuel de la limite de débit. Consultez [Limites de débit de l'API]({{site.baseurl}}/api/api_limits/) pour plus de détails.

<!---/subscription/status/set-->
{% elsif include.endpoint == "subscription status set" %}
Cet endpoint présente une limite de débit de 5 000 requêtes par minute, partagée entre les endpoints `/subscription/status/set` et `/v2/subscription/status/set`, comme documenté dans [Limites de débit de l'API]({{site.baseurl}}/api/api_limits/).

<!-- Add this phrase back ", as documented in [API rate limits]({{site.baseurl}}/api/api_limits/)" to CDI endpoints for GA -->

<!---GET /cdi/integrations--->
{% elsif include.endpoint == "cdi list integrations" %}
Cet endpoint a une limite de débit de 50 requêtes par minute.

<!---POST /cdi/integrations/{integration_id}/sync--->
{% elsif include.endpoint == "cdi job sync" %}
Cet endpoint a une limite de débit de 20 requêtes par minute.

<!---POST /cdi/integrations/{integration_id}/job_sync_status--->
{% elsif include.endpoint == "cdi job sync status" %}
Cet endpoint a une limite de débit de 100 requêtes par minute.

{% endif %}

<!---Additional if statement for Messaging endpoints-->

{% if include.category == "message endpoints" %}

Les endpoints Braze prennent en charge les [requêtes d'API en lots]({{site.baseurl}}/api/api_limits/#batching-api-requests). Une seule requête aux endpoints d'envoi de messages peut atteindre n'importe lequel des éléments suivants :

- Jusqu'à 50 `external_ids` spécifiques, chacun avec des paramètres de message individuels
- Un segment de toute taille créé dans le tableau de bord de Braze, spécifié par son `segment_id`
- Un segment d'audience de toute taille, défini dans la requête en tant qu'objet [audience connectée]({{site.baseurl}}/api/objects_filters/connected_audience/)

{% endif %}

{% if include.category == "send messages endpoints" %}

Les endpoints Braze prennent en charge les [requêtes d'API en lots]({{site.baseurl}}/api/api_limits/#batching-api-requests). Une seule requête aux endpoints d'envoi de messages peut atteindre n'importe lequel des éléments suivants :

- Jusqu'à 50 `external_ids` spécifiques, chacun avec des paramètres de message individuels
- Un segment d'audience de toute taille, défini dans la requête en tant qu'objet [audience connectée]({{site.baseurl}}/api/objects_filters/connected_audience/)

{% endif %}

<!---Additional if statement for Translation endpoints-->

{% if include.endpoint == "translation endpoints" %}

Cet endpoint est soumis à une limite de débit de 250 000 requêtes par minute.

{% endif %}

<!---Additional if statement for /messages/send endpoint-->

{% if include.category == "message send endpoint" %}

Les endpoints Braze prennent en charge les [requêtes d'API en lots]({{site.baseurl}}/api/api_limits/#batching-api-requests). Une seule requête aux endpoints d'envoi de messages peut atteindre n'importe lequel des éléments suivants :

- Jusqu'à 50 `external_ids` spécifiques
- Un segment de toute taille créé dans le tableau de bord de Braze, spécifié par son `segment_id`
- Un segment d'audience de toute taille, défini dans la requête en tant qu'objet [audience connectée]({{site.baseurl}}/api/objects_filters/connected_audience/)

{% endif %}

{% if include.endpoint == "asynchronous catalog item" %}

Cet endpoint a une limite de débit partagée de 16 000 requêtes par minute entre tous les endpoints d'éléments de catalogue asynchrones, comme documenté dans [Limites de débit de l'API]({{site.baseurl}}/api/api_limits/).

{% endif %}

{% if include.endpoint == "synchronous catalog item" %}

Cet endpoint a une limite de débit partagée de 50 requêtes par minute entre tous les endpoints d'éléments de catalogue synchrones, comme documenté dans [Limites de débit de l'API]({{site.baseurl}}/api/api_limits/).

{% endif %}

{% if include.endpoint == "synchronous catalog" %}

Cet endpoint a une limite de débit partagée de 50 requêtes par minute entre tous les endpoints de catalogues synchrones, comme documenté dans [Limites de débit de l'API]({{site.baseurl}}/api/api_limits/).

{% endif %}

{% if include.endpoint == "asynchronous catalog fields" or include.endpoint == "asynchronous catalog selections" %}

Cet endpoint a une limite de débit partagée de 50 requêtes par minute entre tous les endpoints de champs et sélections de catalogues asynchrones, comme documenté dans [Limites de débit de l'API]({{site.baseurl}}/api/api_limits/).

{% endif %}

{% if include.endpoint == "export campaign analytics" %}

Cet endpoint a une limite de débit de 50 000 requêtes par minute.

{% endif %}