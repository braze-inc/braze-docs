---
nav_title: "GET : Afficher la traduction et les paramètres locaux spécifiques pour le modèle d'e-mail"
article_title: "GET : Afficher la traduction et la langue spécifiques pour le modèle d'e-mail"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "Cet article décrit les détails de la traduction et de la locale spécifiques à l'affichage pour l'endpoint des modèles d'e-mail."
---

{% api %}
# Afficher une traduction et une locale spécifiques pour l'endpoint du modèle d'e-mail
{% apimethod get %}
/templates/translations/email
{% endapimethod %}

> Utilisez cet endpoint pour afficher une traduction et une région spécifiques pour un [modèle d'e-mail.]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates) Pour plus d'informations sur les fonctionnalités de traduction, reportez-vous à la section [Locales dans les messages]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/).

{% alert important %}
Cet endpoint est actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé.
{% endalert %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `templates.translations.get`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Paramètres de recherche

| Paramètre     | Requis | Type de données | Description                     |
|---------------|----------|-----------|---------------------------------|
| `template_id` | Requis | Chaîne de caractères    | L'ID de votre modèle d'e-mail. |
| `locale_id`   | Facultatif | Chaîne de caractères    | L'ID (UUID) de la locale.           |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Tous les ID de traduction sont considérés comme des identifiants uniques universels (UUID), qui peuvent être trouvés dans la réponse de l'endpoint GET.
{% endalert %}

## Exemple de demande

```
curl --location --request GET 'https://rest.iad-03.braze.com/templates/translations/email?locale_id={locale_uuid}&template_id={template_id}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Réponse

Quatre réponses de code de statut existent pour cet endpoint : `200`, `400`, `404` et `429`.

### Exemple de réponse réussie

Le code de statut `200` pourrait retourner l’en-tête et le corps de réponse suivant.

```json
{
    "translations": [
        {
            "locale": {
                "uuid": "c7c12345-te35-1234-5678-abcdefa99r3f",
                "name": "es-MX",
                "country": "MX",
                "language": "es",
                "locale_key": "es-mx"
            },
            "translation_map": {
                "id_0": "¡Hola!",
                "id_1": "Me llamo Jacky",
                "id_2": "¿Dónde está la biblioteca?"
            }
        }
    ]
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

{% endapi %}
