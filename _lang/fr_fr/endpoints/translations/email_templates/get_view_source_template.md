---
nav_title: "GET : Voir les traductions de la source pour e-mail template"
article_title: "GET : Voir les traductions de Source pour Email Template"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Cet article présente les détails de l'affichage des traductions de la source pour un endpoint de modèle d'e-mail."
---

{% api %}
# Afficher les traductions sources d'un modèle d'e-mail
{% apimethod get %}
/templates/email/translations/source
{% endapimethod %}

> Utilisez cet endpoint pour afficher les traductions sources d'un [modèle d'e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates).

{% alert important %}
Cet endpoint est actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé.
{% endalert %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `templates.email.info`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Paramètres de recherche

| Paramètre     | Requis | Type de données | Description                     |
|---------------|----------|-----------|---------------------------------|
| `template_id` | Requis | Chaîne de caractères    | L'ID de votre modèle d'e-mail. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemple de demande

```
curl --location --request GET 'https://rest.iad-03.braze.com/templates/email/translations/source' 
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
--Request Body
---template_id: "6ad1507f-ca10-44c4-95bf-aj39fm10fm1ps"
```

## Réponse

Quatre réponses de code de statut existent pour cet endpoint : `200`, `400`, `404` et `429`.

### Exemple de réponse réussie

Le code de statut `200` pourrait retourner l’en-tête et le corps de réponse suivant.

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "translations": {
        "translation_map": {
            "id_0": "Here's a limited time offer for your membership tier!",
            "id_1": "Welcome to a new fashion-forward season!"
        }
    },
    "message": "success"
}
```

### Exemple de réponse échouée

Le code de statut `400` pourrait renvoyer le corps de réponse suivant. Consultez la [résolution des problèmes](#troubleshooting) pour plus d’informations concernant les erreurs que vous pourriez rencontrer.

```json
{
    "errors": [
        {
            "message": "The provided locale code does not exist."
        }
    ]
}
```

## Résolution des problèmes

Le tableau suivant répertorie les erreurs renvoyées possibles et les étapes de résolution des problèmes associées.

| Message d’erreur                           | Résolution des problèmes                                                                    |
|-----------------------------------------|------------------------------------------------------------------------------------|
| `MULTI_LANGUAGE_NOT_ENABLED`            | Les paramètres multilingues ne sont pas activés pour votre espace de travail.                       |
| `MULTI_LANGUAGE_NOT_ENABLED_ON_MESSAGE` | Seuls les modèles d'e-mails et les campagnes d'e-mails, de push et de messages in-app ou les messages Canvas avec les e-mails peuvent être traduits.             |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
