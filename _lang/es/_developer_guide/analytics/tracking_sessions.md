---
nav_title: Seguimiento de sesiones
article_title: Seguimiento de sesiones a través del SDK de Braze
page_order: 3.3
description: "Aprende a hacer un seguimiento de las sesiones a través del SDK de Braze."

---

# Sesiones de seguimiento

> Aprende a hacer un seguimiento de las sesiones a través del SDK de Braze.

{% alert note %}
Para los SDK envoltorio que no aparecen en la lista, utiliza en su lugar el método nativo de Android o Swift correspondiente.
{% endalert %}

## Sobre el ciclo de vida de la sesión

Una sesión se refiere al periodo de tiempo durante el cual el SDK de Braze realiza un seguimiento de la actividad del usuario en tu aplicación después de su lanzamiento. También puedes forzar una nueva sesión [llamando al método `changeUser()` ]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/#setting-a-user-id).

{% tabs %}
{% tab Android %}
{% alert note %}
Si has configurado la [devolución de llamada del ciclo de vida de la actividad]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android) para Android, Braze llamará automáticamente a `openSession()` y `closeSession()` para cada actividad de tu aplicación.
{% endalert %}

Por defecto, una sesión se inicia cuando se llama por primera vez a `openSession()`. Si tu aplicación pasa a segundo plano, la sesión permanecerá activa durante `10` segundos (a menos que [cambies el tiempo de espera predeterminado de la sesión](#changing-the-default-session-timeout)) o el usuario cierre tu aplicación. Ten en cuenta que, si el usuario cierra tu aplicación mientras está en segundo plano, es posible que los datos de la sesión no se configuren en Braze hasta que vuelva a abrir la aplicación. 

Si llamas a `closeSession()`, la sesión no finalizará inmediatamente. En cambio, finalizará la sesión al cabo de 10 segundos si el usuario no vuelve a llamar a `openSession()` para iniciar otra actividad.
{% endtab %}

{% tab swift %}
Por defecto, una sesión se inicia cuando llamas a `Braze.init(configuration:)`. Esto ocurre cuando se desencadena la notificación `UIApplicationWillEnterForegroundNotification`, lo que significa que la aplicación ha pasado a primer plano.

Si tu aplicación pasa a segundo plano, se desencadenará `UIApplicationDidEnterBackgroundNotification`. La sesión permanecerá activa durante `10` segundos (a menos que [cambies el tiempo de espera predeterminado de la sesión](#changing-the-default-session-timeout)) o el usuario cierre tu aplicación.
{% endtab %}

{% tab Web %}
Por defecto, una sesión se inicia cuando llamas por primera vez a `braze.openSession()`. La sesión permanecerá activa hasta `30` minutos de inactividad (a menos que [cambies el tiempo de espera predeterminado de la sesión](#change-session-timeout)) o el usuario cierre la aplicación.
{% endtab %}
{% endtabs %}

## Suscribirse a las actualizaciones de la sesión

### Paso 1: Suscribirse a las actualizaciones

Para suscribirte a las actualizaciones de la sesión, utiliza el método `subscribeToSessionUpdates()`.

{% tabs %}
{% tab Android %}
{% subtabs %}
{% subtab java %}

```java
Braze.getInstance(this).subscribeToSessionUpdates(new IEventSubscriber<SessionStateChangedEvent>() {
  @Override
  public void trigger(SessionStateChangedEvent message) {
    if (message.getEventType() == SessionStateChangedEvent.ChangeType.SESSION_STARTED) {
      // A session has just been started
    }
  }
});
```

{% endsubtab %}
{% subtab kotlin %}

```kotlin
Braze.getInstance(this).subscribeToSessionUpdates { message ->
  if (message.eventType == SessionStateChangedEvent.ChangeType.SESSION_STARTED) {
    // A session has just been started
  }
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
Si registras una devolución de llamada de fin de sesión, se dispara cuando la aplicación vuelve al primer plano. La duración de la sesión se mide desde que la aplicación se abre o está en primer plano, hasta que se cierra o está en segundo plano.

{% subtabs %}
{% subtab swift %}
```swift
// This subscription is maintained through a Braze cancellable, which will observe changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
let cancellable = AppDelegate.braze?.subscribeToSessionUpdates { event in
  switch event {
  case .started(let id):
    print("Session \(id) has started")
  case .ended(let id):
    print("Session \(id) has ended")
  }
}
```

Para suscribirte a un flujo asíncrono, puedes utilizar [`sessionUpdatesStream`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/sessionupdatesstream) en su lugar.

```swift
for await event in braze.sessionUpdatesStream {
  switch event {
  case .started(let id):
    print("Session \(id) has started")
  case .ended(let id):
    print("Session \(id) has ended")
  }
}
```
{% endsubtab %}

{% subtab objective-c %}
```objc
// This subscription is maintained through a Braze cancellable, which will observe changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
BRZCancellable *cancellable = [AppDelegate.braze subscribeToSessionUpdates:^(BRZSessionEvent * _Nonnull event) {
  switch (event.state) {
    case BRZSessionStateStarted:
      NSLog(@"Session %@ has started", event.sessionId);
      break;
    case BRZSessionStateEnded:
      NSLog(@"Session %@ has ended", event.sessionId);
      break;
    default:
      break;
  }
}];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Web %}
En este momento, la suscripción a las actualizaciones de sesión no es compatible con el SDK de Web Braze.
{% endtab %}
{% endtabs %}

### Paso 2: Seguimiento de la sesión de prueba (opcional)

Para probar el seguimiento de la sesión, inicia una sesión en tu dispositivo, luego abre el panel de Braze y busca al usuario correspondiente. En su perfil de usuario, selecciona **Resumen de sesiones**. Si las métricas se actualizan como se espera, el seguimiento de la sesión funciona correctamente.

![La sección de resumen de sesiones de un perfil de usuario que muestra el número de sesiones, la última fecha de uso y la primera fecha de uso.]({% image_buster /assets/img_archive/test_session.png %}){: style="max-width:50%;"}

{% alert note %}
Los detalles específicos de la aplicación sólo se muestran a los usuarios que han utilizado más de una aplicación.
{% endalert %}

## Cambiar el tiempo de espera predeterminado de la sesión {#change-session-timeout}

Puedes cambiar el tiempo que transcurre antes de que una sesión caduque automáticamente.

{% tabs %}
{% tab android %}
Por defecto, el tiempo de espera de la sesión está predeterminado en `10` segundos. Para cambiar esto, abre tu archivo `braze.xml` y añade el parámetro `com_braze_session_timeout`. Puede establecerse en cualquier número entero mayor o igual que `1`.

```xml
<!-- Sets the session timeout to 60 seconds. -->
<integer name="com_braze_session_timeout">60</integer>
```
{% endtab %}

{% tab swift %}
Por defecto, el tiempo de espera de la sesión está predeterminado en `10` segundos. Para cambiar esto, configura `sessionTimeout` en el objeto `configuration` que se pasa a [`init(configuration)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class). Puede establecerse en cualquier número entero mayor o igual que `1`.

{% subtabs %}
{% subtab swift %}
```swift
// Sets the session timeout to 60 seconds
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)
configuration.sessionTimeout = 60;
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endsubtab %}
{% subtab objective-c %}

```objc
// Sets the session timeout to 60 seconds
BRZConfiguration *configuration =
  [[BRZConfiguration alloc] initWithApiKey:brazeApiKey
                                  endpoint:brazeEndpoint];
configuration.sessionTimeout = 60;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Web %}
Por defecto, el tiempo de espera de la sesión está predeterminado en `30` segundos. Para cambiar esto, pasa la opción `sessionTimeoutInSeconds` a tu [`initialize`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize) función. Puede establecerse en cualquier número entero mayor o igual que `1`. 

```js
// Sets the session timeout to 15 minutes instead of the default 30
braze.initialize('YOUR-API-KEY-HERE', { sessionTimeoutInSeconds: 900 });
```
{% endtab %}
{% endtabs %}

{% alert note %}
Si estableces un tiempo de espera de la sesión, toda la semántica de la sesión se extenderá automáticamente hasta el tiempo de espera establecido.
{% endalert %}
