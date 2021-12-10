---
nav_title: "GET: [Nom de la terminaise]"
page_order:
layout: api_page
excerpt_separator: ""
page_type: Référence
platform: API
channel:
  - Courriel
  - Pousser
tool:
  - Toile
  - Campagnes
description: "Cet article décrit l'utilisation et les paramètres pour utiliser le point de terminaison Get [endpoint name] Braze."
noindex: vrai
---

{% api %}
# Requête ou liste [Point de terminaison de l'élément "Gets"]

{% apimethod get %}
/fr/email/hard_bounces
{% endapimethod %}

Ceci est la description de la terminaison. Par exemple: "L'abonnement aux utilisateurs par courriel peut être mis à jour et récupéré via Braze en utilisant une API RESTful . Vous pouvez utiliser l'API pour configurer la synchronisation bidirectionnelle entre Braze et d'autres systèmes de messagerie ou votre propre base de données. Toutes les requêtes API sont effectuées via HTTPS."

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1614a82f-510a-4c37-95a6-8207a125e487 {% endapiref %}

## Paramètres de requête

Vous devez fournir un `end_date`, ainsi qu'un `email` ou un `start_date`.

| Paramètre       | Requis | Type de données             | Libellé                                                                                                                                                   |
| --------------- | ------ | --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Date de début` | Non *  | Chaîne au format AAAA-MM-JJ | La date de début de l'intervalle de récupération des rebonds durs doit être inférieure à `end_date`. Ceci est traité comme minuit en heure UTC par l'API. |
| `date_de fin`   | Non *  | Chaîne au format AAAA-MM-JJ | Date de fin de la plage pour récupérer les rebonds durs. Ceci est traité comme minuit en heure UTC par l'API.                                             |
| `limite`        | Non    | Nombre entier               | Champ facultatif pour limiter le nombre de résultats retournés. La valeur par défaut est 100, le maximum est de 500.                                      |
| `décalage`      | Non    | Nombre entier               | Point de début optionnel dans la liste à récupérer de                                                                                                     |
| `Email`         | Non *  | Chaîne de caractères        | Si fourni, nous retournerons si l'utilisateur a rebondi dur ou non                                                                                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

Si votre plage de dates a plus de `limite` nombre de bounces durs, vous devrez faire plusieurs appels API, chaque fois en augmentant le décalage `` jusqu'à ce qu'un appel renvoie soit moins de `limite` ou zéro résultats.

### Exemple de réponse

Les entrées sont listées en ordre décroissant.

```json
{
  "emails": [
    {
      "email": "foo@braze. om",
      "hard_bounced_at": "2016-08-25 15:24:32 +0000"
    },
    {
      "email": "bar@braze. om",
      "hard_bounced_at": "2016-08-24 17:41:58 +0000"
    },
    {
      "email": "baz@braze. om",
      "hard_bounced_at": "2016-08-24 12:01:13 +0000"
    }
  ],
  "message": "success"
}
```
{% endapi %}
