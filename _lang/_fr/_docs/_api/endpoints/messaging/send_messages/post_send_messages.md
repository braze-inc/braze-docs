---
nav_title: "POST: Envoyer des messages immédiatement via l'API uniquement"
article_title: "POST: Envoyer des messages immédiatement via l'API uniquement"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: Référence
description: "Cet article décrit les détails sur le point d'envoi de messages immédiatement Braze terminal."
---

{% api %}
# Envoyer des messages immédiatement via l'API uniquement
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/fr/messages/send
{% endapimethod %}

Ce point de terminaison vous permet d'envoyer vos messages en utilisant notre API. Assurez-vous d'inclure des objets de messagerie dans votre corps pour compléter vos demandes.

Le point de terminaison d'envoi vous permet d'envoyer immédiatement des messages ad hoc à des utilisateurs désignés. Si vous visez un segment, un enregistrement de votre requête sera stocké dans la [Console développeur](https://dashboard.braze.com/app_settings/developer_console/activitylog/).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#946cb701-96e3-48d7-868c-f079785b6d24 {% endapiref %}

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
   // Inclure les deux enverra aux utilisateurs fournis s'ils sont dans le segment
   "broadcast": (optionnel, boolean) voir broadcast -- false par défaut sur 8/31/17, doit être défini à true si aucun alias ou id external_user_ids n'est fourni,
   "external_user_ids": (optionnel, tableau de chaînes) voir l'identifiant utilisateur externe,
   "user_aliases": (optionnel, tableau d'alias de l'utilisateur) voir l'alias de l'utilisateur,
   "segment_id": (optionnel, chaîne) voir l'identifiant du segment,
   "public": (optionnel, objet public connecté) voir public connecté,
   "campaign_id": (optionnel*, chaîne) *requis si vous souhaitez suivre les statistiques de campagne (e. . envois, clics, rebondissements, etc.). voir l'identifiant de la campagne,
   "send_id": (optionnel, chaîne) voir l'identifiant d'envoi,
   "override_frequency_capping": (optionnel, bool) ignorer frequency_capping pour les campagnes, par défaut à false,
   "recipient_subscription_state": (optionnel, string) utilisez ceci pour envoyer des messages uniquement aux utilisateurs qui ont choisi ('opted_in'), seuls les utilisateurs qui se sont abonnés ou qui sont inscrits à ('abonné') ou à tous les utilisateurs, y compris les utilisateurs désabonnés ('tous'), ces derniers étant utiles pour les messages électroniques transactionnels. Par défaut, 'subscribed',
   "messages": {
     "apple_push": (optionnel, pomme push object),
     "android_push": (optionnel, android push object),
     "windows_phone8_push": (optionnel, windows phone 8 push object),
     "windows_universal_push": (optionnel, windows universal push object),
     "kindle_push" : (optionnel, kindle/fireOS push object),
     "web_push": (optionnel, objet push web),
     "email": (optionnel, objet email),
     "webhook": (optionnel, objet webhook),
     "content_card": (optionnel, objet de carte de contenu),
     "sms": (optionnel, objet SMS)
   }
}
```

## Paramètres de la requête

| Paramètre                         | Requis     | Type de données                           | Libellé                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------------------------- | ---------- | ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Diffusion`                       | Optionnel  | Boolean                                   | Voir la diffusion [de]({{site.baseurl}}/api/parameters/#broadcast). Ce paramètre par défaut est false (à partir du 31 août 2017). <br><br> Si `destinataires` est omis, `envoyer à tous` doit être défini à vrai. Cependant, faites preuve de prudence lorsque vous définissez `broadcast: true`, comme paramétrage involontaire de ce drapeau peut vous faire envoyer vos messages à un public plus grand que prévu. |
| `ID_utilisateur_externe`          | Optionnel  | Tableau de chaînes                        | Voir [ID utilisateur externe]({{site.baseurl}}/api/parameters/#external-user-id).                                                                                                                                                                                                                                                                                                                                                 |
| `Alias utilisateur`               | Optionnel  | Tableau des objets alias de l'utilisateur | Voir [l'objet alias utilisateur]({{site.baseurl}}/api/objects_filters/user_alias_object/).                                                                                                                                                                                                                                                                                                                                        |
| `identifiant_segment`             | Optionnel  | Chaîne de caractères                      | See [segment identifier]({{site.baseurl}}/api/identifier_types/).                                                                                                                                                                                                                                                                                                                                                                 |
| `public`                          | Optionnel  | Objet public connecté                     | Voir [audience connectée]({{site.baseurl}}/api/objects_filters/connected_audience/).                                                                                                                                                                                                                                                                                                                                              |
| `campaign_id`                     | Optionnel* | Chaîne de caractères                      | Voir [l'identifiant de campagne]({{site.baseurl}}/api/identifier_types/) pour plus d'informations. <br><br>*Requis si vous souhaitez suivre les statistiques de campagne (par exemple, envois, clics, bounces, etc.) sur le tableau de bord de Braze.                                                                                                                                                                 |
| `id_expéditeur`                   | Optionnel  | Chaîne de caractères                      | Voir [l'identifiant d'envoi]({{site.baseurl}}/api/identifier_types/)                                                                                                                                                                                                                                                                                                                                                              |
| `override_fréquence_plafonnement` | Optionnel  | Boolean                                   | Ignorer fréquence_plafonnement pour les campagnes, la valeur par défaut est false.                                                                                                                                                                                                                                                                                                                                                |
| `État de l'abonnement`            | Optionnel  | Chaîne de caractères                      | Utilisez ceci pour envoyer des messages aux seuls utilisateurs qui ont opté pour (`opted_in`), seuls les utilisateurs qui se sont inscrits ou qui sont inscrits (`inscrits`) ou à tous les utilisateurs, y compris les utilisateurs désabonnés (`tous`). <br><br>L'utilisation de `tous les utilisateurs` est utile pour les messages électroniques transactionnels. Par défaut, `abonné`.                            |
| `Messages`                        | Optionnel  | Objets de messagerie                      | Voir les [objets de messagerie disponibles](#available-messaging-objects), ci-dessous.                                                                                                                                                                                                                                                                                                                                            |
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
curl --location --request POST 'https://rest.iad-01.braze. om/messages/send' \
--data-raw '{
  "broadcast": "false",
  "external_user_ids": "external_user_identifiers",
  "user_aliases": {
    "alias_name": "exemple_name",
    "alias_label": "example_label"
  },
  "segment_id": "segment_identifier",
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
  "override_frequency_capping": "false",
  "recipient_subscription_state": "all",
  "messages": {
    "android_push": "(optionnel, Android Push Object)",
    "apple_push": "(optionnel, Apple Push Object)",
    "content_card": "(optionnel, objet de carte de contenu)",
    "email": "(optionnel, Email Object)",
    "kindle_push": "(optionnel, objet Push Kindle/FireOS)",
    "web_push": "(optionnel, Web Push Object)",
    "windows_phone8_push": "(optionnel, Objet Push de Windows Phone 8)",
    "windows_universal_push": "(optionnel, Windows Universal Push Object)"
  }
}'''
```

## Détails de la réponse

Les réponses aux points de terminaison du message incluront le message `dispatch_id` pour être référencé à l'envoi du message. Le `dispatch_id` est l'id de l'envoi de message (id unique pour chaque « transmission» envoyée depuis la plate-forme Braze). Pour plus d'informations sur `dispatch_id` , consultez notre [documentation]({{site.baseurl}}/help/help_articles/data/dispatch_id/).

{% endapi %}

