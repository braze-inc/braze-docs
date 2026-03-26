---
nav_title: "POST: Actualizar el estado del grupo de suscripción de los usuarios"
article_title: "POST: Actualizar el estado del grupo de suscripción del usuario"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto de conexión Actualizar el estado del grupo de suscripción del usuario de Braze."
---
{% api %}
# Actualizar el estado del grupo de suscripción del usuario
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/subscription/status/set
{% endapimethod %}

> Utiliza este punto de conexión para actualizar por lotes el estado de suscripción de hasta 50 usuarios en el panel de Braze.

Puedes acceder al `subscription_group_id` de un grupo de suscripción navegando a la página **Grupo de suscripción**.

Si quieres ver ejemplos o probar este punto de conexión para **grupos de suscripción por correo electrónico**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#8895e87e-6324-47a3-a833-adf29a258bb9 {% endapiref %}

Si quieres ver ejemplos o probar este punto de conexión para **grupos de suscripción SMS y RCS**:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#72558b32-7dbe-4cba-bd22-a7ce513076dd {% endapiref %}

## Requisitos previos

Para utilizar este punto de conexión, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key/) con el permiso `subscription.status.set`.

{% alert note %}
Si te interesa utilizar este punto de conexión con [grupos de suscripción de LINE]({{site.baseurl}}/user_guide/message_building_by_channel/line/line_users/subscription_groups/), ponte en contacto con tu administrador del éxito del cliente.
{% endalert %}

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
   "use_double_opt_in_logic": (optional, boolean) defaults to `false`; when `subscription_state` is "subscribed", set to `true` to enter the user into the SMS double opt-in workflow,
   // SMS and RCS subscription group - you must include one of external_id or phone
 }
```
\* Grupos de suscripción SMS y RCS: Braze solo acepta `external_id` o `phone`.

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
   // Email subscription group - you must include one of external_id or email
   // Note that sending an email address that is linked to multiple profiles updates all relevant profiles
 }
```
\* Grupos de suscripción por correo electrónico: debes incluir `email` o `external_id`.
{% endtab %}
{% endtabs %}

Esta propiedad no debe utilizarse para actualizar la información del perfil de un usuario. Utiliza en su lugar la propiedad [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).

{% alert tip %}
**Añadir usuarios existentes a un grupo de suscripción:** Este punto de conexión es la forma recomendada de rellenar o actualizar de forma masiva la pertenencia a grupos de suscripción para usuarios existentes. Puedes pasar hasta 50 `external_id`s, direcciones de correo electrónico o números de teléfono por solicitud. Los usuarios también pueden actualizar su propio estado de suscripción a través de un enlace de [centro de preferencias de correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/).

**Crear nuevos usuarios con un grupo de suscripción:** Al crear nuevos usuarios utilizando el punto de conexión [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), puedes establecer grupos de suscripción dentro del objeto de atributos de usuario, lo que te permite crear un usuario y establecer el estado del grupo de suscripción en una sola llamada a la API.
{% endalert %}

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
|---|---|---|---|
| [`subscription_group_id`]({{site.baseurl}}/api/identifier_types/?tab=subscription%20group%20ids) | Obligatoria | Cadena | El `id` de tu grupo de suscripción. |
| `subscription_state` | Obligatoria | Cadena | Los valores disponibles son `unsubscribed` (no en el grupo de suscripción) o `subscribed` (en el grupo de suscripción). |
| `external_id` | Obligatoria* | Matriz de cadenas | El `external_id` del usuario o usuarios, puede incluir hasta 50 `id`s. |
| `email` | Obligatoria* | Cadena o matriz de cadenas | La dirección de correo electrónico del usuario, se puede pasar como una matriz de cadenas. Debe incluir al menos una dirección de correo electrónico (con un máximo de 50). <br><br>Si varios usuarios (`external_id`) del mismo espacio de trabajo comparten la misma dirección de correo electrónico, Braze actualiza a todos los usuarios que comparten la dirección de correo electrónico con los cambios del grupo de suscripción. |
| `phone` | Obligatoria* | Cadena en formato [E.164](https://en.wikipedia.org/wiki/E.164) | El número de teléfono del usuario, puede pasarse como una matriz de cadenas. Debe incluir al menos un número de teléfono (hasta 50). <br><br>Si varios usuarios (`external_id`) del mismo espacio de trabajo comparten el mismo número de teléfono, Braze actualiza a todos los usuarios que comparten el número de teléfono con los mismos cambios de grupo de suscripción. |
| `use_double_opt_in_logic` | Opcional | Booleano | Se aplica solo a grupos de suscripción SMS; se ignora para correo electrónico y otros tipos de grupos de suscripción. El valor predeterminado es `false` si se omite. Para grupos de suscripción SMS, establécelo en `true` para que el usuario entre en el flujo de trabajo de [doble adhesión voluntaria de SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/double_opt_in/) cuando su estado de suscripción se establezca en `subscribed`. Si este parámetro se omite o se establece en `false`, los usuarios se suscriben sin entrar en el flujo de trabajo de doble adhesión voluntaria. |
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

## Ejemplo de respuesta correcta

El código de estado `201` podría devolver el siguiente cuerpo de respuesta.

```json
{
    "message": "success"
}
```

{% alert important %}
El punto de conexión solo acepta el valor `email` o `phone`, no ambos. Si proporcionas ambos, recibirás esta respuesta: `{"message":"Either an email address or a phone number should be provided, but not both."}`
{% endalert %}

{% endapi %}