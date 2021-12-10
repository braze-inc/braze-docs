---
nav_title: "GET: Récupérer les alias de lien (Campaign)"
layout: api_page
page_type: Référence
hidden: vrai
permalink: /get_campaign_link_alias/
platform: API
channel:
  - Courriel
tool:
  - Toile
  - Campagnes
description: "Cet article présente des détails sur le point de terminaison GET Link Alias, qui vous permet de récupérer les alias définis sur une variante de message de campagne."
---

{% api %}
# Point de terminaison du lien de campagne
{% apimethod get %}
/fr/campaigns/url_info/details
{% endapimethod %}

Utilisez ce point de terminaison pour lister l'alias de lien défini dans une variante de message de campagne.

{% apiref postman %}  {% endapiref %}

## Paramètres de requête

| Paramètre                      | Requis    | Type de données      | Libellé                                                                                                                                                           |
| ------------------------------ | --------- | -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `campaign_id`                  | Requis    | Chaîne de caractères | Voir [l'identifiant API de la campagne]({{site.baseurl}}/api/identifier_types/#campaign-api-identifier).                                                          |
| `Id de la variante du message` | Requis    | Chaîne de caractères | Identificateur de la variante de l'API. Vous pouvez le trouver sur la page de détails de la campagne pour une campagne, dans la section **Identificateur d'API**. |
| `inclue l'id du lien`          | Optionnel | Chaîne de caractères | Un identifiant de lien spécifique (comme assigné par le Brésil) ou `null`. Ceci est utilisé pour filtrer les résultats par un `link_id spécifique`.               |
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
  "name": "Variante 1",
  "link_data": [
    {
      "link_URL": "https://www. raze.com? id=014tk4e0kg97",
      "link_id": "014tk4e0kg97",
      "content_block_path_info": [],
      "link_alias": "link5"
    }
  ],
  "message": "success"
}
```

### Erreurs possibles

- `Identifiant de campagne manquant / non valide` - L'ID API de la campagne doit être un identifiant API. Vous pouvez le trouver en utilisant le [point d'extrémité de la liste des campagnes]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/) ou en vous connectant au tableau de bord.

- `ID de variante de message manquant/invalide` - L'ID API de la variante de message de message doit être un identifiant API. Vous pouvez le trouver en utilisant le [Point de terminaison des détails de la campagne]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/) ou en vous connectant au tableau de bord.


{% endapi %}
