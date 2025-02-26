---
nav_title: Conector de corrientes personalizado
alias: /currents_connector/
hidden: true
---

# Conector Currents personalizado para socios

## Serialización y formato de los datos

El formato de datos de destino es JSON sobre HTTPS. Los eventos se agruparán por predeterminado en lotes de 100 eventos, y se enviarán al punto final como una matriz JSON que contiene todos los eventos. Los lotes se enviarán en el siguiente formato:

`{"events": [event1, event2, event3, etc...]}`

Habrá un objeto JSON de nivel superior con la clave "events" que se asigna a una matriz de otros objetos JSON, cada uno de los cuales representa un único evento.

Los siguientes ejemplos son para eventos _individuales_ (tal y como formarían parte de la matriz más grande de objetos JSON, con cada objeto JSON representando un único evento en el lote).

### Actos relacionados con la campaña

A continuación se muestran algunos ejemplos de cargas útiles para varios eventos, tal y como aparecerían si estuvieran asociados a una campaña:

```
// In-App Message Click: users.messages.inappmessage.Click
{
  "event_type": "users.messages.inappmessage.Click",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
    "campaign_name": "Test Campaign",
    "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
    "message_variation_name": "Test Message Variation",
    "platform": "android",
     "os_version": "Android (N)",
    "device_model": "Nexus 5X",
    "button_id": "0",
    "send_id": "f123456789abcdef01234567"
  }
}
```

```
// Push Notification Send: users.messages.pushnotification.Send
{
  "event_type": "users.messages.pushnotification.Send",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
    "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
    "campaign_name": "Test Campaign",
    "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
    "message_variation_name": "Test Message Variation",
    "send_id": "f123456789abcdef01234567",
    "dispatch_id": "01234567-89ab-cdef-0123-456789abcdef"
  }
}
```

```
// Email Open: users.messages.email.Open
{
  "event_type": "users.messages.email.Open",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "timezone": "America/Chicago"
  },
  "properties": {
    "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
    "campaign_name": "Test Campaign",
    "dispatch_id": "12345qwert",
    "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
    "message_variation_name": "Test Message Variation",
    "email_address": "test@test.com",
    "send_id": "f123456789abcdef01234567",
    "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
  }
}
```

```
// SMS Delivery: users.messages.sms.Delivery
{
  "event_type": "users.messages.sms.Delivery",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "timezone": "America/Chicago"
  },
  "properties": {
    "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
    "campaign_name": "Test Campaign",
    "dispatch_id": "12345qwert",
    "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
    "message_variation_name": "Test Message Variation",
    "to_phone_number": "+16462345678",
    "subscription_group_id": "41234567-89ab-cdef-0123-456789abcdef",
    "from_phone_number": "+12123470922"
  }
}
```

### Eventos asociados a Canvas

A continuación se muestran algunos ejemplos de cargas útiles para varios eventos, tal y como aparecerían si se asociaran a un Canvas:

```
// In-App Message Click: users.messages.inappmessage.Click
{
  "event_type": "users.messages.inappmessage.Click",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "canvas_id": "11234567-89ab-cdef-0123-456789abcdef",
    "canvas_name": "My Cool Campaign",
    "canvas_variation_id": "31234567-89ab-cdef-0123-456789abcdef",
    "canvas_step_id": "41234567-89ab-cdef-0123-456789abcdef",
    "platform": "android",
    "os_version": "Android (N)",
    "device_model": "Nexus 5X",
    "button_id": "0",
    "send_id": "f123456789abcdef01234567"
  }
}
```

```
// Push Notification Send: users.messages.pushnotification.Send
{
  "event_type": "users.messages.pushnotification.Send",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
    "canvas_id": "11234567-89ab-cdef-0123-456789abcdef",
    "canvas_name": "My Cool Campaign",
    "canvas_variation_id": "31234567-89ab-cdef-0123-456789abcdef",
    "canvas_step_id": "41234567-89ab-cdef-0123-456789abcdef",
    "send_id": "f123456789abcdef01234567",
    "dispatch_id": "01234567-89ab-cdef-0123-456789abcdef"
  }
}
```

```
// Email Open: users.messages.email.Open
{
  "event_type": "users.messages.email.Open",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "timezone": "America/Chicago"
  },
  "properties": {
    "canvas_id": "11234567-89ab-cdef-0123-456789abcdef",
    "canvas_name": "My Cool Canvas",
    "canvas_variation_id": "31234567-89ab-cdef-0123-456789abcdef",
    "canvas_step_id": "41234567-89ab-cdef-0123-456789abcdef",
    "dispatch_id": "12345qwert",
    "email_address": "test@test.com",
    "send_id": "f123456789abcdef01234567",
    "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
  }
}
```

```
// SMS Delivery: users.messages.sms.Delivery
{
  "event_type": "users.messages.sms.Delivery",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "timezone": "America/Chicago"
  },
  "properties": {
    "canvas_id": "11234567-89ab-cdef-0123-456789abcdef",
    "canvas_name": "My Cool Canvas",
    "canvas_variation_id": "31234567-89ab-cdef-0123-456789abcdef",
    "canvas_step_id": "41234567-89ab-cdef-0123-456789abcdef",
    "dispatch_id": "12345qwert",
    "to_phone_number": "+16462345678",
    "subscription_group_id": "41234567-89ab-cdef-0123-456789abcdef",
    "from_phone_number": "+12123470922"
  }
}
```

### Otros acontecimientos

A continuación se muestran algunos ejemplos de cargas útiles para otros eventos que no están asociados ni a campañas ni a lienzos:

```
// Custom Event: users.behaviors.CustomEvent
{
  "event_type": "users.behaviors.CustomEvent",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
    "os_version": "iOS 10.3.1",
    "device_model": "iPhone 7 Plus",
    "name": "custom event name",
    "ad_id": "01234567-89ab-cdef-0123-456789abcdef",
    "ad_id_type": "roku_ad_id",
    "ad_tracking_enabled": true,
    "custom_properties": {
      "string property name": "a",
      "number property name": 1,
      "list property name": ["a", "b"]
    }
  }
}
```

```
// Purchase Event: users.behaviors.Purchase
{
  "event_type": "users.behaviors.Purchase",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id"
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
    "os_version": "iOS 10.3.1",
    "device_model": "iPhone 7 Plus",
    "product_id": "1234",
    "price": 12.34,
    "currency": "AED,
    "ad_id": "01234567-89ab-cdef-0123-456789abcdef",
    "ad_id_type": "roku_ad_id",
    "ad_tracking_enabled": true,
    "purchase_properties": {
      "string property name": "a",
      "number property name": 1,
      "list property name": ["a", "b"]
    }
  }
}
```

```
// Session Start: users.behaviors.app.SessionStart
{
  "event_type": "users.behaviors.app.SessionStart",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
    "os_version": "iOS 10.3.1",
    "device_model": "iPhone 7 Plus",
    "session_id": "b1234567-89ab-cdef-0123-456789abcdef"
  }
}
```

## Autenticación

Si es necesario, la autenticación se realizará pasando un token en la cabecera de `Authorization` HTTP, mediante el esquema de autorización `Bearer`, tal y como se especifica en [el RFC 6750](https://tools.ietf.org/html/rfc6750#section-2.1). En el futuro, Braze puede optar por utilizar el encabezado `Authorization` para implantar un esquema de autorización personalizado (único para Braze) de par clave-valor conforme [al RFC 7235](https://tools.ietf.org/html/rfc7235) (que es como funciona, por ejemplo, el esquema de autenticación personalizado de AWS).

Según la RFC 6750, el token será un valor codificado en Base64 de al menos un carácter. Una peculiaridad notable del RFC 6750 es que permite que el token contenga los siguientes caracteres además de los caracteres normales de Base64: '-', '.', '_' y '~'. Los socios y clientes son libres de decidir si incluyen o no estos personajes en su token. Ten en cuenta que los clientes deben proporcionar este token en formato Base64; Braze no realizará esta codificación por nuestra parte.

Según el RFC 6750, la cabecera se construirá con el siguiente formato:

`"Authorization: Bearer " + <token>`

Así, por ejemplo, si el token de la API es `0p3n5354m3==`, la cabecera de autorización tendrá el siguiente aspecto:

`Authorization: Bearer 0p3n5354m3==`

## Control de versiones

Todas las solicitudes de nuestros Conectores HTTP integrables se enviarán con un encabezado personalizado que designa la versión de la solicitud de Currents que se está realizando:

`Braze-Currents-Version: 1`

La versión siempre será `1` a menos que realicemos cambios gravemente incompatibles con el pasado en la carga útil o la semántica de la solicitud. No tenemos previsto incrementar este número muy a menudo, si es que lo hacemos alguna vez.

Los eventos individuales seguirán las mismas reglas de evolución que nuestros esquemas S3 Avro existentes para la Exportación de Datos Currents. Es decir, se garantizará que los campos de cada evento sean compatibles con versiones anteriores de las cargas útiles de los eventos según la definición Avro de compatibilidad con versiones anteriores, incluidas las siguientes reglas:

- Se garantiza que los campos de eventos específicos tengan siempre el mismo tipo de datos a lo largo del tiempo.
- Cualquier nuevo campo que se añada a la carga útil con el tiempo debe ser considerado opcional por todas las partes.
- Los campos obligatorios nunca se eliminarán.

## Tratamiento de errores y mecanismo de reintento

En caso de error, Braze pondrá en cola y reintentará la solicitud en función del código de retorno HTTP recibido. Cualquier código de error HTTP que no figure a continuación se tratará como un error HTTP 5XX.

{% alert important %}
Si nuestro mecanismo de reintento no consigue entregar eventos a su punto final durante más de 24 horas, se producirá una pérdida de datos.
{% endalert %}

Los siguientes códigos de estado HTTP serán reconocidos por nuestro cliente conector:
- **2XX** \- Éxito
  - Los datos del evento no se reenviarán.<br><br>
- **5XX** \- Error del servidor
  - Los datos de eventos se reenviarán siguiendo un patrón de backoff exponencial con jitter. Si los datos no se envían correctamente en 24 horas, se descartarán.<br><br>
- **400** \- Error del lado del cliente
  - Nuestro conector de alguna manera envió al menos un evento malformado. Si esto ocurre, los datos del evento se dividirán en lotes de tamaño 1 y se volverán a enviar. Todos los eventos de estos lotes de tamaño 1 que reciban una respuesta HTTP 400 adicional se eliminarán de forma permanente. Animamos a nuestros socios y/o clientes a que nos informen si detectan que esto está ocurriendo.<br><br>
- **401** (No autorizado), **403** (Prohibido), **404**
  - El conector se ha configurado con credenciales no válidas. Los datos del suceso se reenviarán tras un retraso de entre 2 y 5 minutos. Si el cliente no resuelve este problema en un plazo de 48 horas, se eliminarán los datos del evento.<br><br>
- **413** \- Carga útil demasiado grande
  - Los datos del evento se dividirán en lotes más pequeños y se volverán a enviar.<br><br>
- **429** \- Demasiadas peticiones
  - Indica el límite de velocidad. Los datos de eventos se reenviarán siguiendo un patrón de backoff exponencial con jitter. Si los datos no se envían correctamente en 24 horas, se descartarán.