---
nav_title: "GET: Consultar lista de direcciones de correo electrónico dadas de baja"
article_title: "GET: Consulta la lista de direcciones de correo electrónico no suscritas"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles sobre el punto final Braze Recuperar lista de correo electrónico o consulta de cancelaciones de suscripción."

---
{% api %}
# Consultar lista de direcciones de correo electrónico dadas de baja
{% apimethod get %}
/email/unsubscribes
{% endapimethod %}

> Utiliza este endpoint para devolver los últimos correos electrónicos que se han dado de baja durante el periodo de tiempo comprendido entre `start_date` y `end_date`. Para obtener un historial completo del estado de la suscripción, utiliza [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) para hacer un seguimiento de estos datos.

Puedes utilizar este punto final para configurar una sincronización bidireccional entre Braze y otros sistemas de correo electrónico o tu propia base de datos.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d2966b81-188a-407b-ba7e-e6c252c44b4a {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `email.unsubscribe`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| ----------|-----------| ---------|------ |
| `start_date` | Opcional <br>(ver nota) | Cadena en formato AAAA-MM-DD| Fecha de inicio del intervalo para recuperar las cancelaciones de suscripción, debe ser anterior a end_date. La API la trata como medianoche en hora UTC. |
| `end_date` | Opcional <br>(ver nota) | Cadena en formato AAAA-MM-DD | Fecha de finalización del intervalo para recuperar las bajas. La API lo considera medianoche en hora UTC. |
| `limit` | Opcional | Entero | Campo opcional para limitar el número de resultados devueltos. De forma predeterminada, 100, el máximo es 500. |
| `offset` | Opcional | Entero | Punto de inicio opcional de la lista desde el que recuperar. |
| `sort_direction` | Opcional | Cadena | Introduce el valor `asc` para ordenar las bajas de la más antigua a la más reciente. Introduce `desc` para ordenar de más reciente a más antiguo. Si no se incluye `sort_direction`, el orden predeterminado es de más reciente a más antiguo. |
| `email` | Opcional <br>(ver nota) | Cadena | Si se proporciona, devolveremos si el usuario se ha dado de baja o no. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Debes proporcionar un valor para `end_date`, así como para `email` o `start_date`.
{% endalert %}

Si tu intervalo de fechas tiene más de `limit` número de cancelaciones de suscripción, tendrás que hacer varias llamadas a la API, aumentando cada vez el `offset` hasta que una llamada devuelva menos de `limit` o cero resultados.

## Ejemplo de solicitud
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/unsubscribes?start_date=2020-01-01&end_date=2020-02-01&limit=1&offset=1&sort_direction=desc&email=example@braze.com' \
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
      "email": (string) an email that has been unsubscribed,
      "unsubscribed_at": (string) the time the email was unsubscribed in ISO 8601
    },
    {
      "email": (string) an email that has been unsubscribed,
      "unsubscribed_at": (string) the time the email was unsubscribed in ISO 8601
    },
    {
      "email": (string) an email that has been unsubscribed,
      "unsubscribed_at": (string) the time the email was unsubscribed in ISO 8601
    }
  ],
  "message": "success"
}
```
{% endapi %}
