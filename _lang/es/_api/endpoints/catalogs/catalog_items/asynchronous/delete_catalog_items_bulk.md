---
nav_title: "DELETE: Eliminar varios elementos del catálogo"
article_title: "DELETE: Eliminar varios elementos del catálogo"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Eliminar varios elementos del catálogo de Braze."

---
{% api %}
# Eliminar varios elementos del catálogo
{% apimethod delete %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> Utilice este punto final para eliminar varios elementos de su catálogo.

Cada solicitud puede admitir hasta 50 elementos. Este punto final es asíncrono.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#647c82e8-8b38-4df2-bde2-b1d8e19fd332 {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `catalogs.delete_items`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog item' %}

## Parámetros de la ruta

| Parámetro | Obligatoria | Tipo de datos | Descripción |
|---|---|---|---|
| `catalog_name` | Obligatoria | Cadena | Nombre del catálogo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
|---|---|---|---|
| `items` | Obligatoria | Matriz | Un array que contiene objetos item. Los objetos de elemento deben contener un `id` que haga referencia a los elementos que Braze debe eliminar. Se permite un máximo de 50 objetos por solicitud. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {"id": "restaurant1"},
    {"id": "restaurant2"},
    {"id": "restaurant3"}
  ]
}'
```

## Respuesta

Existen tres respuestas de código de estado para este punto final: `202`, `400` y `404`.

### Ejemplo de respuesta positiva

El código de estado `202` podría devolver el siguiente cuerpo de respuesta.

```json
{
  "message": "success"
}
```

### Ejemplo de respuesta de error

El código de estado `400` podría devolver el siguiente cuerpo de respuesta. Consulte la sección [Solución de problemas](#troubleshooting) para obtener más información sobre los errores que puede encontrar.

```json
{
  "errors": [
    {
      "id": "items-missing-ids",
      "message": "There are 1 item(s) that do not have ids",
      "parameters": [],
      "parameter_values": []
    }
  ],
  "message": "Invalid Request",
}
```

## Solución de problemas

La siguiente tabla enumera los posibles errores devueltos y los pasos asociados para solucionarlos.

| Error | Solución de problemas |
| --- | --- |
| `catalog-not-found` | Compruebe que el nombre del catálogo es válido. |
| `ids-too-large` | Los ID de los artículos no pueden tener más de 250 caracteres. |
| `ids-not-unique` | Comprueba que los ID de los elementos sean únicos en la solicitud. |
| `ids-not-strings` | Los ID de artículo deben ser de tipo cadena. |
| `items-missing-ids` | Algunos artículos no tienen ID de artículo. Compruebe que cada artículo tiene un ID de artículo. |
| `invalid-ids` | Los ID de elementos solo pueden incluir letras, números, guiones y guiones bajos. |
| `request-includes-too-many-items` | Su solicitud tiene demasiados elementos. El límite de elementos por solicitud es de 50. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
