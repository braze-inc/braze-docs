---
nav_title: "GET: Enumerar múltiples detalles de elementos del catálogo"
article_title: "GET: Listar varios detalles de elementos del catálogo"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Enumerar múltiples detalles de elementos del catálogo de Braze."

---
{% api %}
# Enumerar múltiples detalles de elementos del catálogo
{% apimethod get %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> Utilice este punto final para devolver varios elementos del catálogo y su contenido.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#63a19dd5-10e0-4649-bdf0-097216748bbb {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `catalogs.get_items`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='synchronous catalog item' %}

## Parámetros de la ruta

| Parámetro | Obligatoria | Tipo de datos | Descripción |
|---|---|---|---|
| `catalog_name` | Obligatoria | Cadena | Nombre del catálogo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Parámetros de consulta

Ten en cuenta que cada llamada a este punto final devolverá 50 elementos. Para un catálogo con más de 50 artículos, utilice la cabecera `Link` para recuperar los datos en la página siguiente, como se muestra en el siguiente ejemplo de respuesta.

| Parámetro | Obligatoria | Tipo de datos | Descripción |
|---|---|---|---|
| `cursor` | Opcional | Cadena | Determina la paginación de los elementos del catálogo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Parámetros de la solicitud

No hay cuerpo de petición para este punto final.

## Ejemplos de solicitudes

### Sin cursor

```
curl --location --request GET 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

### Con cursor

```
curl --location --request GET 'https://rest.iad-03.braze.com/catalogs/restaurants/items?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Respuesta

Existen tres respuestas de código de estado para este punto final: `200`, `400` y `404`.

### Ejemplo de respuesta positiva

El código de estado `200` podría devolver la siguiente cabecera y cuerpo de respuesta.

{% alert note %}
La cabecera `Link` no existirá si el catálogo tiene menos o igual a 50 artículos. Para las llamadas sin cursor, `prev` no se mostrará. Al consultar la última página de elementos, `next` no se mostrará.
{% endalert %}

```
Link: </catalogs/all_restaurants/items?cursor=c2tpcDow>; rel="prev",</catalogs/all_restaurants/items?cursor=c2tpcDoxMDA=>; rel="next"
```

```json
{
  "items": [
    {
      "id": "restaurant1",
      "Name": "Restaurant1",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 5,
      "Loyalty_Program": true,
      "Open_Time": "2022-11-02T09:03:19.967Z"
    },
    {
      "id": "restaurant2",
      "Name": "Restaurant2",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 10,
      "Loyalty_Program": true,
      "Open_Time": "2022-11-02T09:03:19.967Z"
    },
    {
      "id": "restaurant3",
      "Name": "Restaurant3",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 5,
      "Loyalty_Program": false,
      "Open_Time": "2022-11-02T09:03:19.967Z"
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
      "id": "invalid-cursor",
      "message": "'cursor' is not valid",
      "parameters": [
        "cursor"
      ],
      "parameter_values": [
        "bad-cursor"
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
| `invalid-cursor` | Compruebe que su `cursor` es válido. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
