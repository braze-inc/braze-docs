---
nav_title: "POST: Mettre à jour le bloc de contenu"
article_title: "POST: Mettre à jour le bloc de contenu"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: Référence
description: "Cet article décrit les détails de la mise à jour du contenu des blocs de contenu Braze."
---

{% api %}
# Mettre à jour le bloc de contenu
{% apimethod post %}
/fr/content_blocks/update
{% endapimethod %}

Utilisez ce point de terminaison ci-dessous pour mettre à jour un [bloc de contenu de courriel]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4782239a-cb60-4217-9de0-51411434d57d {% endapiref %}

## Limite de taux

{% include rate_limits.md endpoint='default' %}

## Corps de la requête

```
Type de contenu : application/json
Autorisation : Bearer YOUR-REST-API-KEY
```

```json
{
  "content_block_id" : (requis, chaîne) Identifiant API du bloc de contenu.
  "name": (obligatoire, chaîne) Doit comporter moins de 100 caractères,
  "description": (optionnel, chaîne) La description du bloc de contenu. Doit comporter moins de 250 caractères,
  "content": (obligatoire, chaîne) HTML ou contenu texte dans le bloc de contenu,
  "state": (optionnel, chaîne) Choisissez `active` ou `draft`. Par défaut, `active` si non spécifié,
  "tags": (optionnel, tableau de chaînes) Les balises doivent déjà exister
}
```

## Paramètres de la requête

| Paramètre                    | Requis    | Type de données      | Libellé                                                                                                             |
| ---------------------------- | --------- | -------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `format@@0 content_block_id` | Requis    | Chaîne de caractères | L'identifiant API de votre bloc de contenu.                                                                         |
| `Nom`                        | Requis    | Chaîne de caractères | Nom du bloc de contenu. Doit comporter moins de 100 caractères.                                                     |
| `Libellé`                    | Optionnel | Chaîne de caractères | Description du bloc de contenu. Doit comporter moins de 250 caractères.                                             |
| `contenu`                    | Requis    | Chaîne de caractères | Contenu HTML ou texte dans les blocs de contenu.                                                                    |
| `Etat`                       | Optionnel | Chaîne de caractères | Choisissez `actif` ou `brouillon`. Par défaut, `active` si non spécifiée.                                           |
| `Tags`                       | Optionnel | Tableau de chaînes   | [Les balises]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/) doivent déjà exister. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze. om/content_blocks/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "content_block_id" :"content_block_id", 
  "name": "content_block",
  "description": "Ceci est mon bloc de contenu",
  "contenu": "HTML ou contenu texte dans le bloc",
  "state": "brouillon",
  "tags": ["marketing"]
}'
```

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "content_block_id": "newly-generated-block-id",
  "liquid_tag": "generated-block-tag-from-content_block_name",
  "created_at": "time-created-in-iso",
  "message": "success"

```

### Erreurs possibles
- `Le contenu ne peut pas être vide.`

- `Le contenu doit être une chaîne.`

- `Le contenu doit être inférieur à 50 kb.` - Le contenu de votre bloc de contenu doit être inférieur à 50 kb au total.

- `Le contenu contient un liquide malformé.` - Le liquide fourni par le liquide n'est pas valide ou parsable. Veuillez réessayer ou contacter le support.

- `Le bloc de contenu ne peut pas être référencé en lui-même.`

- `La description du bloc de contenu ne peut pas être vide.`

- `La description du bloc de contenu doit être une chaîne.`

- `La description du bloc de contenu doit être inférieure à 250 caractères.` - La description de votre bloc de contenu doit être inférieure à 250 caractères.

- `Le nom du bloc de contenu ne peut pas être vide.`

- `Le nom du bloc de contenu doit contenir moins de 100 caractères.`

- `Le nom du bloc de contenu ne peut contenir que des caractères alphanumériques.` - Les noms de blocs de contenu peuvent inclure n'importe lequel des caractères suivants : les lettres (majuscules ou minuscules) `A` à travers `Z`, les nombres `0` à `9`, tirets `-`, et tirets bas `_`. Il ne peut pas contenir des caractères non alphanumériques comme des émojis, `!`, `@`, `~`, `&`, et autres caractères "spéciaux".

- `Un bloc de contenu portant ce nom existe déjà.`

- `Le nom du bloc de contenu ne peut pas être mis à jour pour les blocs de contenu actifs.`

- `L'état du bloc de contenu doit être actif ou Brouillon.`

- `Le bloc de contenu actif ne peut pas être mis à jour en brouillon. Veuillez créer un nouveau bloc de contenu.`

- `Les tags doivent être un tableau.`

- `Toutes les balises doivent être des chaînes.`

- `Certaines balises sont introuvables.`

{% endapi %}
