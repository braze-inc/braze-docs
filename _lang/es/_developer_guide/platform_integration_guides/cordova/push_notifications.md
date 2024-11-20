---
nav_title: Notificaciones push
article_title: Notificaciones push para el SDK Braze de Cordova
platform:
  - Cordova
  - iOS
  - Android
page_order: 1
page_type: reference
description: "Este artículo trata sobre la implementación de notificaciones push en Cordova."
channel: push
---

# Integración de notificaciones push

> Aprende a integrar notificaciones push para el SDK Cordova de Braze.

{% multi_lang_include cordova/prerequisites.md %}

## Características básicas de push

De manera predeterminada, las características básicas de notificación push están habilitadas en el plugin Braze Cordova. Puedes desactivar estas características [personalizando tus configuraciones XML]({{site.baseurl}}/developer_guide/platform_integration_guides/cordova/initial_setup/customizations/#customization-options). Para conocer más a fondo las características de las notificaciones push nativas, consulta las guías de notificaciones push [de iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/) y [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/).

## Características push ampliadas

{% alert important %}
Cada vez que añadas, elimines o actualices tus plugins de Cordova, Cordova sobrescribirá el archivo de bibliotecas de tu proyecto Xcode. Esto significa que tendrás que repetir este proceso cada vez que modifiques tus plugins de Cordova.
{% endalert %}

### Notificaciones push enriquecidas

#### Paso 1: Crear una extensión del servicio de notificación

En tu proyecto Xcode, crea una extensión de servicio de notificación. Para un tutorial completo, consulta [Tutorial de notificaciones push enriquecidas de iOS](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications).

#### Paso 2: Añadir un nuevo objetivo

Abre tu archivo de bibliotecas y añade `BrazeNotificationService` al objetivo de extensión del servicio de notificación [que acabas de crear](#step-1-create-a-notification-service-extension). Si ya se ha añadido `BrazeNotificationService` a un objetivo, elimínalo antes de continuar. Para evitar errores de duplicación de símbolos, utiliza la vinculación estática.

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

#### Paso 3: Reinstala tus dependencias de CocoaPods

En el terminal, ve al directorio iOS de tu proyecto y reinstala las dependencias de CocoaPod.

```bash
cd PATH_TO_PROJECT/platform/ios
pod install
```

### Historias push

#### Paso 1: Crear una extensión de contenido de notificación

En tu proyecto Xcode, crea una extensión de contenido de notificación. Para un tutorial completo, consulta [Tutorial de historias push de iOS](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories/).

#### Paso 2: Configura tu grupo de aplicaciones push

En el archivo `config.xml` de tu proyecto, configura el grupo de aplicaciones push [que acabas de crear](#step-1-create-a-notification-content-extension).

```xml
<preference name="com.braze.ios_push_app_group" value="NOTIFICATION_CONTENT_EXTENTION" />
```

Sustituye `PUSH_APP_GROUP` por el nombre de tu grupo de aplicaciones push. Tu `config.xml` debe ser similar al siguiente:

```xml
<preference name="com.braze.ios_push_app_group" value="MyPushAppGroup" />
```

#### Paso 3: Añadir un nuevo objetivo

Abre tu archivo de bibliotecas y añade `BrazePushStory` al objetivo de extensión de contenido de notificación [ que creaste anteriormente](#step-1-create-a-notification-content-extension). Para evitar errores de duplicación de símbolos, utiliza la vinculación estática.

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

#### Paso 4: Reinstala tus dependencias de CocoaPods

En el terminal, ve a tu directorio iOS y reinstala las dependencias de CocoaPod.

```bash
cd PATH_TO_PROJECT/platform/ios
pod install
```
