---
nav_title: "GET: Exportar sesiones de aplicación por tiempo"
article_title: "Get: Exportar sesiones de aplicación por tiempo"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Exportar análisis de las sesiones de aplicaciones por tiempo de Braze."

---
{% api %}
# Exportar sesión de aplicación por tiempo
{% apimethod get %}
/sessions/data_series
{% endapimethod %}

> Utiliza este endpoint para recuperar una serie del número de sesiones de tu aplicación durante un periodo de tiempo determinado.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#79efb6a9-62ec-4b8a-bf4a-e96313aa4be1 {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `sessions.data_series`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parámetros de la solicitud

| Parámetro| Obligatoria | Tipo de datos | Descripción |
| -------- | -------- | --------- | ----------- |
| `length` | Obligatoria | Entero | Número máximo de unidades (días u horas) antes de `ending_at` a incluir en la serie devuelta. Debe estar entre 1 y 100 (ambos inclusive). |
| `unit` | Opcional | Cadena | Unidad de tiempo entre puntos de datos. Puede ser `day` o `hour`, de forma predeterminada, `day`.  |
| `ending_at` | Opcional | Fecha y hora <br>(cadena [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Fecha en la que debe finalizar la serie de datos. De forma predeterminada, la hora de la solicitud. |
| `app_id` | Opcional | Cadena | Identificador de API de la aplicación recuperado de la página [Claves de API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) para limitar el análisis a una aplicación concreta. |
| `segment_id` | Opcional | Cadena | Ver [Identificador API de segmento]({{site.baseurl}}/api/identifier_types/). ID del segmento que indica el segmento habilitado para análisis cuyas sesiones deben devolverse. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/sessions/data_series?length=14&unit=day&ending_at=2018-06-28T23:59:59-5:00&app_id={{app_identifier}}&segment_id={{segment_identifier}}' \
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
            "time" : (string) point in time - as ISO 8601 extended when unit is "hour" and as ISO 8601 date when unit is "day",
            "sessions" : (int)
        },
        ...
    ]
}
```

{% alert tip %}
Para obtener ayuda con las exportaciones CSV y API, visita [Solución de problemas de exportación]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
