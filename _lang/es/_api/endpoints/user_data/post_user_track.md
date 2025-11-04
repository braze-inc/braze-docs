---
nav_title: "POST: Seguimiento de usuarios"
article_title: "POST: Seguimiento de usuarios"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto final Realizar un seguimiento de los usuarios de Braze."

---
{% api %}
# Rastrear usuarios
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/users/track
{% endapimethod %}

> Utiliza este punto final para registrar eventos personalizados y compras, y actualizar los atributos del perfil de usuario.

{% alert note %}
Braze procesa los datos pasados a través de la API en su valor nominal, y los clientes sólo deben pasar deltas (datos cambiantes) para minimizar el consumo innecesario de puntos de datos. Para saber más, consulta [Puntos de datos]({{site.baseurl}}/user_guide/data/data_points/).
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4cf57ea9-9b37-4e99-a02e-4373c9a4ee59 {% endapiref %}

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/api_key/) con el permiso `users.track`.

Es posible que los clientes que utilicen la API para llamadas de servidor a servidor tengan que permitir la lista `rest.iad-01.braze.com` si están detrás de un cortafuegos.

## Límite de velocidad

{% multi_lang_include rate_limits.md endpoint='users track' %}

## Cuerpo de la solicitud

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "attributes": (optional, array of attributes object),
  "events": (optional, array of event object),
  "purchases": (optional, array of purchase object),
}
```

### Parámetros de la solicitud

{% alert important %}
Para cada componente de la solicitud que aparece en la tabla siguiente, se requiere uno de los siguientes: `external_id`, `user_alias`, `braze_id`, `email`, o `phone`.
{% endalert %}

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
| `attributes` | Opcional | Matriz de objetos con atributos | Ver [objeto atributos del usuario]({{site.baseurl}}/api/objects_filters/user_attributes_object/) |
| `events` | Opcional | Matriz de objetos de eventos | Ver [objeto eventos]({{site.baseurl}}/api/objects_filters/event_object/) |
| `purchases` | Opcional | Matriz de objetos de compra | Ver [objeto de compras]({{site.baseurl}}/api/objects_filters/purchase_object/) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Ejemplos de solicitudes

### Actualizar un perfil de usuario por correo electrónico

Puedes actualizar el perfil de un usuario por correo electrónico utilizando el punto final `/users/track`. 

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "email": "test@braze.com",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 26,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ],
    "events": [
        {
            "email": "test@braze.com",
            "app_id": "your_app_identifier",
            "name": "rented_movie",
            "time": "2022-12-06T19:20:45+01:00",
            "properties": {
                "release": {
                    "studio": "FilmStudio",
                    "year": "2022"
                },
                "cast": [
                    {
                        "name": "Actor1"
                    },
                    {
                        "name": "Actor2"
                    }
                ]
            }
        },
        {
            "user_alias": {
                "alias_name": "device123",
                "alias_label": "my_device_identifier"
            },
            "app_id": "your_app_identifier",
            "name": "rented_movie",
            "time": "2013-07-16T19:20:50+01:00"
        }
    ],
    "purchases": [
        {
            "email": "test@braze.com",
            "app_id": "your_app_identifier",
            "product_id": "product_name",
            "currency": "USD",
            "price": 12.12,
            "quantity": 6,
            "time": "2017-05-12T18:47:12Z",
            "properties": {
                "color": "red",
                "monogram": "ABC",
                "checkout_duration": 180,
                "size": "Large",
                "brand": "Backpack Locker"
            }
        }
    ]
}'
```

### Actualizar un perfil de usuario por número de teléfono

Puedes actualizar un perfil de usuario por número de teléfono utilizando el punto final `/users/track`. Este punto final sólo funciona si incluyes un número de teléfono válido.

{% alert important %}
Si incluyes una solicitud tanto en `email` como en `phone`, Braze utilizará el correo electrónico como identificador.
{% endalert %}

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "phone": "+15043277269",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ],
}'
```
### Configurar grupos de suscripción

Este ejemplo muestra cómo crear un usuario y establecer su grupo de suscripción dentro del objeto de atributos de usuario. 

La actualización del estado de suscripción con este punto final actualizará al usuario especificado por su `external_id` (como Usuario1) y actualizará el estado de suscripción de cualquier usuario con el mismo correo electrónico que ese usuario (Usuario1).

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "attributes": [
  {
    "external_id": "user_identifier",
    "email": "example@email.com",
    "email_subscribe": "subscribed",
    "subscription_groups": [{
      "subscription_group_id": "subscription_group_identifier_1",
      "subscription_state": "unsubscribed"
      },
      {
        "subscription_group_id": "subscription_group_identifier_2",
        "subscription_state": "subscribed"
        },
        {
          "subscription_group_id": "subscription_group_identifier_3",
          "subscription_state": "subscribed"
        }
      ]
    }
  ]
}'
```

### Ejemplo de solicitud para crear un usuario sólo con alias

Puedes utilizar el punto final `/users/track` para crear un nuevo usuario de sólo alias estableciendo la clave `_update_existing_only` con un valor de `false` en el cuerpo de la solicitud. Si se omite este valor, no se creará el perfil de usuario de sólo alias. Utilizar un usuario de sólo alias garantiza que existirá un perfil con ese alias. Esto es especialmente útil cuando se crea una nueva integración, ya que evita la creación de perfiles de usuario duplicados.

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
{
    "attributes": [
        {
            "_update_existing_only": false,
            "user_alias": {
                "alias_name": "example_name",
                "alias_label": "example_label"
            },
            "email": "email@example.com"
        }
    ],
}'
```


## Respuestas

Al utilizar cualquiera de las solicitudes de API mencionadas, deberías recibir una de las tres respuestas generales siguientes: un [mensaje correcto](#successful-message), un [mensaje correcto con errores no fatales](#successful-message-with-non-fatal-errors) o un [mensaje con errores fatales](#message-with-fatal-errors).

### Mensaje correcto

Los mensajes correctos recibirán la siguiente respuesta:

```json
{
  "message": "success",
  "attributes_processed": (optional, integer), if attributes are included in the request, this will return an integer of the number of external_ids with attributes that were queued to be processed,
  "events_processed": (optional, integer), if events are included in the request, this will return an integer of the number of events that were queued to be processed,
  "purchases_processed": (optional, integer), if purchases are included in the request, this will return an integer of the number of purchases that were queued to be processed,
}
```

### Mensaje correcto con errores no fatales

Si tu mensaje tiene éxito pero tiene errores no fatales, como un objeto de evento no válido de una larga lista de eventos, recibirás la siguiente respuesta:

```json
{
  "message": "success",
  "errors": [
    {
      <minor error message>
    }
  ]
}
```

En el caso de mensajes con éxito, se seguirán procesando los datos no afectados por un error en la matriz `errors`. 

### Mensaje con errores fatales

Si tu mensaje tiene un error fatal, recibirás la siguiente respuesta:

```json
{
  "message": <fatal error message>,
  "errors": [
    {
      <fatal error message>
    }
  ]
}
```

### Códigos de respuesta de error fatal

Para conocer los códigos de estado y los mensajes de error asociados que se devolverán si tu solicitud encuentra un error fatal, consulta [Errores fatales y respuestas.]({{site.baseurl}}/api/errors/#fatal-errors)

Si recibes el error "provided external_id is blacklisted and disallowed", es posible que tu solicitud haya incluido un "usuario ficticio". Para más información, consulta [Bloqueo de correo no deseado]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking). 

## Preguntas más frecuentes

{% multi_lang_include email-via-sms-warning.md %}

### ¿Qué ocurre cuando se encuentran varios perfiles con la misma dirección de correo electrónico?
Si existe `external_id`, el perfil actualizado más recientemente con un ID externo tendrá prioridad para las actualizaciones. Si no existe `external_id`, se dará prioridad al perfil actualizado más recientemente.

### ¿Qué ocurre si no existe actualmente ningún perfil con la dirección de correo electrónico?
Se creará un nuevo perfil y un usuario sólo por correo electrónico. No se creará un alias. El campo de correo electrónico se configurará en test@braze.com, como se indica en el ejemplo de solicitud de actualización de un perfil de usuario por correo electrónico.

### ¿Cómo se utiliza `/users/track` para importar datos de usuario heredados?
Puedes enviar datos a través de la API de Braze de un usuario que aún no haya utilizado tu aplicación móvil para generar un perfil de usuario. Si el usuario utiliza posteriormente la aplicación, toda la información posterior a su identificación mediante el SDK se fusionará con el perfil de usuario existente que creaste mediante la llamada a la API. Cualquier comportamiento de usuario registrado anónimamente por el SDK antes de la identificación se perderá al fusionarse con el perfil de usuario existente generado por la API.

La herramienta de segmentación incluirá a estos usuarios independientemente de si han interactuado o no con la aplicación. Si quieres excluir a los usuarios subidos mediante la API de usuario que aún no han interactuado con la aplicación, añade el filtro `Session Count > 0`.

### ¿Cómo gestiona `/users/track` los eventos duplicados?

Cada objeto evento de la matriz de eventos representa una única ocurrencia de un evento personalizado por parte de un usuario en un momento determinado. Esto significa que cada evento ingestado en Braze tiene su propio ID de evento, por lo que los eventos "duplicados" se tratan como eventos separados y únicos.

### ¿Cómo gestiona `/users/track` los atributos personalizados anidados no válidos?

Cuando un atributo personalizado anidado contiene algún valor no válido (como formatos de hora no válidos o valores nulos), todas las actualizaciones de atributos personalizados anidados de la solicitud se eliminarán del procesamiento. Esto se aplica a todas las estructuras anidadas dentro de ese atributo específico. Para garantizar el éxito del proceso, comprueba que todos los valores de los atributos personalizados anidados son válidos antes de enviarlos.

## Usuarios activos al mes CY 24-25
Para los clientes que hayan comprado Usuarios activos al mes - CY 24-25, Braze gestiona diferentes límites de velocidad en su punto final `/users/track`:
- Los límites de velocidad por hora se establecen en función de la actividad prevista de ingesta de datos en tu cuenta, que puede corresponder al número de usuarios activos al mes que hayas comprado, al sector, a la estacionalidad o a otros factores.
- Además del límite horario, Braze aplica un límite de ráfagas al número de solicitudes que pueden enviarse cada tres segundos.
- Cada solicitud puede contener hasta 50 actualizaciones combinadas de objetos de atributo, evento o compra.

Los límites actuales basados en la ingesta prevista se pueden encontrar en el panel en **Configuración** > **API e identificadores** > **Panel de uso de API**. Podemos modificar los límites de velocidad para proteger la estabilidad del sistema o permitir un mayor caudal de datos en tu cuenta. Ponte en contacto con el soporte de Braze o con tu administrador del éxito del cliente si tienes preguntas o dudas sobre el límite de solicitudes por hora o por segundo y las necesidades de tu empresa.



{% endapi %}
