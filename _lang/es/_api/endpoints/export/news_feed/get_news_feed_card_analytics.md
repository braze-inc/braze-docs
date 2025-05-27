---
nav_title: "GET: Exportar análisis de tarjeta de canal de noticias"
article_title: "GET: Exportar análisis de tarjeta de canal de noticias"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Exportar análisis de tarjetas de noticias de Braze."

---
{% api %}
# Exportar análisis de tarjeta de canal de noticias
{% apimethod get %}
/feed/data_series
{% endapimethod %}

> Utiliza este punto final para recuperar una serie diaria de estadísticas de interacción de una tarjeta a lo largo del tiempo.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9cdc3b1e-641e-4d62-b9e8-42d04ee9d4d8 {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `feed.data_series`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parámetros de la solicitud

| Parámetro   | Obligatoria | Tipo de datos | Descripción |
| ----------- | -------- | --------- | ----------- |
| `card_id` | Obligatoria | Cadena | Ver [Identificador API de tarjeta]({{site.baseurl}}/api/identifier_types/). <br><br> Puedes encontrar el `card_id` de una tarjeta determinada en la página [Claves de API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) y en la página de detalles de la tarjeta dentro de tu panel, o puedes utilizar el [punto final Exportar lista de tarjetas de canal de noticias]({{site.baseurl}}/api/endpoints/export/news_feed/get_news_feed_cards/).|
| `length` | Obligatoria | Entero | Número máximo de unidades (días u horas) antes de `ending_at` a incluir en la serie devuelta. Debe estar entre 1 y 100 (ambos inclusive). |
| `unit` | Opcional | Cadena | Unidad de tiempo entre puntos de datos. Puede ser `day` o `hour`, de forma predeterminada, `day`.  |
| `ending_at` | Opcional | Fecha y hora <br>(cadena [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Fecha en la que debe finalizar la serie de datos. De forma predeterminada, la hora de la solicitud. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/feed/data_series?card_id={{card_identifier}}&length=14&unit=day&ending_at=2018-06-28T23:59:59-5:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Respuesta

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "data" : [
        {
            "time" : (string) the point in time - as ISO 8601 extended when unit is "hour" and as ISO 8601 date when unit is "day",
            "clicks" : (int) the number of clicks,
            "impressions" : (int) the number of impressions,
            "unique_clicks" : (int) the number of unique clicks,
            "unique_impressions" : (int) the number of unique impressions
        },
        ...
    ]
}
```

{% alert tip %}
Para obtener ayuda con las exportaciones CSV y API, visita [Solución de problemas de exportación]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
