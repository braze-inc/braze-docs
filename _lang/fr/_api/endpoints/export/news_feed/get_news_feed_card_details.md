---
nav_title: "GET : Informations relatives à la carte de fil d’actualité"
article_title: "GET : Informations relatives à la carte de fil d’actualité"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: référence
description: "Cet article présente en détail l’endpoint Informations relatives à la carte de fil d’actualité."

---
{% api %}
# Endpoint Informations relatives à la carte de fil d’actualité
{% apimethod get %}
/feed/details
{% endapimethod %}

Utilisez cet endpoint pour récupérer des informations pertinentes sur une carte, qui peuvent être identifiées par le `card_id`.

{% alert note %}
Les fils d'actualités deviennent obsolètes. Braze recommande aux clients qui utilisent son outil Fil d'actualité de passer à son canal de communication de cartes de contenu qui est plus flexible, personnalisable et fiable. Pour en savoir plus, consultez le [guide de migration]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/).
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5b1401a6-f12c-4827-82c9-8dc604f1671e {% endapiref %}

## Limites de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de demande

| Paramètre | Requis | Type de données | Description            |
| --------- | -------- | --------- | ---------------------- |
| `card_id` | Requis | String | Voir [Identifiant API de carte]({{site.baseurl}}/api/identifier_types/). <br><br> Le `card_id` pour une carte donnée se trouve sur la page **Console du développeur** et sur la page d'informations relatives à la carte dans votre tableau de bord, sinon vous pouvez utiliser l'[endpoint Liste des fils d'actualité]({{site.baseurl}}/api/endpoints/export/news_feed/get_news_feed_cards/).|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

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
    "message": (required, string) Le statut de l’exportation, renvoie « réussite » lorsqu’elle s’achève sans erreur,
    "created_at" : (string) la date de création en tant que date ISO 8601,
    "updated_at" : (string) la date de dernière mise à jour en tant que date ISO 8601,
    "name" : (string) le nom de carte,
    "publish_at" : (string) la date à laquelle la carte a été publiée en tant que date ISO 8601,
    "end_at" : (string) la date à laquelle la carte arrêtera de s’afficher pour les utilisateurs en tant que date ISO 8601,
    "tags" : (array) les noms de balise associés à la carte,
    "title" : (string) le titre de la carte,
    "image_url" : (string) l’URL de l’image utilisée par cette carte,
    "extras" : (dictionary) un dictionnaire contenant des données d’une paire clé-valeur jointe à cette carte,
    "description" : (string) le texte de la description utilisée par cette carte,
    "archived": (boolean) si cette carte est archivée ou non,
    "draft": (boolean) si cette carte est un brouillon ou non,
}
```

{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et de l'API, consultez la section [Résolution des problèmes d'exportation]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
