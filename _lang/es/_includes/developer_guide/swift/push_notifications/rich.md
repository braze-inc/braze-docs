{% multi_lang_include developer_guide/prerequisites/swift.md %} También tendrás que [configurar las notificaciones push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

## Configuración de notificaciones push enriquecidas

### Paso 1: Crear una extensión de servicio

Para crear una [extensión del servicio de notificación](https://developer.apple.com/reference/usernotifications/unnotificationserviceextension), ve a **Archivo > Nuevo > Destino** en Xcode y selecciona **Extensión del servicio de notificación**.

![]({% image_buster /assets/img_archive/ios10_se_at.png %}){: style="max-width:90%"}

Asegúrate de que la opción **Incrustar en la aplicación** está activada para incrustar la extensión en tu aplicación.

### Paso 2: Configuración de la extensión del servicio de notificación

Una extensión del servicio de notificación es un binario propio que se incluye con tu aplicación. Debe configurarse en el [Portal del Desarrollador de Apple](https://developer.apple.com) con su propio ID de aplicación y perfil de aprovisionamiento.

El ID del paquete de la extensión del servicio de notificación debe ser distinto del ID del paquete de tu aplicación principal. Por ejemplo, si el ID del paquete de tu aplicación es `com.company.appname`, puedes utilizar `com.company.appname.AppNameServiceExtension` para la extensión de tu servicio.

### Paso 3: Integración de notificaciones push enriquecidas

Para una guía paso a paso sobre la integración de notificaciones push enriquecidas con `BrazeNotificationService`, consulta nuestro [tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications).

Para ver un ejemplo, consulta el uso en [`NotificationService`](https://github.com/braze-inc/braze-swift-sdk/blob/main/Examples/Swift/Sources/PushNotificationsServiceExtension/NotificationService.swift) de nuestra aplicación Ejemplos.

#### Añadir el framework de notificaciones push enriquecidas a tu aplicación

{% tabs local %}
{% tab Swift Package Manager %}

Después de seguir la [guía de integración de Swift Package Manager]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sdk_integration/?tab=swift%20package%20manager/), añade `BrazeNotificationService` a tu `Notification Service Extension` haciendo lo siguiente:

1. En Xcode, en marcos y bibliotecas, selecciona el ícono <i class="fas fa-plus"></i> añadir para añadir un framework. <br><br>![El ícono "más" se encuentra en frameworks y bibliotecas en Xcode.]({% image_buster /assets/img_archive/rich_notification.png %})<br><br>

2. Selecciona el marco "BrazeNotificationService". <br><br>![El "framework BrazeNotificationService se puede seleccionar en el modal que se abre.]({% image_buster /assets/img_archive/rich_notification2.png %})

{% endtab %}
{% tab CocoaPods %}

Añade lo siguiente a tu archivo de bibliotecas:

```ruby
target 'YourAppTarget' do
  pod 'BrazeKit'
  pod 'BrazeUI'
  pod 'BrazeLocation'
end

target 'YourNotificationServiceExtensionTarget' do
  pod 'BrazeNotificationService'
end

# Only include the below if you want to also integrate Push Stories
target 'YourNotificationContentExtensionTarget' do
  pod 'BrazePushStory'
end
```

{% alert note %}
Para obtener instrucciones sobre cómo poner en práctica las historias push, consulta la [documentación]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/push_story/?tab=swift%20package%20manager).
{% endalert %}

Tras actualizar el archivo de bibliotecas, ve al directorio de tu proyecto de aplicación Xcode dentro de tu terminal y ejecuta `pod install`.

{% endtab %}

{% tab Manual %}

Para añadir `BrazeNotificationService.xcframework` a tu `Notification Service Extension`, consulta [Integración manual]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sdk_integration?tab=manual/).

![]({% image_buster /assets/img/swift/rich_push/manual1.png %})

{% endtab %}
{% endtabs %}

#### Utilizar tu propia UNNotificationServiceExtension

Si necesitas utilizar tu propia UNNotificationServiceExtension, puedes llamar en su lugar a [`brazeHandle`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazenotificationservice/brazehandle(request:contenthandler:)) en tu método `didReceive`.

```swift
import BrazeNotificationService
import UserNotifications

class NotificationService: UNNotificationServiceExtension {

  override func didReceive(
    _ request: UNNotificationRequest,
    withContentHandler contentHandler: @escaping (UNNotificationContent) -> Void
  ) {
    if brazeHandle(request: request, contentHandler: contentHandler) {
      return
    }

    // Custom handling here

    contentHandler(request.content)
  }
}
```

### Paso 4: Crear una notificación enriquecida en tu panel de control

Tu equipo de marketing también puede crear notificaciones enriquecidas desde el panel. Crea una notificación push a través del compositor push y simplemente adjunta una imagen o GIF, o proporciona una URL que aloje una imagen, GIF o video. Ten en cuenta que los activos se descargan al recibir las notificaciones push, por lo que debes prever grandes picos sincrónicos de solicitudes si alojas tus contenidos.
