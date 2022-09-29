---
nav_title: "POST : Mettre à jour le statut du groupe d’abonnement de l’utilisateur V2"
permalink: /post_update_user_subscription_group_status_v2/
hidden: true
layout: api_page
page_type: reference
description: "Cet article présente des informations concernant l’endpoint Mettre à jour le statut du groupe d’abonnement Braze V2 de l’utilisateur."

platform: API
channel:
  - E-mail
---

{% api %}
# Mettre à jour le statut du groupe d’abonnement des utilisateurs
{% apimethod post %}
/v2/subscription/status/set
{% endapimethod %}

Utilisez cet endpoint pour mettre à jour le statut du groupe d’abonnement (50 utilisateurs maximum) sur le tableau de bord de Braze. Vous pouvez accéder au groupe d’abonnement `subscription_group_id` en vous rendant sur la page **Subscription Groups**.

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

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `subscription_group_id` | Requis | Chaîne de caractères | Le `id` de votre groupe d’abonnement. |
| `subscription_state` | Requis | Chaîne de caractères | Les valeurs disponibles sont `unsubscribed` (pas dans le groupe d’abonnement) ou `subscribed` (dans le groupe d’abonnement). |
| `external_ids` | Requis* | Tableau de chaînes de caractères | Le `external_id` de l’utilisateur ou des utilisateurs (50 `id`s max). |
| `emails` | Requis* | Chaîne de caractères ou tableau de chaîne de caractères | L’adresse e-mail de l’utilisateur, peut être transmise comme un tableau de chaînes de caractères. Doit inclure au moins une adresse e-mail (50 maximum). <br><br>Si plusieurs utilisateurs (`external_id`) dans le même groupe d’apps partagent la même adresse e-mail, tous les utilisateurs qui partagent l’adresse e-mail sont mis à jour avec les modifications du groupe d’abonnement. |
| `phones` | Requis* | Chaîne de caractères au format [E.164](https://en.wikipedia.org/wiki/E.164) | Les numéros de téléphone de l’utilisateur, peuvent être transmis comme un tableau de chaînes de caractères. Doit inclure au moins un numéro de téléphone (50 maximum). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

{% alert note %}
Notez que vous ne pouvez pas envoyer `emails` et `phones` dans la même section du groupe d’abonnement de l’appel. Envoyez plutôt `emails` ou `phones` avec les `external_ids`. Vous pouvez envoyer `emails`, `phones`, ou `external_ids` séparément.
{% endalert %}

## Exemple de demande d’e-mail et de SMS

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

## Exemple de demande d’e-mail

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
```

## Exemple de demande de SMS

```
curl --location --request POST 'https://rest.iad-01.braze.com/v2/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_groups":[
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "phones":["+12223334444","+15556667777”]
    }
  ]
}
```

{% endapi %}
