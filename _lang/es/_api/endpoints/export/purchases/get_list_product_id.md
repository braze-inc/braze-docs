---
nav_title: "GET: Exportar ID de productos"
article_title: "GET: Exportar ID de productos"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Exportar ID de productos de Braze."

---
{% api %}
# Exportar ID de productos
{% apimethod get %}
/purchases/product_list
{% endapimethod %}

> Utiliza este punto final para devolver una lista paginada de ID de productos.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#dff4ed40-81f5-451d-9d44-accc0e932285{% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `purchases.product_list`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='purchases product list' %}

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
|---|---|---|---|
| `page` | Opcional | Cadena | La página de su lista de productos que desea ver. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud

{% raw %}
```
https://rest.iad-01.braze.com/purchases/product_list?page=1
```
{% endraw %}

## Respuesta

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "products": [
    "product_name" (string), the name of the product
  ],
  "message": "success"
}
```

{% endapi %}

{% alert tip %}
Para obtener ayuda con las exportaciones CSV y API, visita [Solución de problemas de exportación]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}
