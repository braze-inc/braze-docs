---
nav_title: "GET : Alias de lien de liste pour les campagnes"
layout: api_page
page_type: reference
hidden: true
permalink: /get_campaign_link_alias/

platform: API
channel:
  - Email
tool:
  - Canvas
  - Campaigns

description: "Cet article présente les détails du point de terminaison List link alias Braze."
---
{% api %}
# Liste des alias de liens pour la campagne
{% apimethod get %}
/campaigns/url_info/details
{% endapimethod %}

> Utilisez cet endpoint pour dresser la liste des alias de liens définis dans une variante de message de campagne spécifique.

{% apiref postman %}  {% endapiref %}

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `campaign_id`  | Nécessaire | Chaîne de caractères | Voir l'[identifiant API de la campagne.]({{site.baseurl}}/api/identifier_types/#campaign-api-identifier)|
| `message_variation_id `  |  Nécessaire | Chaîne de caractères | Identifiant API de variante : Vous trouverez cette information sur la page des détails d'une campagne, dans la section **Identifiant API.**  |
| `includes_link_id` | Facultatif | Chaîne de caractères | Un identifiant de lien spécifique (tel qu’attribué par Braze) ou `null`. Ceci permet de filtrer les résultats par un `link_id` spécifique. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

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
  "message": "success"
}
```

### Résolution des problèmes

Le tableau suivant répertorie les erreurs renvoyées possibles et les étapes de résolution des problèmes associées.

| Erreur | Résolution des problèmes |
| --- | --- |
| `Missing/Invalid Campaign ID` | L'ID API de la campagne doit être un identifiant API. Vous pouvez le trouver en utilisant le [point de terminaison de la liste des campagnes d'exportation]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/) ou en vous connectant au tableau de bord. |
| `Missing/Invalid Message Variant ID` | L'ID de variante de message API doit être un identifiant API. Vous pouvez le trouver en utilisant l'[endpoint Exporter les détails de la campagne]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/) ou en vous connectant au tableau de bord. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


{% endapi %}
