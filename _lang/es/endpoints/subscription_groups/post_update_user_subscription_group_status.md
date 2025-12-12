---
nav_title: "PUBLICAR: Actualizar el estado del grupo de suscripción de los usuarios"
article_title: "PUBLICAR: Actualizar el estado del grupo de suscripción del usuario"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Actualizar el estado del grupo de suscripción del usuario de Braze."
---
{% api %}
# Actualizar el estado del grupo de suscripción del usuario
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/subscription/status/set
{% endapimethod %}

> Utiliza este punto final para actualizar por lotes el estado de suscripción de hasta 50 usuarios en el panel de Braze. 

Puedes acceder a la página `subscription_group_id` de un grupo de suscripción navegando a la página **Grupo de suscripción**.

Si quieres ver ejemplos o probar este punto final para **Grupos de suscripción por correo electrónico**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#8895e87e-6324-47a3-a833-adf29a258bb9 {% endapiref %}

Si quieres ver ejemplos o probar este punto final para **Grupos de suscripción SMS y RCS**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#72558b32-7dbe-4cba-bd22-a7ce513076dd {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `subscription.status.set`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='subscription status set' %}

## Cuerpo de la solicitud

{% tabs %}
{% tab SMS and RCS %}
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
   "subscription_group_id": (required, string) the id of your subscription group,
   "subscription_state": (required, string) available values are "unsubscribed" (not in subscription group) or "subscribed" (in subscription group),
   "external_id": (required*, array of strings) the external ID of the user or users, may include up to 50 IDs,
   "phone": (required*, array of strings in E.164 format) The phone number of the user (must include at least one phone number and at most 50 phone numbers),
   // SMS and RCS subscription group - one of external_id or phone is required
 }
```
\* Grupos de suscripción SMS y RCS: Solo se acepta `external_id` o `phone`.

{% endtab %}
{% tab Email %}
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
   "subscription_group_id": (required, string) the id of your subscription group,
   "subscription_state": (required, string) available values are "unsubscribed" (not in subscription group) or "subscribed" (in subscription group),
   "external_id": (required*, array of strings) the external ID of the user or users, may include up to 50 IDs,
   "email": (required*, array of strings) the email address of the user (must include at least one email and at most 50 emails),
   // Email subscription group - one of external_id or email is required
   // Note that sending an email address that is linked to multiple profiles will update all relevant profiles
 }
```
\* Grupos de suscripción por correo electrónico: Se requiere `email` o `external_id`.
{% endtab %}
{% endtabs %}

Esta propiedad no debe utilizarse para actualizar la información del perfil de un usuario. Utiliza en su lugar la propiedad [/usuarios/seguimiento]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).

{% alert tip %}
Al crear nuevos usuarios utilizando el punto final [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), puedes establecer grupos de suscripción dentro del objeto de atributos de usuario, lo que te permite crear un usuario y establecer el estado del grupo de suscripción en una sola llamada a la API.
{% endalert %}

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
|---|---|---|---|
| [`subscription_group_id`]({{site.baseurl}}/api/identifier_types/?tab=subscription%20group%20ids) | Obligatoria | Cadena | La dirección `id` de su grupo de suscripción. |
| `subscription_state` | Obligatoria | Cadena | Los valores disponibles son `unsubscribed` (no en el grupo de suscripción) o `subscribed` (en el grupo de suscripción). |
| `external_id` | Requerido* | Matriz de cadenas | El `external_id` del usuario o usuarios, puede incluir hasta 50 `id`s. |
| `email` | Requerido* | Cadena o matriz de cadenas | La dirección de correo electrónico del usuario, se puede pasar como una matriz de cadenas. Debes incluir al menos una dirección de correo electrónico (con un máximo de 50). <br><br>Si varios usuarios (`external_id`) del mismo espacio de trabajo comparten la misma dirección de correo electrónico, todos los usuarios que compartan la dirección de correo electrónico se actualizarán con los cambios del grupo de suscripción. |
| `phone` | Requerido* | Cadena en [E.164](https://en.wikipedia.org/wiki/E.164) formato | El número de teléfono del usuario, puede pasarse como una matriz de cadenas. Debe incluir al menos un número de teléfono (hasta 50). <br><br>Si varios usuarios (`external_id`) del mismo espacio de trabajo comparten el mismo número de teléfono, todos los usuarios que comparten el número de teléfono se actualizan con los mismos cambios de grupo de suscripción. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Ejemplos de solicitudes

### Correo electrónico

```
curl --location --request POST 'https://rest.iad-01.braze.com/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_group_id": "subscription_group_identifier",
  "subscription_state": "unsubscribed",
  "external_id": "external_identifier",
  "email": ["example1@email.com", "example2@email.com"]
}
'
```

### SMS y RCS

```
curl --location --request POST 'https://rest.iad-01.braze.com/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_group_id": "subscription_group_identifier",
  "subscription_state": "unsubscribed",
  "external_id": "external_identifier",
  "phone": ["+12223334444", "+11112223333"]
}
'
```

## Ejemplo de respuesta positiva

El código de estado `201` podría devolver el siguiente cuerpo de respuesta.

```json
{
    "message": "success"
}
```

{% alert important %}
El punto final solo acepta el valor `email` o `phone`, no ambos. Si se te dan las dos cosas, recibirás esta respuesta: `{"message":"Either an email address or a phone number should be provided, but not both."}`
{% endalert %}

{% endapi %}

