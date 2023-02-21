---
nav_title: "GET : Informations relatives au Canvas"
article_title: "GET : Informations relatives au Canvas"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Informations relative au Canvas."

---
{% api %}
# Endpoint Informations relatives au Canvas
{% apimethod get %}
/canvas/details
{% endapimethod %}

Utilisez cet endpoint pour exporter des métadonnées sur un Canvas, telles que le nom, l’heure de création, l’état actuel, etc.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5188873c-13a3-4aaf-a54b-9fa1daeac5f8 {% endapiref %}

## Limites de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de demande

| Paramètre   | Requis | Type de données | Description            |
| ----------- | -------- | --------- | ---------------------- |
| `canvas_id` | Requis | String | Voir [Identifiant API Canvas]({{site.baseurl}}/api/identifier_types/) |
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
  "created_at": (string) la date de création en tant que date ISO 8601,
  "updated_at": (string) la date de mise à jour en tant que date ISO 8601,
  "name": (string) le nom du Canvas,
  "description": (string) la description du Canvas,
  "archived": (boolean) si ce Canvas est archivé ou non,
  "draft": (boolean) si ce Canvas est un brouillon ou non,
  "schedule_type": (string) le type d’action de planification,
  "first_entry": (string) la date de la première entrée en tant que date ISO 8601,
  "last_entry": (string) la date de la dernière entrée en tant que date ISO 8601,
  "channels": (array of strings) les canaux d’étape utilisés avec Canvas,
  "variants": [
    {
      "name": (string) le nom de la variante,
      "id": (string) l’identifiant API de la variante,
      "first_step_ids": (array of strings) les identifiants API des premières étapes de la variante,
      "first_step_id": (string) l’identifiant API de la première étape de la variante (dépréciée en novembre 2017, comprise uniquement dans la variante pour une seule première étape)
    },
    ... (plus de variations)
  ],
  "tags": (array of strings) les noms de balise associés au Canvas,
  "steps": [
    {
      "name": (string) le nom de l’étape,
      "type": (string) le type de composant Canvas,
      "id": (string) l’identifiant API de l’étape,
      "next_step_ids": (tableau de chaînes de caractères) ID pour les étapes suivantes qui sont des étapes complètes ou des étapes de message,
      "next_paths": {
      // pour les décisions de séparation, cette propriété doit être évaluée sur « Oui » ou « Non »"
      // pour le parcours d'audience et les parcours d’action, cette propriété doit être évaluée sur le nom du groupe
      // pour les parcours d’expérience, cette propriété doit être évaluée sur le nom du chemin
      // pour d’autres étapes, cette propriété doit être évaluée sur « nul »"
        "name": (string) nommer le nom de l’étape,
        "next_step_id": (tableau de chaînes de caractères) ID pour les étapes suivantes qui sont des étapes complètes ou des étapes de message,
        }
      "channels": (array of strings) les canaux utilisés dans l’étape,
      "messages": {
          "message_variation_id": (string) {  // <=Ceci est l’ID réel
              "channel": (string) le type de canal du message (par ex., « e-mail »),
              // champs spécifiques au canal pour ce message, voir la réponse API de l’endpoint de détails de campagne pour voir des exemples de messages de réponse
          }
      }
    },
    ... (plus d’étapes)
  ],
  "message": (required, string) le statut de l’exportation, renvoie « réussite » lorsqu’elle s’achève sans erreur
}
```

{% alert tip %}
Pour obtenir de l’aide sur les exportations CSV et de l’API, consultez la section [Résolution des problèmes d’exportation]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/)..
{% endalert %}

{% endapi %}
