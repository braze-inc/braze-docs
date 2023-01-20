---
nav_title: "GET : Récupérer des alias de lien (campagne)"
layout: api_page
page_type: article de référence
hidden: true
permalink: /get_campaign_link_alias/

platform: API
channel:
  - E-mail
tool:
  - Canvas
  - Campagnes

description: "Cet article présente des informations concernant l’endpoint d’alias de lien GET, qui vous permet de récupérer les alias définis sur une variante de message de campagne."
---
{% api %}
# Endpoint d’alias de lien de campagne
{% apimethod get %}
/campaigns/url_info/details
{% endapimethod %}

Utilisez cet endpoint pour lister l’alias de lien défini dans une variante de message de campagne.

{% apiref postman %}  {% endapiref %}

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `campaign_id`  | Requis | Chaîne de caractères | Voir [identifiant API de campagne]({{site.baseurl}}/api/identifier_types/#campaign-api-identifier).|
| `message_variation_id `  |  Requis | Chaîne de caractères | Identifiant API de variante : Pour cela, cliquez sur la page d’informations de campagne, dans la section **Identifiant API** section. |
| `includes_link_id` | Facultatif | Chaîne de caractères | Un identifiant de lien spécifique (tel qu’attribué par Braze) ou `null`. Ceci permet de filtrer les résultats par un `link_id` spécifique. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Exemple de demande
```
curl --location --request GET 'https://rest.iad-01.braze.com/campaigns/url_info/details?campaign_id=4615a404-b2c2-421e-9a04-2233bb3ec4f9&message_variation_id=0ea708fe-36b4-43f7-9f5c-a0650ea2a7a0&includes_link_id=014tk4e0kg97' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "channel": "email",
  "name": "Variant 1",
  "link_data": [
    {
      "link_URL": "https://www.braze.com?lid=014tk4e0kg97",
      "link_id": "014tk4e0kg97",
      "content_block_path_info": [],
      "link_alias": "link5"
    }
  ],
  "message": "réussite"
}
```

### Erreurs possibles

- `Missing/Invalid Campaign ID` -L’ID API de campagne doit être un identifiant API. Pour cela, cliquez sur [l’endpoint Listes de campagnes]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/) ou en vous connectant au tableau de bord.
- `Missing/Invalid Message Variant ID` -L’ID API de variante de message doit être un identifiant API. Pour cela, cliquez sur [l’endpoint Informations sur la campagne]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/) ou en vous connectant au tableau de bord.


{% endapi %}
