---
nav_title: "PUBLICAR: Crear selección de catálogo"
article_title: "PUBLICAR: Crear selección de catálogo"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Crear selección del catálogo de Braze."

---
{% api %}
# Crear selección de catálogo
{% apimethod post %}
/catalogs/{catalog_name}/selections
{% endapimethod %}

> Utiliza este punto final para crear una selección en tu catálogo.

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `catalogs.create_selection`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog selections' %}

## Parámetros de la ruta

| Parámetro      | Obligatoria | Tipo de datos | Descripción          |
| -------------- | -------- | --------- | -------------------- |
| `catalog_name` | Obligatoria | Cadena    | Nombre del catálogo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Parámetros de la solicitud

| Parámetro   | Obligatoria | Tipo de datos | Descripción                                                                                                                                                        |
| ----------- | -------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `selection` | Obligatoria | Objeto    | Un objeto que contiene criterios de selección. Los objetos de selección pueden contener `name`, `description`, `filters`, `results_limit`, `sort_field` y `sort_order`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud

```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs/restaurants/selections' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "selection": {
    "name": "favorite-restaurants",
    "description": "Favorite restaurants in NYC",
    "filters": [
      {
        "field": "City",
        "operator": "equals",
        "value": "NYC"
      },
      {
        "field": "Rating",
        "operator": "greater than",
        "value": 7
      }
    ]
  }
}'
```

### Operadores de filtrado

| Tipo de campo | Operadores admitidos                                     |
| ---------- | ------------------------------------------------------- |
| `string`   | `equals`, `does not equal`                              |
| `number`   | `equals`, `does not equal`, `greater than`, `less than` |
| `boolean`  | `is`                                                    |
| `time`     | `before`, `after`                                       |
| `array`    | `includes value`, `does not include value`              |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

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

La siguiente tabla enumera los posibles errores devueltos y sus pasos asociados para la solución de problemas.

| Error                                | Solución de problemas                                                                               |
|--------------------------------------|-----------------------------------------------------------------------------------------------|
| `catalog-not-found`                  | Compruebe que el nombre del catálogo es válido.                                                         |
| `company-size-limit-already-reached` | Se ha alcanzado el límite de tamaño de almacenamiento del catálogo.                                                    |
| `selection-limit-reached`            | Se ha alcanzado el límite de selecciones del catálogo.                                                      |
| `invalid-selection`                  | Comprueba que la selección es válida.                                                            |
| `too-many-filters`                   | Comprueba si la selección tiene demasiados filtros.                                                  |
| `selection-name-already-exists`      | Comprueba si el nombre de la selección ya existe en el catálogo.                                    |
| `selection-has-invalid-filter`       | Comprueba si el filtro de selección es válido.                                                       |
| `selection-invalid-results-limit`    | Comprueba si el límite de resultados de la selección es válido.                                                |
| `invalid-sorting`                    | Comprueba si la ordenación de la selección es válida.                                                      |
| `invalid-sort-field`                 | Comprueba si el campo de ordenación de la selección es válido.                                                   |
| `invalid-sort-order`                 | Comprueba si el orden de clasificación de la selección es válido.                                                   |
| `selection-contains-too-many-arrays` | Comprueba si la selección contiene más de un campo con el tipo `array`. Solo se admite uno. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
