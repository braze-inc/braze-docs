---
nav_title: "GET: Exportar análisis de eventos personalizados"
article_title: "GET: Exportar análisis de eventos personalizados"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Exportar análisis de eventos personalizados de Braze."

---
{% api %}
# Exportar análisis de eventos personalizados
{% apimethod get %}
/events/data_series
{% endapimethod %}

> Utiliza este punto final para recuperar una serie del número de ocurrencias de un evento personalizado en tu aplicación durante un periodo de tiempo designado.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0bd1ab63-d1a5-4301-8d17-246cf24a178c {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `events.data_series`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parámetros de la solicitud

| Parámetro| Obligatoria | Tipo de datos | Descripción |
| -------- | -------- | --------- | ----------- |
| `event` | Obligatoria | Cadena | El nombre del evento personalizado para el que devolver los análisis. |
| `length` | Obligatoria | Entero | Número máximo de unidades (días u horas) antes de `ending_at` a incluir en la serie devuelta. Debe estar entre 1 y 100 (ambos inclusive). |
| `unit` | Opcional | Cadena | Unidad de tiempo entre puntos de datos. Puede ser `day` o `hour`, de forma predeterminada, `day`.  |
| `ending_at` | Opcional | Fecha y hora <br>(cadena [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Fecha en la que debe finalizar la serie de datos. De forma predeterminada, la hora de la solicitud. |
| `app_id` | Opcional | Cadena | Identificador de API de la aplicación recuperado de la página [Claves de API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) para limitar el análisis a una aplicación concreta. |
| `segment_id` | Opcional | Cadena | Ver [Identificador API de segmento]({{site.baseurl}}/api/identifier_types/). ID del segmento que indica el segmento habilitado para el análisis para el que debe devolverse el análisis de eventos. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }


## Ejemplo de solicitud
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/events/data_series?event=event_name&length=24&unit=hour&ending_at=2014-12-10T23:59:59-05:00&app_id={{app_identifier}}&segment_id={{segment_identifier}}' \
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
            "count" : (int) the number of occurrences of provided custom event
        },
        ...
    ]
}
```

### Códigos de respuesta de error fatal {#fatal-export}

Para conocer los códigos de estado y los mensajes de error asociados que se devolverán si tu solicitud encuentra un error fatal, consulta [Errores fatales & responses]({{site.baseurl}}/api/errors/#fatal-errors).

{% alert tip %}
Para obtener ayuda con las exportaciones CSV y API, visita [Solución de problemas de exportación]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
