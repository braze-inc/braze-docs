## Integración del SDK Swift

Puedes integrar y personalizar el SDK Braze Swift utilizando el Swift Package Manager (SPM), CocoaPods o métodos de integración manual. Para más información sobre los distintos símbolos del SDK, consulta [la documentación de referencia de Braze Swift](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/).

### Requisitos previos

Antes de empezar, comprueba que tu entorno es compatible con la [última versión del SDK de Braze Swift](https://github.com/braze-inc/braze-swift-sdk#version-information).

### Paso 1: Instalar el SDK Swift de Braze

Te recomendamos que utilices [Swift Package Manager (SwiftPM)](https://swift.org/package-manager/) o [CocoaPods](http://cocoapods.org/) para instalar el SDK Braze Swift. También puedes instalar el SDK manualmente.

{% tabs local %}
{% tab Swift Package Manager %}
#### Paso 1.1: Importar versión del SDK

Abre tu proyecto y ve a la configuración del mismo. Selecciona la pestaña **Paquetes Swift** y haz clic en el botón <i class="fas fa-plus"></i> añadir debajo de la lista de paquetes.

![]({% image_buster /assets/img/swiftpackages.png %})

{% alert note %}
A partir de la versión 7.4.0, el SDK Swift de Braze tiene canales de distribución adicionales como [XCFrameworks estáticos](https://github.com/braze-inc/braze-swift-sdk-prebuilt-static) y [XCFrameworks dinámicos](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic). Si quieres utilizar cualquiera de estos formatos en su lugar, sigue las instrucciones de instalación de su repositorio respectivo.
{% endalert %}

Introduce la URL de nuestro repositorio del SDK Swift para iOS `https://github.com/braze-inc/braze-swift-sdk` en el campo de texto. En la sección **Regla de dependencia**, selecciona la versión del SDK. Por último, haz clic en **Añadir paquete**.

![]({% image_buster /assets/img/importsdk_example.png %})

#### Paso 1.2: Selecciona tus paquetes

El SDK de Swift de Braze separa las características en bibliotecas independientes para proporcionar a los desarrolladores un mayor control sobre qué características importar a sus proyectos.

| Paquete         | Detalles                                                                                                                                                         |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `BrazeKit`      | Biblioteca principal del SDK que proporciona soporte para análisis y notificaciones push.                                                                                        |
| `BrazeLocation` | Biblioteca de ubicación que proporciona soporte para el análisis de la ubicación y la supervisión del geovallado.                                                                              |
| `BrazeUI`       | Biblioteca de interfaz de usuario proporcionada por Braze para mensajes dentro de la aplicación, tarjetas de contenido y pancartas. Importa esta biblioteca si quieres utilizar los componentes predeterminados de la interfaz de usuario. |

{: .ws-td-nw-1}

##### Acerca de las bibliotecas de extensión

{% alert warning %}
[BrazeNotificationService](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications) y [BrazePushStory](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories) son módulos de extensión que proporcionan funcionalidad adicional y no deben añadirse directamente al objetivo principal de tu aplicación. En su lugar, sigue las guías enlazadas para integrarlos por separado en sus respectivas extensiones de destino.
{% endalert %}

| Paquete                    | Detalles                                                                               |
| -------------------------- | ------------------------------------------------------------------------------------- |
| `BrazeNotificationService` | Biblioteca de extensión de servicios de notificación que proporciona soporte para notificaciones push enriquecidas. |
| `BrazePushStory`           | Biblioteca de extensión de contenido de notificaciones que ofrece soporte para historias push.            |

{: .ws-td-nw-1}

Selecciona el paquete que mejor se adapte a tus necesidades y haz clic en **Añadir paquete**. Asegúrate de seleccionar `BrazeKit` como mínimo.

![]({% image_buster /assets/img/add_package.png %})
{% endtab %}

{% tab CocoaPods %}
#### Paso 1.1: Instalar CocoaPods

Para una guía completa, consulta la [Guía de inicio de](https://guides.cocoapods.org/using/getting-started.html) CocoaPods. Si no, puedes ejecutar el siguiente comando para empezar rápidamente:

```bash
$ sudo gem install cocoapods
```

Si te quedas atascado, consulta la Guía de solución de problemas de CocoaPods.

#### Paso 1.2: Construir el archivo de bibliotecas

A continuación, crea un archivo en el directorio de tu proyecto Xcode llamado `Podfile`.

{% alert note %}
A partir de la versión 7.4.0, el SDK Swift de Braze tiene canales de distribución adicionales como [XCFrameworks estáticos](https://github.com/braze-inc/braze-swift-sdk-prebuilt-static) y [XCFrameworks dinámicos](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic). Si quieres utilizar cualquiera de estos formatos en su lugar, sigue las instrucciones de instalación de su repositorio respectivo.
{% endalert %}

Añade la siguiente línea a tu archivo de bibliotecas:

```
target 'YourAppTarget' do
  pod 'BrazeKit'
end
```

`BrazeKit` contiene la biblioteca principal del SDK, que proporciona soporte para análisis y notificaciones push.

Te sugerimos que versiones Braze para que las actualizaciones de vainas cojan automáticamente cualquier cosa menor que una actualización de versión menor. Esto parece `pod 'BrazeKit' ~> Major.Minor.Build`. Si quieres integrar automáticamente la última versión del SDK de Braze, incluso con cambios importantes, puedes utilizar `pod 'BrazeKit'` en tu archivo de bibliotecas.

##### Sobre bibliotecas adicionales

El SDK de Swift de Braze separa las características en bibliotecas independientes para proporcionar a los desarrolladores un mayor control sobre qué características importar a sus proyectos. Además de `BrazeKit`, puedes añadir las siguientes bibliotecas a tu archivo de bibliotecas:

| Biblioteca               | Detalles                                                                                                                                                         |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `pod 'BrazeLocation'` | Biblioteca de ubicación que proporciona soporte para el análisis de la ubicación y la supervisión del geovallado.                                                                              |
| `pod 'BrazeUI'`       | Biblioteca de interfaz de usuario proporcionada por Braze para mensajes dentro de la aplicación, tarjetas de contenido y pancartas. Importa esta biblioteca si quieres utilizar los componentes predeterminados de la interfaz de usuario. |

{: .ws-td-nw-1}

###### Bibliotecas de extensión

[BrazeNotificationService](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications) y [BrazePushStory](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories) son módulos de extensión que proporcionan funcionalidad adicional y no deben añadirse directamente al objetivo principal de tu aplicación. En su lugar, tendrás que crear objetivos de extensión independientes para cada uno de estos módulos e importar los módulos Braze en sus objetivos correspondientes.

| Biblioteca                          | Detalles                                                                               |
| -------------------------------- | ------------------------------------------------------------------------------------- |
| `pod 'BrazeNotificationService'` | Biblioteca de extensión de servicios de notificación que proporciona soporte para notificaciones push enriquecidas. |
| `pod 'BrazePushStory'`           | Biblioteca de extensión de contenido de notificaciones que ofrece soporte para historias push.            |

{: .ws-td-nw-1}

#### Paso 1.3: Instalar el SDK

Para instalar el SDK de Braze CocoaPod, navega hasta el directorio del proyecto de tu aplicación en Xcode dentro de tu terminal y ejecuta el siguiente comando:
```
pod install
```

En este punto, deberías poder abrir el nuevo espacio de trabajo del proyecto Xcode creado por CocoaPods. Asegúrate de utilizar este espacio de trabajo de Xcode en lugar de tu proyecto de Xcode.

![Una carpeta de Ejemplo de Braze ampliada para mostrar el nuevo `BrazeExample.workspace`.]({% image_buster /assets/img/braze_example_workspace.png %})

#### Actualizar el SDK con CocoaPods

Para actualizar un CocoaPod, simplemente ejecuta el siguiente comando dentro del directorio de tu proyecto:

```
pod update
```
{% endtab %}

{% tab Manual %}
#### Paso 1.1: Descargar el SDK de Braze

Ve a [la página de lanzamiento del SDK de Braze en GitHub](https://github.com/braze-inc/braze-swift-sdk/releases) y descarga `braze-swift-sdk-prebuilt.zip`.

!["La página de lanzamiento del SDK de Braze en GitHub"]({% image_buster /assets/img/swift/sdk_integration/download-braze-swift-sdk-prebuilt.png %})

#### Paso 1.2: Elige tus marcos

El SDK Swift de Braze contiene diversos XCFrameworks independientes, lo que te da libertad para integrar las características que desees, sin necesidad de integrarlos todos. Consulta la tabla siguiente para elegir tus XCFrameworks:

| Paquete                    | ¿Es necesario? | Descripción                                                                                                                                                                                                                                                                                                                          |
| -------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `BrazeKit`                 | Sí       | Biblioteca principal del SDK que proporciona soporte para análisis y notificaciones push.                                                                                                                                                                                                                                                         |
| `BrazeLocation`            | No        | Biblioteca de ubicación que proporciona soporte para análisis de ubicación y control de geovallas.                                                                                                                                                                                                                                               |
| `BrazeUI`                  | No        | Biblioteca de interfaz de usuario proporcionada por Braze para mensajes dentro de la aplicación, tarjetas de contenido y pancartas. Importa esta biblioteca si quieres utilizar los componentes predeterminados de la interfaz de usuario.                                                                                                                                                                      |
| `BrazeNotificationService` | No        | Biblioteca de extensión del servicio de notificaciones que proporciona soporte para notificaciones push enriquecidas. No añadas esta biblioteca directamente al objetivo principal de tu aplicación, [añade en su lugar la biblioteca `BrazeNotificationService` por separado](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications).                 |
| `BrazePushStory`           | No        | Biblioteca de extensión de contenido de notificaciones que proporciona soporte para historias push. No añadas esta biblioteca directamente al objetivo principal de tu aplicación, [añade en su lugar la biblioteca `BrazePushStory` por separado](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories).                                                 |
| `BrazeKitCompat`           | No        | Biblioteca de compatibilidad que contiene todas las clases y métodos de `Appboy` y `ABK*` que estaban disponibles en la versión 4 de `Appboy-iOS-SDK`.X.X. Para conocer los detalles de uso, consulta el escenario de migración mínima en la [guía de migración](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/).            |
| `BrazeUICompat`            | No        | Biblioteca de compatibilidad que contiene todas las clases y métodos de `ABK*` que estaban disponibles en la biblioteca `AppboyUI` a partir de la versión 4 de `Appboy-iOS-SDK`.X.X. Para conocer los detalles de uso, consulta el escenario de migración mínima en la [guía de migración](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/). |
| `SDWebImage`               | No        | Dependencia utilizada sólo por `BrazeUICompat` en el escenario de migración mínima.                                                                                                                                                                                                                                                           |

{: .ws-td-nw-1 .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Paso 1.3: Prepara tus archivos

Decide si quieres utilizar XCFrameworks **estáticos** o **dinámicos**, y luego prepara tus archivos:

1. Crea un directorio temporal para tus XCFrameworks.
2. En `braze-swift-sdk-prebuilt`, abre el directorio `dynamic` y mueve `BrazeKit.xcframework` a tu directorio. Tu directorio debe ser similar al siguiente
    ```bash
    temp_dir
    └── BrazeKit.xcframework
    ```
3. Mueve cada uno de los [XCFrameworks que hayas elegido](#swift_step-2-choose-your-frameworks) a tu directorio temporal. Tu directorio debe ser similar al siguiente
    ```bash
    temp_dir
    ├── BrazeKit.xcframework
    ├── BrazeKitCompat.xcframework
    ├── BrazeLocation.xcframework
    └── SDWebImage.xcframework
    ```

#### Paso 1.4: Integra tus marcos de trabajo

A continuación, integra los XCFrameworks **dinámicos** o **estáticos** que [preparaste anteriormente](#swift_step-3-prepare-your-files):

En tu proyecto Xcode, selecciona tu objetivo de compilación y, a continuación, **General**. En **Frameworks, Bibliotecas y Contenido incrustado**, arrastra y suelta los [archivos que preparaste anteriormente](#swift_step-3-prepare-your-files).

!["Un proyecto Xcode de ejemplo con cada biblioteca Braze configurada como 'Incrustar y firmar'"]({% image_buster /assets/img/swift/sdk_integration/embed-and-sign.png %})

{% alert note %}
A partir del SDK de Swift 12.0.0, debes seleccionar siempre **Incrustar y firmar** para los XCFrameworks de Braze, tanto para las variantes estáticas como para las dinámicas. Esto garantiza que los recursos de los frameworks se incrusten correctamente en el paquete de tu aplicación.
{% endalert %}

{% alert tip %}
Para habilitar la compatibilidad con GIF, añade `SDWebImage.xcframework`, situado en `braze-swift-sdk-prebuilt/static` o `braze-swift-sdk-prebuilt/dynamic`.
{% endalert %}

#### Errores comunes de los proyectos Objective-C

Si tu proyecto Xcode sólo contiene archivos Objective-C, es posible que aparezcan errores de "símbolo ausente" cuando intentes compilar tu proyecto. Para solucionar estos errores, abre tu proyecto y añade un archivo Swift vacío a tu árbol de archivos. Esto forzará a tu cadena de herramientas de compilación a incrustar [Swift Runtime](https://support.apple.com/kb/dl1998) y enlazar con los frameworks apropiados durante el tiempo de compilación.

```bash
FILE_NAME.swift
```

Sustituye `FILE_NAME` por cualquier cadena no espaciada. Tu archivo debe tener un aspecto similar al siguiente

```bash
empty_swift_file.swift
```
{% endtab %}
{% endtabs local %}

### Paso 2: Configurar la inicialización retardada (opcional)

Puedes elegir retrasar la inicialización del SDK de Braze Swift, lo que resulta útil si tu aplicación necesita cargar la configuración o esperar el consentimiento del usuario antes de iniciar el SDK. La inicialización retardada garantiza que las notificaciones push de Braze se pongan en cola hasta que el SDK esté listo.

Para habilitarlo, llama a `Braze.prepareForDelayedInitialization()` lo antes posible -idealmente dentro o antes de tu `application(_:didFinishLaunchingWithOptions:)`.

{% alert note %}
Esto sólo se aplica a las notificaciones push de Braze. Otras notificaciones push son gestionadas normalmente por los delegados del sistema.
{% endalert %}

{% tabs %}
{% tab Swift %}
{% subtabs local %}
{% subtab UIKit %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
  // Prepare the SDK for delayed initialization
  Braze.prepareForDelayedInitialization()

  // ... Additional non-Braze setup code

  return true
}
```
{% endsubtab %}

{% subtab SwiftUI %}
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
{% endsubtab %}
{% endsubtabs %}
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
[`Braze.prepareForDelayedInitialization(pushAutomation:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/preparefordelayedinitialization(pushautomation:)) acepta un parámetro opcional `pushAutomation`. Si se establece en `nil`, se habilitan todas las características de automatización push, excepto la solicitud de autorización push en el lanzamiento.
{% endalert %}

### Paso 3: Actualiza el delegado de tu aplicación

{% alert important %}
Lo siguiente supone que ya has añadido un `AppDelegate` a tu proyecto (que no se generan por predeterminado). Si no piensas utilizarlo, asegúrate de inicializar el SDK de Braze lo antes posible, por ejemplo, durante el lanzamiento de la aplicación.
{% endalert %}

{% subtabs local %}
{% subtab swift %}
Añade la siguiente línea de código a tu archivo `AppDelegate.swift` para importar las características incluidas en el SDK de Swift de Braze:

```swift
import BrazeKit
```

A continuación, añade una propiedad estática a tu clase `AppDelegate` para mantener una referencia fuerte a la instancia de Braze durante toda la vida de tu aplicación:

```swift
class AppDelegate: UIResponder, UIApplicationDelegate {
  static var braze: Braze? = nil
}
```

Por último, en `AppDelegate.swift`, añade el siguiente fragmento de código a tu método `application:didFinishLaunchingWithOptions:`:

```swift
let configuration = Braze.Configuration(
    apiKey: "YOUR-APP-IDENTIFIER-API-KEY",
    endpoint: "YOUR-BRAZE-ENDPOINT"
)
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```

Actualiza `YOUR-APP-IDENTIFIER-API-KEY` y `YOUR-BRAZE-ENDPOINT` con el valor correcto desde la página de **configuración de tu aplicación**. Consulta nuestros [tipos de identificadores de API]({{site.baseurl}}/api/identifier_types/?tab=app%20ids) para obtener más información sobre dónde encontrar la clave de API de tu identificador de aplicación.

{% endsubtab %}
{% subtab OBJECTIVE-C %}

Añade la siguiente línea de código a tu archivo `AppDelegate.m`:

```objc
@import BrazeKit;
```

A continuación, añade una variable estática a tu archivo `AppDelegate.m` para mantener una referencia a la instancia de Braze durante toda la vida de tu aplicación:

```objc
static Braze *_braze;

@implementation AppDelegate
+ (Braze *)braze {
  return _braze;
}

+ (void)setBraze:(Braze *)braze {
  _braze = braze;
}
@end
```

Por último, dentro de tu archivo `AppDelegate.m`, añade el siguiente fragmento de código dentro de tu método `application:didFinishLaunchingWithOptions:`:

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:"YOUR-APP-IDENTIFIER-API-KEY"
                                                                  endpoint:"YOUR-BRAZE-ENDPOINT"];
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

Actualiza `YOUR-APP-IDENTIFIER-API-KEY` y `YOUR-BRAZE-ENDPOINT` con el valor correcto desde tu página **Administrar configuración**. Consulta nuestra [documentación sobre la API]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key) para obtener más información sobre dónde encontrar la clave de API del identificador de tu aplicación.

{% endsubtab %}
{% endsubtabs local %}

## Configuraciones opcionales

### Registro

#### Niveles de registro

El nivel de registro predeterminado para el SDK de Braze Swift es `.error`-también es el nivel mínimo habilitado cuando se habilitan los registros-. Esta es la lista completa de niveles de registro:

| Swift       | Objective-C              | Descripción                                                  |
| ----------- | ------------------------ | ------------------------------------------------------------ |
| `.debug`    | `BRZLoggerLevelDebug`    | (predeterminado) Registrar información de depuración + `.info` + `.error`.    |
| `.info`     | `BRZLoggerLevelInfo`     | Registra la información general del SDK (cambios de usuario, etc.) + `.error`. |
| `.error`    | `BRZLoggerLevelError`    | Errores de registro.                                                  |
| `.disabled` | `BRZLoggerLevelDisabled` | No se produce ningún registro.                                           |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Configuración del nivel de registro

Puedes asignar el nivel de registro en tiempo de ejecución en tu objeto `Braze.Configuration`. Para más detalles sobre su uso, consulta [`Braze.Configuration.Logger`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/logger-swift.class).

{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)
// Enable logging of general SDK information (such as user changes, etc.)
configuration.logger.level = .info
let braze = Braze(configuration: configuration)
```

{% endtab %}
{% tab OBJETIVO-C %}

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:self.APIKey
                                                                  endpoint:self.apiEndpoint];
// Enable logging of general SDK information (such as user changes, etc.)
[configuration.logger setLevel:BRZLoggerLevelInfo];
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
```

{% endtab %}
{% endtabs %}
