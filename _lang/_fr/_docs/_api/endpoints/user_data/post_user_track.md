---
nav_title: "POST: Piste utilisateur"
article_title: "POST: Piste utilisateur"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: Référence
description: "Cet article décrit les détails sur le point de terminaison de la piste utilisateur de Braze."
---

{% api %}
# Suivi de l'utilisateur
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/fr/users/track
{% endapimethod %}

Utilisez ce point de terminaison pour enregistrer des événements personnalisés, des achats et mettre à jour les attributs du profil utilisateur.

{% alert note %}
Braze traite les données passées via l'API à la valeur faciale et les clients ne doivent passer des deltas (changement de données) que pour minimiser la consommation inutile de points de données. Pour en savoir plus, reportez-vous à [Data points]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/#data-points).
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4cf57ea9-9b37-4e99-a02e-4373c9a4ee59 {% endapiref %}

## Limite de taux

{% include rate_limits.md endpoint='users track' %}

## Corps de la requête

```
Type de contenu : application/json
Autorisation : Bearer YOUR-REST-API-KEY
```

```json
{
   "attributes" : (optionnel, tableau d'attributs object),
   "events" : (optionnel, tableau d'objet événement),
   "achats" : (optionnel, tableau d'objet d'achat),
}
```

Les clients qui utilisent l'API pour les appels de serveur à serveur peuvent avoir besoin de la liste blanche `rest.iad-01.braze.com` s'ils sont derrière un pare-feu.

### Paramètres de la requête

{% alert important %}
Pour chacun des composants de requête listés ci-dessous, un des `external_id`, `user_alias`, ou `braze_id` est requis.
{% endalert %}

| Paramètre    | Requis    | Type de données              | Libellé                                                                                            |
| ------------ | --------- | ---------------------------- | -------------------------------------------------------------------------------------------------- |
| `attributs`  | Optionnel | Tableau d'objets d'attributs | Voir l'objet [attributs utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object/) |
| `Evénements` | Optionnel | Tableau d'objets d'événement | Voir l'objet [événements]({{site.baseurl}}/api/objects_filters/event_object/)                      |
| `achats`     | Optionnel | Tableau des objets d'achat   | Voir [l'objet achats]({{site.baseurl}}/api/objects_filters/purchase_object/)                       |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% alert note %}
- Lors de la création d'utilisateurs uniquement alias à travers cette extrémité, vous devez définir explicitement le drapeau `_update_existing_only` à `false`.
- La mise à jour de l'état de l'abonnement avec ce point de terminaison ne mettra pas seulement à jour l'utilisateur spécifié par leur `external_id` (e. Utilisateur1), mais il mettra également à jour le statut d'abonnement de tous les utilisateurs avec le même email que cet utilisateur (User1).
{% endalert %}

## Exemple de corps de requête pour le suivi des événements

```json
{
  "events": [
    {
      "external_id": "string",
      "name": "string",
      "time": "string"
    }
  ]
 } } }
```

## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze. om/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "attributes": [ 
  {
    "external_id":"user_identifier",
      "string_attribute": "fruit",
      "boolean_attribute_1": true,
      "integer_attribute": 25,
      "attribut_tableau": ["banane", "pomme"]
    }
    ],
    "événements": [
    {
      "external_id": "user_identifier",
      "app_id" : "app_identifier",
      "name": "watched_trailer",
      "temps": "2013-07-16T19:20:30+1:00"
    }  
   ],
  "achats": [
     {
      "external_id": "user_identifier",
      "app_id": "app_identifier",
      "product_id": "nom_du_produit",
      "devise": "USD",
      "prix": 12. 2,
      "quantité": 6,
      "temps": "2017-05-12T18:47:12Z",
      "properties": {
         "integer_property": 3,
         "string_property": "Russell",
         "date_property": "2014-02-02T00:00:00Z"
       } 
     }
  ]
}'
```

## Réponses

Lorsque vous utilisez l'une des requêtes API susmentionnées, vous devriez recevoir l'une des trois réponses générales suivantes :

### Message réussi

Les messages réussis seront rencontrés avec la réponse suivante:

```json
{
  "message" : "success",
  "attributes_processed" : (facultatif, entier), si les attributs sont inclus dans la requête, retournera un entier du nombre d'external_ids avec des attributs qui ont été mis en file d'attente pour être traités,
  "events_processed" : (optionnel, entier), si les événements sont inclus dans la requête, cela retournera un entier du nombre d'événements qui ont été mis en file d'attente,
  "achats_traité" : (optionnel, integer), si les achats sont inclus dans la requête, retournera un entier du nombre d'achats qui ont été mis en file d'attente à traiter,
}
```

### Message réussi avec des erreurs non fatales

Si votre message est réussi mais a des erreurs non fatales, tel qu'un objet événement invalide dans une longue liste d'événements, vous recevrez la réponse suivante :

```json
{
  "message" : "success",
  "errors" : [
    {
      <minor error message>
    }
  ]
}
```

Pour les messages de réussite, toutes les données qui n'ont pas été affectées par une erreur dans le tableau `erreurs` seront toujours traitées.

### Message avec erreurs fatales

Si votre message a une erreur fatale, vous recevrez la réponse suivante:

```json
{
  "message" : <fatal error message>,
  "erreurs" : [
    {
      <fatal error message>
    }
  ]
}
```

### Code de réponse d'erreur fatal

Les codes de statut suivants et les messages d'erreur associés seront retournés si votre requête rencontre une erreur fatale. Les codes d'erreur suivants indiquent qu'aucune donnée ne sera traitée.

| Code d'erreur          | Raison / Cause                                                                 |
| ---------------------- | ------------------------------------------------------------------------------ |
| `400 Mauvaise requête` | Syntaxe incorrecte.                                                            |
| `401 Non autorisé`     | Clé d'API REST inconnue ou manquante.                                          |
| `404 introuvable`      | Clé d'API REST inconnue (si fournie).                                          |
| `Tarif Limité 429`     | Limite de débit.                                                               |
| `5XX`                  | Erreur interne du serveur, vous devriez réessayer avec un backoff exponentiel. |
{: .reset-td-br-1 .reset-td-br-2}

Si vous recevez l'erreur "external_id fourni est blacklisté et rejeté", votre requête peut avoir inclus un "utilisateur factice". Pour plus d'informations, reportez-vous à [Blocage de spam]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking).

## Importation des données utilisateur existantes

Vous pouvez soumettre des données via l'API Braze pour un utilisateur qui n'a pas encore utilisé votre application mobile afin de générer un profil utilisateur. Si l'utilisateur utilise l'application par la suite, toutes les informations après leur identification via le SDK seront fusionnées avec le profil utilisateur existant que vous avez créé via l'appel API. Tout comportement de l'utilisateur qui est enregistré anonymement par le SDK avant l'identification sera perdu lors de la fusion avec le profil utilisateur généré par l'API existante.

L'outil de segmentation inclura ces utilisateurs, qu'ils se soient engagés ou non avec l'application. Si vous voulez exclure les utilisateurs téléchargés via l'API utilisateur qui n'ont pas encore participé à l'application, ajoutez simplement le filtre : `Nombre de sessions > 0`.

## Mise à jour en masse

Si vous avez un cas d'utilisation où vous devez faire des mises à jour par lots pour les `utilisateurs/parcours` terminal, Nous vous recommandons d'ajouter l'en-tête de mise à jour en masse afin que Braze puisse correctement identifier, observer et acheminer votre demande.

Reportez-vous à l'échantillon de requête suivant avec l'en-tête `X-Braze-Bulk`:

```
curl --location --request POST 'https://rest.iad-01.braze. om/users/track' \
--header 'Content-Type: application/json' \
--header 'X-Braze-Bulk: true' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{ "attributes": [ ], "événements": [ ], "achats": [ ] }'
```

{% alert warning %}
Lorsque l'en-tête `X-Braze-Bulk` est présent avec n'importe quelle valeur, Braze prend en considération la requête en vrac. Veuillez définir la valeur à `true`. Actuellement, définir la valeur à `false` ne désactive pas l'en-tête — il sera toujours traité comme s'il était vrai.
{% endalert %}

### Cas d'utilisation

Considérez les cas d'utilisation suivants où vous pouvez utiliser l'en-tête de mise à jour en vrac :

- Un travail quotidien où les attributs personnalisés de plusieurs utilisateurs sont mis à jour via le point de terminaison `/users/track`.
- Un script de remplissage de données utilisateur ad-hoc qui met à jour les informations de l'utilisateur via le point de terminaison `/users/track`.

{% endapi %}
