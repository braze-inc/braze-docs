{% multi_lang_include developer_guide/prerequisites/cordova.md %} También tendrás que [configurar las notificaciones push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=cordova).

## Configuración de las historias push

### Paso 1: Crear una extensión de contenido de notificación

En tu proyecto Xcode, crea una extensión de contenido de notificación. Para un tutorial completo, consulta [Tutorial de historias push de iOS](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories/).

### Paso 2: Configura tu grupo de aplicaciones push

En el archivo `config.xml` de tu proyecto, configura el grupo de aplicaciones push [que acabas de crear](#cordova_step-1-create-a-notification-content-extension).

```xml
<preference name="com.braze.ios_push_app_group" value="NOTIFICATION_CONTENT_EXTENTION" />
```

Sustituye `PUSH_APP_GROUP` por el nombre de tu grupo de aplicaciones push. Tu `config.xml` debe ser similar al siguiente:

```xml
<preference name="com.braze.ios_push_app_group" value="MyPushAppGroup" />
```

### Paso 3: Añadir un nuevo objetivo

Abre tu archivo de bibliotecas y añade `BrazePushStory` al objetivo de extensión de contenido de notificación [ que creaste anteriormente](#cordova_step-1-create-a-notification-content-extension). Para evitar errores de duplicación de símbolos, utiliza la vinculación estática.

```ruby
target 'NOTIFICATION_CONTENT_EXTENSION' do
  use_frameworks! :linkage => :static
  pod 'BrazePushStory'
end
```

Sustituye `NOTIFICATION_CONTENT_EXTENSION` por el nombre de tu extensión de contenido de notificación. Tu archivo de bibliotecas debe ser similar al siguiente:

```ruby
target 'MyAppNotificationContentExtension' do
  use_frameworks! :linkage => :static
  pod 'BrazePushStory'
end
```

### Paso 4: Reinstala tus dependencias de CocoaPods

En el terminal, ve a tu directorio iOS y reinstala las dependencias de CocoaPod.

```bash
cd PATH_TO_PROJECT/platform/ios
pod install
```
