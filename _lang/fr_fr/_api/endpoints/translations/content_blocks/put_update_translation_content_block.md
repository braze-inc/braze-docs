---
nav_title: "PUT : Mettre à jour la traduction dans un bloc de contenu"
article_title: "PUT : Mettre à jour la traduction dans un bloc de contenu"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "Cet article décrit en détail la mise à jour de la traduction dans un endpoint de bloc de contenu."
---

{% api %}
# Mettre à jour la traduction dans un bloc de contenu
{% apimethod put %}
/content_blocks/translations
{% endapimethod %}

> Veuillez utiliser cet endpoint pour mettre à jour plusieurs traductions d'un [bloc de contenu]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/). Veuillez consulter [la section Locales dans les messages]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/) pour plus d'informations sur les fonctionnalités de traduction.

{% include early_access_beta_alert.md feature='This endpoint' %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `content_blocks.translations.update`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Paramètres de chemin

Cet endpoint n’a pas de chemin de paramètres.

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
| `content_block_id` | Requis | Chaîne de caractères | L'ID de votre bloc de contenu. |
| `locale_id`| Requis | Chaîne de caractères | L'ID (UUID) de la locale. |
| `translation_map` | Requis | Objet | Objet contenant les nouvelles traductions. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Tous les ID de traduction sont considérés comme des identifiants uniques universels (UUID), qui peuvent être trouvés dans la réponse de l'endpoint GET.
{% endalert %}

## Exemple de demande

```json
{
    "content_block_id": "e24404b3-3626-4de0-bdec-06935f3aa0ab",
    "locale_id": "h94404b3-3626-4de0-bdec-06935f3aa0ad",
    "translation_map": {
        "id_3": "Ein Absatz ohne Formatierung"
    }
}
```

## Réponse

Quatre réponses de code de statut existent pour cet endpoint : `200`, `400`, `404` et `429`.

### Exemple de réponse réussie

```json
{
	"message": "success"
}
```

### Exemple de réponse échouée

Le code de statut `400` pourrait renvoyer le corps de réponse suivant. Consultez la résolution des problèmes[](#troubleshooting) pour plus d’informations concernant les erreurs que vous pourriez rencontrer.

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
