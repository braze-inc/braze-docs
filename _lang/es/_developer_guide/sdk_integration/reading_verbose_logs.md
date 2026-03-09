---
page_order: 1.5
nav_title: Lectura de registros detallados
article_title: Lectura de registros detallados
description: "Aprende a leer e interpretar los registros detallados del SDK de Braze, incluidas las entradas clave para notificaciones push, mensajes dentro de la aplicación, tarjetas de contenido y vínculos profundos."
---

# Lectura de registros detallados

> En esta página se explica cómo interpretar la salida detallada del registro del SDK de Braze. Para cada canal de mensajería, encontrarás las entradas clave del registro que debes buscar, su significado y los problemas comunes a los que debes prestar atención.

Antes de empezar, asegúrate de haber [habilitado el registro detallado]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging) y de saber cómo recopilar registros en tu plataforma.

## Sesiones

Las sesiones son la base del análisis y la entrega de mensajes de Braze. Muchas características de mensajería, incluidos los mensajes dentro de la aplicación y las tarjetas de contenido, dependen de que se inicie una sesión válida antes de que puedan funcionar. Si las sesiones no se registran correctamente, investiga esto primero. Para obtener más información sobre cómo habilitar el seguimiento de sesiones, consulta [el Paso 5: Habilita el seguimiento de ]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_step-5-enable-user-session-tracking)sesiones de usuario.

### Entradas clave del registro

{% tabs %}
{% tab Swift %}

**Inicio de la sesión:**

```
Started user session (id: <SESSION_ID>)
```

**Fin de la sesión:**

```
Ended user session (id: <SESSION_ID>, duration: <DURATION>s)
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: sessionEnd(duration: <DURATION>)
```

{% endtab %}
{% tab Android %}

**Inicio de la sesión:**

Busca las siguientes entradas:

```
New session created with ID: <SESSION_ID>
Session start event for new session received
Completed the openSession call
Opened session with activity: <ACTIVITY_NAME>
```

Filtra las solicitudes de red para tu punto final Braze configurado (por ejemplo, sdk.iad-01.braze.com) para ver el evento de inicio de sesión (`ss`).

**Fin de la sesión:**

```
Closed session with activity: <ACTIVITY_NAME>
Closed session with session ID: <SESSION_ID>
Requesting data flush on internal session close flush timer.
```

{% endtab %}
{% endtabs %}

### Qué hay que comprobar

- Comprueba que aparece un registro de inicio de sesión cuando se inicia la aplicación.
- Si no ves que se inicia una sesión, comprueba que el SDK esté correctamente inicializado y que`openSession`  (Android) se esté llamando.
- En Android, confirma que se está realizando una solicitud de red al punto final de Braze. Si no ves esto, verifica tu clave de API y la configuración del punto final.

## Notificaciones push

Los registros de notificaciones push te ayudan a verificar que los tokens de los dispositivos estén registrados, que las notificaciones se entreguen correctamente y que se realice el seguimiento de los eventos de clic.

### Registro de tokens

Cuando se inicia una sesión, el SDK realiza el registro del token de notificaciones push del dispositivo en Braze.

{% tabs %}
{% tab Swift %}

```
Updated push notification authorization:
- authorization: authorized

Received remote notifications device token: <PUSH_TOKEN>
```

Filtra las solicitudes a tu punto final Braze configurado (por ejemplo, sdk.iad-01.braze.com) y busca`push_token`  en los atributos del cuerpo de la solicitud:

```
"attributes": [
  {
    "push_token": "<PUSH_TOKEN>",
    "user_id": "<USER_ID>"
  }
]
```

Confirma también que la información del dispositivo incluye:

```
"device": {
  "ios_push_auth": "authorized",
  "remote_notification_enabled": 1
}
```

{% endtab %}
{% tab Android %}

Busca el registro de inscripción en FCM:

```
Registering for Firebase Cloud Messaging token using sender id: <SENDER_ID>
```

Verifica lo siguiente:

- `com_braze_firebase_cloud_messaging_registration_enabled` es `true`.
- El ID del remitente FCM coincide con tu proyecto Firebase.

Un error común es `SENDER_ID_MISMATCH`, lo que significa que el ID de remitente configurado no coincide con tu proyecto de Firebase.

{% endtab %}
{% endtabs %}

### Qué hay que comprobar

- Si  no`push_token` aparece en el cuerpo de la solicitud, significa que no se ha capturado el token. Verifica la configuración de push en la configuración de tu aplicación.
- Si`ios_push_auth`muestra`denied`  o `provisional`, el usuario no ha concedido permiso push completo.
- En Android, si ves `SENDER_ID_MISMATCH`, actualiza tu ID de remitente FCM para que coincida con tu proyecto Firebase.

### Entrega urgente y clic

Cuando se pulsa una notificación push, el SDK registra los eventos de procesamiento y clic.

{% tabs %}
{% tab Swift %}

```
Processing push notification:
- date: <TIMESTAMP>
- silent: false
- userInfo: {
  "ab": { ... },
  "ab_uri": "<DEEP_LINK_OR_URL>",
  "aps": {
    "alert": {
      "body": "<MESSAGE_BODY>",
      "title": "<MESSAGE_TITLE>"
    }
  }
}
```

Seguido del evento de clic:

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: pushClick(campaignId: ...)
```

Si la push contiene un vínculo profundo, también verás:

```
Opening '<URL>':
- channel: notification
- useWebView: false
- isUniversalLink: false
```

{% endtab %}
{% tab Android %}

```
BrazeFirebaseMessagingService: Got Remote Message from FCM
```

A continuación, se muestran los registros de carga útil y visualización. Para vínculos profundos, busca las entradas Deep Link `UriAction`Delegate o .

{% endtab %}
{% endtabs %}

### Qué hay que comprobar

- Verifica que la carga útil del push contenga lo esperado`title`,`body` , y cualquier vínculo profundo (`ab_uri`).
- Confirma que se registra un`pushClick`evento después de tocar.
- Si falta el evento de clic, comprueba que el delegado de tu aplicación o el controlador de notificaciones estén reenviando correctamente los eventos push al SDK de Braze.

## Mensajes dentro de la aplicación

Los registros de mensajes dentro de la aplicación muestran el ciclo de vida completo: entrega desde el servidor, desencadenamiento basado en eventos, visualización, registro de impresiones y seguimiento de clics.

### Entrega de mensajes

Cuando un usuario inicia una sesión y es elegible para recibir un mensaje dentro de la aplicación, el SDK recibe la carga útil del mensaje desde el servidor.

{% tabs %}
{% tab Swift %}

Filtra las respuestas de tu punto final Braze configurado (por ejemplo, sdk.iad-01.braze.com) que contengan los datos de los mensajes dentro de la aplicación.

El cuerpo de la respuesta contiene la carga útil del mensaje, que incluye:

```
"templated_message": {
  "data": {
    "message": "...",
    "type": "HTML",
    "message_close": "SWIPE",
    "trigger_id": "<TRIGGER_ID>"
  },
  "type": "inapp"
}
```

{% endtab %}
{% tab Android %}

Busca el registro que coincide con el evento que desencadena:

```
Triggering action: <CAMPAIGN_BSON_ID>
```

Esto confirma que el mensaje dentro de la aplicación se correspondía con un evento desencadenante.

{% endtab %}
{% endtabs %}

### Visualización e impresión de mensajes

{% tabs %}
{% tab Swift %}

```
In-app message ready for display:
- triggerId: (campaignId: <CAMPAIGN_ID>, ...)
- extras: { ... }
```

A continuación, el registro de impresiones:

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: inAppMessageImpression(triggerIds: [...])
```

{% endtab %}
{% tab Android %}

```
handleExistingInAppMessagesInStackWithDelegate:: Displaying in-app message
```

{% endtab %}
{% endtabs %}

### Eventos de clic y botón

Cuando un usuario pulsa un botón o cierra el mensaje:

{% tabs %}
{% tab Swift %}

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: inAppMessageButtonClick(triggerIds: [...], buttonId: "<BUTTON_ID>")
```

Si no hay más mensajes desencadenados que coincidan, también verás:

```
No matching trigger for event.
```

Este es el comportamiento esperado cuando no se configuran mensajes adicionales dentro de la aplicación para el evento.

{% endtab %}
{% tab Android %}

Filtra las solicitudes a tu punto final Braze configurado (por ejemplo, sdk.iad-01.braze.com) y busca eventos con el nombre`sbc`  (clic en el botón) o`si`  (impresión) en el cuerpo de la solicitud.

{% endtab %}
{% endtabs %}

### Qué hay que comprobar

- Si no se muestra el mensaje dentro de la aplicación, comprueba primero que se haya registrado el inicio de la sesión.
- Filtra las respuestas de tu punto final Braze configurado para confirmar que se ha entregado la carga útil del mensaje.
- Si las impresiones no se registran, comprueba que no hayas implementado un delegado `inAppMessageDisplay`personalizado que suprima el registro.
- Si aparece «No hay ningún activador que coincida con el evento», es normal y significa que no hay ningún mensaje adicional dentro de la aplicación configurado para ese evento.

## Tarjetas de contenido

Los registros de tarjetas de contenido te ayudan a verificar que las tarjetas se sincronizan con el dispositivo, se muestran al usuario y que se realiza el seguimiento de las interacciones (impresiones, clics, rechazos).

### Sincronización de tarjetas

Las tarjetas de contenido se sincronizan al inicio de la sesión y cuando se solicita una actualización manual. Si no hay ninguna sesión registrada, no se muestran tarjetas de contenido.

{% tabs %}
{% tab Swift %}

Filtra las respuestas de tu punto final Braze configurado (por ejemplo, sdk.iad-01.braze.com) que contengan los datos de la tarjeta.

El cuerpo de la respuesta contiene los datos de la tarjeta, incluyendo:

```
"cards": [
  {
    "id": "<CARD_ID>",
    "tt": "<CARD_TITLE>",
    "ds": "<CARD_DESCRIPTION>",
    "tp": "short_news",
    "v": 0,
    "cl": 0,
    "p": 1
  }
]
```

Campos clave:
- `v` (visto):`0`  = no visto,`1`  = visto
- `cl` (clic):`0`  = sin clic,`1`  = clic
- `p` (fijado):`0`  = no fijado,`1`  = fijado
- `tp` (tipo): `short_news`, `captioned_image`, `classic`, etc.

{% endtab %}
{% tab Android %}

```
Requesting content cards sync.
```

A continuación, se envía una solicitud POST al punto final de Braze que hayas configurado (por ejemplo, sdk.iad-01.braze.com) con información sobre el usuario y el dispositivo.

{% endtab %}
{% endtabs %}

### Impresiones, clics y rechazos

{% tabs %}
{% tab Swift %}

**impresión:**

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: contentCardImpression(cardIds: [...])
```

**Clic:**

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: contentCardClick(cardIds: [...])
```

Si la tarjeta tiene una URL, también verás:

```
Opening '<URL>':
- channel: contentCard
- useWebView: true
```

**Despido:**

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: contentCardDismissed(cardIds: [...])
```

{% endtab %}
{% tab Android %}

Filtra las solicitudes a tu punto final Braze configurado (por ejemplo, sdk.iad-01.braze.com) y busca los nombres de los eventos en el cuerpo de la solicitud:
- `cci` — Impresión de la tarjeta de contenido
- `ccc` — Tarjeta de contenido clic
- `ccd` — Tarjeta de contenido descartada

{% endtab %}
{% endtabs %}

### Qué hay que comprobar

- **No se muestran tarjetas**: Verifica que se haya registrado el inicio de la sesión. Las tarjetas de contenido requieren una sesión activa para sincronizarse.
- **Faltan tarjetas para los nuevos usuarios**: Es posible que los nuevos usuarios no vean las tarjetas de contenido en su primera sesión hasta la siguiente sesión. Este es el comportamiento esperado.
- **La tarjeta supera el límite de tamaño**: Las tarjetas de contenido de más de 2 KB no se muestran y el mensaje se cancela.
- **La tarjeta persiste después de detener la campaña**: Comprueba que la sincronización se haya completado después de detener la campaña. Las tarjetas de contenido se eliminan del dispositivo después de una sincronización correcta. Al detener una campaña, asegúrate de que la opción para eliminar las tarjetas activas de las fuentes de los usuarios esté seleccionada.

## Vínculos en profundidad

Los registros de vínculos profundos aparecen en las notificaciones push, los mensajes dentro de la aplicación y las tarjetas de contenido. La estructura del registro es coherente independientemente del canal de origen.

{% tabs %}
{% tab Swift %}

Cuando el SDK procesa un vínculo profundo:

```
Opening '<DEEP_LINK_URL>':
- channel: <SOURCE_CHANNEL>
- useWebView: false
- isUniversalLink: false
- extras: { ... }
```

Donde`<SOURCE_CHANNEL>`  es uno de los siguientes: `notification`,`inAppMessage` , o `contentCard`.

{% endtab %}
{% tab Android %}

Para los vínculos profundos, busca las entradas **Deep Link Delegate** o **UriAction** en Logcat. Para probar la resolución de vínculos profundos de forma independiente, ejecuta el siguiente comando:

```bash
adb shell am start -W -a android.intent.action.VIEW -d "<YOUR_DEEP_LINK>" "<YOUR_PACKAGE_NAME>"
```

Esto confirma si el vínculo profundo se resuelve correctamente fuera del SDK de Braze.

{% endtab %}
{% endtabs %}

### Qué hay que comprobar

- Comprueba que la URL del vínculo profundo coincide con la que has configurado en la campaña.
- Si el vínculo profundo funciona desde un canal (por ejemplo, push), pero no desde otro (por ejemplo, tarjetas de contenido), comprueba que la implementación del manejo de vínculos profundos sea compatible con todos los canales.
- En iOS, los enlaces universales requieren un manejo adicional. Si los enlaces universales no funcionan desde los canales de Braze, comprueba que tu aplicación implemente el`BrazeDelegate`protocolo para el manejo de URL.
- En Android, comprueba que la gestión automática de vínculos profundos esté desactivada si utilizas un controlador personalizado. De lo contrario, el controlador predeterminado podría entrar en conflicto con tu implementación.

## Identificación del usuario

Cuando se asigna un identificador`external_id` a un usuario, el SDK registra un evento de cambio de usuario.

{% tabs %}
{% tab Android %}

```
changeUser called with: <EXTERNAL_ID>
```

Aspectos clave que debes saber:
- Llama`changeUser`tan pronto como el usuario inicie sesión; cuanto antes, mejor.
- Si un usuario cierra sesión, no hay forma de llamarte`changeUser`para revertirlo a un usuario anónimo.
- Si no deseas usuarios anónimos, llama a`changeUser`  durante el inicio de la sesión o el inicio de la aplicación.

{% endtab %}
{% tab Swift %}

Filtra las solicitudes a tu punto final Braze configurado (por ejemplo, sdk.iad-01.braze.com) y busca la identificación del usuario en el cuerpo de la solicitud:

```
"user_id": "<EXTERNAL_ID>"
```

{% endtab %}
{% endtabs %}

## Solicitudes de red

Los registros detallados incluyen todos los detalles de las solicitudes y respuestas HTTP para la comunicación del SDK con los servidores de Braze. Son útiles para diagnosticar problemas de conectividad.

### Estructura de la solicitud

Filtra las solicitudes a tu punto final Braze configurado (por ejemplo, sdk.iad-01.braze.com). La estructura de la solicitud incluye:

{% tabs %}
{% tab Swift %}

```
[http] request POST: <YOUR_BRAZE_ENDPOINT>
- Headers:
  - Content-Type: application/json
  - X-Braze-Api-Key: <REDACTED>
  - X-Braze-Req-Attempt: 1
  - X-Braze-Req-Tokens-Remaining: <COUNT>
- Body: { ... }
```

{% endtab %}
{% tab Android %}

```
Making request(id = <REQUEST_ID>) to <YOUR_BRAZE_ENDPOINT>
```

{% endtab %}
{% endtabs %}

### Qué hay que comprobar

- **Clave de API**: Verifica`XBraze-ApiKey`que coincida con la clave de API de tu espacio de trabajo.
- **Punto final**: Confirma que la URL de la solicitud coincide con el punto final SDK que has configurado.
- **Intentos de reintento**:`XBraze-Req-Attempt`  un valor superior a 1 indica que el SDK está reintentando una solicitud fallida, lo que puede indicar problemas de conectividad.
- **Límite de velocidad**:`XBraze-Req-Tokens-Remaining`muestra los tokens de solicitud restantes. Un recuento bajo puede indicar que el SDK se está acercando a los límites de velocidad.
- **Solicitudes pendientes**: En Android, si no ves una solicitud al punto final de Braze después del inicio de la sesión, verifica tu clave de API y la configuración del punto final.

## Abreviaturas comunes de eventos

En las cargas útiles de registros detallados, Braze utiliza nombres de eventos abreviados. Aquí tienes una referencia:

| Abreviatura | Evento |
|---|---|
| `ss` | Inicio de la sesión |
| `se` | Fin de la sesión |
| `si` | Impresión de mensajes dentro de la aplicación |
| `sbc` | Clic en el botón de mensajes dentro de la aplicación |
| `cci` | Impresión de la tarjeta de contenido |
| `ccc` | Tarjeta de contenido clic |
| `ccd` | Descarte de tarjeta de contenido |
| `lr` | Ubicación registrada |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }