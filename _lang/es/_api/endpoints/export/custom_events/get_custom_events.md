---
nav_title: "GET: Exportar lista de eventos personalizados"
article_title: "GET: Exportar lista de eventos personalizados"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Exportar lista de eventos personalizados de Braze."

---
{% api %}
# Exportar lista de eventos personalizados
{% apimethod get %}
/events/list
{% endapimethod %}

> Utiliza este punto final para exportar una lista de eventos personalizados que se han registrado para tu aplicación. Los nombres de los eventos se devuelven en grupos de 250, ordenados alfabéticamente.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#93ecd8a5-305d-4b72-ae33-2d74983255c1 {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `events.list`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='events list' %}

## Parámetros de la solicitud

| Parámetro| Obligatoria | Tipo de datos | Descripción |
| -------- | -------- | --------- | ----------- |
| `page` | Opcional | Entero | La página de nombres de eventos a devolver, predeterminada a 0 (devuelve el primer conjunto de hasta 250). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud
```
curl --location --request GET 'https://rest.iad-01.braze.com/events/list?page=3' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Respuesta

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "events" : [
        "Event A", (string) the event name,
        "Event B", (string) the event name,
        "Event C", (string) the event name,
        ...
    ]
}
```

### Códigos de respuesta de error fatal {#fatal-export}

Para conocer los códigos de estado y los mensajes de error asociados que se devolverán si tu solicitud encuentra un error fatal, consulta [Errores fatales y respuestas.]({{site.baseurl}}/api/errors/#fatal-errors)

{% alert tip %}
Para obtener ayuda con las exportaciones CSV y API, visita [Solución de problemas de exportación]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
