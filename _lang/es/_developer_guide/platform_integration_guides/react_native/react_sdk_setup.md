---
nav_title: Configuración inicial del SDK
article_title: Configuración inicial del SDK para React Native
platform: React Native
page_order: 1
description: "Esta referencia presenta el SDK de React Native y explica cómo integrarlo de forma nativa en Android e iOS."
search_rank: 1
---

# Configuración inicial del SDK

> En este artículo de referencia se explica cómo instalar el SDK de Braze para React Native. La instalación del SDK React Native de Braze proporciona una funcionalidad básica de análisis y te permite integrar mensajes dentro de la aplicación y tarjetas de contenido tanto para iOS como para Android con una sola base de código.

## Requisitos previos y compatibilidad

Para configurar este SDK, se necesita React Native versión 0.71 o posterior. Para ver la lista completa de versiones compatibles, consulta nuestro [repositorio GitHub del SDK para React Native](https://github.com/braze-inc/braze-react-native-sdk?tab=readme-ov-file#version-support).

### Soporte de la nueva arquitectura React Native

{% sdk_min_versions reactnative:2.0.1 %}

## Utilizar Braze con la Nueva Arquitectura

El SDK de React Native de Braze es compatible con cualquier aplicación que utilice la [nueva arquitectura React Native](https://reactnative.dev/docs/the-new-architecture/landing-page) a partir de la versión 2.0.1+ del SDK.

A partir de la versión 6.0.0 del SDK, Braze se ha actualizado internamente a un Módulo Turbo React Native, que puede seguir utilizándose con la nueva arquitectura o con la arquitectura puente heredada. Dado que el módulo Turbo es compatible con versiones anteriores, no se requiere ningún paso de migración aparte de los cambios de última hora mencionados en [el registro de cambios](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md) y que requieren React Native v0.70+.

{% alert warning %}
Si tu aplicación iOS se ajusta a `RCTAppDelegate` y seguía nuestra configuración anterior de `AppDelegate` en esta documentación, o en el proyecto de ejemplo de Braze, asegúrate de hacer referencia a los ejemplos de la [configuración nativa Completa](#step-2-complete-native-setup) para evitar que se produzcan fallos al suscribirse a eventos en el módulo Turbo.
{% endalert %}

## Paso 1: Integrar la biblioteca Braze

{% tabs local %}
{% tab npm %}
```bash
npm install @braze/react-native-sdk
```
{% endtab %}
{% tab hilo %}
```bash
yarn add @braze/react-native-sdk
```
{% endtab %}
{% endtabs %}

## Paso 2: Configuración nativa completa

{% tabs %}
{% tab Expo %}

#### Paso 2.1: Instala el plugin Braze Expo

Asegúrate de que tu SDK de React Native de Braze sea de la versión 1.37.0 en adelante. A continuación, instala el complemento Braze Expo.

```bash
expo install @braze/expo-plugin
```

#### Paso 2.2: Añade el plugin a tu app.json

En tu `app.json`, añade el Plugin Braze Expo. Puedes proporcionar las siguientes opciones de configuración:

| Método                                        | Tipo    | Descripción                                                                                                                                              |
| --------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `androidApiKey`                               | cadena  | Se requiere. La [clave de API]({{site.baseurl}}/api/identifier_types/) para tu aplicación Android, ubicada en tu panel Braze en **Administrar configuración**. |
| `iosApiKey`                                   | cadena  | Se requiere. La [clave de API]({{site.baseurl}}/api/identifier_types/) para tu aplicación iOS, ubicada en tu panel Braze en **Gestionar configuración**.     |
| `baseUrl`                                     | cadena  | Se requiere. El [punto final de SDK]({{site.baseurl}}/api/basics/#endpoints) de tu aplicación, situado en tu panel de Braze, en **Administrar configuración**.    |
| `enableBrazeIosPush`                          | booleano | Solo para iOS. Si utilizar Braze para gestionar las notificaciones push en iOS. Introducido en el SDK de React Native versión 1.38.0 y Expo Plugin versión 0.4.0.                       |
| `enableFirebaseCloudMessaging`                | booleano | Solo para Android. Si se utiliza Firebase Cloud Messaging para las notificaciones push. Introducido en el SDK de React Native versión 1.38.0 y Expo Plugin versión 0.4.0.             |
| `firebaseCloudMessagingSenderId`              | cadena  | Solo para Android. Tu ID de remitente de Firebase Cloud Messaging. Introducido en el SDK de React Native versión 1.38.0 y Expo Plugin versión 0.4.0.                                    |
| `sessionTimeout`                              | entero | El tiempo de espera de la sesión Braze para tu aplicación en segundos.                                                                                               |
| `enableSdkAuthentication`                     | booleano | Si se habilita la característica [de autentificación del SDK](https://www.braze.com/docs/developer_guide/platform_wide/sdk_authentication#sdk-authentication).      |
| `logLevel`                                    | entero | El nivel de registro de tu aplicación. El nivel de registro predeterminado es 8 y registrará mínimamente la información. Para habilitar el registro detallado para la depuración, utiliza el nivel de registro 0.    |
| `minimumTriggerIntervalInSeconds`             | entero | El intervalo de tiempo mínimo en segundos entre desencadenamientos. Predeterminado a 30 segundos.                                                                           |
| `enableAutomaticLocationCollection`           | booleano | Si está habilitada la recogida automática de ubicaciones (si el usuario lo permite).                                                                                  |
| `enableGeofence`                              | booleano | Si están habilitadas las geovallas.                                                                                                                           |
| `enableAutomaticGeofenceRequests`             | booleano | Si las solicitudes de geovalla deben hacerse automáticamente.                                                                                                  |
| `dismissModalOnOutsideTap`                    | booleano | Solo para iOS. Si un mensaje modal dentro de la aplicación se descartará cuando el usuario haga clic fuera del mensaje dentro de la aplicación.                                           |
| `androidHandlePushDeepLinksAutomatically`     | booleano | Solo para Android. Si el SDK de Braze debe gestionar automáticamente los vínculos profundos push.                                                                         |
| `androidPushNotificationHtmlRenderingEnabled` | booleano | Solo para Android. Establece si el contenido de texto de una notificación push debe ser interpretado y renderizado como HTML utilizando `android.text.Html.fromHtml`.        |
| `androidNotificationAccentColor`              | cadena  | Solo para Android. Establece el color de acento de las notificaciones de Android.                                                                                                |
| `androidNotificationLargeIcon`                | cadena  | Solo para Android. Establece el icono grande de notificación de Android.                                                                                                  |
| `androidNotificationSmallIcon`                | cadena  | Solo para Android. Establece el icono pequeño de notificación de Android.                                                                                                  |
| `iosRequestPushPermissionsAutomatically`      | booleano | Solo para iOS. Si se debe pedir automáticamente al usuario permisos push al iniciar la aplicación.                                                          |
| `enableBrazeIosRichPush`                      | booleano | Solo para iOS. Si se habilitan las características de notificaciones push enriquecidas para iOS.                                                                                                  |
| `enableBrazeIosPushStories`                   | booleano | Solo para iOS. Habilitar o no las Historias push de Braze para iOS.                                                                                                  |
| `iosPushStoryAppGroup`                        | cadena  | Solo para iOS. El grupo de aplicaciones utilizado para las historias push de iOS.                                                                                                       |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Ejemplo de configuración:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "androidApiKey": "YOUR-ANDROID-API-KEY",
          "iosApiKey": "YOUR-IOS-API-KEY",
          "baseUrl": "YOUR-SDK-ENDPOINT",
          "sessionTimeout": 60,
          "enableGeofence": false,
          "enableBrazeIosPush": false,
          "enableFirebaseCloudMessaging": false,
          "firebaseCloudMessagingSenderId": "YOUR-FCM-SENDER-ID",
          "androidHandlePushDeepLinksAutomatically": true,
          "enableSdkAuthentication": false,
          "logLevel": 0,
          "minimumTriggerIntervalInSeconds": 0,
          "enableAutomaticLocationCollection": false,
          "enableAutomaticGeofenceRequests": false,
          "dismissModalOnOutsideTap": true,
          "androidPushNotificationHtmlRenderingEnabled": true,
          "androidNotificationAccentColor": "#ff3344",
          "androidNotificationLargeIcon": "@drawable/custom_app_large_icon",
          "androidNotificationSmallIcon": "@drawable/custom_app_small_icon",
          "iosRequestPushPermissionsAutomatically": false,
          "enableBrazeIosPushStories": true,
          "iosPushStoryAppGroup": "group.com.example.myapp.PushStories"
        }
      ],
    ]
  }
}
```

#### Paso 2.3: Construye y ejecuta tu aplicación

Preconstruir tu aplicación generará los archivos nativos necesarios para que funcione el SDK de Braze.

```bash
expo prebuild
```

Ejecuta tu aplicación como se especifica en [los documentos de la Expo](https://docs.expo.dev/workflow/customizing/). Ten en cuenta que cualquier cambio en las opciones de configuración te obligará a precompilar y ejecutar de nuevo la aplicación.

{% endtab %}
{% tab Android %}

#### Paso 2.1: Añade nuestro repositorio

En tu proyecto de nivel superior `build.gradle`, añade lo siguiente en `buildscript` > `dependencies`:

```groovy
buildscript {
    dependencies {
        ...
        // Choose your Kotlin version
        classpath("org.jetbrains.kotlin:kotlin-gradle-plugin:1.8.10")
    }
}
```

Esto añadirá Kotlin a tu proyecto.

#### Paso 2.2: Configurar el SDK de Braze

Para conectarte a los servidores de Braze, crea un archivo `braze.xml` en la carpeta `res/values` de tu proyecto. Pega el siguiente código y sustituye la [clave de]({{site.baseurl}}/api/identifier_types/) API y el [punto final]({{site.baseurl}}/api/basics/#endpoints) por tus valores:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">YOU_APP_IDENTIFIER_API_KEY</string>
<string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

Añade los permisos necesarios a tu archivo `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert tip %}
En la versión 12.2.0 o posterior del SDK de Braze, puedes introducir automáticamente la biblioteca android-sdk-location configurando `importBrazeLocationLibrary=true` en tu archivo `gradle.properties`.
{% endalert %}

#### Paso 2.3: Implementar el seguimiento de la sesión del usuario

Las llamadas a `openSession()` y `closeSession()` se gestionan automáticamente.
Añade el siguiente código al método `onCreate()` de tu clase `MainApplication`:

{% subtabs local %}
{% subtab JAVA %}
```java
import com.braze.BrazeActivityLifecycleCallbackListener;

@Override
public void onCreate() {
    super.onCreate();
    ...
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
}
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
import com.braze.BrazeActivityLifecycleCallbackListener

override fun onCreate() {
    super.onCreate()
    ...
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener())
}
```
{% endsubtab %}
{% endsubtabs %}

#### Paso 2.4: Maneja las actualizaciones de intención

Si tu MainActivity tiene `android:launchMode` configurado en `singleTask`, añade el siguiente código a tu clase `MainActivity`:

{% subtabs local %}
{% subtab JAVA %}
```java
@Override
public void onNewIntent(Intent intent) {
    super.onNewIntent(intent);
    setIntent(intent);
}
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
override fun onNewIntent(intent: Intent) {
    super.onNewIntent(intent)
    setIntent(intent)
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab iOS %}

#### Paso 2.1: (Opcional) Configurar archivo de bibliotecas para XCFrameworks dinámicos

Para importar determinadas bibliotecas Braze, como BrazeUI, en un archivo Objective-C++, tendrás que utilizar la sintaxis `#import`. A partir de la versión 7.4.0 del SDK Swift de Braze, los binarios tienen un [canal de distribución opcional como XCFrameworks dinámicos](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic), que son compatibles con esta sintaxis.

Si quieres utilizar este canal de distribución, anula manualmente las ubicaciones de las fuentes de CocoaPods en tu archivo de bibliotecas. Consulta el ejemplo que aparece a continuación y sustituye `{your-version}` por la versión correspondiente que desees importar:

```ruby
pod 'BrazeKit', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeKit.podspec'
pod 'BrazeUI', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeUI.podspec'
pod 'BrazeLocation', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeLocation.podspec'
```

#### Paso 2.2: Instalar pods

Dado que React Native vincula automáticamente las bibliotecas a la plataforma nativa, puedes instalar el SDK con la ayuda de CocoaPods.

Desde la carpeta raíz del proyecto:

```bash
# To install using the React Native New Architecture
cd ios && RCT_NEW_ARCH_ENABLED=1 pod install

# To install using the React Native legacy architecture
cd ios && pod install
```

#### Paso 2.3: Configurar el SDK de Braze

{% subtabs local %}
{% subtab SWIFT %}

Importa el SDK de Braze en la parte superior del archivo `AppDelegate.swift`:
```swift
import BrazeKit
```

En el método `application(_:didFinishLaunchingWithOptions:)`, sustituye la [clave de]({{site.baseurl}}/api/identifier_types/) API y el [punto final]({{site.baseurl}}/api/basics/#endpoints) por los valores de tu aplicación. A continuación, crea la instancia de Braze utilizando la configuración, y crea una propiedad estática en la dirección `AppDelegate` para facilitar el acceso:

{% alert note %}
Nuestro ejemplo supone una implementación de [RCTAppDelegate](https://github.com/facebook/react-native/blob/e64756ae5bb5c0607a4d97a134620fafcb132b3b/packages/react-native/Libraries/AppDelegate/RCTAppDelegate.h), que proporciona una serie de abstracciones en la configuración de React Native. Si utilizas una configuración diferente para tu aplicación, asegúrate de ajustar tu implementación según sea necesario.
{% endalert %}

```swift
func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil
) -> Bool {
    // Setup Braze
    let configuration = Braze.Configuration(
        apiKey: "{BRAZE_API_KEY}",
        endpoint: "{BRAZE_ENDPOINT}")
    // Enable logging and customize the configuration here.
    configuration.logger.level = .info
    let braze = BrazeReactBridge.perform(
      #selector(BrazeReactBridge.initBraze(_:)),
      with: configuration
    ).takeUnretainedValue() as! Braze

    AppDelegate.braze = braze

    /* Other configuration */

    return true
}

// MARK: - AppDelegate.braze

static var braze: Braze? = nil
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

Importa el SDK de Braze en la parte superior del archivo `AppDelegate.m`:
```objc
#import <BrazeKit/BrazeKit-Swift.h>
#import "BrazeReactBridge.h"
```

En el método `application:didFinishLaunchingWithOptions:`, sustituye la [clave de]({{site.baseurl}}/api/identifier_types/) API y el [punto final]({{site.baseurl}}/api/basics/#endpoints) por los valores de tu aplicación. A continuación, crea la instancia de Braze utilizando la configuración, y crea una propiedad estática en la dirección `AppDelegate` para facilitar el acceso:

{% alert note %}
Nuestro ejemplo supone una implementación de [RCTAppDelegate](https://github.com/facebook/react-native/blob/e64756ae5bb5c0607a4d97a134620fafcb132b3b/packages/react-native/Libraries/AppDelegate/RCTAppDelegate.h), que proporciona una serie de abstracciones en la configuración de React Native. Si utilizas una configuración diferente para tu aplicación, asegúrate de ajustar tu implementación según sea necesario.
{% endalert %}

```objc
- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Setup Braze
  BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"{BRAZE_API_KEY}"
                                                                    endpoint:@"{BRAZE_ENDPOINT}"];
  // Enable logging and customize the configuration here.
  configuration.logger.level = BRZLoggerLevelInfo;
  Braze *braze = [BrazeReactBridge initBraze:configuration];
  AppDelegate.braze = braze;

  /* Other configuration */

  return YES;
}

#pragma mark - AppDelegate.braze

static Braze *_braze = nil;

+ (Braze *)braze {
  return _braze;
}

+ (void)setBraze:(Braze *)braze {
  _braze = braze;
}
```

{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% endtabs %}

## Paso 3: Uso

Una vez instalada, puedes `import` la biblioteca en tu código de React Native:

```javascript
import Braze from "@braze/react-native-sdk";
```

Consulta nuestro [proyecto de ejemplo](https://github.com/braze-inc/braze-react-native-sdk/tree/master/BrazeProject) para más detalles.

## Prueba tu integración básica

En este punto, puedes verificar que el SDK está integrado comprobando las estadísticas de sesión en el panel. Si ejecutas tu aplicación en cualquiera de las dos plataformas, deberías ver una nueva sesión en el panel (en la sección **Resumen** ).

Puedes iniciar una sesión para un usuario concreto llamando al código siguiente en tu aplicación.

```javascript
Braze.changeUser("userId");
```

Por ejemplo, puedes asignar el ID de usuario al iniciar la aplicación:

```javascript
import React, { useEffect } from "react";
import Braze from "@braze/react-native-sdk";

const App = () => {
  useEffect(() => {
    Braze.changeUser("some-user-id");
  }, []);

  return (
    <div>
      ...
    </div>
  )
```

A continuación, puedes buscar al usuario con `some-user-id` en el panel, en [Búsqueda de usuarios]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search#using-user-search). Allí podrás comprobar que se han registrado los datos de sesión y de dispositivo.


