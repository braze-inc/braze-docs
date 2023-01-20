---
nav_title: "GET : Informations relatives au segment"
article_title: "GET : Informations relatives au segment"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: référence
description: "Cet article présente en détail l’endpoint Informations relatives au segment pour exporter une liste de segments disponibles et son utilisation."

---
{% api %}
# Endpoint Informations relatives au segment
{% apimethod get %}
/segments/details
{% endapimethod %}

Utilisez cet endpoint pour récupérer des informations pertinentes sur un segment, qui peuvent être identifiées par le `segment_id`.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aab56ed9-0a28-476a-8b57-b79786dbb9c1 {% endapiref %}

## Limites de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de demande

| Paramètre    | Requis | Type de données | Description            |
| ------------ | -------- | --------- | ---------------------- |
| `segment_id` | Requis | String | Voir [Identifiant API de segment]({{site.baseurl}}/api/identifier_types/).<br><br> Le `segment_id` pour un segment donné se trouve dans votre **Console du développeur** sur votre compte Braze, sinon vous pouvez utiliser l'[endpoint Liste des segments]({{site.baseurl}}/api/endpoints/export/segments/get_segment/).  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/segments/details?segment_id={{segment_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
      "message": (required, string) le statut de l’exportation, renvoie « réussite » lorsqu’elle s’achève sans erreur,
      "created_at" : (string) la date de création en tant que date ISO 8601,
      "updated_at" : (string) la date de dernière mise à jour en tant que date ISO 8601,
      "name" : (string) le nom du segment,
      "description" : (string) une description des filtres pouvant être lue par un humain,
      "text_description" : (string) la description du segment 
      "tags" : (array) les noms de balise associés au segment formatés en tant que chaînes de caractères
}
```

{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et de l'API, consultez la section [Résolution des problèmes d'exportation]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
