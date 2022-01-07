---
nav_title: "GET: Interrogation des e-mails rebondis"
article_title: "GET: Interrogation des e-mails rebondis"
search_tag: Endpoint
page_order: 0
layout: api_page
page_type: Référence
description: "Cet article décrit l'utilisation et les paramètres pour l'utilisation de la récupération d'une liste d'adresses de courriel rebondissant dur."
---

{% api %}
# Requête ou liste des e-mails rebondis
{% apimethod get %}
/fr/email/hard_bounces
{% endapimethod %}

Ce point de terminaison vous permet de tirer une liste d'adresses e-mail qui ont "rebondi dur" vos messages électroniques dans un certain laps de temps.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7c2ef84f-ddf5-451a-a72c-beeabc06ad9d {% endapiref %}

## Limite de taux

{% include rate_limits.md endpoint='default' %}

## Paramètres de la requête

Vous devez fournir soit un `start_date` et `end_date` OU un `email`.

Si vous fournissez un `start_date`, `end_date`, et un `email`, nous priorisons le ou les courriels donnés et négligeons la plage de dates.

| Paramètre       | Requis     | Type de données             | Libellé                                                                                                                                                   |
| --------------- | ---------- | --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Date de début` | Optionnel* | Chaîne au format AAAA-MM-JJ | La date de début de l'intervalle de récupération des rebonds durs doit être inférieure à `end_date`. Ceci est traité comme minuit en heure UTC par l'API. |
| `date_de fin`   | Optionnel* | Chaîne au format AAAA-MM-JJ | Date de fin de la plage pour récupérer les rebonds durs. Ceci est traité comme minuit en heure UTC par l'API.                                             |
| `limite`        | Optionnel  | Nombre entier               | Champ facultatif pour limiter le nombre de résultats retournés. La valeur par défaut est 100, le maximum est de 500.                                      |
| `décalage`      | Optionnel  | Nombre entier               | Point de début optionnel dans la liste à récupérer de                                                                                                     |
| `Email`         | Optionnel* | Chaîne de caractères        | Si fourni, nous retournerons si l'utilisateur a rebondi dur ou non                                                                                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

Si votre plage de dates a plus de `limite` de bounces durs, vous devrez faire plusieurs appels API, chaque fois en augmentant le décalage `` jusqu'à ce qu'un appel renvoie soit moins de `limite` ou zéro résultats.

## Exemple de demande
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/hard_bounces?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&email=example@braze.com' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Réponse
Les entrées sont listées en ordre décroissant.

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "emails": [
    {
      "email": "example1@braze. om",
      "hard_bounced_at": "2016-08-25 15:24:32 +0000"
    },
    {
      "email": "example2@braze. om",
      "hard_bounced_at": "2016-08-24 17:41:58 +0000"
    },
    {
      "email": "example3@braze. om",
      "hard_bounced_at": "2016-08-24 12:01:13 +0000"
    }
  ],
  "message": "success"
}
```
{% endapi %}
