---
nav_title: "GET: Consultar correos electrónicos de rebote duro"
article_title: "GET: Consultar correos electrónicos de rebote duro"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Consultar o enumerar las direcciones de correo electrónico de rebote duro de Braze."

---
{% api %}
# Consultar correos electrónicos de rebote duro
{% apimethod get %}
/email/hard_bounces
{% endapimethod %}

> Utiliza este punto final para obtener una lista de direcciones de correo electrónico que han "rebotado duramente" tus mensajes de mensajería en un plazo de tiempo determinado.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7c2ef84f-ddf5-451a-a72c-beeabc06ad9d {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `email.hard_bounces`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| ----------|-----------| ----------|----- |
| `start_date` | Opcional\*. | Cadena en formato AAAA-MM-DD| \*Se requiere uno de `start_date` o `email`. Es la fecha de inicio del intervalo para recuperar rebotes duros y debe ser anterior a `end_date`. La API lo considera medianoche en hora UTC. |
| `end_date` | Obligatoria | Cadena en formato AAAA-MM-DD | Fecha de finalización del intervalo para recuperar rebotes duros. La API lo considera medianoche en hora UTC. |
| `limit` | Opcional | Entero | Campo opcional para limitar el número de resultados devueltos. De forma predeterminada, 100, el máximo es 500. |
| `offset` | Opcional | Entero | Punto de inicio opcional de la lista desde el que recuperar. |
| `email` | Opcional\*. | Cadena | \*Se requiere uno de `start_date` o `email`. Si se proporciona, devolveremos si el usuario ha rebotado duro o no. Comprueba que las cadenas de correo electrónico tienen el formato adecuado. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert important %}
Debes proporcionar un `end_date`, y un `email` o un `start_date`. Si proporcionas los tres, `start_date`, `end_date` y un `email`, damos prioridad a los correos electrónicos proporcionados y no tenemos en cuenta el intervalo de fechas.
{% endalert %}

Si tu intervalo de fechas tiene más del número `limit` de rebotes duros, tendrás que hacer varias llamadas a la API, aumentando cada vez el `offset` hasta que una llamada devuelva menos de `limit` o cero resultados. Incluir los parámetros `offset` y `limit` con `email` puede devolver una respuesta vacía.

## Ejemplo de solicitud
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/hard_bounces?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Respuesta
Las entradas aparecen en orden descendente.

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "emails": [
    {
      "email": (string) an email that has hard bounced,
      "hard_bounced_at": (string) the time the email hard bounced in ISO 8601
    },
    {
      "email": (string) an email that has hard bounced,
      "hard_bounced_at": (string) the time the email hard bounced in ISO 8601
    },
    {
      "email": (string) an email that has hard bounced,
      "hard_bounced_at": (string) the time the email hard bounced in ISO 8601
    }
  ],
  "message": "success"
}
```
{% endapi %}
