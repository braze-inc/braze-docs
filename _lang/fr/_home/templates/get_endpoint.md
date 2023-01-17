---
nav_title: "GET : [Nom de l’endpoint]"
article_title: "GET : [Nom de l’endpoint]"
search_tag: Endpoint

page_order: 1
excerpt_separator: ""

layout: api_page
page_type: reference
description: "Cet article décrit l’utilisation et les paramètres pour se servir de l’endpoint Braze Get [nom de l’endpoint]."

noindex: true
#ATTENTION: supprimer le noindex et l’alerte de ce modèle
---
{% api %}
# Requête ou liste [Endpoint de produit "Gets"]

{% apimethod get %}
/sms/invalid_phone_numbers
{% endapimethod %}

<!--
This is the description of the endpoint. API descriptions usually start with "Use this endpoint to..."-->
Cet endpoint vous permet d’extraire une liste des numéros de téléphone considérés comme « non valides » dans un certain laps de temps.

<!-- Your postman link. Once you have published the endpoint to postman, you will be able get a direct link to the info in the postman docs to share here-->
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1614a82f-510a-4c37-95a6-8207a125e487 {% endapiref %}

## Limites de débit

<!-- The rate limit of the endpoint. This pulls from /includes/rate_limits/ and displays specific endpoint limits based on the endpoint provided -->
{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de demande

<!--This is where you can give more information about your endpoint parameters. -->

| Paramètre | Requis | Type de données | Description |
| ----------|-----------| ----------|----- |
| `start_date` | Facultatif <br>(voir la note) | Chaîne de caractères au format AAAA-MM-JJ| La date de début de la plage pour récupérer les numéros de téléphone non valides doit être antérieure à `end_date`. Ce traitement est effectué à minuit (UTC) par l’API. |
| `end_date` | Facultatif <br>(voir la note) | Chaîne de caractères au format AAAA-MM-JJ | Date de fin de la plage pour récupérer les numéros de téléphone non valides. Ce traitement est effectué à minuit (UTC) par l’API. |
| `limit` | Facultatif | Entier | Champ facultatif pour limiter le nombre de résultats renvoyés. Par défaut à 100, le maximum est 500. |
| `offset` | Facultatif | Entier | Point de départ facultatif dans la liste où récupérer les informations. |
| `phone_numbers` | Facultatif <br>(voir la note) | Tableau de chaînes de caractères au format e.164 | S’il est fourni, nous renverrons le numéro de téléphone s’il s’avère non valide. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% alert note %}
Vous devez fournir une `start_date` et une `end_date`, OU un `phone_numbers`. Si vous fournissez les trois, une `start_date`, une `end_date`, et un `phone_numbers`, nous donnerons la priorité aux numéros de téléphone communiqués et ignorerons la plage de dates.
{% endalert %}

## Exemple de demande

<!--The following example demonstrates a request that will pull a list of phone numbers that have been deemed invalid via the API:-->
```
curl --location --request GET 'https://rest.iad-01.braze.com/sms/invalid_phone_numbers?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&phone_numbers[]=12345678901' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Réponse

<!-- An example response that defines the different variables returned-->
```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "sms": [
    {
      "phone": (chaîne de caractères) le numéro de téléphone au format E.164,
      "invalid_detected_at": (chaîne de caractères) l’heure à laquelle le numéro invalide a été détecté dans le format ISO 8601
    },
    {
      "phone": (chaîne de caractères) le numéro de téléphone au format E.164,
      "invalid_detected_at": (chaîne de caractères) l’heure à laquelle le numéro invalide a été détecté dans le format ISO 8601
    },
    {
      "phone": (chaîne de caractères) le numéro de téléphone au format E.164,
      "invalid_detected_at": (chaîne de caractères) l’heure à laquelle le numéro invalide a été détecté dans le format ISO 8601
    }
  ],
  "message": "réussite"
}
```

{% endapi %}
