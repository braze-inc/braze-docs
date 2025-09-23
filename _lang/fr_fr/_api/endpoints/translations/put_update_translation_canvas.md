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

> Utilisez cet endpoint pour mettre à jour plusieurs traductions pour un Canvas.

{% alert important %}
La mise à jour d’une traduction pour les messages de canvas via l’API est actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé.
{% endalert %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `canvas.translations.update`.

## Limite de débit

Cet endpoint a une limitation du débit de 250 000 requêtes par jour.

## Paramètres de chemin

Cet endpoint n’a pas de chemin de paramètres.

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
|`step_id`| Requis | Chaîne de caractères | L'ID de votre étape du canvas. |
|`message_variation_id`| Requis | Chaîne de caractères | L'ID de votre message. |
|`locale_id`| Requis | Chaîne de caractères | L'ID de la locale. |
|`workflow_id` | Requis | Chaîne de caractères | L'ID de la toile. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Notez que tous les ID de traduction sont considérés comme des identifiants uniques universels (UUID), qui peuvent être trouvés dans les paramètres de **prise en charge multilingue** ou dans la réponse à la requête GET.

## Exemple de demande

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "canvas_id": "9a0ba932-11c0-4c33-b529-e79aafc12409",
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

Le code de statut `400` pourrait renvoyer le corps de réponse suivant. Consultez la résolution des problèmes[](#troubleshooting) pour plus d’informations concernant les erreurs que vous pourriez rencontrer.

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

| Message d’erreur | Résolution des problèmes |
| --- | --- |
|`INVALID_CAMPAIGN_ID`|Confirmez que l'ID de la campagne correspond à la campagne que vous traduisez.|
|`INVALID_LOCALE_ID`|Confirmez que votre ID local existe dans la traduction de votre message.|
|`INVALID_MESSAGE_VARIATION_ID`|Confirmez que l'ID de votre message est correct.|
|`INVALID_TRANSLATION_OBJECT`|Les ID de traduction ne correspondent pas ou le texte traduit dépasse les limites.|
|`MESSAGE_NOT_FOUND`|Vérifiez que le message à traduire.|
|`LOCALE_NOT_FOUND`| Confirmez que le paramètre local existe dans vos paramètres multilingues. |
|`MISSING_TRANSLATIONS`|Les ID de traduction doivent correspondre au message.|
|`MULTI_LANGUAGE_NOT_ENABLED`|Les paramètres multilingues ne sont pas activés pour votre espace de travail.|
|`MULTI_LANGUAGE_NOT_ENABLED_ON_MESSAGE`|Seules les campagnes de communication par e-mail ou les messages canvas contenant des e-mails peuvent être traduits.|
|`UNSUPPORTED_CHANNEL`| Seuls les messages des campagnes de communication par e-mail ou les envois de canvas par e-mail peuvent être traduits.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


          INVALID_CAMPAIGN_ID = "Invalid campaign or step ID"
          INVALID_LOCALE_ID = "Invalid locale ID"
          INVALID_MESSAGE_VARIATION_ID = "Invalid message ID"
          INVALID_TRANSLATION_OBJECT = "Invalid translation object"
          MESSAGE_NOT_FOUND = "Message not found"
          LOCALE_NOT_FOUND = "Locale not found"
          MISSING_TRANSLATIONS = "Missing translations from the request body"
          MULTI_LANGUAGE_NOT_ENABLED = "Multi-language feature is not enabled on this company"
          MULTI_LANGUAGE_NOT_ENABLED_ON_MESSAGE = "This message does not have multi-language setup"
          UNSUPPORTED_CHANNEL = "This message type does not support multi-language"

{% endapi %}
