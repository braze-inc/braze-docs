---
nav_title: Errores y respuestas
article_title: Errores y respuestas de la API
description: "Este artículo de referencia cubre los distintos errores y respuestas del servidor que pueden surgir al utilizar la API de Braze y cómo solucionarlos." 
page_type: reference
page_order: 2.3

---
# Errores y respuestas de la API

> Este artículo de referencia cubre los distintos errores y respuestas del servidor que pueden surgir al utilizar la API de Braze y cómo solucionarlos. 

{% raw %}

## Respuestas del servidor

Si nuestros servidores aceptaron la payload de tu POST, recibirá un mensaje exitoso con la siguiente respuesta:

```json
{
  "message" : "success"
}
```

Ten en cuenta que el éxito solo significa que la payload de la API RESTful se formó correctamente y se pasó a nuestra notificación push, correo electrónico u otros servicios de mensajería. Esto no significa que los mensajes hayan sido realmente entregados, ya que otros factores podrían impedir la entrega del mensaje (por ejemplo, un dispositivo podría estar fuera de línea, el token push podría ser rechazado por los servidores de Apple, puede que hayas proporcionado un ID de usuario desconocido).

Si tu mensaje tiene éxito, pero contiene errores no fatales, recibirás la siguiente respuesta:

```json
{
  "message" : "success", "errors" : [<minor error message>]
}
```

En caso de éxito, los mensajes que no se hayan visto afectados por un error en la matriz `errors` se seguirán enviando. Si tu mensaje tiene un error fatal recibirás la siguiente respuesta:

```json
{
  "message" : <fatal error message>, "errors" : [<minor error message>]
}
```

## Respuestas para los ID de envío rastreados

Los análisis están siempre disponibles para las campañas. Además, los análisis están disponibles para una instancia de envío de campaña específica cuando la campaña se envía como difusión. Cuando el seguimiento esté disponible para una instancia de envío de campaña específica, recibirá la siguiente respuesta:

```json
{
  "message": "success", "send_id" : "example_send_id"
}
```

El identificador de envío proporcionado puede utilizarse como parámetro para que el punto final `/send/data_series` recupere análisis específicos del envío.

## Errores

El elemento de código de estado de una respuesta del servidor es un número de 3 dígitos en el que el primer dígito del código define la clase de respuesta.

- La **clase** de código de estado **2XX** (no fatal) indica que **su solicitud** ha sido recibida, comprendida y aceptada correctamente.
- La **clase** de código de estado **4XX** (fatal) indica un **error del cliente**. Consulte la tabla de errores fatales para obtener una lista completa de los códigos de error 4XX y sus descripciones.
- La **clase** de código de estado **5XX** (fatal) indica un **error del servidor**. Hay varias causas posibles, por ejemplo, el servidor al que intenta acceder no puede ejecutar la solicitud, el servidor está en mantenimiento por lo que no puede ejecutar la solicitud, o el servidor está experimentando altos niveles de tráfico. Cuando esto ocurra, le recomendamos que reintente su petición con un backoff exponencial. En caso de incidente o interrupción, Braze no puede reproducir ninguna llamada a la API REST que haya fallado durante la ventana del incidente. Deberá reintentar las llamadas que hayan fallado durante la ventana de incidencias.
  - Un **error 502** es un fallo antes de llegar al servidor de destino.
  - Un **error 503** significa que la solicitud ha llegado al servidor de destino, pero no podemos completarla porque no hay capacidad suficiente, o hay un problema de red, o algo similar.
  - Un **error 504** indica que un servidor no ha recibido una respuesta de otro servidor anterior.

### Errores fatales

Los siguientes códigos de estado y mensajes de error asociados serán devueltos si su solicitud encuentra un error fatal.

{% endraw %}
{% alert warning %}
Todos los códigos de error siguientes indican que no se enviará ningún mensaje.
{% endalert %}
{% raw %}

| Código de error | Descripción |
|---|---|
| `5XX Internal Server Error` | Reintenta tu solicitud con retirada exponencial.|
| `400 Bad Request` | Mala sintaxis.|
| `400 No Recipients` | No hay IDs externos o IDs de segmento, o no hay tokens push en la solicitud.|
| `400 Invalid Campaign ID` | No se ha encontrado ninguna campaña de la API de mensajería para el ID de campaña proporcionado.|
| `400 Message Variant Unspecified` | Usted proporciona un ID de campaña pero no un ID de variación de mensaje.|
| `400 Invalid Message Variant` | Has proporcionado un ID de campaña válido, pero el ID de variación del mensaje no coincide con ninguno de los mensajes de esa campaña.|
| `400 Mismatched Message Type` | Ha proporcionado una variación de mensaje del tipo de mensaje incorrecto para al menos uno de sus mensajes.|
| `400 Invalid Extra Push Payload` | Proporcionas la clave `extra` para `apple_push` o `android_push` pero no es un diccionario.|
| `400 Max Input Length Exceeded` | Causado por la llamada a más de 75 ID externos al acceder al punto final `/users/track`.|
| `400 The max number of external_ids and aliases per request was exceeded` | Causado por llamar a más de 50 ID externos.|
| `400 The max number of ids per request was exceeded` | Causado por llamar a más de 50 ID externos.|
| `400 No message to send` | No se especifica ninguna carga útil para el mensaje.|
| `400 Slideup Message Length Exceeded` | El mensaje de Slideup contiene más de 140 caracteres.|
| `400 Apple Push Length Exceeded` | La carga útil JSON es superior a 1.912 bytes.|
| `400 Android Push Length Exceeded` | La carga útil JSON es superior a 4.000 bytes.|
| `400 Bad Request` | No se puede analizar datetime `send_at`.|
| `400 Bad Request` | En su solicitud, `in_local_time` es cierto pero `time` ya ha pasado en la zona horaria de su empresa.|
| `401 Unauthorized` | Clave de API no válida. Este error también puede producirse si<br><br> \- Estás enviando la solicitud a la [instancia]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) incorrecta. Por ejemplo, si tu cuenta está en nuestra instancia de la UE (`https://dashboard-01.braze.eu`), la solicitud debe enviarse a `https://rest.fra-01.braze.eu`.<br>\- La sintaxis de la clave de API es utilizar comillas simples o dobles. La sintaxis correcta es `Authorization: Bearer {YOUR-API-KEY}`. |
| `403 Forbidden` | No se admite el plan de tarifas o la cuenta se desactiva por cualquier otro motivo.|
| `403 Access Denied` | La clave API REST que está utilizando no tiene permisos suficientes, compruebe los permisos de la clave API en la página **Configuración**.|
| `404 Not Found` | URL no válida. |
| `429 Rate Limited` | Por encima del límite de velocidad. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endraw %}
