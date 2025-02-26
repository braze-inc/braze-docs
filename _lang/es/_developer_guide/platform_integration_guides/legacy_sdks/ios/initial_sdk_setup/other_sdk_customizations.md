---
nav_title: Otras personalizaciones del SDK
article_title: Otras personalizaciones del SDK para iOS
platform: iOS
description: "En este artículo de referencia se cubre la personalización del SDK, como el nivel de registro, la recogida de IDFA y otras personalizaciones."
page_order: 3

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Otras personalizaciones del SDK

## Nivel de registro Braze

El nivel de registro predeterminado para el SDK Braze iOS es mínimo, o `8` en la siguiente tabla. Este nivel suprime la mayoría de los registros para que no se registre ninguna información sensible en una aplicación lanzada en producción.

Consulta la siguiente lista de niveles de registro disponibles:

### Niveles de registro

| Nivel    | Descripción |
|----------|-------------|
| 0        | Verboso. Toda la información de registro se registrará en la consola de iOS.  |
| 1        | Depurar. La información de depuración y de registro superior se registrará en la consola de iOS.  |
| 2        | Advertencia. La información de advertencia y de registro superior se registrará en la consola de iOS.  |
| 4        | Error. Los errores y la información de registro superior se registrarán en la consola de iOS.  |
| 8        | Mínimo. Se registrará información mínima en la consola de iOS. La configuración predeterminada del SDK. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Registro detallado

Puedes configurar el nivel de registro a cualquier valor disponible. Sin embargo, establecer el nivel de registro en verbose, o `0`, puede ser muy útil para depurar problemas con tu integración. Este nivel solo está pensado para entornos de desarrollo y no debe establecerse en una aplicación publicada. El registro verboso no enviará ninguna información adicional o nueva del usuario a Braze.

### Configuración del nivel de registro

El nivel de registro se puede asignar en tiempo de compilación o en tiempo de ejecución:

{% tabs local %}
{% tab Tiempo de compilación %}

Añade un diccionario llamado `Braze` a tu archivo `Info.plist`. Dentro del diccionario `Braze`, añade la subentrada de cadena `LogLevel` y establece el valor `0`. 

{% alert note %}
Antes de la versión 4.0.2 del SDK de iOS de Braze, debe usarse la clave de diccionario `Appboy` en lugar de `Braze`.
{% endalert %} 

Ejemplo de contenidos `Info.plist`:

```
<key>Braze</key>
<dict>
  <key>LogLevel</key>
  <string>0</string>
</dict>
```

{% endtab %}
{% tab Tiempo de ejecución %}

Añade el `ABKLogLevelKey` dentro del parámetro `appboyOptions` pasado a `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`. Establece su valor en el número entero `0`.

{% subtabs %}
{% subtab OBJECTIVE-C %}

```objc
NSMutableDictionary *appboyOptions = [NSMutableDictionary dictionary];
appboyOptions[ABKLogLevelKey] = @(0);
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

{% endsubtab %}
{% subtab swift %}

```swift
let appboyOptions: [AnyHashable: Any] = [
  ABKLogLevelKey : 0
]
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions, withAppboyOptions:appboyOptions)
```

{% endsubtab %}
{% endsubtabs %}

{% alert note %}
El nivel de registro solo se puede configurar en tiempo de ejecución con la versión 4.4.0 del SDK de iOS de Braze o posterior. Si utilizas una versión anterior del SDK, establece el nivel de registro en tiempo de compilación.
{% endalert %} 

{% endtab %}
{% endtabs %}

## Recopilación opcional IDFV - Swift

En versiones anteriores del SDK de Braze para iOS Swift, el campo IDFV (identificador del proveedor) se recogía automáticamente como ID del dispositivo del usuario. 

A partir de la versión 5.7.0 del SDK Swift, el campo IDFV puede desactivarse opcionalmente y, en su lugar, Braze establecerá un UUID aleatorio como ID del dispositivo. Para más información, consulta [Recopilación de IDFV]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/swift_idfv/).

## Colección IDFA opcional

La Colección IDFA es opcional dentro del SDK de Braze y está desactivada por defecto. La recopilación de IDFA sólo es necesaria en Braze si pretendes utilizar nuestras [integraciones de atribución de instalación]({{site.baseurl}}/partners/advertising_technologies/attribution/adjust/). Si optas por almacenar tu IDFA, lo haremos de forma gratuita, para que puedas aprovechar estas opciones inmediatamente después de la publicación, sin trabajo de desarrollo adicional.

Por ello, te recomendamos que sigas recopilando el IDFA si cumples alguno de los siguientes criterios:

- Estás atribuyendo la instalación de la aplicación a un anuncio publicado anteriormente.
- Estás atribuyendo una acción dentro de la aplicación a un anuncio servido previamente

### iOS 14.5 AppTrackingTransparencia

Apple exige a los usuarios que se adhieran voluntariamente a través de un mensaje de permiso para recopilar IDFA.

Para recopilar IDFA, además de implementar nuestro protocolo `ABKIDFADelegate`, tu aplicación tendrá que solicitar autorización al usuario utilizando la dirección `ATTrackingManager` de Apple en el marco de transparencia de seguimiento de aplicaciones. Consulta el artículo sobre [privacidad del usuario](https://developer.apple.com/app-store/user-privacy-and-data-use/) de Apple para obtener más información.

La solicitud de autorización de transparencia de seguimiento de la aplicación requiere una entrada en `Info.plist` para explicar el uso que haces del identificador:

```
<key>NSUserTrackingUsageDescription</key>
<string>To retarget ads and build a global profile to better serve you things you would like.</string>
```

### Implementar la recopilación de IDFA

Sigue estos pasos para implementar la recopilación de IDFA:

##### Paso 1: Implementar ABKIDFADelegado

Crea una clase que se ajuste al protocolo [`ABKIDFADelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKIDFADelegate.h):

{% tabs %}
{% tab OBJETIVO-C %}

```objc
#import "IDFADelegate.h"
#import <AdSupport/ASIdentifierManager.h>
#import <AppTrackingTransparency/AppTrackingTransparency.h>

@implementation IDFADelegate

- (NSString *)advertisingIdentifierString {
  return [[[ASIdentifierManager sharedManager] advertisingIdentifier] UUIDString];
}

- (BOOL)isAdvertisingTrackingEnabledOrATTAuthorized {
  if (@available(iOS 14, *)) {
    return [ATTrackingManager trackingAuthorizationStatus] == ATTrackingManagerAuthorizationStatusAuthorized;
  }
  return [[ASIdentifierManager sharedManager] isAdvertisingTrackingEnabled];
}

@end
```

{% endtab %}
{% tab swift %}

```swift
import Appboy_iOS_SDK
import AdSupport
import AppTrackingTransparency

class IDFADelegate: NSObject, ABKIDFADelegate {
   func advertisingIdentifierString() -> String {
    return ASIdentifierManager.shared().advertisingIdentifier.uuidString
  }

  func isAdvertisingTrackingEnabledOrATTAuthorized() -> Bool {
    if #available(iOS 14, *) {
      return ATTrackingManager.trackingAuthorizationStatus ==  ATTrackingManager.AuthorizationStatus.authorized
    }
    return ASIdentifierManager.shared().isAdvertisingTrackingEnabled
  }
}
```
{% endtab %}
{% endtabs %}

##### Paso 2: Configura el delegado durante la inicialización de Braze

En el diccionario `appboyOptions` pasado a `startWithApiKey:inApplication:withAppboyOptions:`, establece la clave `ABKIDFADelegateKey` en una instancia de tu clase conforme `ABKIDFADelegate`.

## Tamaño aproximado del SDK de iOS {#ios-sdk-size}

El tamaño de archivo aproximado del framework del SDK de iOS es de 30 MB, y el tamaño aproximado del archivo .ipa (archivo adicional a la aplicación) está entre 1 MB y 2 MB.

Braze mide el tamaño de nuestro SDK para iOS observando el efecto del SDK en el tamaño de `.ipa`, según las [recomendaciones de Apple sobre el tamaño de las aplicaciones](https://developer.apple.com/library/content/qa/qa1795/_index.html). Si estás calculando la adición de tamaño del SDK de iOS a tu aplicación, te recomendamos lo siguiente [Obtener un informe del tamaño de la aplicación](https://developer.apple.com/library/content/qa/qa1795/_index.html) para comparar la diferencia de tamaño en tu `.ipa` antes y después de integrar el SDK de Braze para iOS. Cuando compares los tamaños del informe sobre el tamaño de las aplicaciones, te recomendamos que mires también los tamaños de las aplicaciones para los archivos `.ipa` reducidos, ya que los archivos universales `.ipa` serán mayores que los binarios descargados de la App Store e instalados en los dispositivos de los usuarios.

{% alert note %}
Si estás integrando a través de CocoaPods con `use_frameworks!`, establece `Enable Bitcode = NO` en la Configuración de compilación del objetivo para obtener un tamaño preciso.
{% endalert %}

