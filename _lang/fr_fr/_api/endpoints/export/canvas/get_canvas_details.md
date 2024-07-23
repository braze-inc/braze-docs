---
nav_title: "GET : Exporter les détails du canevas"
article_title: "GET : Exporter les détails du canevas"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze les détails du Canvas."

---
{% api %}
# Exporter les détails du Canvas
{% apimethod get %}
/canvas/details
{% endapimethod %}

> Utilisez cet endpoint pour exporter des métadonnées sur un Canvas, telles que le nom, l’heure de création, l’état actuel, etc.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5188873c-13a3-4aaf-a54b-9fa1daeac5f8 {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `canvas.details`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | -------- | --------- | ----------- |
| `canvas_id` | Obligatoire | Chaîne | Voir [Identifiant d’API Canvas]({{site.baseurl}}/api/identifier_types/) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande

{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/details?canvas_id={{canvas_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Réponse

{% alert note %}
Toutes les étapes Canvas ont un champ `next_paths` qui est un tableau de données `{name, next_step_id}`. Pour les étapes complètes et les étapes de message, le champ `next_step_ids` sera présent mais ne contiendra pas de données pour les autres étapes de Canvas Flow.
{% endalert %}

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "created_at": (string) the date created as ISO 8601 date,
  "updated_at": (string) the date updated as ISO 8601 date,
  "name": (string) the Canvas name,
  "description": (string) the Canvas description,
  "archived": (boolean) whether this Canvas is archived,
  "draft": (boolean) whether this Canvas is a draft,
  "schedule_type": (string) the type of scheduling action,
  "first_entry": (string) the date of first entry as ISO 8601 date,
  "last_entry": (string) the date of last entry as ISO 8601 date,
  "channels": (array of strings) step channels used with Canvas,
  "variants": [
    {
      "name": (string) the name of variant,
      "id": (string) the API identifier of the variant,
      "first_step_ids": (array of strings) the API identifiers for first steps in variant,
      "first_step_id": (string) the API identifier of first step in variant (deprecated in November 2017, only included if the variant has only one first step)
    },
    ... (more variations)
  ],
  "tags": (array of strings) the tag names associated with the Canvas,
  "teams" : (array) the names of the Teams associated with the Canvas,
  "steps": [
    {
      "name": (string) the name of step,
      "type" (string) the type of Canvas component,
      "id": (string) the API identifier of the step,
      "next_step_ids": (array of strings) IDs for next steps that are full steps or Message steps,
      "next_paths": { (array of objects)
      // for Decision Splits, this property should evaluate to "Yes" or "No"
      // for Audience Path and Action Paths, this property should evaluate to the group name
      // for Experiment Paths, this property should evaluate to the path name
      // for other steps, this property should evaluate to "null"
        "name": (string) name the name of step,
        "next_step_id": (string) IDs for next steps that are full steps or Message steps,
        }
      "channels": (array of strings) the channels used in step,
      "messages": {
          "message_variation_id": (string) {  // <=This is the actual id
              "channel": (string) the channel type of the message (for example, "email"),
              // channel-specific fields for this message, see Campaign Details endpoint API Response for example message responses
          }
      }
    },
    ... (more steps)
  ],
  "message": (required, string) the status of the export, returns 'success' when completed without errors
}
```

{% alert tip %}
Pour obtenir de l’aide sur les exportations CSV et de l’API, consultez la section Résolution des problèmes d’exportation[]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
