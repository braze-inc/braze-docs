---
nav_title: "GET: Récupérer les alias de lien (Canvas)"
layout: api_page
page_type: Référence
hidden: vrai
permalink: /fr/get_canvas_link_alias/
platform: API
channel:
  - Courriel
tool:
  - Toile
  - Campagnes
description: "Cet article présente des détails sur le point de terminaison GET Link Alias, qui vous permet de récupérer les alias définis à l'étape du courriel de Canvas ."
---

{% api %}
# Point de terminaison de l'alias de lien de canvas
{% apimethod get %}
/fr/canvas/url_info/details
{% endapimethod %}

Utilisez ce point de terminaison pour lister l'alias de lien défini dans une étape particulière du Canevas de courriel.

{% apiref postman %}  {% endapiref %}

## Paramètres de requête

| Paramètre                      | Requis    | Type de données      | Libellé                                                                                                                                                                                                          |
| ------------------------------ | --------- | -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `canas_step_id`                | Requis    | Chaîne de caractères | Voir l'identifiant API [Canvas Step]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier).                                                                                                              |
| `Id de la variante du message` | Requis    | Chaîne de caractères | Identifiant API de la variante de message (pour la variante du message e-mail à cette étape). Vous pouvez le trouver en cliquant sur **Analyser les variantes** sur la page de détails de Canvas pour un Canvas. |
| `inclue l'id du lien`          | Optionnel | Chaîne de caractères | Un identifiant de lien spécifique (comme assigné par le Brésil) ou `null`. Ceci est utilisé pour filtrer les résultats par un `link_id spécifique`.                                                              |
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

- `ID canvas manquant/ID invalide` - L'ID API Canvas doit être un identifiant API. Vous pouvez le trouver en utilisant le [point d'extrémité de la liste des canvas]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/) ou en vous connectant au tableau de bord.

- `ID de variante de message manquant/invalide` - L'ID API de la variante de message de message doit être un identifiant API. Vous pouvez le trouver en utilisant le [Point d'extrémité des détails de Canvas]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/) ou en vous connectant au tableau de bord.


{% endapi %}
