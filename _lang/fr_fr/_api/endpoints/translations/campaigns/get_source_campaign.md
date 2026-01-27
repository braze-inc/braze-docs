---
nav_title: "GET : Afficher les valeurs source par défaut pour les tags de traduction de la campagne"
article_title: "GET : Afficher les valeurs source par défaut pour les tags de traduction de la campagne"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "Cet article présente les détails de l'endpoint source de traduction de la campagne."
---

{% api %}
# Affichez les valeurs source par défaut pour les tags de traduction d'une campagne.
{% apimethod get %}
/campagnes/traductions/source
{% endapimethod %}

> Utilisez cet endpoint pour afficher toutes les sources de traduction par défaut pour les étiquettes de traduction d'une campagne. Il s'agit des valeurs contenues dans le site {% raw %}`{% translation id %} source {% endtranslation %}`{% endraw %}. Pour plus d'informations sur les fonctionnalités de traduction, reportez-vous à la section [Locales dans les messages]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/).

{% alert important %}
Cet endpoint est actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé.
{% endalert %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `campaigns.translations.get`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Paramètres de recherche

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
|`campaign_id`| Requis | Chaîne de caractères | L'ID de votre campagne. |
|`message_variation_id`| Requis | Chaîne de caractères | L'ID de la variation de votre message. |
|`locale_id`| Facultatif | Chaîne de caractères | Un UUID local pour filtrer les réponses. |
|`post_launch_draft_version`| Facultatif | Valeur booléenne | Lorsque `true` renvoie la dernière version provisoire au lieu de la dernière version publiée en ligne/instantanée. La valeur par défaut est `false`, qui renvoie la dernière version en ligne/en production/instantanée.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Tous les ID de traduction sont considérés comme des identifiants uniques universels (UUID), qui peuvent être trouvés dans la réponse de l'endpoint GET.
{% endalert %}

## Exemple de demande

```
curl --location --request GET 'https://rest.iad-03.braze.com/campaigns/translations/source?campaign_id={campaign_id}&message_variation_id={message_variation_id}&locale_id={locale_uuid}&post_launch_draft_version=true' \
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

Le code de statut `400` pourrait renvoyer le corps de réponse suivant. Consultez la [résolution des problèmes](#troubleshooting) pour plus d’informations concernant les erreurs que vous pourriez rencontrer.

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
