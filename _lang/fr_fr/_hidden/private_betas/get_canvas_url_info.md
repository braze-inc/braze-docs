---
nav_title: "GET : Répertorier les alias de lien pour Canvas"
layout: api_page
page_type: reference
hidden: true
permalink: /get_canvas_link_alias/

platform: API
channel:
  - Email
tool:
  - Canvas
  - Campaigns

description: "Cet article présente en détails l’endpoint Lister les alias de liens pour Canvas."
---
{% api %}
# Liste des alias de lien pour Canvas
{% apimethod get %}
/canvas/url_info/details
{% endapimethod %}

> Utilisez ce point de terminaison pour lister l'alias de lien défini dans une étape spécifique de l'email Canvas.

{% apiref postman %}  {% endapiref %}

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `canvas_step_id` | Nécessaire | Chaîne de caractères | Voir [Identifiant de l'API de l'étape de Canvas]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier). |
| `message_variation_id ` | Nécessaire | Chaîne de caractères | Identifiant API de variante de message (pour la variante de message e-mail dans cette étape). Vous pouvez trouver cela en cliquant sur **Analyser les variantes** sur la page **Détails de la toile**. |
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
  "message": "success"
}
```

### Résolution des problèmes

Le tableau suivant répertorie les erreurs renvoyées possibles et les étapes de résolution des problèmes associées.

| Erreur | Résolution des problèmes |
| --- | --- |
| `Missing/Invalid Canvas ID` | L'ID de l'API Canvas doit être un identifiant d'API. Vous pouvez trouver cela en utilisant le point de terminaison [Export Canvas list]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/) ou en vous connectant au tableau de bord. |
| `Missing/Invalid Message Variant ID` | L'ID de variante de message API doit être un identifiant API. Vous pouvez trouver cette information en utilisant l’[endpoint Exporter les détails du Canvas]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/) ou en vous connectant au tableau de bord. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
