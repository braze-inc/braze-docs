La instalación del SDK de Braze te proporcionará una funcionalidad básica de análisis{% if include.platform == 'iOS' %}, así como mensajes dentro de la aplicación con los que podrás interactuar con tus usuarios{% endif %}.

El SDK de Braze de {{include.platform}} debe instalarse o actualizarse mediante [CocoaPods](http://cocoapods.org/), un administrador de dependencias para proyectos Objective-C y Swift. CocoaPods proporciona una mayor simplicidad para la integración y la actualización.

## {{include.platform}} Integración de SDK CocoaPods

### Paso 1: Instalar CocoaPods

La instalación del SDK a través de {{include.platform}} [CocoaPods](http://cocoapods.org/) automatiza por ti la mayor parte del proceso de instalación. Antes de comenzar este proceso, comprueba que utilizas [la versión de Ruby 2.0.0 o superior](https://www.ruby-lang.org/en/installation/). Ten en cuenta que no es necesario conocer la sintaxis de Ruby para instalar este SDK.

Sólo tienes que ejecutar el siguiente comando para empezar:

```bash
$ sudo gem install cocoapods
```

**Nota**: Si se te pide que sobrescribas el ejecutable de `rake`, consulta las [Instrucciones de inicio en CocoaPods.org](http://guides.cocoapods.org/using/getting-started.html) para más detalles.

**Nota**: Si tienes problemas relacionados con [CocoaPods](http://guides.cocoapods.org/using/troubleshooting.html), consulta la [Guía de solución de problemas de CocoaPods](http://guides.cocoapods.org/using/troubleshooting.html).

### Paso 2: Construir el archivo de bibliotecas

Ahora que has instalado la Gema Ruby de CocoaPods, tendrás que crear un archivo en el directorio de tu proyecto de Xcode llamado `Podfile`.

Añade la siguiente línea a tu archivo de bibliotecas:

```
target 'YourAppTarget' do
  pod 'Appboy-{{include.platform}}-SDK'
end
```

**Nota**: Te sugerimos que versiones Braze para que las actualizaciones de vainas cojan automáticamente cualquier cosa menor que una actualización de versión menor. Esto parece 'pod 'Appboy-{{include.platform}}-SDK' ~> Major.Minor.Build'. Si quieres integrar automáticamente la última versión del SDK de Braze incluso con cambios importantes, puedes utilizar `pod 'Appboy-{{include.platform}}-SDK'` en tu archivo de bibliotecas.
{% if include.platform == 'iOS' %}
**Nota**: Si no utilizas ninguna interfaz de usuario predeterminada de Braze y no quieres introducir la dependencia de SDWebImage, apunta tu dependencia de Braze en tu archivo de bibliotecas a nuestra subespecífica Core, como `pod 'Appboy-iOS-SDK/Core'` en tu archivo de bibliotecas. {% endif %}.

### Paso 3: Instalación del SDK de Braze

Para instalar los SDK de Braze CocoaPods, ve al directorio de tu proyecto de aplicación Xcode en tu terminal y ejecuta el siguiente comando:
```
pod install
```

En este punto deberías poder abrir el nuevo espacio de trabajo del proyecto Xcode creado por CocoaPods. Asegúrate de utilizar este espacio de trabajo de Xcode en lugar de tu proyecto de Xcode. 

![Nuevo espacio de trabajo]({% image_buster /assets/img_archive/podsworkspace.png %})

### Paso 4: Actualizar el delegado de tu aplicación

{% tabs %}
{% tab OBJECTIVE-C %}

Añade la siguiente línea de código a tu archivo `AppDelegate.m`:

```objc
{% if include.platform == 'iOS' %}#import "Appboy-iOS-SDK/AppboyKit.h"{% else %}#import <AppboyTVOSKit/AppboyKit.h>{% endif %}
```

Dentro de tu archivo `AppDelegate.m`, añade el siguiente fragmento de código dentro de tu método `application:didFinishLaunchingWithOptions`:

```objc
[Appboy startWithApiKey:@"YOUR-API-KEY"
         inApplication:application
     withLaunchOptions:launchOptions];
```

{% endtab %}
{% tab swift %}

Si estás integrando el SDK de Braze con CocoaPods o Carthage, añade la siguiente línea de código a tu archivo `AppDelegate.swift`:

```swift
{% if include.platform == 'iOS' %}import Appboy_iOS_SDK{% else %}import AppboyTVOSKit{% endif %}
```

Para más información sobre el uso de código Objective-C en proyectos Swift, consulta [los documentos para desarrolladores de Apple](https://developer.apple.com/library/ios/documentation/swift/conceptual/buildingcocoaapps/MixandMatch.html).

En `AppDelegate.swift`, añade el siguiente fragmento de código a tu `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool`:

```swift
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions)
```

**Nota**: El singleton de Braze `sharedInstance` será nulo antes de llamar a `startWithApiKey:`, ya que es un requisito previo para utilizar cualquier funcionalidad de Braze.

{% endtab %}
{% endtabs %}

{% alert important %}
Asegúrate de actualizar `YOUR-API-KEY` con el valor correcto desde tu página Administrar configuración.
{% endalert %}

{% alert warning %}
Asegúrate de inicializar Braze en el hilo principal de tu aplicación. Inicializar de forma asíncrona puede provocar fallos en la funcionalidad.
{% endalert %}


### Paso 5: Especifica tu punto final personalizado o clúster de datos

{% alert note %}
Ten en cuenta que, a partir de diciembre de 2019, ya no se entregarán puntos finales personalizados; si tienes un punto final personalizado preexistente, puedes seguir utilizándolo. Para más detalles, consulta nuestra <a href="{{site.baseurl}}/api/basics/#endpoints">lista de puntos finales disponibles</a>.
{% endalert %}

Tu representante de Braze ya debería haberte informado del [punto final correcto]({{ site.baseurl }}/user_guide/administrative/access_braze/sdk_endpoints/).

#### Configuración del punto final en tiempo de compilación (recomendado)
Si se te da un punto final personalizado preexistente...
- A partir de la versión 3.0.2 del SDK iOS de Braze, puedes establecer un punto final personalizado utilizando el archivo `Info.plist`. Añade el diccionario `Appboy` a tu archivo Info.plist. Dentro del diccionario `Appboy`, añade la subentrada de cadena `Endpoint` y establece el valor en la autoridad de la url de tu punto final personalizado (por ejemplo, `sdk.iad-01.braze.com`, no `https://sdk.iad-01.braze.com`).

#### Configuración del punto final en tiempo de ejecución

Si se te da un punto final personalizado preexistente...
- A partir de la versión 3.17.0 del SDK iOS de Braze, puedes anular la configuración de tu punto final a través de `ABKEndpointKey` dentro del parámetro `appboyOptions` pasado a `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`. Establece el valor de la autoridad de tu url personalizada (por ejemplo, `sdk.iad-01.braze.com`, no `https://sdk.iad-01.braze.com`).

{% alert note %}
Se ha eliminado el soporte del SDK versión 3.17.0 del iOS de Braze para la configuración de puntos finales en tiempo de ejecución mediante `ABKAppboyEndpointDelegate`. Si ya utilizas `ABKAppboyEndpointDelegate`, nota que en las versiones v3.14.1 a v3.16.0 del SDK de Braze para iOS, cualquier referencia a `dev.appboy.com` en tu método `getApiEndpoint()` debe sustituirse por una referencia a `sdk.iad-01.braze.com`.
{% endalert %}

{% alert important %}
Para conocer tu clúster específico, pregunta a tu administrador del éxito del cliente o ponte en contacto con nuestro equipo de soporte.
{% endalert %}

### Integración de SDK completa

Ahora Braze debería estar recopilando datos de tu aplicación y tu integración básica debería estar completa. {% if include.platform == 'iOS' %}Consulta las secciones siguientes para habilitar el seguimiento de eventos personalizado, la mensajería push, la fuente de noticias y la línea completa de productos Braze.{% else %}Ten en cuenta que al compilar tu aplicación tvOS y cualquier otra biblioteca de terceros, Bitcode debe estar habilitado.{% endif %}

### Actualizar el SDK de Braze mediante CocoaPods

Para actualizar un Cocoapod simplemente ejecuta los siguientes comandos dentro del directorio de tu proyecto:

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

**Nota**: Este método sustituiría al método de inicialización `startWithApiKey:inApplication:withLaunchOptions:`.

Este método se llama con los siguientes parámetros:

- `YOUR-API-KEY` - La clave de API de tu aplicación desde el panel de Braze
- `application` - La aplicación actual
- `launchOptions` - Las opciones `NSDictionary` que obtienes de `application:didFinishLaunchingWithOptions:`
- `appboyOptions` - Un `NSDictionary` opcional con valores de configuración de inicio para Braze

Consulta [Appboy.h](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h) para ver una lista de las teclas de inicio de Braze.

## Appboy.sharedInstance() y anulabilidad Swift
A diferencia de la práctica habitual, el singleton `Appboy.sharedInstance()` es opcional. Esto se debe a que `sharedInstance` es `nil` antes de que se llame a `startWithApiKey:`, y hay algunas implementaciones no estándar pero no inválidas en las que se puede utilizar una inicialización retardada.

Si llamas a `startWithApiKey:` en tu delegado `didFinishLaunchingWithOptions:` antes de cualquier acceso a `sharedInstance` de Appboy (la implementación estándar), puedes utilizar el encadenamiento opcional, como `Appboy.sharedInstance()?.changeUser("testUser")`, para evitar comprobaciones engorrosas. Esto tendrá paridad con una implementación de Objective-C que haya asumido un `sharedInstance` no nulo.

