---
nav_title: "GET: Lista de plantillas de correo electrónico disponibles"
article_title: "GET: Lista de plantillas de correo electrónico disponibles"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Enumerar las plantillas de correo electrónico disponibles de Braze."

---
{% api %}
# Lista de plantillas de correo electrónico disponibles
{% apimethod get %}
/templates/email/list
{% endapimethod %}

> Utilice este punto final para obtener una lista de las plantillas de correo electrónico disponibles en su cuenta Braze.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#eec24bf4-a3f4-47cb-b4d8-bb8f03964cca {% endapiref %}

## Requisitos previos
Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/api_key/) con el permiso `templates.email.list`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
|---|---|---|---|
| `modified_after`  | Opcional | Cadena en formato [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)  | Recupera solo las plantillas actualizadas a partir de la hora indicada o después. |
| `modified_before`  |  Opcional | Cadena en formato [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)  | Recuperar sólo las plantillas actualizadas a la hora indicada o antes. |
| `limit` | Opcional | Número positivo | Número máximo de plantillas a recuperar. Por defecto 100 si no se indica, con un valor máximo aceptable de 1000. |
| `offset`  |  Opcional | Número positivo | Número de plantillas que se omiten antes de devolver el resto de plantillas que se ajustan a los criterios de búsqueda. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud
```
curl --location --request GET 'https://rest.iad-01.braze.com/templates/email/list?modified_after=2020-01-01T01:01:01.000000&modified_before=2020-02-01T01:01:01.000000&limit=1&offset=0' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Respuesta 

{% alert important %}
Las plantillas creadas con el editor de arrastrar y soltar para correo electrónico no se proporcionan en esta respuesta.
{% endalert %}

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "count": the number of templates returned
  "templates": [template with the following properties]:
    "email_template_id": (string) your email template's API Identifier,
    "template_name": (string) the name of your email template,
    "created_at": (string) the time the email was created at in ISO 8601,
    "updated_at": (string) the time the email was updated in ISO 8601,
    "tags": (array of strings) tags appended to the template
}
```
{% endapi %}



