---
nav_title: "PUT : Mise à jour des traductions d'un modèle d'e-mail"
article_title: "PUT : Mise à jour des traductions d'un modèle d'e-mail"
search_tag: Endpoint
page_order: 4

layout: api_page
page_type: reference
description: "Cet article présente les détails des traductions de mise à jour pour un endpoint de modèle d'e-mail."
---

{% api %}
# Mise à jour des traductions d'un modèle d'e-mail
{% apimethod put %}
/templates/email/translations/
{% endapimethod %}

> Utilisez cet endpoint pour mettre à jour les traductions d'un [modèle d'e-mail.]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates)

{% alert important %}
Cet endpoint est actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé.
{% endalert %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `templates.translations.update`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Paramètres de chemin

Cet endpoint n’a pas de chemin de paramètres.

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
| `template_id` | Requis | Chaîne de caractères | L'ID de votre modèle d'e-mail. |
| `locale_id` | Requis | Chaîne de caractères | L'ID de la locale. |
| `translations` | Requis | Chaîne de caractères | Le mappage des traductions pour votre modèle d'e-mail. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Notez que tous les ID de traduction sont considérés comme des identifiants uniques universels (UUID), qui peuvent être trouvés dans les paramètres de **prise en charge multilingue** ou dans la réponse à la requête GET.

## Exemple de demande

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "template_id": "e24404b3-3626-4de0-bdec-06935f3aa0ab",
    "locale_id": "h94404b3-3626-4de0-bdec-06935f3aa0ad",
    "translations": [
        {
            "translation_map": {
                "id_0": "¡Hola!",
                "id_1": "Me llamo Jacky",
                "id_2": "¿Dónde está la biblioteca?"
            }
        }
    ]
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
			"id": "1234567-abc-123-012345678",
			"message": "The provided translations yielded errors when parsing. Please contact Braze for more information."
		}
	]
}
```


## Résolution des problèmes

Le tableau suivant répertorie les erreurs renvoyées possibles et les étapes de résolution des problèmes associées.

| Message d’erreur  | Résolution des problèmes |
|----|----------|
| `The provided translations yielded errors when parsing. Please contact Braze for more information.` | Se produit lorsque le traducteur tiers fournit des traductions comportant des exceptions qui génèrent des erreurs Liquid. Contactez le service d'assistance de Braze pour obtenir de l'aide. |
| `The provided translations are missing 'id_1', 'id_2'` | Les ID de traduction ne correspondent pas ou le texte traduit dépasse les limites. Par exemple, cela peut signifier qu'il manque des champs dans l'objet de traduction de la forme de la charge utile. Chaque message (lorsqu'il est activé pour le multilinguisme) devrait avoir un nombre spécifique de "blocs de traduction" avec un ID associé. S'il manque l'un des ID dans la charge utile fournie, celle-ci sera considérée comme un objet incomplet et entraînera une erreur. |
| `The provided locale code does not exist.` | La charge utile du traducteur tiers contient un code régional qui n'existe pas dans Braze. |
| `The provided translations have exceeded the maximum of 20MB.` | La charge utile fournie dépasse la limite de taille. |
| `You have exceeded the maximum number of requests. Please try again later.` | Toutes les API de Braze intègrent une limite de débit, et cette erreur est automatiquement renvoyée lorsque le débit a dépassé le montant alloué pour ce jeton d'authentification. |
| `This message does not support multi-language.` | Cela peut se produire lorsqu'un ID de message ne prend pas encore en charge les messages multilingues. Seuls les messages des canaux suivants peuvent être traduits : push, messages in-app et e-mail. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
