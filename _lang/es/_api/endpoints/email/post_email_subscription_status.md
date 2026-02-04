---
nav_title: "PUBLICAR: Cambiar el estado de la suscripción por correo electrónico"
article_title: "PUBLICAR: Cambiar el estado de la suscripción por correo electrónico"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Cambiar el estado de la suscripción por correo electrónico del usuario de Braze."

---
{% api %}
# Cambiar el estado de la suscripción por correo electrónico
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/email/status
{% endapimethod %}

> Utilice este punto final para establecer el estado de suscripción de correo electrónico para sus usuarios.

Los usuarios pueden ser `opted_in`, `unsubscribed`, o `subscribed` (sin opción específica de inclusión o exclusión).

Puede establecer el estado de suscripción por correo electrónico para una dirección de correo electrónico que aún no esté asociada a ninguno de sus usuarios dentro de Braze. Cuando esa dirección de correo electrónico se asocie posteriormente a un usuario, se establecerá automáticamente el estado de suscripción de correo electrónico que usted cargó.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#be852462-0cda-4a48-b68b-85bd8a9f2147 {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `email.status`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='default' %}

## Cuerpo de la solicitud

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": "example@braze.com",
  "subscription_state": "subscribed"
}
```

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
| `email` | Obligatoria | Cadena o matriz | Cadena de direcciones de correo electrónico a modificar, o una matriz de hasta 50 direcciones de correo electrónico a modificar. |
| `subscription_state` | Obligatoria | Cadena | O bien "suscrito", "dado de baja", o bien "opted_in". |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/status' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "email": "example@braze.com",
  "subscription_state": "subscribed"
}'
```


{% endapi %}
