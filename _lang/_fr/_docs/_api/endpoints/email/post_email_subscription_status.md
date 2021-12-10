---
nav_title: "POST: Changer le statut d'abonnement à l'email"
article_title: "POST: Changer le statut d'abonnement à l'email"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: Référence
description: "Cet article décrit l'utilisation et les paramètres pour changer le statut d'abonnement d'un utilisateur avec le point de terminaison de statut d'abonnement à l'email postal."
---

{% api %}
# Changer le statut d'abonnement aux emails de l'utilisateur
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/email/status
{% endapimethod %}

Ce point de terminaison vous permet de définir l'état d'abonnement à vos utilisateurs. Les utilisateurs peuvent être `opted_in`, `désabonnés`, ou `abonnés` (pas spécifiquement optés dans ou non).

Vous pouvez définir l'état d'abonnement aux e-mails pour une adresse e-mail qui n'est pas encore associée à aucun de vos utilisateurs au Brésil. Lorsque cette adresse e-mail est associée par la suite à un utilisateur, le statut d'abonnement à l'e-mail que vous avez téléchargé sera automatiquement défini.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#be852462-0cda-4a48-b68b-85bd8a9f2147 {% endapiref %}

## Corps de la requête

```
Type de contenu : application/json
Autorisation : Bearer YOUR-REST-API-KEY
```

```json
{
  "email": "example@braze.com",
  "subscription_state": "subscribed"
}
```

## Paramètres de la requête

| Paramètre              | Requis | Type de données      | Libellé                                                                             |
| ---------------------- | ------ | -------------------- | ----------------------------------------------------------------------------------- |
| `Email`                | Requis | Chaîne ou tableau    | Chaîne d'adresse e-mail à modifier, ou un tableau de 50 adresses e-mail à modifier. |
| `état de l'abonnement` | Requis | Chaîne de caractères | Soit "abonné", "désabonné", soit "opted_in".                                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/status' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "email": "example@braze. om",
  "subscription_state": "subscribed"
}'
```


{% endapi %}
