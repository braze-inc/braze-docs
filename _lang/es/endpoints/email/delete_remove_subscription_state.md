---
nav_title: "DELETE: Eliminar el estado de suscripción por dirección de correo electrónico o número de teléfono"
article_title: "DELETE: Eliminar estado de suscripción por dirección de correo electrónico o número de teléfono"
search_tag: Endpoint
page_order: 0
hidden: true
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles sobre el punto final de Braze Eliminar estado de suscripción por dirección de correo electrónico o número de teléfono."

---

{% api %}
# Eliminar el estado de suscripción por dirección de correo electrónico o número de teléfono
{% apimethod delete %}
/users/subscription
{% endapimethod %}

> Utilice este punto final para eliminar el valor del estado de suscripción basado en una dirección de correo electrónico o un número de teléfono.

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --- | --- | --- | --- |
| `email` | Sí | Cadena | La dirección de correo electrónico del usuario (debe incluir al menos una dirección y un máximo de 50 direcciones). |
| `phone` | Sí | Cadena | El número de teléfono del usuario (debe incluir al menos un número de teléfono y como máximo 50 números de teléfono). Le recomendamos que lo facilite en formato E.164. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  {phone: "+12125551212"},
  {email: "dont.spam@me.com"},
  {phone: "+17185551212"}
}
```

## Respuesta

```json
{
  "status": "The emails and/or phone numbers have been queued for deletion",
  "message": "success"
}
```

{% endapi %}
