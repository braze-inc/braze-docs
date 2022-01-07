---
nav_title: "POST: Supprimer les adresses e-mail de la liste de spam"
article_title: "POST: Supprimer les adresses e-mail de la liste de spam"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: Référence
description: "Cet article décrit les détails sur et l'utilisation des adresses e-mail de la liste de spam Braze."
---

{% api %}
# Supprimer les adresses e-mail de la liste de spam
{% apimethod post %}
/fr/email/spam/remove
{% endapimethod %}

Ce point de terminaison vous permet de supprimer les adresses e-mail de votre liste de spam Braze. Nous les supprimerons également de la liste de spam maintenue par votre fournisseur de messagerie.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1614a82f-510a-4c37-95a6-8207a125e487 {% endapiref %}

## Limite de taux

{% include rate_limits.md endpoint='default' %}

## Corps de la requête
```
Type de contenu : application/json
Autorisation : Bearer YOUR-REST-API-KEY
```

```json
{
  "email": "exemple@braze.com"
}
```

## Paramètres de la requête

| Paramètre | Requis | Type de données   | Libellé                                                                             |
| --------- | ------ | ----------------- | ----------------------------------------------------------------------------------- |
| `Email`   | Requis | Chaîne ou tableau | Chaîne d'adresse e-mail à modifier, ou un tableau de 50 adresses e-mail à modifier. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/spam/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "email": "example@braze.com"
}'
```
{% endapi %}
