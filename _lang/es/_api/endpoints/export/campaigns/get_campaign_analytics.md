---
nav_title: "GET: Exportar análisis de campaña"
article_title: "GET: Exportar análisis de campaña"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Exportar análisis de campaña de Braze."

---
{% api %}
# Exportar análisis de campaña
{% apimethod get %}
/campaigns/data_series
{% endapimethod %}

> Utiliza este punto final para recuperar una serie diaria de diversas estadísticas de una campaña a lo largo del tiempo. 

Los datos devueltos incluyen cuántos mensajes se enviaron, se abrieron, se clicaron o se convirtieron por canal de mensajería.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c07b5ebd-0246-471e-b154-416d63ae28a1 {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `campaigns.data_series`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='export campaign analytics' %}

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | -------- | --------- | ----------- |
| `campaign_id` | Obligatoria | Cadena | Ver [identificador API de campaña]({{site.baseurl}}/api/identifier_types/).<br><br> Puedes encontrar la dirección `campaign_id` para las campañas API en la página [Claves API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) y en la página **Detalles de campaña** dentro de tu panel, o puedes utilizar el [punto final Listar campañas]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/). |
| `length` | Obligatoria | Entero | Número máximo de días antes de `ending_at` a incluir en la serie devuelta. Debe estar comprendido entre 1 y 100 (ambos inclusive). |
| `ending_at` | Opcional | Fecha y hora <br>(cadena [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Fecha en la que debe finalizar la serie de datos. De forma predeterminada, la hora de la solicitud. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud 

{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/campaigns/data_series?campaign_id={{campaign_identifier}}&length=7&ending_at=2020-06-28T23:59:59-5:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Respuestas

### Respuesta multicanal

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "data" : [
        {
            "time": (string) the date as ISO 8601 date,
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
            "messages" : {
                "ios_push" : [
                    {
                      "variation_api_id": (string) the variation API identifier,
                      "sent" : (int) the number of sends,
                      "direct_opens" : (int) the number of direct opens,
                      "total_opens" : (int)the number of total opens,
                      "bounces" : (int) the number of bounces,
                      "body_clicks" : (int) the number of body clicks
                    }
                ],
                "android_push" : [
                    {
                      "variation_api_id": (string) the variation API identifier,
                      "sent" : (int) the number of sends,
                      "direct_opens" : (int) the number of direct opens,
                      "total_opens" : (int)the number of total opens,
                      "bounces" : (int) the number of bounces,
                      "body_clicks" : (int) the number of body clicks
                    }
                ],
                "webhook": [
                    {
                      "variation_api_id": (string) the variation API identifier,
                      "sent": (int) the number of sends,
                      "errors": (int) the number of errors
                    }
                ],
                "email" : [
                    {
                      "variation_api_id": (string) the variation API identifier,
                      "sent": (int) the number of sends,
                      "opens": (int) the number of opens,
                      "unique_opens": (int) the number of unique opens,
                      "clicks": (int) the number of clicks,
                      "unique_clicks": (int) the number of unique clicks,
                      "unsubscribes": (int) the number of unsubscribes,
                      "bounces": (int) the number of bounces,
                      "delivered": (int) the number of messages delivered,
                      "reported_spam": (int) the number of messages reported as spam
                    }
                ],
                "sms" : [
                    {
                      "variation_api_id": (string) the variation API identifier,
                      "sent": (int) the number of sends,
                      "sent_to_carrier" : (int) the number of messages sent to the carrier,
                      "delivered": (int) the number of delivered messages,
                      "rejected": (int) the number of rejected messages,
                      "delivery_failed": (int) the number of failed deliveries,
                      "clicks": (int) the number of clicks on shortened links,
                      "opt_out" : (int) the number of opt outs,
                      "help" : (int) the number of help messages received
                  }
                ],
                "whats_app": [
                    {
                      "variation_api_id": (string) the variation API identifier,
                      "sent": (int) the number of sends, 
                      "delivered": (int) the number of delivered messages,
                      "failed": (int) the number of failed deliveries,
                      "read": (int) the number of opened messages
                    },
                ],
                "content_cards" : [
                  { 
                    "variation_api_id": (string) the variation API identifier, 
                    "sent": (int) the number of sends, 
                    "total_clicks": (int) the number of total clicks, 
                    "total_dismissals": (int) the number of total dismissals, 
                    "total_impressions": (int) the number of total impressions, 
                    "unique_clicks": (int) the number of unique clicks, 
                    "unique_dismissals": (int) the number of unique dismissals, 
                    "unique_impressions": (int) the number of unique impressions
                  }
                ],
                ...
            }
        }
    ],
}
```

### Respuesta multivariante

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "data" : [
        {
            "time" : (string) the date as ISO 8601 date,
            "conversions" : (int) the number of conversions,
            "revenue": (float) the number of dollars of revenue (USD),
            "conversions_by_send_time": (int) the number of conversions attributed to the date the campaign was sent,
            "messages" : {
               "trigger_in_app_message": [{
                    "variation_name": (optional, string) the variation name,
                    "impressions": (int) the number of impressions,
                    "clicks": (int) the number of clicks,
                    "first_button_clicks": (int) the number of first button clicks,
                    "second_button_clicks": (int) the number of second button clicks,
                    "revenue": (float) the number of dollars of revenue (USD),
                    "unique_recipients": (int) the number of unique recipients,
                    "conversions": (int) the number of conversions,
                    "conversions_by_send_time": (int) the number of conversions attributed to the date the campaign was sent,
                    "conversions1": (optional, int) the number of conversions for the second conversion event,
                    "conversions1_by_send_time": (optional, int) the number of conversions for the second conversion event attributed to the date the campaign was sent,
                    "conversions2": (optional, int) the number of conversions for the third conversion event,
                    "conversions2_by_send_time": (optional, int) the number of conversions for the third conversion event attributed to the date the campaign was sent,
                    "conversions3": (optional, int) the number of conversions for the fourth conversion event,
                    "conversions3_by_send_time": (optional, int) the number of conversions for the fourth conversion event attributed to the date the campaign was sent
      			}, {
      				"variation_name": (optional, string) the variation name,
      				"impressions": (int) the number of impressions,
      				"clicks": (int) the number of clicks,
      				"first_button_clicks": (int) the number of first button clicks,
      				"second_button_clicks": (int) the number of second button clicks,
                    "revenue": (float) the number of dollars of revenue (USD),
                    "unique_recipients": (int) the number of unique recipients,
                    "conversions": (int) the number of conversions,
                    "conversions_by_send_time": (int) the number of conversions attributed to the date the campaign was sent,
                    "conversions1": (optional, int) the number of conversions for the second conversion event,
                    "conversions1_by_send_time": (optional, int) the number of conversions for the second conversion event attributed to the date the campaign was sent,
                    "conversions2": (optional, int) the number of conversions for the third conversion event,
                    "conversions2_by_send_time": (optional, int) the number of conversions for the third conversion event attributed to the date the campaign was sent,
                    "conversions3": (optional, int) the number of conversions for the fourth conversion event,
                    "conversions3_by_send_time": (optional, int) the number of conversions for the fourth conversion event attributed to the date the campaign was sent
      			}, {
      				"variation_name": (optional, string) the variation name,
      				"revenue": (float) the number of dollars of revenue (USD),
      				"unique_recipients": (int) the number of unique recipients,
      				"conversions": (int) the number of conversions,
                    "conversions_by_send_time": (int) the number of conversions attributed to the date the campaign was sent,
                    "conversions1": (optional, int) the number of conversions for the second conversion event,
                    "conversions1_by_send_time": (optional, int) the number of conversions for the second conversion event attributed to the date the campaign was sent,
                    "conversions2": (optional, int) the number of conversions for the third conversion event,
                    "conversions2_by_send_time": (optional, int) the number of conversions for the third conversion event attributed to the date the campaign was sent,
                    "conversions3": (optional, int) the number of conversions for the fourth conversion event,
                    "conversions3_by_send_time": (optional, int) the number of conversions for the fourth conversion event attributed to the date the campaign was sent
      				"enrolled": (optional, int) the number of enrolled users
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

Los posibles tipos de mensajería son: `email`, `in_app_message`, `webhook`, `android_push`, `ios_push`, `kindle_push`, y `web_push`. Todos los tipos de mensajes push tendrán las mismas estadísticas mostradas para `android_push`.

{% alert tip %}
Para obtener ayuda con las exportaciones CSV y API, visita [Solución de problemas de exportación]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
