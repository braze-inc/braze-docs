---
nav_title: "POST : Mettre à jour le bloc de contenu"
article_title: "POST : Mettre à jour le bloc de contenu"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Mettre à jour des blocs de contenu d’e-mail."

---
{% api %}
# Mettre à jour le bloc de contenu
{% apimethod post %}
/content_blocks/update
{% endapimethod %}

Utilisez cet endpoint pour mettre à jour un [bloc de contenu]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4782239a-cb60-4217-9de0-51411434d57d {% endapiref %}

## Limites de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "content_block_id" : (required, string) Content block's API identifier.
  "name": (required, string) Must be less than 100 characters,
  "description": (optional, string) The description of the content block. Must be less than 250 character,
  "content": (required, string) HTML or text content within content block,
  "state": (optional, string) Choose `active` or `draft`. Defaults to `active` if not specified,
  "tags": (optional, array of strings) Tags must already exist
}
```

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `content_block_id`|	Requis |	Chaîne de caractères | L’identifiant API de votre bloc de contenu.|
| `name` | Requis | Chaîne de caractères | Nom du bloc de contenu. Doit contenir moins de 100 caractères. |
| `description` | Facultatif | Chaîne de caractères | Description du bloc de contenu. Doit contenir moins de 250 caractères. |
| `content` | Requis | Chaîne de caractères | HTML ou contenu texte dans les blocs de contenu.
| `state` | Facultatif | Chaîne de caractères | Choisir `active` ou `draft`. Défini par défaut sur `active` si cela n’est pas spécifié. |
| `tags` | Facultatif | Tableau de chaînes de caractères | [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/) doit déjà exister. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze.com/content_blocks/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "content_block_id" :"content_block_id", 
  "name": "content_block",
  "description": "This is my content block",
  "content": "HTML or text content within block",
  "state": "draft",
  "tags": ["marketing"]
}'
```

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "content_block_id": (string) Your newly generated block id,
  "liquid_tag": (string) The generated block tag from the Content Block name,
  "created_at": (string) The time the Content Block was created in ISO 8 601,
  "message": "success"
}
```

### Erreurs possibles

Le tableau suivant répertorie les erreurs renvoyées possibles et les étapes de résolution des problèmes associées, le cas échéant.

| Erreur | Résolution des problèmes |
| --- | --- |
| Le contenu ne peut pas être vide |
| Le contenu doit être une chaîne de caractères | Assurez-vous que votre contenu est compris entre des guillemets (`""`). |
| Le contenu doit être inférieur à 50 Ko | Le contenu de votre bloc de contenu doit être inférieur à 50 Ko. |
| Le contenu contient du langage Liquid incorrect | Le langage Liquid fourni n’est pas valide ou pas analysable. Réessayez avec un langage Liquid valide ou contactez-nous pour obtenir de l’aide. |
| Le bloc de contenu ne peut pas être référencé en soi |
| La description du bloc de contenu ne peut pas être vide |
| La description du bloc de contenu doit être une chaîne de caractères | Assurez-vous que la description de votre bloc de contenu est comprise entre des guillemets (`""`). |
| La description du bloc de contenu doit être inférieure à 250 caractères |
| Le nom du bloc de contenu ne peut pas être vide |
| Le nom du bloc de contenu doit être inférieur à 100 caractères |
| Le nom du bloc de contenu ne peut contenir que des caractères alphanumériques | Les noms de bloc de contenu peuvent comprendre l’un des caractères suivants : les lettres (majuscules ou minuscules) de `A` à `Z`, les chiffres de `0` à `9`, les tirets `-`, et les traits de soulignement `_`. Il ne peut pas contenir de caractères non alphanumériques comme des émojis, `!`, `@`, `~`, `&` et d’autres caractères « spéciaux ». |
| Le bloc de contenu avec ce nom existe déjà | Essayez un autre nom. |
| Le nom du bloc de contenu ne peut pas être mis à jour pour les blocs de contenu actifs |
| L’état du bloc de contenu doit être Actif ou Brouillon |
| Le bloc de contenu actif ne peut pas être mis à jour vers Ébauche. Créer un nouveau bloc de contenu |
| Les balises doivent être un tableau | Les balises doivent être formatées en tant que tableau de chaînes de caractères comme par exemple ["marketing", "promotional", "transactional"]`. |
| Toutes les balises doivent être des chaînes de caractères | Assurez-vous que vos balises sont comprises entre des guillemets (`""`). |
| Certaines balises sont introuvables | Pour ajouter une balise lors de la création d’un bloc de contenu, la balise doit déjà exister dans Braze. |
{: .reset-td-br-1 .reset-td-br-2}


{% endapi %}

