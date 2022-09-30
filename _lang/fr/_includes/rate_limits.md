
<!---DEFAULT RATE LIMIT-->

{% if include.endpoint == "default" %}
Nous appliquons la limitation du débit Braze par défaut de 250 000 demandes par heure à cet endpoint, comme documenté dans [Limites de débit de l’API]({{site.baseurl}}/api/api_limits/).

<!---PUT /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "update dashboard developer" %}
Cet endpoint a une limitation du débit de 5 000 demandes par jour, par entreprise. Cette limitation du débit est partagée avec les endpoints `/scim/v2/Users/YOUR_ID_HERE` GET, DELETE et `/scim/v2/Users` POST<!--, as documented in [API rate limits]({{site.baseurl}}/api/api_limits/)--->.

<!---GET /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "look up dashboard developer" %}
Cet endpoint a une limitation du débit de 5 000 demandes par jour, par entreprise. Cette limitation du débit est partagée avec les endpoints `/scim/v2/Users/YOUR_ID_HERE` GET, DELETE et `/scim/v2/Users` POST<!--, as documented in [API rate limits]({{site.baseurl}}/api/api_limits/)--->.

<!---DELETE /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "delete dashboard developer" %}
Cet endpoint a une limitation du débit de 5 000 demandes par jour, par entreprise. Cette limitation du débit est partagée avec les endpoints `/scim/v2/Users/YOUR_ID_HERE` PUT, GET et `/scim/v2/Users` POST<!--, as documented in [API rate limits]({{site.baseurl}}/api/api_limits/)--->.

<!---POST /scim/v2/Users--->
{% elsif include.endpoint == "create dashboard developer" %}
Cet endpoint a une limitation du débit de 5 000 demandes par jour, par entreprise. Cette limitation du débit est partagée avec les endpoints `/scim/v2/Users/YOUR_ID_HERE` PUT, GET et DELETE <!--, as documented in [API rate limits]({{site.baseurl}}/api/api_limits/)--->.


<!---/users/external_id/rename-->
<!---/users/external_id/remove-->

{% elsif include.endpoint == "external id migration" %}
Nous appliquons la limitation du débit de 1 000 demandes par minute à cet endpoint, comme documenté dans [Limites de débit de l’API]({{site.baseurl}}/api/api_limits/).

<!---/users/track-->

{% elsif include.endpoint == "users track" %}
Nous appliquons une limite de vitesse de base de 50 000 demandes par minute à cet endpoint pour tous les clients. Chaque demande adressée à l’endpoint `/users/track` peut contenir jusqu’à 75 événements, 75 mises à jour d’attributs et 75 achats. Chaque composant (tableau d’événements, d’attributs et d’achats) peut mettre à jour jusqu’à 75 utilisateurs chacun pour un maximum de 225 points de données individuels. Chaque mise à jour peut également appartenir au même utilisateur pour un maximum de 225 mises à jour par utilisateur dans une demande.

Consultez notre page sur les [Limites de débit de l’API]({{site.baseurl}}/api/api_limits/) pour plus de détails, et contactez votre gestionnaire du succès des clients si vous avez besoin d’une limite plus haute.

<!---/users/export/ids-->

{% elsif include.endpoint == "users export ids" %}
Pour les clients qui ont rejoint Braze au plus tard le 16 août 2021, nous appliquons une limite de 2 500 demandes par minute à cet endpoint, comme documenté dans [Limites de débit de l’API]({{site.baseurl}}/api/api_limits/).

<!---/users/delete-->

{% elsif include.endpoint == "users delete" %}
Pour les clients qui ont rejoint Braze au plus tard le 16 septembre 2021, nous appliquons une limitation du débit partagée de 20 000 demandes par minute à cet endpoint. Cette limitation du débit est partagée avec les endpoints `/users/alias/new` et `/users/identify`, comme documenté dans [Limites de débit de l’API]({{site.baseurl}}/api/api_limits/).

<!---/users/alias/new-->

{% elsif include.endpoint == "users alias new" %}
Pour les clients qui ont rejoint Braze au plus tard le 16 septembre 2021, nous appliquons une limitation du débit partagée de 20 000 demandes par minute à cet endpoint. Cette limitation du débit est partagée avec les endpoints `/users/delete` et `/users/identify`, comme documenté dans [Limites de débit de l’API]({{site.baseurl}}/api/api_limits/).

<!---/users/identify-->

{% elsif include.endpoint == "users identify" %}
Pour les clients qui ont rejoint Braze au plus tard le 16 septembre 2021, nous appliquons une limitation du débit partagée de 20 000 demandes par minute à cet endpoint. Cette limitation du débit est partagée avec les endpoints `/users/delete` et `/users/alias/new`, comme documenté dans [Limites de débit de l’API]({{site.baseurl}}/api/api_limits/).

<!---/events/list-->

{% elsif include.endpoint == "events list" %}
Pour les clients qui ont rejoint Braze au plus tard le 16 septembre 2021, nous appliquons une limitation du débit partagée de 1 000 demandes par heure à cet endpoint. Cette limitation du débit est partagée avec l’endpoint `/purchases/product_list`, comme documenté dans [Limites de débit de l’API]({{site.baseurl}}/api/api_limits/).

<!---/purchases/product_list-->

{% elsif include.endpoint == "purchases product list" %}
Pour les clients qui ont rejoint Braze au plus tard le 16 septembre 2021, nous appliquons une limitation du débit partagée de 1 000 demandes par heure à cet endpoint. Cette limitation du débit est partagée avec l’endpoint `/events/list`, comme documenté dans [Limites de débit de l’API]({{site.baseurl}}/api/api_limits/).

<!---/messages/send-->
<!---/campaigns/trigger/send-->
<!---/canvas/trigger/send-->

{% elsif include.endpoint == "send endpoints" %}
Lorsque vous spécifiez un segment ou un public connecté dans votre demande, nous appliquons une limitation du débit de 250 demandes par minute à cet endpoint. Sinon, si vous spécifiez un `external_id`, cet endpoint a une limitation du débit par défaut de 250 000 demandes par heure, comme documenté dans [Limites de débit de l’API]({{site.baseurl}}/api/api_limits/).

<!---/transactional/v1/campaigns/YOUR_CAMPAIGN_ID_HERE/send -->

{% elsif include.endpoint == "transactional email" %}
Les e-mails transactionnels ne sont pas soumis à une limitation du débit. Selon le package que vous avez choisi, un nombre défini d’e-mails transactionnels est couvert par heure par le contrat de niveau de service (SLA). Les demandes qui dépassent ce taux continueront d’être envoyées, mais ne sont pas couvertes par le SLA. 99,9 % des e-mails seront envoyés en moins d’une minute.

<!---/sends/id/create-->

{% elsif include.endpoint == "sends id create" %}
Le nombre maximum quotidien d’identificateurs d’envoi personnalisés pouvant être créés via cet endpoint est de 100 pour un groupe d’Apps donné. Chaque combinaison de `send_id` et `campaign_id` que vous créez est comptabilisée dans votre limite quotidienne. Les en-têtes de réponse pour toute demande valide incluent le statut de limitation du débit actuel. Voir [Limites de débit de l’API]({{site.baseurl}}/api/api_limits/) pour plus de détails.

<!---/subscription/status/set-->
{% elsif include.endpoint == "subscription status set" %}
Pour les clients qui ont rejoint Braze au plus tard le 6 janvier 2022, nous appliquons une limitation du débit de 5 000 demandes par minute à cet endpoint, comme documenté dans [Limites de débit de l’API]({{site.baseurl}}/api/api_limits/).

{% endif %}

<!---Additional if statement for Messaging endpoints-->

{% if include.category == "message endpoints" %}

Les endpoints Braze prennent en charge les [demandes d’API en lots]({{site.baseurl}}/api/api_limits/#batching-api-requests). Une seule demande aux endpoints de messagerie peut atteindre n’importe lequel des éléments suivants :

- Jusqu’à 50 `external_ids` spécifiques, chacun avec des paramètres de message individuels
- Un segment de toute taille créée dans le tableau de bord de Braze, spécifié par son `segment_id`
- Un segment public ad hoc de toute taille, défini dans la demande en tant qu’objet [Public connecté]({{site.baseurl}}/api/objects_filters/connected_audience/)

{% endif %}