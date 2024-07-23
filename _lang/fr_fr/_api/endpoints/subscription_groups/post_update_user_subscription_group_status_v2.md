---
nav_title: "POST : Mettre à jour le statut du groupe d’abonnement de l’utilisateur V2"
alias: /post_update_user_subscription_group_status_v2/
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze V2 Mettre à jour le statut du groupe d’abonnement de l’utilisateur."

platform: API
channel:
  - Email
---

{% api %}
# Mettre à jour le statut du groupe d’abonnement de l’utilisateur (V2)
{% apimethod post %}
/v2/subscription/status/set
{% endapimethod %}

> Utilisez cet endpoint pour mettre à jour en masse le statut d’abonnement jusqu’à 50 utilisateurs sur le tableau de bord de Braze. 

Vous pouvez accéder au groupe d'abonnement `subscription_group_id` en accédant à la page **Groupe d'abonnements** .

Si vous souhaitez voir des exemples ou tester ce point de terminaison pour **les groupes d'abonnement par courrier électronique** :

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#b1b9a0e0-6329-4df2-a465-53347f410662 {% endapiref %}

Si vous souhaitez voir des exemples ou tester ce point de terminaison pour **les groupes d'abonnement SMS** :

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#81a5fe65-588b-4b61-82d8-5ce68b681409 {% endapiref %}

Si vous souhaitez voir des exemples ou tester ce point de terminaison pour **les groupes WhatsApp**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#81a5fe65-588b-4b61-82d8-5ce68b681409 {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `subscription.status.set`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='subscription status set' %}

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "subscription_groups":[
    {
      "subscription_group_id": (required, string),
      "subscription_state": (required, string)
      "external_ids": (required*, array of strings),
      "emails": (required*, array of strings),
      "phones": (required*, array of strings in E.164 format),
    }
  ]
}
```
\* Notez que vous ne pouvez pas inclure à la fois les paramètres `emails` et `phones`. De plus, `emails`, `phones` et `external_ids` peuvent tous être envoyés individuellement.

{% alert tip %}
Lors de la création de nouveaux utilisateurs via le [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), vous pouvez définir des groupes d'abonnement dans l'objet d'attributs utilisateur, ce qui vous permet de créer un utilisateur et de définir l'état du groupe d'abonnement dans un seul appel d'API.
{% endalert %}

## Paramètres de demande

| Paramètre | Obligatoire | Type de données | Descriptif |
|---|---|---|---|
| [`subscription_group_id`]({{site.baseurl}}/api/identifier_types/?tab=subscription%20group%20ids) | Obligatoire | Chaîne | Le `id` de votre groupe d'abonnement. |
| `subscription_state` | Obligatoire | Chaîne | Les valeurs disponibles sont `unsubscribed` (pas dans le groupe d'abonnement) ou `subscribed` (dans le groupe d'abonnement). |
| `external_ids` | Obligatoire* | Tableau de chaînes | Le `external_id` du ou des utilisateurs, peut inclure jusqu'à 50 `id`s. |
| `emails` | Obligatoire* | Chaîne ou tableau de chaînes | L'adresse e-mail de l'utilisateur peut être transmise sous forme de tableau de chaînes. Doit inclure au moins une adresse e-mail (maximum 50). <br><br>Si plusieurs utilisateurs (`external_id`) dans le même espace de travail partagent la même adresse e-mail, tous les utilisateurs qui partagent l'adresse e-mail sont mis à jour avec les modifications du groupe d'abonnement. |
| `phones` | Obligatoire* | Chaîne au format [E.164](https://en.wikipedia.org/wiki/E.164) | Les numéros de téléphone de l’utilisateur peuvent être transmis sous forme de tableau de chaînes. Doit inclure au moins un numéro de téléphone (maximum 50).
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

{% alert note %}
Notez que vous ne pouvez pas inclure à la fois les paramètres `emails` et `phones`. De plus, `emails`, `phones` et `external_ids` peuvent tous être envoyés individuellement.
{% endalert %}

### Exemple de requêtes

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

## E-mail

```
curl --location --request POST 'https://rest.iad-01.braze.com/v2/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_groups":[
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "emails":["example1@email.com","example2@email.com"]
    }
  ]
}
'
```

## SMS et WhatsApp

```
curl --location --request POST 'https://rest.iad-01.braze.com/v2/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_groups":[
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "phones":["+12223334444","+15556667777"]
    }
  ]
}
'
```

{% endapi %}
