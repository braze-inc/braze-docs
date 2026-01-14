---
nav_title: "PARCHE: Editar varios elementos del catálogo"
article_title: "PARCHE: Editar varios elementos del catálogo"
alias: /catalogs_items_patch/
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Editar varios elementos del catálogo de Braze."

---
{% api %}
# Editar varios elementos del catálogo
{% apimethod patch %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> Utiliza este punto final para editar varios elementos existentes en tu catálogo.

Cada solicitud puede admitir hasta 50 elementos. Este punto final es asíncrono.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#03f3548e-4139-4f60-812d-7e1a695a738a {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `catalogs.update_items`.

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
| `items` | Obligatoria | Matriz | Una matriz que contiene objetos elemento. Los objetos artículo deben contener campos que existan en el catálogo. Se permiten hasta 50 objetos de artículo por solicitud. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud

```
curl --location --request PATCH 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {
      "id": "restaurant1",
      "Name": "Restaurant",
      "Loyalty_Program": false,
      "Location": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      },
      "Top_Dishes": {
        "$add": [
          "Biscuits",
          "Coleslaw"
        ],
        "$remove": [
          "French Fries"
        ]
      },
      "Open_Time": "2021-09-03T09:03:19.967+00:00"
    },
    {
      "id": "restaurant3",
      "City": "San Francisco",
      "Rating": 2,
      "Top_Dishes": [
        "Buffalo Wings",
        "Philly Cheesesteak"
      ]
    }
  ]
}'
```

{% alert note %}
Los operadores `$add` y `$remove` sólo son aplicables a campos de tipo array, y sólo son compatibles con los extremos PATCH.
{% endalert %}

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
| `catalog-not-found` | Compruebe que el nombre del catálogo es válido. |
| `ids-too-large` | Los ID de los artículos no pueden tener más de 250 caracteres. |
| `ids-not-strings` | Los ID de artículo deben ser de tipo cadena. |
| `ids-not-unique` | Los ID de los artículos deben ser únicos en la solicitud. |
| `invalid-ids` | Los ID de elementos solo pueden incluir letras, números, guiones y guiones bajos. |
| `invalid-fields` | Confirme que todos los campos que está enviando en la solicitud API ya existen en el catálogo. Esto no está relacionado con el campo ID mencionado en el error. |
| `invalid-keys-in-value-object` | Las claves de objeto de artículo no pueden incluir `.` ni `$`. |
| `items-missing-ids` | Algunos artículos no tienen ID de artículo. Compruebe que cada artículo tiene un ID de artículo. |
| `item-array-invalid` | `items` debe ser un array de objetos. |
| `items-too-large` | Los valores de los elementos no pueden superar los 5.000 caracteres. |
| `request-includes-too-many-items` | Su solicitud tiene demasiados elementos. El límite de elementos por solicitud es de 50. |
| `too-deep-nesting-in-value-object` | Los objetos item no pueden tener más de 50 niveles de anidamiento. |
| `unable-to-coerce-value` | Los tipos de artículo no se pueden convertir. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
