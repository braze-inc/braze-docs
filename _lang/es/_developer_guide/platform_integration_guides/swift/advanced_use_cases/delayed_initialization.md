---
nav_title: Inicialización retardada
article_title: Inicialización retardada para el SDK Swift de Braze
platform: Swift
page_order: 6
description: "Este artículo explica cómo implementar la inicialización retardada del SDK Swift para preservar la gestión de notificaciones push cuando el SDK se inicializa de forma asíncrona."

---

# Inicialización retardada para el SDK Swift de Braze

> Aprende a inicializar tu SDK de Braze Swift de forma asíncrona, garantizando al mismo tiempo que se conserva la gestión de las notificaciones push. Esto puede ser útil cuando necesites configurar otros servicios antes de inicializar el SDK, como obtener datos de configuración de un servidor o esperar el consentimiento del usuario.

## Configuración de la inicialización retardada

### Paso 1: Preparar el SDK para la inicialización retardada

Por predeterminado, si un usuario final abre tu notificación push mientras tu aplicación está en estado finalizado, la notificación push no puede procesarse antes de que se inicialice el SDK.

A partir de [la versión de Braze Swift 10.1.0 del SDK](https://github.com/braze-inc/braze-swift-sdk/releases/tag/10.1.0) y posteriores, puedes manejar esto utilizando el método estático de ayuda: [Braze.prepareForDelayedInitialization(pushAutomation:)](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/preparefordelayedinitialization(pushautomation:)). Este método preparará el SDK para la inicialización retardada configurando el sistema de automatización push.

Antes de inicializar el SDK, todas las notificaciones push procedentes de Braze serán capturadas y puestas en cola. Una vez inicializado el SDK, esas notificaciones push serán procesadas por el SDK. Este método debe llamarse lo antes posible en el ciclo de vida de tu aplicación, ya sea en el método `application(_:didFinishLaunchingWithOptions:)` de tu `AppDelegate` o antes.

{% alert note %}
El SDK de Swift no captura notificaciones push que no sean de Braze: éstas seguirán siendo gestionadas por los métodos de delegado del sistema.
{% endalert %}

{% tabs %}
{% tab Swift - UIKit %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
  // Prepare the SDK for delayed initialization
  Braze.prepareForDelayedInitialization()

  // ... Additional non-Braze setup code

  return true
}
```
{% endtab %}

{% tab Swift - SwiftUI %}
Las aplicaciones SwiftUI necesitan implementar el envoltorio de propiedad [@UIApplicationDelegateAdaptor](https://developer.apple.com/documentation/swiftui/uiapplicationdelegateadaptor) para llamar al método `prepareForDelayedInitialization()`.

```swift
@main
struct MyApp: App {
  @UIApplicationDelegateAdaptor var appDelegate: AppDelegate

  var body: some Scene {
    WindowGroup {
      ContentView()
    }
  }
}

class AppDelegate: NSObject, UIApplicationDelegate {
  
  func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil) -> Bool {
    // Prepare the SDK for delayed initialization
    Braze.prepareForDelayedInitialization()

    // ... Additional non-Braze setup code

    return true
  }
  
}
```
{% endtab %}

{% tab Objective-C %}
```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Prepare the SDK for delayed initialization
  [Braze prepareForDelayedInitialization];
  
  // ... Additional non-Braze setup code

  return YES;
}

```
{% endtab %}
{% endtabs %}

{% alert note %}
[Braze.prepareForDelayedInitialization(pushAutomation:)](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/preparefordelayedinitialization(pushautomation:)) toma un parámetro opcional `pushAutomation` que representa la configuración de automatización de las notificaciones push. Cuando [Braze.Configuration.Push.Automation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.class) es `nil`, se habilitan todas las características de automatización, salvo la solicitud de autorización en el lanzamiento.
{% endalert %}

### Paso 2: Inicializar el SDK de Braze

Después de haber preparado el SDK para una inicialización diferida, puedes inicializarlo de forma asíncrona en cualquier momento futuro. A continuación, el SDK procesará todos los eventos de notificaciones push en cola procedentes de Braze.

Para inicializar el SDK de Braze, sigue el [proceso estándar de inicialización del SDK de Swift]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/).

## Consideraciones

Al utilizar `Braze.prepareForDelayedInitialization(pushAutomation:)`, estás configurando el SDK para que utilice automáticamente las características de automatización de las notificaciones push. No se llamará a ningún método delegado del sistema que gestione notificaciones push para notificaciones push procedentes de Braze.

El SDK sólo procesará una notificación push de Braze y la acción resultante **una vez** inicializado el SDK. Por ejemplo, si un usuario toca una notificación push que abre un vínculo profundo, éste sólo se abrirá una vez inicializada la instancia `Braze`.

Si necesitas realizar un procesamiento adicional de las notificaciones push de Braze, consulta [Suscribirse a las actualizaciones de las notificaciones push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#subscribing-to-push-notifications-updates). Ten en cuenta que, para recibir actualizaciones de notificaciones push que se hayan puesto en cola previamente, debes implementar el controlador de suscripción directamente después de inicializar el SDK.
