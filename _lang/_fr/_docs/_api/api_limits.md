---
nav_title: Limites de taux
article_title: Limites de tarif de l'API
page_order: 4.5
description: "Cet article de référence couvre les limites de taux de l'API pour l'infrastructure API de Braze."
page_type: reference
---

# Limites de débit de l'API

L'infrastructure de l'API Braze est conçue pour gérer des volumes élevés de données à travers notre clientèle. Pour assurer un utilisateur responsable de l'API, nous appliquons les limites de taux de l'API par groupe d'applications. Une limite de taux est le nombre de requêtes que l'API peut recevoir dans une période donnée. Si trop de requêtes sont envoyées dans une période donnée, vous pouvez voir des réponses d'erreur avec un code de statut de `429`, qui indique que la limite de taux a été touchée.

{% alert warning %}
Les limites de taux de l'API et leurs valeurs (limitées ou illimitées) sont sujettes à changement selon l'utilisation correcte de notre système. Nous encourageons les limites raisonnables lors d'un appel à l'API pour prévenir les dommages ou les mauvais usages.
{% endalert %}

## Évaluer les limites par type de requête

Le tableau suivant répertorie les limites spécifiques de débit de l'API pour différents types de requêtes. Toutes les autres requêtes qui ne sont pas listées dans ce tableau ont une limite de 250 000 requêtes par heure.

| Type de requête                                                                          | Limite de débit API par défaut                                                                                                                                                                                                                                                                                                                           |
| ---------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`/fr/users/track`][10]                                                                  | **Requêtes :** 50 000 demandes par minute. Cette limite peut être augmentée sur demande. Contactez votre Customer Success Manager pour plus d'informations.<br><br>**Batching:** 75 événements, 75 achats et 75 attributs par requête API. Reportez-vous à [Batching User Track requests](#batch-user-track) ci-dessous pour en savoir plus. |
| [`/fr/users/export/ids`][11]                                                             | 2 500 demandes par minute.                                                                                                                                                                                                                                                                                                                               |
| [`/users/delete`][12]<br>[`/users/alias/new`][13]<br>[`/users/identify`][14] | 20 000 demandes par minute, partagées entre les terminaux.                                                                                                                                                                                                                                                                                               |
| [`/fr/events/list`][15]                                                                  | 1000 requêtes par heure, partagées avec le point de terminaison `/purchases/product_list`.                                                                                                                                                                                                                                                               |
| [`/fr/purchases/product_list`][16]                                                       | 1000 requêtes par heure, partagées avec le point de terminaison `/events/list`.                                                                                                                                                                                                                                                                          |
| [`/fr/messages/send`][17]                                                                | 250 requêtes par minute lorsque vous spécifiez un segment ou une audience connectée. Sinon, 250 000 demandes par heure.                                                                                                                                                                                                                                  |
| [`/fr/campaigns/trigger/send`][17.1]                                                     | 250 requêtes par minute lorsque vous spécifiez un segment ou une audience connectée. Sinon, 250 000 demandes par heure.                                                                                                                                                                                                                                  |
| [`/fr/canvas/trigger/send`][17.2]                                                        | 250 requêtes par minute lorsque vous spécifiez un segment ou une audience connectée. Sinon, 250 000 demandes par heure.                                                                                                                                                                                                                                  |
| [`/fr/sends/id/create`][18]                                                              | 100 demandes par jour.                                                                                                                                                                                                                                                                                                                                   |
{: .reset-td-br-1 .reset-td-br-2}

## Demande API en cours de traitement

Les APIs de Braze sont construits pour supporter le batching. Avec batching, Braze peut prendre autant de données que possible en un seul appel API pour que vous n'ayez pas besoin de faire beaucoup d'appels API. Il est plus efficace pour Braze de traiter les données en lots que de traiter les données un seul appel à la fois. Par exemple, la gestion de 1000 appels par lots d'API nécessite moins de ressources que la gestion de 75 000 appels individuels. Le traitement par lots est extrêmement important pour toute application qui peut nécessiter plus de 75 000 appels par heure.

{% alert note %}
Les augmentations de taux d'API REST sont prises en compte en fonction des besoins des clients qui utilisent les capacités de traitement de lots de l'API.
{% endalert %}

### Traitement des demandes de suivi de l'utilisateur {#batch-user-track}

Chaque requête `/users/track` peut contenir jusqu'à 75 événements, 75 mises à jour d'attributs et 75 achats. Chaque composant (événement, attribut et tableau d'achat), peut mettre à jour jusqu'à 75 utilisateurs chacun (maximum de 225 utilisateurs individuels). Chaque mise à jour peut également appartenir au même utilisateur pour un maximum de 225 mises à jour à un seul utilisateur dans une requête.

Les demandes faites à ce point de terminaison commenceront généralement à être traitées dans cet ordre:

1. Attributs
2. Évènements
3. Achats

### Demande de point de terminaison de messagerie batch

Une seule requête aux [terminaux de messagerie][1] peut atteindre n'importe laquelle des éléments suivants :

- Jusqu'à 50 `external_ids`spécifiques, chacun avec des paramètres de message individuels
- Un segment de toute taille créé dans le tableau de bord Braze, spécifié par son `segment_id`
- Un segment d'audience ad hoc de toute taille, défini dans la requête en tant qu'objet [Audience connectée][2]

## Surveiller vos limites de taux

Chaque requête API envoyée à Braze retourne les informations suivantes dans les en-têtes de réponse :

| Nom de l'en-tête      | Libellé                                                                                                  |
| --------------------- | -------------------------------------------------------------------------------------------------------- |
| `Limite de taux X`    | Le nombre maximum de requêtes que vous pouvez faire dans un intervalle spécifié (votre limite de taux).  |
| `X-RateLimit-Restant` | Le nombre de requêtes restantes dans la fenêtre de limite de taux actuelle.                              |
| `X-RateLimit-Reset`   | Le temps à partir duquel la fenêtre de limite de taux actuelle se réinitialise en secondes d'époque UTC. |
{: .reset-td-br-1 .reset-td-br-2}

Ces informations sont intentionnellement incluses dans l'en-tête de la réponse à la requête API plutôt que le tableau de bord Braze. Cela permet à votre système de mieux réagir en temps réel lorsque vous interagissez avec notre API. Par exemple, si la valeur `X-RateLimit-Reading` descend sous un certain seuil, vous pouvez ralentir l'envoi pour vous assurer que tous les courriels transactionnels sortent. Ou, si elle atteint zéro, vous pouvez mettre en pause tous les envois jusqu'à ce que le temps spécifié dans `X-RateLimit-Reset` s'écoule.

Si vous avez des questions au sujet des limites de l’API, veuillez contacter votre gestionnaire de succès client ou ouvrir un [ticket d’assistance][support].

### Délai optimal entre les terminaux

> Nous vous recommandons de prévoir un délai de 5 minutes entre les appels suivants pour minimiser la probabilité d'erreur.

Comprendre le délai optimal entre les terminaux est crucial lors des appels consécutifs à l'API Braze. Des problèmes surviennent lorsque les terminaux dépendent du traitement réussi d'autres terminaux, et s'ils sont appelés trop tôt, ils pourraient déclencher des erreurs. Par exemple, si vous assignez aux utilisateurs un alias via notre point de terminaison `/user/alias/new` puis en appuyant sur cet alias pour envoyer un événement personnalisé via notre point de terminaison `/users/track` , combien de temps devez-vous attendre ?

Dans des conditions normales, le temps de cohérence de nos données est de 10 à 100 ms (1/10 de seconde). Cependant, il peut y avoir des cas où il faut plus de temps pour que cette cohérence se produise. Par conséquent, nous vous recommandons de prévoir un délai de 5 minutes entre les appels suivants pour minimiser la probabilité d'erreur.

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
