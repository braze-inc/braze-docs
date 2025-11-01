---
nav_title: "PUBLICAR: Crear catálogo"
article_title: "PUBLICAR: Crear catálogo"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Crear catálogo de Braze."

---
{% api %}
# Crear catálogo
{% apimethod post %}
/catalogs
{% endapimethod %}

> Utiliza este punto final para crear un catálogo.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#af9f3e2d-b7e7-49e7-aa64-f4652892be6e {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `catalogs.create`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='synchronous catalog' %}

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
|---|---|---|---|
| `catalogs` | Obligatoria | Matriz | Una matriz que contiene objetos de catálogo. Sólo se permite un objeto de catálogo para esta solicitud. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Parámetros del objeto del catálogo

| Parámetro | Obligatoria | Tipo de datos | Descripción |
|---|---|---|---|
| `name` | Obligatoria | Cadena | El nombre del catálogo que quieres crear. |
| `description` | Obligatoria | Cadena | La descripción del catálogo que quieres crear. |
| `fields` | Obligatoria | Matriz | Una matriz de objetos en la que el objeto contiene las claves `name` y `type`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud
```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "catalogs": [
    {
      "name": "restaurants",
      "description": "My Restaurants",
      "fields": [
        {
          "name": "id",
          "type": "string"
        },
        {
          "name": "Name",
          "type": "string"
        },
        {
          "name": "City",
          "type": "string"
        },
        {
          "name": "Cuisine",
          "type": "string"
        },
        {
          "name": "Rating",
          "type": "number"
        },
        {
          "name": "Loyalty_Program",
          "type": "boolean"
        },
        {
          "name": "Location",
          "type": "object"
        },
        {
          "name": "Top_Dishes",
          "type": "array"
        },
        {
          "name": "Created_At",
          "type": "time"
        }
      ]
    }
  ]
}'
```

## Respuesta

Hay dos respuestas de código de estado para este punto final: `201` y `400`.

### Ejemplo de respuesta satisfactoria

El código de estado `201` podría devolver el siguiente cuerpo de respuesta.

```json
{
  "catalogs": [
    {
      "description": "My Restaurants",
      "fields": [
        {
          "name": "id",
          "type": "string"
        },
        {
          "name": "Name",
          "type": "string"
        },
        {
          "name": "City",
          "type": "string"
        },
        {
          "name": "Cuisine",
          "type": "string"
        },
        {
          "name": "Rating",
          "type": "number"
        },
        {
          "name": "Loyalty_Program",
          "type": "boolean"
        },
        {
          "name": "Location",
          "type": "object"
        },
        {
          "name": "Top_Dishes",
          "type": "array"
        },
        {
          "name": "Created_At",
          "type": "time"
        }
      ],
      "name": "restaurants",
      "num_items": 0,
      "updated_at": "2022-11-02T20:04:06.879+00:00"
    }
  ],
  "message": "success"
}
```

### Ejemplo de respuesta de error

El código de estado `400` podría devolver el siguiente cuerpo de respuesta. Consulte la sección [Solución de problemas](#troubleshooting) para obtener más información sobre los errores que puede encontrar.

```json
{
  "errors": [
    {
      "id": "catalog-name-already-exists",
      "message": "A catalog with that name already exists",
      "parameters": [
        "name"
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

La siguiente tabla enumera los posibles errores devueltos y sus pasos asociados para la solución de problemas.

| Error | Solución de problemas |
| --- | --- |
| `catalog-array-invalid` | `catalogs` debe ser un array de objetos. |
| `catalog-name-already-exists` | Ya existe un catálogo con ese nombre. |
| `catalog-name-too-large`  | El límite de caracteres para el nombre de un catálogo es de 250. |
| `description-too-long` | El límite de caracteres para la descripción es de 250. |
| `field-names-not-unique` | Se hace referencia dos veces al mismo nombre de campo. |
| `field-names-too-large` | El límite de caracteres para un nombre de campo es 250. |
| `id-not-first-column` | El `id` debe ser el primer campo de la matriz. Comprueba que el tipo es una cadena. |
| `invalid-catalog-name` | El nombre del catálogo sólo puede incluir letras, números, guiones y guiones bajos. |
| `invalid-field-names` | Los campos sólo pueden incluir letras, números, guiones y guiones bajos. |
| `invalid-field-types` | Asegúrate de que los tipos de campo son válidos. |
| `invalid-fields` | `fields` no está formateado correctamente. |
| `too-many-catalog-atoms` | Sólo puedes crear un catálogo por solicitud. |
| `too-many-fields` | El límite de campos es 500. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
