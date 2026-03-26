---
nav_title: "GET : Afficher les valeurs sources par défaut pour les étiquettes de traduction canvas"
article_title: "GET : Afficher les valeurs sources par défaut pour les étiquettes de traduction canvas"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "Cet article présente en détail l'endpoint source de traduction canvas."
---

{% api %}
# Afficher les valeurs sources par défaut des tags de traduction d'un canvas
{% apimethod get %}
/canvas/traductions/source
{% endapimethod %}

> Veuillez utiliser cet endpoint pour afficher toutes les sources de traduction par défaut pour les tags de traduction d'un canvas. Ce sont les valeurs avec le {% raw %}`{% translation id %} source {% endtranslation %}`{% endraw %}. Veuillez consulter [la section Locales dans les messages]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/) pour plus d'informations sur les fonctionnalités de traduction.

{% multi_lang_include early_access_beta_alert.md feature='This endpoint' %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `canvas.translations.get`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Paramètres de recherche

| Paramètre              | Requis | Type de données | Description                        |
|------------------------|----------|-----------|------------------------------------|
| `workflow_id`          | Requis | Chaîne de caractères    | L'ID de la toile.              |
| `step_id`              | Requis | Chaîne de caractères    | L'ID de votre étape du canvas.        |
|`message_variation_id`| Requis | Chaîne de caractères | L'ID de la variation de votre message. |
| `locale_id`            | Facultatif | Chaîne de caractères    | L'ID (UUID) de la locale.              |
| `post_launch_draft_version`| Facultatif | Valeur booléenne | Lorsque`true`  renvoie la dernière version préliminaire au lieu de la dernière version publiée en ligne/en production/instantanée. Par défaut, la dernière version `false`instantanée en ligne est renvoyée.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Tous les ID de traduction sont considérés comme des identifiants uniques universels (UUID), qui peuvent être trouvés dans la réponse de l'endpoint GET.
{% endalert %}

## Exemple de demande

```
curl --location --request GET 'https://rest.iad-03.braze.com/canvas/translations/source?workflow_id={workflow_id}&step_id={step_id}&message_variation_id={message_variation_id}&locale_id={locale_uuid}&post_launch_draft_version=true' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Réponse

Quatre réponses de code de statut existent pour cet endpoint : `200`, `400`, `404` et `429`.

### Exemple de réponse réussie

Le code de statut `200` pourrait retourner l’en-tête et le corps de réponse suivant.

```json
{
   "translations": {
       "translation_map": {
           "id_0": "Here's a Million Dollars",
           "id_1": "Hello World!"
       }
   },
   "message": "success"
}
```

### Exemple de réponse échouée

Le code de statut `400` pourrait renvoyer le corps de réponse suivant. Consultez la résolution des problèmes[](#troubleshooting) pour plus d’informations concernant les erreurs que vous pourriez rencontrer.

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
