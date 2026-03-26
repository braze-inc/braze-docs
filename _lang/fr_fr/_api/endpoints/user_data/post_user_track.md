---
nav_title: "POST : Créer et mettre à jour des utilisateurs"
article_title: "POST : Créer et mettre à jour des utilisateurs"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l'endpoint Braze Suivi utilisateur."
toc_headers: h2
---
{% api %}
# Créer et mettre à jour des utilisateurs
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/users/track
{% endapimethod %}

> Utilisez cet endpoint pour enregistrer des événements personnalisés et des achats, et pour mettre à jour les attributs du profil utilisateur.

{% alert note %}
Braze traite les données transmises par l'API telles quelles. Les clients ne doivent transmettre que les deltas (données modifiées) afin de minimiser la consommation inutile de points de données. Pour en savoir plus, consultez la rubrique [Points de données]({{site.baseurl}}/user_guide/data/data_points/).
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4cf57ea9-9b37-4e99-a02e-4373c9a4ee59 {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/api_key/) avec l'autorisation `users.track`.

Les clients qui utilisent l'API pour des appels de serveur à serveur devront peut-être ajouter `rest.iad-01.braze.com` à leur liste d'autorisations s'ils sont derrière un pare-feu.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='users track' %}

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "attributes": (optional, array of attributes object),
  "events": (optional, array of event object),
  "purchases": (optional, array of purchase object),
}
```

### Paramètres de demande

{% alert important %}
Pour chaque composant de la demande listé dans le tableau suivant, vous devez inclure l'un des éléments suivants : `external_id`, `user_alias`, `braze_id`, `email` ou `phone`.
{% endalert %}

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
| `attributes` | Facultatif | Tableau d'objets Attributs | Voir [objet attributs de l'utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object/) |
| `events` | Facultatif | Tableau d'objets Événement | Voir l'[objet événements]({{site.baseurl}}/api/objects_filters/event_object/) |
| `purchases` | Facultatif | Tableau d'objets Achat | Voir l'[objet achats]({{site.baseurl}}/api/objects_filters/purchase_object/) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Résolution des identifiants

Chaque objet de la demande doit contenir au moins un identifiant. Le tableau suivant décrit comment Braze détermine quel identifiant utiliser pour la recherche du profil utilisateur.

| Type d'identifiant | Identifiants | Comportement |
| --------------- | ----------- | -------- |
| Primaire | `external_id`, `user_alias`, `braze_id` | Utilisé pour la recherche du profil utilisateur. Un seul identifiant primaire est autorisé par objet de demande — en inclure plusieurs entraîne le rejet de cet objet. |
| Secondaire | `email`, `phone` | Utilisé pour la recherche du profil utilisateur **uniquement** lorsqu'aucun identifiant primaire n'est présent. Si `email` et `phone` sont tous deux inclus sans identifiant primaire, `email` est prioritaire. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Lorsqu'un identifiant primaire est présent, les valeurs `email` ou `phone` dans le même objet de demande sont traitées comme des attributs de profil, et non comme des identifiants pour la recherche d'utilisateur. Par exemple, si une demande inclut à la fois un `external_id` et un `email` :

- Braze recherche le profil utilisateur par `external_id`.
- La valeur `email` est définie (ou mise à jour) en tant qu'attribut sur le profil résolu.

{% alert important %}
L'inclusion d'un identifiant primaire qui ne correspond à aucun profil existant peut créer un profil en double, même si les valeurs `email` ou `phone` de la même demande correspondent à un profil existant. Pour plus d'informations, consultez [Comment éviter la création de profils utilisateurs en double ?](#how-do-i-avoid-creating-duplicate-user-profiles).
{% endalert %}

## Exemples de requêtes

### Mise à jour d'un profil utilisateur par adresse e-mail

Vous pouvez mettre à jour un profil utilisateur par adresse e-mail en utilisant l'endpoint `/users/track`.

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "email": "test@braze.com",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 26,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ],
    "events": [
        {
            "email": "test@braze.com",
            "app_id": "your_app_identifier",
            "name": "rented_movie",
            "time": "2022-12-06T19:20:45+01:00",
            "properties": {
                "release": {
                    "studio": "FilmStudio",
                    "year": "2022"
                },
                "cast": [
                    {
                        "name": "Actor1"
                    },
                    {
                        "name": "Actor2"
                    }
                ]
            }
        },
        {
            "user_alias": {
                "alias_name": "device123",
                "alias_label": "my_device_identifier"
            },
            "app_id": "your_app_identifier",
            "name": "rented_movie",
            "time": "2013-07-16T19:20:50+01:00"
        }
    ],
    "purchases": [
        {
            "email": "test@braze.com",
            "app_id": "your_app_identifier",
            "product_id": "product_name",
            "currency": "USD",
            "price": 12.12,
            "quantity": 6,
            "time": "2017-05-12T18:47:12Z",
            "properties": {
                "color": "red",
                "monogram": "ABC",
                "checkout_duration": 180,
                "size": "Large",
                "brand": "Backpack Locker"
            }
        }
    ]
}'
```

### Mise à jour d'un profil utilisateur par numéro de téléphone

Vous pouvez mettre à jour un profil utilisateur par numéro de téléphone en utilisant l'endpoint `/users/track`. Cet endpoint ne fonctionne que si vous indiquez un numéro de téléphone valide.

{% alert important %}
Si vous incluez à la fois `email` et `phone` dans une demande, Braze utilise l'e-mail comme identifiant.
{% endalert %}

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "phone": "+15043277269",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ],
}'
```
### Définir les groupes d'abonnement

Cet exemple montre comment créer un utilisateur et définir son groupe d'abonnement dans l'objet attributs de l'utilisateur.

La mise à jour de l'état de l'abonnement avec cet endpoint met à jour l'utilisateur spécifié par son `external_id` (par exemple User1) et met à jour l'état de l'abonnement de tous les utilisateurs ayant le même e-mail que cet utilisateur (User1).

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "attributes": [
  {
    "external_id": "user_identifier",
    "email": "example@email.com",
    "email_subscribe": "subscribed",
    "subscription_groups": [{
      "subscription_group_id": "subscription_group_identifier_1",
      "subscription_state": "unsubscribed"
      },
      {
        "subscription_group_id": "subscription_group_identifier_2",
        "subscription_state": "subscribed"
        },
        {
          "subscription_group_id": "subscription_group_identifier_3",
          "subscription_state": "subscribed",
          "use_double_opt_in_logic": true
        }
      ]
    }
  ]
}'
```

{% alert note %}
Pour les groupes d'abonnement SMS, lorsque vous définissez le `subscription_state` d'un groupe sur `subscribed`, vous pouvez inclure le paramètre facultatif `use_double_opt_in_logic` défini sur `true` dans cet objet de groupe d'abonnement afin de faire entrer l'utilisateur dans le workflow de [double opt-in SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/double_opt_in/). Si ce paramètre est omis ou défini sur `false` lorsque `subscription_state` est `subscribed`, l'utilisateur est abonné sans passer par le workflow de double opt-in. Ce paramètre n'est pas appliqué lorsque `subscription_state` est défini sur d'autres valeurs, telles que `unsubscribed`.
{% endalert %}

### Exemple de requête pour créer un utilisateur alias uniquement

Vous pouvez utiliser l'endpoint `/users/track` pour créer un utilisateur alias uniquement en attribuant à la clé `_update_existing_only` la valeur `false` dans le corps de la requête. Si vous omettez cette valeur, Braze ne crée pas le profil utilisateur alias uniquement. L'utilisation d'un utilisateur alias uniquement garantit l'existence d'un profil avec cet alias. C'est particulièrement utile lors de la création d'une intégration, car cela empêche Braze de créer des profils utilisateurs en double.

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
{
    "attributes": [
        {
            "_update_existing_only": false,
            "user_alias": {
                "alias_name": "example_name",
                "alias_label": "example_label"
            },
            "email": "email@example.com"
        }
    ],
}'
```


## Réponses

Lorsque vous utilisez l'une des requêtes API mentionnées ci-dessus, vous devriez recevoir l'une des trois réponses générales suivantes : un [message de réussite](#successful-message), un [message de réussite avec des erreurs non fatales](#successful-message-with-non-fatal-errors) ou un [message avec des erreurs fatales](#message-with-fatal-errors).

### Message de réussite

Les messages de réussite reçoivent la réponse suivante :

```json
{
  "message": "success",
  "attributes_processed": (optional, integer), if attributes are included in the request, this returns an integer of the number of external_ids with attributes that Braze queued for processing,
  "events_processed": (optional, integer), if events are included in the request, this returns an integer of the number of events that Braze queued for processing,
  "purchases_processed": (optional, integer), if purchases are included in the request, this returns an integer of the number of purchases that Braze queued for processing,
}
```

### Message de réussite avec des erreurs non fatales

Si votre message aboutit mais comporte des erreurs non fatales, telles qu'un objet d'événement non valide parmi une longue liste d'événements, vous recevez la réponse suivante :

```json
{
  "message": "success",
  "errors": [
    {
      <minor error message>
    }
  ]
}
```

En cas de réussite, Braze traite quand même toutes les données qui ne sont pas affectées par une erreur dans le tableau `errors`.

### Message avec des erreurs fatales

Si votre message comporte une erreur fatale, vous recevez la réponse suivante :

```json
{
  "message": <fatal error message>,
  "errors": [
    {
      <fatal error message>
    }
  ]
}
```

### Codes de réponse des erreurs fatales

Pour connaître les codes d'état et les messages d'erreur associés que Braze renvoie si votre demande rencontre une erreur fatale, reportez-vous à la section [Erreurs fatales et réponses]({{site.baseurl}}/api/errors/#fatal-errors).

Si vous recevez l'erreur "provided external_id is blacklisted and disallowed", il se peut que votre demande ait inclus un « utilisateur fictif ». Pour plus d'informations, consultez la section [Filtrage du spam]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking).

### Erreurs spécifiques à l'endpoint

Les erreurs suivantes sont spécifiques à l'endpoint `/users/track` et sont renvoyées dans le tableau `errors` de la réponse. Utilisez-les pour résoudre les problèmes liés aux objets individuels d'une demande.

| Erreur | Description |
|---|---|
| `BAD_DEVICE_ID` | Le `device_id` pour une importation de jeton doit contenir entre 8 et 255 octets. |
| `BAD_EMAIL_SUBSCRIPTION_STATE` | `email_subscribe` doit être `subscribed`, `unsubscribed` ou `opted_in`. |
| `BAD_LOCATION_UPDATE` | `current_location` doit être un objet contenant `longitude` et `latitude`. |
| `BAD_PUSH_SUBSCRIPTION_STATE` | `push_subscribe` doit être `subscribed`, `unsubscribed` ou `opted_in`. |
| `BAD_PUSH_TOKEN_APP_ID` | Le `app_id` dans une importation de jeton doit être un identifiant d'application valide de l'espace de travail actuel. |
| `BAD_PUSH_TOKEN_IMPORT` | Les importations de jetons doivent inclure des jetons et exclure `external_id` et `braze_id`. |
| `BAD_PUSH_TOKEN_STRING` | La valeur `token` dans une importation de jeton doit être une chaîne de caractères. |
| `BAD_PUSH_TOKEN_VALUE` | `push_tokens` doit être un tableau d'objets. |
| `BAD_SUBSCRIPTION_GROUP_ARRAY` | `subscription_groups` doit être un tableau. |
| `BAD_SUBSCRIPTION_GROUP_HASH` | Chaque élément du tableau `subscription_groups` doit être un objet JSON avec les clés `subscription_group_id` et `subscription_state`. |
| `BAD_SUBSCRIPTION_GROUP_ID` | `subscription_group_id` doit être un UUID de groupe d'abonnement valide. |
| `BAD_SUBSCRIPTION_GROUP_STATE` | `subscription_state` pour un groupe d'abonnement doit être `subscribed` ou `unsubscribed`. |
| `BLACKLISTED_EXTERNAL_USER_ID` | Le `external_id` fourni est bloqué et non autorisé. |
| `EMAIL_BAD_FORMAT` | La valeur fournie pour `email` n'est pas une adresse e-mail valide. |
| `EXTERNAL_USER_ID_TOO_LARGE` | Le `external_id` dépasse la longueur maximale autorisée de 987 octets. |
| `INVALID_ATTRIBUTE_EMAIL_SUBSCRIPTION_INFO` | `email_subscription_info` n'est pas un attribut valide. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Foire aux questions

{% multi_lang_include alerts/important_alerts.md alert='Email via SMS' %}

### Que se passe-t-il lorsque plusieurs profils avec la même adresse e-mail sont trouvés ?
Si le `external_id` existe, Braze donne la priorité au profil le plus récemment mis à jour possédant un ID externe. Si le `external_id` n'existe pas, Braze donne la priorité au profil le plus récemment mis à jour.

### Que se passe-t-il si aucun profil n'existe avec l'adresse e-mail ?
Braze crée un profil et un utilisateur e-mail uniquement, et définit le champ e-mail à test@braze.com, comme indiqué dans l'exemple de demande de mise à jour d'un profil utilisateur par adresse e-mail. Braze ne crée pas d'alias.

### Comment utiliser `/users/track` pour importer des données utilisateur héritées ?
Vous pouvez soumettre des données via l'API de Braze pour un utilisateur qui n'a pas encore utilisé votre application mobile afin de générer un profil utilisateur. Si l'utilisateur utilise ensuite l'application, toutes les informations suivant son identification via le SDK sont fusionnées avec le profil utilisateur existant créé via l'appel API. Tout comportement utilisateur enregistré de manière anonyme par le SDK avant l'identification est perdu lors de la fusion avec le profil utilisateur existant généré par l'API.

L'outil de segmentation inclut ces utilisateurs, qu'ils aient interagi ou non avec l'application. Si vous souhaitez exclure les utilisateurs téléchargés via l'API utilisateur qui n'ont pas encore utilisé l'application, ajoutez le filtre `Session Count > 0`.

### Comment éviter la création de profils utilisateurs en double ?

Des profils en double peuvent apparaître lorsqu'une demande inclut un identifiant primaire (tel que `external_id`) qui ne correspond à aucun profil existant, accompagné d'une valeur `email` ou `phone` qui correspond à un profil existant. Étant donné que les identifiants primaires sont utilisés pour la recherche d'utilisateur, Braze crée un nouveau profil pour le `external_id` non reconnu au lieu de mettre à jour le profil existant basé uniquement sur l'e-mail ou le téléphone.

Pour éviter les doublons :

- Lorsque vous faites passer des utilisateurs de profils basés uniquement sur l'e-mail ou le téléphone à des profils identifiés, utilisez l'[endpoint `/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) pour attribuer un `external_id` au profil existant, plutôt que d'envoyer les deux à `/users/track`.
- Si des doublons existent déjà, fusionnez-les à l'aide de l'[endpoint `/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/).

### Comment `/users/track` gère-t-il les événements en double ?

Chaque objet d'événement du tableau d'événements représente une occurrence unique d'un événement personnalisé par un utilisateur à un moment donné. Chaque événement ingéré dans Braze possède donc son propre ID d'événement, ce qui signifie que les événements « dupliqués » sont traités comme des événements distincts et uniques.

### Comment `/users/track` gère-t-il les attributs personnalisés imbriqués non valides ?

Lorsqu'un attribut personnalisé imbriqué contient des valeurs non valides (telles que des formats d'heure incorrects ou des valeurs nulles), Braze abandonne le traitement de toutes les mises à jour d'attributs personnalisés imbriqués de la demande. Cela s'applique à toutes les structures imbriquées au sein de cet attribut spécifique. Pour garantir un traitement réussi, vérifiez que toutes les valeurs des attributs personnalisés imbriqués sont valides avant l'envoi.

## Utilisateurs actifs mensuels CY 24-25, MAU universel, MAU web et MAU mobile

Pour les clients bénéficiant d'une nouvelle tarification, les limites de débit sont appliquées au niveau de l'entreprise. Les clients peuvent définir des limites de débit par espace de travail pour les limites horaires, mais les limites de rafale restent partagées entre tous les espaces de travail.

Pour les clients qui ont acheté des utilisateurs actifs mensuels CY 24-25, Universal MAU, Web MAU ou Mobile MAU, Braze applique des limites de débit différentes sur son endpoint `/users/track` :
- Les limites de débit horaires sont fixées en fonction de l'activité d'ingestion de données prévue sur votre compte, qui peut correspondre au nombre d'utilisateurs actifs par mois que vous avez achetés, au secteur d'activité, à la saisonnalité ou à d'autres facteurs.
- En plus de la limite horaire, Braze applique une limite de rafale sur le nombre de demandes pouvant être envoyées toutes les trois secondes.
- Chaque demande peut regrouper jusqu'à 75 mises à jour combinées portant sur des attributs, des événements ou des objets d'achat.

Les limites actuelles basées sur l'ingestion prévue sont disponibles dans le tableau de bord sous **Paramètres** > **API et identifiants** > **Tableau de bord de l'utilisation de l'API**. Nous pouvons modifier les limites de débit pour protéger la stabilité du système ou permettre une augmentation du débit de données sur votre compte. N'hésitez pas à contacter l'assistance Braze ou votre Customer Success Manager pour toute question concernant la limite de demandes horaire ou par seconde et les besoins de votre entreprise.

### En-têtes de limite de débit pour les utilisateurs actifs mensuels CY 24-25, Universal MAU, Web MAU et Mobile MAU

Toutes les réponses non limitées par le débit (c'est-à-dire non `429`) contiennent les en-têtes de réponse HTTP suivants, qui indiquent au client l'état de la fenêtre de limite de débit horaire. Utilisez ces en-têtes pour gérer votre fréquence de demandes :

| Nom de l'en-tête             | Description                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------- |
| `X-RateLimit-Limit`     | Le nombre de demandes autorisées par période de temps                                              |
| `X-RateLimit-Remaining` | Le nombre approximatif de demandes restantes dans la fenêtre en cours                                |
| `X-RateLimit-Reset`     | Le nombre de secondes restantes avant la réinitialisation de la fenêtre actuelle                                    |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Notez que les en-têtes `RateLimit-Limit`, `RateLimit-Remaining` et `RateLimit-Reset` ne sont pas renvoyés lorsque vous rencontrez une erreur HTTP `429`. Dans ce cas, ces en-têtes sont remplacés par un en-tête `X-Ratelimit-Retry-After` qui renvoie un nombre entier indiquant le nombre de secondes à attendre avant de pouvoir recommencer à envoyer des demandes.

{% endapi %}