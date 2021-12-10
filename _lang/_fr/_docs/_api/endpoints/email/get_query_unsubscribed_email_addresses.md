---
nav_title: "GET: Liste de requêtes des adresses e-mail désabonnées"
article_title: "GET: Liste de requêtes des adresses e-mail désabonnées"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: Référence
description: "Cet article décrit l'utilisation et les paramètres pour l'utilisation du point de terminaison Get Email Unsubscribes Braze."
---

{% api %}
# Récupérer la liste ou les désinscriptions de l'e-mail de requête
{% apimethod get %}
/fr/email/désinscriptions
{% endapimethod %}

Utilisez le point de terminaison /email/unsubscribes pour renvoyer les e-mails qui se sont désabonnés pendant la période allant de `start_date` à `end_date`. Vous pouvez utiliser ce point de terminaison pour configurer une synchronisation bidirectionnelle entre Braze et d'autres systèmes de messagerie ou votre propre base de données.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d2966b81-188a-407b-ba7e-e6c252c44b4a {% endapiref %}

## Paramètres de la requête

Vous devez fournir un `end_date`, ainsi qu'un `email` ou un `start_date`.

| Paramètre       | Requis     | Type de données             | Libellé                                                                                                                                                                                                                                    |
| --------------- | ---------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `Date de début` | Optionnel* | Chaîne au format AAAA-MM-JJ | La date de début de la plage pour récupérer les désabonnés, doit être antérieure à la date de fin. Ceci est traité comme minuit en heure UTC par l'API.                                                                                    |
| `date_de fin`   | Optionnel* | Chaîne au format AAAA-MM-JJ | Date de fin de la plage pour récupérer les désabonnés. Ceci est traité comme minuit en heure UTC par l'API.                                                                                                                                |
| `limite`        | Optionnel  | Nombre entier               | Champ facultatif pour limiter le nombre de résultats retournés. La valeur par défaut est 100, le maximum est de 500.                                                                                                                       |
| `décalage`      | Optionnel  | Nombre entier               | Point de début optionnel dans la liste à récupérer de                                                                                                                                                                                      |
| `direction_tri` | Optionnel  | Chaîne de caractères        | Passez dans la valeur `asc` pour trier les désinscriptions de la plus ancienne à la plus récente. Passez dans `desc` pour trier du plus récent au plus ancien. Si sort_direction n'est pas incluse, l'ordre par défaut est le plus ancien. |
| `Email`         | Optionnel* | Chaîne de caractères        | Si fourni, nous retournerons si l'utilisateur s'est désabonné ou non                                                                                                                                                                       |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

Si votre plage de dates a plus de `limite` nombre de désabonnés, vous devrez effectuer plusieurs appels API, chaque fois en augmentant le décalage `` jusqu'à ce qu'un appel renvoie soit moins de `limite` ou zéro résultats.

## Exemple de demande
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/unsubscribes?start_date=2020-01-01&end_date=2020-02-01&limit=1&offset=1&sort_direction=desc&email=example@braze.com' \
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
      "unsubscribed_at": "2016-08-25 15:24:32 +0000"
    },
    {
      "email": "example2@braze. om",
      "unsubscribed_at": "2016-08-24 17:41:58 +0000"
    },
    {
      "email": "example3@braze. om",
      "unsubscribed_at": "2016-08-24 12:01:13 +0000"
    }
  ],
  "message": "success"
}
```
{% endapi %}
