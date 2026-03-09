---
nav_title: "POST : Veuillez télécharger une ressource dans la bibliothèque multimédia."
article_title: "POST : Veuillez télécharger une ressource dans la bibliothèque multimédia."
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Cet article fournit des informations détaillées sur l'endpoint `POST /media_library/create`."
---

{% api %}
# Veuillez télécharger une ressource dans la bibliothèque multimédia.
{% apimethod post %}
/media_library/create
{% endapimethod %}

> Veuillez utiliser cet endpoint pour ajouter une ressource à la [bibliothèque multimédia Braze](https://www.braze.com/docs/user_guide/engagement_tools/templates_and_media/media_library) à l'aide d'une URL hébergée en externe ou de`asset_url` données de fichier binaire envoyées dans le corps de la requête.`asset_file` Ce endpoint prend en charge les images et les fichiers ZIP contenant des images.

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `media_library.create`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corps de la demande

Lorsque vous incluez `asset_url`, l'endpoint télécharge le fichier à partir de l'URL. Lorsque vous incluez `asset_file`, l'endpoint utilise les données binaires dans le corps de la requête.

Exemple de corps de requête pour `asset_url`:

```json
{
  "asset_url": "https://cdn.example.com/assets/cat.jpg",
  "name": "Cat Graphic"
}
```

Exemple de corps de requête pour `asset_file`:

```json
{
  "asset_file": <BINARY FILE DATA>,
  "name": "Cat Graphic"
}
```

Le corps de la requête comprend les paramètres suivants :

| Paramètre | Requis | Type de données | Description |
| --------- | -------- | --------- | ----------- |
| `asset_url` | Facultatif | Chaîne de caractères | Une URL accessible au public pour la ressource à télécharger dans Braze. |
| `asset_file` | Facultatif | Binaire | Données de fichier binaire. |
| `name` | Facultatif | Chaîne de caractères | Un nom qui apparaîtra dans la bibliothèque multimédia pour cette ressource. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert important %}
`asset_url` et`asset_file`sont mutuellement exclusifs, vous devez n'inclure qu'un seul d'entre eux dans votre requête API.
{% endalert %}

### Noms des fichiers téléchargés

Cette section explique comment l'endpoint attribue des noms aux fichiers téléchargés selon que vous incluez ou non le`name`paramètre.

#### Téléchargements de fichiers individuels

| Scénario | Résultat |
| --- | --- |
| `name` fourni | La`name`valeur est utilisée comme nom de la ressource dans la bibliothèque multimédia. |
| `name` exclu | Le nom de fichier original provenant de l'URL ou du fichier téléchargé est utilisé. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" style="table-layout: fixed; width: 100%;" }

#### Téléchargements de fichiers ZIP

| Scénario | Résultat |
| --- | --- |
| `name` fourni | La`name`valeur est utilisée comme préfixe, avec un numéro incrémentiel ajouté comme suffixe (par exemple, « Mon fichier 1 », « Mon fichier 2 », « Mon fichier 3 »). |
| `name` exclu | Chaque fichier conserve son nom d'origine tel qu'il figurait dans le fichier ZIP. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" style="table-layout: fixed; width: 100%;" }

## Exemple de demande

Cette section comprend deux exemples`curl`de requêtes, l'une pour ajouter une ressource à l'aide d'une URL et l'autre à l'aide de données de fichier binaire.

Cette requête illustre un exemple d'ajout d'une ressource à la bibliothèque multimédia à l'aide d'un fichier `asset_url`.

```
curl -X POST --location 'https://rest.iad-01.braze.com/media_library/create' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--header 'Content-Type: application/json' \
--data '{"asset_url": "https://cdn.example.com/assets/cat.jpg", "name": "Cat Graphic"}'
```

Cette requête illustre un exemple d'ajout d'une ressource à la bibliothèque multimédia à l'aide d'un fichier `asset_file`.

```
curl -X POST --location 'https://rest.iad-01.braze.com/media_library/create' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--header 'Content-Type: application/json' \
--data '{"asset_file":<BINARY FILE DATA>, "name":"Cat Graphic"}'
```

### Réponses d'erreur

Cette section répertorie les erreurs potentielles ainsi que les messages et descriptions correspondants. 

#### Erreurs de validation

Les erreurs de validation renvoient une structure telle que celle-ci :

```json
{
  "message": (String) Human-readable error description
}
```

Ce tableau répertorie les erreurs de validation possibles.

| Statut HTTP | Message | Description |
| --- | --- | --- |
| 400 | Il est nécessaire de asset_filefournir l'unasset_urlou l'autre. | Aucun paramètre de ressource n'a été fourni dans la demande. |
| 400 | Il n'est pas possible de fournir à asset_filela foisasset_url  et . Veuillez n'en fournir qu'un seul. | Les deux paramètres de ressource ont été fournis ; un seul est autorisé. |
| 403 | Les API publiques de la bibliothèque multimédia ne sont pas activées pour cette entreprise. | La fonctionnalité de la bibliothèque multimédia n'est pas activée pour cet espace de travail. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Erreurs de traitement

Les erreurs de traitement renvoient une réponse différente avec des codes d'erreur :

```json
{
  "message": (String) Human-readable error description,
  "error_code": (String) error code,
  "meta": { }
}
```

Ce tableau répertorie les erreurs de traitement possibles.

| Code d'erreur | Statut HTTP | Description |
| --- | --- | --- |
| `UNSUPPORTED_FILE_TYPE` | 400 | Le type de fichier téléchargé n'est pas pris en charge. L'objet`meta` contient l'élément`file_type`qui a été rejeté. |
| `ASSET_SIZE_EXCEEDS_LIMIT` | 400 | Le fichier dépasse la taille maximale autorisée. Les images sont limitées à 5 Mo. |
| `MEDIA_LIBRARY_LIMIT_REACHED` | 400 | L'espace de travail a atteint son nombre maximal de ressources (200 par défaut pour les entreprises en période d'essai gratuit, illimité dans les autres cas). `meta`L'objet inclut le .`limit` |
| `ASSET_UPLOAD_FAILED` | 400 | Le téléchargement de la ressource a échoué en raison de problèmes de traitement. |
| `ZIP_UPLOAD_ERROR` | 400 | Le fichier ZIP est endommagé ou n'a pas pu être ouvert. L'objet`meta` contient le`original_error`message. |
| `ZIP_FILE_TOO_LARGE` | 400 | La taille totale non compressée du fichier ZIP dépasse la limite de 5 Mo. L'objet`meta` comprend le`zip_file_name`et `zip_file_size`le . |
| `ZIPPED_ENTITY_HAS_NO_NAME` | 400 | Une entrée de fichier à l'intérieur du ZIP n'a pas de nom. Veuillez vous assurer que le fichier ZIP n'est pas endommagé et attribuer un nom à tout fichier sans nom. |
| `ZIPPED_ENTITY_CANNOT_HAVE_NESTED_DIRECTORY` | 400 | Le fichier ZIP contient des répertoires imbriqués, qui ne sont pas pris en charge. Tous les fichiers doivent se trouver à la racine du fichier ZIP. |
| `GENERIC_ERROR` | 500 | Une erreur imprévue s'est produite lors du téléchargement. L'objet`meta` contient le`original_error`message pour le débogage. Veuillez réessayer ou contacter [le service d'assistance]({{site.baseurl}}/support_contact/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


## Réponse

Il existe cinq réponses de code d'état pour cet endpoint : `200`, `400`,`403` `429`, et `500`.

Le JSON suivant présente la forme attendue de la réponse.

```json
{ 
    "new_assets": [
        {
            "name": (String) the name of the asset,
            "size": (Integer) the byte size of the asset,
            "url": (String) the URL to access the asset,
            "ext": (String) the file extension (e.g., "png", "jpg", "gif")
        }
    ],
    "errors": [
        {
            "name": (String) the name of the asset,
            "size": (Integer) the byte size of the asset,
            "ext": (String) the file extension (e.g., "png", "jpg", "gif"),
            "error": (String) the error that occurred
        }
    ],
    "dashboard_url": (String) the URL to view this asset in the Braze dashboard
}
```

{% endapi %}
