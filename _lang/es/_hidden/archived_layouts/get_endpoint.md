---
nav_title: "GET: [Nombre del punto final]"
article_title: "Ejemplo de diseño: GET: [Nombre del punto final]"
search_tag: Endpoint
page_order: 1
excerpt_separator: ""
layout: api_page
page_type: reference
description: "En este artículo se describen el uso y los parámetros para utilizar el punto final Get [nombre del punto final] de Braze."

noindex: true
#ATTENTION: remove noindex and this alert from template
---
{% api %}
# Consulta o lista [Punto final del elemento "Gets"]

{% apimethod get %}
/sms/invalid_phone_numbers
{% endapimethod %}

<!--
This is the description of the endpoint. API descriptions usually start with "Use this endpoint to..."-->
Utiliza este punto final para obtener una lista de los números de teléfono que se han considerado "no válidos" en un periodo de tiempo determinado.

<!-- Your postman link. After you have published the endpoint to postman, you will be able get a direct link to the information in the postman docs to share here-->
{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1614a82f-510a-4c37-95a6-8207a125e487 {% endapiref %}

## Límite de velocidad

<!-- The rate limit of the endpoint. This pulls from /includes/rate_limits/ and displays specific endpoint limits based on the endpoint provided -->
{% multi_lang_include rate_limits.md endpoint='default' %}

## Parámetros de la solicitud

<!--This is where you can give more information about your endpoint parameters. -->

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| ----------|-----------| ----------|----- |
| `start_date` | Opcional <br>(ver nota) | Cadena en formato AAAA-MM-DD| Fecha de inicio del intervalo para recuperar números de teléfono no válidos, debe ser anterior a `end_date`. La API lo considera medianoche en hora UTC. |
| `end_date` | Opcional <br>(ver nota) | Cadena en formato AAAA-MM-DD | Fecha final del intervalo para recuperar números de teléfono no válidos. La API lo considera medianoche en hora UTC. |
| `limit` | Opcional | Entero | Campo opcional para limitar el número de resultados devueltos. De forma predeterminada, 100, el máximo es 500. |
| `offset` | Opcional | Entero | Punto de inicio opcional de la lista desde el que recuperar. |
| `phone_numbers` | Opcional <br>(ver nota) | Matriz de cadenas en formato e.164  | Si lo proporcionas, te devolveremos el número de teléfono si se comprueba que no es válido. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Debes proporcionar un `start_date` y un `end_date` O `phone_numbers`. Si proporcionas los tres, `start_date`, `end_date`, y `phone_numbers`, damos prioridad a los números de teléfono indicados y no tenemos en cuenta el intervalo de fechas.
{% endalert %}

## Ejemplo de solicitud

<!--The following example demonstrates a request that will pull a list of phone numbers that have been deemed invalid via the API:-->
```
curl --location --request GET 'https://rest.iad-01.braze.com/sms/invalid_phone_numbers?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&phone_numbers[]=12345678901' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Respuesta

<!-- An example response that defines the different variables returned-->
```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "sms": [
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
    },
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
    },
    {
      "phone": (string) phone number in e.164 format,
      "invalid_detected_at": (string) the time the invalid number was detected in ISO 8601
    }
  ],
  "message": "success"
}
```

{% endapi %}
