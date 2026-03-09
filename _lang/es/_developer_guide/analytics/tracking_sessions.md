---
nav_title: Sesión de seguimiento
article_title: Realiza el seguimiento de las sesiones a través del SDK de Braze.
page_order: 3.3
description: "Aprende a realizar el seguimiento de las sesiones a través del SDK de Braze."

---

# Sesión de seguimiento

> Aprende a realizar el seguimiento de las sesiones a través del SDK de Braze.

{% alert note %}
Para los SDK de envoltura que no aparecen en la lista, utiliza el método nativo de Android o SWIFT correspondiente.
{% endalert %}

{% multi_lang_include developer_guide/_shared/about_session_lifecycle.md %}

## Definición de inactividad

Comprender cómo se define y se mide la inactividad es fundamental para administrar eficazmente los ciclos de vida de las sesiones en el SDK Web. La inactividad se refiere al periodo durante el cual el SDK Web de Braze no detecta ningún evento de seguimiento realizado por el usuario.

### Cómo se mide la inactividad

El SDK Web realiza el seguimiento de la inactividad basándose en [los eventos rastreados por el SDK]({{site.baseurl}}/user_guide/data/activation/custom_data/events/#events). El SDK mantiene un temporizador interno que se reinicia cada vez que se envía un evento de seguimiento. Si no se produce ningún evento de seguimiento rastreado por el SDK dentro del período de tiempo de espera configurado, la sesión se considera inactiva y finaliza.

Para obtener más información sobre cómo se implementa el ciclo de vida de la sesión en el SDK web, consulta el código fuente de gestión de sesiones en el [repositorio GitHub del SDK web de Braze](https://github.com/braze-inc/braze-web-sdk/blob/master/src/session.ts).

**Lo que se considera actividad predeterminada:**
- Abrir o actualizar la aplicación Web
- Interactuar con elementos de la interfaz de usuario impulsados por Braze (como [mensajes dentro de la aplicación]({{site.baseurl}}/developer_guide/in_app_messages/) o [tarjetas de contenido]({{site.baseurl}}/developer_guide/content_cards/)).
- Llamar a métodos SDK que envían eventos rastreados (como [eventos personalizados]({{site.baseurl}}/developer_guide/analytics/logging_events/) o [actualizaciones de atributos de usuario]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/))

**Lo que no se considera actividad predeterminada:**
- Cambiar a otra pestaña del navegador
- Minimizar la ventana del navegador
- Eventos de enfoque o desenfoque del navegador
- Desplazamiento o movimientos del ratón en la página

{% alert note %}
El SDK web no realiza un seguimiento automático de los cambios de visibilidad del navegador, los cambios de pestaña o el foco del usuario. Sin embargo, puedes realizar el seguimiento de estas interacciones a nivel del navegador implementando detectores de eventos personalizados mediante la [API de visibilidad de página](https://developer.mozilla.org/en-US/docs/Web/API/Page_Visibility_API) del navegador y enviando [eventos personalizados]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=web) a Braze. Para ver un ejemplo de implementación, consulta [Seguimiento](#tracking-custom-inactivity) de [la inactividad personalizada](#tracking-custom-inactivity).
{% endalert %}

### Configuración del tiempo de espera de la sesión

De forma predeterminada, el SDK web considera que una sesión está inactiva tras 30 minutos sin eventos de seguimiento. Puedes personalizar este umbral al inicializar el SDK utilizando el`sessionTimeoutInSeconds`parámetro . Para obtener más información sobre cómo configurar este parámetro, incluidos ejemplos de código, consulta [Cambiar el tiempo de espera predeterminado de la sesión](#changing-the-default-session-timeout).

### Ejemplo: Comprender los escenarios de inactividad

Considera el siguiente escenario:

1. Un usuario abre tu sitio web y el SDK inicia una sesión llamando a [`braze.openSession()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#opensession).
2. El usuario cambia a otra pestaña del navegador para ver otro sitio web durante 30 minutos.
3. Durante este tiempo, no se producen eventos de seguimiento del SDK en tu sitio web.
4. Tras 30 minutos de inactividad, la sesión finaliza automáticamente.
5. Cuando el usuario vuelve a la pestaña de tu sitio web y desencadena un evento SDK (como ver una página o interactuar con el contenido), comienza una nueva sesión.

### Seguimiento de la inactividad personalizada

Si necesitas realizar un seguimiento de la inactividad basándote en la visibilidad del navegador o el cambio de pestañas, implementa detectores de eventos personalizados en tu código JavaScript. Utiliza eventos del navegador como`visibilitychange`  para detectar cuándo los usuarios abandonan tu página y envía manualmente [eventos personalizados]({{site.baseurl}}/developer_guide/analytics/logging_events/) a Braze o llama a[`braze.openSession()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#opensession)  cuando sea apropiado.

```javascript
// Example: Track when user switches away from tab
document.addEventListener('visibilitychange', function() {
  if (document.hidden) {
    // User switched away - optionally log a custom event
    braze.logCustomEvent('tab_hidden');
  } else {
    // User returned - optionally start a new session and/or log an event
    // braze.openSession();
    braze.logCustomEvent('tab_visible');
  }
});
```

Para obtener más información sobre cómo registrar eventos personalizados, consulta [Registrar eventos personalizados]({{site.baseurl}}/developer_guide/analytics/logging_events/). Para obtener más información sobre el ciclo de vida de la sesión y la configuración del tiempo de espera, consulta [Cambiar el tiempo de espera predeterminado de la sesión](#change-session-timeout).

## Suscribirse a las actualizaciones de la sesión

### Paso 1: Suscribirse a las actualizaciones

Para suscribirte a las actualizaciones de la sesión, utiliza el`subscribeToSessionUpdates()`método .

{% tabs %}
{% tab web %}
En este momento, la suscripción a las actualizaciones de sesión no es compatible con el SDK de Web Braze.
{% endtab %}

{% tab android %}
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
Si realizas el registro de una devolución de llamada al final de la sesión, esta se activa cuando la aplicación vuelve al primer plano. La duración de la sesión se mide desde el momento en que se abre la aplicación o pasa a primer plano, hasta que se cierra o pasa a segundo plano.

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

Para suscribirte a una transmisión asíncrona, puedes utilizar[`sessionUpdatesStream`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/sessionupdatesstream)  en su lugar.

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

{% tab react native %}
El SDK de React Native no ofrece un método para suscribirse directamente a las actualizaciones de la sesión. El ciclo de vida de la sesión se administra mediante el SDK nativo subyacente, por lo que, para suscribirte a las actualizaciones, utiliza el enfoque de plataforma nativa para la pestaña **Android** o **SWIFT**.
{% endtab %}
{% endtabs %}

### Paso 2: Seguimiento de sesiones de prueba (opcional)

Para probar el seguimiento de sesiones, inicia una sesión en tu dispositivo, luego abre el panel de Braze y busca al usuario correspondiente. En tu perfil de usuario, selecciona **Resumen de sesiones.** Si las métricas se actualizan según lo esperado, el seguimiento de sesiones funciona correctamente.

![La sección de resumen de sesiones de un perfil de usuario que muestra el número de sesiones, la última fecha de uso y la primera fecha de uso.]({% image_buster /assets/img_archive/test_session.png %}){: style="max-width:50%;"}

{% alert note %}
Los detalles específicos de la aplicación solo se muestran a los usuarios que han utilizado más de una aplicación.
{% endalert %}

## Cambiar el tiempo de espera predeterminado de la sesión {#change-session-timeout}

Puedes cambiar el tiempo que transcurre antes de que una sesión caduque automáticamente.

{% tabs %}
{% tab web %}
De forma predeterminada, el tiempo de espera de la sesión está establecido en`30`  minutos. Para cambiar esto, pasa la`sessionTimeoutInSeconds`opción a tu[`initialize`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize)función. Se puede establecer en cualquier número entero mayor o igual que `1`. 

```js
// Sets the session timeout to 15 minutes instead of the default 30
braze.initialize('YOUR-API-KEY-HERE', { sessionTimeoutInSeconds: 900 });
```
{% endtab %}

{% tab android %}
De forma predeterminada, el tiempo de espera de la sesión está establecido en`10`  segundos. Para cambiar esto, abre tu`braze.xml`archivo y añade el`com_braze_session_timeout`parámetro. Se puede establecer en cualquier número entero mayor o igual que `1`.

```xml
<!-- Sets the session timeout to 60 seconds. -->
<integer name="com_braze_session_timeout">60</integer>
```
{% endtab %}

{% tab swift %}
De forma predeterminada, el tiempo de espera de la sesión está establecido en`10`  segundos. Para cambiar esto, configura`sessionTimeout`  en el`configuration`objeto que se pasa a [`init(configuration)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class). Se puede establecer en cualquier número entero mayor o igual que `1`.

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

{% tab react native %}
El SDK de React Native depende de los SDK nativos para administrar las sesiones. Para cambiar el tiempo de espera predeterminado de la sesión, configúralo en la capa nativa:

- **Android:** Configura `com_braze_session_timeout`tu`braze.xml`archivo. Para obtener más información, selecciona la pestaña **Android**.
- **iOS:** Coloca  `sessionTimeout`tu`Braze.Configuration`  objeto. Para obtener más información, selecciona la pestaña **SWIFT**.
{% endtab %}
{% endtabs %}

{% alert note %}
Si estableces un tiempo de espera para la sesión, toda la semántica de la sesión se ampliará automáticamente hasta el tiempo de espera establecido en la configuración.
{% endalert %}
