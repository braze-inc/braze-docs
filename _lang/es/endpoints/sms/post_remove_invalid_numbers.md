---
nav_title: "PUBLICAR: Eliminar números de teléfono no válidos"
article_title: "PUBLICAR: Eliminar números de teléfono no válidos"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Eliminar números de teléfono no válidos de Braze."

---
{% api %}
# Eliminar números de teléfono no válidos
{% apimethod post %}
/sms/invalid_phone_numbers/remove
{% endapimethod %}

> Utilice este punto final para eliminar números de teléfono "inválidos" de nuestra lista de inválidos.

Se puede utilizar para volver a validar números de teléfono después de haberlos marcado como no válidos.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#76495aac-8c2d-4e1a-8cac-12e3856ab1d3 {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `sms.invalid_phone_numbers.remove`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='default' %}

## Cuerpo de la solicitud

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "phone_numbers": (required, array of string in e.164 format)
}
```

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| ----------|-----------| ---------|------ |
| `phone_number` | Obligatoria | Matriz de cadenas en formato e.164  | Un conjunto de hasta 50 números de teléfono para modificar. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud

```
curl --location --request POST 'https://rest.iad-01.braze.com/sms/invalid_phone_numbers/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "phone_numbers" : ["12183095514","14255551212"]
}'
```

{% endapi %}
