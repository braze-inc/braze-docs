---
nav_title: "POST: Enviar mensajes de Canvas mediante entrega desencadenada por API"
article_title: "POST: Enviar mensajes de Canvas mediante entrega desencadenada por API"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Enviar Canvas mediante entrega desencadenada por API de Braze."

---
{% api %}
# Envía mensajes Canvas mediante entrega desencadenada por API
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/canvas/trigger/send
{% endapimethod %}

> Utiliza este punto final para enviar mensajes Canvas mediante la entrega desencadenada por la API.

La entrega desencadenada por API te permite almacenar el contenido de los mensajes en el panel de Braze, a la vez que dictas cuándo se envía un mensaje y a quién a través de tu API.

Para poder enviar mensajes con este punto final, debes tener un [ID de Canvas]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier) (que se crea cuando construyes un Canvas).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c9a8a5fe-a101-4755-99f2-73aa8fc146fe {% endapiref %}

## Requisitos previos

Para utilizar este punto final, deberás generar una clave de API con el permiso `canvas.trigger.send`.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='send endpoints' category='message endpoints' %}

## Cuerpo de la solicitud

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) see Canvas identifier,
  "canvas_entry_properties": (optional, object) personalization key-value pairs that will apply to all users in this request,
  "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if `recipients` is omitted,
  "audience": (optional, connected audience object) see connected audience,
  // Including 'audience' will only send to users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to 'false', message will send to the entire segment targeted by the Canvas)
    [{
      // Either "external_user_id" or "user_alias" or "email" is required. Requests must specify only one.
      "user_alias": (optional, user alias object) user alias of user to receive message,
      "external_user_id": (optional, string) external identifier of user to receive message,
      "email": (optional, string) email address of user to receive message,
      "prioritization": (optional, array) prioritization array; required when using email,
      "canvas_entry_properties": (optional, object) personalization key-value pairs that will apply to this user (these key-value pairs will override any keys that conflict with the parent `canvas_entry_properties`)
      "send_to_existing_only": (optional, boolean) defaults to true, can't be used with user aliases
      "attributes": (optional, object) fields in the attributes object will create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values will be overwritten
    }],
    ...
}
```

## Parámetros de la solicitud

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
|`canvas_id`| Obligatoria | Cadena | Ver [identificador de Canvas]({{site.baseurl}}/api/identifier_types/). |
|`canvas_entry_properties`| Opcional | Objeto | Consulta [las propiedades de entrada en Canvas]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/). Pares clave-valor de personalización que se aplicarán a todos los usuarios de esta solicitud. El objeto Propiedades de entrada del Canvas tiene un límite de tamaño máximo de 50 KB. |
|`broadcast`| Opcional | Booleano | Debes establecer `broadcast` en verdadero cuando envíes un mensaje a un segmento completo al que se dirige una campaña o Canvas. Este parámetro está predeterminado como falso (a 31 de agosto de 2017). <br><br> Si `broadcast` tiene el valor true, no se puede incluir una lista `recipients`. Sin embargo, ten cuidado al configurar `broadcast: true`, ya que si lo haces involuntariamente puede que envíes tu mensaje a una audiencia mayor de la esperada. |
|`audience`| Opcional| Objeto de audiencia conectado | Ver [Audiencia conectada]({{site.baseurl}}/api/objects_filters/connected_audience/). |
|`recipients`| Opcional | Matriz | Ver [objeto de destinatarios]({{site.baseurl}}/api/objects_filters/recipient_object/). Si no se proporciona y `broadcast` está configurado como verdadero, el mensaje se enviará a todo el segmento al que se dirige el Canvas.<br><br> La matriz `recipients` puede contener hasta 50 objetos, y cada objeto puede contener una única cadena `external_user_id` y un único objeto `canvas_entry_properties`. Para esta llamada, se requiere `external_user_id` o `user_alias`. Las solicitudes deben especificar sólo una. <br><br> Cuando `send_to_existing_only` es `true`, Braze sólo enviará el mensaje a los usuarios existentes; sin embargo, esta bandera no puede utilizarse con alias de usuario. Cuando `send_to_existing_only` es `false` y no existe un usuario con el `id` dado, Braze creará un usuario con ese ID y atributos antes de enviar el mensaje.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Es posible que los clientes que utilicen la API para llamadas de servidor a servidor tengan que permitir la URL de API adecuada si están detrás de un cortafuegos.

{% alert important %}
Especificar un destinatario por dirección de correo electrónico está actualmente en acceso temprano. Ponte en contacto con tu administrador del éxito del cliente si estás interesado en participar en este acceso anticipado.
{% endalert %}

{% alert note %}
Si incluyes tanto usuarios específicos en tu llamada a la API como un segmento objetivo en el panel, el mensaje se enviará específicamente a los perfiles de usuario que estén tanto en la llamada a la API como que cumplan los requisitos para los filtros de segmento.
{% endalert %}

## Ejemplo de solicitud
```
curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/send' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "canvas_entry_properties": {"product_name" : "shoes", "product_price" : 79.99},
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

Las respuestas de los puntos finales de envío de mensajes incluirán la dirección `dispatch_id` del mensaje como referencia para el envío del mensaje. El `dispatch_id` es el ID del envío del mensaje (ID único para cada "transmisión" enviada desde la plataforma Braze). Echa un vistazo [al comportamiento de Dispatch ID]({{site.baseurl}}/help/help_articles/data/dispatch_id/) para obtener más información.

### Ejemplo de respuesta satisfactoria

El código de estado `201` podría devolver el siguiente cuerpo de respuesta. Si el Canvas está archivado, detenido o en pausa, no se enviará a través de este punto final.

```
{
  "notice": "The Canvas is paused. Resume the Canvas to ensure trigger requests will take effect.",
  "dispatch_id": "example_dispatch_id",
  "message": "success"
}
```

Si tu Canvas está archivado, verás este mensaje `notice`: "El Canvas" está archivado. Desarchiva el Canvas para asegurarte de que las solicitudes de desencadenamiento surtan efecto". Si tu Canvas no está activo, verás este mensaje `notice`: "El Canvas" está en pausa. Reanuda el Canvas para asegurarte de que las peticiones desencadenadas surtan efecto".

Si tu solicitud encuentra un error fatal, consulta [Errores y respuestas]({{site.baseurl}}/api/errors/#fatal-errors) para ver el código de error y la descripción.

## Objeto de atribución para Canvas

Utiliza el objeto de mensajería `attributes` para añadir, crear o actualizar atributos y valores de un usuario antes de enviarle un Canvas desencadenado por la API utilizando el punto final `canvas/trigger/send`. Esta llamada a la API procesa el objeto de atributos del usuario antes de procesar y enviar el Canvas. Esto ayuda a minimizar el riesgo de problemas causados por [condiciones de carrera]({{site.baseurl}}/help/best_practices/race_conditions/).

{% alert note %}
¿Buscas la versión de las campañas de este punto final? Consulta [Envío de mensajes de campaña mediante entrega desencadenada por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/).
{% endalert %}

{% endapi %}
