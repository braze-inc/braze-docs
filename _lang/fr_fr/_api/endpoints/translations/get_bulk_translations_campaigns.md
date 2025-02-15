---
nav_title: "GET : Voir les traductions pour une campagne"
article_title: "GET : Voir les traductions pour une campagne"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Cet article décrit en détail l’endpoint Afficher les traductions pour une campagne."
---

{% api %}
# Voir les traductions pour une campagne
{% apimethod get %}
/campagnes/traductions
{% endapimethod %}

> Utilisez ce point de terminaison pour voir toutes les traductions de chaque variante de message dans une campagne.

{% alert important %}
La visualisation des traductions des messages de campagne via l'API est actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé.
{% endalert %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `campaigns.translations.get`.

## Limite de débit

Cet endpoint a une limitation du débit de 250 000 requêtes par jour.

## Paramètres de chemin

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
|`campaign_id`| Requis pour traduire une campagne | Chaîne de caractères | L'ID de votre campagne. |
| `message_variation_id` | Requis | Chaîne de caractères | L'ID de votre message. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Notez que tous les ID de traduction sont considérés comme des identifiants uniques universels (UUID), qui peuvent être trouvés dans les paramètres de **prise en charge multilingue** ou dans la réponse à la demande.

## Exemple de demande

```
curl --location --request GET 'https://rest.iad-03.braze.com/campaign/translations' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Réponse

Quatre réponses de code de statut existent pour cet endpoint : `200`, `400`, `404` et `429`.

## Exemple de réponse réussie

Le code de statut `200` pourrait retourner l’en-tête et le corps de réponse suivant.

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
	"translations": [
		{
			"locale": {
 				"name": "zh-HK",
 				"country": "Hong Kong",
 				"language": "Chinese (Traditional)",
			},
			"translation_map": {
				"id_0": "Hello",
				"id_1": "My name is Jacky",
				"id_2": "Where is the library?"
			}
		}
	]
}
```

## Exemple de réponse échouée

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

## Résolution des problèmes

Le tableau suivant répertorie les erreurs renvoyées possibles et les étapes de résolution des problèmes associées.

| Message d’erreur                           | Résolution des problèmes                                                                    |
|-----------------------------------------|------------------------------------------------------------------------------------|
| `INVALID_CAMPAIGN_ID`                   | Confirmez que l'ID de la campagne correspond à la campagne que vous traduisez.                   |
| `INVALID_MESSAGE_VARIATION_ID`          | Confirmez que l'ID de votre message est correct.                                                |
| `MESSAGE_NOT_FOUND`                     | Vérifiez que le message à traduire.                                           |
| `MULTI_LANGUAGE_NOT_ENABLED`            | Les paramètres multilingues ne sont pas activés pour votre espace de travail.                       |
| `MULTI_LANGUAGE_NOT_ENABLED_ON_MESSAGE` | Seules les campagnes de communication par e-mail ou les messages canvas contenant des e-mails peuvent être traduits.             |
| `UNSUPPORTED_CHANNEL`                   | Seuls les messages des campagnes de communication par e-mail ou les envois de canvas par e-mail peuvent être traduits. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
