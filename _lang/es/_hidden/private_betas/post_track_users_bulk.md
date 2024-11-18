---
nav_title: "PUBLICAR: Seguimiento de usuarios (masivo)"
layout: api_page
page_type: reference
hidden: true
permalink: /track_users_bulk/
description: "En este artículo se describen los detalles del punto final Seguimiento de usuarios (masivo)."
---

{% api %}
# Seguimiento de usuarios (masivo)
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/users/track/bulk
{% endapimethod %}

> Utiliza este punto final para registrar eventos personalizados y compras, y actualizar los atributos del perfil de usuario de forma masiva.

{% alert important %}
Este punto final está actualmente en fase beta. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en la versión beta.
{% endalert %}

## Cuándo utilizar este punto final

Similar al [POST: Punto final de seguimiento de usuarios]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#prerequisites), puedes utilizar este punto final para actualizar los perfiles de usuario. Sin embargo, este punto final es más adecuado para realizar actualizaciones masivas:

- **Peticiones más grandes:** Este punto final permite 10.000 usuarios por solicitud, lo que significa que tienes que hacer menos solicitudes para satisfacer tus necesidades de actualización masiva.
- **Priorización:** Durante los picos de tráfico, las solicitudes de `/users/track` tendrán prioridad sobre las de `/users/track/bulk`. Utilizar ambos puntos finales te proporciona un mayor control sobre la ingesta de datos.

Ten en cuenta que las actualizaciones de los usuarios en este punto final no desencadenarán ninguna campaña basada en acciones o Lienzos basados en acciones, no desencadenarán ningún evento de excepción ni harán un seguimiento de las métricas de conversión. Las actualizaciones de los usuarios en este punto final están disponibles para segmentación y personalización.

Considera la posibilidad de utilizar este punto final cuando estés rellenando muchos perfiles de usuario durante la incorporación o sincronizando grandes cantidades de perfiles de usuario como parte de una sincronización diaria.

## Requisitos previos

Para utilizar este punto final, necesitarás una clave de API con el permiso `users.track.bulk`.

Si utilizas la API para llamadas de servidor a servidor, puede que tengas que permitir el punto final (por ejemplo, `rest.iad-01.braze.com`) si estás detrás de un cortafuegos. Consulta los [puntos finales por instancia]({{site.baseurl}}/api/basics#endpoints) para obtener más información.

## Límite de velocidad

Aplicamos un límite de velocidad base de 5 peticiones por segundo a este punto final para todos los clientes.

Cada solicitud a `/users/sync/bulk` tiene un límite de carga útil de 4 MB, y puede contener hasta 10.000 objetos de evento, atributo o compra.

Cada objeto (evento, atributo y matrices de compra) puede actualizar un usuario cada uno, lo que significa que se pueden actualizar hasta 10.000 usuarios diferentes en una sola solicitud. Un solo perfil de usuario puede actualizarse con hasta 100 objetos en una sola solicitud.

{% alert note %}
Si necesitas aumentar el límite de velocidad, ponte en contacto con tu administrador del éxito del cliente.
{% endalert %}


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

### Actualización masiva de 10.000 perfiles de usuario en una sola solicitud

Puedes actualizar hasta 10.000 perfiles de usuario. He aquí un ejemplo truncado en el que la solicitud consta de 10.000 objetos de atributo:

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/bulk' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "external_id": "user1",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        },
        {
            "external_id": "user2",
            "string_attribute": "vegetables",
            "boolean_attribute_1": false,
            "integer_attribute": 25,
            "array_attribute": [
                "broccoli",
                "asparagus",	
            ]
        },

...

        {
            "external_id": "user10000",
            "string_attribute": "nuts",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "hazelnut",
                "pistachio"
            ]
        }
    ]
}'
```

Aquí tienes un ejemplo en el que la solicitud consta de objetos de atributo y de evento:

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/bulk' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "external_id": "user1",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ],
    "events": [
        {
            "external_id": "user2",
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
...
        {
            "external_id": "user10000",
            "app_id": "your_app_identifier",
            "name": "rented_movie",
            "time": "2023-09-16T08:00:00+10:00",
            "properties": {
                "release": {
                    "studio": "FilmStudio",
                    "year": "1988"
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
        }
    ]
}'
```

## Respuestas

### Mensajes con éxito

Los mensajes correctos recibirán la siguiente respuesta:

```json
{
  "message": "success",
  "attributes_processed": (optional, integer), if attributes are included in the request, this will return an integer of the number of external_ids with attributes that were queued to be processed,
  "events_processed": (optional, integer), if events are included in the request, this will return an integer of the number of events that were queued to be processed,
  "purchases_processed": (optional, integer), if purchases are included in the request, this will return an integer of the number of purchases that were queued to be processed,
}
```

#### Mensaje correcto con errores no fatales

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

#### Códigos de respuesta de error fatal

Para conocer los códigos de estado y los mensajes de error asociados que se devolverán si tu solicitud encuentra un error fatal, consulta [Errores fatales y respuestas]({{site.baseurl}}/api/errors/#fatal-errors).

Si recibes el error `provided external_id is blacklisted and disallowed`, es posible que tu solicitud haya incluido un "usuario ficticio". Para más información, consulta [Bloqueo de correo no deseado]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking).

## Preguntas más frecuentes

### ¿Debo utilizar este punto final o el normal `/users/track`?

Te recomendamos que utilices ambos.

Para grandes rellenos de perfiles de usuario y sincronizaciones en las que no se necesita desencadenar campañas basadas en acciones y Lienzos, seguimiento de conversiones y eventos de excepción, utiliza `/users/track/bulk`. 

Para casos de uso en tiempo real, utiliza el punto final `/users/track`.

### ¿Qué identificadores puedo utilizar en /users/track/bulk?

Se requiere una de las siguientes opciones: `external_id`, `braze_id`, `user_alias`, `email`, o `phone`. Para más ejemplos, consulta nuestra documentación sobre el [objeto atributos de usuario]({{site.baseurl}}/api/objects_filters/user_attributes_object/), el [objeto eventos]({{site.baseurl}}/api/objects_filters/event_object/) o [el objeto compras]({{site.baseurl}}/api/objects_filters/purchase_object/). 

### ¿Puedo incluir atributos, eventos y compras en 1 solicitud?

Sí. Puedes construir tu solicitud con cualquier cantidad de atributos, eventos y objetos de compra, hasta 10.000 objetos por solicitud.


{% endapi %}
