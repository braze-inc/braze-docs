---
nav_title: "GET : Récupérer des alias de lien (Canvas)"
layout: api_page
page_type: article de référence
hidden: true
permalink: /get_canvas_link_alias/

platform: API
channel:
  - E-mail
tool:
  - Canvas
  - Campagnes

description: "Cet article présente des informations concernant l’endpoint d’alias de lien GET, qui vous permet de récupérer les alias définis sur une étape d’e-mail Canvas."
---
{% api %}
# Endpoint d’alias de lien de Canvas
{% apimethod get %}
/canvas/url_info/details
{% endapimethod %}

Utilisez cet endpoint pour lister l’alias de lien défini dans une étape Canvas relative aux e-mails.

{% apiref postman %}  {% endapiref %}

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `canvas_step_id`  | Requis | Chaîne de caractères | Voir [Identifiant API de Canvas Step]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier). |
| `message_variation_id `  |  Requis | Chaîne de caractères | Identifiant API de variante de message (pour la variante de message e-mail dans cette étape). Pour cela, cliquez sur **Analyser les variantes** sur la page d’informations d’un Canvas. |
| `includes_link_id` | Facultatif | Chaîne de caractères | Un identifiant de lien spécifique (tel qu’attribué par Braze) ou `null`. Ceci permet de filtrer les résultats par un `link_id` spécifique. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

## Exemple de demande
```
curl --location --request GET 'https://rest.iad-01.braze.com/canvas/url_info/details?campaign_id=4615a404-b2c2-421e-9a04-2233bb3ec4f9&message_variation_id=0ea708fe-36b4-43f7-9f5c-a0650ea2a7a0&includes_link_id=014tk4e0kg97' \
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

- `Missing/Invalid Canvas ID` - L’ID API de Canvas doit être un identifiant API. Pour cela, cliquez sur [l’endpoint Liste des Canvas]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/) ou en vous connectant au tableau de bord.
- `Missing/Invalid Message Variant ID` -L’ID API de variante de message doit être un identifiant API. Pour cela, cliquez sur [l’endpoint Informations sur le Canvas]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/) ou en vous connectant au tableau de bord.


{% endapi %}
