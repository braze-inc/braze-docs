{% multi_lang_include developer_guide/prerequisites/swift.md %} También tendrás que [configurar las notificaciones push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift), lo que incluye implementar el framework `UNNotification`.

Se requiere la siguiente versión mínima del SDK para recibir historias push:

{% sdk_min_versions swift:5.0.0 %}

## Configuración de las historias push

### Paso 1: Añadir el objetivo de la extensión de contenido de notificación {#notification-content-extension}

En el proyecto de tu aplicación, ve al menú **Archivo > Nuevo > Objetivo** y añade un nuevo objetivo `Notification Content Extension` y actívalo.

![]({% image_buster /assets/img/swift/push_story/add_content_extension.png %})

Xcode debe generar un nuevo objetivo para usted y crear archivos automáticamente para ti, entre ellos:

- `NotificationViewController.swift`
- `MainInterface.storyboard`

### Paso 2: Habilitar capacidades {#enable-capabilities}

En Xcode, añade la capacidad Modos de fondo utilizando el panel **Firma y capacidades** al objetivo principal de la aplicación. Selecciona las casillas de verificación **Obtención en segundo plano** y **Notificaciones remotas**.

![]({% image_buster /assets/img/swift/push_story/enable_background_mode.png %})

#### Añadir un grupo de aplicaciones

Además, desde el panel **Firma y capacidades** de Xcode, añade la capacidad Grupos de aplicaciones a tu objetivo de aplicación principal, así como a los objetivos de Extensión de contenido de notificaciones. Después, haz clic en el botón **+**. Utiliza el ID del paquete de tu aplicación para crear el grupo de aplicaciones. Por ejemplo, si el ID del paquete de tu aplicación es `com.company.appname`, puedes llamar a tu grupo de aplicaciones `group.com.company.appname.xyz`.

{% alert important %}
En este contexto, Grupos de aplicaciones se refiere al [derecho de Grupos de aplicaciones](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_application-groups) de Apple y no a tu ID de espacio de trabajo Braze (antes "grupo de aplicaciones").
{% endalert %}

Si no añades tu aplicación a un grupo de aplicaciones, es posible que tu aplicación no rellene determinados campos de la carga útil push y no funcione completamente como se espera.

### Paso 3: Añadir el framework de historias push a tu aplicación {#enable-capabilities}

{% tabs local %}
{% tab Swift Package Manager %}

Después de seguir [la guía de integración de Swift Package Manager]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sdk_integration/?tab=swift%20package%20manager/), añade `BrazePushStory` a tu `Notification Content Extension`:

![En Xcode, en frameworks y librerías, selecciona el ícono "+" para añadir un framework.]({% image_buster /assets/img/swift/push_story/spm1.png %})

![]({% image_buster /assets/img/swift/push_story/spm2.png %})

{% endtab %}
{% tab CocoaPods %}

Añade la siguiente línea a tu archivo de bibliotecas:

```ruby
target 'YourAppTarget' do
pod 'BrazeKit'
pod 'BrazeUI'
pod 'BrazeLocation'
end

target 'YourNotificationContentExtensionTarget' do
pod 'BrazePushStory'
end

# Only include the below if you want to also integrate Rich Push
target 'YourNotificationServiceExtensionTarget' do
pod 'BrazeNotificationService'
end
```

{% alert note %}
Para obtener instrucciones para implementar Rich Push, consulta [Notificaciones enriquecidas]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/rich_notifications/?tab=swift%20package%20manager).
{% endalert %}

Tras actualizar el archivo de bibliotecas, ve al directorio de tu proyecto de aplicación Xcode dentro de tu terminal y ejecuta `pod install`.

{% endtab %}
{% tab Manual %}

Descarga el último `BrazePushStory.zip` de la [página de versiones de GitHub](https://github.com/braze-inc/braze-swift-sdk/releases), extráelo y añade el `BrazePushStory.xcframework` al `Notification Content Extension` de tu proyecto.

![]({% image_buster /assets/img/swift/push_story/manual1.png %})

{% alert important %}
Asegúrate de que la opción **No incrustar** está seleccionada para **BrazePushStory.xcframework** en la columna **Incrustar**.
{% endalert %}

{% endtab %}
{% endtabs %}

### Paso 4: Actualizar tu controlador de vista de notificación {#enable-capabilities}

En `NotificationViewController.swift`, añade la siguiente línea para importar los archivos de cabecera:

```swift
import BrazePushStory
```

A continuación, sustituye la implementación predeterminada heredando [`BrazePushStory.NotificationViewController`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazepushstory/notificationviewcontroller/):

```swift
class NotificationViewController: BrazePushStory.NotificationViewController {}
```

#### Manejo personalizado de eventos de historias push

Si quieres implementar tu propia lógica personalizada para gestionar eventos de notificación push de historias push, hereda `BrazePushStory.NotificationViewController` como se indica arriba y anula los métodos [`didReceive`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazepushstory/notificationviewcontroller/didreceive(_:)) como se indica a continuación.

```swift
import BrazePushStory
import UserNotifications
import UserNotificationsUI

class NotificationViewController: BrazePushStory.NotificationViewController {
  override func didReceive(_ notification: UNNotification) {
    super.didReceive(notification)
    
    // Custom handling logic
  }
  
  override func didReceive(_ response: UNNotificationResponse, completionHandler completion: @escaping (UNNotificationContentExtensionResponseOption) -> Void) {
    super.didReceive(response, completionHandler: completion)
    
    // Custom handling logic
  }
}
```

### Paso 5: Configuración del plist de Extensión de Contenido de Notificación {#notification-content-extension}

Abre el archivo `Info.plist` del `Notification Content Extension`, luego añade y cambia las siguientes claves en `NSExtension \ NSExtensionAttributes`:

| Clave                                              | Tipo    | Valor                  |
|--------------------------------------------------|---------|------------------------|
| `UNNotificationExtensionCategory`                | Cadena  | `ab_cat_push_story_v2` |
| `UNNotificationExtensionDefaultContentHidden`    | Booleano | `YES`                  |
| `UNNotificationExtensionInitialContentSizeRatio` | Número  | `0.6`                  |
| `UNNotificationExtensionUserInteractionEnabled`  | Booleano | `YES`                  |

Tu archivo `Info.plist` debe coincidir con la siguiente imagen:

![]({% image_buster /assets/img/swift/push_story/notificationcontentextension_plist.png %})

### Paso 6: Actualizar la integración de Braze en tu aplicación principal {#update-braze}

Antes de inicializar Braze, asigna el nombre de tu grupo de aplicaciones a la propiedad [`push.appGroup`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/appgroup) de tu configuración Braze.

```swift
let configuration = Braze.Configuration(apiKey: "<YOUR-BRAZE-API-KEY>",
                                        endpoint: "<YOUR-BRAZE-ENDPOINT>")
configuration.push.appGroup = "REPLACE_WITH_APPGROUP"
let braze = Braze(configuration: configuration)
```
