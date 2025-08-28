
<!---DEFAULT RATE LIMIT-->

{% if include.endpoint == "default" %}
Nous appliquons la limitation du débit Braze par défaut de 250 000 requêtes par heure à cet endpoint, comme documenté dans [Limites de débit de l’API]({{site.baseurl}}/api/api_limits/).

<!---PUT /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "update dashboard user" %}
Cet endpoint a une limitation du débit de 5 000 demandes par jour, par entreprise. Cette limitation du débit est partagée avec les endpoints GET, DELETE et POST `/scim/v2/Users/`, comme documenté dans [Limites de débit de l'API]({{site.baseurl}}/api/api_limits/).

<!---GET /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "look up dashboard user" %}
Cet endpoint a une limitation du débit de 5 000 demandes par jour, par entreprise. Cette limitation du débit est partagée avec les endpoints PUT, GET, DELETE et POST `/scim/v2/Users/`, comme documenté dans [Limites de débit de l'API]({{site.baseurl}}/api/api_limits/).

<!---DELETE /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "delete dashboard user" %}
Cet endpoint a une limitation du débit de 5 000 demandes par jour, par entreprise. Cette limitation du débit est partagée avec les endpoints PUT, GET et POST `/scim/v2/Users/`, comme documenté dans [Limites de débit de l'API]({{site.baseurl}}/api/api_limits/).

<!---POST /scim/v2/Users--->
{% elsif include.endpoint == "create dashboard user" %}
Cet endpoint a une limitation du débit de 5 000 demandes par jour, par entreprise. Cette limitation du débit est partagée avec les endpoints PUT, GET et DELETE `/scim/v2/Users/`, comme documenté dans [Limites de débit de l'API]({{site.baseurl}}/api/api_limits/).

<!---GET /scim/v2/Users--->
{% elsif include.endpoint == "look up dashboard user email" %}
Cet endpoint a une limitation du débit de 5 000 demandes par jour, par entreprise. Cette limitation du débit est partagée avec les endpoints PUT, GET, DELETE et POST `/scim/v2/Users/`, comme documenté dans [Limites de débit de l'API]({{site.baseurl}}/api/api_limits/).

<!---/users/external_id/rename-->
<!---/users/external_id/remove-->

{% elsif include.endpoint == "external id migration" %}
Nous appliquons la limitation du débit de 1 000 requêtes par minute à cet endpoint, comme documenté dans [Limites de débit de l’API]({{site.baseurl}}/api/api_limits/).

<!---/users/track-->

{% elsif include.endpoint == "users track" %}
À partir du 28 octobre 2024, nous appliquons une limite de vitesse de base de 3 000 requêtes par trois secondes à cet endpoint pour tous les clients. Chaque demande `/users/track` peut contenir jusqu’à 75 objets d’événement, 75 objets d’attributs et 75 objets d’achats. Chaque objet (événement, attribut et tableau d’achat) peut mettre à jour un utilisateur chacun. Au total, cela signifie qu’un maximum de 225 utilisateurs peuvent être mis à jour en un seul appel. En outre, un profil utilisateur unique peut être mis à jour par plusieurs objets.

Des limites différentes s'appliquent aux clients qui ont acheté le service **Utilisateurs actifs par mois - CY 24-25**. Pour plus de détails sur ces limites, voir [Utilisateurs actifs par mois - Limites CY 24-25]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#monthly-active-users-cy-24-25).

Consultez notre page sur les [Limites de débit de l’API]({{site.baseurl}}/api/api_limits/) pour plus de détails, et contactez votre gestionnaire du succès des clients si vous avez besoin d’élever votre limite.

<!---/users/export/ids-->

{% elsif include.endpoint == "users export ids" %}
Si vous avez réalisé l’onboarding avec Braze le 22 août 2024 ou après, cet endpoint présente une limite de débit de 250 requêtes par minute, comme documenté dans [Limites de débit de l'API]({{site.baseurl}}/api/api_limits/).

Vous pouvez également augmenter la limite de débit de cet endpoint à 40 requêtes par seconde en remplissant les conditions suivantes :

- La limite de débit par défaut (250 requêtes par minute) est activée dans votre espace de travail. Contactez votre gestionnaire de compte Braze pour obtenir de l'aide afin de supprimer toute limite de débit préexistante.
- Votre demande comprend le paramètre `fields_to_export` pour énumérer tous les champs que vous souhaitez recevoir.

{% alert important %}
Si vous incluez `canvases_received` ou `campaigns_received` dans le paramètre `fields_to_export`, votre demande ne pourra pas bénéficier de la limite de débit plus rapide. Nous vous recommandons de ne les inclure dans votre demande que si vous avez un cas d'utilisation spécifique.
{% endalert %}

<!---/users/delete-->

{% elsif include.endpoint == "users delete" %}
Nous appliquons à cet endpoint une limite de débit partagée de 20 000 requêtes par minute. Cette limitation du débit est partagée avec les endpoints `/users/alias/new`, `/users/identify`, `/users/merge` et `/users/alias/update`, comme documenté dans [Limites de débit de l'API]({{site.baseurl}}/api/api_limits/).

<!---/users/alias/new-->

{% elsif include.endpoint == "users alias new" %}
Nous appliquons à cet endpoint une limite de débit partagée de 20 000 requêtes par minute. Cette limitation du débit est partagée avec les endpoints `/users/delete`, `/users/identify`, `/users/merge` et `/users/alias/update`, comme documenté dans [Limites de débit de l'API]({{site.baseurl}}/api/api_limits/).

<!---/users/alias/update-->

{% elsif include.endpoint == "users alias update" %}
Nous appliquons à cet endpoint une limite de débit partagée de 20 000 requêtes par minute. Cette limitation du débit est partagée avec les endpoints `/users/delete`, `/users/alias/new`, `/users/identify` et `/users/merge`, comme documenté dans [Limites de débit de l'API]({{site.baseurl}}/api/api_limits/).

<!---/users/identify-->

{% elsif include.endpoint == "users identify" %}
Nous appliquons à cet endpoint une limite de débit partagée de 20 000 requêtes par minute. Cette limitation du débit est partagée avec les endpoints `/users/delete`, `/users/alias/new`, `/users/merge` et `/users/alias/update`, comme documenté dans [Limites de débit de l'API]({{site.baseurl}}/api/api_limits/).

<!---/users/merge-->

{% elsif include.endpoint == "users merge" %}
Nous appliquons à cet endpoint une limite de débit partagée de 20 000 requêtes par minute. Cette limitation du débit est partagée avec les endpoints `/users/delete`, `/users/alias/new`, `/users/identify` et `/users/alias/update`, comme documenté dans [Limites de débit de l'API]({{site.baseurl}}/api/api_limits/).

<!---/custom_attributes-->

{% elsif include.endpoint == "custom_attributes" %}
Nous appliquons à cet endpoint une limite de débit partagée de 1 000 requêtes par heure. Cette limitation du débit est partagée avec les endpoints `/events`, `/events/list` et `/purchases/product_list`, comme documenté dans [Limites de débit de l’API]({{site.baseurl}}/api/api_limits/).

<!---/events-->

{% elsif include.endpoint == "events" %}
Nous appliquons à cet endpoint une limite de débit partagée de 1 000 requêtes par heure. Cette limitation du débit est partagée avec les endpoints `/custom_attributes`, `/events/list` et `/purchases/product_list`, comme documenté dans [Limites de débit de l’API]({{site.baseurl}}/api/api_limits/).

<!---/events/list-->

{% elsif include.endpoint == "events list" %}
Nous appliquons à cet endpoint une limite de débit partagée de 1 000 requêtes par heure. Cette limitation du débit est partagée avec les endpoints `/custom_attributes`, `/events` et `/purchases/product_list`, comme documenté dans [Limites de débit de l’API]({{site.baseurl}}/api/api_limits/).

<!---/purchases/product_list-->

{% elsif include.endpoint == "purchases product list" %}
Nous appliquons à cet endpoint une limite de débit partagée de 1 000 requêtes par heure. Cette limitation du débit est partagée avec les endpoints `/custom_attributes`, `/events` et `/events/list`, comme documenté dans [Limites de débit de l’API]({{site.baseurl}}/api/api_limits/).

<!---/messages/send-->
<!---/campaigns/trigger/send-->
<!---/canvas/trigger/send-->

{% elsif include.endpoint == "send endpoints" %}
Lorsque vous spécifiez un segment ou une audience connectée dans votre demande, nous appliquons une limitation du débit de 250 demandes par minute à cet endpoint. Sinon, si vous spécifiez un `external_id`, cet endpoint présente une limitation du débit par défaut de 250 000 requêtes par heure, partagées entre `/messages/send`, `/campaigns/trigger/send` et `/canvas/trigger/send`, comme documenté dans [Limites de débit de l'API]({{site.baseurl}}/api/api_limits/).

<!---/transactional/v1/campaigns/{campaign_id}/send -->

{% elsif include.endpoint == "transactional email" %}
Les e-mails transactionnels de Braze ne sont pas soumis à une limitation du débit. Selon le package que vous avez choisi, un nombre défini d’e-mails transactionnels est couvert par heure par l’accord de niveau de service (SLA). Les requêtes qui dépassent ce taux sont toujours envoyées, mais ne sont pas couvertes par l'accord de niveau de service. 99,9 % des e-mails sont envoyés en moins d'une minute.

<!---/sends/id/create-->

{% elsif include.endpoint == "sends id create" %}
Le nombre maximum quotidien d’identificateurs d’envoi personnalisés pouvant être créés via cet endpoint est de 100 pour un espace de travail donné. Chaque combinaison de `send_id` et `campaign_id` que vous créez est prise en compte dans votre limite quotidienne. Les en-têtes de réponse pour toute requête valide incluent le statut de limitation du débit actuel. Voir [Limites de débit de l’API]({{site.baseurl}}/api/api_limits/) pour plus de détails.

<!---/subscription/status/set-->
{% elsif include.endpoint == "subscription status set" %}
Cet endpoint présente une limitation du débit de 5 000 requêtes par minute, partagées entre les endpoints `/subscription/status/set` et `/v2/subscription/status/set`, comme documenté dans [Limites de débit de l'API]({{site.baseurl}}/api/api_limits/).

<!-- Add this phrase back ", as documented in [API rate limits]({{site.baseurl}}/api/api_limits/)" to CDI endpoints for GA -->

<!---GET /cdi/integrations--->
{% elsif include.endpoint == "cdi list integrations" %}
Cet endpoint a une limitation du débit de 50 requêtes par minute.

<!---POST /cdi/integrations/{integration_id}/sync--->
{% elsif include.endpoint == "cdi job sync" %}
Cet endpoint a une limitation du débit de 20 requêtes par minute.

<!---POST /cdi/integrations/{integration_id}/job_sync_status--->
{% elsif include.endpoint == "cdi job sync status" %}
Cet endpoint a une limitation du débit de 100 requêtes par minute.

{% endif %}

<!---Additional if statement for Messaging endpoints-->

{% if include.category == "endpoints de message" %}

Les endpoints Braze prennent en charge les [requêtes d’API en lots]({{site.baseurl}}/api/api_limits/#batching-api-requests). Une seule demande aux endpoints de messagerie peut atteindre n’importe lequel des éléments suivants :

- Jusqu’à 50 `external_ids` spécifiques, chacun avec des paramètres de message individuels
- Un segment de toute taille créé dans le tableau de bord de Braze, spécifié par son `segment_id`
- Un segment d'audience de toute taille, défini dans la requête en tant qu’objet [audience connectée]({{site.baseurl}}/api/objects_filters/connected_audience/)

{% endif %}

<!---Additional if statement for Translation endpoints-->

{% if include.endpoint == "les endpoints de traduction" %}

Le débit de cet endpoint est limité à 250 000 requêtes par minute.

{% endif %}

<!---Additional if statement for /messages/send endpoint-->

{% if include.category == "endpoint envoi de messages" %}

Les endpoints Braze prennent en charge les [requêtes d’API en lots]({{site.baseurl}}/api/api_limits/#batching-api-requests). Une seule demande aux endpoints de messagerie peut atteindre n’importe lequel des éléments suivants :

- Jusqu'à 50 `external_ids` spécifiques
- Un segment de toute taille créé dans le tableau de bord de Braze, spécifié par son `segment_id`
- Un segment d'audience de toute taille, défini dans la requête en tant qu’objet [audience connectée]({{site.baseurl}}/api/objects_filters/connected_audience/)

{% endif %}

{% if include.endpoint == "asynchronous catalog item" %}

Cet endpoint a une limitation du débit de 16 000 requêtes par minute, partagée entre tous les endpoints de produits de catalogue asynchrones, comme documenté dans [Limites de débit de l'API]({{site.baseurl}}/api/api_limits/).

{% endif %}

{% if include.endpoint == "synchronous catalog item" %}

Cet endpoint a une limitation du débit de 50 requêtes par minute, partagée entre tous les endpoints de produits de catalogue synchrones, comme documenté dans [Limites de débit de l'API]({{site.baseurl}}/api/api_limits/).

{% endif %}

{% if include.endpoint == "synchronous catalog" %}

Cet endpoint a une limitation du débit de 50 requêtes par minute, partagée entre tous les endpoints de catalogues synchrones, comme documenté dans [Limites de débit de l'API]({{site.baseurl}}/api/api_limits/).

{% endif %}

{% if include.endpoint == "asynchronous catalog fields" or include.endpoint == "asynchronous catalog selections" %}

Cet endpoint a une limitation du débit de 50 requêtes par minute, partagée entre tous les endpoints de sélections et champs de catalogues asynchrones, comme documenté dans [Limites de débit de l'API]({{site.baseurl}}/api/api_limits/).

{% endif %}

{% if include.endpoint == "export campaign analytics" %}

Cet endpoint a une limitation du débit de 50 000 requêtes par minute.

{% endif %}

