---
nav_title: Conector de corrientes personalizado
alias: /currents_connector/
hidden: true
---

# Conector Currents personalizado

> Aprende a integrar un conector Currents personalizado, para que puedas obtener datos de eventos de Braze en tiempo real, habilitando análisis, informes y automatización más personalizados.

## Requisitos previos

Para integrar un conector de Currents personalizado en Braze, tendrás que proporcionar una URL de punto final y un [token de autenticación opcional](#authentication).

Además, si tienes más de un grupo de aplicaciones en Braze, tendrás que configurar un conector Currents personalizado para cada grupo. Sin embargo, puedes dirigir todos los grupos de aplicaciones al mismo punto final, o a un punto final con un parámetro adicional `GET`, como `your_app_group_key=”Brand A”`.

## Evitar la pérdida de datos

### Control de errores

Para evitar la pérdida de datos y la interrupción del servicio, es esencial que supervises tus puntos finales en todo momento y que intentes solucionar los errores graves o el tiempo de inactividad en un plazo de 24 horas.

Para la mayoría de los tipos de error (como errores del servidor, errores de conexión a la red, etc.), Braze continuará poniendo en cola y reintentando las transmisiones de eventos durante un máximo de 24 horas. Pasado ese tiempo, se descartarán los eventos no transmitidos. Los conectores con tasas de error o tiempo de actividad constantemente bajos se suspenderán automáticamente.

### Cambiar la resiliencia

Ocasionalmente, realizaremos cambios no radicales en los esquemas de Braze Currents. Los cambios que no se rompen son nuevas columnas anulables o tipos de eventos.

Normalmente avisamos de estos cambios con dos semanas de antelación, pero a veces no es posible. Es esencial que diseñes tu integración para manejar campos o tipos de eventos no reconocidos, de lo contrario es probable que se produzca una pérdida de datos.

{% alert tip %}
Para consultar la lista completa de esquemas de eventos Currents, [Eventos de interacción con mensajes]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events).
{% endalert %}

## Procesamiento por lotes y serialización

El formato de datos de destino es JSON sobre HTTPS. Por predeterminado, los eventos se agrupan en lotes de 100 en función de lo siguiente:

- **Número de eventos en cola**: Por ejemplo, si el tamaño del lote está configurado para 200 eventos y hay 200 eventos en la cola.
- **Duración de un evento:** Normalmente, los eventos no se ponen en cola si duran más de 15 minutos. Cada tipo de evento tiene una cola independiente, por lo que la latencia puede variar según el tipo de evento.

A continuación, los eventos se envían al punto final como una matriz JSON de todos los eventos con el siguiente formato:

```json
{"events": [event1, event2, event3, etc...]}
```

Habrá un objeto JSON de nivel superior con la clave `"events"` que mapeará a una matriz de otros objetos JSON, cada uno de los cuales representará un único evento.

## Ejemplos de carga útil

Los siguientes ejemplos muestran cargas útiles para eventos individuales, lo que significa que las cargas útiles pertenecerían a una matriz mayor de objetos JSON, donde cada objeto JSON representa un único evento del lote.

Además, su estructura varía ligeramente de la estructura plana de [los Eventos de interacción con mensajes]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events). En concreto, contienen dos subobjetos:

|Apellidos|Descripción|
|----|-----------|
|`"user"`|Contiene propiedades de usuario como `user_id`, `external_user_id`, `device_id` y `timezone`.|
|`"properties"`|Contiene atributos de un suceso, como el `app/campaign/canvas/platform` al que se aplica.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Si un punto final descendente recibe una carga útil con cero eventos o un cuerpo de solicitud vacío, el resultado debe considerarse un no-op, lo que significa que no deben producirse efectos descendentes de esta llamada. Sin embargo, debes seguir comprobando el encabezado `Authorization` (como harías con una llamada normal a la API), y dar una respuesta HTTP adecuada para las [credenciales no válidas](#authentication), como `401` o `403`. Esto permite a Braze saber que las credenciales del conector son válidas.

### Actos relacionados con la campaña

A continuación se muestran algunos ejemplos de cargas útiles para varios eventos, tal y como aparecerían si estuvieran asociados a una campaña:

#### Clic en mensaje dentro de la aplicación

```json
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

#### Envío de notificación push

```json
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

#### Apertura del correo electrónico

```json
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

#### Entrega de SMS

```json
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

#### Clic en mensaje dentro de la aplicación

```json
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

#### Envío de notificación push

```json
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

#### Apertura del correo electrónico

```json
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

#### Entrega de SMS

```json
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

#### Evento personalizado

```json
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

#### Evento de compra

```json
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

#### Comienzo de sesión

```json
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

Los tokens de autenticación en tu carga útil son opcionales. Se pueden pasar a través de una cabecera HTTP `Authorization` utilizando el esquema de autorización `Bearer`, tal y como se especifica en [el RFC 6750](https://tools.ietf.org/html/rfc6750#section-2.1). Aunque es opcional, si se pasa un token de autenticación, Braze siempre lo validará primero, aunque no haya eventos en la carga útil.

Según la RFC 6750, los tokens deben ser valores codificados en Base64 con al menos un carácter. Ten en cuenta que la RFC 6750 permite que los tokens contengan los siguientes caracteres, además de los caracteres normales de Base64: `-`, `.`, `_`, y `~`. Puedes elegir si quieres incluir o no estos caracteres en tu token; sin embargo, debe estar en formato Base64.

Además, si la cabecera `Authorization` está presente, se construirá con el siguiente formato:

```plaintext
"Authorization: Bearer " + <token>
```

Por ejemplo, si tu token de autenticación es `0p3n5354m3==`, tu cabecera `Authorization` debería ser similar a la siguiente:

```plaintext
Authorization: Bearer 0p3n5354m3==
```

{% alert note %}
En el futuro, podemos utilizar las cabeceras `Authorization` para implementar un esquema de autorización personalizado, par clave-valor, que sea único para Braze. Esto se adheriría a la especificación [RFC 7235](https://tools.ietf.org/html/rfc7235), que es como algunas empresas implementan sus esquemas de autenticación, como Amazon Web Services (AWS).
{% endalert %}

## Control de versiones

Todas las solicitudes de nuestra integración de conector HTTP se enviarán con un encabezado personalizado que designará la versión de la solicitud de Currents que se está realizando:

```plaintext
Braze-Currents-Version: 1
```

La versión siempre será `1` a menos, ya que no esperamos incrementar este número muy a menudo, si es que lo hacemos alguna vez.

Al igual que los [esquemas de almacenamiento de nuestro almacén de datos]({{site.baseurl}}/user_guide/data/braze_currents/event_delivery_semantics?redirected=1), se garantiza que cada campo de evento de un evento individual es compatible con versiones anteriores de la carga útil del evento, según la definición de compatibilidad con versiones anteriores de [Apache Avro](https://avro.apache.org/):

1. Se garantiza que los campos de eventos específicos tengan siempre el mismo tipo de datos a lo largo del tiempo.
2. Cualquier nuevo campo que se añada a la carga útil con el tiempo debe ser considerado opcional por todas las partes.
3. Los campos obligatorios nunca se eliminarán.

## Tratamiento de errores y mecanismo de reintento

Si se produce un error, Braze pondrá en cola y reintentará la solicitud en función del código de retorno HTTP recibido. Seguirá intentándolo durante al menos dos días, mientras haya datos almacenados en el sistema. Si los datos se bloquean durante más de 24 horas, nuestros ingenieros de guardia serán alertados automáticamente. En este momento, nuestra estrategia de reintento es reintentar periódicamente.

Si tu integración de Currents empieza a devolver errores `4XX`, Braze te enviará automáticamente un correo electrónico de notificación y ampliará automáticamente el periodo de retención a un mínimo de siete días.

Cualquier código de error HTTP que no aparezca a continuación se tratará como un error HTTP `5XX`.

{% alert warning %}
Si el mecanismo de reintento de Braze no entrega un evento durante más de 24 horas, se producirá una pérdida de datos.
{% endalert %}

Los siguientes códigos de estado HTTP serán reconocidos por nuestro cliente conector:

<table>
  <thead>
    <tr>
      <th>Código de estado</th>
      <th>Respuesta</th>
      <th>Descripción</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>2XX</code></td>
      <td>Correcto</td>
      <td>Los datos del evento no se reenviarán.</td>
    </tr>
    <tr>
      <td><code>5XX</code></td>
      <td>Error del lado del servidor</td>
      <td>Los datos de eventos se reenviarán siguiendo un patrón de backoff exponencial con jitter. Si los datos no se envían correctamente en 24 horas, se descartarán.</td>
    </tr>
    <tr>
      <td><code>400</code></td>
      <td>Error del lado del cliente</td>
      <td>El conector envió al menos un evento malformado. Los datos del suceso se dividirán en lotes de tamaño 1 y se volverán a enviar. Cualquier suceso de estos lotes de tamaño 1 que reciba otro <code>400</code> respuesta se eliminará de forma permanente. Debes denunciar los casos repetidos.</td>
    </tr>
    <tr>
      <td><code>401</code></td>
      <td>No autorizado</td>
      <td>El conector se ha configurado con credenciales no válidas. Los datos del evento se volverán a enviar tras un retraso de 2-5 minutos. Si no se resuelve en 48 horas, se eliminarán los datos del evento.</td>
    </tr>
    <tr>
      <td><code>403</code></td>
      <td>Prohibido</td>
      <td>El conector se ha configurado con credenciales no válidas. Los datos del evento se volverán a enviar tras un retraso de 2-5 minutos. Si no se resuelve en 48 horas, se eliminarán los datos del evento.</td>
    </tr>
    <tr>
      <td><code>404</code></td>
      <td>No se ha encontrado</td>
      <td>El conector se ha configurado con credenciales no válidas. Los datos del evento se volverán a enviar tras un retraso de 2-5 minutos. Si no se resuelve en 48 horas, se eliminarán los datos del evento.</td>
    </tr>
    <tr>
      <td><code>413</code></td>
      <td>Payload demasiado grande</td>
      <td>Los datos del evento se dividirán en lotes más pequeños y se volverán a enviar.</td>
    </tr>
    <tr>
      <td><code>429</code></td>
      <td>Demasiadas peticiones</td>
      <td>Indica el límite de velocidad. Los datos de eventos se reenviarán siguiendo un patrón de backoff exponencial con jitter. Si no se envía correctamente en 24 horas, se descartará.</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
