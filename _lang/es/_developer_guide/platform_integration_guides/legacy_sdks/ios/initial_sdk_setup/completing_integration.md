---
nav_title: Completar la integración
article_title: Completar la integración de SDK de iOS
platform: iOS
description: "Este artículo de referencia muestra cómo terminar de integrar el SDK de Braze después de instalarlo mediante una de las opciones de integración."
page_order: 2

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Completar la integración

Antes de seguir estos pasos, asegúrate de haber integrado el SDK mediante [Carthage]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/carthage_integration/), [CocoaPods]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/cocoapods/), [Swift Package Manager]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/swift_package_manager/) o una integración [manual]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/manual_integration_options/).

## Paso 1: Actualiza el delegado de tu aplicación

{% tabs %}
{% tab OBJETIVO-C %}

Si estás integrando el SDK de Braze con CocoaPods, Carthage o con una [integración manual dinámica]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/manual_integration_options/), añade la siguiente línea de código a tu archivo `AppDelegate.m`:

```objc
#import "Appboy-iOS-SDK/AppboyKit.h"
```

Si estás integrando con Swift Package Manager o con una [integración manual estática]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/manual_integration_options/), utiliza esta línea en su lugar:

```objc
#import "AppboyKit.h"
```

A continuación, dentro de tu archivo `AppDelegate.m`, añade el siguiente fragmento de código dentro de tu método `application:didFinishLaunchingWithOptions:`:

```objc
[Appboy startWithApiKey:@"YOUR-APP-IDENTIFIER-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions];
```

Actualiza `YOUR-APP-IDENTIFIER-API-KEY` con el valor correcto desde tu página **Administrar configuración**. Consulta nuestra [documentación sobre la API]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key) para obtener más información sobre dónde encontrar la clave de API del identificador de tu aplicación.

{% endtab %}
{% tab swift %}

Si estás integrando el SDK de Braze con CocoaPods, Carthage o con una [integración manual dinámica]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/manual_integration_options/), añade la siguiente línea de código a tu archivo `AppDelegate.swift`:

```swift
import Appboy_iOS_SDK
```

Si estás integrando con Swift Package Manager o con una [integración manual estática]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/manual_integration_options/), utiliza esta línea en su lugar:

```swift
import AppboyKit
```
Consulta [la documentación para desarrolladores de Apple](https://developer.apple.com/library/ios/documentation/swift/conceptual/buildingcocoaapps/MixandMatch.html) para obtener más información sobre el uso de código Objective-C en proyectos Swift.

A continuación, en `AppDelegate.swift`, añade el siguiente fragmento de código a tu `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool`:

```swift
Appboy.start(withApiKey: "YOUR-APP-IDENTIFIER-API-KEY", in:application, withLaunchOptions:launchOptions)
```

Actualiza `YOUR-APP-IDENTIFIER-API-KEY` con el valor correcto desde tu página **Administrar configuración**. Consulta nuestra [documentación sobre la API]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key) para obtener más información sobre dónde encontrar la clave de API del identificador de tu aplicación.

{% endtab %}
{% endtabs %}

{% alert note %}
El singleton `sharedInstance` será nulo antes de llamar a `startWithApiKey:`, ya que es un requisito previo para utilizar cualquier función de Braze.
{% endalert %}

{% alert warning %}
Asegúrate de inicializar Braze en el hilo principal de tu aplicación. Inicializar de forma asíncrona puede provocar fallos en la funcionalidad.
{% endalert %}


## Paso 2: Especifica tu clúster de datos

{% alert note %}
Ten en cuenta que, a partir de diciembre de 2019, ya no se proporcionarán puntos finales personalizados. Si tienes un punto final personalizado preexistente, puedes seguir utilizándolo. Para más detalles, consulta nuestra <a href="{{site.baseurl}}/api/basics/#endpoints">lista de puntos finales disponibles</a>.
{% endalert %}

### Configuración del punto final en tiempo de compilación (recomendado)

Si se te da un punto final personalizado preexistente:
- A partir de la versión 3.0.2 del SDK iOS de Braze, puedes establecer un punto final personalizado utilizando el archivo `Info.plist`. Añade el diccionario `Braze` a tu archivo `Info.plist`. Dentro del diccionario `Braze`, añade la subentrada de cadena `Endpoint` y establece el valor en la autoridad de la URL de tu punto final personalizado (por ejemplo, `sdk.iad-01.braze.com`, no `https://sdk.iad-01.braze.com`). Ten en cuenta que antes de la versión 4.0.2 del SDK iOS de Braze, se debe utilizar la clave de diccionario `Appboy` en lugar de `Braze`.

Tu representante de Braze ya debería haberte indicado el [punto final correcto]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/).

### Configuración del punto final en tiempo de ejecución

Si se te da un punto final personalizado preexistente:
- A partir de la versión 3.17.0 del SDK iOS de Braze, puedes anular la configuración de tu punto final a través de `ABKEndpointKey` dentro del parámetro `appboyOptions` pasado a `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`. Establece el valor de la autoridad de la URL de tu punto final personalizado (por ejemplo, `sdk.iad-01.braze.com`, no `https://sdk.iad-01.braze.com`).

## Integración de SDK completa

Ahora Braze debería estar recopilando datos de tu aplicación, y tu integración básica debería estar completa. Consulta los artículos siguientes para habilitar [el seguimiento de eventos personalizado]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/), la [mensajería push]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/) y la línea completa de características de Braze.

## Personalizar Braze al iniciarse

Si deseas personalizar Braze al iniciarse, puedes utilizar en su lugar el método de inicialización de Braze `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:` y pasar un `NSDictionary` opcional de claves de inicio de Braze.
{% tabs %}
{% tab OBJETIVO-C %}

En tu archivo `AppDelegate.m`, dentro de tu método `application:didFinishLaunchingWithOptions:`, añade el siguiente método Braze:

```objc
[Appboy startWithApiKey:@"YOUR-APP-IDENTIFER-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

Nota que este método sustituiría al método de inicialización `startWithApiKey:inApplication:withLaunchOptions:`.

{% endtab %}
{% tab swift %}

En `AppDelegate.swift`, dentro de tu método `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool`, añade el siguiente método Braze donde `appboyOptions` es un `Dictionary` de valores de configuración de inicio:

```swift
Appboy.start(withApiKey: "YOUR-APP-IDENTIFIER-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:appboyOptions)
```

Nota que este método sustituiría al método de inicialización `startWithApiKey:inApplication:withLaunchOptions:`.

{% endtab %}
{% endtabs %}

Este método se llama con los siguientes parámetros:

- `YOUR-APP-IDENTIFIER-API-KEY` - Tu clave de API [identificadora de la aplicación]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key) desde el panel de Braze.
- `application` - La aplicación actual.
- `launchOptions` - Las opciones `NSDictionary` que obtienes de `application:didFinishLaunchingWithOptions:`.
- `appboyOptions` - Un `NSDictionary` opcional con valores de configuración de inicio para Braze.

Consulta [Appboy.h](https://github.com/braze-inc/braze-ios-sdk/blob/master/AppboyKit/include/Appboy.h) para ver una lista de las teclas de inicio de Braze.

## Appboy.sharedInstance() y anulabilidad Swift
A diferencia de la práctica habitual, el singleton `Appboy.sharedInstance()` es opcional. Esto se debe a que `sharedInstance` es `nil` antes de que se llame a `startWithApiKey:`, y hay algunas implementaciones no estándar pero no inválidas en las que se puede utilizar una inicialización retardada.

Si llamas a `startWithApiKey:` en tu delegado `didFinishLaunchingWithOptions:` antes de cualquier acceso a `sharedInstance` de Appboy (la implementación estándar), puedes utilizar el encadenamiento opcional, como `Appboy.sharedInstance()?.changeUser("testUser")`, para evitar comprobaciones engorrosas. Esto tendrá paridad con una implementación de Objective-C que haya asumido un `sharedInstance` no nulo.

## Recursos adicionales

[Documentación completa de las clases de iOS](http://appboy.github.io/appboy-ios-sdk/docs/annotated.html " La documentación completa de las clases de iOS") está disponible para proporcionar orientación adicional sobre cualquier método del SDK.

