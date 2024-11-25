---
nav_title: "GET: Lista de bloques de contenido disponibles"
article_title: "GET: Lista de bloques de contenido disponibles"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Enumerar los bloques de contenido disponibles de Braze."

---
{% api %}
# Lista de bloques de contenido disponibles
{% apimethod get %}
/content_blocks/list
{% endapimethod %}

> Utiliza este punto final para listar la información de tus [Bloques de contenido]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) existentes.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6d87048f-68fd-46c9-aa15-3a970e99540e {% endapiref %}

## Requisitos previos
Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/api_key/) con el permiso `content_blocks.list`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
|---|---|---|---|
| `modified_after`  | Opcional | Cadena en formato [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)  | Recupera sólo los bloques de contenido actualizados a la hora dada o después. |
| `modified_before`  |  Opcional | Cadena en formato [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)  | Recupera sólo los bloques de contenido actualizados en el momento dado o antes. |
| `limit` | Opcional | Número positivo | Número máximo de Bloques de contenido para recuperar. Predeterminado a 100 si no se proporciona, con un valor máximo aceptable de 1000. |
| `offset`  |  Opcional | Número positivo | Número de bloques de contenido que hay que omitir antes de devolver el resto de plantillas que se ajustan a los criterios de búsqueda. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud
```
curl --location --request GET 'https://rest.iad-01.braze.com/content_blocks/list?modified_after=2020-01-01T01:01:01.000000&modified_before=2020-02-01T01:01:01.000000&limit=100&offset=1' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Respuesta

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "count": "integer",
  "content_blocks": [
    {
      "content_block_id": (string) the Content Block identifier,
      "name": (string) the name of the Content Block,
      "content_type": (string) the content type, html or text,
      "liquid_tag": (string) the Liquid tags,
      "inclusion_count" : (integer) the inclusion count,
      "created_at": (string) The time the Content Block was created in ISO 8601,
      "last_edited": (string) The time the Content Block was last edited in ISO 8601,
      "tags": (array) An array of tags formatted as strings,
    }
  ]
}
```

## Solución de problemas

La siguiente tabla enumera los posibles errores devueltos y sus pasos asociados para la solución de problemas.

| Error | Solución de problemas |
| --- | --- |
| `Modified after time is invalid` | La fecha proporcionada no es una fecha válida o analizable. Reformatea este valor como una cadena en formato ISO 8601 (`yyyy-mm-ddThh:mm:ss.ffffff`). |
| `Modified before time is invalid` | La fecha proporcionada no es una fecha válida o analizable. Reformatea este valor como una cadena en formato ISO 8601 (`yyyy-mm-ddThh:mm:ss.ffffff`). |
| `Modified after time must be earlier than or the same as modified before time.` | Cambia el valor de `modified_after` a una hora anterior a la de `modified_before`. |
| `Content Block number limit is invalid` | El parámetro `limit` debe ser un número entero (positivo) mayor que 0. |
| `Content Block number limit must be greater than 0` | Cambia el parámetro `limit` por un número entero mayor que 0. |
| `Content Block number limit exceeds maximum of 1000` | Cambia el parámetro `limit` por un número entero inferior a 1000. |
| `Offset is invalid` | El parámetro `offset` debe ser un número entero mayor que 0. |
| El desplazamiento debe ser mayor que 0 | Cambia el parámetro `offset` por un número entero mayor que 0. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
