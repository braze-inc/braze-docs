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

Cet endpoint vous permet de récupérer une série quotidienne de diverses statistiques pour une campagne au fil du temps. Les données renvoyées comprennent le nombre de messages envoyés, ouverts, cliqués ou convertis par canal de messagerie.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c07b5ebd-0246-471e-b154-416d63ae28a1 {% endapiref %}

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | -------- | --------- | ----------- |
| `campaign_id` | Requis | Chaîne de caractères | Voir [Identifiant API de campagne]({{site.baseurl}}/api/identifier_types/).<br><br> Le `campaign_id` pour les campagnes API se trouvent sur la page **Developer Console (Console du développeur)** et la page **Campaign Details (Informations relatives à la campagne)** dans votre tableau de bord, sinon vous pouvez utiliser l’[endpoint Liste de campagnes](#campaign-list-endpoint). |
| `length` | Requis | Entier | Nombre maximum de jours avant `ending_at` à inclure dans la série renvoyée. Doit être compris entre 1 et 100 (inclus). |
| `ending_at` | Facultatif | Datetime <br>(chaîne de caractères [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Date à laquelle la série de données doit se terminer. Par défaut, l’heure de la demande. |
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
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "data" : [
        {
            "time" : (string) date as ISO 8601 date,
            "messages" : {
                "ios_push" : [
                    {
                      "variation_name": "iOS_Push",
                      "sent" : (int),
                      "direct_opens" : (int),
                      "total_opens" : (int),
                      "bounces" : (int),
                      "body_clicks" : (int)
                      "revenue": (optional, float),
                      "unique_recipients": (int),
                      "conversions": (int),
                      "conversions_by_send_time": (optional, int),
                      "conversions1": (optional, int),
                      "conversions1_by_send_time": (optional, int),
                      "conversions2": (optional, int),
                      "conversions2_by_send_time": (optional, int),
                      "conversions3": (optional, int),
                      "conversions3_by_send_time": (optional, int),
                      "carousel_slide_[NUM]_[TITLE]_click": (optional, int),
                      "notif_button_[NUM]_[TITLE]_click": (optional, int)
                    }
                ],
                "android_push" : [
                    {
                      "sent" : (int),
                      "direct_opens" : (int),
                      "total_opens" : (int),
                      "bounces" : (int),
                      "body_clicks" : (int)
                    }
                ],
                "webhook": [
                    {
                      "sent": (int),
                      "errors": (int)
                    }
                ],
                "email" : [
                    {
                      "sent": (int),
                      "opens": (int),
                      "unique_opens": (int),
                      "clicks": (int),
                      "unique_clicks": (int),
                      "unsubscribes": (int),
                      "bounces": (int),
                      "delivered": (int),
                      "reported_spam": (int)
                    }
                ],
                "sms" : [
                  {
                    "sent": (int),
                    "sent_to_carrier" : (int),
                    "delivered": (int),
                    "rejected": (int),
                    "delivery_failed": (int),
                    "opt_out" : (int),
                    "help" : (int)
                  }
                ],
                "content_cards" : [
                  { 
                    "variation_name": "Variant 1", 
                    "variation_api_id": (string), 
                    "sent": (int), 
                    "total_impressions": (int), 
                    "unique_impressions": (int),
                    "total_clicks": (int), 
                    "unique_clicks": (int), 
                    "total_dismissals": (int), 
                    "unique_dismissals": (int), 
                    "revenue": (optional, float), 
                    "unique_recipients": (int), 
                    "conversions": (int), 
                    "conversions_by_send_time": (optional, int), 
                    "conversions1": (optional, int), 
                    "conversions1_by_send_time": (optional, int), 
                    "conversions2": (optional, int), 
                    "conversions2_by_send_time": (optional, int), 
                    "conversions3": (optional, int), 
                    "conversions3_by_send_time": (optional, int) 
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
            "time" : (string) date as ISO 8601 date,
            "conversions" : (int),
            "revenue": (float),
            "conversions_by_send_time": (int),
            "messages" : {
               "trigger_in_app_message": [{
      				"variation_name": (optional, string),
      				"impressions": (int),
      				"clicks": (int),
      				"first_button_clicks": (int),
      				"second_button_clicks": (int),
      				"revenue": (optional, float),,
      				"unique_recipients": (int),
      				"conversions": (optional, int),
      				"conversions_by_send_time": (optional, int),
      				"conversions1": (optional, int),
      				"conversions1_by_send_time": (optional, int),
      				"conversions2": (optional, int),
      				"conversions2_by_send_time": (optional, int),
      				"conversions3": (optional, int),
      				"conversions3_by_send_time": (optional, int)
      			}, {
      				"variation_name": (optional, string),
      				"impressions": (int),
      				"clicks": (int),
      				"first_button_clicks": (int),
      				"second_button_clicks": (int),
      				"revenue": (optional, float),,
      				"unique_recipients": (int),
      				"conversions": (optional, int),
      				"conversions_by_send_time": (optional, int),
      				"conversions1": (optional, int),
      				"conversions1_by_send_time": (optional, int),
      				"conversions2": (optional, int),
      				"conversions2_by_send_time": (optional, int),
      				"conversions3": (optional, int).
      				"conversions3_by_send_time": (optional, int)
      			}, {
      				"variation_name": (optional, string),
      				"revenue": (optional, float),,
      				"unique_recipients": (int),
      				"conversions": (optional, int),
      				"conversions_by_send_time": (optional, int),
      				"conversions1": (optional, int),
      				"conversions1_by_send_time": (optional, int),
      				"conversions2": (optional, int),
      				"conversions2_by_send_time": (optional, int),
      				"conversions3": (optional, int),
      				"conversions3_by_send_time": (optional, int),
      				"enrolled": (optional, int)
      			}]
      		},
      		"conversions_by_send_time": (optional, int),
      		"conversions1_by_send_time": (optional, int),
      		"conversions2_by_send_time": (optional, int),
      		"conversions3_by_send_time": (optional, int),
      		"conversions": (optional, int,
      		"conversions1": (optional, int),
      		"conversions2": (optional, int),
      		"conversions3": (optional, int),
      		"unique_recipients": (int),
      		"revenue": (optional, float)
         }],
         ...
}
```

Les types de messages possibles sont `email`, `in_app_message`, `webhook`, `android_push`, `ios_push`, `kindle_push`, `web_push`, `windows_phone8_push`, et `windows_universal_push`. Tous les types de messages des notifications push auront les mêmes statistiques que celles d’`android_push`.

{% alert tip %}
Pour obtenir de l’aide sur les exportations CSV et de l’API, consultez la section [Résolution des problèmes d’exportation]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
