---
nav_title: "POST: Supprimer les numéros de téléphone non valides"
article_title: "POST: Supprimer les numéros de téléphone non valides"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "Cet article décrit l'utilisation et les paramètres pour l'utilisation de ce point de terminaison Braze pour supprimer une liste de numéros de téléphone non valides."
---

{% api %}
# Supprimer les numéros de téléphone non valides
{% apimethod post %}
/fr/sms/invalid_phone_numbers/remove
{% endapimethod %}

Ce point de terminaison vous permet de supprimer les numéros de téléphone « invalides » de la liste invalide de Brase. Ceci peut être utilisé pour revalider les numéros de téléphone après qu'ils aient été marqués comme non valides.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#76495aac-8c2d-4e1a-8cac-12e3856ab1d3 {% endapiref %}

## Corps de la requête

```
Type de contenu : application/json
Autorisation : Bearer YOUR-REST-API-KEY
```

```json
{
  "phone_numbers": ["12183095514","142555512"]
}
```

## Paramètres de la requête

| Paramètre          | Requis | Type de données                    | Libellé                                           |
| ------------------ | ------ | ---------------------------------- | ------------------------------------------------- |
| `numéro_téléphone` | Requis | Tableau de chaînes au format e.164 | Un tableau de 50 numéros de téléphone à modifier. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande

```
curl --location --request POST 'https://rest.iad-01.braze. om/sms/invalid_phone_numbers/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "phone_numbers" : ["12183095514","142555512"]
}'
```

{% endapi %}
