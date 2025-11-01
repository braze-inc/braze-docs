---
nav_title: "GET : Voir les informations sur les blocs de contenu"
article_title: "GET : Voir les informations sur les blocs de contenu"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Afficher les informations sur les blocs de contenu."
---

{% api %}
# Voir les informations sur les blocs de contenu
{% apimethod get %}
/content_blocks/info
{% endapimethod %}

> Utilisez cet endpoint pour appeler les informations relatives à vos [blocs de contenu]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) existants.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#589adda3-0def-4369-9ddc-eae71923c0ee {% endapiref %}

## Conditions préalables
Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/api_key/) avec l’autorisation `content_blocks.info`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `content_block_id`  | Requis | Chaîne de caractères | L'identifiant du bloc de contenu. <br><br>Vous pouvez le trouver soit en listant les informations du bloc de contenu par le biais d'un appel API, soit en vous rendant sur la page des [clés API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/), puis en défilant vers le bas et en recherchant votre identifiant API du bloc de contenu.|
| `include_inclusion_data`  | Facultatif | Valeur booléenne | Lorsqu'elle est définie sur `true`, l'API renvoie l'identifiant API de la variation de message des campagnes et des canevas dans lesquels ce bloc de contenu est inclus, afin qu'il soit utilisé dans les appels ultérieurs.  Les résultats excluent les campagnes ou Canvas archivé(e)s ou supprimé(e)s. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemple de demande
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/content_blocks/info?content_block_id={{content_block_id}}&include_inclusion_data=false' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "content_block_id": (string) the Content Block identifier,
  "name": (string) the name of the Content Block,
  "content": (string) the content in the Content Block,
  "description": (string) the Content Block description,
  "content_type": (string) the content type, html or text,
  "tags": (array) An array of tags formatted as strings,
  "created_at": (string) The time the Content Block was created in ISO 8601,
  "last_edited": (string) The time the Content Block was last edited in ISO 8601,
  "inclusion_count" : (integer) the inclusion count,
  "inclusion_data": (array) the inclusion data,
  "message": "success",
}
```

## Résolution des problèmes

Le tableau suivant répertorie les erreurs renvoyées possibles et les étapes de résolution des problèmes associées.

| Erreur | Résolution des problèmes |
| --- | --- |
| `Content Block ID cannot be blank` | Assurez-vous qu’un bloc de contenu est répertorié dans votre demande et compris entre des guillemets (`""`). |
| `Content Block ID is invalid for this workspace` | Ce bloc de contenu n'existe pas ou se trouve dans un compte d'entreprise ou un espace de travail différent. |
| `Content Block has been deleted—content not available` | Ce bloc de contenu, bien qu’il ait pu exister, a été supprimé. |
| `Include Inclusion Data—error` | Ce paramètre accepte uniquement les valeurs booléennes (vrai ou faux). Assurez-vous que la valeur de `include_inclusion_data` n’est pas comprise entre des guillemets (`""`), sinon la valeur est envoyée comme chaîne de caractères. Voir les [paramètres de la demande](#request-parameters) pour plus de détails. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


{% endapi %}
