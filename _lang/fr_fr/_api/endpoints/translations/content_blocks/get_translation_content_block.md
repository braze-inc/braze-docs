---
nav_title: "GET : Afficher toutes les traductions pour un bloc de contenu"
article_title: "GET : Afficher toutes les traductions pour un bloc de contenu"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Cet article fournit des informations détaillées sur l'endpoint Afficher toutes les traductions pour un bloc de contenu."
---

{% api %}
# Afficher toutes les traductions pour un bloc de contenu
{% apimethod get %}
/content_blocks/translations
{% endapimethod %}

> Veuillez utiliser cet endpoint pour afficher toutes les traductions d'un [bloc de contenu]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/). Veuillez consulter [la section Locales dans les messages]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/) pour plus d'informations sur les fonctionnalités de traduction.

{% include early_access_beta_alert.md feature='This endpoint' %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `content_blocks.translations.get`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Paramètres de recherche

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
|`content_block_id`| Requis | Chaîne de caractères | L'ID de votre bloc de contenu. |
|`locale_id`| Facultatif | Chaîne de caractères | Un UUID local pour filtrer les réponses. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Tous les ID de traduction sont considérés comme des identifiants uniques universels (UUID), qui peuvent être trouvés dans la réponse de l'endpoint GET.
{% endalert %}

## Exemple de demande

```
curl --location --request GET 'https://rest.iad-03.braze.com/content_blocks/translations?content_block_id={content_block_id}&locale_id={locale_uuid}' \
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
            "translation_map": {
                "id_0": "¡Hola!",
                "id_1": "Me llamo Jacky",
                "id_2": "¿Dónde está la biblioteca?"
            },
            "locale": {
                "uuid": "c7c12345-te35-1234-5678-abcdefa99r3f",
                "name": "es-MX",
                "country": "MX",
                "language": "es",
                "locale_key": "es-mx"
            }
        },
        {
            "translation_map": {
                "id_0": "你好",
                "id_1": "我的名字是 Jacky",
                "id_2": "圖書館在哪裡?"
            },
            "locale": {
                "uuid": "a1b12345-cd35-1234-5678-abcdefa99r3f",
                "name": "zh-HK",
                "country": "HK",
                "language": "zh",
                "locale_key": "zh-hk"
            }
        }
    ]
}
```

### Exemple de réponse échouée

Le code de statut `400` pourrait renvoyer le corps de réponse suivant.

```json
{
	"errors": [
		{
			"message": "This message does not support multi-language."
		}
	]
}
```


{% endapi %}
