---
nav_title: "PUT : Mise à jour de la traduction dans un canvas"
article_title: "PUT : Mise à jour de la traduction dans un canvas"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Mettre à jour la traduction dans un canvas."
---

{% api %}
# Mise à jour de la traduction dans un canvas
{% apimethod put %}
/canvas/translations
{% endapimethod %}

> Utilisez cet endpoint pour mettre à jour plusieurs traductions pour un Canvas. Pour plus d'informations sur les fonctionnalités de traduction, reportez-vous à la section [Locales dans les messages]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/).

Si vous souhaitez mettre à jour les traductions après le lancement d'un canvas, vous devrez d'abord [enregistrer votre message en tant que brouillon]({{site.baseurl}}/post-launch_edits/).

{% alert important %}
Cet endpoint est actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé.
{% endalert %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `canvas.translations.update`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Paramètres de chemin

Cet endpoint n’a pas de chemin de paramètres.

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
|`workflow_id` | Requis | Chaîne de caractères | L'ID de la toile. |
|`step_id`| Requis | Chaîne de caractères | L'ID de votre étape du canvas. |
|`message_variation_id`| Requis | Chaîne de caractères | L'ID de la variation de votre message. |
|`locale_id`| Requis | Chaîne de caractères | L'ID (UUID) de la locale. |
|`translation_map` | Requis | Objet | Objet contenant les nouvelles traductions. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Tous les ID de traduction sont considérés comme des identifiants uniques universels (UUID), qui peuvent être trouvés dans la réponse de l'endpoint GET.
{% endalert %}

## Exemple de demande

```json
{
    "workflow_id": "a74404b3-3626-4de0-bdec-06935f3aa0ad",
    "step_id": "a74404b3-3626-4de0-bdec-06935f3aa0ac",
    "message_variation_id": "a74404b3-3626-4de0-bdec-06935f3aa0ac",
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
