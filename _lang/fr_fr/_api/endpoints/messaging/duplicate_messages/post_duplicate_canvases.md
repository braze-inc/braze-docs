---
nav_title: "POST : Dupliquer les Canvas"
article_title: "POST : Dupliquer les Canvas"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "Cet article présente les détails de l'endpoint Dupliquer les Canvas."
---

{% api %}
# Dupliquer des Canvas à l'aide de l'API
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/canvas/duplicate
{% endapimethod %}

> Utilisez cet endpoint pour dupliquer des Canvas. Cet endpoint API fonctionne de manière similaire à la [duplication de Canvas dans le tableau de bord de Braze][1].

## Conditions préalables

Pour utiliser cet endpoint, vous devez générer une clé API avec l'autorisation `canvas.duplicate`.

## Limite de débit

Cet endpoint est limité à 100 appels API par minute.

## Corps de la requête

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) The Canvas identifier,
  "name": (required, string) The name of the resulting Canvas,
  "description": (optional, string) The description of the resulting Canvas,
  "tag_names": (optional, string) The tags of the resulting Canvas,
}
```

## Paramètres de requête

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
|`canvas_id`| Requis | Chaîne de caractères | Voir [Identifiant Canvas](https://www.braze.com/docs/api/identifier_types/). |
|`name`| Requis | Chaîne de caractères | Le nom du Canvas résultant. |
|`description`| Facultatif | Chaîne de caractères | Le champ de description du Canvas résultant. |
|`tag_names` | Facultatif | Chaîne de caractères | Les étiquettes du Canvas résultant. Il doit s'agir d'étiquettes existantes. Si vous ajoutez de nouvelles étiquettes dans la requête, elles remplaceront toutes les étiquettes présentes sur le Canvas d'origine. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Réponse

Cet endpoint renvoie un code d'état `202` et la création du Canvas s'effectue de manière asynchrone. Vous pouvez utiliser le [téléchargement des événements de sécurité][2] pour consulter les enregistrements indiquant quand les Canvas ont été dupliqués et par quelle clé API.

[1]: {{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/duplicating
[2]: {{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings

{% endapi %}