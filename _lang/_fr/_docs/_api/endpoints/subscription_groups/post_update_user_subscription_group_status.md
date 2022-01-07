---
nav_title: "POST: Mettre à jour le statut du groupe d'abonnement de l'utilisateur"
article_title: "POST: Mettre à jour le statut du groupe d'abonnement de l'utilisateur"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: Référence
description: "Cet article décrit les détails sur le point de terminaison du statut de groupe d'abonnement de l'utilisateur de mise à jour."
---

{% api %}
# Mettre à jour le statut du groupe d'abonnement des utilisateurs
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/fr/subscription/status/set
{% endapimethod %}

Utilisez les points de terminaison ci-dessous pour mettre à jour l'état d'abonnement de jusqu'à 50 utilisateurs sur le tableau de bord Braze. Vous pouvez accéder à un groupe d'abonnements `subscription_group_id` en y naviguant sur la page du Groupe d'Abonnement.

Si vous voulez voir des exemples ou tester ce point de terminaison pour les __Groupes d'abonnement par e-mail__:

{% apiref postman %}https://documentmenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#8895e87e-6324-47a3-a833-adf29a258bb9 {% endapiref %}

Si vous voulez voir des exemples ou tester ce point de terminaison pour __SMS Subscription Groups__:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#72558b32-7dbe-4cba-bd22-a7ce513076dd {% endapiref %}

## Limite de taux

{% include rate_limits.md endpoint='default' %}

## Corps de la requête

{% tabs %}
{% tab SMS %}
```
Type de contenu : application/json
Autorisation : Bearer YOUR-REST-API-KEY
```

```json
{
   "subscription_group_id": (requis, chaîne) l'id de votre groupe d'abonnement,
   "subscription_state": (requis, chaîne) les valeurs disponibles sont “unsubscribed” (pas dans le groupe d'abonnement) ou “subscribed” (dans le groupe d'abonnement),
   "external_id" : (obligatoire*, table de chaînes) l'id externe de l'utilisateur ou des utilisateurs, peut inclure jusqu'à 50 ids,
   "phone": (required*, tableau de chaînes de caractères en E. 64 format) Le numéro de téléphone de l'utilisateur (doit inclure au moins un numéro de téléphone et au plus 50 numéros de téléphone),
   // Groupe d'abonnement SMS - un de external_id ou téléphone est requis
}
```
\* Les groupes d'abonnement SMS : seuls `external_id` ou `téléphone` sont acceptés.

{% endtab %}
{% tab Email %}
```
Type de contenu : application/json
Autorisation : Bearer YOUR-REST-API-KEY
```

```json
{
   "subscription_group_id": (requis, chaîne) l'id de votre groupe d'abonnement,
   "subscription_state": (requis, chaîne) les valeurs disponibles sont “unsubscribed” (pas dans le groupe d'abonnement) ou “subscribed” (dans le groupe d'abonnement),
   "external_id" : (obligatoire*, table de chaînes) l'id externe de l'utilisateur ou des utilisateurs, peut inclure jusqu'à 50 ids,
   "email": (obligatoire*, tableau de chaînes) l'adresse email de l'utilisateur (doit inclure au moins un email et au plus 50 emails),
   // Groupe d'abonnement aux e-mails - un de external_id ou email est requis
   // Veuillez noter que l'envoi d'une adresse e-mail liée à plusieurs profils mettra à jour tous les profils pertinents
}
```
\* Groupes d'abonnement aux e-mails : soit `email` soit `external_id` est requis.
{% endtab %}
{% endtabs %}

Cette propriété ne doit pas être utilisée pour mettre à jour les informations de profil d'un utilisateur. Veuillez utiliser la propriété [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) à la place.

{% alert important %}
Lors de la création de nouveaux utilisateurs via le point de terminaison [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) , vous devriez laisser un délai d'environ 2 minutes avant d'ajouter des utilisateurs au groupe d'abonnement concerné afin de laisser à Braze le temps de créer pleinement le profil de l'utilisateur.
{% endalert %}

## Paramètres de la requête

| Paramètre                   | Requis       | Type de données                                               | Libellé                                                                                                                                                                                                                                                                                                                                                                                                                  |
| --------------------------- | ------------ | ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `ID de groupe d'abonnement` | Requis       | Chaîne de caractères                                          | L'id `` de votre groupe d'abonnement.                                                                                                                                                                                                                                                                                                                                                                                    |
| `état de l'abonnement`      | Requis       | Chaîne de caractères                                          | Les valeurs disponibles sont `désabonnés` (pas dans le groupe d'abonnement) ou `abonné` (dans le groupe d'abonnements).                                                                                                                                                                                                                                                                                                  |
| `id externe`                | Obligatoire* | Tableau de chaînes                                            | Le `external_id` de l'utilisateur ou des utilisateurs, peut inclure jusqu'à 50 `id`s.                                                                                                                                                                                                                                                                                                                                    |
| `Email`                     | Obligatoire* | Chaîne de caractères                                          | L'adresse email de l'utilisateur, peut être passée sous la forme d'un tableau de chaînes. Doit inclure au moins une adresse e-mail (avec un maximum de 50). <br><br>Si plusieurs utilisateurs (`external_id`) dans le même groupe d'applications partagent la même adresse e-mail, alors tous les utilisateurs qui partagent l'adresse e-mail sont mis à jour avec les modifications du groupe d'abonnement. |
| `Téléphone`                 | Obligatoire* | Chaîne au format [E.164](https://en.wikipedia.org/wiki/E.164) | Le numéro de téléphone de l'utilisateur, peut être passé sous la forme d'un tableau de chaînes. Doit inclure au moins un numéro de téléphone (avec un maximum de 50).                                                                                                                                                                                                                                                    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de courrier électronique des demandes
```
curl --location --request POST 'https://rest.iad-01.braze. om/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_group_id": "subscription_group_identifier",
  "subscription_state": "unsubscribed",
  "external_id": "example-user",
  "email": ["example1@email. om", "example2@email.com"]
}
'
```

## Exemple de demandes SMS
```
curl --location --request POST 'https://rest.iad-01.braze. om/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_group_id": "subscription_group_identifier",
  "subscription_state": "unsubscribed",
  "external_id": "external_identifier",
  "phone": ["+12223334444", "+11112223333"]
}

```

## Exemple de réponse réussie

Réponse : (statut 201)

```json
{
    "message": "success"
}
```

{% alert important %}
Le point de terminaison n'accepte que la valeur `e-mail` ou `téléphone` , pas les deux. Si vous recevez les deux, vous recevrez cette réponse : `{"message":"Soit une adresse e-mail soit un numéro de téléphone doit être fourni, mais pas les deux."}`
{% endalert %}

{% endapi %}

