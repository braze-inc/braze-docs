---
nav_title: "PUBLICAR: Crear varios elementos del catálogo"
article_title: "PUBLICAR: Crear varios elementos de catálogo"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Crear varios elementos del catálogo de Braze."

---
{% api %}
# Crear varios elementos del catálogo
{% apimethod post %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> Utiliza este punto final para crear varios elementos en tu catálogo.

Cada solicitud puede admitir hasta 50 elementos. Este punto final es asíncrono.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#cea18bb3-b83a-4160-81fe-8cd42aa6e7cc {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `catalogs.add_items`.

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
| `items` | Obligatoria | Matriz | Un array que contiene objetos item. Los objetos de artículo deben contener todos los campos del catálogo. Se permite un máximo de 50 objetos por solicitud. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud

```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {
      "id": "restaurant1",
      "Name": "Restaurant1",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 5,
      "Loyalty_Program": true,
      "Location": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      },
      "Top_Dishes": [
        "Hamburger",
        "Deluxe Cheeseburger"
      ],
      "Created_At": "2022-11-01T09:03:19.967+00:00"
    },
    {
      "id": "restaurant2",
      "Name": "Restaurant2",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 10,
      "Loyalty_Program": true,
      "Location": {
        "Latitude": 40.7413,
        "Longitude": -73.9764
      },
      "Top_Dishes": [
        "Hot Dog",
        "French Fries"
      ],
      "Created_At": "2022-11-02T09:03:19.967+00:00"
    },
    {
      "id": "restaurant3",
      "Name": "Restaurant3",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 3,
      "Loyalty_Program": false,
      "Location": {
        "Latitude": 40.7489,
        "Longitude": -73.9972
      },
      "Top_Dishes": [
        "Buffalo Wings",
        "Philly Cheesesteak"
      ],
      "Created_At": "2022-11-03T09:03:19.967+00:00"
    }
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

La siguiente tabla enumera los posibles errores devueltos y sus pasos asociados para la solución de problemas.

| Error | Solución de problemas |
| --- | --- |
| `catalog-not-found` | Compruebe que el nombre del catálogo es válido. |
| `ids-not-strings` | Los ID de artículo deben ser de tipo cadena. |
| `ids-not-unique` | Los ID de los artículos deben ser únicos en la solicitud. |
| `ids-too-large` | Los ID de los artículos no pueden tener más de 250 caracteres. |
| `invalid-ids` | Los ID de elementos solo pueden incluir letras, números, guiones y guiones bajos. |
| `invalid-fields` | Confirme que todos los campos que está enviando en la solicitud API ya existen en el catálogo. Esto no está relacionado con el campo ID mencionado en el error. |
| `invalid-keys-in-value-object` | Las claves de objeto de artículo no pueden incluir `.` ni `$`. |
| `item-array-invalid` | `items` debe ser un array de objetos. |
| `items-missing-ids` | Algunos artículos no tienen ID de artículo. Compruebe que cada artículo tiene un ID de artículo. |
| `items-too-large` | Los valores de los elementos no pueden superar los 5.000 caracteres. |
| `request-includes-too-many-items` | Su solicitud tiene demasiados elementos. El límite de elementos por solicitud es de 50. |
| `too-deep-nesting-in-value-object` | Los objetos item no pueden tener más de 50 niveles de anidamiento. |
| `unable-to-coerce-value` | Los tipos de artículo no se pueden convertir. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
