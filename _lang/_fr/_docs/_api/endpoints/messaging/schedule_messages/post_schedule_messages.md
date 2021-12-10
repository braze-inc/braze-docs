---
nav_title: "POST: Programmer des messages"
article_title: "POST: Programmer des messages"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: Référence
description: "Cet article décrit les détails du point de terminaison Schedule Messages Braze."
---

{% api %}
# Créer des messages planifiés
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/fr/messages/schedule/create
{% endapimethod %}

Utilisez ce point de terminaison pour envoyer des messages directement depuis l'API.

Le point de terminaison de l'horaire de création vous permet de planifier une campagne, Canvas, ou tout autre message à envoyer à une heure désignée (jusqu'à 90 jours dans le futur) et vous fournit un identifiant pour référencer ce message pour les mises à jour. Si vous visez un segment, un enregistrement de votre demande sera stocké dans la [Console développeur](https://dashboard.braze.com/app_settings/developer_console/activitylog/) après l'envoi de tous les messages programmés.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#25272fb8-bc39-41df-9a41-07ecfd76cb1d {% endapiref %}

## Corps de la requête

```
Type de contenu : application/json
Autorisation : Bearer YOUR-REST-API-KEY
```

```json
{
  // Vous devrez inclure au moins un de 'segment_id', 'external_user_ids', et 'audience'
  // Inclure 'segment_id' enverra aux membres de ce segment
  // Incluant 'external_user_ids' et/ou 'user_aliases' enverra à ces utilisateurs
  // Inclure à la fois un segment et les utilisateurs enverront aux utilisateurs fournis s'ils sont dans le segment
  "broadcast": (optionnel, boolean) see broadcast -- false par défaut sur 8/31/17, doit être défini à true si les utilisateurs ne sont pas spécifiés,
  "external_user_ids": (optionnel, tableau de chaînes) voir l'identifiant utilisateur externe,
  "user_aliases": (optionnel, tableau d'alias de l'utilisateur) voir l'alias de l'utilisateur,
  "public": (optionnel, objet public connecté) voir public connecté,
  "segment_id": (optionnel, chaîne) voir l'identifiant du segment,
  "campaign_id": (optionnel, chaîne) voir l'identifiant de la campagne,
  "send_id": (optionnel, chaîne) voir l'identifiant d'envoi,
  "override_messaging_limits": (optionnel, bool) ignorer les règles de plafonnement de fréquence, la valeur par défaut est false,
  "recipient_subscription_state": (optionnel, string) utilisez ceci pour envoyer des messages uniquement aux utilisateurs qui ont choisi ('opted_in'), seuls les utilisateurs qui se sont abonnés ou qui sont inscrits à ('abonné') ou à tous les utilisateurs, y compris les utilisateurs désabonnés ('tous'), ces derniers étant utiles pour les messages électroniques transactionnels. Par défaut, 'subscribed',
  "schedule": { 
    "time": (requis, datetime en tant que chaîne ISO 8601) heure pour envoyer le message, (jusqu'à 90 jours dans le futur),
    "in_local_time": (optionnel, bool),
    "at_optimal_time": (optionnel, bool),
  },
  "messages": {
    "apple_push": (optionnel, pomme push object),
    "android_push": (optionnel, android push object),
    "windows_push": (optionnel, windows Phone 8 push object),
    "windows8_push" : (optionnel, windows Universal push object),
    "kindle_push": (optionnel, kindle/fireOS push object),
    "web_push": (optionnel, objet push web),
    "email": (optionnel, objet email),
    "webhook": (optionnel, objet webhook),
    "content_card": (optionnel, objet de carte de contenu),
    "sms": (optionnel, objet SMS)
  }
}
```

## Paramètres de la requête

| Paramètre                             | Requis    | Type de données                           | Libellé                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------- | --------- | ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Diffusion`                           | Optionnel | Boolean                                   | Voir la diffusion [de]({{site.baseurl}}/api/parameters/#broadcast). Ce paramètre par défaut est false (à partir du 31 août 2017). <br><br> Si `destinataires` est omis, `envoyer à tous` doit être défini à vrai. Cependant, faites preuve de prudence lorsque vous définissez `broadcast: true`, comme paramétrage involontaire de ce drapeau peut vous faire envoyer votre message à un public plus grand que prévu. |
| `ID_utilisateur_externe`              | Optionnel | Tableau de chaînes                        | Voir [l'identifiant utilisateur externe]({{site.baseurl}}/api/parameters/#external-user-id).                                                                                                                                                                                                                                                                                                                                       |
| `Alias utilisateur`                   | Optionnel | Tableau des objets alias de l'utilisateur | Voir [l'objet alias utilisateur]({{site.baseurl}}/api/objects_filters/user_alias_object/).                                                                                                                                                                                                                                                                                                                                         |
| `public`                              | Optionnel | Objet public connecté                     | Voir [audience connectée]({{site.baseurl}}/api/objects_filters/connected_audience/).                                                                                                                                                                                                                                                                                                                                               |
| `identifiant_segment`                 | Optionnel | Chaîne de caractères                      | See [segment identifier]({{site.baseurl}}/api/identifier_types/).                                                                                                                                                                                                                                                                                                                                                                  |
| `campaign_id`                         | Optionnel | Chaîne de caractères                      | Voir [l'identifiant de la campagne]({{site.baseurl}}/api/identifier_types/).                                                                                                                                                                                                                                                                                                                                                       |
| `Destinataires`                       | Optionnel | Tableau des objets destinataires          | Voir l'objet [destinataires]({{site.baseurl}}/api/objects_filters/recipient_object/).                                                                                                                                                                                                                                                                                                                                              |
| `id_expéditeur`                       | Optionnel | Chaîne de caractères                      | Voir [l'identifiant d'envoi]({{site.baseurl}}/api/identifier_types/).                                                                                                                                                                                                                                                                                                                                                              |
| `outrepasser les limites de messages` | Optionnel | Boolean                                   | Ignorer les limites de taux globales pour les campagnes, la valeur par défaut est false                                                                                                                                                                                                                                                                                                                                            |
| `État de l'abonnement`                | Optionnel | Chaîne de caractères                      | Utilisez ceci pour envoyer des messages aux seuls utilisateurs qui ont opté pour (`opted_in`), seuls les utilisateurs qui se sont inscrits ou qui sont inscrits (`inscrits`) ou à tous les utilisateurs, y compris les utilisateurs désabonnés (`tous`). <br><br>L'utilisation de `tous les utilisateurs` est utile pour les messages électroniques transactionnels. Par défaut, `abonné`.                             |
| `Horaire`                             | Requis    | Planifier l'objet                         | Voir [l'objet de planification]({{site.baseurl}}/api/objects_filters/schedule_object/)                                                                                                                                                                                                                                                                                                                                             |
| `Messages`                            | Optionnel | Objet de messagerie                       | Voir les [objets de messagerie disponibles](#available-messaging-objects), ci-dessous.                                                                                                                                                                                                                                                                                                                                             |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### Objets de messagerie disponibles {#available-messaging-objects}

Vous pouvez utiliser ces objets dans le corps de la [requête](#request-body) ci-dessus.
- [Objets Android]({{site.baseurl}}/api/objects_filters/android_objects/)
- [Objets Apple]({{site.baseurl}}/api/objects_filters/apple_objects/)
- [Objet Cartes de Contenu]({{site.baseurl}}/api/objects_filters/content_cards_object/)
- [Objet Email]({{site.baseurl}}/api/objects_filters/email_object/)
- [Objet Kindle ou FireOS]({{site.baseurl}}/api/objects_filters/kindle_and_fireos_object/)
- [Objet SMS]({{site.baseurl}}/api/objects_filters/sms_object/)
- [Objets Web]({{site.baseurl}}/api/objects_filters/web_objects/)
- [Objet Webhook]({{site.baseurl}}/api/objects_filters/webhook_object/)
- [Objets Windows]({{site.baseurl}}/api/objects_filters/windows_objects/)

## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze. om/messages/schedule/create' \
--data-raw '{
    "broadcast": "false",
    "external_user_ids": "external_user_identifiers",
    "user_aliases": {
      "alias_name" : "example_name",
      "alias_label" : "example_label"
    },
    "segment_id": "segment_identifiers",
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
      }
    ]
  },
    "campaign_id": "campaign_identifier",
    "send_id": "send_identifier",
    "override_messaging_limits": false,
  "recipient_subscription_state": "subscribed",
  "schedule": {
    "time": "",
    "in_local_time": true,
    "at_optimal_time": vrai
  },
  "messages": {
    "apple_push": (optionnel, Apple Push Object),
    "android_push": (optionnel, objet push Android),
    "windows_push": (optionnel, Objet Push de Windows Phone 8),
    "windows8_push" : (optionnel, Objet Push Universal de Windows),
    "kindle_push" : (optionnel, objet Push Kindle/FireOS),
    "web_push": (optionnel, objet Push Web),
    "email": (optionnel, Objet e-mail)
    "webhook": (optionnel, objet Webhook)
    "content_card": (optionnel, Objet de carte de contenu)
  }
}'\'''
```


{% endapi %}

