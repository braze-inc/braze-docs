---
nav_title: "GET: Exportar lista de segmentos"
article_title: "GET: Exportar lista de segmentos"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Exportar la lista de segmentos de Braze."

---
{% api %}
# Exportar lista de segmentos
{% apimethod get %}
/segments/list
{% endapimethod %}

> Utilice este punto final para exportar una lista de segmentos, cada uno de los cuales incluirá su nombre, identificador de API de segmento y si tiene activado el seguimiento analítico.

Los segmentos se devuelven en grupos de 100 ordenados por hora de creación (de más antiguo a más reciente por defecto). No se incluyen los segmentos archivados.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1349e6f4-3ce7-4e60-b3e9-951c99c0993f {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `segments.list`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parámetros de la solicitud

| Parámetro| Obligatoria | Tipo de datos | Descripción |
| -------- | -------- | --------- | ----------- |
| `page` | Opcional | Entero | La página de segmentos a devolver, por defecto 0 (devuelve el primer conjunto de hasta 100). |
| `sort_direction` | Opcional | Cadena | \- Ordenar la hora de creación de más reciente a más antigua: introduce el valor `desc`.<br> \- Ordenar la hora de creación de más antiguo a más reciente: introduce el valor `asc`. <br><br>Si no se incluye `sort_direction`, el orden predeterminado es del más antiguo al más reciente. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud
```
curl --location --request GET 'https://rest.iad-01.braze.com/segments/list?page=1&sort_direction=desc' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Respuesta

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "segments" : [
        {
            "id" : (string) the Segment API identifier,
            "name" : (string) segment name,
            "analytics_tracking_enabled" : (boolean) whether the segment has analytics tracking enabled,
            "tags" : (array) the tag names associated with the segment formatted as strings
        },
        ...
    ]
}
```

{% alert tip %}
Para obtener ayuda con las exportaciones CSV y API, visita [Solución de problemas de exportación]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
