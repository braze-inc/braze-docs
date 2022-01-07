---
nav_title: "GET: Liste des identifiants de produits"
article_title: "GET: Liste des identifiants de produits"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: Référence
description: "Cet article décrit les détails sur la liste des identifiants de produits Braze terminal."
---

{% api %}
# Liste des ID de terminaison du produit
{% apimethod get %}
/fr/purchases/product_list
{% endapimethod %}

Ce point de terminaison renvoie les listes paginées des identifiants de produit.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#dff4ed40-81f5-451d-9d44-accc0e932285{% endapiref %}

## Limite de taux

{% include rate_limits.md endpoint='purchases product list' %}

## Paramètres de la requête

| Paramètre | Requis    | Type de données      | Libellé                                                          |
| --------- | --------- | -------------------- | ---------------------------------------------------------------- |
| `page`    | Optionnel | Chaîne de caractères | La page de votre liste de produits que vous souhaitez consulter. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande

{% raw %}
```
https://rest.iad-01.braze.com/purchases/product_list?page=1
```
{% endraw %}

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "products": [
    "5499334426779",
    "5499334819995",
    "5499335442587",
    "5499335835803",
    "Peau de Masque de Calendula",
    "Glose de Lièvre Dior",
    "Bol de riz",
    "nom_du_produit"
  ],
  "message": "succès"
}
```

{% endapi %}
