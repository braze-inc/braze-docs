---
nav_title: "GET: Exportar cantidad de compras"
article_title: "GET: Exportar cantidad de compras"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Exportar cantidad de compras de Braze."

---
{% api %}
# Exportar cantidad de compras
{% apimethod get %}
/purchases/quantity_series
{% endapimethod %}

> Utiliza este endpoint para devolver el número total de compras en tu aplicación durante un intervalo de tiempo.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6ac59282-d231-4317-88df-f7f12169b94e{% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `purchases.quantity_series`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='purchases product list' %}

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
|---|---|---|---|
| `ending_at` | Opcional | Fecha y hora (cadena [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Fecha en la que debe finalizar la exportación de datos. De forma predeterminada, la hora de la solicitud. |
| `length` | Obligatoria | Entero | Número máximo de días antes de `ending_at` a incluir en la serie devuelta. Debe estar comprendido entre 1 y 100 (ambos inclusive). |
| `unit` | Opcional | Cadena | Unidad de tiempo entre puntos de datos. Puede ser día u hora, por defecto día. |
| `app_id` | Opcional | Cadena | Identificador de API de la aplicación recuperado de la página [Claves de API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/). Si se excluye, se mostrarán los resultados de todas las aplicaciones de un espacio de trabajo. |
| `product` | Opcional | Cadena | Nombre del producto por el que filtrar la respuesta. Si se excluye, se mostrarán los resultados de todas las aplicaciones. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud

```
curl --location --request GET 'https://rest.iad-01.braze.com/purchases/quantity_series?length=100' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Respuesta

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "message": (required, string) the status of the export, returns 'success' when completed without errors,
  "data" : [
    {
      "time" : (string) the date as ISO 8601 date,
      "purchase_quantity" : (int) the number of items purchased in the time period
      },
    ...
  ]
}
```

{% endapi %}

{% alert tip %}
Para obtener ayuda con las exportaciones CSV y API, visita [Solución de problemas de exportación]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}
