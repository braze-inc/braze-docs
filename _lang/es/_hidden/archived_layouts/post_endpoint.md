---
nav_title: "POST: [Nombre del punto final]"
article_title: "Ejemplo de diseño: PUBLICAR: Seguimiento del usuario"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
excerpt_separator: ""

description: "En este artículo se describen los detalles sobre el uso de este punto final POST [nombre del punto final] de Braze."

noindex: true
#ATTENTION: remove noindex and this alert from template
---
{% api %}
# [Nombre del punto final]

{% apimethod post %}
/sms/invalid_phone_numbers/remove
{% endapimethod %}

<!--
This is the description of the endpoint. API descriptions usually start with "Use this endpoint to..."-->
Utiliza este punto final para eliminar números de teléfono "no válidos" de la lista de no válidos en Braze. Se puede utilizar para volver a validar números de teléfono después de haberlos marcado como no válidos.

<!-- Your postman link. Once you have published the endpoint to postman, you will be able get a direct link to the information in the postman docs to share here-->
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1614a82f-510a-4c37-95a6-8207a125e487 {% endapiref %}

## Límite de velocidad

<!-- The rate limit of the endpoint. This pulls from /includes/rate_limits/ and displays specific endpoint limits based on the endpoint provided -->
{% multi_lang_include rate_limits.md endpoint='default' %}

## Cuerpo de la solicitud

<!--This is where you can give more information about your endpoint request body. -->

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "phone_numbers": (required, array of string in e.164 format)
}
```

### Parámetros de la solicitud

<!--This is a place for you to describe additional details for the parameters in the request body.-->

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| ----------|-----------| ---------|------ |
| `phone_number` | Obligatoria | Matriz de cadenas en formato e.164  | Un conjunto de hasta 50 números de teléfono para modificar. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud

<!--The following example demonstrates a request that will remove specific SMS numbers from Braze's invalid phone number list via the API:-->

```
curl --location --request POST 'https://rest.iad-01.braze.com/sms/invalid_phone_numbers/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "phone_numbers" : ["12183095514","14255551212"]
}'
```
{% endapi %}
