---
nav_title: Seguimiento de la sesión
article_title: Seguimiento de sesión para iOS
platform: Swift
page_order: 0
search_rank: 1
description: "En este artículo de referencia se muestra cómo suscribirse a las actualizaciones de sesión del SDK Swift."

---

# Seguimiento de la sesión

> El SDK de Braze informa de los datos de sesión utilizados por el panel de Braze para calcular la participación de los usuarios y otros análisis esenciales para comprender a tus usuarios. 

Nuestro SDK genera puntos de datos de "inicio de sesión" y "cierre de sesión" que tienen en cuenta la duración de la sesión y el recuento de sesiones visibles dentro del panel Braze, basándose en la siguiente semántica de sesión.

## Ciclo de vida de la sesión

Una sesión se inicia cuando llamas a `Braze.init(configuration:)`. Por defecto, esto ocurre cuando se dispara la notificación `UIApplicationWillEnterForegroundNotification` (cuando la aplicación entra en primer plano). El final de la sesión se produce cuando la aplicación abandona el primer plano (por ejemplo, cuando se dispara la notificación `UIApplicationDidEnterBackgroundNotification` o cuando la aplicación muere).

{% alert note %}
Si necesitas forzar una nueva sesión, puedes hacerlo cambiando de usuario.
{% endalert %}

## Personalizar el tiempo de espera de la sesión

Puedes establecer el `sessionTimeout` al valor entero deseado en tu objeto `configuration` pasado a [`init(configuration)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class).

{% tabs %}
{% tab swift %}

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
{% endtab %}
{% tab objective-c %}

```objc
// Sets the session timeout to 60 seconds
BRZConfiguration *configuration =
  [[BRZConfiguration alloc] initWithApiKey:brazeApiKey
                                  endpoint:brazeEndpoint];
configuration.sessionTimeout = 60;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endtab %}
{% endtabs %}

Si has establecido un tiempo de espera de la sesión, toda la semántica de la sesión se extiende a ese tiempo de espera personalizado.

{% alert note %}
El valor mínimo de `sessionTimeout` es 1 segundo. El valor predeterminado es 10 segundos.
{% endalert %}

## Probar el seguimiento de la sesión

Para detectar sesiones a través de tu usuario, busca a tu usuario en el panel y ve a **Resumen de sesiones** en el perfil de usuario. Puedes confirmar que el seguimiento de sesiones funciona comprobando que la métrica "Sesiones" aumenta cuando esperas que lo haga. Los detalles específicos de la aplicación se mostrarán cuando el usuario haya utilizado más de una aplicación.

![La sección de resumen de sesiones de un perfil de usuario que muestra el número de sesiones, la última fecha de uso y la primera fecha de uso.]({% image_buster /assets/img_archive/test_session.png %}){: style="max-width:40%;"}

Los detalles específicos de la aplicación sólo se mostrarán si el usuario ha utilizado más de una aplicación.

## Suscribirse a las actualizaciones de la sesión

Para escuchar las actualizaciones de la sesión, utiliza el método [`subscribeToSessionUpdates(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/subscribetosessionupdates(_:)). Los eventos de inicio y fin de sesión sólo se registrarán cuando la aplicación se esté ejecutando en primer plano. Si registras una devolución de llamada a eventos de fin de sesión y la aplicación está en segundo plano, la devolución se disparará cuando la aplicación vuelva a estar en primer plano. Sin embargo, la duración de la sesión se sigue midiendo como el tiempo transcurrido desde que se abre la aplicación o se pone en primer plano hasta que se cierra o se pone en segundo plano.

{% tabs %}
{% tab swift %}
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
{% endtab %}

{% tab objective-c %}
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
{% endtab %}
{% endtabs %}

Alternativamente, en Swift, puedes utilizar la función [`sessionUpdatesStream`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/sessionupdatesstream) `AsyncStream` para observar los cambios asíncronos:

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

