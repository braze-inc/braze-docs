---
nav_title: Conexión a la API de datos de clientes
article_title: Conexión a la API de datos de clientes de Movable Ink
description: "Este artículo de referencia describe cómo conectarse para activar los datos de eventos de clientes almacenados en Braze para generar contenido personalizado en Movable Ink mediante la API de datos de clientes."
page_type: partner
search_tag: Partner
---

# Conexión a la API de datos de clientes de Movable Ink

> La integración de la API de datos de clientes de Braze y Movable Ink permite a los profesionales del marketing activar los datos de eventos de clientes almacenados en Braze para generar contenido personalizado dentro de Movable Ink.

Movable Ink es capaz de ingerir eventos de comportamiento de Braze a través de su API de datos de clientes. Los eventos se almacenarán en los perfiles de usuario en función del identificador único de usuario (UUID) que se pase a Movable Ink.

Para obtener más información sobre Stories, la API de datos de clientes de Movable Ink y cómo Movable Ink aprovecha los datos de comportamiento, visita los siguientes artículos del centro de soporte:

- [Potenciar los contenidos con datos de comportamiento](https://support.movableink.com/hc/en-us/sections/360001239453-Power-content-with-behavioral-data)
- [Introducción y guía de la API de datos de clientes](https://support.movableink.com/hc/en-us/articles/13815957200663-Customer-Data-API-introduction-and-guide)
- [PREGUNTAS FRECUENTES: API de datos de clientes](https://support.movableink.com/hc/en-us/articles/12423178752279-FAQ-Customer-Data-API)

## Requisitos previos

| Requisito | Descripción |
|---|---|
| Cuenta Movable Ink | Se necesita una cuenta Movable Ink para beneficiarse de esta asociación. |
| Credenciales de la API de Movable Ink | El equipo de soluciones de Movable Ink generará las credenciales API por ti. Las credenciales de la API consisten en:{::nomarkdown}<ul><li>Una URL de punto final (a la que se enviarán los datos)</li><li>Nombre de usuario y contraseña (utilizados para autenticar la API)</li></ul>{:/} Si lo desea, Movable Ink puede proporcionar el nombre de usuario y la contraseña como un valor codificado en base64 para ser utilizado como un valor de cabecera de autorización básica. |
| Cargas útiles de eventos de comportamiento | Deberás compartir las cargas útiles de tus eventos con tu equipo de Movable Ink Client Experience. Consulte [Compartir cargas útiles de eventos](#event-payloads) con Movable Ink para obtener más detalles. |
| Activos creativos y lógica empresarial | Tendrás que compartir activos creativos con Movable Ink, incluidos archivos de Adobe Photoshop (PSD) que indiquen a Movable Ink cómo construir el bloque y una imagen alternativa. También tendrá que proporcionar la lógica de negocio para saber cómo y cuándo mostrar el Bloque de Contenido activado por el socio. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

### Paso 1: Crear una campaña webhook en Braze

#### Paso 1a: Crear una nueva campaña

1. En Braze, [crea una campaña webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).
2. Dé a su campaña un nombre y una descripción opcional.
3. Seleccione **Plantilla en blanco** como plantilla.

#### Paso 1b: Añade tus credenciales API de datos de clientes

1. En el campo **Webhook URL**, introduce la URL del punto final de Movable Ink.

![Pestaña Componer del compositor de webhooks en Braze con la URL del punto final de Movable Ink y el cuerpo de la solicitud configurados como par clave-valor JSON.]({% image_buster /assets/img/movable_ink/cd_api_webhook_url.png %}){: style="max-width:75%" }

{:start="2"}
2\. Seleccione la pestaña **Configuración**.
3\. Añada las siguientes cabeceras de solicitud como pares clave-valor:

| Clave | Valor |
| --- | --- |
| Tipo de contenido | application/json |
| Autorización | Introduzca la autenticación básica que recibió de Movable Ink. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Pestaña de configuración del compositor de webhooks en Braze con pares clave-valor para Tipo de contenido y Autorización.]({% image_buster /assets/img/movable_ink/cd_api_webhook_settings.png %}){: style="max-width:75%" }

#### Paso 1c: Configura tu carga útil

1. Vuelva a la pestaña **Redactar**.
2. Para tu **cuerpo** de solicitud, crea tu propio cuerpo de solicitud con pares clave-valor JSON o introduce la carga útil de tu evento como texto sin formato. Consulta las [cargas útiles de muestra](#sample-payloads) para ver ejemplos de eventos estándar de comercio electrónico.

![Pestaña Componer del compositor de webhooks en Braze con pares clave-valor JSON para ID, marca de tiempo, ID de usuario y tipo de evento.]({% image_buster /assets/img/movable_ink/cd_api_webhook_kvp.png %}){: style="max-width:75%" }

#### Paso 1d: Pruebe su webhook {#step-1d}

Tendrás que compartir una carga útil de muestra con tu equipo de Movable Ink Client Experience. Puede generar esta carga útil en la pestaña **Prueba** basándose en la carga útil que ha construido.

{% alert important %}
Movable Ink recomienda esperar para probar tu webhook en Braze hasta que tu equipo de Experiencia del cliente de Movable Ink haya confirmado que ha completado el mapeado y está listo para recibir una prueba. Si esta asignación no está completa, es probable que reciba un error al realizar la prueba.
{% endalert %}

Para probar su webhook, haga lo siguiente:

1. Seleccione la pestaña **Prueba**.
2. Previsualice el mensaje como un usuario para ver una muestra de la carga útil del evento para ese usuario. Puede elegir entre previsualizar como usuario aleatorio, usuario específico o usuario personalizado.
3. Si todo parece correcto, haga clic en **Enviar prueba** para enviar una solicitud de prueba.

![Mensaje de respuesta de webhook en Braze que muestra una respuesta 200 OK.]({% image_buster /assets/img/movable_ink/cd_api_webhook_response.png %}){: style="max-width:75%" }

### Paso 2: Finalice la configuración de su campaña

#### Paso 2a: Programa tu campaña

Cuando hayas terminado de componer y probar el webhook, [programa tu campaña]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types). 

Braze admite entregas programadas, basadas en acciones y activadas por API. [La entrega basada en acciones]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) suele ser la más adecuada para la mayoría de los casos de uso de eventos de comportamiento. Si tienes preguntas sobre lo que tiene sentido para tu caso de uso, ponte en contacto con tus administradores del éxito del cliente de Braze y Movable Ink.

Para la entrega basada en acciones:

1. Especifica la acción desencadenante. Este es el evento que activará el webhook a Movable Ink.
2. Asegúrese de que el **Retraso de programación** está establecido en **Inmediatamente**. Los datos de los eventos deben enviarse a Movable Ink inmediatamente después de que se produzca el evento, sin demora.
3. Establezca la duración de la campaña especificando una hora de inicio. Es probable que no se aplique una hora de finalización, aunque puede establecerse si es necesario para el caso de uso.

{% alert note %}
Para asegurarte de que los datos se transmiten a Movable Ink en tiempo real, no selecciones **Enviar campaña a los usuarios de su zona horaria local**.
{% endalert %}

#### Paso 2b: Especifica tu audiencia

A continuación, determina a qué usuarios quieres dirigir esta campaña. Para más información, consulte la sección [Dirigirse a los usuarios]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/).

Asegúrese de no utilizar pruebas A/B en su campaña desactivando la casilla **Grupo de control**. Si se incluye un grupo de control, a un porcentaje de usuarios no se les enviarán datos a Movable Ink. Toda su audiencia debe dirigirse a la variante y no al grupo de control.

![Panel de pruebas A/B en una campaña Braze con una distribución de variantes del 100% asignada a la variante 1, y sin grupo de control.]({% image_buster /assets/img/movable_ink/cd_api_webhook_ab.png %})

#### Paso 2c: Elegir eventos de conversión (opcional)

Si lo desea, puede asignar eventos de conversión a esta campaña dentro de Braze.

Sin embargo, dado que el webhook sólo pretende transmitir datos, es probable que la atribución a este nivel sea menos útil que la atribución a nivel de campaña después de que los datos de comportamiento de Braze se utilicen para personalizar el contenido.

### Paso 3: Lanzar la campaña

Revise la configuración de su webhook y lance su campaña.

## Consideraciones

### Alineación con un identificador único de usuario

Asegúrese de que el valor del identificador único de usuario (UUID) que está utilizando como su `mi_u`, está disponible dentro de Braze y se puede incluir en las cargas útiles de eventos enviados a Movable Ink.

Esto garantiza que los eventos de comportamiento a los que Movable Ink hace referencia al generar una imagen están asociados al mismo cliente para el que recibieron los eventos de comportamiento. Si el valor UUID no es el mismo que el de Braze `external_id`, el UUID debe capturarse y pasarse a Braze como atributo o en las propiedades de evento de un evento Braze para aprovechar este identificador.

Braze rastrea el comportamiento de los usuarios en múltiples plataformas (como la web y la aplicación móvil), por lo que un mismo usuario puede tener varios identificadores anónimos distintos. Estos identificadores pueden fusionarse en el perfil de usuario único conocido de Stories cuando se envía un evento `identify` a Movable Ink, siempre y cuando el evento `identify` incluya tanto un identificador anónimo como el identificador único conocido.

Una vez que Movable Ink recibe un `user_id` para un único usuario, todos los eventos futuros para ese usuario deben incluir ese mismo `user_id`.

### Compartir cargas útiles de eventos con Movable Ink {#event-payloads}

Antes de configurar el conector a la API de Datos de Cliente de Movable Ink, asegúrate de compartir tus cargas útiles de eventos con tu equipo de Experiencia del Cliente de Movable Ink. Esto permite a Movable Ink asignar tus eventos a su esquema de eventos y evitará cualquier llamada a la API rechazada o fallida.

Puede generar una carga útil de evento dentro de Braze utilizando cualquier propiedad de evento. Generar una carga útil de muestra para un usuario aleatorio o buscando un ID de usuario específico. Consulte [el paso 1d](#step-1d) anterior para obtener más información.

Comparta esta carga útil de muestra con su equipo de Movable Ink Client Experience. Asegúrate de que no hay información sensible de identificación personal en la carga útil de la muestra (como dirección de correo electrónico, número de teléfono o fechas de nacimiento completas). 

Para obtener más información sobre las propiedades de eventos personalizados y el formato esperado de los datos contenidos en las propiedades, consulte [Propiedades de eventos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties).

### Usuarios conocidos frente a anónimos

En Braze, los eventos pueden registrarse bajo un perfil de usuario anónimo. Los identificadores que se vinculan al perfil de usuario durante el registro de eventos dependen de cómo se creó el usuario (a través de Braze SDK o API) y de su etapa actual en el ciclo de vida del usuario.

#### Sólo reenvío de eventos Braze para usuarios conocidos

En su campaña webhook, utilice el filtro `External User ID` para dirigirse únicamente a los usuarios que tengan un `external_id` con el filtro `External User ID` `is not blank`.

#### Reenvío de eventos Braze para usuarios anónimos y conocidos

Si quieres reenviar eventos Braze de usuarios anónimos (usuarios antes de que se asigne un `external_id` a su perfil), tendrás que decidir qué identificador utilizar como `anonymous_id` para Movable Ink hasta que esté disponible un `external_id`. Elige un `anonymous_id` que permanecerá constante en tu perfil de usuario Braze. Puede utilizar la lógica Liquid en el cuerpo del webhook para decidir si pasa un `anonymous_id` o un `user_id`.

Para más información, consulte los webhooks de ejemplo en [payloads de ejemplo](#sample-payloads).

## Ejemplos de cargas útiles

### Evento de vista del producto

{% tabs local %}
{% tab Ejemplo de evento de activación de Braze %}

{% raw %}

```json
{
  "events": [
    {
      "email": "test@braze.com",
      "name": "Product Viewed",
      "time": "2023-12-06T19:20:45+01:00",
      "properties": {
        "categories": [
          {
            "id": "Bathroom",
            "url": "https://example.com/cat/bathroom"
          }
        ],
        "meta": {
          "color": "green"
        },
        "title": "All-Purpose Cleaning Wipes",
        "price": 1.99,
        "id": "56544",
        "url": "https://www.example.com/variants_id/5f08cb918dcc595aa74b0fbc"
      }
    }
  ]
}
```

{% endraw %}

{% endtab %}
{% tab Carga útil esperada de la solicitud de Movable Ink %}

{% raw %}

```
curl --location --request POST 'https://collector.movableink-dmz.com/behavioral/{{key}}' \
--header 'Authorization: Basic {{authorization}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "anonymous_id": "123-abc-678",
  "event": "product_viewed",
  "properties": {
    "categories": [
      {
        "id": "Bathroom",
        "url": "https://example.com/cat/bathroom"
      }
    ],
    "meta": {
      "color": "green"
    },
    "title": "All-Purpose Cleaning Wipes",
    "price": 1.99,
    "id": "56544",
    "url": "https://www.example.com/variants_id/5f08cb918dcc595aa74b0fbc"
  },
  "timestamp": 1257894000000,
  "timezone": "America/New_York",
  "type": "track",
  "user_id": "5c3aa83113dd490100d3d8d7"
}'

```

{% endraw %}
{% endtab %}
{% tab Ejemplo de webhook %}

En este ejemplo, se utiliza una dirección de correo electrónico con hash como `anonymous_id` para los usuarios que no disponen de `external_id`.

{% raw %}

```liquid
// Converts the timestamp of "now" to seconds since 1970 and assigns it to a local variable "timestamp"
{% assign timestamp = "now" | date: "%s" %}

// Example of md5 hashing the email address to use as the anonymous_id
{% assign anon_id = {{${email_address}}} | md5 %}

// Condition logic to determine which identifier to use. If an external_id is available use that, otherwise use the anonymous_id
{% if {{${user_id}}} %}
{% capture user_identifier %}"user_id": "{{${user_id}}}"{% endcapture %}
{% else %}
{% capture user_identifier %}"anonymous_id": "{{anon_id}}"{% endcapture %}
{% endif %}

{
  {{user_identifier}}
  "event": "product_viewed",
  "properties": {
    "categories": [
      {
        "id": "{{event_properties.${categories}[0].id}}",
        "url": "{{event_properties.${categories}[0].url}}"
      }
    ],
    "meta": {
      "color": "{{event_properties.${meta}.color}}"
    },
    "title": "{{event_properties.${title}}}",
    "price": "{{event_properties.${price}}}",
    "id": "{{event_properties.${id}}}",
    "url": "{{event_properties.${url}}}"
  },
  "timestamp": "{{timestamp}}",
  "timezone": "{{${time_zone}}}",
  "type": "track",
}

```

{% endraw %}
{% endtab %}
{% endtabs %}

### Evento de vista de categoría

{% tabs local %}
{% tab Ejemplo de evento de activación de Braze %}

{% raw %}

```json
{
  "events": [
    {
      "external_id": "123456789",
      "name": "Category Viewed",
      "time": "2023-12-06T19:20:45+01:00",
      "properties": {
        "id": "bathroom-1",
        "title": "Bathroom Stuff",
        "url": "https://www.example.com/categories/bathroom"
      }
    }
  ]
}
```

{% endraw %}

{% endtab %}
{% tab Carga útil esperada de la solicitud de Movable Ink %}

{% raw %}

```
curl --location --request POST 'https://collector.movableink-dmz.com/behavioral/{{key}}' \
--header 'Authorization: Basic {{authorization}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "anonymous_id": "123-abc-678",
  "event": "category_viewed",
  "properties": {
    "id": "bathroom-1",
    "title": "Bathroom Stuff",
    "url": "https://www.example.com/categories/bathroom"
  },
  "timestamp": 1257894000000,
  "timezone": "America/New_York",
  "type": "track",
  "user_id": "5c3aa83113dd490100d3d8d7"
}'
```

{% endraw %}

{% endtab %}
{% tab Ejemplo de webhook %}

Este ejemplo muestra un webhook que rastrea eventos sólo para usuarios conocidos (usuarios con un `external_id`).

{% raw %}

```liquid
// Converts the timestamp of "now" to seconds since 1970 and assigns it to a local variable "timestamp"
{% assign timestamp = "now" | date: "%s" %}

{
  "event": "category_viewed",
  "properties": {
    "id": "{{event_properties.${id}}}",
    "title": "{{event_properties.${title}}}",
    "url": "{{event_properties.${url}}}"
  },
  "timestamp": "{{timestamp}}",
  "timezone": "{{${time_zone}}}",
  "type": "track",
  "user_id": "{{${user_id}}}"
}

```

{% endraw %}

{% endtab %}
{% endtabs %}

### Identificar el evento

{% tabs local %}
{% tab Ejemplo de evento de activación de Braze %}

{% raw %}

```json
{
  "events": [
    {
      "external_id": "123456789",
      "name": "Account Created",
      "time": "2023-12-06T19:20:45+01:00"
    }
  ]
}
```

{% endraw %}
{% endtab %}
{% tab Carga útil esperada de la solicitud de Movable Ink %}

{% raw %}

```
curl --location --request POST 'https://collector.movableink-dmz.com/behavioral/{{key}}' \
--header 'Authorization: Basic {{authorization}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "anonymous_id": "jg0iq5gd30dqpwn8zmx05p06mzjmjir4r8",
  "timestamp": 1257894000000,
  "timezone": "America/New_York",
  "type": "identify",
  "user_id": "mycustomerid123"
}'
```

{% endraw %}
{% endtab %}
{% tab Ejemplo de webhook %}

En este ejemplo, se utiliza una dirección de correo electrónico con hash como `anonymous_id` para los usuarios que no disponen de `external_id`.

{% raw %}

```liquid
// Converts the timestamp of "now" to seconds since 1970 and assigns it to a local variable "timestamp"
{% assign timestamp = "now" | date: "%s" %}

// Example of md5 hashing the email address to use as the anonymous_id
{% assign anon_id = {{${email_address}}} | md5 %}

{
  "anonymous_id": "{{anon_id}}",
  "timestamp": "{{timestamp}}",
  "timezone": "{{${time_zone}}}",
  "type": "identify",
  "user_id": "{{${user_id}}}"
}

```

{% endraw %}

{% endtab %}
{% endtabs %}



