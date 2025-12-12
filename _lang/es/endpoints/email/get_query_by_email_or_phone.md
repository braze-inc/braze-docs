---
nav_title: "GET: Estado de suscripción a la lista con dirección de correo electrónico o número de teléfono"
article_title: "GET: Estado de suscripción a la lista con dirección de correo electrónico o número de teléfono"
search_tag: Endpoint
page_order: 2
hidden: true
layout: api_page
page_type: reference
description: "Este artículo describe los detalles sobre el estado de suscripción a la lista con una dirección de correo electrónico o un número de teléfono del punto final Braze."

---
{% api %}
# Estado de suscripción a la lista con una dirección de correo electrónico o un número de teléfono
{% apimethod get %}
/users/subscription
{% endapimethod %}

> Utiliza este punto final para devolver el valor del estado de suscripción basado en una dirección de correo electrónico o un número de teléfono.

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --- | --- | --- | --- |
| `email` | Sí | Cadena | La dirección de correo electrónico del usuario (debe incluir al menos una dirección y un máximo de 50 direcciones). |
| `phone` | Sí | Cadena | El número de teléfono del usuario (debe incluir al menos un número de teléfono y como máximo 50 números de teléfono). Le recomendamos que lo facilite en formato E.164. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud
```
curl --location --request GET 'https://rest.iad-01.braze.com/users/subscriptions?phone=+12123355555&email=example%40braze.com' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Respuesta

Las entradas aparecen en orden descendente.

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "emails": [
    {
      "email": "example@braze.com",
      "email_subscribe": {
        "email_subscription_event_date": "2019-11-20T19:58:04.825Z",
        "email_subscription_state": "Subscribed"
      },
      "subscription_group": [
        {
          "subscription_group_id": "5f5536d2a76e0f4e323a1234",
          "subscription_group_event_date": "2021-03-11T21:29:22.347Z",
          "subscription_group_state": "Unsubscribed"
        }
      ],
      "hard_bounced_at": null,
      "spam_at": null
    }
  ],
	"phone": [{
		"phone": "+12123355555",
		"subscription_group": [{
			"subscription_group_id": "3f5536d2a76e0f4e323a5555",
			"subscription_group_state": "Subsscribed",
			"subscription_group_event_date": "2021-03-11T21:29:22.347Z"
		}]
	}],
	"message": "success"
}
```

{% endapi %}
