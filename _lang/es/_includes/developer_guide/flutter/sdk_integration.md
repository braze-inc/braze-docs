## Acerca del SDK de Flutter Braze

Después de integrar el SDK Braze Flutter en Android e iOS, podrás utilizar la API Braze en tus [aplicaciones Flutter](https://flutter.dev/) escritas en Dart. Este complemento proporciona una funcionalidad básica de análisis y te permite integrar mensajes dentro de la aplicación y tarjetas de contenido tanto para iOS como para Android con una única base de código.

## Integración del SDK de Flutter

### Requisitos previos

Antes de integrar el SDK de Braze Flutter, tendrás que completar lo siguiente:

| Requisito previo | Descripción |
| --- | --- |
| Identificador de la aplicación API Braze | Para localizar el identificador de tu aplicación, ve a **Configuración** > **API e identificadores** > Identificadores de aplicación. Para más información, consulta [Tipos de identificadores API]({{site.baseurl}}/api/identifier_types/#app-identifier).|
| Punto final REST Braze | La URL de su punto final REST. Tu punto final dependerá de la [URL Braze de tu instancia]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints).|
| SDK de Flutter | Instala el [SDK](https://docs.flutter.dev/get-started/install) oficial [de Flutter](https://docs.flutter.dev/get-started/install) y asegúrate de que cumple la [versión mínima admitida](https://github.com/braze-inc/braze-flutter-sdk#requirements) del SDK de Flutter de Braze. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Paso 1: Integrar la biblioteca Braze

Añade el paquete SDK Flutter de Braze desde la línea de comandos. Esto añadirá la línea apropiada a tu `pubspec.yaml`.

```bash
flutter pub add braze_plugin
```

### Paso 2: Configuración completa del SDK nativo

{% tabs %}
{% tab Android %}

Para conectarte a los servidores de Braze, crea un archivo `braze.xml` en la carpeta `android/res/values` de tu proyecto. Pega el siguiente código y sustituye la clave de identificador de API y el punto final por tus valores:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
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

### Paso 3: Configurar el plugin

Para importar el plugin en tu código Dart, utiliza lo siguiente:

```dart
import 'package:braze_plugin/braze_plugin.dart';
```

A continuación, inicializa una instancia del complemento Braze llamando a `new BrazePlugin()` como en [nuestra aplicación de ejemplo](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart).

{% alert important %}
Para evitar comportamientos indefinidos, sólo asigna y utiliza una única instancia de `BrazePlugin` en tu código Dart.
{% endalert %}

## Probar la integración

Puedes verificar que el SDK está integrado comprobando las estadísticas de sesión en el panel. Si ejecutas tu aplicación en cualquiera de las dos plataformas, deberías ver una nueva sesión en el panel (en la sección **Resumen** ).

Abre una sesión para un usuario concreto llamando al código siguiente en tu aplicación.

```dart
BrazePlugin braze = BrazePlugin();
braze.changeUser("{some-user-id}");
```

Busca al usuario con `{some-user-id}` en el panel, en **Audiencia** > **Buscar usuarios**. Allí podrás comprobar que se han registrado los datos de sesión y de dispositivo.

