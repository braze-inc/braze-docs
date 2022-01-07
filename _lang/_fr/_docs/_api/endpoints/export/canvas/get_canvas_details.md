---
nav_title: "GET: Détails de la toile"
article_title: "GET: Détails de la toile"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: Référence
description: "Cet article décrit les détails sur le point de terminaison des détails de Canvas ."
---

{% api %}
# Point de terminaison des détails du canevas
{% apimethod get %}
/fr/canvas/details
{% endapimethod %}

Ce point de terminaison vous permet d'exporter des métadonnées sur un Canvas, comme son nom, quand il a été créé, son statut actuel, et plus encore.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5188873c-13a3-4aaf-a54b-9fa1daeac5f8 {% endapiref %}

## Limite de taux

{% include rate_limits.md endpoint='default' %}

## Paramètres de la requête

| Paramètre  | Requis | Type de données      | Libellé                                                              |
| ---------- | ------ | -------------------- | -------------------------------------------------------------------- |
| `id_toile` | Requis | Chaîne de caractères | Voir [Canvas API Identifier]({{site.baseurl}}/api/identifier_types/) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/details?canvas_id={{canvas_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "created_at": (string) date créée en tant que date ISO 8601,
  "updated_at": (string) date mise à jour en tant que date ISO 8601,
  "name": (string) Nom du canevas,
  "description": (string) Description du canevas,
  "archivé" : (booléen) si ce Canvas est archivé,
  "brouillon : (booléen) si ce Canvas est un brouillon,
  "schedule_type": (chaîne) type d'action de planification,
  "first_entry": (chaîne) date de la première entrée en tant que date ISO 8601,
  "last_entry": (chaîne) date de la dernière entrée en date ISO 8601,
  "channels": (tableau de chaînes) pas de canaux utilisés avec Canvas,
  "variants": [
    {
      "name": (string) nom de variante,
      "id": (string) identifiant API de la variante,
      "first_step_ids": (tableau de chaînes) identifiants API pour les premières étapes de la variante,
      "first_step_id": (string) API identifiant de première étape dans la variante (obsolète en Novembre 2017, seulement inclus si la variante n'a qu'une première étape)
    },
    . . (plus de variations)
  ],
  "tags": (tableau de chaînes) noms de balises associés à la Canvas,
  "étapes": [
    {
      "name": (string) nom de l'étape,
      "id": (string) identifiant API de l'étape
      "next_step_ids": (tableau de chaînes) identifiants API des étapes suivantes,
      "canaux": (tableau de chaînes) canaux utilisés à l'étape
      "messages": {
          "message_variation_id": (string) { // <=Ceci est l'id actuel
              "channel": (string) type de canal du message (par exemple. "email"),
              ... champs spécifiques au canal pour ce message, voir les détails de la campagne Réponse de l'API de l'Endpoint pour les réponses de message d'exemple ...
          }
      } }
    },
    ... (plus d'étapes)
  ],
  "message": (obligatoire, chaîne) le statut de l'exportation, retourne 'success' une fois terminé sans erreurs
}
```
{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et API, visitez notre article de dépannage [ici]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
