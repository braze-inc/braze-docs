---
nav_title: "COLOCAR: Sustituir artículo del catálogo"
article_title: "COLOCAR: Sustituir artículo del catálogo"
search_tag: Endpoint
page_order: 6

layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Braze Reemplazar elemento de catálogo."

---
{% api %}
# Sustituir artículo del catálogo
{% apimethod put %}
/catalogs/{catalog_name}/items/{item_id}
{% endapimethod %}

> Utiliza este punto final para sustituir un elemento de tu catálogo.

Si no se encuentra `item_id`, este punto final creará el elemento en tu catálogo. Este punto final es síncrono.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#b2871ed7-734e-4a37-b8f1-e11584e569f5 {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `catalogs.replace_item`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='synchronous catalog item' %}

## Parámetros de la ruta

| Parámetro | Obligatoria | Tipo de datos | Descripción |
|---|---|---|---|
| `catalog_name` | Obligatoria | Cadena | Nombre del catálogo. |
| `item_id` | Obligatoria | Cadena | El ID del elemento del catálogo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
|---|---|---|---|
| `items` | Obligatoria | Matriz | Un array que contiene objetos item. Los objetos de artículo deben contener campos que existan en el catálogo, excepto el campo `id`. Sólo se permite un objeto por solicitud. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud

```
curl --location --request PUT 'https://rest.iad-03.braze.com/catalogs/restaurants/items/restaurant1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {
      "Name": "Restaurant",
      "Loyalty_Program": false,
      "Location": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      },
      "Top_Dishes": [
        "Hamburger",
        "Deluxe Cheeseburger"
      ],
      "Open_Time": "2021-09-03T09:03:19.967+00:00"
    }
  ]
}'
```

## Respuesta

Existen tres respuestas de código de estado para este punto final: `200`, `400` y `404`.

### Ejemplo de respuesta positiva

El código de estado `200` podría devolver el siguiente cuerpo de respuesta.

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
      "id": "invalid-fields",
      "message": "Some of the fields given do not exist in the catalog",
      "parameters": [
        "id"
      ],
      "parameter_values": [
        "restaurant1"
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
| `arbitrary-error` | Se ha producido un error arbitrario. Vuelva a intentarlo o póngase en contacto con [el servicio de asistencia]({{site.baseurl}}/support_contact/). |
| `catalog-not-found` | Compruebe que el nombre del catálogo es válido. |
| `filtered-set-field-too-long` | El valor del campo se está utilizando en un conjunto filtrado que supera el límite de caracteres de un elemento. |
| `id-in-body` | Elimina cualquier ID de artículo en el cuerpo de la solicitud. |
| `ids-too-large` | El límite de caracteres para cada ID de artículo es de 250 caracteres. |
| `invalid-ids` | Los caracteres admitidos para los nombres de ID de artículos son letras, números, guiones y guiones bajos. |
| `invalid-fields` | Confirme que todos los campos que está enviando en la solicitud API ya existen en el catálogo. Esto no está relacionado con el campo ID mencionado en el error. |
| `invalid-keys-in-value-object` | Las claves de objeto de artículo no pueden incluir `.` ni `$`. |
| `item-already-exists` | El artículo ya existe en el catálogo. |
| `item-array-invalid` | `items` debe ser un array de objetos. |
| `items-too-large` | El límite de caracteres para cada elemento es de 5000 caracteres. |
| `request-includes-too-many-items` | Sólo puede crear un elemento de catálogo por solicitud. |
| `too-deep-nesting-in-value-object` | Los objetos item no pueden tener más de 50 niveles de anidamiento. |
| `unable-to-coerce-value` | Los tipos de artículo no se pueden convertir. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
