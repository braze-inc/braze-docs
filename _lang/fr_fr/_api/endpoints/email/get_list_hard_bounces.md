---
nav_title: "GET : Extraire les e-mails ayant reçu un échec d'envoi définitif"
article_title: "GET : Extraire les e-mails ayant reçu un échec d'envoi définitif"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Interroger ou lister les adresses e-mail ayant reçu un échec d'envoi définitif."

---
{% api %}
# Extraire les e-mails ayant reçu un échec d'envoi définitif
{% apimethod get %}
/email/hard_bounces
{% endapimethod %}

> Utilisez cet endpoint pour extraire une liste d’adresses e-mail ayant rejeté définitivement vos e-mails au cours d'une certaine période.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7c2ef84f-ddf5-451a-a72c-beeabc06ad9d {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `email.hard_bounces`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| ----------|-----------| ----------|----- |
| `start_date` | En option* | Chaîne de caractères au format YYYY-MM-DD| \*L'un des sites `start_date` ou `email` est requis. Il s'agit de la date de début de la plage de récupération des échecs d'envoi définitifs, qui doit être antérieure à `end_date`. Ce traitement est effectué à minuit (UTC) par l’API. |
| `end_date` | Requis | Chaîne de caractères au format YYYY-MM-DD | Date de fin de la période d'extraction des échecs d'envoi définitifs. Ce traitement est effectué à minuit (UTC) par l’API. |
| `limit` | Facultatif | Entier | Champ facultatif pour limiter le nombre de résultats renvoyés. Par défaut à 100, le maximum est 500. |
| `offset` | Facultatif | Entier | Point de départ facultatif dans la liste où récupérer les informations. |
| `email` | En option* | Chaîne de caractères | \*L'un des sites `start_date` ou `email` est requis. Si cette information est fournie, nous indiquerons si l'utilisateur a fait l'objet d'un échec d'envoi définitif. Vérifiez que les chaînes d'e-mails sont correctement formatées. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert important %}
Vous devez fournir un `end_date` et un `email` ou un `start_date`. Si vous fournissez les trois, une `start_date`, une `end_date`, et un `email`, nous donnerons la priorité aux e-mails communiqués et ignorerons la plage de dates.
{% endalert %}

Si votre plage de dates dépasse le nombre `limit` d'échecs d'envoi définitifs, vous devrez effectuer plusieurs appels d’API, en augmentant à chaque fois le `offset` jusqu’à ce qu’un appel renvoie un résultat inférieur à `limit` ou égal à zéro. L'inclusion des paramètres `offset` et `limit` avec `email` peut renvoyer une réponse vide.

## Exemple de demande
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/hard_bounces?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Réponse
Les entrées sont répertoriées par ordre décroissant.

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "emails": [
    {
      "email": (string) an email that has hard bounced,
      "hard_bounced_at": (string) the time the email hard bounced in ISO 8601
    },
    {
      "email": (string) an email that has hard bounced,
      "hard_bounced_at": (string) the time the email hard bounced in ISO 8601
    },
    {
      "email": (string) an email that has hard bounced,
      "hard_bounced_at": (string) the time the email hard bounced in ISO 8601
    }
  ],
  "message": "success"
}
```
{% endapi %}
