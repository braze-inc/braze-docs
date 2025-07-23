---
nav_title: "GET: Exportar lista de tarjetas de noticias"
article_title: "GET: Exportar lista de tarjetas de noticias"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Exportar lista de tarjetas de noticias de Braze."

---
{% api %}
# Exportar lista de tarjetas de noticias
{% apimethod get %}
/feed/list
{% endapimethod %}

> Utilice este punto final para exportar una lista de tarjetas de noticias, cada una de las cuales incluirá su nombre y el identificador API de la tarjeta.

Las tarjetas se devuelven en grupos de 100 ordenadas por hora de creación (de la más antigua a la más reciente por defecto).

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9fa7a3bc-4a02-4de2-bc4c-8f111750665e {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `feed.list`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | -------- | --------- | ----------- |
| `page` | Opcional | Entero   | La página de tarjetas para devolver, de forma predeterminada es 0 (devuelve el primer conjunto de hasta 100). |
| `include_archived` | Opcional | Booleano   | Incluir o no las tarjetas archivadas, por defecto falso. |
| `sort_direction` | Opcional | Cadena | \- Ordenar la hora de creación de más reciente a más antigua: introduce el valor `desc`.<br> \- Ordenar la hora de creación de más antiguo a más reciente: introduce el valor `asc`. <br><br>Si no se incluye `sort_direction`, el orden predeterminado es del más antiguo al más reciente. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud
```
curl --location --request GET 'https://rest.iad-01.braze.com/feed/list?page=1&include_archived=true&sort_direction=desc' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Respuesta

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "cards" : [
        {
            "id" : (string) the card API identifier,
            "type" : (string) type of the card - NewsItem (classic cards), CaptionedImage, Banner
            "title" : (string) the title of the card,
            "tags" : (array) the tag names associated with the card
        },
        ...
    ]
}
```

{% alert tip %}
Para obtener ayuda con las exportaciones CSV y API, visita [Solución de problemas de exportación]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
