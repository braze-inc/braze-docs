---
nav_title: "POST : Mettre à jour le statut du groupe d’abonnement de l’utilisateur"
article_title: "POST : Mettre à jour le statut du groupe d’abonnement de l’utilisateur"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Mettre à jour le statut du groupe d’abonnement de l’utilisateur."
---
{% api %}
# Mettre à jour le statut du groupe d’abonnement de l’utilisateur
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/subscription/status/set
{% endapimethod %}

> Utilisez cet endpoint pour mettre à jour en masse le statut d’abonnement jusqu’à 50 utilisateurs sur le tableau de bord de Braze. 

Vous pouvez accéder au site `subscription_group_id` d'un groupe d'abonnement en accédant à la page **Groupe d'abonnement**.

Si vous souhaitez voir des exemples ou tester cet endpoint pour les **groupes d'abonnement e-mail**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#8895e87e-6324-47a3-a833-adf29a258bb9 {% endapiref %}

Si vous souhaitez voir des exemples ou tester cet endpoint pour les **groupes d'abonnement SMS et RCS :**

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#72558b32-7dbe-4cba-bd22-a7ce513076dd {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `subscription.status.set`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='subscription status set' %}

## Corps de la demande

{% tabs %}
{% tab SMS et RCS %}
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
   "subscription_group_id": (required, string) the id of your subscription group,
   "subscription_state": (required, string) available values are "unsubscribed" (not in subscription group) or "subscribed" (in subscription group),
   "external_id": (required*, array of strings) the external ID of the user or users, may include up to 50 IDs,
   "phone": (required*, array of strings in E.164 format) The phone number of the user (must include at least one phone number and at most 50 phone numbers),
   // SMS and RCS subscription group - one of external_id or phone is required
 }
```
\* groupes d'abonnement SMS et RCS : Uniquement `external_id` ou `phone` est accepté.

{% endtab %}
{% tab E-mail %}
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
   "subscription_group_id": (required, string) the id of your subscription group,
   "subscription_state": (required, string) available values are "unsubscribed" (not in subscription group) or "subscribed" (in subscription group),
   "external_id": (required*, array of strings) the external ID of the user or users, may include up to 50 IDs,
   "email": (required*, array of strings) the email address of the user (must include at least one email and at most 50 emails),
   // Email subscription group - one of external_id or email is required
   // Note that sending an email address that is linked to multiple profiles will update all relevant profiles
 }
```
\* Groupes d'abonnement e-mail : `email` ou `external_id` est nécessaire.
{% endtab %}
{% endtabs %}

Cette propriété ne doit pas être utilisée pour mettre à jour les informations de profil d’un utilisateur. Utilisez plutôt la propriété [/users/track.]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) 

{% alert tip %}
Lorsque vous créez de nouveaux utilisateurs à l'aide de l'endpoint [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), vous pouvez définir des groupes d'abonnement dans l'objet des attributs de l'utilisateur, ce qui vous permet de créer un utilisateur et de définir l'état du groupe d'abonnement en un seul appel d'API.
{% endalert %}

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| [`subscription_group_id`]({{site.baseurl}}/api/identifier_types/?tab=subscription%20group%20ids) | Requis | Chaîne de caractères | L’`id` de votre groupe d’abonnement. |
| `subscription_state` | Requis | Chaîne de caractères | Les valeurs disponibles sont `unsubscribed` (pas dans le groupe d’abonnement) ou `subscribed` (dans le groupe d’abonnement). |
| `external_id` | Obligatoire* | Tableau de chaînes de caractères | L’`external_id` de l’utilisateur ou des utilisateurs (50 `id`s max). |
| `email` | Obligatoire* | Chaîne de caractères ou tableau de chaînes de caractères | L’adresse e-mail de l’utilisateur peut être transmise comme un tableau de chaînes de caractères. Doit inclure au moins une adresse e-mail (maximum 50). <br><br>Si plusieurs utilisateurs (`external_id`) d'un même espace de travail partagent la même adresse e-mail, tous les utilisateurs qui partagent cette adresse sont mis à jour en fonction des modifications apportées au groupe d'abonnement. |
| `phone` | Obligatoire* | Chaîne de caractères dans [E.164](https://en.wikipedia.org/wiki/E.164) format | Le numéro de téléphone de l’utilisateur peut être transmis comme un tableau de chaînes de caractères. Vous devez inclure au moins un numéro de téléphone (jusqu'à 50). <br><br>Si plusieurs utilisateurs (`external_id`) du même espace de travail partagent le même numéro de téléphone, tous les utilisateurs qui partagent le numéro de téléphone sont mis à jour avec les mêmes changements de groupe d'abonnement. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemple de requêtes

### E-mail

```
curl --location --request POST 'https://rest.iad-01.braze.com/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_group_id": "subscription_group_identifier",
  "subscription_state": "unsubscribed",
  "external_id": "external_identifier",
  "email": ["example1@email.com", "example2@email.com"]
}
'
```

### SMS et RCS

```
curl --location --request POST 'https://rest.iad-01.braze.com/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_group_id": "subscription_group_identifier",
  "subscription_state": "unsubscribed",
  "external_id": "external_identifier",
  "phone": ["+12223334444", "+11112223333"]
}
'
```

## Exemple de réponse réussie

Le code de statut `201` pourrait renvoyer le corps de réponse suivant.

```json
{
    "message": "success"
}
```

{% alert important %}
L’endpoint accepte uniquement la valeur `email` ou `phone`, et non les deux. Si vous disposez des deux, vous recevrez cette réponse : `{"message":"Either an email address or a phone number should be provided, but not both."}`
{% endalert %}

{% endapi %}

