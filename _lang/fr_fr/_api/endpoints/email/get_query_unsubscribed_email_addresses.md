---
nav_title: "GET : Requête de la liste des adresses e-mail désinscrites"
article_title: "GET : Requête de la liste des adresses e-mail désinscrites"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Récupérer la liste ou Interroger les désabonnements par e-mail."

---
{% api %}
# Extraire la liste des adresses e-mail désinscrites
{% apimethod get %}
/email/unsubscribes
{% endapimethod %}

> Utilisez cet endpoint pour renvoyer les e-mails qui ont été désinscrits entre le `start_date` et le `end_date`. Pour un historique complet de l'état de l'abonnement, utilise [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents) pour suivre ces données.

Vous pouvez utiliser cet endpoint pour configurer une synchronisation bidirectionnelle entre Braze et d’autres systèmes de messagerie ou votre propre base de données.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d2966b81-188a-407b-ba7e-e6c252c44b4a {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `email.unsubscribe`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de demande

| Paramètre - Requis - Type de données - Description - Paramètre - Requis - Type de données - Description - Paramètre - Requis - Type de données - Description
| ----------|-----------| ---------|------ |
| `start_date` | Facultatif <br>(voir note) | Chaîne au format AAAA-MM-JJ| Date de début de l'intervalle pour récupérer les désabonnements, doit être antérieure à la date de fin. Ce traitement est effectué à minuit (UTC) par l’API.
| `end_date` | Facultatif <br>(voir note) | Chaîne au format AAAA-MM-JJ | Date de fin de l'intervalle pour récupérer les désabonnements. Ce traitement est effectué à minuit (UTC) par l’API.
| `limit` | Facultatif | Entier | Champ facultatif pour limiter le nombre de résultats renvoyés. Par défaut à 100, le maximum est 500.
| `offset` | Facultatif | Entier | Facultatif point de départ de la liste à partir duquel la recherche doit s'effectuer. |
| `sort_direction` | Facultatif | Chaîne | Passe la valeur `asc` pour trier les désabonnements du plus ancien au plus récent. Indiquez la valeur `desc` pour trier de la plus récente à la plus ancienne. Si `sort_direction` n'est pas inclus, l'ordre par défaut est du plus récent au plus ancien. |
| `email` | Facultatif <br>(voir note) | Chaîne | Si elle est fournie, nous indiquerons si l'utilisateur s'est désabonné ou non. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% alert note %}
Vous devez fournir une `end_date`, ainsi qu’un `email` ou une `start_date`.
{% endalert %}

Si votre plage de dates dépasse le nombre `limit` de désinscriptions, vous devrez effectuer plusieurs appels d’API, en augmentant à chaque fois le `offset` jusqu’à ce qu’un appel renvoie un résultat inférieur à `limit` ou égal à zéro.

## Exemple de demande 
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/unsubscribes?start_date=2020-01-01&end_date=2020-02-01&limit=1&offset=1&sort_direction=desc&email=example@braze.com' \
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
      "email": (string) an email that has been unsubscribed,
      "unsubscribed_at": (string) the time the email was unsubscribed in ISO 8601
    },
    {
      "email": (string) an email that has been unsubscribed,
      "unsubscribed_at": (string) the time the email was unsubscribed in ISO 8601
    },
    {
      "email": (string) an email that has been unsubscribed,
      "unsubscribed_at": (string) the time the email was unsubscribed in ISO 8601
    }
  ],
  "message": "success"
}
```
{% endapi %}
