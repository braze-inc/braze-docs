---
nav_title: "POST : Mise à jour du bloc de contenu"
article_title: "POST : Mettre à jour le bloc de contenu"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Mettre à jour des blocs de contenu."

---
{% api %}
# Mettre à jour le bloc de contenu
{% apimethod post %}
/content_blocks/update
{% endapimethod %}

> Utilisez cet endpoint pour mettre à jour un [bloc de contenu]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4782239a-cb60-4217-9de0-51411434d57d {% endapiref %}

## Conditions préalables
Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/api_key/) avec l’autorisation `content_blocks.update`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "content_block_id" : (required, string) Content Block's API identifier.
  "name": (optional, string) Must be less than 100 characters,
  "description": (optional, string) The description of the Content Block. Must be less than 250 character,
  "content": (optional, string) HTML or text content within Content Block,
  "state": (optional, string) Choose `active` or `draft`. Defaults to `active` if not specified,
  "tags": (optional, array of strings) Tags must already exist
}
```

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `content_block_id`|	Requis |	Chaîne de caractères | L'identifiant API de votre bloc de contenu.|
| `name` | Facultatif | Chaîne de caractères | Nom du bloc de contenu. Doit contenir moins de 100 caractères. |
| `description` | Facultatif | Chaîne de caractères | Description du bloc de contenu. Doit contenir moins de 250 caractères. |
| `content` | Facultatif | Chaîne de caractères | Contenu HTML ou texte dans les blocs de contenu.
| `state` | Facultatif | Chaîne de caractères | Choisir `active` ou `draft`. Défini par défaut sur `active` si cela n’est pas spécifié. |
| `tags` | Facultatif | Tableau de chaînes de caractères | Les [étiquettes]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) doivent déjà exister. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemple de demande
```json
curl --location --request POST 'https://rest.iad-01.braze.com/content_blocks/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "content_block_id" :"content_block_id",
  "name": "content_block",
  "description": "This is my Content Block",
  "content": "HTML or text content within block",
  "state": "draft",
  "tags": ["marketing"]
}'
```

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "content_block_id": (string) Your newly generated block id,
  "liquid_tag": (string) The generated block tag from the Content Block name,
  "created_at": (string) The time the Content Block was created in ISO 8601,
  "message": "success"
}
```

## Résolution des problèmes

Le tableau suivant répertorie les erreurs renvoyées possibles et les étapes de résolution des problèmes associées.

| Erreur | Résolution des problèmes |
| --- | --- |
| `Content cannot be blank` |
| `Content must be a string` | Assurez-vous que votre contenu est compris entre des guillemets (`""`). |
| `Content must be smaller than 50kb` | Le contenu de votre bloc de contenu doit être inférieur à 50 Ko au total. |
| `Content contains malformed liquid` | Le langage Liquid fourni n’est pas valide ou pas analysable. Réessayez avec un langage Liquid valide ou contactez-nous pour obtenir de l’aide. |
| `Content Block cannot be referenced within itself` |
| `Content Block description cannot be blank` |
| `Content Block description must be a string` | Assurez-vous que la description de votre bloc de contenu est comprise entre des guillemets (`""`). |
| `Content Block description must be shorter than 250 characters` |
| `Content Block name cannot be blank` |
| `Content Block name must be shorter than 100 characters` |
| `Content Block name can only contain alphanumeric characters` | Les noms de bloc de contenu peuvent comprendre l’un des caractères suivants : les lettres (majuscules ou minuscules) de `A` à `Z`, les chiffres de `0` à `9`, les tirets `-`, et les traits de soulignement `_`. Il ne peut pas contenir de caractères non alphanumériques comme des émojis, `!`, `@`, `~`, `&` et d’autres caractères « spéciaux ». |
| `Content Block with this name already exists` | Essayez un autre nom. |
| `Content Block name cannot be updated for active Content Blocks` |
| `Content Block state must be either active or draft` |
| `Active Content Block can not be updated to Draft. Create a new Content Block.` |
| `Tags must be an array` | Les balises doivent être un tableau de chaînes de caractères, par exemple `["marketing", "promotional", "transactional"]`. |
| `All tags must be strings` | Assurez-vous que vos balises sont comprises entre des guillemets (`""`). |
| `Some tags could not be found` | Pour ajouter une balise lors de la création d’un bloc de contenu, la balise doit déjà exister dans Braze. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


{% endapi %}
