{% multi_lang_include developer_guide/prerequisites/cordova.md %} También tendrás que [configurar las notificaciones push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=cordova).

## Configuración de notificaciones push enriquecidas

### Paso 1: Crear una extensión del servicio de notificación

En tu proyecto Xcode, crea una extensión de servicio de notificación. Para un tutorial completo, consulta [Tutorial de notificaciones push enriquecidas de iOS](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications).

### Paso 2: Añadir un nuevo objetivo

Abre tu archivo de bibliotecas y añade `BrazeNotificationService` al objetivo de extensión del servicio de notificación [que acabas de crear](#cordova_step-1-create-a-notification-service-extension). Si ya se ha añadido `BrazeNotificationService` a un objetivo, elimínalo antes de continuar. Para evitar errores de duplicación de símbolos, utiliza la vinculación estática.

```ruby
target 'NOTIFICATION_SERVICE_EXTENSION' do
  use_frameworks! :linkage => :static
  pod 'BrazeNotificationService'
end
```

Sustituye `NOTIFICATION_SERVICE_EXTENSION` por el nombre de la extensión de tu servicio de notificación. Tu archivo de bibliotecas debe ser similar al siguiente:

```ruby
target 'MyAppRichNotificationService' do
  use_frameworks! :linkage => :static
  pod 'BrazeNotificationService'
end
```

### Paso 3: Reinstala tus dependencias de CocoaPods

En el terminal, ve al directorio iOS de tu proyecto y reinstala las dependencias de CocoaPod.

```bash
cd PATH_TO_PROJECT/platform/ios
pod install
```
