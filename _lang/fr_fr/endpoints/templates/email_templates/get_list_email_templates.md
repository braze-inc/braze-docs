---
nav_title: "GET : Répertorier les modèles d’e-mail disponibles"
article_title: "GET : Répertorier les modèles d’e-mail disponibles"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Répertorier les modèles d’e-mail disponibles."

---
{% api %}
# Répertorier les modèles d’e-mail disponibles
{% apimethod get %}
/templates/email/list
{% endapimethod %}

> Utilisez cet endpoint pour obtenir une liste des modèles d’e-mails disponibles sur votre compte Braze.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#eec24bf4-a3f4-47cb-b4d8-bb8f03964cca {% endapiref %}

## Conditions préalables
Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/api_key/) avec l’autorisation `templates.email.list`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `modified_after`  | Facultatif | Chaîne de caractères au format [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)  | Récupérer uniquement les modèles mis à jour à l’heure donnée ou après. |
| `modified_before`  |  Facultatif | Chaîne de caractères au format [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)  | Récupérer uniquement les modèles mis à jour à l’heure donnée ou avant. |
| `limit` | Facultatif | Nombre positif | Nombre maximum de modèles à récupérer. Par défaut à 100 si non renseigné, avec une valeur maximale acceptable de 1 000. |
| `offset`  |  Facultatif | Nombre positif | Nombre de modèles à ignorer avant de renvoyer le reste des modèles qui correspondent aux critères de recherche. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemple de demande
```
curl --location --request GET 'https://rest.iad-01.braze.com/templates/email/list?modified_after=2020-01-01T01:01:01.000000&modified_before=2020-02-01T01:01:01.000000&limit=1&offset=0' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Réponse 

{% alert important %}
Les modèles créés à l'aide de l'éditeur par glisser-déposer pour l'e-mail ne sont pas fournis dans cette réponse.
{% endalert %}

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "count": the number of templates returned
  "templates": [template with the following properties]:
    "email_template_id": (string) your email template's API Identifier,
    "template_name": (string) the name of your email template,
    "created_at": (string) the time the email was created at in ISO 8601,
    "updated_at": (string) the time the email was updated in ISO 8601,
    "tags": (array of strings) tags appended to the template
}
```
{% endapi %}



