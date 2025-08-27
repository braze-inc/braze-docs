---
nav_title: Receptor de difusión de devolución de llamada push
article_title: Devolución de llamada push personalizada del receptor de difusión para Android
description: "Este artículo de referencia trata sobre la creación de un receptor de difusión personalizado para las notificaciones push de Android"
---

# Gestión personalizada de las recepciones push, aperturas, rechazos y pares clave-valor mediante el receptor de difusión {#android-push-listener-broadcast-receiver}

{% alert important %}
El uso de un `BroadcastReceiver` personalizado para las notificaciones push ha quedado obsoleto. Utiliza [` subscribeToPushNotificationEvents()`]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android#android_using-a-callback-for-push-events) en su lugar.
{% endalert %}

Braze también difunde intenciones personalizadas cuando se reciben, abren o descartan notificaciones push. Si tienes un caso de uso específico para estos escenarios (como la necesidad de escuchar los pares clave-valor personalizados o la gestión propietaria de los vínculos profundos), tendrás que escuchar estas intenciones creando un `BroadcastReceiver` personalizado.

## Paso 1: Registra tu BroadcastReceiver

Registra tu `BroadcastReceiver` personalizado para escuchar las intenciones push Braze abiertas y recibidas en tu [`AndroidManifest.xml`](https://github.com/braze-inc/braze-android-sdk/blob/master/samples/custom-broadcast/src/main/AndroidManifest.xml):

```xml
<receiver android:name="YOUR-BROADCASTRECEIVER-NAME" android:exported="false" >
  <intent-filter>
    <action android:name="com.braze.push.intent.NOTIFICATION_RECEIVED" />
    <action android:name="com.braze.push.intent.NOTIFICATION_OPENED" />
    <action android:name="com.braze.push.intent.NOTIFICATION_DELETED" />
  </intent-filter>
</receiver>
```

## Paso 2: Crea tu BroadcastReceiver

Tu receptor debe gestionar las intenciones emitidas por Braze y lanzar tu actividad con ellas:

- Debería subclasificar [`BroadcastReceiver`](https://developer.android.com/reference/android/content/BroadcastReceiver.html) y anular `onReceive()`.
- El método `onReceive()` debe escuchar las intenciones emitidas por Braze.
  - Se recibirá una intención `NOTIFICATION_RECEIVED` cuando llegue una notificación push.
  - Se recibirá una intención `NOTIFICATION_OPENED` cuando el usuario haga clic en una notificación push.
  - Se recibirá una intención `NOTIFICATION_DELETED` cuando el usuario rechace una notificación push.
- Debe realizar tu lógica personalizada para cada uno de estos casos. Si tu receptor abre vínculos profundos, asegúrate de desactivar la apertura automática de vínculos profundos configurando `com_braze_handle_push_deep_links_automatically` en `false` en tu `braze.xml`.

Para ver un ejemplo detallado de receptor personalizado, consulta los siguientes fragmentos de código:

{% tabs %}
{% tab JAVA %}

```java
public class CustomBroadcastReceiver extends BroadcastReceiver {
  private static final String TAG = CustomBroadcastReceiver.class.getName();

  @Override
  public void onReceive(Context context, Intent intent) {
    String pushReceivedAction = Constants.BRAZE_PUSH_INTENT_NOTIFICATION_RECEIVED;
    String notificationOpenedAction = Constants.BRAZE_PUSH_INTENT_NOTIFICATION_OPENED;
    String notificationDeletedAction = Constants.BRAZE_PUSH_INTENT_NOTIFICATION_DELETED;

    String action = intent.getAction();
    Log.d(TAG, String.format("Received intent with action %s", action));

    if (pushReceivedAction.equals(action)) {
      Log.d(TAG, "Received push notification.");
    } else if (notificationOpenedAction.equals(action)) {
      BrazeNotificationUtils.routeUserWithNotificationOpenedIntent(context, intent);
    } else if (notificationDeletedAction.equals(action)) {
      Log.d(TAG, "Received push notification deleted intent.");
    } else {
      Log.d(TAG, String.format("Ignoring intent with unsupported action %s", action));
    }
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class CustomBroadcastReceiver : BroadcastReceiver() {
  override fun onReceive(context: Context, intent: Intent) {
    val pushReceivedAction = Constants.BRAZE_PUSH_INTENT_NOTIFICATION_RECEIVED
    val notificationOpenedAction = Constants.BRAZE_PUSH_INTENT_NOTIFICATION_OPENED
    val notificationDeletedAction = Constants.BRAZE_PUSH_INTENT_NOTIFICATION_DELETED

    val action = intent.action
    Log.d(TAG, String.format("Received intent with action %s", action))

    when (action) {
      pushReceivedAction -> {
        Log.d(TAG, "Received push notification.")
      }
      notificationOpenedAction -> {
        BrazeNotificationUtils.routeUserWithNotificationOpenedIntent(context, intent)
      }
      notificationDeletedAction -> {
        Log.d(TAG, "Received push notification deleted intent.")
      }
      else -> {
        Log.d(TAG, String.format("Ignoring intent with unsupported action %s", action))
      }
    }
  }

  companion object {
    private val TAG = CustomBroadcastReceiver::class.java.name
  }
}
```

{% endtab %}
{% endtabs %}

{% alert tip %}
Con los botones de acción de notificación, las intenciones `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` se disparan cuando se hace clic en los botones con acciones `opens app` o `deep link`. El tratamiento de los vínculos profundos y los extras sigue siendo el mismo. Los botones con acciones `close` no disparan las intenciones `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` y descartan la notificación automáticamente.
{% endalert %}

## Paso 3: Acceder a pares clave-valor personalizados

Los pares clave-valor personalizados enviados a través del panel o de las API de mensajería estarán accesibles en tu receptor de difusión personalizado para cualquier propósito que elijas:

{% tabs %}
{% tab JAVA %}

```java
// intent is the Braze push intent received by your custom broadcast receiver.
String deepLink = intent.getStringExtra(Constants.BRAZE_PUSH_DEEP_LINK_KEY);

// The extras bundle extracted from the intent contains all custom key-value pairs.
Bundle extras = intent.getBundleExtra(Constants.BRAZE_PUSH_EXTRAS_KEY);

// example of getting specific key-value pair from the extras bundle.
String myExtra = extras.getString("my_key");
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
// intent is the Braze push intent received by your custom broadcast receiver.
val deepLink = intent.getStringExtra(Constants.BRAZE_PUSH_DEEP_LINK_KEY)

// The extras bundle extracted from the intent contains all custom key-value pairs.
val extras = intent.getBundleExtra(Constants.BRAZE_PUSH_EXTRAS_KEY)

// example of getting specific key-value pair from the extras bundle.
val myExtra = extras.getString("my_key")
```

{% endtab %}
{% endtabs %}

{% alert note %}
Para obtener documentación sobre las teclas de datos push de Braze, consulta el [SDK de Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-constants/index.html?query=object%20Constants).
{% endalert %}

