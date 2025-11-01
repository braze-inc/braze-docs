---
nav_title: "POST : Supprimer des ID externes"
article_title: "POST : Supprimer l'ID externe"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Supprimer des ID externes."

---
{% api %}
# Supprimer des ID externes
{% apimethod post %}
/users/external_ids/remove
{% endapimethod %}

> Utilisez cet endpoint pour supprimer les anciens ID externes obsolètes de vos utilisateurs. 

Vous pouvez envoyer jusqu’à 50 ID externes par demande. 

{% alert warning %}
Cet endpoint supprime complètement l’ID obsolète et ne peut pas être annulé. Utilisez cet endpoint pour enlever des `external_ids` obsolètes qui sont toujours associés à des utilisateurs dans votre système peut vous empêcher définitivement de trouver les données de ces utilisateurs.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e16b5340-5f44-42b6-9033-2398faf8908e {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/api_key/) avec l’autorisation `users.external_ids.remove`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='external id migration' %}

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_ids" : (required, array of external identifiers to remove)
}
```

### Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
| `external_ids` | Requis | Tableau de chaînes de caractères | Identifiants externes pour les utilisateurs à supprimer. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemple de demande

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/external_ids/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "external_ids" :[
    "existing_deprecated_external_id_string",
    ...
  ]
}'
```

{% alert important %}
Seuls les ID obsolètes peuvent être supprimés ; la tentative de suppression d’un ID externe principal entraînera une erreur.
{% endalert %}

## Réponse

La réponse confirmera toutes les suppressions réussies et les suppressions infructueuses avec les erreurs associées. Les messages d’erreur dans le champ `removal_errors` référenceront l’index dans le tableau de la demande d’origine.

```
{
  "message" : (string) status message,
  "removed_ids" : (array of strings) successful remove operations,
  "removal_errors": (array of arrays) <minor error message>
}
```

Le champ `message` renverra `success` pour toutes les demandes valides. Des erreurs plus spécifiques sont saisies dans le tableau `removal_errors`. Le champ `message` renvoie une erreur dans les cas suivants :
- Clé API non valide
- Tableau `external_ids` vide
- Tableau `external_ids` avec plus de 50 éléments
- Atteinte de la limite de débit (plus de 1 000 requêtes/minute)

{% endapi %}
