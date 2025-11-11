---
nav_title: "PUBLICAR: Seguimiento de usuarios (sincrónico)"
article_title: "PUBLICAR: Seguimiento de usuarios (sincrónico)"
alias: /post_user_track_synchronous/
layout: api_page
page_order: 4.5
page_type: reference
description: "En este artículo se describen los detalles del punto final sincrónico de seguimiento de usuarios de Braze."

---
{% api %}
# Seguimiento de usuarios (sincrónico)
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/usuarios/seguimiento/sincronización
{% endapimethod %}

> Utiliza este punto final para registrar eventos personalizados y compras, y actualizar los atributos del perfil de usuario de forma sincrónica. Este punto final funciona de forma similar al [punto final `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track), que actualiza los perfiles de usuario de forma asíncrona.

{% alert important %}
Este punto final está actualmente en fase beta. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en esta beta.
{% endalert %}

## Llamadas a la API síncronas y asíncronas

En una llamada asíncrona, la API devolverá el código de estado `201`, que indica que tu solicitud se ha recibido, comprendido y aceptado correctamente. Sin embargo, esto no significa que tu solicitud se haya completado en su totalidad.

En una llamada sincrónica, la API devolverá un código de estado `201`, que indica que tu solicitud se ha recibido, comprendido, aceptado y completado correctamente. La respuesta a la llamada mostrará campos seleccionados del perfil de usuario como resultado de la operación.

Este punto final tiene un límite de velocidad menor que el punto final `/users/track` (ver [límite de velocidad](#rate-limit) más abajo). Cada solicitud de `/users/track/sync` sólo puede contener un objeto de evento, un objeto de atributo **o** un objeto de compra. Este punto final debe reservarse para las actualizaciones del perfil de usuario en las que se necesite una llamada síncrona. Para una aplicación saludable, te recomendamos que utilices `/users/track/sync` y `/users/track` juntos.

Por ejemplo, si envías solicitudes consecutivas para el mismo usuario durante un breve período de tiempo, es posible que se produzcan condiciones de carrera con el punto final asíncrono `/users/track`, pero con el punto final `/users/track/sync` puedes enviar esas solicitudes en secuencia, cada una después de recibir una respuesta `2XX`.

## Requisitos previos

Para utilizar este punto final, necesitarás una [clave de API]({{site.baseurl}}/api/api_key/) con el permiso `users.track.sync`.

Es posible que los clientes que utilicen la API para llamadas de servidor a servidor tengan que permitir la lista `rest.iad-01.braze.com` si están detrás de un cortafuegos.

## Límite de velocidad

Aplicamos un límite de velocidad base de 500 solicitudes por minuto a este punto final para todos los clientes. Cada solicitud de `/users/track/sync` puede contener hasta un objeto de evento, un objeto de atributo o un objeto de compra. Cada objeto (evento, atributo y matrices de compra) puede actualizar un usuario cada uno.

## Cuerpo de la solicitud

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "attributes": (optional, one attributes object),
  "events": (optional, one event object),
  "purchases": (optional, one purchase object),
}
```

### Parámetros de la solicitud

{% alert important %}
Para cada componente de la solicitud que aparece en la tabla siguiente, se requiere uno de los siguientes: `external_id`, `user_alias`, `braze_id`, `email`, o `phone`.
{% endalert %}

| Parámetro | Obligatoria | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
| `attributes` | Opcional | Un objeto de atribución | Ver [objeto atributos del usuario]({{site.baseurl}}/api/objects_filters/user_attributes_object/) |
| `events` | Opcional | Un objeto de evento | Ver [objeto eventos]({{site.baseurl}}/api/objects_filters/event_object/) |
| `purchases` | Opcional | Un objeto de compra | Ver [objeto de compras]({{site.baseurl}}/api/objects_filters/purchase_object/) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Respuestas

Al utilizar los [parámetros de solicitud](#request-parameters) de este punto final, deberías recibir una de las siguientes respuestas: un mensaje correcto o un mensaje con errores fatales.

### Mensaje correcto

Los mensajes con éxito devolverán la siguiente respuesta, que incluye información sobre los datos del perfil de usuario que se actualizaron.

```json
{
    "users": (optional, object), the identifier of the user in the request. May be empty if no users are found and _update_existing_only key is set to true,
        "custom_attributes": (optional, object), the custom attributes as a result of the request. Only custom attributes from the request will be listed,
        "custom_events": (optional, object), the custom events as a result of the request. Only custom events from the request will be listed,
        "purchase_events": (optional, object), the purchase events as a result of the request. Only purchase events from the request will be listed,
    },
    "message": "success"
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

## Ejemplos de solicitudes y respuestas

### Actualizar un atributo personalizado por ID externo

#### Solicitud

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "external_id": "xyz123",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ]
}'
```

#### Respuesta

```
{
    "users": [
        {
            "external_id": "xyz123",
            "custom_attributes": {
                "string_attribute": "fruit",
                "boolean_attribute_1": true,
                "integer_attribute": 25,
                "array_attribute": [
                    "banana",
                    "apple",
                ]
            }
        }
    ],
    "message": "success"
} 
```

### Actualizar un evento personalizado por correo electrónico

#### Solicitud

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
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
        }
    ]
}'
```

#### Respuesta

```
{
    "users": [
        {
            "email": "test@braze.com",
            "custom_events": [
                {
                "name": "rented_movie",
                "first": "2022-01-001T00:00:00.000Z",
                "last": "2022-12-06T18:20:45.000Z",
                "count": 10
                }
            ]
        }
    ],
    "message": "success"
} 
```

### Actualizar un evento de compra por alias de usuario

#### Solicitud

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "purchases" : [
    {
      "user_alias" : { 
          "alias_name" : "device123", 
          "alias_label" : "my_device_identifier"
      }
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "Completed Order",
      "currency" : "USD",
      "price" : 219.98,
      "time" : "2022-12-06T19:20:45+01:00",
      "properties" : {
          "products" : [ 
            {
              "name": "Monitor",
              "category": "Gaming",
              "product_amount": 19.99
            },
            { 
              "name": "Gaming Keyboard",
              "category": "Gaming ",
              "product_amount": 199.99
            }
          ]
      }
   }
  ]
}'
```

#### Respuesta

```
{
    "users": [
        {
          "user_alias" : { 
            "alias_name" : "device123", 
            "alias_label" : "my_device_identifier"
          },
          "purchase_events": [
                {
                "product_id": "Completed Order",
                "first": "2013-07-16T19:20:30+01:00",
                "last": "2022-12-06T18:20:45.000Z",
                "count": 3
                }
            ]
        }
    ],
    "message": "success"
} 
```

## Preguntas más frecuentes

### ¿Debo utilizar el punto final asíncrono o síncrono?

Para la mayoría de las actualizaciones de perfiles, el punto final `/users/track` funcionará mejor debido a su mayor límite de velocidad y a su flexibilidad para permitirte realizar solicitudes por lotes. Sin embargo, el punto final `/users/track/sync` es útil si experimentas condiciones de carrera debido a solicitudes rápidas y consecutivas para el mismo usuario.

### ¿Difiere el tiempo de respuesta del punto final `/users/track`?

Con una llamada sincrónica, la API espera a que se complete la solicitud para devolver una respuesta. Como resultado, las solicitudes sincrónicas tardarán más en promedio que las asíncronas en `/users/track`. Para la mayoría de las solicitudes, puedes esperar una respuesta en cuestión de segundos.

### ¿Puedo enviar varias solicitudes al mismo tiempo?

Sí, siempre que las solicitudes sean para usuarios diferentes, o que cada solicitud actualice diferentes atributos, eventos, compras para un usuario.

Si envías varias solicitudes para un usuario, para el mismo atributo, evento o compra, Braze recomienda esperar una respuesta satisfactoria entre cada solicitud para evitar que se produzcan condiciones de carrera.

### ¿Por qué el valor de respuesta no coincide con el de mi solicitud original?

Aunque tu solicitud se ha completado, es posible que el valor de tu atributo personalizado no se haya actualizado. Esto puede ocurrir cuando la actualización de tu atributo personalizado supera el número máximo de caracteres, supera los límites de la matriz o si el usuario no existe en Braze y tienes `_update_existing_only = true`.

En estos casos, trata la respuesta como una indicación de que tu solicitud, aunque completada, no se ha realizado la actualización deseada. Resuelve el problema con las razones por las que puede ocurrir desde arriba.

{% endapi %}
