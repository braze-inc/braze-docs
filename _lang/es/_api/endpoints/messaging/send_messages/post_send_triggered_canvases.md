---
nav_title: "PUBLICAR: Envía mensajes Canvas utilizando la entrega desencadenada por API"
article_title: "PUBLICAR: Envía mensajes Canvas mediante la entrega desencadenada por API"
search_tag: Punto de conexión
page_order: 4
layout: api_page
page_type: reference
description: "Este artículo describe en detalle el punto final Braze de Enviar lienzos mediante entrega desencadenada por API."

---
{% api %}
# Envía mensajes Canvas utilizando la entrega desencadenada por API
{% apimethod postcore_endpoint|https://www.braze.com/docs/core_endpoints  %}
/canvas/trigger/send
{% endapimethod %}

> Utiliza este punto final para enviar mensajes Canvas con entrega desencadenada por la API.

La entrega desencadenada por la API te permite almacenar el contenido de los mensajes en el panel Braze, al tiempo que dictas cuándo se envía un mensaje y a quién mediante tu API.

Para poder enviar mensajes con este punto final, debes tener un [ID de Canvas]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier) (que se crea cuando construyes un Canvas).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c9a8a5fe-a101-4755-99f2-73aa8fc146fe {% endapiref %}

## Requisitos previos

Para utilizar este punto final, deberás generar una clave de API con el permiso `canvas.trigger.send`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='send endpoints' category='send messages endpoints' %}

## Cuerpo de la solicitud

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) see Canvas identifier,
  "context": (optional, object) personalization key-value pairs that apply to all users in this request,
  "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if `recipients` is omitted,
  "audience": (optional, connected audience object) see connected audience,
  // Including 'audience' will only send to users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to 'false', message sends to the entire segment targeted by the Canvas)
    [{
      // Either "external_user_id" or "user_alias" or "email" is required. Requests must specify only one.
      "user_alias": (optional, user alias object) user alias of user to receive message,
      "external_user_id": (optional, string) external identifier of user to receive message,
      "email": (optional, string) email address of user to receive message,
      "prioritization": (optional, array) prioritization array; required when using email,
      "context": (optional, object) personalization key-value pairs that apply to this user (these key-value pairs override any keys that conflict with the parent `context`)
      "send_to_existing_only": (optional, boolean) defaults to true, can't be used with user aliases
      "attributes": (optional, object) fields in the attributes object create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values are overwritten
    }],
    ...
}
```

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
|`canvas_id`| Obligatoria | Cadena | Ver [identificador de Canvas]({{site.baseurl}}/api/identifier_types/). |
|`context`| Opcional | Objeto | Esto incluye las propiedades de entrada de Canvas. Los pares clave-valor de personalización se aplican a todos los usuarios de esta solicitud. El objeto de contexto puede tener un tamaño máximo de 50 KB. |
|`broadcast`| Opcional | Booleano | Debes establecer`broadcast`  en verdadero cuando envíes un mensaje a todo el segmento configurado como audiencia objetivo de Canvas en el panel de Braze. Este parámetro está predeterminado como falso (a 31 de agosto de 2017). <br><br> Si `broadcast` tiene el valor true, no se puede incluir una lista `recipients`. Sin embargo, ten cuidado al configurar `broadcast: true`, ya que si lo haces involuntariamente puede que envíes tu mensaje a una audiencia mayor de la esperada. |
|`audience`| Opcional| Objeto de audiencia conectado | Ver [Audiencia conectada]({{site.baseurl}}/api/objects_filters/connected_audience/). Cuando incluyes `audience`, el mensaje solo se envía a los usuarios que coinciden con los filtros definidos, como los atributos personalizados y los estados de suscripción. |
|`recipients`| Opcional | Matriz | Ver [objeto de destinatarios]({{site.baseurl}}/api/objects_filters/recipient_object/). <br><br>Si no se proporciona y`broadcast`  está configurado en `true`, el mensaje se envía a todo el segmento configurado como audiencia objetivo de Canvas en el panel de Braze.<br><br> La matriz `recipients` puede contener hasta 50 objetos, cada uno de los cuales contiene una única cadena `external_user_id` y un objeto `canvas_entry_properties`. Esta llamada requiere un `external_user_id`, `user_alias`, o `email`. Las solicitudes deben especificar sólo una. <br><br>Si`email`  es el identificador, debes incluir[`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify#identifying-users-by-email)  en el objeto destinatarios. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Ejemplo de solicitud
```
curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/send' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "context": {"product_name" : "shoes", "product_price" : 79.99},
  "broadcast": false,
  "audience": {
    "AND": [
      {
        "custom_attribute": {
          "custom_attribute_name": "eye_color",
          "comparison": "equals",
          "value": "blue"
        }
      },
      {
        "custom_attribute": {
          "custom_attribute_name": "favorite_foods",
          "comparison": "includes_value",
          "value": "pizza"
        }
      },
      {
        "OR": [
          {
            "custom_attribute": {
              "custom_attribute_name": "last_purchase_time",
              "comparison": "less_than_x_days_ago",
              "value": 2
            }
          },
          {
            "push_subscription_status": {
              "comparison": "is",
              "value": "opted_in"
            }
          }
        ]
      },
      {
        "email_subscription_status": {
          "comparison": "is_not",
          "value": "subscribed"
        }
      },
      {
        "last_used_app": {
          "comparison": "after",
          "value": "2019-07-22T13:17:55+0000"
        }
      }
    ]
  },
  "recipients": [
    {
      "user_alias": {
        "alias_name" : "example_name",
        "alias_label" : "example_label"
      },
      "external_user_id": "user_identifier",
      "send_to_existing_only": true,
      "attributes": {
          "first_name" : "Alex"
      }
    }
  ]
}'
```

## Detalles de la respuesta

Las respuestas de los puntos finales de envío de mensajes incluyen el mensaje`dispatch_id`para poder hacer referencia al envío del mensaje. El `dispatch_id` es el ID del envío del mensaje (ID único para cada "transmisión" enviada desde la plataforma Braze). Echa un vistazo [al comportamiento de Dispatch ID]({{site.baseurl}}/help/help_articles/data/dispatch_id/) para obtener más información.

### Ejemplo de respuesta positiva

El código de estado `201` podría devolver el siguiente cuerpo de respuesta. Si el Canvas está archivado, detenido o en pausa, no se envía a través de este punto final.

```
{
  "notice": "The Canvas is paused. Resume the Canvas to ensure trigger requests will take effect.",
  "dispatch_id": "example_dispatch_id",
  "message": "success"
}
```

Si tu Canvas está archivado, verás este`notice`mensaje: "El Canvas" está archivado. Desarchiva el Canvas para asegurarte de que las solicitudes de desencadenamiento surtan efecto". Si tu Canvas no está activo, verás este`notice`mensaje: "El Canvas" está en pausa. Reanuda el Canvas para asegurarte de que las peticiones desencadenadas surtan efecto".

Si tu solicitud encuentra un error fatal, consulta [Errores y respuestas]({{site.baseurl}}/api/errors/#fatal-errors) para ver el código de error y la descripción.

## Consideraciones

Ten en cuenta lo siguiente al realizar llamadas a la API para enviar mensajes de Canvas mediante la entrega activada por la API:

- **Envío a usuarios existentes**: Cuando`send_to_existing_only`  se establece en`true`  (el valor predeterminado), el mensaje solo se envía a los usuarios existentes en Braze.
- **Creación de nuevos usuarios**: Cuando la `send_to_existing_only`configuración de  está establecida en `false`, debes incluir un`attributes`objeto . Si no existe un usuario con el ID especificado, Braze crea un usuario con ese ID y esos atributos antes de enviar el mensaje.
- **Limitación de alias de usuario**: La`send_to_existing_only`bandera no se puede utilizar con alias de usuario. Para enviar a un usuario que solo tiene un alias de usuario, este debe existir ya en Braze.
- **Segmentación por segmentos**: El`segment_id`parámetro no es compatible con este punto final. Para dirigirte a un segmento, configúralo en la configuración de audiencia objetivo del Canvas en el panel de Braze y utiliza `broadcast: true`, o utiliza el`audience`parámetro  con los filtros [de audiencia de Connected Audience]({{site.baseurl}}/api/objects_filters/connected_audience/).
- **Focalización combinada**: Cuando incluyes tanto el`recipients`parámetro como configurar un segmento de destino en el panel, el mensaje solo se envía a los perfiles de usuario que se especifican en la llamada a la API y que también coinciden con los filtros del segmento.
- **Llamadas de servidor a servidor**: Si estás realizando llamadas de servidor a servidor, es posible que tengas que incluir la URL de la API correspondiente en la lista de permitidos si estás protegido por un cortafuegos.

## Objeto de atribución para Canvas

Utiliza el objeto de mensajería `attributes` para añadir, crear o actualizar atributos y valores de un usuario antes de enviarle un Canvas desencadenado por la API utilizando el punto final `canvas/trigger/send`. Esta llamada a la API procesa el objeto de atributos del usuario antes de procesar y enviar el Canvas. Esto ayuda a minimizar el riesgo de problemas causados por [condiciones de carrera]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/). Sin embargo, por defecto, los grupos de suscripción no pueden actualizarse de esta forma.

{% alert note %}
¿Buscas la versión de campaña de este punto final? Consulta [Enviar mensajes de campaña utilizando la entrega desencadenada por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/).
{% endalert %}

{% endapi %}
