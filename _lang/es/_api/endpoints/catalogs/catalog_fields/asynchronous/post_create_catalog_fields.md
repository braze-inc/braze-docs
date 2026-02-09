---
nav_title: "PUBLICAR: Crear campos de catálogo"
article_title: "PUBLICAR: Crear campos de catálogo"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Crear campos de catálogo de Braze."

---
{% api %}
# Crear campos de catálogo
{% apimethod post %}
/catalogs/{catalog_name}/fields
{% endapimethod %}

> Utiliza este punto final para crear varios campos en tu catálogo.

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `catalogs.create_fields`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog fields' %}

## Parámetros de la ruta

| Parámetro      | Obligatoria | Tipo de datos | Descripción          |
| -------------- | -------- | --------- | -------------------- |
| `catalog_name` | Obligatoria | Cadena    | Nombre del catálogo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción                                                                                                  |
| --------- | -------- | --------- | ------------------------------------------------------------------------------------------------------------ |
| `fields`  | Obligatoria | Matriz     | Una matriz que contiene objetos de campo. Los objetos fields deben contener el nombre y el tipo de los nuevos campos. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud

```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs/restaurants/fields' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "fields": [
    {
      "name": "Name",
      "type": "string"
    },
    {
      "name": "Ratings",
      "type": "number"
    },
    {
      "name": "Loyalty_Program",
      "type": "boolean"
    },
    {
      "name": "Created_At",
      "type": "time"
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

| Error                                | Solución de problemas                                                                                        |
|--------------------------------------|--------------------------------------------------------------------------------------------------------|
| `arbitrary-error`                    | Se ha producido un error arbitrario. Vuelva a intentarlo o póngase en contacto con [el servicio de asistencia]({{site.baseurl}}/support_contact/). |
| `catalog-not-found`                  | Compruebe que el nombre del catálogo es válido.                                                                  |
| `company-size-limit-already-reached` | Se ha alcanzado el límite de tamaño de almacenamiento del catálogo.                                                             |
| `request-includes-too-many-fields`   | Cada solicitud puede admitir hasta 50 campos nuevos.                                                          |
| `catalog-exceeds-fields-limit`       | El catálogo no puede tener más de 500 campos.                                                              |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
