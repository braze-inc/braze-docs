---
nav_title: Entrega de mensajes dentro de la aplicación
article_title: Entrega de mensajes dentro de la aplicación para Android y FireOS
page_order: 3
platform: 
  - Android
  - FireOS
description: "Este artículo de referencia cubre la entrega de mensajes dentro de la aplicación de Android y FireOS, enumerando los diferentes tipos de desencadenantes, la semántica de la entrega y los pasos para desencadenar eventos."
channel:
  - in-app messages

---

# Entrega de mensajes dentro de la aplicación

> Este artículo de referencia cubre la entrega de mensajes dentro de la aplicación de Android y FireOS, enumerando los diferentes tipos de desencadenantes, la semántica de la entrega y los pasos para desencadenar eventos.

## Tipos de desencadenantes

Nuestro producto de mensajes dentro de la aplicación te permite desencadenar la visualización de un mensaje dentro de la aplicación debido a varios tipos de eventos diferentes: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event`, y `Push Click`. Además, los desencadenadores `Specific Purchase` y `Custom Event` pueden contener filtros de propiedades robustos.

{% alert note %}
Los mensajes desencadenados dentro de la aplicación sólo funcionan con eventos personalizados registrados a través del SDK de Braze. Los mensajes dentro de la aplicación no pueden desencadenarse a través de la API o por eventos de la API (como eventos de compra). Asegúrate de comprobar cómo [registrar eventos personalizados]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/).
{% endalert %}

## Semántica de la entrega

Todos los mensajes dentro de la aplicación para los que un usuario es elegible se entregan al dispositivo del usuario al [inicio de la sesión]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/#session-lifecycle). Tras la entrega, el SDK precargará los activos para que estén disponibles inmediatamente en el momento del desencadenamiento, minimizando la latencia de visualización.

Cuando un evento desencadenante tiene asociado más de un mensaje dentro de la aplicación elegible, sólo se entregará el mensaje dentro de la aplicación con la prioridad más alta.

Puede haber cierta latencia en los mensajes dentro de la aplicación que se muestran inmediatamente después de la entrega (como el inicio de sesión y el clic push) debido a que los activos no se precargan.

## Intervalo de tiempo mínimo entre desencadenamientos

De forma predeterminada, limitamos la tasa de los mensajes dentro de la aplicación a una vez cada 30 segundos para garantizar una experiencia de usuario de calidad.

Para anular este valor, configura `com_braze_trigger_action_minimum_time_interval_seconds` en tu `braze.xml` a través de:

```xml
  <integer name="com_braze_trigger_action_minimum_time_interval_seconds">5</integer>
```

## Desencadenar eventos del servidor

Por predeterminado, los mensajes dentro de la aplicación se desencadenan por eventos personalizados registrados por el SDK. Si quieres desencadenar mensajes dentro de la aplicación mediante eventos enviados por el servidor, también puedes conseguirlo.

Para habilitar esta característica, se envía un push silencioso al dispositivo, que permite una devolución de llamada push personalizada para registrar un evento basado en SDK. Este evento SDK desencadenará posteriormente el mensaje dentro de la aplicación dirigido al usuario.

### Paso 1: Crea una devolución de llamada push para recibir el push silencioso

Registra tu devolución de llamada push personalizada para escuchar una notificación push silenciosa específica. Para más información, consulta [Integración push estándar de Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#android-push-listener-callback).

Se registrarán dos eventos para que se entregue el mensaje dentro de la aplicación, uno por parte del servidor y otro desde dentro de tu devolución de llamada push personalizada. Para asegurarte de que no se duplica el mismo evento, el evento registrado desde dentro de tu devolución de llamada push debe seguir una convención de nomenclatura genérica, por ejemplo, "evento de desencadenamiento de mensaje dentro de la aplicación", y no el mismo nombre que el evento enviado por el servidor. Si no se hace así, la segmentación y los datos de usuario pueden verse afectados por el registro de sucesos duplicados para una única acción de usuario.

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

### Paso 2: Crear una campaña push

Crea una [campaña push silenciosa]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/silent_push_notifications/) desencadenada a través del evento enviado por el servidor.

![]({% image_buster /assets/img_archive/serverSentPush.png %})

La campaña push debe incluir extras de par clave-valor que indiquen que esta campaña push se envía para registrar un evento personalizado del SDK. Este evento se utilizará para desencadenar el mensaje dentro de la aplicación.

![Dos conjuntos de pares clave-valor: IS_SERVER_EVENT ajustado a "true", y CAMPAIGN_NAME ajustado a "nombre de campaña de ejemplo".]({% image_buster /assets/img_archive/kvpConfiguration.png %}){: style="max-width:70%;" }

El código de ejemplo de devolución de llamada push anterior reconoce los pares clave-valor y registra el evento personalizado SDK apropiado.

Si quieres incluir propiedades del evento para adjuntarlas a tu evento "desencadenador de mensajes dentro de la aplicación", puedes hacerlo pasándolas a los pares clave-valor de la carga útil push. En este ejemplo, se ha incluido el nombre de la campaña del mensaje dentro de la aplicación posterior. Tu devolución de llamada push personalizada puede entonces pasar el valor como parámetro de la propiedad del evento al registrar el evento personalizado.

### Paso 3: Crea una campaña de mensajes dentro de la aplicación

Crea tu campaña de mensajes dentro de la aplicación visible para el usuario en el panel de Braze. Esta campaña debe tener una entrega basada en acciones y desencadenarse desde el evento personalizado registrado desde dentro de tu devolución de llamada push personalizada.

En el siguiente ejemplo, el mensaje específico dentro de la aplicación que se va a desencadenar se ha configurado enviando la propiedad del evento como parte del push silencioso inicial.

![Una campaña de entrega basada en acciones en la que se desencadenará un mensaje dentro de la aplicación cuando "nombre_campaña" sea igual a "ejemplo de nombre de campaña de IAM".]({% image_buster /assets/img_archive/iam_event_trigger.png %})

Si se registra un evento enviado por el servidor mientras la aplicación no está en primer plano, el evento se registrará, pero no se mostrará el mensaje dentro de la aplicación. Si quieres que el evento se retrase hasta que la aplicación esté en primer plano, debes incluir una comprobación en tu receptor push personalizado para descartar o retrasar el evento hasta que la aplicación haya entrado en primer plano.

## Mensajes locales dentro de la aplicación

Los mensajes dentro de la aplicación pueden crearse dentro de la aplicación y mostrarse localmente en tiempo real. Todas las opciones de personalización disponibles en el panel también están disponibles localmente. Esto es especialmente útil para mostrar mensajes que deseas desencadenar dentro de la aplicación en tiempo real.

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

### Desencadenar manualmente la visualización de mensajes dentro de la aplicación

El siguiente método mostrará manualmente tu mensaje dentro de la aplicación:

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

