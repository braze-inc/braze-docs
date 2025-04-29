---
nav_title: "GET: Exportar eventos personalizados"
article_title: "GET: Exportar eventos personalizados"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Exportar eventos personalizados de Braze."

---
{% api %}
# Exportar eventos personalizados
{% apimethod get %}
/eventos
{% endapimethod %}

> Utiliza este punto final para exportar una lista de eventos personalizados registrados para tu aplicación. Los eventos se devuelven en grupos de 50, ordenados alfabéticamente.

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `events.get`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='events' %}

## Parámetros de consulta

Ten en cuenta que cada llamada a este punto final devolverá 50 eventos. Para más de 50 eventos, utiliza la cabecera `Link` para recuperar los datos en la página siguiente, como se muestra en el siguiente ejemplo de respuesta.

| Parámetro | Obligatoria | Tipo de datos | Descripción |
|---|---|---|---|
| `cursor` | Opcional | Cadena | Determina la paginación de los eventos personalizados. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Ejemplos de solicitudes

### Sin cursor

```
curl --location --request GET 'https://rest.iad-01.braze.com/events' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

### Con cursor

```
curl --location --request GET 'https://rest.iad-03.braze.com/events?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Respuesta

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "events" : [
        {
            "name": "The event name", (string) the event name,
            "description": "The event description", (string) the event description,
            "included_in_analytics_report": false, (boolean) the analytics report inclusion,
            "status": "Active", (string) the event status,
            "tag_names": ["Tag One", "Tag Two"] (array) the tag names associated with the event formatted as strings,
        },
        ...
    ]
}
```

### Códigos de respuesta de error fatal {#fatal-export}

Para conocer los códigos de estado y los mensajes de error asociados que se devolverán si tu solicitud encuentra un error fatal, consulta [Errores fatales]({{site.baseurl}}/api/errors/#fatal-errors).

{% alert tip %}
Para obtener ayuda con las exportaciones CSV y API, visita [Solución de problemas de exportación]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}
