---
nav_title: "PUBLICAR: Actualizar estado del grupo de suscripción de usuarios v2"
alias: /post_update_user_subscription_group_status_v2/
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Actualizar el estado del grupo de suscripción del usuario (V2) de Braze."

platform: API
channel:
  - Email
---

{% api %}
# Actualizar el estado del grupo de suscripción del usuario (V2)
{% apimethod post %}
/v2/subscription/status/set
{% endapimethod %}

> Utilice este punto final para actualizar por lotes el estado de suscripción de hasta 50 usuarios en el panel Braze. 

Puede acceder a la página `subscription_group_id` de un grupo **de** suscripción accediendo a la página **Grupo de suscripciones**.

Si desea ver ejemplos o probar este punto final para **Grupos de suscripción por correo electrónico**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#b1b9a0e0-6329-4df2-a465-53347f410662 {% endapiref %}

Si quieres ver ejemplos o probar este punto final para **Grupos de Suscripción SMS**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#81a5fe65-588b-4b61-82d8-5ce68b681409 {% endapiref %}

Si quieres ver ejemplos o probar este punto final para **Grupos de WhatsApp**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#81a5fe65-588b-4b61-82d8-5ce68b681409 {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `subscription.status.set`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='subscription status set' %}

## Cuerpo de la solicitud

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "subscription_groups":[
    {
      "subscription_group_id": (required, string),
      "subscription_state": (required, string)
      "external_ids": (required*, array of strings),
      "emails": (required*, array of strings),
      "phones": (required*, array of strings in E.164 format),
    }
  ]
}
```
\* Tenga en cuenta que no puede incluir los parámetros `emails` y `phones`. Además, `emails`, `phones` y `external_ids` pueden enviarse individualmente.

{% alert tip %}
Al crear nuevos usuarios utilizando el [punto final`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), puedes establecer grupos de suscripción dentro del objeto de atributos de usuario, lo que te permite crear un usuario y establecer el estado del grupo de suscripción en una sola llamada a la API.
{% endalert %}

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
|---|---|---|---|
| [`subscription_group_id`]({{site.baseurl}}/api/identifier_types/?tab=subscription%20group%20ids) | Obligatoria | Cadena | La dirección `id` de su grupo de suscripción. |
| `subscription_state` | Obligatoria | Cadena | Los valores disponibles son `unsubscribed` (no en el grupo de suscripción) o `subscribed` (en el grupo de suscripción). |
| `external_ids` | Requerido* | Matriz de cadenas | El `external_id` del usuario o usuarios, puede incluir hasta 50 `id`s. |
| `emails` | Requerido* | Cadena o matriz de cadenas | La dirección de correo electrónico del usuario, se puede pasar como una matriz de cadenas. Debe incluir al menos una dirección de correo electrónico (con un máximo de 50). <br><br>Si varios usuarios (`external_id`) del mismo espacio de trabajo comparten la misma dirección de correo electrónico, todos los usuarios que comparten la dirección de correo electrónico se actualizan con los cambios del grupo de suscripción. |
| `phones` | Requerido* | Cadena en [E.164](https://en.wikipedia.org/wiki/E.164) formato | Los números de teléfono del usuario, se pueden pasar como una matriz de cadenas. Debe incluir al menos un número de teléfono (hasta 50). <br><br>Si varios usuarios (`external_id`) del mismo espacio de trabajo comparten el mismo número de teléfono, todos los usuarios que comparten el número de teléfono se actualizan con los mismos cambios de grupo de suscripción.|
| `use_double_opt_in_logic` | Opcional | Booleano | Si este parámetro se omite o se establece en `false`, los usuarios no entrarán en el flujo de trabajo de doble adhesión voluntaria por SMS. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert note %}
Tenga en cuenta que no puede incluir los parámetros `emails` y `phones`. Además, `emails`, `phones` y `external_ids` pueden enviarse individualmente.
{% endalert %}

### Ejemplos de solicitudes

En el siguiente ejemplo, se utiliza `external_id` para realizar una llamada API para correo electrónico y SMS.

```
curl --location --request POST 'https://rest.iad-01.braze.com/v2/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_groups":[
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "external_ids":["example-user","example1@email.com"]
    },
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "external_ids":["example-user","example1@email.com"]
    }
  ]
}
```

## Correo electrónico

```
curl --location --request POST 'https://rest.iad-01.braze.com/v2/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_groups":[
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "emails":["example1@email.com","example2@email.com"]
    }
  ]
}
'
```

## SMS y WhatsApp

```
curl --location --request POST 'https://rest.iad-01.braze.com/v2/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_groups":[
    {
      "subscription_group_id":"subscription_group_identifier",
      "subscription_state":"subscribed",
      "phones":["+12223334444","+15556667777"]
    }
  ]
}
'
```

{% endapi %}
