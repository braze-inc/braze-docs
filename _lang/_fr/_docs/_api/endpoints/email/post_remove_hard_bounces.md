---
nav_title: "POST: Supprimer les e-mails rebondis"
article_title: "POST: Supprimer les e-mails rebondis"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: Référence
description: "Cet article décrit les détails à propos et l'utilisation du point de terminaison Supprimer les adresses de courriel rendues difficiles Braze."
---

{% api %}
# Supprimer les rebonds durs
{% apimethod post %}
/fr/email/bounce/remove
{% endapimethod %}

Ce point de terminaison vous permet de supprimer les adresses e-mail de votre liste de rebond de Braze. Nous les retirerons également de la liste de rebond maintenue par votre fournisseur de messagerie.

{% apiref postman %}https://documentmenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7b87a884-fa20-4085-b9f1-18363103575f {% endapiref %}

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
curl --location --request POST 'https://rest.iad-01.braze.com/email/bounce/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "email": "example@braze.com"
}'
```

{% endapi %}
