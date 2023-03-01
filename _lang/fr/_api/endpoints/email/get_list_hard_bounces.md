---
nav_title: "GET : Requête des e-mails avec rebond élevé"
article_title: "GET : Requête des e-mails avec rebond élevé"
search_tag: Endpoint
page_order: 0
layout: api_page
page_type: reference
description: "Cet article décrit l’utilisation et les paramètres pour se servir de l’endpoint Braze Récupérer une liste d’adresses e-mail avec rebond élevé."

---
{% api %}
# Requête ou liste des e-mails avec rebond élevé.
{% apimethod get %}
/email/hard_bounces
{% endapimethod %}

Utilisez cet endpoint pour extraire une liste d’adresses e-mail qui ont rejeté définitivement vos e-mails dans un certain délai.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7c2ef84f-ddf5-451a-a72c-beeabc06ad9d {% endapiref %}

## Limites de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| ----------|-----------| ----------|----- |
| `start_date` | Facultatif<br>(voir la note) | Chaîne de caractères au format AAAA-MM-JJ| Date de début de la plage pour récupérer les rebonds élevés. Doit être antérieure à `end_date`. Ce traitement est effectué à minuit (UTC) par l’API. |
| `end_date` | Facultatif<br>(voir la note) | Chaîne de caractères au format AAAA-MM-JJ | Date de fin de la plage pour récupérer les rebonds élevés. Ce traitement est effectué à minuit (UTC) par l’API. |
| `limit` | Facultatif | Entier | Champ facultatif pour limiter le nombre de résultats renvoyés. Par défaut à 100, le maximum est 500. |
| `offset` | Facultatif | Entier | Point de départ facultatif dans la liste où récupérer les informations. |
| `email` | Facultatif<br>(voir la note) | Chaîne de caractères | S’il est fourni, nous renverrons si l’utilisateur a un rebond élevé ou pas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% alert note %}
Vous devez fournir une `start_date` et une `end_date`, OU un `email`. Si vous fournissez les trois, une `start_date`, une `end_date`, et un `email`, nous donnerons la priorité aux e-mails communiqués et ignorerons la plage de dates.
{% endalert %}

Si votre plage de dates dépasse le nombre `limit` de rebonds élevés, vous devrez effectuer plusieurs appels d’API, en augmentant à chaque fois le `offset` jusqu’à ce qu’un appel renvoie un résultat inférieur à `limit` ou égal à zéro.

## Exemple de demande
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/hard_bounces?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&email=example@braze.com' \
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
      "unsubscribed_at": (string) the time the email hard bounced in ISO 8601
    },
    {
      "email": (string) an email that has hard bounced,
      "unsubscribed_at": (string) the time the email hard bounced in ISO 8601
    },
    {
      "email": (string) an email that has hard bounced,
      "unsubscribed_at": (string) the time the email hard bounced in ISO 8601
    }
  ],
  "message": "success"
}
```
{% endapi %}
