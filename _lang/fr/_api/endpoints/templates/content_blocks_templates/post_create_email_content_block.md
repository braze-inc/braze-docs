---
nav_title: "POST : Créer un bloc de contenu"
article_title: "POST : Créer un bloc de contenu"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Créer des blocs de contenu d’e-mail."

---
{% api %}
# Créer un bloc de contenu
{% apimethod post %}
/content_blocks/create
{% endapimethod %}

Utilisez cet endpoint pour créer un [bloc de contenu]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f1cefa8b-7a28-4e64-b579-198a4610d0a5 {% endapiref %}

## Limites de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "name": (required, string) Doit contenir moins de 100 caractères.,
  "description": (optional, string) La description du bloc de contenu. Doit contenir moins de 250 caractères.,
  "content": (required, string) HTML ou contenu texte dans un bloc de contenu,
  "state": (optional, string) Choisissez `actif` ou `brouillon`. Défini par défaut sur `actif` si cela n’est pas spécifié.,
  "tags": (optional, array of strings) Tags doit déjà exister.
}
```

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `name` | Requis | String | Nom du bloc de contenu. Doit contenir moins de 100 caractères. |
| `description` | Facultatif | String | Description du bloc de contenu. Doit contenir moins de 250 caractères. |
| `content` | Requis | String | HTML ou contenu texte dans le bloc de contenu. |
| `state` | Facultatif | String | Choisir `active` ou `draft`. Défini par défaut sur `active` si cela n’est pas spécifié. |
| `tags` | Facultatif | Tableau de chaînes de caractères | [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/) doit déjà exister. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze.com/content_blocks/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "name": "content_block",
  "description": "Ceci est mon bloc de contenu",
  "content": "HTML content within block",
  "state": "draft",
  "tags": ["marketing"]
}
'
```

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "content_block_id": (string) Votre ID de bloc venant d’être généré,
  "liquid_tag": (string) La balise de bloc générée à partir du nom du bloc de contenu,
  "created_at": (string) Le moment auquel le bloc de contenu a été créé en ISO 8601,
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
| L’état du bloc de contenu doit être Actif ou Brouillon |
| Les balises doivent être un tableau | Les balises doivent être un array de strings, par exemple `["marketing", "promotional", "transactional"]`. |
| Toutes les balises doivent être des chaînes de caractères | Assurez-vous que vos balises sont comprises entre des guillemets (`""`). |
| Certaines balises sont introuvables | Pour ajouter une balise lors de la création d’un bloc de contenu, la balise doit déjà exister dans Braze. |
{: .reset-td-br-1 .reset-td-br-2}


{% endapi %}
