---
nav_title: "GET : Afficher la traduction d’un canvas"
article_title: "GET : Afficher la traduction d’un canvas"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Afficher la traduction d’un canvas."
---

{% api %}
# Afficher la traduction d’un canvas
{% apimethod get %}
/canvas/translations/?locale_id={locale_id}
{% endapimethod %}

> Utilisez cet endpoint pour afficher un message traduit afin de voir à quoi ressemble ce message pour un utilisateur.

{% alert important %}
L’affichage d’un message traduit pour un canvas via l’API est actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé.
{% endalert %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `canvas.translations.get`.

## Limite de débit

Cet endpoint a une limitation du débit de 250 000 requêtes par jour.

## Paramètres de chemin

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
|`step_id`| Requis | Chaîne de caractères | L'ID de votre étape du canvas. |
|`message_variation_id`| Requis | Chaîne de caractères | L'ID de la variation de votre message. |
|`locale_id`| Requis | Chaîne de caractères | L'ID de la locale. |
|`workflow_id` | Requis | Chaîne de caractères | L'ID de la toile. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Notez que tous les ID de traduction sont considérés comme des identifiants uniques universels (UUID), qui peuvent être trouvés dans les paramètres de **prise en charge multilingue** ou dans la réponse à la demande.

## Exemple de demande

```
curl --location --request GET 'https://rest.iad-03.braze.com/canvas/translations/?locale_id={locale_id}' \
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
 				"name": "es-MX",
 				"country": "Mexico",
 				"language": "Spanish",
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

### Exemple de réponse échouée

Le code de statut `400` pourrait renvoyer le corps de réponse suivant. Consultez la résolution des problèmes[](#troubleshooting) pour plus d’informations concernant les erreurs que vous pourriez rencontrer.

```json
{
	"errors": [
		{
			"message": "Invalid locale ID"
		}
	]
}
```

## Résolution des problèmes

Le tableau suivant répertorie les erreurs renvoyées possibles et les étapes de résolution des problèmes associées.

| Message d’erreur                           | Résolution des problèmes                                                                    |
|-----------------------------------------|------------------------------------------------------------------------------------|
| `INVALID_CAMPAIGN_ID`                   | Confirmez que l'ID de la campagne correspond à la campagne que vous traduisez.                   |
| `INVALID_LOCALE_ID`                     | Confirmez que votre ID local existe dans la traduction de votre message.                         |
| `INVALID_MESSAGE_VARIATION_ID`          | Confirmez que l'ID de votre message est correct.                                                |
| `MESSAGE_NOT_FOUND`                     | Vérifiez que le message à traduire.                                           |
| `LOCALE_NOT_FOUND`                      | Confirmez que le paramètre local existe dans vos paramètres multilingues.                         |
| `MULTI_LANGUAGE_NOT_ENABLED`            | Les paramètres multilingues ne sont pas activés pour votre espace de travail.                       |
| `MULTI_LANGUAGE_NOT_ENABLED_ON_MESSAGE` | Seules les campagnes de communication par e-mail ou les messages canvas contenant des e-mails peuvent être traduits.             |
| `UNSUPPORTED_CHANNEL`                   | Seuls les messages des campagnes de communication par e-mail ou les envois de canvas par e-mail peuvent être traduits. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
