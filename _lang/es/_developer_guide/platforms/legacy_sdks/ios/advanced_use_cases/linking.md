---
nav_title: Vinculación en profundidad
article_title: Vinculación en profundidad para iOS
platform: iOS
page_order: 0
description: "En este artículo se explica cómo implementar el delegado universal de vinculación en profundidad para tu aplicación de iOS y se dan ejemplos de cómo establecer una vinculación en profundidad con la configuración de la aplicación."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Vinculación en profundidad para iOS

Para obtener información introductoria sobre los vínculos profundos, consulta [el artículo de nuestra Guía del usuario]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking). Si quieres implementar vínculos en profundidad por primera vez en tu aplicación Braze, los pasos siguientes te ayudarán a empezar.

## Paso 1: Registrar un esquema

Debes indicar un esquema personalizado en el archivo `Info.plist`. La estructura de navegación está definida por una matriz de diccionarios. Cada uno de esos diccionarios contiene una matriz de cadenas.

Utiliza Xcode para editar tu archivo `Info.plist`:

1. Añade una nueva clave, `URL types`. Xcode lo convertirá automáticamente en una matriz que contiene un diccionario llamado `Item 0`.
2. Dentro de `Item 0`, añade una clave `URL identifier`. Ajusta el valor a tu esquema personalizado.
3. Dentro de `Item 0`, añade una clave `URL Schemes`. Será automáticamente una matriz que contendrá una cadena `Item 0`.
4. Configura `URL Schemes` >> `Item 0` a tu esquema personalizado.

Alternativamente, si deseas editar tu archivo `Info.plist` directamente, puedes seguir esta especificación:

```html
<key>CFBundleURLTypes</key>
<array>
    <dict>
        <key>CFBundleURLName</key>
        <string>{YOUR.SCHEME}</string>
        <key>CFBundleURLSchemes</key>
        <array>
            <string>{YOUR.SCHEME}</string>
        </array>
    </dict>
</array>
```

## Paso 2: Permitir el esquema personalizado (iOS 9+)

A partir de iOS 9, las aplicaciones deben tener una lista de esquemas personalizados que la aplicación puede abrir. Si intentas llamar a esquemas que están fuera de esta lista, el sistema registrará un error en los registros del dispositivo y el vínculo profundo no se abrirá. Un ejemplo de este error es el siguiente

```
<Warning>: -canOpenURL: failed for URL: "yourapp://deeplink" – error: "This app is not allowed to query for scheme yourapp"
```

Por ejemplo, si un mensaje dentro de la aplicación debe abrir la aplicación de Facebook al tocarlo, la aplicación tiene que tener el esquema personalizado de Facebook (`fb`) en la lista de permitidos. De lo contrario, el sistema rechazará el deep link. Los vínculos profundos que dirigen a una página o vista dentro de tu propia aplicación siguen requiriendo que el esquema personalizado de tu aplicación aparezca en el sitio `Info.plist` de tu aplicación.

Debes añadir todos los esquemas a los que la aplicación necesita vincularse en profundidad en una lista de permitidos en la página `Info.plist` de tu aplicación con la clave `LSApplicationQueriesSchemes`. Por ejemplo:

```html
<key>LSApplicationQueriesSchemes</key>
<array>
    <string>myapp</string>
    <string>facebook</string>
    <string>twitter</string>
</array>
```

Para más información, consulta [la documentación de Apple](https://developer.apple.com/library/content/documentation/General/Reference/InfoPlistKeyReference/Articles/LaunchServicesKeys.html#//apple_ref/doc/uid/TP40009250-SW14) sobre la tecla `LSApplicationQueriesSchemes`.

## Paso 3: Implementa un controlador

Tras activar tu aplicación, iOS llamará al método [`application:openURL:options:`](https://developer.apple.com/reference/uikit/uiapplicationdelegate/1623112-application?language=objc). El argumento importante es el objeto [NSURL](https://developer.apple.com/library/ios/DOCUMENTATION/Cocoa/Reference/Foundation/Classes/NSURL_Class/Reference/Reference.html#//apple_ref/doc/c_ref/NSURL).

{% tabs %}
{% tab OBJETIVO-C %}

```objc
- (BOOL)application:(UIApplication *)app openURL:(NSURL *)url options:(NSDictionary<UIApplicationOpenURLOptionsKey, id> *)options {
  NSString *path  = [url path];
  NSString *query = [url query];
  // Here you should insert code to take some action based upon the path and query.
  return YES;
}
```

{% endtab %}
{% tab swift %}

```swift
func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
  let path = url.path
  let query = url.query
  // Here you should insert code to take some action based upon the path and query.
  return true
}
```

{% endtab %}
{% endtabs %}

![]({% image_buster /assets/img_archive/deep_link.png %})

# Enlaces universales

Para utilizar los enlaces universales, asegúrate de haber añadido un dominio registrado a las capacidades de tu aplicación y de haber subido un archivo `apple-app-site-association`. A continuación, implementa el método `application:continueUserActivity:restorationHandler:` en tu `AppDelegate`. Por ejemplo:

{% tabs %}
{% tab OBJETIVO-C %}

```objc
- (BOOL)application:(UIApplication *)application
continueUserActivity:(NSUserActivity *)userActivity
  restorationHandler:(void (^)(NSArray *restorableObjects))restorationHandler {
  if ([userActivity.activityType isEqualToString:NSUserActivityTypeBrowsingWeb]) {
    NSURL *url = userActivity.webpageURL;
    // Handle url
  }
  return YES;
}
```

{% endtab %}
{% tab swift %}

```swift
func application(_ application: UIApplication, continue userActivity: NSUserActivity, restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {
  if (userActivity.activityType == NSUserActivityTypeBrowsingWeb) {
    let url = userActivity.webpageURL
    // Handle url
  }
  return true
}
```

{% endtab %}
{% endtabs %}

Consulta [Apple](https://developer.apple.com/library/content/documentation/General/Conceptual/AppSearch/UniversalLinks.html) para más información.

{% alert note %}
La integración predeterminada del enlace universal no es compatible con las notificaciones push de Braze ni con los mensajes dentro de la aplicación. Consulta la [personalización de](#linking-handling-customization) enlaces para manejar enlaces universales dentro de tu aplicación. Alternativamente, recomendamos utilizar [vínculos en profundidad basados en esquemas](#step-1-registering-a-scheme) con notificaciones push y mensajes dentro de la aplicación.
{% endalert%}

## Seguridad en el transporte de aplicaciones (ATS)
iOS 9 introdujo un cambio de última hora que afecta a las URL web incrustadas en mensajes dentro de la aplicación y notificaciones push.

### Requisitos ATS
De [la documentación de Apple:](https://developer.apple.com/library/prerelease/ios/releasenotes/General/WhatsNewIniOS/Articles/iOS9.html#//apple_ref/doc/uid/TP40016198-SW14) "App Transport Security" es una característica que mejora la seguridad de las conexiones entre una aplicación y los servicios Web. La característica consiste en requisitos de conexión predeterminados que se ajustan a las mejores prácticas para conexiones seguras. Las aplicaciones pueden anular este comportamiento predeterminado y desactivar la seguridad del transporte".

El ATS se aplica por predeterminado en iOS 9+. Requiere que todas las conexiones utilicen HTTPS y estén encriptadas mediante TLS 1.2 con confidencialidad directa. Consulta los [Requisitos para conectarse mediante ATS](https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW35) para obtener más información. Todas las imágenes servidas por Braze a dispositivos finales son gestionadas por una red de entrega de contenidos ("CDN") que admite TLS 1.2 y es compatible con ATS.

A menos que se especifiquen como excepciones en la página `Info.plist` de tu aplicación, las conexiones que no sigan estos requisitos fallarán con errores parecidos a éste:

```
CFNetwork SSLHandshake failed (-9801)
Error Domain=NSURLErrorDomain Code=-1200 "An SSL error has occurred, and a secure connection to the server cannot be made."
```

```
NSURLSession/NSURLConnection HTTP load failed (kCFStreamErrorDomainSSL, -9802)
```

El cumplimiento de la ATS se aplica a los enlaces abiertos dentro de la aplicación móvil (nuestro tratamiento predeterminado de los enlaces en los que se hace clic) y no se aplica a los sitios abiertos externamente a través de un navegador web.

### Gestión de los requisitos ATS

Puedes manejar ATS de una de las tres formas siguientes:

#### Confirma que todos los enlaces cumplen la normativa ATS (recomendado)
Tu integración con Braze puede satisfacer los requisitos de ATS asegurándote de que cualquier enlace existente al que dirijas a los usuarios (mediante campañas de mensajería dentro de la aplicación y push) satisfaga los requisitos de ATS. Aunque hay formas de eludir las restricciones de la ATS, te recomendamos que compruebes que todas las URL enlazadas cumplen la ATS. Dado el creciente énfasis de Apple en la seguridad de las aplicaciones, no está garantizado que Apple admita los siguientes enfoques para permitir excepciones ATS.

Una herramienta SSL puede ayudarte a detectar problemas de seguridad del servidor Web. Esta [prueba de servidor SSL](https://www.ssllabs.com/ssltest/index.html) de Qualys, Inc. proporciona una partida específica para el cumplimiento de Apple ATS 9 e iOS 9.

#### Desactiva parcialmente el ATS
Puedes permitir que un subconjunto de enlaces con determinados dominios o esquemas sean tratados como excepciones a las normas ATS. Tu integración Braze satisfará los requisitos de ATS si cada enlace que utilices en un canal de mensajería Braze es compatible con ATS o se gestiona mediante una excepción.

Para añadir un dominio como excepción del ATS, añade lo siguiente al archivo `Info.plist` de tu aplicación:

```html
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>
    <key>NSExceptionDomains</key>
    <dict>
        <key>example.com</key>
        <dict>
            <key>NSExceptionAllowsInsecureHTTPLoads</key>
            <false/>
            <key>NSIncludesSubdomains</key>
            <true/>
        </dict>
    </dict>
</dict>
```

Consulta el artículo de Apple sobre [las claves de seguridad para el transporte de aplicaciones](https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW33) para obtener más información.

#### Desactiva por completo el ATS

Puedes desactivar ATS por completo. Ten en cuenta que no es una práctica recomendada, tanto por la pérdida de protecciones de seguridad como por la futura compatibilidad con iOS. Para desactivar ATS, inserta lo siguiente en el archivo `Info.plist` de tu aplicación:

```html
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>
</dict>
```

Consulta [Enviar una aplicación con seguridad de transporte de aplicaciones](http://timekl.com/blog/2015/08/21/shipping-an-app-with-app-transport-security/?utm_campaign=iOS+Dev+Weekly&utm_medium=email&utm_source=iOS_Dev_Weekly_Issue_213) para obtener más información sobre cómo depurar fallos de ATS.

## Codificación URL

A partir del SDK v2.21.0 de Braze para iOS, el SDK codifica porcentualmente los enlaces para crear `NSURL` válidos. Todos los caracteres de enlace que no estén permitidos en una URL correctamente formada, como los caracteres Unicode, se escaparán en porcentaje.

Para descodificar un enlace codificado, utiliza el método `NSString` [`stringByRemovingPercentEncoding`](https://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Classes/NSString_Class/index.html#//apple_ref/occ/instm/NSString/stringByRemovingPercentEncoding). Ten en cuenta que también debes devolver `YES` en `ABKURLDelegate` y que es necesaria una llamada a la acción para desencadenar la manipulación de la URL por parte de la aplicación. Por ejemplo:

{% tabs %}
{% tab OBJETIVO-C %}

```objc
- (BOOL)application:(UIApplication *)application openURL:(NSURL *)url options:(NSDictionary<NSString *, id> *)options {
  NSString *urlString = url.absoluteString.stringByRemovingPercentEncoding;
  // Handle urlString
  return YES;
}
```

{% endtab %}
{% tab swift %}

```swift
  func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
    let urlString = url.absoluteString.removingPercentEncoding
    // Handle urlString
    return true
  }
```

{% endtab %}
{% endtabs %}

## Personalización {#linking-customization}

### Personalización predeterminada de WebView

La clase personalizable `ABKModalWebViewController` muestra las URL web abiertas por el SDK, normalmente, cuando se selecciona "Abrir URL web dentro de la aplicación" para un vínculo profundo web.

Puedes declarar una categoría para la clase `ABKModalWebViewController`, o modificarla directamente, para aplicar la personalización a la vista Web. Consulta el [ archivo .h](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKModalWebViewController.h) y el [ archivo .m](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/ABKModalWebViewController.m) de la clase para obtener más detalles.

### Personalización de la gestión de enlaces

El protocolo `ABKURLDelegate` puede utilizarse para personalizar el tratamiento de las URL, como los vínculos profundos, las URL web y los vínculos universales. Para configurar el delegado durante la inicialización de Braze, pasa un objeto delegado a `ABKURLDelegateKey` en la dirección `appboyOptions` de [`startWithApiKey:inApplication:withAppboyOptions:`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24). A continuación, Braze llamará a la implementación de `handleAppboyURL:fromChannel:withExtras:` de tu delegado antes de gestionar cualquier URI.

#### Ejemplo de integración: ABKURLDelegado

{% tabs %}
{% tab OBJETIVO-C %}

```objc
- (BOOL)handleAppboyURL:(NSURL *)url fromChannel:(ABKChannel)channel withExtras:(NSDictionary *)extras {
  if ([[url.host lowercaseString] isEqualToString:@"MY-DOMAIN.com"]) {
    // Custom handle link here
    return YES;
  }
  // Let Braze handle links otherwise
  return NO;
}
```

{% endtab %}
{% tab swift %}

```swift
func handleAppboyURL(_ url: URL?, from channel: ABKChannel, withExtras extras: [AnyHashable : Any]?) -> Bool {
  if (url.host == "MY-DOMAIN.com") {
    // Custom handle link here
    return true;
  }
  // Let Braze handle links otherwise
  return false;
}
```

{% endtab %}
{% endtabs %}

Para más información, consulta [`ABKURLDelegate.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKURLDelegate.h).

## Casos de uso frecuentes

### Vinculación en profundidad con la configuración de la aplicación

iOS puede llevar a los usuarios de tu aplicación a su página en la aplicación de configuración de iOS. Puedes aprovechar `UIApplicationOpenSettingsURLString` para vincular en profundidad a los usuarios a la configuración desde las notificaciones push y los mensajes dentro de la aplicación.

1. En primer lugar, asegúrate de que tu aplicación está configurada para [enlaces profundos basados en esquemas](#deep-links) o [enlaces universales](#universal-links).
2. Decide un URI para la vinculación en profundidad a la página de **configuración** (por ejemplo, `myapp://settings` o `https://www.braze.com/settings`).
3. Si utilizas vínculos profundos personalizados basados en esquemas, añade el siguiente código a tu método `application:openURL:options:`:

{% tabs %}
{% tab OBJETIVO-C %}

```objc
- (BOOL)application:(UIApplication *)app
            openURL:(NSURL *)url
            options:(NSDictionary<UIApplicationOpenURLOptionsKey,id> *)options {
  NSString *path  = [url path];
  if ([path isEqualToString:@"settings"]) {
    NSURL *settingsURL = [NSURL URLWithString:UIApplicationOpenSettingsURLString];
    [[UIApplication sharedApplication] openURL:settingsURL];
  }
  return YES;
}
```

{% endtab %}
{% tab swift %}

```swift
func application(_ app: UIApplication, open url: URL, options: [UIApplicationOpenURLOptionsKey : Any] = [:]) -> Bool {
  let path = url.path
  if (path == "settings") {
    UIApplication.shared.openURL(URL(string:UIApplicationOpenSettingsURLString)!)
  }
  return true
}
```

{% endtab %}
{% endtabs %}

