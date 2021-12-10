---
nav_title: "GET: Voir les informations des blocs de contenu"
article_title: "GET: Voir les informations des blocs de contenu"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: Référence
description: "Cet article décrit les détails sur le point de terminaison de Braze de l'information des blocs de contenu disponibles."
---

{% api %}
# Voir les informations du bloc de contenu
{% apimethod get %}
/fr/content_blocks/info
{% endapimethod %}

Cet endpoint appellera des informations pour vos [blocs de contenu d'e-mail existants]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#589adda3-0def-4369-9ddc-eae71923c0ee {% endapiref %}

## Paramètres de la requête

| Paramètre                         | Requis    | Type de données      | Libellé                                                                                                                                                                                                                                                                                          |
| --------------------------------- | --------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `format@@0 content_block_id`      | Requis    | Chaîne de caractères | L'identifiant du bloc de contenu. <br><br>Vous pouvez le trouver en listant les informations du bloc de contenu via un appel API ou en allant dans **Console Développeur** > **Paramètres de l'API**, puis défile vers le bas et recherche votre identifiant API de bloc de contenu. |
| `Inclure les données d'inclusion` | Optionnel | Boolean              | Quand réglé sur `true`, l'API retourne l'identifiant API Message Variation API des campagnes et Canvases où ce bloc de contenu est inclus, pour être utilisé dans les appels suivants.  Les résultats excluent les campagnes archivées ou supprimées ou les Canvases.                            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/content_blocks/info?content_block_id={{content_block_id}}&include_inclusion_data=No' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR-API-KEY-HERE
{
  "content_block_id": "string",
  "name": "string",
  "content": "string",
  "description": "string",
  "content_type": "html ou texte",
  "tags": "tableau de chaînes",
  "created_at": "time-in-iso",
  "last_edited": "time-in-iso",
  "inclusion_count" : "integer",
  "inclusion_data": "tableau",
  "message": "success",
}
```

### Erreurs possibles
- `L'ID de bloc de contenu ne peut pas être vide.` - Un bloc de contenu n'a pas été listé ou n'est pas encapsulé entre guillemets.

- `L'ID de bloc de contenu n'est pas valide pour ce groupe d'applications.` - Ce bloc de contenu n'existe pas ou est dans un autre compte d'entreprise ou groupe d'applications.

- `Le bloc de contenu a été supprimé - contenu non disponible.` - Ce bloc de contenu, bien qu'il ait pu exister auparavant, a été supprimé.

- `Inclure les données d'inclusion - erreur` - Un de vrai ou faux n'est pas fourni.

{% endapi %}
