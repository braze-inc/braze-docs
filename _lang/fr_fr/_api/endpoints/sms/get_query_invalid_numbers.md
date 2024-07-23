---
nav_title: "GET : Extraire les numéros de téléphone non valides"
article_title: "GET : Extraire les numéros de téléphone non valides"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Interroger les numéros de téléphone non valides."
---
{% api %}
# Extraire les numéros de téléphone non valides
{% apimethod get %}
/sms/invalid_phone_numbers
{% endapimethod %}

> Utilisez ce point de terminaison pour extraire une liste de numéros de téléphone qui ont été marqués « invalides » au cours d'une certaine période. Consultez la documentation [sur la gestion des numéros de téléphone invalides]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#handling-invalid-phone-numbers) pour plus d’informations.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#81ceae19-15d1-4ac1-ad22-a6b86a92456d {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `sms.invalid_phone_numbers`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de demande

| Paramètre | Obligatoire | Type de données | Descriptif |
| ----------|-----------| ----------|----- |
| `start_date` | Facultatif <br>(voir remarque) | Chaîne au format AAAA-MM-JJ| La date de début de la plage pour récupérer les numéros de téléphone invalides doit être antérieure à `end_date`. Ce traitement est effectué à minuit (UTC) par l’API.
| `end_date` | Optional <br>(voir remarque) | Chaîne au format AAAA-MM-JJ | Date de fin de la plage pour récupérer les numéros de téléphone invalides. Ce traitement est effectué à minuit (UTC) par l’API.
| `limit` | Facultatif | Entier | Champ facultatif pour limiter le nombre de résultats renvoyés. Par défaut à 100, le maximum est 500.
| `offset` | Facultatif | Entier | Point de départ facultatif dans la liste à partir duquel récupérer. |
| `phone_numbers` | Facultatif <br>(voir remarque) | Tableau de chaînes au format e.164 | S'il est fourni, nous vous renverrons le numéro de téléphone s'il s'avère invalide. |
| `reason` | Facultatif <br>(voir remarque) | Chaîne | Les valeurs disponibles sont "provider\_error" (une erreur du fournisseur indique que le téléphone ne peut pas recevoir de SMS) ou "deactivated" (le numéro de téléphone a été désactivé). En cas d'omission, toutes les raisons sont retournées. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% alert note %}
Vous devez fournir une `start_date` et une `end_date`, OU un `phone_numbers`. Si vous fournissez les trois, une `start_date`, une `end_date`, et un `phone_numbers`, nous donnerons la priorité aux numéros de téléphone communiqués et ignorerons la plage de dates.
{% endalert %}

Si votre plage de dates dépasse le nombre `limit` de numéros de téléphone non valides, vous devrez effectuer plusieurs appels d’API, en augmentant à chaque fois le `offset` jusqu’à ce qu’un appel renvoie un résultat inférieur à `limit` ou égal à zéro.

## Exemple de demande
```
curl --location --request GET 'https://rest.iad-01.braze.com/sms/invalid_phone_numbers?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&phone_numbers[]=12345678901' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Réponse
Les entrées sont répertoriées par ordre décroissant.

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "sms": [
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
      "reason" : "provider_error"
    },
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
      "reason" : "deactivated"
    },
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
      "reason" : "provider_error"
    }
  ],
  "message": "success"
}
```
{% endapi %}
