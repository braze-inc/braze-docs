{% multi_lang_include developer_guide/prerequisites/android.md %}

## Mensajes desencadenados

### Tipos de desencadenantes

Los mensajes dentro de la aplicación se desencadenan automáticamente cuando el SDK registra uno de los siguientes tipos de eventos personalizados: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event`, y `Push Click`. Ten en cuenta que los desencadenadores `Specific Purchase` y `Custom Event` también contienen sólidos filtros de propiedades.

{% alert note %}
Los mensajes dentro de la aplicación no pueden desencadenarse a través de la API ni mediante eventos de la API: sólo eventos personalizados registrados por el SDK. Para saber más sobre el registro, consulta [Registrar eventos personalizados]({{site.baseurl}}/developer_guide/analytics/logging_events/).
{% endalert %}

### Semántica de la entrega

Todos los mensajes elegibles dentro de la aplicación se entregan al dispositivo del usuario al inicio de su sesión. Cuando se entreguen, el SDK precargará los activos, para que estén disponibles en el momento de desencadenar, minimizando la latencia de visualización. Si el evento desencadenado tiene más de un mensaje dentro de la aplicación elegible, sólo se entregará el mensaje con la prioridad más alta.

Para más información sobre la semántica de inicio de sesión del SDK,[consultaCiclo de vida de]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=android) la sesión.

### Límite de velocidad

De forma predeterminada, limitamos la tasa de los mensajes dentro de la aplicación a una vez cada 30 segundos para garantizar una experiencia de usuario de calidad.

Para anular este valor, configura `com_braze_trigger_action_minimum_time_interval_seconds` en tu `braze.xml` a través de:

```xml
  <integer name="com_braze_trigger_action_minimum_time_interval_seconds">5</integer>
```

## Pares clave-valor

Cuando creas una campaña en Braze, puedes establecer pares clave-valor como `extras`, que el objeto de mensajería dentro de la aplicación puede utilizar para enviar datos a tu aplicación. Por ejemplo:

{% tabs %}
{% tab JAVA %}
```java
Map<String, String> getExtras()
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
extras: Map<String, String>
```
{% endtab %}
{% endtabs %}

{% alert note %}
Para más información, consulta el [KDoc.](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html#1498425856%2FProperties%2F-1725759721)
{% endalert %}

## Desactivar los desencadenantes automáticos

Para evitar que los mensajes dentro de la aplicación se desencadenen automáticamente:

1. Asegúrate de que utilizas el inicializador automático de integración, que está habilitado por defecto a partir de la versión `2.2.0`.
2. Define la operación de mensajes dentro de la aplicación predeterminada en `DISCARD` añadiendo la siguiente línea a tu archivo `braze.xml`.

```xml
<string name="com_braze_flutter_automatic_integration_iam_operation">DISCARD</string>
```

## Desencadenar mensajes manualmente

Por defecto, los mensajes dentro de la aplicación se desencadenan automáticamente cuando el SDK registra un evento personalizado. Sin embargo, puedes desencadenar manualmente un mensaje utilizando los siguientes métodos.

### Utilizar un evento del lado del servidor

Para desencadenar un mensaje dentro de la aplicación utilizando un evento enviado por servidor, envía una notificación push silenciosa al dispositivo, que permita una devolución de llamada push personalizada para registrar un evento basado en SDK. Este evento desencadenará el mensaje dentro de la aplicación dirigido al usuario.

#### Paso 1: Crea una devolución de llamada push para recibir el push silencioso

Registra [tu devolución de llamada push personalizada]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android#push-callback) para escuchar una notificación push silenciosa específica.

En el siguiente ejemplo, se registrarán dos eventos para que se entregue el mensaje dentro de la aplicación, uno por parte del servidor y otro desde dentro de tu devolución de llamada push personalizada. Para asegurarte de que no se duplica el mismo evento, el evento registrado desde dentro de tu devolución de llamada push debe seguir una convención de nomenclatura genérica, por ejemplo, "evento de desencadenamiento de mensaje dentro de la aplicación", y no el mismo nombre que el evento enviado por el servidor. Si no se hace así, la segmentación y los datos de usuario pueden verse afectados por el registro de sucesos duplicados para una única acción de usuario.

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).subscribeToPushNotificationEvents(event -> {
  final Bundle kvps = event.getNotificationPayload().getBrazeExtras();
  if (kvps.containsKey("IS_SERVER_EVENT")) {
    BrazeProperties eventProperties = new BrazeProperties();

    // The campaign name is a string extra that clients can include in the push
    String campaignName = kvps.getString("CAMPAIGN_NAME");
    eventProperties.addProperty("campaign_name", campaignName);
    Braze.getInstance(context).logCustomEvent("IAM Trigger", eventProperties);
  }
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(applicationContext).subscribeToPushNotificationEvents { event ->
    val kvps = event.notificationPayload.brazeExtras
    if (kvps.containsKey("IS_SERVER_EVENT")) {
        val eventProperties = BrazeProperties()

        // The campaign name is a string extra that clients can include in the push
        val campaignName = kvps.getString("CAMPAIGN_NAME")
        eventProperties.addProperty("campaign_name", campaignName)
        Braze.getInstance(applicationContext).logCustomEvent("IAM Trigger", eventProperties)
    }
}
```

{% endtab %}
{% endtabs %}

#### Paso 2: Crear una campaña push

Crea una [campaña push silenciosa]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android) desencadenada a través del evento enviado por el servidor.

![]({% image_buster /assets/img_archive/serverSentPush.png %})

La campaña push debe incluir extras de par clave-valor que indiquen que esta campaña push se envía para registrar un evento personalizado del SDK. Este evento se utilizará para desencadenar el mensaje dentro de la aplicación.

![Dos conjuntos de pares clave-valor: IS_SERVER_EVENT ajustado a "true", y CAMPAIGN_NAME ajustado a "nombre de campaña de ejemplo".]({% image_buster /assets/img_archive/kvpConfiguration.png %}){: style="max-width:70%;" }

El código de ejemplo de devolución de llamada push anterior reconoce los pares clave-valor y registra el evento personalizado SDK apropiado.

Si quieres incluir propiedades del evento para adjuntarlas a tu evento "desencadenador de mensajes dentro de la aplicación", puedes hacerlo pasándolas a los pares clave-valor de la carga útil push. En este ejemplo, se ha incluido el nombre de la campaña del mensaje dentro de la aplicación posterior. Tu devolución de llamada push personalizada puede entonces pasar el valor como parámetro de la propiedad del evento al registrar el evento personalizado.

#### Paso 3: Crea una campaña de mensajes dentro de la aplicación

Crea tu campaña de mensajes dentro de la aplicación visible para el usuario en el panel de Braze. Esta campaña debe tener una entrega basada en acciones y desencadenarse desde el evento personalizado registrado desde dentro de tu devolución de llamada push personalizada.

En el siguiente ejemplo, el mensaje específico dentro de la aplicación que se va a desencadenar se ha configurado enviando la propiedad del evento como parte del push silencioso inicial.

![Una campaña de entrega basada en acciones en la que se desencadenará un mensaje dentro de la aplicación cuando "campaign_name" sea igual a "Ejemplo de nombre de campaña de IAM."]({% image_buster /assets/img_archive/iam_event_trigger.png %})

Si se registra un evento enviado por el servidor mientras la aplicación no está en primer plano, el evento se registrará, pero no se mostrará el mensaje dentro de la aplicación. Si quieres que el evento se retrase hasta que la aplicación esté en primer plano, debes incluir una comprobación en tu receptor push personalizado para descartar o retrasar el evento hasta que la aplicación haya entrado en primer plano.

### Mostrar un mensaje predefinido

Para mostrar manualmente un mensaje dentro de la aplicación predefinido, utiliza el siguiente método:

{% tabs %}
{% tab JAVA %}

```java
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage)
```

{% endtab %}
{% endtabs %}

### Mostrar un mensaje en tiempo real 

También puedes crear y mostrar mensajes locales dentro de la aplicación en tiempo real, utilizando las mismas opciones de localización disponibles en el panel. Para ello:

{% tabs %}
{% tab JAVA %}

```java
// Initializes a new slideup type in-app message and specifies its message.
InAppMessageSlideup inAppMessage = new InAppMessageSlideup();
inAppMessage.setMessage("Welcome to Braze! This is a slideup in-app message.");
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
// Initializes a new slideup type in-app message and specifies its message.
val inAppMessage = InAppMessageSlideup()
inAppMessage.message = "Welcome to Braze! This is a slideup in-app message."
```

{% endtab %}
{% endtabs %}

{% alert important %}
No muestres mensajes dentro de la aplicación cuando el teclado de software se muestra en la pantalla, ya que la representación no está definida en esta circunstancia.
{% endalert %}
