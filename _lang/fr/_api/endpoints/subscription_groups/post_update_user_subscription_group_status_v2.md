---
nav_title: "POST : mettre à jour le statut du groupe d’abonnement de l’utilisateur V2"
alias: /post_update_user_subscription_group_status_v2/
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze V2 Mettre à jour le statut du groupe d’abonnement de l’utilisateur."

platform: API
channel:
  - E-mail
---

{% api %}
# Mettre à jour le statut du groupe d’abonnement de l’utilisateur (V2)
{% apimethod post %}
/v2/subscription/status/set
{% endapimethod %}

> Utilisez cet endpoint pour mettre à jour en masse le statut d’abonnement jusqu’à 50 utilisateurs sur le tableau de bord de Braze. 

Vous pouvez accéder au groupe d’abonnement `subscription_group_id` en vous rendant sur la page **Subscription Groups**.

Si vous souhaitez voir des exemples ou tester cet endpoint pour les **groupes d’abonnement aux e-mails** :

{% apiref postman %}hhttps://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#b1b9a0e0-6329-4df2-a465-53347f410662 {% endapiref %}

Si vous souhaitez voir des exemples ou tester cet endpoint pour les **groupes d’abonnement aux SMS** :

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#81a5fe65-588b-4b61-82d8-5ce68b681409 {% endapiref %}

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
Lorsque vous créez de nouveaux utilisateurs au moyen de l’endpoint [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), vous pouvez définir des groupes d'abonnement dans l’objet attributs d’utilisateur, ce qui vous permet de créer un utilisateur et de définir l’état du groupe d’abonnement dans un seul appel API.
{% endalert %}

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `subscription_group_id` | Requis | String | L’`id` de votre groupe d’abonnement. |
| `subscription_state` | Requis | String | Les valeurs disponibles sont `unsubscribed` (pas dans le groupe d’abonnement) ou `subscribed` (dans le groupe d’abonnement). |
| `external_ids` | Requis* | Tableau de chaînes de caractères | L’`external_id` de l’utilisateur ou des utilisateurs (50 `id`s max). |
| `emails` | Requis* | Chaîne de caractères ou tableau de chaînes de caractères | L’adresse e-mail de l’utilisateur peut être transmise comme un tableau de chaînes de caractères. Doit inclure au moins une adresse e-mail (50 maximum). <br><br>Si plusieurs utilisateurs (`external_id`) dans le même groupe d’apps partagent la même adresse e-mail, tous les utilisateurs qui partagent l’adresse e-mail sont mis à jour avec les modifications du groupe d’abonnement. |
| `phones` | Requis* | Chaîne de caractères au format [E.164](https://en.wikipedia.org/wiki/E.164) | Les numéros de téléphone de l’utilisateur, peuvent être transmis comme un tableau de chaînes de caractères. Doit inclure au moins un numéro de téléphone (50 maximum). |
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

## SMS

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
