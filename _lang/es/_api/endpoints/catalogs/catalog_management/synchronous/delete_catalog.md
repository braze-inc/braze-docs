---
nav_title: "DELETE: Eliminar catálogo"
article_title: "DELETE: Eliminar catálogo"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Eliminar catálogo de Braze."

---
{% api %}
# Borrar catálogo
{% apimethod delete %}
/catalogs/{catalog_name}
{% endapimethod %}

> Utiliza este punto final para eliminar un catálogo.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c0915a86-797a-4486-8217-24cd1c689d0f {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `catalogs.delete`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='synchronous catalog' %}

## Parámetros de la ruta

| Parámetro | Obligatoria | Tipo de datos | Descripción |
|---|---|---|---|
| `catalog_name` | Obligatoria | Cadena | Nombre del catálogo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
```

## Respuesta

Hay dos respuestas de código de estado para este punto final: `200` y `404`.

### Ejemplo de respuesta satisfactoria

El código de estado `200` podría devolver el siguiente cuerpo de respuesta:

```json
{
  "message": "success"
}
```

### Ejemplo de respuesta de error

El código de estado `404` podría devolver el siguiente cuerpo de respuesta. Consulte la sección [Solución de problemas](#troubleshooting) para obtener más información sobre los errores que puede encontrar.

```json
{
  "errors": [
    {
      "id": "catalog-not-found",
      "message": "Could not find catalog",
      "parameters": [
        "catalog_name"
      ],
      "parameter_values": [
        "restaurants"
      ]
    }
  ],
  "message": "Invalid Request"
}
```

## Solución de problemas

La siguiente tabla enumera los posibles errores devueltos y los pasos asociados para solucionarlos.

| Error | Solución de problemas |
| --- | --- |
| `catalog-not-found` | Compruebe que el nombre del catálogo es válido. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
