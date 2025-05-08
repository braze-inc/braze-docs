---
nav_title: Configuración inicial del SDK
article_title: Configuración inicial del SDK para Flutter
platform: Flutter
page_order: 1
description: "Esta referencia presenta el SDK de Flutter y explica cómo integrarlo de forma nativa en Android e iOS."
search_rank: 1
---

# Configuración inicial del SDK

> En este artículo de referencia se explica cómo instalar el SDK de Braze para Flutter. Sigue estas instrucciones para instalar el [SDK de Flutter de Braze](https://pub.dev/packages/braze_plugin), que contiene un paquete que permite a los integradores utilizar las API de Braze en [aplicaciones de Flutter](https://flutter.dev/) escritas en Dart.

Este complemento proporciona una funcionalidad básica de análisis y te permite integrar mensajes dentro de la aplicación y tarjetas de contenido tanto para iOS como para Android con una única base de código.

{% alert note %}
Tendrás que completar los pasos de instalación en ambas plataformas por separado.
{% endalert %}

## Requisitos previos

Para completar la instalación, necesitarás la [clave de API del identificador de la aplicación]({{site.baseurl}}/api/identifier_types/), así como el [punto final de SDK]({{site.baseurl}}/api/basics/#endpoints). Ambos se encuentran en el panel en **Administrar configuración**.

Antes de seguir estos pasos, instala y configura el [SDK de Flutter](https://docs.flutter.dev/get-started/install). Asegúrate de que tu máquina y tu proyecto ejecutan las versiones mínimas necesarias de Flutter y Dart [que se indican aquí](https://github.com/braze-inc/braze-flutter-sdk#readme).

## Paso 1: Integrar la biblioteca Braze

Añade el paquete SDK Flutter de Braze desde la línea de comandos.

```bash
flutter pub add braze_plugin
```

Esto añadirá la línea apropiada a tu `pubspec.yaml`.

## Paso 2: Configuración nativa completa

{% tabs %}
{% tab Android %}

Para conectarte a los servidores de Braze, crea un archivo `braze.xml` en la carpeta `android/res/values` de tu proyecto. Pega el siguiente código y sustituye la clave de identificador de API y el punto final por tus valores:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
<string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

Añade los permisos necesarios a tu archivo `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% endtab %}
{% tab iOS %}
{% subtabs global %}
{% subtab SWIFT %}
Añade la importación del SDK de Braze en la parte superior del archivo `AppDelegate.swift`:
```swift
import BrazeKit
import braze_plugin
```

En el mismo archivo, crea el objeto de configuración Braze en el método `application(_:didFinishLaunchingWithOptions:)` y sustituye la clave de API y el punto final por los valores de tu aplicación. A continuación, crea la instancia de Braze utilizando la configuración, y crea una propiedad estática en la dirección `AppDelegate` para facilitar el acceso:

```swift
static var braze: Braze? = nil

func application(
  _ application: UIApplication,
  didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil
) -> Bool {
  // Setup Braze
  let configuration = Braze.Configuration(
    apiKey: "<BRAZE_API_KEY>",
    endpoint: "<BRAZE_ENDPOINT>"
  )
  // - Enable logging or customize configuration here
  configuration.logger.level = .info
  let braze = BrazePlugin.initBraze(configuration)
  AppDelegate.braze = braze

  return true
}
```
{% endsubtab %}
{% subtab OBJECTIVE-C %}
Importa `BrazeKit` en la parte superior del archivo `AppDelegate.m`:
```objc
@import BrazeKit;
```

En el mismo archivo, crea el objeto de configuración Braze en el método `application:didFinishLaunchingWithOptions:` y sustituye la clave de API y el punto final por los valores de tu aplicación. A continuación, crea la instancia de Braze utilizando la configuración, y crea una propiedad estática en la dirección `AppDelegate` para facilitar el acceso:

```objc
- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Setup Braze
  BRZConfiguration *configuration =
      [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
                                      endpoint:@"<BRAZE_ENDPOINT>"];
  // - Enable logging or customize configuration here
  configuration.logger.level = BRZLoggerLevelInfo;
  Braze *braze = [BrazePlugin initBraze:configuration];
  AppDelegate.braze = braze;

  [self.window makeKeyAndVisible];
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

Para importar el plugin en tu código Dart, utiliza lo siguiente:

```dart
import 'package:braze_plugin/braze_plugin.dart';
```

A continuación, inicializa una instancia del complemento Braze llamando a `new BrazePlugin()` como en [nuestra aplicación de ejemplo](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart).

## Prueba tu integración básica

En este punto, puedes verificar que el SDK está integrado comprobando las estadísticas de sesión en el panel. Si ejecutas tu aplicación en cualquiera de las dos plataformas, deberías ver una nueva sesión en el panel (en la sección **Resumen** ).

Puedes abrir una sesión para un usuario concreto llamando al código siguiente en tu aplicación.

```dart
BrazePlugin braze = BrazePlugin();
braze.changeUser("{some-user-id}");
```

A continuación, busca al usuario con `{some-user-id}` en el panel, en **Audiencia** > **Buscar usuarios**. Allí podrás comprobar que se han registrado los datos de sesión y de dispositivo.

{% alert note %}
Si utilizas la [navegación antigua]({{site.baseurl}}/navigation), puedes buscar usuarios desde **Usuarios** > **Búsqueda de usuarios**.
{% endalert %}

