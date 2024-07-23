---
nav_title: "PUT : Mettre à jour la traduction dans une campagne"
article_title: "PUT : Mettre à jour la traduction dans une campagne"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Mettre à jour la traduction dans une campagne."
---

{% api %}
# Mettre à jour la traduction dans une campagne
{% apimethod put %}
/campaigns/translations
{% endapimethod %}

> Utilise ce point de terminaison pour mettre à jour plusieurs traductions pour une campagne.

{% alert important %}
La mise à jour d'une traduction dans une campagne via l'API est actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé.
{% endalert %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `campaigns.translations.update`.

## Limite de débit

Cet endpoint a une limitation du débit de 250 000 requêtes par jour.

## Paramètres de chemin

Cet endpoint n’a pas de chemin de paramètres.

## Paramètres de demande

| Paramètre - Requis - Type de données - Description - Paramètre - Requis - Type de données - Description - Paramètre - Requis - Type de données - Description
| --------- | ---------| --------- | ----------- |
|`locale_id`| Obligatoire | Chaîne de caractères | ID du paramètre régional. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "campaign_id": "9a0ba932-11c0-4c33-b529-e79aafc12409",
    "message_variation_id": "f5896eec-847d-4c0d-a4b6-7695e67520d7",
    "locale_id": "3fa10d31-83ae-4ff4-9631-f52cea9ec8fa",
    "translation_map": {
        "id_4": "¿Dónde está la biblioteca? Me llamo T-Bone, La araña discoteca.",
        "subject_1": "¿Dónde está la biblioteca? Me llamo T-Bone, La araña discoteca.",
        "id_1": "¿Dónde está la biblioteca? Me llamo T-Bone, La araña discoteca.",
        "image": "¿Dónde está la biblioteca? Me llamo T-Bone, La araña discoteca."
    }
}
```

## Exemple de réponse réussie

```json
{
	"message": "success"
}
```

### Exemple de réponse échouée

Le code de statut `400` pourrait renvoyer le corps de réponse suivant. Consultez la `400`résolution des problèmes[](#troubleshooting) pour plus d’informations concernant les erreurs que vous pourriez rencontrer.

```json
{
	"errors": [
		{
			"message": "Something went wrong. Translation IDs are mismatched or translated text exceeds limits."
		}
	]
}
```


## Résolution des problèmes

Le tableau suivant répertorie les erreurs renvoyées possibles et les étapes de résolution des problèmes associées.

| Message d'erreur
|-----------------------------------------|------------------------------------------------------------------------------------|
| `INVALID_CAMPAIGN_ID`                   | Vérifiez que l’ID de campagne correspond à la campagne que vous traduisez.                   |
| `INVALID_LOCALE_ID` | Confirme que ton identifiant local existe dans la traduction de ton message.                         |
| `INVALID_MESSAGE_VARIATION_ID` | Confirme que l'identifiant de ton message est correct.                                                |
| `INVALID_TRANSLATION_OBJECT`            | Les ID de traduction ne correspondent pas ou le texte traduit dépasse les limites.                  |
| `MESSAGE_NOT_FOUND`                     | Vérifiez le message à traduire.                                           |
| `LOCALE_NOT_FOUND` | Confirme que le paramètre local existe dans tes paramètres multilingues.                         |
| `MISSING_TRANSLATIONS` | Les ID de traduction doivent correspondre au message.                                         |
| `MULTI_LANGUAGE_NOT_ENABLED` | Les paramètres multilingues ne sont pas activés pour ton espace de travail.                       |
| `MULTI_LANGUAGE_NOT_ENABLED_ON_MESSAGE` | Seules les campagnes d’e-mails ou les messages de canvas avec e-mails peuvent être traduits.             |
| `UNSUPPORTED_CHANNEL`                   | Seuls les messages des campagnes d’e-mails ou les messages de canvas avec e-mails peuvent être traduits. |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}