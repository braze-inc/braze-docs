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

Utilisez cet endpoint pour mettre à jour en masse le statut d’abonnement jusqu’à 50 utilisateurs sur le tableau de bord de Braze. Vous pouvez accéder à un groupe d’abonnement `subscription_group_id` en accédant à la page **Groupe d’abonnements**.

Si vous souhaitez voir des exemples ou tester cet endpoint pour les **groupes d’abonnement aux e-mails** :

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#8895e87e-6324-47a3-a833-adf29a258bb9 {% endapiref %}

Si vous souhaitez voir des exemples ou tester cet endpoint pour les **groupes d’abonnement aux SMS** :

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#72558b32-7dbe-4cba-bd22-a7ce513076dd {% endapiref %}

## Limites de débit

{% multi_lang_include rate_limits.md endpoint='subscription status set' %}

## Corps de la demande

{% tabs %}
{% tab SMS %}
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
   "subscription_group_id": (required, string) L’ID de votre groupe d’abonnement,
   "subscription_state": (required, string) les valeurs disponibles sont « unsubscribed » (désinscrit) (n’appartenant pas à un groupe d’abonnement) ou « subscribed » (inscrit) (appartenant à un groupe d’abonnement),,
   "external_id": (required*, array of strings) le external_id de l’utilisateur ou des utilisateurs, peut inclure jusqu’à 50 identifiants.,
   "phone": (required*, array of strings in E.164 format) Le numéro de téléphone de l’utilisateur (doit comprendre au moins un et au maximum 50 numéros de téléphone),
   // Groupe d’abonnement SMS ; un external_id ou un téléphone est nécessaire
 }
```
\* Groupes d’abonnement aux SMS : Uniquement `external_id` ou `phone` est accepté.

{% endtab %}
{% tab E-mail %}
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
   "subscription_group_id": (required, string) L’ID de votre groupe d’abonnement,
   "subscription_state": (required, string) les valeurs disponibles sont « unsubscribed » (désinscrit) (n’appartenant pas à un groupe d’abonnement) ou « subscribed » (inscrit) (appartenant à un groupe d’abonnement),,
   "external_id": (required*, array of strings) le external_id de l’utilisateur ou des utilisateurs, peut inclure jusqu’à 50 identifiants.,
   "email": (required*, array of strings) l’adresse e-mail de l’utilisateur (doit comprendre au moins un et au maximum 50 e-mails),
   // Groupe d’abonnement par e-mail ; un external_id ou un e-mail est nécessaire
   // Remarquez qu’envoyer une adresse e-mail qui est liée à plusieurs profils mettra à jour tous les profils pertinents.
 }
```
\* Groupes d’abonnement aux e-mails : `email` ou `external_id` est nécessaire.
{% endtab %}
{% endtabs %}

Cette propriété ne doit pas être utilisée pour mettre à jour les informations de profil d’un utilisateur. Utiliser la propriété [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) plutôt.

{% alert tip %}
Lorsque vous créez de nouveaux utilisateurs au moyen de l’endpoint [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), vous pouvez définir des groupes d'abonnement dans l’objet attributs d’utilisateur, ce qui vous permet de créer un utilisateur et de définir l’état du groupe d’abonnement dans un seul appel API.
{% endalert %}

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `subscription_group_id` | Requis | String | Le `id` de votre groupe d’abonnement. |
| `subscription_state` | Requis | String | Les valeurs disponibles sont `unsubscribed` (pas dans le groupe d’abonnement) ou `subscribed` (dans le groupe d’abonnement). |
| `external_id` | Requis* | Tableau de chaînes de caractères | Le `external_id` de l’utilisateur ou des utilisateurs, peut inclure jusqu’à 50 `id`s. |
| `email` | Requis* | String or array of strings | L’adresse e-mail de l’utilisateur peut être transmise comme un tableau de chaînes de caractères. Doit inclure au moins une adresse e-mail (maximum 50). <br><br>Si plusieurs utilisateurs (`external_id`) dans le même groupe d’apps partagent la même adresse e-mail, alors tous les utilisateurs qui partagent l’adresse e-mail sont mis à jour avec les modifications du groupe d’abonnement. |
| `phone` | Requis* | Chaîne de caractères au format [E.164](https://en.wikipedia.org/wiki/E.164) | Le numéro de téléphone de l’utilisateur peut être transmis comme un tableau de chaînes de caractères. Doit inclure au moins un numéro de téléphone (maximum 50). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande d’e-mail
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

## Exemple de demande de SMS
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

Response: (statut 201)

```json
{
    "message": "success"
}
```

{% alert important %}
L’endpoint accepte uniquement la valeur `email` ou `phone`, et non les deux. Si vous disposez des deux, vous recevrez cette réponse : `{"message":"Une adresse e-mail ou un numéro de téléphone doit être fourni, mais pas les deux."}`
{% endalert %}

{% endapi %}

