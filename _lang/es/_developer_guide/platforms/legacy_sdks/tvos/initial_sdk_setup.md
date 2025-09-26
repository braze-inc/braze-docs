---
nav_title: Configuración inicial del SDK
article_title: Configuración inicial del SDK para tvOS
platform: tvOS
page_order: 0
page_type: reference
description: "Esta página cubre los pasos de configuración inicial para el SDK Braze de tvOS."
search_rank: 1
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Configuración inicial del SDK

> En este artículo de referencia se explica cómo instalar el SDK de Braze para tvOS. La instalación del SDK de Braze te proporcionará una funcionalidad básica de análisis.

{% alert note %}
Nuestro SDK para tvOS admite actualmente la función de análisis. Para añadir una aplicación tvOS en tu panel, abre un [ticket de soporte]({{site.baseurl}}/braze_support/).
{% endalert %}

El SDK Braze de tvOS debe instalarse o actualizarse mediante [CocoaPods](http://cocoapods.org/), un administrador de dependencias para proyectos Objective-C y Swift. CocoaPods proporciona una mayor simplicidad para la integración y la actualización.

## Integración del SDK de tvOS en CocoaPods

### Paso 1: Instalar CocoaPods

La instalación del SDK a través de [los CocoaPods](http://cocoapods.org/) de tvOS automatiza la mayor parte del proceso de instalación por ti. Antes de comenzar este proceso, asegúrate de que utilizas la [versión de Ruby 2.0.0](https://www.ruby-lang.org/en/installation/) o superior.

Ejecuta el siguiente comando para empezar:

```bash
$ sudo gem install cocoapods
```

- Si se te pide que sobrescribas el ejecutable `rake`, consulta [Introducción](http://guides.cocoapods.org/using/getting-started.html) en CocoaPods.org para más detalles.
- Si tienes problemas relacionados con [CocoaPods](http://guides.cocoapods.org/using/troubleshooting.html), consulta la [guía de solución de problemas de CocoaPods](http://guides.cocoapods.org/using/troubleshooting.html).

### Paso 2: Construir el archivo de bibliotecas

Ahora que has instalado la Gema Ruby de CocoaPods, tendrás que crear un archivo en el directorio de tu proyecto de Xcode llamado `Podfile`.

Añade la siguiente línea a tu archivo de bibliotecas:

```
target 'YourAppTarget' do
  pod 'Appboy-tvOS-SDK'
end
```

Te sugerimos que versiones Braze para que las actualizaciones de vainas cojan automáticamente cualquier cosa menor que una actualización de versión menor. Esto parece `pod 'Appboy-tvOS-SDK' ~> Major.Minor.Build`. Si quieres integrar automáticamente la última versión del SDK de Braze, incluso con cambios importantes, puedes utilizar `pod 'Appboy-tvOS-SDK'` en tu archivo de bibliotecas.

### Paso 3: Instalación del SDK de Braze

Para instalar los SDK de Braze CocoaPods, ve al directorio de tu proyecto de aplicación Xcode en tu terminal y ejecuta el siguiente comando:
```
pod install
```

En este punto, deberías poder abrir el nuevo espacio de trabajo del proyecto Xcode creado por CocoaPods. Asegúrate de utilizar este espacio de trabajo de Xcode en lugar de tu proyecto de Xcode. 

![]({% image_buster /assets/img_archive/podsworkspace.png %})

### Paso 4: Actualizar el delegado de tu aplicación

{% tabs %}
{% tab OBJECTIVE-C %}

Añade la siguiente línea de código a tu archivo `AppDelegate.m`:

```objc
#import <AppboyTVOSKit/AppboyKit.h>
```

Dentro de tu archivo `AppDelegate.m`, añade el siguiente fragmento de código dentro de tu método `application:didFinishLaunchingWithOptions`:

```objc
[Appboy startWithApiKey:@"YOUR-API-KEY"
         inApplication:application
     withLaunchOptions:launchOptions];
```

Por último, actualiza `YOUR-API-KEY` con el valor correcto desde tu página **Administrar configuración**.

{% endtab %}
{% tab swift %}

Si estás integrando el SDK de Braze con CocoaPods o Carthage, añade la siguiente línea de código a tu archivo `AppDelegate.swift`:

```swift
import AppboyTVOSKit
```

Para más información sobre el uso de código Objective-C en proyectos Swift, consulta [los documentos para desarrolladores de Apple](https://developer.apple.com/library/ios/documentation/swift/conceptual/buildingcocoaapps/MixandMatch.html).

En `AppDelegate.swift`, añade el siguiente fragmento de código a tu `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool`:

```swift
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions)
```

A continuación, actualiza `YOUR-API-KEY` con el valor correcto desde tu página **Administrar configuración**.

Nuestro singleton `sharedInstance` será nulo antes de llamar a `startWithApiKey:`, ya que es un requisito previo para utilizar cualquier función de Braze.

{% endtab %}
{% endtabs %}

{% alert warning %}
Asegúrate de inicializar Braze en el hilo principal de tu aplicación. Inicializar de forma asíncrona puede provocar fallos en la funcionalidad.
{% endalert %}

### Paso 5: Especifica tu punto final personalizado o clúster de datos

{% alert note %}
A partir de diciembre de 2019, ya no se entregarán puntos finales personalizados; si tienes un punto final personalizado preexistente, puedes seguir utilizándolo. Para más detalles, consulta nuestra <a href="{{site.baseurl}}/api/basics/#endpoints">lista de puntos finales disponibles</a>.
{% endalert %}

Tu representante de Braze ya debería haberte informado del [punto final correcto]({{ site.baseurl }}/user_guide/administrative/access_braze/sdk_endpoints/).

#### Configuración del punto final en tiempo de compilación (recomendado)
Si se te da un punto final personalizado preexistente:
- A partir de la versión 3.0.2 del SDK iOS de Braze, puedes establecer un punto final personalizado utilizando el archivo `Info.plist`. Añade el diccionario `Appboy` a tu archivo Info.plist. Dentro del diccionario `Appboy`, añade la subentrada de cadena `Endpoint` y establece el valor a tu autoridad de URL de punto final personalizada (por ejemplo, `sdk.iad-01.braze.com`, no `https://sdk.iad-01.braze.com`).

#### Configuración del punto final en tiempo de ejecución
Si se le da un punto final personalizado preexistente:
- A partir de la versión 3.17.0 del SDK iOS de Braze, puedes anular la configuración de tu punto final a través de `ABKEndpointKey` dentro del parámetro `appboyOptions` pasado a `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`. Establece el valor a tu autoridad de URL de punto final personalizada (por ejemplo, `sdk.iad-01.braze.com`, no `https://sdk.iad-01.braze.com`).

{% alert note %}
Se ha eliminado el soporte del SDK versión 3.17.0 del iOS de Braze para la configuración de puntos finales en tiempo de ejecución mediante `ABKAppboyEndpointDelegate`. Si ya utilizas `ABKAppboyEndpointDelegate`, nota que en las versiones v3.14.1 a v3.16.0 del SDK de Braze para iOS, cualquier referencia a `dev.appboy.com` en tu método `getApiEndpoint()` debe sustituirse por una referencia a `sdk.iad-01.braze.com`.
{% endalert %}

### Integración de SDK completa

Ahora Braze debería estar recopilando datos de tu aplicación, y tu integración básica debería estar completa. Ten en cuenta que al compilar tu aplicación tvOS y cualquier otra biblioteca de terceros, Bitcode debe estar habilitado.

### Actualizar el SDK de Braze mediante CocoaPods

Para actualizar un CocoaPod, simplemente ejecuta los siguientes comandos dentro del directorio de tu proyecto:

```
pod update
```

## Personalizar Braze al iniciarse

Si deseas personalizar Braze al iniciarse, puedes utilizar en su lugar el método de inicialización de Braze `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions` y pasar un `NSDictionary` opcional de claves de inicio de Braze.
{% tabs %}
{% tab OBJECTIVE-C %}

En tu archivo `AppDelegate.m`, dentro de tu método `application:didFinishLaunchingWithOptions`, añade el siguiente método Braze:

```objc
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

{% endtab %}
{% tab swift %}

En `AppDelegate.swift`, dentro de tu método `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool`, añade el siguiente método Braze:

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:appboyOptions)
```

donde `appboyOptions` es un `Dictionary` de valores de configuración de inicio.

{% endtab %}
{% endtabs %}

Este método sustituiría al método de inicialización `startWithApiKey:inApplication:withLaunchOptions:` y se llama con los siguientes parámetros:

- `YOUR-API-KEY`: La clave de API de tu aplicación se encuentra en **Administrar configuración** en el panel de Braze.
- `application`: La aplicación actual.
- `launchOptions`: Las opciones `NSDictionary` que obtienes de `application:didFinishLaunchingWithOptions:`.
- `appboyOptions`: Un `NSDictionary` opcional con valores de configuración de inicio para Braze.

Consulta [Appboy.h](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h) para ver una lista de las teclas de inicio de Braze.

## Appboy.sharedInstance() y anulabilidad Swift
A diferencia de la práctica habitual, el singleton `Appboy.sharedInstance()` es opcional. Esto se debe a que `sharedInstance` es `nil` antes de que se llame a `startWithApiKey:`, y hay algunas implementaciones no estándar pero no inválidas en las que se puede utilizar una inicialización retardada.

Si llamas a `startWithApiKey:` en tu delegado `didFinishLaunchingWithOptions:` antes de cualquier acceso a `sharedInstance` de Appboy (la implementación estándar), puedes utilizar el encadenamiento opcional, como `Appboy.sharedInstance()?.changeUser("testUser")`, para evitar comprobaciones engorrosas. Esto tendrá paridad con una implementación de Objective-C que haya asumido un `sharedInstance` no nulo.

## Opciones de integración manual

También puedes integrar nuestro SDK para tvOS manualmente: simplemente coge el Framework de nuestro [Repositorio Público](https://github.com/appboy/appboy-ios-sdk) e inicializa Braze como se indica en las secciones anteriores.

## Identificador de usuarios y análisis de informes
Consulta nuestra [documentación de]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=swift) iOS para obtener información sobre la configuración de ID de usuario, el registro de eventos personalizados y la configuración de atributos de usuario. También te recomendamos que te familiarices con [nuestras convenciones de denominación de eventos]({{site.baseurl}}/user_guide/data/custom_data/event_naming_conventions/).

