---
nav_title: "POST : Mettre à jour le statut du groupe d'abonnement des utilisateurs v2"
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

Vous pouvez accéder au site `subscription_group_id` d'un groupe d'abonnement en accédant à la page **Groupe d'abonnement**.

Pour consulter des exemples ou tester cet endpoint pour **les groupes d'abonnement par e-mail** :

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#b1b9a0e0-6329-4df2-a465-53347f410662 {% endapiref %}

Pour consulter des exemples ou tester cet endpoint pour **les groupes d'abonnement SMS** :

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#81a5fe65-588b-4b61-82d8-5ce68b681409 {% endapiref %}

Pour consulter des exemples ou tester cet endpoint pour **les groupes WhatsApp** :

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#81a5fe65-588b-4b61-82d8-5ce68b681409 {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, il est nécessaire de disposer d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l'autorisation`subscription.status.set`requise.

{% alert note %}
Si vous souhaitez utiliser cet endpoint avec [les groupes d'abonnement LINE]({{site.baseurl}}/user_guide/message_building_by_channel/line/line_users/subscription_groups/), veuillez contacter votre gestionnaire de la satisfaction client.
{% endalert %}

## Différences par rapport à la version 1

L'endpoint V2 diffère de l'[endpoint]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) [V1]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) de la manière suivante :

- **Groupes d'abonnement multiples** : La version 2 vous permet de mettre à jour plusieurs groupes d'abonnement en une seule requête API, tandis que la version 1 ne prend en charge qu'un seul groupe d'abonnement par requête.
- **Veuillez mettre à jour à la fois votre adresse e-mail et votre numéro de téléphone par SMS en un seul appel** : Lorsque vous utilisez `external_ids`, vous pouvez mettre à jour les groupes d'abonnement par e-mail et par SMS pour les mêmes utilisateurs en un seul appel API. Avec la version 1, il est nécessaire d'effectuer des appels API distincts pour les groupes d'abonnement par e-mail et par SMS.
- **Utilisation des identifiants de e-mail ou de téléphone** : Si vous utilisez`emails`  ou`phones`  au lieu de `external_ids`, il n'est pas possible de mettre à jour à la fois les groupes d'abonnement par e-mail et par SMS dans la même requête. Il est nécessaire d'effectuer des appels API distincts : un pour les groupes d'abonnement par e-mail et un autre pour les groupes d'abonnement par SMS.

{% alert important %}
**Format du numéro de téléphone** : Les numéros de téléphone doivent être au[E.164](https://en.wikipedia.org/wiki/E.164)[format](https://en.wikipedia.org/wiki/E.164) (par exemple, `+12223334444`). Les numéros de téléphone qui ne sont pas auE.164format  sont refusés.
{% endalert %}

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

{% alert tip %}
Lorsque vous créez de nouveaux utilisateurs à l'aide de l'[endpoint`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), vous pouvez définir des groupes d'abonnement dans l'objet des attributs de l'utilisateur, ce qui vous permet de créer un utilisateur et de définir l'état du groupe d'abonnement en un seul appel d'API.
{% endalert %}

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| [`subscription_group_id`]({{site.baseurl}}/api/identifier_types/?tab=subscription%20group%20ids) | Requis | Chaîne de caractères | L’`id` de votre groupe d’abonnement. |
| `subscription_state` | Requis | Chaîne de caractères | Les valeurs disponibles sont `unsubscribed` (pas dans le groupe d’abonnement) ou `subscribed` (dans le groupe d’abonnement). |
| `external_ids` | Obligatoire* | Tableau de chaînes de caractères | L’`external_id` de l’utilisateur ou des utilisateurs (50 `id`s max). |
| `emails` | Obligatoire* | Chaîne de caractères ou tableau de chaînes de caractères | L’adresse e-mail de l’utilisateur peut être transmise comme un tableau de chaînes de caractères. Doit inclure au moins une adresse e-mail (maximum 50). <br><br>Si plusieurs utilisateurs (`external_id`) du même espace de travail partagent la même adresse e-mail, tous les utilisateurs qui partagent l'adresse e-mail sont mis à jour avec les modifications apportées au groupe d'abonnement. |
| `phones` | Obligatoire* | Chaîne de caractères dans [E.164](https://en.wikipedia.org/wiki/E.164) format | Vous pouvez transmettre les numéros de téléphone des utilisateurs sous forme de tableau de chaînes de caractères. Vous devez inclure au moins un numéro de téléphone (jusqu'à 50). Les numéros de téléphone doivent être auE.164format (par exemple, `+12223334444`). <br><br>Si plusieurs utilisateurs (`external_id`) du même espace de travail partagent le même numéro de téléphone, tous les utilisateurs qui partagent le numéro de téléphone sont mis à jour avec les mêmes changements de groupe d'abonnement.|
| `use_double_opt_in_logic` | Facultatif | Valeur booléenne | Si ce paramètre est omis ou défini sur `false`, les utilisateurs ne sont pas intégrés au processus d’abonnement par SMS. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert important %}
**Sélection de l'identifiant** : 
- Pour mettre à jour les groupes d'abonnement aux e-mails et aux SMS en un seul appel API, veuillez utiliser `external_ids`. Il n'est pas possible d'inclure à la fois`emails`  et`phones`  dans la même requête.
- Si vous utilisez`emails`  ou`phones`  au lieu de `external_ids`, veuillez effectuer des appels API distincts : un pour les groupes d'abonnement par e-mail et un pour les groupes d'abonnement par SMS.
- Vous pouvez envoyer `emails`, `phones`, ou`external_ids`  individuellement.
{% endalert %}

### Exemple de requêtes

L'exemple suivant utilise`external_ids`  pour mettre à jour les groupes d'abonnement par e-mail et par SMS en un seul appel API. Cela n'est possible que lorsque vous utilisez `external_ids`— vous ne pouvez pas mettre à jour à la fois les groupes d'abonnement par e-mail et par SMS en un seul appel lorsque vous utilisez`emails`ou `phones`.

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
