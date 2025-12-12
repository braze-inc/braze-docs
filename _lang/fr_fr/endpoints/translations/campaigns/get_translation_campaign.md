---
nav_title: "GET : Voir la traduction d'une campagne"
article_title: "GET : Voir la traduction pour une campagne"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Cet article décrit en détail l’endpoint Afficher les traductions pour une campagne."
---

{% api %}
# Voir la traduction d'une campagne
{% apimethod get %}
/campaigns/translations/?locale_id={locale_id}
{% endapimethod %}

> Utilisez cet endpoint pour prévisualiser un message traduit pour une campagne.

{% alert important %}
Cet endpoint est actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé.
{% endalert %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `campaigns.translations.get`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Paramètres de recherche

| Paramètre              | Requis | Type de données | Description                        |
|------------------------|----------|-----------|------------------------------------|
| `campaign_id`          | Requis | Chaîne de caractères    | L'ID de votre campagne.           |
| `message_variation_id` | Requis | Chaîne de caractères    | L'ID de la variation de votre message. |
| `locale_id`            | Requis | Chaîne de caractères    | L'ID de la locale.              |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Notez que tous les ID de traduction sont considérés comme des identifiants uniques universels (UUID), qui peuvent être trouvés dans les paramètres de **prise en charge multilingue** ou dans la réponse à la demande.

## Exemple de demande

```
curl --location --request GET 'https://rest.iad-03.braze.com/campaigns/translations/?locale_id={locale_uuid}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Réponse

Quatre réponses de code de statut existent pour cet endpoint : `200`, `400`, `404` et `429`.

### Exemple de réponse réussie

Le code de statut `200` pourrait retourner l’en-tête et le corps de réponse suivant.

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
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
| `MULTI_LANGUAGE_NOT_ENABLED_ON_MESSAGE` | Seules les campagnes d'e-mails, de push et de messages in-app ou les messages Canvas avec des e-mails peuvent être traduits.             |
| `UNSUPPORTED_CHANNEL`                   | Seules les campagnes par e-mail, push ou messages in-app ou les messages Canvas peuvent être traduits. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
