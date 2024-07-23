---
nav_title: "GET : Afficher la traduction d'une campagne"
article_title: "GET : Afficher la traduction d'une campagne"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Cet article décrit en détail l’endpoint Afficher les traductions pour une campagne."
---

{% api %}
# Afficher la traduction d'une campagne
{% apimethod get %}
/campaign/translations/?locale_id={locale_id}
{% endapimethod %}

> Utilisez ce point de terminaison pour afficher un message de campagne traduit afin de voir à quoi ressemble ce message pour un utilisateur.

{% alert important %}
L'affichage d'un message de campagne traduit via l'API est actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé.
{% endalert %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `campaigns.translations.get`.

## Limite de débit

Cet endpoint a une limitation du débit de 250 000 requêtes par jour.

## Paramètres de chemin

| Paramètre | Obligatoire | Type de données | Descriptif |
| --------- | ---------| --------- | ----------- |
|`campaign_id`| Obligatoire | Chaîne de caractères | L'identifiant de votre campagne. |
|`message_variation_id`| Obligatoire | Chaîne | L’ID de votre variante de message. |
|`locale_id`| Obligatoire | Chaîne | L’ID des paramètres régionaux. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}


## Exemple de demande

```
curl --location --request GET 'https://rest.iad-03.braze.com/campaign/translations/?locale_id={locale_id}' \
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

Le code de statut `400` pourrait renvoyer le corps de réponse suivant. Consultez la `400`résolution des problèmes[](#troubleshooting) pour plus d’informations concernant les erreurs que vous pourriez rencontrer.

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

| Message d'erreur | Dépannage |
|-----------------------------------------|------------------------------------------------------------------------------------|
| `INVALID_CAMPAIGN_ID`                   | Vérifiez que l’ID de campagne correspond à la campagne que vous traduisez.                   |
| `INVALID_LOCALE_ID` | Confirmez que votre identifiant de paramètres régionaux existe dans la traduction de votre message. |
| `INVALID_MESSAGE_VARIATION_ID` | Confirmez que votre identifiant de message est correct. |
| `MESSAGE_NOT_FOUND`                     | Vérifiez le message à traduire.                                           |
| `LOCALE_NOT_FOUND`                      | Vérifiez que le paramètre régional existe dans vos paramètres multilingues.                         |
| `MULTI_LANGUAGE_NOT_ENABLED` | Les paramètres multilingues ne sont pas activés pour votre espace de travail. |
| `MULTI_LANGUAGE_NOT_ENABLED_ON_MESSAGE` | Seules les campagnes d’e-mails ou les messages de canvas avec e-mails peuvent être traduits.             |
| `UNSUPPORTED_CHANNEL`                   | Seuls les messages des campagnes d’e-mails ou les messages de canvas avec e-mails peuvent être traduits. |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}