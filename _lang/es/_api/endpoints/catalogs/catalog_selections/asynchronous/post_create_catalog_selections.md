---
nav_title: "PUBLICAR: Crear selección de catálogo"
article_title: "PUBLICAR: Crear selección de catálogo"
search_tag: Punto de conexión
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
| `selection` | Obligatoria | Objeto    | Un objeto que contiene criterios de selección. Consulta [el objeto de selección del catálogo]({{site.baseurl}}/api/objects_filters/catalog_selection_object/) para obtener un desglose completo del objeto y sus campos. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Parámetros del objeto de selección

| Parámetro        | Obligatoria | Tipo de datos | Descripción                                                                                                                                                        |
| ---------------- | -------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `name`           | Obligatoria | Cadena    | El nombre de la selección del catálogo. |
| `description`    | Opcional | Cadena    | Descripción de la selección del catálogo. |
| `external_id`    | Obligatoria | Cadena    | Un identificador único para la selección. |
| `source`         | Obligatoria | Cadena    | La fuente de los datos del catálogo. Para los catálogos de Shopify, utiliza `"Shopify"`. Para catálogos personalizados, utiliza `"custom"`. |
| `filters`        | Opcional | Matriz    | Una matriz de objetos para filtrar los elementos del catálogo. Puedes especificar hasta cuatro filtros por solicitud. Si no se proporcionan filtros, se incluyen todos los artículos del catálogo. |
| `results_limit`  | Opcional | Entero   | El número máximo de resultados que se devolverán. Debe ser un número entre 1 y 50. |
| `sort_field`     | Opcional | Cadena    | El campo por el que ordenar los resultados. Esto debe combinarse con `sort_order`. Si no están `sort_order`presentes ni`sort_field`  ni , los resultados se aleatorizan. |
| `sort_order`     | Opcional | Cadena    | El orden para clasificar los resultados. Los valores aceptados son`"asc"`  (ascendente) o`"desc"`  (descendente). Esto debe combinarse con `sort_field`. Si no están `sort_order`presentes ni`sort_field`  ni , los resultados se aleatorizan. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert note %}
Los parámetros`sort_field`  `sort_order`y  deben utilizarse juntos. Si proporcionas uno sin el otro, u omites ambos parámetros, los resultados de la selección se devuelven en orden aleatorio.
{% endalert %}

## Ejemplo de solicitud

```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs/restaurants/selections' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "selection": {
    "name": "favorite-restaurants",
    "description": "Favorite restaurants in NYC",
    "external_id": "favorite-nyc-restaurants",
    "source": "custom",
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
    ],
    "results_limit": 10,
    "sort_field": "Rating",
    "sort_order": "desc"
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

{% alert note %}
La API admite un máximo de cuatro filtros por solicitud de selección. En el panel de Braze, puedes añadir hasta 10 filtros por selección. Los filtros se aplican en el orden en que aparecen en la matriz.
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
