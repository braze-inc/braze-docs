---
nav_title: "POST: Planifier les messages de campagne déclenchés par l'API"
article_title: "POST: Planifier les messages de campagne déclenchés par l'API"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: Référence
description: "Cet article décrit les détails sur le point de terminaison Schedule API-Triggered Campaigns Braze."
---

{% api %}
# Planifier les campagnes déclenchées par l'API
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/fr/campaigns/trigger/schedule/create
{% endapimethod %}

Utilisez ce point de terminaison pour déclencher des campagnes déclenchées par API, qui sont créées sur le tableau de bord et initiées via l'API. Vous pouvez passer `trigger_properties` qui seront tempérés dans le message lui-même.

Ce point de terminaison vous permet d'envoyer des messages de campagne (jusqu'à 90 jours à l'avance) via une livraison déclenchée par API, vous permettant de décider quelle action doit déclencher le message à envoyer. Veuillez noter que pour envoyer des messages avec ce terminal, vous devez avoir un ID de campagne, créé lorsque vous construisez une [Campagne déclenchée par l'API]({{site.baseurl}}/api/api_campaigns/).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#b7e61de7-f2c2-49c9-9e46-b85a0aa01bba {% endapiref %}

## Corps de la requête

```
Type de contenu : application/json
Autorisation : Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (requis, chaîne) voir l'identifiant de la campagne,
  "send_id": (optionnel, chaîne) voir l'identifiant d'envoi,
  // Inclure 'recipients' n'enverra aux identifiants d'utilisateurs fournis que s'ils sont dans le segment de la campagne
  "recipients": (optionnel, tableau d'objet destinataires),
  // pour toutes les clés qui entrent en conflit entre ces propriétés de déclenchement et celles d'un objet destinataire, la valeur de l'objet Destinataires sera utilisée
  "public" : (optionnel, objet public connecté) voir public connecté,
  // Inclure 'audience' n'enverra aux utilisateurs que dans l'auditoire
  // Si 'destinataires' et 'public' ne sont pas fournis et que la diffusion n'est pas réglée sur 'false',
  // le message enverra à tout le segment ciblé par la campagne
  "diffusion": (optionnel, boolean) see broadcast -- false par défaut sur 8/31/17, doit être défini à true si l'objet "destinataires" est omis,
  "trigger_properties": (optionnel, objet) personnalisation des paires clé-valeur pour tous les utilisateurs dans cet envoi ; voir les propriétés du déclencheur,
  "schedule": {
    "time": (requis, datetime au format ISO 8601) heure pour envoyer le message (jusqu'à 90 jours dans le futur),
    "in_local_time": (optionnel, bool),
    "at_optimal_time": (optionnel, bool),
  }
}
```
## Paramètres de la requête

| Paramètre                      | Requis    | Type de données                  | Libellé                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------ | --------- | -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `campaign_id`                  | Requis    | Chaîne de caractères             | Voir l'identifiant de la campagne []({{site.baseurl}}/api/identifier_types/)                                                                                                                                                                                                                                                                                                                                                       |
| `id_expéditeur`                | Optionnel | Chaîne de caractères             | Voir [l'identifiant d'envoi]({{site.baseurl}}/api/identifier_types/).                                                                                                                                                                                                                                                                                                                                                              |
| `Destinataires`                | Optionnel | Tableau des objets destinataires | Voir l'objet [destinataires]({{site.baseurl}}/api/objects_filters/recipient_object/).                                                                                                                                                                                                                                                                                                                                              |
| `public`                       | Optionnel | Objet public connecté            | Voir [audience connectée]({{site.baseurl}}/api/objects_filters/connected_audience/).                                                                                                                                                                                                                                                                                                                                               |
| `Diffusion`                    | Optionnel | Boolean                          | Voir la diffusion [de]({{site.baseurl}}/api/parameters/#broadcast). Ce paramètre par défaut est false (à partir du 31 août 2017). <br><br> Si `destinataires` est omis, `envoyer à tous` doit être défini à vrai. Cependant, faites preuve de prudence lorsque vous définissez `broadcast: true`, comme paramétrage involontaire de ce drapeau peut vous faire envoyer votre message à un public plus grand que prévu. |
| `format@@0 trigger_properties` | Optionnel | Objet                            | Paires clé-valeur de personnalisation pour tous les utilisateurs dans cet envoi. Voir [les propriétés du déclencheur]({{site.baseurl}}/api/objects_filters/trigger_properties_object/).                                                                                                                                                                                                                                            |
| `Horaire`                      | Requis    | Planifier l'objet                | Voir [l'objet de planification]({{site.baseurl}}/api/objects_filters/schedule_object/).                                                                                                                                                                                                                                                                                                                                            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze. om/campaigns/trigger/schedule/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "send_id": "send_identifier",
  "recipients": [{
    "user_alias": "example_alias",
    "external_user_id": "external_user_identifier",
    "trigger_properties": {},
    "canvas_entry_properties": {}
  }],
  "audience": {
    "AND": [
      {
        "custom_attribute": {
          "custom_attribute_name": "eye_color",
          "comparaison": "égal",
          "valeur": "bleu"
        }
      },
      {
        "custom_attribute": {
          "custom_attribute_name": "favorite_foods",
          "comparaison": "includes_value",
          "valeur": "pizza"
        }
      },
      {
        "OU": [
          {
            "custom_attribute": {
              "custom_attribute_name": "last_purchase_time",
              "comparaison": "less_than_x_days_ago",
              "valeur": 2
            }
          },
          {
            "push_subscription_status": {
              "comparison": "is",
              "valeur": "opted_in"
            }
          }
        ]
      },
      {
        "email_subscription_status": {
          "comparison": "is_not",
          "valeur": "abonné"
        }
      },
      {
        "last_used_app": {
          "comparison": "after",
          "valeur": "2019-07-22T13:17:55+0000"
        }

    ]
  },
  "broadcast": false,
  "trigger_properties": {},
  "schedule": {
    "time": "",
    "in_local_time": false,
    "at_optimal_time": false
  }
}
'
```


{% endapi %}
