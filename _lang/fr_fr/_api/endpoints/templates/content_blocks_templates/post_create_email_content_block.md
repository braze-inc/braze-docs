---
nav_title: "POST : Créer un bloc de contenu"
article_title: "POST : Créer un bloc de contenu"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Créer des blocs de contenu."

---
{% api %}
# Créer un bloc de contenu
{% apimethod post %}
/content_blocks/create
{% endapimethod %}

> Utilise ce point de terminaison pour créer un [bloc de contenu]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f1cefa8b-7a28-4e64-b579-198a4610d0a5 {% endapiref %}

## Conditions préalables
Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/api_key/) avec l’autorisation `content_blocks.create`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "name": (required, string) Must be less than 100 characters,
  "description": (optional, string) The description of the Content Block. Must be less than 250 character,
  "content": (required, string) HTML or text content within Content Block,
  "state": (optional, string) Choose `active` or `draft`. Defaults to `active` if not specified,
  "tags": (optional, array of strings) Tags must already exist
}
```

## Paramètres de demande

| Paramètre - Requis - Type de données - Description - Paramètre - Requis - Type de données - Description - Paramètre - Requis - Type de données - Description
|---|---|---|---|
| `name` | Requis | Chaîne de caractères | Nom du bloc de contenu. Doit contenir moins de 100 caractères.
| `description` | Facultatif | Chaîne de caractères | Description du bloc de contenu. Doit contenir moins de 250 caractères.
| `content` | Requis | Chaîne | HTML ou texte contenu dans le bloc de contenu. |
| `state` | Facultatif | Chaîne de caractères | Choisis `active` ou `draft`. La valeur par défaut est `active` si elle n'est pas spécifiée. |
(optionnel, tableau de chaînes de caractères) les balises doivent déjà exister,
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
```json
curl --location --request POST 'https://rest.iad-01.braze.com/content_blocks/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "name": "content_block",
  "description": "This is my Content Block",
  "content": "HTML content within block",
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
| `Content cannot be blank` | | |
| `Content must be a string` | Assure-toi que ton contenu est entre guillemets (`""`). |
| `Content must be smaller than 50kb` | Le contenu de votre bloc de contenu doit être inférieur à 50 ko. |
| `Content contains malformed liquid` | Le liquide fourni n'est pas valide ou analysable. Réessayez avec un langage Liquid valide ou contactez-nous pour obtenir de l’aide.
| `Content Block cannot be referenced within itself` | |
| `Content Block description cannot be blank` | |
| `Content Block description must be a string` | Assure-toi que la description de ton bloc de contenu est entre guillemets (`""`). |
| `Content Block description must be shorter than 250 characters` | |
| `Content Block name cannot be blank` | |
| `Content Block name must be shorter than 100 characters` | |
`Content Block name can only contain alphanumeric characters` | Les noms des blocs de contenu peuvent inclure l'un des caractères suivants : les lettres (majuscules ou minuscules) `A` à `Z`, les chiffres `0` à `9`, les tirets `-` et les traits de soulignement `_`. Le nom ne peut pas contenir de caractères non alphanumériques comme les emojis, `!`, `@`, `~`, `&` et d'autres caractères « spéciaux ». |
| `Content Block with this name already exists` | Essaie un autre nom. |
| `Content Block state must be either active or draft` | |
| `Tags must be an array` | Les balises doivent être formatées comme un tableau de chaînes de caractères, par exemple `["marketing", "promotional", "transactional"]`. | |
| `All tags must be strings` | Assure-toi que tes balises sont entre guillemets (`""`). |
`Some tags could not be found` | Pour ajouter une balise lors de la création d'un bloc de contenu, la balise doit déjà exister dans Braze. |
{: .reset-td-br-1 .reset-td-br-2}


{% endapi %}
