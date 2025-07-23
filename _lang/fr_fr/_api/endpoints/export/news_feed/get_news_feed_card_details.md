---
nav_title: "GET : Détails de la carte de fil d'actualité pour l'exportation"
article_title: "GET : Détails de la carte de fil d'actualité pour l'exportation"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Exporter les informations relatives à la carte de fil d’actualité."

---
{% api %}
# Exporter les informations relatives à la carte de fil d’actualité
{% apimethod get %}
/feed/details
{% endapimethod %}

> Utilisez cet endpoint pour récupérer des informations pertinentes sur une carte, qui peuvent être identifiées par le `card_id`.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5b1401a6-f12c-4827-82c9-8dc604f1671e {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `feed.details`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de demande

| Paramètre | Requis | Type de données | Description            |
| --------- | -------- | --------- | ---------------------- |
| `card_id` | Requis | Chaîne de caractères | Voir l'[identifiant API de la carte]({{site.baseurl}}/api/identifier_types/). <br><br> Vous trouverez le site `card_id` pour une carte donnée sur la page des [clés API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) et sur la page des détails de la carte dans votre tableau de bord, ou vous pouvez utiliser le [point de terminaison Exporter la liste des cartes du fil d'actualité]({{site.baseurl}}/api/endpoints/export/news_feed/get_news_feed_cards/).|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemple de demande
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/feed/details?card_id={{card_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) The status of the export, returns 'success' when completed without errors,
    "created_at" : (string) the ate created as ISO 8601 date,
    "updated_at" : (string) the ate last updated as ISO 8601 date,
    "name" : (string) the card name,
    "publish_at" : (string) the date the card was published as ISO 8601 date,
    "end_at" : (string) the date the card will stop displaying for users as ISO 8601 date,
    "tags" : (array) the tag names associated with the card,
    "title" : (string) the title of the card,
    "image_url" : (string) the image URL used by this card,
    "extras" : (dictionary) a dictionary containing key-value pair data attached to this card,
    "description" : (string) the description text used by this card,
    "archived": (boolean) whether this Card is archived,
    "draft": (boolean) whether this Card is a draft,
}
```

{% alert tip %}
Pour obtenir de l’aide sur les exportations CSV et de l’API, consultez la section [Résolution des problèmes d’exportation]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
