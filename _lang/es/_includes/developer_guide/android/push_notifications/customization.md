{% multi_lang_include developer_guide/prerequisites/android.md %} También tendrás que [configurar las notificaciones push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android).

## Utilizar una devolución de llamada para eventos push {#push-callback}

Braze proporciona una [`subscribeToPushNotificationEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/subscribe-to-push-notification-events.html) devolución de llamada para cuando se reciben, abren o descartan notificaciones push. Se recomienda colocar esta devolución de llamada en tu `Application.onCreate()` para no perderte ningún evento que ocurra mientras tu aplicación no se esté ejecutando.

{% alert note %}
Si antes utilizabas un Receptor de difusión personalizado para esta funcionalidad en tu aplicación, puedes eliminarlo sin problemas en favor de esta opción de integración.
{% endalert %}

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).subscribeToPushNotificationEvents(event -> {
  final BrazeNotificationPayload parsedData = event.getNotificationPayload();

  //
  // The type of notification itself
  //
  final boolean isPushOpenEvent = event.getEventType() == BrazePushEventType.NOTIFICATION_OPENED;
  final boolean isPushReceivedEvent = event.getEventType() == BrazePushEventType.NOTIFICATION_RECEIVED;
  // Sent when a user has dismissed a notification
  final boolean isPushDeletedEvent = event.getEventType() == BrazePushEventType.NOTIFICATION_DELETED;

  //
  // Notification data
  //
  final String pushTitle = parsedData.getTitleText();
  final Long pushArrivalTimeMs = parsedData.getNotificationReceivedTimestampMillis();
  final String deeplink = parsedData.getDeeplink();

  //
  // Custom KVP data
  //
  final String myCustomKvp1 = parsedData.getBrazeExtras().getString("my first kvp");
  final String myCustomKvp2 = parsedData.getBrazeExtras().getString("my second kvp");
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).subscribeToPushNotificationEvents { event ->
    val parsedData = event.notificationPayload

    //
    // The type of notification itself
    //
    val isPushOpenEvent = event.eventType == BrazePushEventType.NOTIFICATION_OPENED
    val isPushReceivedEvent = event.eventType == BrazePushEventType.NOTIFICATION_RECEIVED
    // Sent when a user has dismissed a notification
    val isPushDeletedEvent = event.eventType == BrazePushEventType.NOTIFICATION_DELETED

    //
    // Notification data
    //
    val pushTitle = parsedData.titleText
    val pushArrivalTimeMs = parsedData.notificationReceivedTimestampMillis
    val deeplink = parsedData.deeplink

    //
    // Custom KVP data
    //
    val myCustomKvp1 = parsedData.brazeExtras.getString("my first kvp")
    val myCustomKvp2 = parsedData.brazeExtras.getString("my second kvp")
}
```

{% endtab %}
{% endtabs %}

{% alert tip %}
Con los botones de acción de notificación, las intenciones `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` se disparan cuando se hace clic en los botones con acciones `opens app` o `deep link`. El tratamiento de los vínculos profundos y los extras sigue siendo el mismo. Los botones con acciones `close` no disparan las intenciones `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` y descartan la notificación automáticamente.
{% endalert %}

{% alert important %}
Crea tu receptor de notificaciones push en `Application.onCreate` para asegurarte de que se desencadena cuando un usuario final toca una notificación mientras tu aplicación está en estado finalizado.
{% endalert %}

## Personalizar la visualización de notificaciones {#customization-display}

### Paso 1: Crea tu fábrica de notificaciones personalizada

En algunos casos, es posible que desees personalizar las notificaciones push de formas que serían engorrosas o no estarían disponibles en el servidor. Para darte un control completo de la visualización de notificaciones, hemos añadido la posibilidad de definir tus propias [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) objetos de notificación para que los muestre Braze.

Si se configura un `IBrazeNotificationFactory` personalizado, Braze llamará al método `createNotification()` de tu fábrica tras la recepción push antes de que se muestre la notificación al usuario. Braze pasará un `Bundle` que contiene datos push de Braze y otro `Bundle` que contiene pares clave-valor personalizados enviados a través del panel o de las API de mensajería:

Braze pasará un archivo [`BrazeNotificationPayload`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/index.html) que contiene los datos de la notificación push de Braze.

{% tabs %}
{% tab JAVA %}

```java
// Factory method implemented in your custom IBrazeNotificationFactory
@Override
public Notification createNotification(BrazeNotificationPayload brazeNotificationPayload) {
  // Example of getting notification title
  String title = brazeNotificationPayload.getTitleText();

  // Example of retrieving a custom KVP ("my_key" -> "my_value")
  String customKvp = brazeNotificationPayload.getBrazeExtras().getString("my_key");
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
// Factory method implemented in your custom IBrazeNotificationFactory
override fun createNotification(brazeNotificationPayload: BrazeNotificationPayload): Notification {
  // Example of getting notification title
  val title = brazeNotificationPayload.getTitleText()

  // Example of retrieving a custom KVP ("my_key" -> "my_value")
  val customKvp = brazeNotificationPayload.getBrazeExtras().getString("my_key")
}
```

{% endtab %}
{% endtabs %}

Puedes devolver `null` desde tu método personalizado `createNotification()` para no mostrar la notificación en absoluto, utilizar `BrazeNotificationFactory.getInstance().createNotification()` para obtener nuestro objeto predeterminado `notification` para esos datos y modificarlo antes de mostrarlo, o generar un objeto `notification` completamente independiente para mostrarlo.

{% alert note %}
Para obtener documentación sobre las teclas de datos push de Braze, consulta el [SDK de Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-constants/index.html).
{% endalert %}

### Paso 2: Configura tu fábrica de notificaciones personalizada

Para indicar a Braze que utilice tu fábrica de notificaciones personalizada, utiliza el método `setCustomBrazeNotificationFactory` para configurar tus [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html):

{% tabs %}
{% tab JAVA %}


```java
setCustomBrazeNotificationFactory(IBrazeNotificationFactory brazeNotificationFactory);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
setCustomBrazeNotificationFactory(brazeNotificationFactory: IBrazeNotificationFactory)
```

{% endtab %}
{% endtabs %}

El lugar recomendado para configurar tu `IBrazeNotificationFactory` personalizado es el método de ciclo de vida de la aplicación `Application.onCreate()` (no la actividad). Esto permitirá que la fábrica de notificaciones se configure correctamente siempre que el proceso de tu aplicación esté activo.

{% alert important %}
Crear tu propia notificación desde cero es un caso de uso avanzado y sólo debe hacerse con pruebas exhaustivas y un conocimiento profundo de la funcionalidad push de Braze. Por ejemplo, debes asegurarte de que tus registros de notificación push se abren correctamente.
{% endalert %}

Para desactivar tu sistema personalizado [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) y volver a la gestión predeterminada de Braze para push, pasa `null` a nuestro configurador de fábrica de notificaciones personalizadas:

{% tabs %}
{% tab JAVA %}


```java
setCustomBrazeNotificationFactory(null);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
setCustomBrazeNotificationFactory(null)
```

{% endtab %}
{% endtabs %}

## Renderizado de texto multicolor

En la versión 3.1.1 del SDK de Braze, se puede enviar HTML a un dispositivo para mostrar texto multicolor en las notificaciones push.

![Un mensaje push de Android "Mensaje de prueba push multicolor" en el que las letras son de distintos colores, están en cursiva y tienen un color de fondo.]({% image_buster /assets/img/multicolor_android_push.png %}){: style="max-width:40%;"}

Este ejemplo se muestra con el siguiente HTML:

```html
<p><span style="color: #99cc00;">M</span>u<span style="color: #008080;">lti</span>Colo<span style="color: #ff6600;">r</span> <span style="color: #000080;">P</span><span style="color: #00ccff;">u</span><span style="color: #ff0000;">s</span><span style="color: #808080;">h</span></p>

<p><em>test</em> <span style="text-decoration: underline; background-color: #ff6600;"><strong>message</strong></span></p>
```

Ten en cuenta que, Android limita qué elementos y etiquetas HTML son válidos en tus notificaciones push. Por ejemplo, `marquee` no está permitido.

{% alert important %}
La representación del texto multicolor es específica del dispositivo y puede que no se muestre según el dispositivo o la versión de Android.
{% endalert %}

Para representar texto multicolor en una notificación push, puedes actualizar tu `braze.xml` o `BrazeConfig`:

{% tabs local %}
{% tab braze.xml %}
Añade lo siguiente en tu `braze.xml`:

```xml
<bool translatable="false" name="com_braze_push_notification_html_rendering_enabled">true</bool>
```
{% endtab %}

{% tab BrazeConfig %}
Añade lo siguiente en tu [`BrazeConfig`]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/#runtime-configuration):

{% subtabs local %}
{% subtab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
  .setPushHtmlRenderingEnabled(true)
  .build();
Braze.configure(this, brazeConfig);
```
 
{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
    .setPushHtmlRenderingEnabled(true)
    .build()
Braze.configure(this, brazeConfig)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Etiquetas HTML compatibles

Actualmente, Google no enumera las etiquetas HTML compatibles con Android directamente en su documentación; esta información sólo puede encontrarse en [el archivo `Html.java` de](https://android.googlesource.com/platform/frameworks/base/+/master/core/java/android/text/Html.java) su [repositorio Git.](https://android.googlesource.com/platform/frameworks/base/+/master/core/java/android/text/Html.java) Tenlo en cuenta cuando consultes la siguiente tabla, ya que esta información se extrajo de este archivo, y sus etiquetas HTML compatibles podrían estar sujetas a cambios.

<table>
  <thead>
    <tr>
      <th>Categoría</th>
      <th>Etiqueta HTML</th>
      <th>Descripción</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="7">Estilización básica del texto</td>
      <td><code>&lt;b&gt;</code>, <code>&lt;strong&gt;</code></td>
      <td>Texto en negrita</td>
    </tr>
    <tr>
      <td><code>&lt;i&gt;</code>, <code>&lt;em&gt;</code></td>
      <td>Texto en cursiva</td>
    </tr>
    <tr>
      <td><code>&lt;u&gt;</code></td>
      <td>Subrayar texto</td>
    </tr>
    <tr>
      <td><code>&lt;s&gt;</code>, <code>&lt;strike&gt;</code>, <code>&lt;del&gt;</code></td>
      <td>Texto tachado</td>
    </tr>
    <tr>
      <td><code>&lt;sup&gt;</code></td>
      <td>Texto superíndice</td>
    </tr>
    <tr>
      <td><code>&lt;sub&gt;</code></td>
      <td>Texto del subíndice</td>
    </tr>
    <tr>
      <td><code>&lt;tt&gt;</code></td>
      <td>Texto monospace</td>
    </tr>
    <tr>
      <td rowspan="3">Tamaño/Fuente</td>
      <td><code>&lt;big&gt;</code>, <code>&lt;small&gt;</code></td>
      <td>Cambios relativos en el tamaño del texto</td>
    </tr>
    <tr>
      <td><code>&lt;font color="..."&gt;</code></td>
      <td>Establece el color de primer plano</td>
    </tr>
    <tr>
      <td><code>&lt;span&gt;</code> (con CSS en línea)</td>
      <td>Estilos en línea (e.g., color, fondo)</td>
    </tr>
    <tr>
      <td rowspan="4">Párrafo y Bloque</td>
      <td><code>&lt;p&gt;</code>, <code>&lt;div&gt;</code></td>
      <td>Secciones a nivel de bloque</td>
    </tr>
    <tr>
      <td><code>&lt;br&gt;</code></td>
      <td>Salto de línea</td>
    </tr>
    <tr>
      <td><code>&lt;blockquote&gt;</code></td>
      <td>Bloque citado</td>
    </tr>
    <tr>
      <td><code>&lt;ul&gt;</code> + <code>&lt;li&gt;</code></td>
      <td>Lista desordenada con viñetas</td>
    </tr>
    <tr>
      <td>Rúbricas</td>
      <td><code>&lt;h1&gt;</code> - <code>&lt;h6&gt;</code></td>
      <td>Títulos (varios tamaños)</td>
    </tr>
    <tr>
      <td rowspan="2">Enlaces e imágenes</td>
      <td><code>&lt;a href="..."&gt;</code></td>
      <td>Enlace clicable</td>
    </tr>
    <tr>
      <td><code>&lt;img src="..."&gt;</code></td>
      <td>Imagen en línea</td>
    </tr>
    <tr>
      <td>Otros en línea</td>
      <td><code>&lt;em&gt;</code>, <code>&lt;strong&gt;</code>, <code>&lt;dfn&gt;</code>, <code>&lt;cite&gt;</code></td>
      <td>Sinónimos de cursiva o negrita</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Renderizado de imágenes en línea

### Cómo funciona

Puedes mostrar una imagen más grande dentro de tu notificación push de Android utilizando el push de imagen en línea. Con este diseño, los usuarios no tendrán que expandir manualmente el push para ampliar la imagen. A diferencia de las notificaciones push normales de Android, las imágenes push en línea tienen una relación de aspecto de 3:2.

![]({% image_buster /assets/img/android/push/inline_image_push_android_1.png %}){: style="max-width:50%;"}

### Compatibilidad

Aunque puedes enviar imágenes en línea a cualquier dispositivo, los dispositivos y SDK que no cumplan las versiones mínimas mostrarán en su lugar una imagen estándar. Para que las imágenes en línea se muestren correctamente, se necesita el SDK de Android Braze v10.0.0+ y un dispositivo que ejecute Android M+. El SDK también debe estar habilitado para que la imagen se renderice.

{% alert note %}
Los dispositivos con Android 12 se mostrarán de forma diferente debido a los cambios en los estilos personalizados de las notificaciones push.
{% endalert %}

### Enviar una imagen en línea push

Al crear un mensaje push de Android, esta característica está disponible en el desplegable **Tipo de notificación**.

![El editor de campañas push muestra la ubicación del desplegable "Tipo de notificación" (encima de la vista previa push estándar).]({% image_buster /assets/img/android/push/android_inline_image_notification_type.png %})

## Configuración

Hay muchas configuraciones avanzadas disponibles para las notificaciones push de Android enviadas a través del panel de Braze. En este artículo se describirán estas características y cómo utilizarlas con éxito.

![]({% image_buster /assets/img_archive/android_advanced_settings.png %})

### ID de notificación {#notification-id}

Un **ID de notificación** es un identificador único para una categoría de mensajes de tu elección que informa al servicio de mensajería para que sólo respete el mensaje más reciente de ese ID. Establecer un ID de notificación te permite enviar sólo el mensaje más reciente y relevante, en lugar de una pila de mensajes desfasados e irrelevantes.

### Prioridad de entrega de la mensajería Firebase {#fcm-priority}

El campo [Prioridad de entrega de la mensajería de Firebase](https://firebase.google.com/docs/cloud-messaging/concept-options#setting-the-priority-of-a-message) te permite controlar si un push se envía con prioridad "normal" o "alta" a la mensajería en la nube de Firebase.

### Tiempo de vida (TTL) {#ttl}

El campo **Tiempo de vida** (TTL) te permite establecer un tiempo personalizado para almacenar mensajes con el servicio de mensajería push. Los valores predeterminados para el tiempo de vida son cuatro semanas para FCM y 31 días para ADM.

### Texto resumido {#summary-text}

El texto de resumen te permite establecer texto adicional en la vista ampliada de notificaciones. También sirve como pie de foto para las notificaciones con imágenes.

![Un mensaje Android con el título "Este es el título de la notificación" y el texto resumen "Este es el texto resumen de la notificación"]({% image_buster /assets/img/android/push/collapsed-android-notification.png %}){: style="max-width:65%;"}

El texto resumido se mostrará bajo el cuerpo del mensaje en la vista ampliada. 

![Un mensaje Android con el título "Este es el título de la notificación" y el texto resumen "Este es el texto resumen de la notificación"]({% image_buster /assets/img/android/push/expanded-android-notification.png %}){: style="max-width:65%;"}

Para las notificaciones push que incluyan imágenes, el texto del mensaje se mostrará en la vista contraída, mientras que el texto del resumen se mostrará como pie de imagen cuando se expanda la notificación. 

### URIs personalizadas {#custom-uri}

La característica **URI personalizada** te permite especificar una URL Web o un recurso Android al que navegar cuando se haga clic en la notificación. Si no se especifica una URI personalizada, al hacer clic en la notificación los usuarios acceden a tu aplicación. Puedes utilizar el URI personalizado para establecer vínculos profundos dentro de tu aplicación y dirigir a los usuarios a recursos que existen fuera de ella. Esto puede especificarse a través de la [API de mensajería]({{site.baseurl}}/api/endpoints/messaging/) o de nuestro panel en **Configuración avanzada** en el compositor push, como se muestra en la imagen:

![La configuración avanzada de vinculación en profundidad en el compositor push de Braze.]({% image_buster /assets/img_archive/deep_link.png %})

### Prioridad de visualización de notificaciones {#notification-priority}

{% alert important %}
El ajuste Prioridad de visualización de notificaciones ya no se utiliza en dispositivos con Android O o posterior. Para los dispositivos más nuevos, establezca la prioridad a través de [la configuración del canal de notificación](https://developer.android.com/training/notify-user/channels#importance).
{% endalert %}

El nivel de prioridad de una notificación push afecta a cómo se muestra su notificación en la bandeja de notificaciones en relación con otras notificaciones. También puede afectar a la velocidad y forma de entrega, ya que los mensajes normales y de menor prioridad pueden enviarse con una latencia ligeramente superior o por lotes para preservar la duración de la batería, mientras que los mensajes de alta prioridad siempre se envían inmediatamente.

En Android O, la prioridad de notificación pasó a ser una propiedad de los canales de notificación. Tendrás que trabajar con tu desarrollador para definir la prioridad de un canal durante su configuración y luego utilizar el panel de control para seleccionar el canal adecuado al enviar tus sonidos de notificación. Para los dispositivos que ejecutan versiones de Android anteriores a O, es posible especificar un nivel de prioridad para las notificaciones de Android mediante el panel de Braze y la API de mensajería. 

Para enviar mensajes a toda tu base de usuarios con una prioridad específica, te recomendamos que especifiques indirectamente la prioridad mediante la [configuración del canal de notificación](https://developer.android.com/training/notify-user/channels#importance) (para dirigirte a dispositivos O+) *y* envíes la prioridad individual desde el panel (para dirigirte a dispositivos <O).

Los niveles de prioridad que puedes establecer en las notificaciones push de Android o Fire OS son:

| Prioridad | Descripción/uso previsto | `priority` valor (para mensajes API) |
|----------|--------------------------|-------------------------------------|
| Máx.      | Mensajes urgentes o en los que el tiempo es un factor crítico | `2` |
| Alta     | Comunicación importante, como un nuevo mensaje de un amigo | `1` |
| Predeterminado  | La mayoría de las notificaciones: utilízalo si tu mensaje no entra explícitamente en ninguno de los otros tipos de prioridad. | `0` |
| Baja      | Información que quieres que conozcan los usuarios pero que no requiere una acción inmediata | `-1` |
| Mín.      | Información contextual o de fondo. | `-2` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Para más información, consulta la documentación de [notificaciones de Android](http://developer.android.com/design/patterns/notifications.html) de Google.

### Sonidos {#sounds}

En Android O, los sonidos de notificación pasaron a ser una propiedad de los canales de notificación. Tendrás que trabajar con tu desarrollador para definir el sonido de un canal durante su configuración y luego utilizar el panel para seleccionar el canal adecuado al enviar tus notificaciones.

Para los dispositivos que ejecutan versiones de Android anteriores a O, Braze te permite configurar el sonido de un mensaje push individual a través del compositor del panel. Puedes hacerlo especificando un recurso de sonido local en el dispositivo (por ejemplo, `android.resource://com.mycompany.myapp/raw/mysound`). Si especificas "predeterminado" en este campo, se reproducirá el sonido de notificación predeterminado en el dispositivo. Esto puede especificarse a través de la [API de mensajería]({{site.baseurl}}/api/endpoints/messaging/) o del panel en **Configuración avanzada** en el compositor push.

![La configuración avanzada del sonido en el compositor push de Braze.]({% image_buster /assets/img_archive/sound_android.png %})

Introduce el URI completo del recurso de sonido (por ejemplo, `android.resource://com.mycompany.myapp/raw/mysound`) en la consulta del panel.

Para enviar un mensaje a toda tu base de usuarios con un sonido específico, te recomendamos que especifiques indirectamente el sonido a través de [la configuración del canal de notificación](https://developer.android.com/training/notify-user/channels) (para dirigirte a dispositivos O+) *y* envíes el sonido individual desde el panel (para dirigirte a dispositivos <O).
