---
nav_title: Errores y respuestas
article_title: Errores y respuestas de la API
description: "Este artículo de referencia cubre los distintos errores y respuestas del servidor que pueden surgir al utilizar la API de Braze y cómo solucionarlos."
page_type: reference
page_order: 2.3

---
# Errores y respuestas de la API

> Este artículo de referencia cubre los distintos errores y respuestas del servidor que pueden surgir al utilizar la API de Braze y cómo solucionarlos.

## Respuestas del servidor

Si nuestros servidores han aceptado tu carga útil POST, los mensajes correctos recibirán la siguiente respuesta:

```json
{
  "message" : "success"
}
```

Ten en cuenta que el éxito solo significa que la carga útil de la API RESTful se formó correctamente y se transmitió a nuestros servicios de notificación push, correo electrónico u otros servicios de mensajería. Esto no significa que los mensajes se hayan entregado realmente, ya que hay factores adicionales que podrían impedir la entrega del mensaje (por ejemplo, un dispositivo podría estar desconectado, el token de notificaciones push podría ser rechazado por los servidores de Apple o podrías haber proporcionado un ID de usuario desconocido).

Para puntos de conexión como [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify), que no envían mensajes, un mensaje de éxito solo significa que Braze ha recibido la solicitud para su procesamiento. Si no hay ninguna coincidencia para el alias después del procesamiento, la solicitud se detiene.

Si tu mensaje se envía correctamente pero contiene errores no fatales, recibirás la siguiente respuesta:

```json
{
  "message" : "success", "errors" : [<minor error message>]
}
```

En caso de éxito, los mensajes que no se hayan visto afectados por un error en la matriz `errors` se seguirán entregando. Si tu mensaje contiene un error fatal, recibirás la siguiente respuesta:

```json
{
  "message" : <fatal error message>, "errors" : [<minor error message>]
}
```

## Respuestas para los ID de envío rastreados

Los análisis están siempre disponibles para las campañas. Además, los análisis están disponibles para una instancia de envío de campaña específica cuando la campaña se envía como difusión. Cuando el seguimiento está disponible para una instancia de envío de campaña específica, recibes la siguiente respuesta:

```json
{
  "message": "success", "send_id" : "example_send_id"
}
```

El identificador de envío proporcionado puede utilizarse como parámetro para que el punto de conexión `/send/data_series` recupere análisis específicos del envío.

## Errores

El elemento de código de estado de una respuesta del servidor es un número de 3 dígitos en el que el primer dígito del código define la clase de respuesta.

- La **clase 2XX** de código de estado (no fatal) indica que **tu solicitud** ha sido recibida, comprendida y aceptada correctamente.
- La **clase 4XX** de código de estado (fatal) indica un **error del cliente**. Consulta la tabla de errores fatales para obtener una lista completa de los códigos de error 4XX y sus descripciones.
- La **clase 5XX** de código de estado (fatal) indica un **error del servidor**. Hay varias causas posibles, por ejemplo, el servidor al que intentas acceder no puede ejecutar la solicitud, el servidor está en mantenimiento por lo que no puede ejecutar la solicitud, o el servidor está experimentando altos niveles de tráfico. Cuando esto ocurra, te recomendamos que reintentes tu solicitud con retirada exponencial. En caso de incidente o interrupción, Braze no puede reproducir ninguna llamada a la API REST que haya fallado durante la ventana del incidente. Debes volver a intentar cualquier llamada que haya fallado durante la ventana del incidente.
  - Un **error 502** es un fallo que se produce antes de llegar al servidor de destino.
  - Un **error 503** significa que la solicitud llegó al servidor de destino, pero no podemos completarla porque no hay suficiente capacidad, hay un problema de red o algo similar.
  - Un **error 504** indica que un servidor no ha recibido una respuesta de otro servidor ascendente.

### Errores fatales

Si tu solicitud encuentra un error fatal, se devolverán los siguientes códigos de estado y mensajes de error asociados.

{% alert warning %}
Todos los siguientes códigos de error indican que no se envían mensajes.
{% endalert %}

| Código de error | Descripción |
|---|---|
| `5XX Internal Server Error` | Reintenta tu solicitud con retirada exponencial.|
| `400 Bad Request` | Sintaxis incorrecta.|
| `400 No Recipients` | No hay ID externos o ID de segmento, ni tokens push en la solicitud.|
| `400 Invalid Campaign ID` | No se ha encontrado ninguna campaña de la API de mensajería para el ID de campaña proporcionado.|
| `400 Message Variant Unspecified` | Proporcionas un ID de campaña pero no un ID de variación de mensaje.|
| `400 Invalid Message Variant` | Has proporcionado un ID de campaña válido, pero el ID de variación del mensaje no coincide con ninguno de los mensajes de esa campaña.|
| `400 Mismatched Message Type` | Has proporcionado una variación de mensaje del tipo de mensaje incorrecto para al menos uno de tus mensajes.|
| `400 Invalid Extra Push Payload` | Proporcionas la clave `extra` para `apple_push` o `android_push` pero no es un diccionario.|
| `400 Max Input Length Exceeded` | Para `/users/track`, este error se produce al superar el número máximo de objetos permitidos en una sola solicitud. El límite depende del modelo de límite de velocidad: para la mayoría de los clientes, cada solicitud admite hasta 75 objetos en total combinados entre `attributes`, `events` y `purchases`. Para clientes con límites de velocidad heredados, cada matriz admite hasta 75 objetos de forma independiente. Para más información, consulta [POST: Crear y actualizar usuarios]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).|
| `400 The max number of external_ids and aliases per request was exceeded` | Causado por llamar a más de 50 ID externos.|
| `400 The max number of ids per request was exceeded` | Causado por llamar a más de 50 ID externos.|
| `400 No message to send` | No se especifica ninguna carga útil para el mensaje.|
| `400 Slideup Message Length Exceeded` | El mensaje de deslizamiento hacia arriba contiene más de 140 caracteres.|
| `400 Apple Push Length Exceeded` | La carga útil JSON es superior a 1.912 bytes.|
| `400 Android Push Length Exceeded` | La carga útil JSON es superior a 4.000 bytes.|
| `400 Bad Request` | No se puede analizar el datetime `send_at`.|
| `400 Bad Request` | En tu solicitud, `in_local_time` es verdadero pero `time` ya ha pasado en la zona horaria de tu empresa.|
| `401 Unauthorized` | Clave de API no válida. Las causas comunes incluyen:<br><br>- **Encabezado de autorización ausente o mal formado.** El valor del encabezado debe ser `Bearer` seguido de un espacio y luego tu clave de API: `Authorization: Bearer YOUR-API-KEY`. Los errores comunes incluyen omitir `Bearer`, omitir la clave después de `Bearer` o envolver el valor entre comillas.<br>- **Punto de conexión REST incorrecto.** Estás enviando la solicitud a la [instancia]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) incorrecta. Por ejemplo, si tu cuenta se encuentra en nuestra instancia de la UE (`https://dashboard-01.braze.eu`), la solicitud debe enviarse a `https://rest.fra-01.braze.eu`.<br>- **Permisos insuficientes.** Cada clave de API está asociada a un espacio de trabajo y un conjunto de permisos específicos. Verifica los permisos de la clave en **Configuración** > **Claves de API** en el dashboard.<br>- **Clave de API incorrecta.** Las claves de API son específicas de cada espacio de trabajo. Una clave de un espacio de trabajo no puede utilizarse para autenticar solicitudes de un espacio de trabajo diferente. |
| `403 Forbidden` | No se admite el plan de tarifas o la cuenta se ha desactivado por cualquier otro motivo.|
| `403 Access Denied` | La clave de API REST que estás utilizando no tiene permisos suficientes. Las causas comunes incluyen: {::nomarkdown}<ul><li><strong>La clave de API es anterior a la característica.</strong> Si la clave de API se creó antes del lanzamiento de una característica (como grupos de suscripción o catálogos), la clave no hereda automáticamente esos permisos. Crea una nueva clave de API con los permisos necesarios en <strong>Configuración</strong> &gt; <strong>Claves de API</strong>.</li><li><strong>Falta el permiso específico del punto de conexión.</strong> Cada punto de conexión de la API requiere un ámbito de permiso específico (por ejemplo, <code>users.track</code> o <code>email.status</code>). Verifica que los permisos de la clave coincidan con el punto de conexión al que estás llamando.</li><li><strong>Barra diagonal final o error tipográfico en la URL.</strong> Por ejemplo, <code>/users/track/</code> (con barra diagonal final) en lugar de <code>/users/track</code> puede producir errores inesperados.</li></ul>{:/}|
| `404 Not Found` | URL no válida. |
| `415 Unsupported Media Type` | El encabezado de solicitud `Content-Type` falta o es incorrecto. En la página de **Configuración**, añade `Content-Type` con el valor `application/json`. |
| `429 Rate Limited` | Por encima del límite de velocidad. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }