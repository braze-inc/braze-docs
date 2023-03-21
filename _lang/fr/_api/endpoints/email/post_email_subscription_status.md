---
nav_title: "POST : modifier le statut de l’abonnement aux e-mails"
article_title: "POST : modifier le statut de l’abonnement aux e-mails"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "Cet article décrit l’utilisation et les paramètres de modification du statut d’abonnement d’un utilisateur à l’aide de l’endpoint Braze Post statut de l’abonnement aux e-mails."

---
{% api %}
# Modifier l’état de l’abonnement aux e-mails de l’utilisateur
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %} 
/email/status
{% endapimethod %}

Utilisez cet endpoint pour définir l’état de l’abonnement aux e-mails de vos utilisateurs. Les utilisateurs peuvent avoir le statut `opted_in`, `unsubscribed`, ou `subscribed` (sans confirmation d’abonnement/de désabonnement spécifique).

Vous pouvez définir l’état de l’abonnement aux e-mails pour une adresse e-mail qui n’est pas encore associée à l’un de vos utilisateurs dans Braze. Lorsque cette adresse e-mail est ensuite associée à un utilisateur, l’état de l’abonnement aux e-mails que vous avez téléchargé sera automatiquement défini.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#be852462-0cda-4a48-b68b-85bd8a9f2147 {% endapiref %}

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": "example@braze.com",
  "subscription_state": "subscribed"
}
```

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
| `email` | Requis | Chaîne de caractères ou tableau | Envoyez une adresse e-mail par chaîne de caractères ou un tableau de 50 adresses e-mail pour effectuer des modifications. |
| `subscription_state` | Requis | String | Soit « abonné », soit « désabonné » ou « opted_in ». |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/status' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "email": "example@braze.com",
  "subscription_state": "subscribed"
}'
```


{% endapi %}
