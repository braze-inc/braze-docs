---
nav_title: Completar la integración
article_title: Completar la integración de SDK Swift
platform: Swift
description: "Este artículo de referencia muestra cómo terminar de integrar el SDK de Braze Swift después de instalarlo mediante una de las opciones de integración."
page_order: 2

---

# Completar la integración

> Antes de seguir estos pasos, asegúrate de haber integrado el SDK de Swift para iOS mediante [Swift Package Manager]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/swift_package_manager/) o [CocoaPods]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/cocoapods/).

## Actualiza el delegado de tu aplicación

{% tabs %}
{% tab swift %}

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

{% endtab %}
{% tab OBJETIVO-C %}

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

{% endtab %}
{% endtabs %}


## Integración de SDK completa

En este punto, tu integración básica debería estar completa. Ahora Braze debería estar recopilando datos de tu aplicación. Sigue los demás artículos de esta guía de integración para implementar y personalizar toda la gama de características y canales de mensajería de Braze.

## Recursos adicionales

Nuestra [documentación de referencia del SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/ "-documentación completade clases de iOS-") proporciona información adicional y orientación sobre cada símbolo del SDK.

