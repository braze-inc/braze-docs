---
nav_title: "Objeto de selección del catálogo"
article_title: Objeto de selección del catálogo API
page_order: 12
page_type: reference
description: "Este artículo de referencia explica los diferentes componentes del objeto de selección del catálogo."
tool: Catalogs

---

# Objeto de selección del catálogo

> Al crear una selección de catálogo, puedes proporcionar un objeto de selección para definir los criterios para filtrar, clasificar y limitar los elementos devueltos por tu catálogo.

El`selection`objeto te permite especificar qué elementos de tu catálogo deben incluirse en la selección al filtrar, cómo deben ordenarse y cuántos resultados deben devolverse. Utiliza este objeto al crear selecciones de catálogo a través de la API.

## Cuerpo del objeto

```json
{
  "selection": {
    "name": "Sale",
    "description": "Sales Collection",
    "external_id": "12345678",
    "source": "Shopify",
    "filters": [
      {
        "field": "collection",
        "operator": "includes value",
        "value": "Best Seller"
      },
      {
        "field": "collection",
        "operator": "does not include value",
        "value": "Sale"
      }
    ],
    "results_limit": 5,
    "sort_field": "id",
    "sort_order": "asc"
  }
}
```

## Detalles del objeto

| Clave | Obligatoria | Tipo de datos | Descripción |
| --- | -------- | --------- | ----------- |
| `name` | Obligatoria | Cadena | El nombre de la selección del catálogo. |
| `description` | Opcional | Cadena | Descripción de la selección del catálogo. |
| `external_id` | Obligatoria | Cadena | Un identificador único para la selección. |
| `source` | Obligatoria | Cadena | La fuente de los datos del catálogo. Para los catálogos de Shopify, configura esto en `"Shopify"`. Para catálogos que no sean de Shopify, utiliza una cadena descriptiva, como`"custom"`  o el nombre de tu integración. |
| `filters` | Opcional | Conjunto de objetos | Una matriz de objetos para filtrar los elementos del catálogo. Puedes especificar hasta cuatro filtros por solicitud. Si no se proporcionan filtros, se incluyen todos los artículos del catálogo. |
| `results_limit` | Opcional | Entero | El número máximo de resultados que se devolverán. Debe ser un número entre 1 y 50. |
| `sort_field` | Opcional | Cadena | El campo por el que ordenar los resultados. Esto debe combinarse con `sort_order`. Si no están presentes`sort_order` ni`sort_field`, los resultados se devuelven en orden aleatorio. |
| `sort_order` | Opcional | Cadena | El orden para clasificar los resultados. Los valores aceptados son`"asc"`  (ascendente) o`"desc"`  (descendente). Esto debe combinarse con `sort_field`. Si no están presentes`sort_order` ni`sort_field`, los resultados se devuelven en orden aleatorio. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Objeto para filtrar

Cada objeto de filtro de la`filters`matriz contiene los campos descritos en la siguiente tabla.

| Clave | Obligatoria | Tipo de datos                                   | Descripción |
| --- | -------- | ------------------------------------------- | ----------- |
| `field`    | Obligatoria | Cadena                                      | El campo del catálogo por el que filtrar. |
| `operator` | Obligatoria | Cadena                                      | El operador de comparación que se utilizará para filtrar. Algunos ejemplos son`"includes value"`  y `"does not include value"`. |
| `value`    | Obligatoria | Varía (cadena, número, booleano, tiempo)     | El valor con el que comparar. Esto debe coincidir con el tipo de datos del campo del catálogo subyacente (por ejemplo, cadena, número, booleano, hora). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert note %}
La API admite un máximo de cuatro filtros por solicitud de selección. En el panel de Braze, puedes añadir hasta 10 filtros por selección. Los filtros se aplican en el orden en que aparecen en la matriz.
{% endalert %}
