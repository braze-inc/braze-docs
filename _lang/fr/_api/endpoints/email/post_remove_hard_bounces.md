---
nav_title: "POST : Supprimer les e-mails avec rebond élevé"
article_title: "POST : Supprimer les e-mails avec rebond élevé"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Supprimer les adresses e-mail avec rebond élevé et son utilisation."

---
{% api %}
# Supprimer les rebonds élevés
{% apimethod post %}
/email/bounce/remove
{% endapimethod %}

Utilisez cet endpoint pour supprimer les adresses e-mail de votre liste de rebonds de Braze. Nous les supprimerons également de la liste de diffusion conservée par votre fournisseur de messagerie.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7b87a884-fa20-4085-b9f1-18363103575f {% endapiref %}

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": "example@braze.com"
}
```

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| ----------|-----------| ---------|------ |
| `email` | Requis | Chaîne de caractères ou tableau | Envoyez une adresse e-mail par chaîne de caractères ou un tableau de 50 adresses e-mail pour effectuer des modifications. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/bounce/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "email": "example@braze.com"
}'
```

{% endapi %}
