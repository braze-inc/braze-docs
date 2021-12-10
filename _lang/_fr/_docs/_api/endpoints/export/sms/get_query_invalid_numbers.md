---
nav_title: "GET: Requête de numéros de téléphone non valides"
article_title: "GET: Requête de numéros de téléphone non valides"
search_tag: Endpoint
page_order: 0
layout: api_page
page_type: Référence
description: "Cet article décrit l'utilisation et les paramètres pour utiliser la récupération d'une liste de numéros de téléphone non valides Braze point de terminal."
hidden: vrai
---

{% api %}
# Requête ou liste des numéros de téléphone invalides
{% apimethod get %}
/sms/invalid_phone_number
{% endapimethod %}

Ce point de terminaison vous permet de tirer une liste de numéros de téléphone qui ont été considérés comme « invalides » dans un certain laps de temps.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7c2ef84f-ddf5-451a-a72c-beeabc06ad9d {% endapiref %}
## Paramètres de la requête

Vous devez fournir soit un `start_date` et un `end_date` OU `phone_numbers`.

Si vous fournissez un `start_date`, un `end_date`, et `phone_numbers`, nous priorisons les numéros de téléphone donnés et négligeons la plage de date.

| Paramètre          | Requis     | Type de données             | Libellé                                                                                                                                                              |
| ------------------ | ---------- | --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Date de début`    | Optionnel* | Chaîne au format AAAA-MM-JJ | Date de début de la plage pour récupérer des numéros de téléphone invalides, doit être antérieure à `end_date`. Ceci est traité comme minuit en heure UTC par l'API. |
| `date_de fin`      | Optionnel* | Chaîne au format AAAA-MM-JJ | Date de fin de l'intervalle pour récupérer des numéros de téléphone non valides. Ceci est traité comme minuit en heure UTC par l'API.                                |
| `limite`           | Optionnel  | Nombre entier               | Champ facultatif pour limiter le nombre de résultats retournés. La valeur par défaut est 100, le maximum est de 500.                                                 |
| `décalage`         | Optionnel  | Nombre entier               | Point de début optionnel dans la liste à récupérer.                                                                                                                  |
| `numéro_téléphone` | Optionnel* | Tableau                     | Si fourni, nous retournerons si ces numéros de téléphone ont été détectés ou non comme des numéros de téléphone non valides.                                         |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

Si votre plage de dates a plus que la `limite` nombre de numéros de téléphone invalides, vous devrez faire plusieurs appels API en augmentant le `décalage` à chaque fois jusqu'à ce qu'un appel renvoie soit moins de `limite` ou zéro résultats.

## Exemple de demande
```
curl --location --request GET 'https://rest.iad-01.braze.com/sms/invalid_phone_numbers?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&phone_numbers[]=12345678901' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Réponse
Les entrées sont listées en ordre décroissant.

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "sms": [
    {
      "phone": "12345678900",
      "invalid_detected_at": "2016-08-25 15:24:32 +0000"
    },
    {
      "téléphone": "12345678901",
      "invalid_detected_at": "2016-08-24 17:41:58 +0000"
    },
    {
      "téléphone": "12345678902",
      "invalid_detected_at": "2016-08-24 12:01:13 +0000"
    }
  ],
  "message": "success"
}
```
{% endapi %}