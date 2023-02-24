---
nav_title: "GET : Analyse de campagne"
article_title: "GET : Analyse de campagne"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Obtenir les analyses de campagne."

---
{% api %}
# Endpoint Analyse de campagne
{% apimethod get %}
/campaigns/data_series
{% endapimethod %}

Utilisez cet endpoint pour récupérer une série quotidienne de diverses statistiques pour une campagne au fil du temps. Les données renvoyées comprennent le nombre de messages envoyés, ouverts, cliqués ou convertis par canal de messagerie.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c07b5ebd-0246-471e-b154-416d63ae28a1 {% endapiref %}

## Limites de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | -------- | --------- | ----------- |
| `campaign_id` | Requis | String | Voir [Identifiant API de campagne]({{site.baseurl}}/api/identifier_types/).<br><br> Le `campaign_id` pour les campagnes API se trouvent sur la page **Developer Console (Console du développeur)** et la page **Campaign Details (Informations relatives à la campagne)** dans votre tableau de bord, sinon vous pouvez utiliser l’[endpoint Campaign List (Liste de campagnes)](#campaign-list-endpoint). .|
| `length` | Requis | Integer | Nombre maximum de jours avant `ending_at` à inclure dans la série renvoyée. Doit être compris entre 1 et 100 (inclus). |
| `ending_at` | Facultatif | DateTime <br>(chaîne de caractères [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Date à laquelle la série de données doit se terminer. Par défaut, l’heure de la demande. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande 
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/campaigns/data_series?campaign_id={{campaign_identifier}}&length=7&ending_at=2020-06-28T23:59:59-5:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Réponses

### Réponse multicanaux

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) le statut de l’exportation, renvoie « réussite » lorsqu’elle s’achève sans erreur,
    "data" : [
        {
            "time" : (string) la date en tant que date ISO 8601,
            "messages" : {
                "ios_push" : [
                    {
                      "variation_name": (string) le nom du message dans le tableau de bord (par ex., « iOS_Push »),,
                      "sent" : (int) le nombre d’envois,
                      "direct_opens" : (int) le nombre d’ouvertures directes,
                      "total_opens" : (int) le nombre total d’ouvertures,
                      "bounces" : (int) le nombre de rebonds,
                      "body_clicks" : (int) le nombre de clics sur le corps,
                      "revenue": (float) le nombre de dollars de revenus (USD),
                      "unique_recipients": (int) le nombre de destinataires uniques,
                      "conversions": (int) le nombre de conversions,
                      "conversions_by_send_time": (int) le nombre de conversions attribuées à la date à laquelle la campagne a été envoyée,
                      "conversions1": (optional, int) le décompte de conversions pour le deuxième événement de conversion,
                      "conversions1_by_send_time": (optional, int) le décompte de conversions pour le deuxième événement de conversion attribué à la date à laquelle la campagne a été envoyée,
                      "conversions2": (optional, int) le décompte de conversions pour le troisième événement de conversion,
                      "conversions2_by_send_time": (optional, int) le décompte de conversions pour le troisième événement de conversion attribué à la date à laquelle la campagne a été envoyée,
                      "conversions3": (optional, int) le décompte de conversions pour le quatrième événement de conversion,
                      "conversions3_by_send_time": (optional, int) le décompte de conversions pour le quatrième événement de conversion attribué à la date à laquelle la campagne a été envoyée
                      "carousel_slide_[NUM]_[TITLE]_click": (optional, int) le décompte de clicks de diaporama en carrousel,
                      "notif_button_[NUM]_[TITLE]_click": (optional, int) le décompte de clicks de bouton de notification
                    }
                ],
                "android_push" : [
                    {
                      "sent" : (int) le nombre d’envois,
                      "direct_opens" : (int) le nombre d’ouvertures directes,
                      "total_opens" : (int)le nombre total d’ouvertures,
                      "bounces" : (int) le nombre de rebonds,
                      "body_clicks" : (int) le nombre de clics sur le corps
                    }
                ],
                "webhook": [
                    {
                      "sent": (int) le nombre d’envois,
                      "errors": (int) le nombre d’erreurs
                    }
                ],
                "email" : [
                    {
                      "sent": (int) le nombre d’envois,
                      "opens": (int) le nombre d’ouvertures,
                      "unique_opens": (int) le nombre d’ouvertures uniques,
                      "clicks": (int) le nombre de clics,
                      "unique_clicks": (int) le nombre de clics uniques,
                      "unsubscribes": (int) le nombre de désabonnements,
                      "bounces": (int) le nombre de rebonds,
                      "delivered": (int) le nombre de messages livrés,
                      "reported_spam": (int) le nombre de messages signalés comme courriers indésirables
                    }
                ],
                "sms" : [
                  {
                    "sent": (int) le nombre d’envois,
                    "sent_to_carrier" : (int) le nombre de messages envoyés à l’opérateur,
                    "delivered": (int)le nombre de messages livrés,
                    "rejected": (int) le nombre de messages rejetés,
                    "delivery_failed": (int) le nombre de livraisons qui ont échoué,
                    "clicks": (int) le nombre de clics sur les liens raccourcis,
                    "opt_out" : (int) le nombre de refus,
                    "help" : (int) le nombre de messages d’aide reçus
                  }
                ],
                "content_cards" : [
                  { 
                    "variation_name": (string) le nom de la variation, 
                    "variation_api_id": (string) l’identifiant de la variation API, 
                    "sent": (int) le nombre d’envois, 
                    "total_impressions": (int) le nombre total d’impressions, 
                    "unique_impressions": (int) le nombre total d’impressions uniques,,
                    "total_clicks": (int) le nombre total de clics, 
                    "unique_clicks": (int) le nombre de clics uniques, 
                    "total_dismissals": (int) le nombre total de rejets, 
                    "unique_dismissals": (int) le nombre total de rejets uniques, 
                    "revenue": (float) le nombre de dollars de revenus (USD),
                    "unique_recipients": (int) le nombre de destinataires uniques,
                    "conversions": (int) le nombre de conversions,
                    "conversions_by_send_time": (int) le nombre de conversions attribuées à la date à laquelle la campagne a été envoyée,
                    "conversions1": (optional, int) le décompte de conversions pour le deuxième événement de conversion,
                    "conversions1_by_send_time": (optional, int) le décompte de conversions pour le deuxième événement de conversion attribué à la date à laquelle la campagne a été envoyée,
                    "conversions2": (optional, int) le décompte de conversions pour le troisième événement de conversion,
                    "conversions2_by_send_time": (optional, int) le décompte de conversions pour le troisième événement de conversion attribué à la date à laquelle la campagne a été envoyée,
                    "conversions3": (optional, int) le décompte de conversions pour le quatrième événement de conversion,
                    "conversions3_by_send_time": (optional, int) le décompte de conversions pour le quatrième événement de conversion attribué à la date à laquelle la campagne a été envoyée
                  }
                ]
              },
           "conversions_by_send_time": (optional, int),
           "conversions1_by_send_time": (optional, int),
           "conversions2_by_send_time": (optional, int),
           "conversions3_by_send_time": (optional, int),
           "conversions": (int),
           "conversions1": (optional, int),
           "conversions2": (optional, int),
           "conversions3": (optional, int),
           "unique_recipients": (int),
           "revenue": (optional, float)
        },
        ...
    ],
    ...
}
```

### Réponse multivariées

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "data" : [
        {
            "time" : (string) la date en tant que date ISO 8601,
            "conversions" : (int) le nombre de conversions,
            "revenue": (float) le nombre de dollars de revenus (USD),
            "conversions_by_send_time": (int) le nombre de conversions attribuées à la date à laquelle la campagne a été envoyée,
            "messages" : {
               "trigger_in_app_message": [{
                    "variation_name": (optional, string) le nom de la variation,
                    "impressions": (int) le nombre d’impressions,
                    "clicks": (int) le nombre de clics,
                    "first_button_clicks": (int) le nombre de premiers clics de bouton,
                    "second_button_clicks": (int) le nombre de deuxièmes clics de bouton,
                    "revenue": (float) le nombre de dollars de revenus (USD),
                    "unique_recipients": (int) le nombre de destinataires uniques,
                    "conversions": (int) le nombre de conversions,
                    "conversions_by_send_time": (int) le nombre de conversions attribuées à la date à laquelle la campagne a été envoyée,
                    "conversions1": (optional, int) le décompte de conversions pour le deuxième événement de conversion,
                    "conversions1_by_send_time": (optional, int) le décompte de conversions pour le deuxième événement de conversion attribué à la date à laquelle la campagne a été envoyée,
                    "conversions2": (optional, int) le décompte de conversions pour le troisième événement de conversion,
                    "conversions2_by_send_time": (optional, int) le décompte de conversions pour le troisième événement de conversion attribué à la date à laquelle la campagne a été envoyée,
                    "conversions3": (optional, int) le décompte de conversions pour le quatrième événement de conversion,
                    "conversions3_by_send_time": (optional, int) le décompte de conversions pour le quatrième événement de conversion attribué à la date à laquelle la campagne a été envoyée
      			}, {
      				"variation_name": (optional, string) le nom de la variation,
      				"impressions": (int) le nombre d’impressions,
      				"clicks": (int) le nombre de clics,
      				"first_button_clicks": (int) le nombre de premiers clics de bouton,
      				"second_button_clicks": (int) le nombre de deuxièmes clics de bouton,
                    "revenue": (float) le nombre de dollars de revenus (USD),
                    "unique_recipients": (int) le nombre de destinataires uniques,
                    "conversions": (int) le nombre de conversions,
                    "conversions_by_send_time": (int) le nombre de conversions attribuées à la date à laquelle la campagne a été envoyée,
                    "conversions1": (optional, int) le décompte de conversions pour le deuxième événement de conversion,
                    "conversions1_by_send_time": (optional, int) le décompte de conversions pour le deuxième événement de conversion attribué à la date à laquelle la campagne a été envoyée,
                    "conversions2": (optional, int) le décompte de conversions pour le troisième événement de conversion,
                    "conversions2_by_send_time": (optional, int) le décompte de conversions pour le troisième événement de conversion attribué à la date à laquelle la campagne a été envoyée,
                    "conversions3": (optional, int) le décompte de conversions pour le quatrième événement de conversion,
                    "conversions3_by_send_time": (optional, int) le décompte de conversions pour le quatrième événement de conversion attribué à la date à laquelle la campagne a été envoyée
      			}, {
      				"variation_name": (optional, string) le nom de la variation,
      				"revenue": (float) le nombre de dollars de revenus (USD),
      				"unique_recipients": (int) le nombre de destinataires uniques,
      				"conversions": (int) le nombre de conversions,
                    "conversions_by_send_time": (int) le nombre de conversions attribuées à la date à laquelle la campagne a été envoyée,
                    "conversions1": (optional, int) le décompte de conversions pour le deuxième événement de conversion,
                    "conversions1_by_send_time": (optional, int) le décompte de conversions pour le deuxième événement de conversion attribué à la date à laquelle la campagne a été envoyée,
                    "conversions2": (optional, int) le décompte de conversions pour le troisième événement de conversion,
                    "conversions2_by_send_time": (optional, int) le décompte de conversions pour le troisième événement de conversion attribué à la date à laquelle la campagne a été envoyée,
                    "conversions3": (optional, int) le décompte de conversions pour le quatrième événement de conversion,
                    "conversions3_by_send_time": (optional, int) le décompte de conversions pour le quatrième événement de conversion attribué à la date à laquelle la campagne a été envoyée
      				"enrolled": (optional, int) le décompte d’utilisateurs inscrits
      			}]
      		},
      		"conversions_by_send_time": (optional, int),
      		"conversions1_by_send_time": (optional, int),
      		"conversions2_by_send_time": (optional, int),
      		"conversions3_by_send_time": (optional, int),
      		"conversions": (optional, int),
      		"conversions1": (optional, int),
      		"conversions2": (optional, int),
      		"conversions3": (optional, int),
      		"unique_recipients": (int),
      		"revenue": (optional, float)
         }],
         ...
}
```

Les types de messages possibles sont `email`, `in_app_message`, `webhook`, `android_push`, `ios_push`, `kindle_push`, et `web_push`. Tous les types de messages des notifications push auront les mêmes statistiques que celles d’`android_push`.

{% alert tip %}
Pour obtenir de l’aide sur les exportations CSV et de l’API, consultez la section [Résolution des problèmes d’exportation]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/)..
{% endalert %}

{% endapi %}
