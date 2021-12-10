---
nav_title: "GET: Analyses de campagne"
article_title: "GET: Analyses de campagne"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: Référence
description: "Cet article décrit les détails de l'extrémité Analytique Get Campaign Analytics."
---

{% api %}
# Terminal d'analyse de la campagne
{% apimethod get %}
/fr/campaigns/data_series
{% endapimethod %}

Ce point de terminaison vous permet de récupérer une série quotidienne de statistiques différentes pour une campagne au fil du temps. Les données retournées incluent le nombre de messages envoyés, ouverts, cliqués, convertis, etc., répartis par canal de message.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c07b5ebd-0246-471e-b154-416d63ae28a1 {% endapiref %}

## Paramètres de la requête

| Paramètre        | Requis    | Type de données                                                                | Libellé                                                                                                                                                                                                                                                                                                                                                   |
| ---------------- | --------- | ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `campaign_id`    | Requis    | Chaîne de caractères                                                           | Voir [l'identifiant API de la campagne]({{site.baseurl}}/api/identifier_types/).<br><br> La `campaign_id` pour les campagnes API peut être trouvée sur la **Console développeur** et la **page de détails de campagne** de votre tableau de bord ; ou vous pouvez utiliser le [Liste de Campagne point d'extrémité](#campaign-list-endpoint). |
| `Longueur`       | Requis    | Nombre entier                                                                  | Nombre maximum de jours avant `ending_at` pour inclure dans la série retournée. Doit être compris entre 1 et 100 (inclus).                                                                                                                                                                                                                                |
| `finalisation_à` | Optionnel | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) chaîne) | Date à laquelle la série de données doit se terminer. Par défaut, l'heure de la requête.                                                                                                                                                                                                                                                                  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/campaigns/data_series?campaign_id={{campaign_identifier}}&length=7&ending_at=2020-06-28T23:59:59-5:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Réponse

### Réponse multi-canal

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
                      "revenue": 0,
                      "unique_recipients": 1,
                      "conversions": 0,
                      "conversions_by_send_time": 0,
                      "conversions1": 0,
                      "conversions1_by_send_time": 0,
                      "conversions2": 0,
                      "conversions2_by_send_time": 0,
                      "conversions3": 0,
                      "conversions3_by_send_time": 0,
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

### Réponse multivariée

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "data" : [
        {
            "time" : (string) date en ISO 8601 date,
            "conversions" : (int),
            "recettes": (flottant),
            "conversions_by_send_time": (int),
            "messages" : {
               "trigger_in_app_message": [{
                    "variation_name": (optionnel, string),
                    "impressions": (int),
                    "clics": (int),
                    "first_button_clicks": (int),
                    "second_button_clicks": (int),
                    "revenus": (optionnel, float),,
                    "unique_recipients": (int),
                    "conversions": (optionnel, int),
                    "conversions_by_send_time": (optionnel, int),
                    "conversions1": (optionnel, int),
                    "conversions1_by_send_time": (optionnel, int),
                    "conversions2": (optionnel, int),
                    "conversions2_by_send_time": (optionnel, int),
                    "conversions3": (optionnel, int),
                    "conversions3_by_send_time": (facultatif, int)
                }, {
                    "variation_name": (optionnel, string),
                    "impressions": (int),
                    "clics": (int),
                    "first_button_clicks": (int),
                    "second_button_clicks": (int),
                    "recettes": (optionnel, float),,
                    "unique_recipients": (int),
                    "conversions": (optionnel, int),
                    "conversions_by_send_time": (optionnel, int),
                    "conversions1": (optionnel, int),
                    "conversions1_by_send_time": (facultatif, int),
                    "conversions2": (optionnel, int),
                    "conversions2_by_send_time": (facultatif, int),
                    "conversions3": (optionnel, int).
                    "conversions3_by_send_time": (optionnel, int)
                }, {
                    "variation_name": (optionnel, chaîne),
                    "revenus": (optionnel, flottant),
                    "unique_destinataires": (int),
                    "conversions": (optionnel, int),
                    "conversions_by_send_time": (optionnel, int),
                    "conversions1": (optionnel, int),
                    "conversions1_by_send_time": (optionnel, int),
                    "conversions2": (optionnel, int),
                    "conversions2_by_send_time": (optionnel, int),
                    "conversions3": (optionnel, int),
                    "conversions3_by_send_time": (optionnel, int),
                    "inscrit": (optionnel, int)
                }]
            },
            "conversions_by_send_time": (optionnel, int),
            "conversions1_by_send_time": (optionnel, int),
            "conversions2_by_send_time": (optionnel, int),
            "conversions3_by_send_time": (optionnel, int),
            "conversions": (optionnel, int,
            "conversions1": (optionnel, int),
            "conversions2": (optionnel, int),
            "conversions3": (optionnel, int),
            "unique_destinataires": (int),
            "revenus": (optionnel, flottez)
         }],
...
}
```

Les types de messages possibles sont `email`, `in_app_message`, `webhook`, `android_push`, `apple_push`, `kindle_push`, `web_push`, `windows_phone8_push`et `windows_universal_push`. Tous les types de messages push auront les mêmes statistiques affichées pour `android_push` ci-dessus.

{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et API, visitez notre article de dépannage [ici]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
