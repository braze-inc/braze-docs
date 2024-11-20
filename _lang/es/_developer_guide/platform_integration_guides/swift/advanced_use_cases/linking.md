---
nav_title: Vinculación en profundidad
article_title: Vinculación en profundidad para iOS
platform: Swift
page_order: 1
description: "En este artículo se explica cómo implementar el delegado universal de vinculación en profundidad para tu aplicación de iOS y se dan ejemplos de cómo establecer un vínculo profundo con la configuración de la aplicación para el SDK de Swift."

---

# Vínculos profundos

> La vinculación en profundidad es una forma de proporcionar un enlace que inicie una aplicación nativa, muestre un contenido específico o realice alguna acción concreta. Si quieres implementar por primera vez los vínculos en profundidad en tu aplicación para iOS, sigue estos pasos.

Para obtener información general sobre qué son los vínculos profundos, consulta nuestro [artículo de Preguntas frecuentes]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking). 

## Paso 1: Registrar un esquema

Para gestionar la vinculación en profundidad, debe indicarse un esquema personalizado en tu archivo `Info.plist`. La estructura de navegación está definida por una matriz de diccionarios. Cada uno de esos diccionarios contiene una matriz de cadenas.

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
        <string>YOUR.SCHEME</string>
        <key>CFBundleURLSchemes</key>
        <array>
            <string>YOUR.SCHEME</string>
        </array>
    </dict>
</array>
```

## Paso 2: Añadir un esquema de lista permitida

Debes declarar los esquemas de URL que deseas pasar a `canOpenURL(_:)` añadiendo la clave `LSApplicationQueriesSchemes` al archivo Info.plist de tu aplicación. Intentar llamar a esquemas fuera de esta lista permitida hará que el sistema registre un error en los registros del dispositivo, y el vínculo profundo no se abrirá. Un ejemplo de este error tendrá el siguiente aspecto:

```
<Warning>: -canOpenURL: failed for URL: "yourapp://deeplink" – error: "This app is not allowed to query for scheme yourapp"
```

Por ejemplo, si un mensaje dentro de la aplicación debe abrir la aplicación de Facebook al tocarlo, la aplicación tiene que tener el esquema personalizado de Facebook (`fb`) en tu lista de permitidos. De lo contrario, el sistema rechazará el deep link. Los vínculos profundos que dirigen a una página o vista dentro de tu propia aplicación siguen requiriendo que el esquema personalizado de tu aplicación aparezca en el sitio `Info.plist` de tu aplicación.

Tu lista de permitidos de ejemplo podría ser algo así

```html
<key>LSApplicationQueriesSchemes</key>
<array>
    <string>myapp</string>
    <string>fb</string>
    <string>twitter</string>
</array>
```

Para más información, consulta [la documentación de Apple](https://developer.apple.com/library/content/documentation/General/Reference/InfoPlistKeyReference/Articles/LaunchServicesKeys.html#//apple_ref/doc/uid/TP40009250-SW14) sobre la tecla `LSApplicationQueriesSchemes`.

## Paso 3: Implementa un controlador

Tras activar tu aplicación, iOS llamará al método [`application:openURL:options:`](https://developer.apple.com/reference/uikit/uiapplicationdelegate/1623112-application?language=objc). El argumento importante es el objeto [NSURL](https://developer.apple.com/library/ios/DOCUMENTATION/Cocoa/Reference/Foundation/Classes/NSURL_Class/Reference/Reference.html#//apple_ref/doc/c_ref/NSURL).

{% tabs %}
{% tab swift %}

```swift
func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
  let path = url.path
  let query = url.query
  // Insert your code here to take some action based upon the path and query.
  return true
}
```

{% endtab %}
{% tab OBJETIVO-C %}

```objc
- (BOOL)application:(UIApplication *)app openURL:(NSURL *)url options:(NSDictionary<UIApplicationOpenURLOptionsKey, id> *)options {
  NSString *path  = [url path];
  NSString *query = [url query];
  // Insert your code here to take some action based upon the path and query.
  return YES;
}
```

{% endtab %}
{% endtabs %}

## Seguridad en el transporte de aplicaciones (ATS)

### Requisitos ATS
De [la documentación de Apple:](https://developer.apple.com/library/prerelease/ios/releasenotes/General/WhatsNewIniOS/Articles/iOS9.html#//apple_ref/doc/uid/TP40016198-SW14) "App Transport Security" es una característica que mejora la seguridad de las conexiones entre una aplicación y los servicios Web. La característica consiste en requisitos de conexión predeterminados que se ajustan a las mejores prácticas para conexiones seguras. Las aplicaciones pueden anular este comportamiento predeterminado y desactivar la seguridad del transporte".

El ATS se aplica por predeterminado. Requiere que todas las conexiones utilicen HTTPS y estén encriptadas mediante TLS 1.2 con confidencialidad directa. Consulta los [Requisitos para conectarse mediante ATS](https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW35) para obtener más información. Todas las imágenes servidas por Braze a dispositivos finales son gestionadas por una red de entrega de contenidos ("CDN") que admite TLS 1.2 y es compatible con ATS.

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

#### Asegúrate de que todos los enlaces son compatibles con ATS (recomendado)
Tu integración con Braze puede satisfacer los requisitos de ATS asegurándote de que cualquier enlace existente al que dirijas a los usuarios (por ejemplo, mediante campañas de mensajería dentro de la aplicación y notificaciones push) satisfaga los requisitos de ATS. Aunque hay formas de eludir las restricciones de la ATS, nuestra recomendación es que te asegures de que todas las URL enlazadas cumplen la ATS. Dado el creciente énfasis de Apple en la seguridad de las aplicaciones, no está garantizado que Apple admita los siguientes enfoques para permitir excepciones ATS.

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

## Codificación URL

El SDK codifica porcentualmente los enlaces para crear `URL` válidos. Todos los caracteres de enlace que no estén permitidos en una URL correctamente formada, como los caracteres Unicode, se escaparán en porcentaje.

Para descodificar un enlace codificado, utiliza la propiedad `String` [`removingPercentEncoding`](https://developer.apple.com/documentation/swift/stringprotocol/removingpercentencoding). También debes devolver `true` en la dirección `BrazeDelegate.braze(_:shouldOpenURL:)`. Se necesita una llamada a la acción para desencadenar el manejo de la URL por parte de tu aplicación. 

Por ejemplo:

{% tabs %}
{% tab swift %}

```swift
  func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
    let urlString = url.absoluteString.removingPercentEncoding
    // Handle urlString
    return true
  }
```

{% endtab %}
{% tab OBJETIVO-C %}

```objc
- (BOOL)application:(UIApplication *)application openURL:(NSURL *)url options:(NSDictionary<NSString *, id> *)options {
  NSString *urlString = [url.absoluteString stringByRemovingPercentEncoding];
  // Handle urlString
  return YES;
}
```

{% endtab %}
{% endtabs %}


## Vínculo profundo con la configuración de la aplicación

Puedes aprovechar `UIApplicationOpenSettingsURLString` para vincular en profundidad a los usuarios con la configuración de tu aplicación desde las notificaciones push de Braze, los mensajes dentro de la aplicación y la fuente de noticias.

Para llevar a los usuarios de tu aplicación a la configuración de iOS:
1. En primer lugar, asegúrate de que tu aplicación está configurada para [enlaces profundos basados en esquemas](##step-1-registering-a-scheme) o [enlaces universales](#universal-links).
2. Decide un URI para la vinculación en profundidad a la página de **configuración** (por ejemplo, `myapp://settings` o `https://www.braze.com/settings`).
3. Si utilizas vínculos profundos personalizados basados en esquemas, añade el siguiente código a tu método `application:openURL:options:`:

{% tabs %}
{% tab swift %}

```swift
func application(_ app: UIApplication, open url: URL, options: [UIApplicationOpenURLOptionsKey : Any] = [:]) -> Bool {
  let path = url.path
  if (path == "settings") {
    UIApplication.shared.openURL(URL(string:UIApplication.openSettingsURLString)!)
  }
  return true
}
```

{% endtab %}
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
{% endtabs %}

## Personalización {#linking-customization}

### Personalización predeterminada de WebView

La clase `Braze.WebViewController` muestra las URL web abiertas por el SDK, normalmente, cuando se selecciona "Abrir URL web dentro de la aplicación" para un vínculo profundo a la web.

Puedes personalizar el `Braze.WebViewController` mediante el método delegado [`BrazeDelegate.braze(_:willPresentModalWithContext:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate/braze(_:willpresentmodalwithcontext:)-12sqy/).

### Personalización de la gestión de enlaces

El protocolo `BrazeDelegate` puede utilizarse para personalizar el tratamiento de las URL, como los vínculos profundos, las URL web y los vínculos universales. Para configurar el delegado durante la inicialización de Braze, establece un objeto delegado en la instancia de `Braze`. A continuación, Braze llamará a la implementación de `shouldOpenURL` de tu delegado antes de gestionar cualquier URI.

#### Enlaces universales

Braze admite enlaces universales en notificaciones push, mensajes dentro de la aplicación y tarjetas de contenido. Para habilitar la compatibilidad con el enlace universal, [`configuration.forwardUniversalLinks`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/forwarduniversallinks) debe estar configurado en `true`.

Cuando esté habilitado, Braze reenviará los enlaces universales a la página `AppDelegate` de tu aplicación mediante el método [`application:continueUserActivity:restorationHandler:`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623072-application) método. 

Tu aplicación también debe estar configurada para gestionar enlaces universales. Consulta [la documentación de Apple](https://developer.apple.com/documentation/xcode/supporting-universal-links-in-your-app) para asegurarte de que tu aplicación está configurada correctamente para los enlaces universales.

{% alert warning %}
El reenvío universal de enlaces requiere acceso a los derechos de la aplicación. Al ejecutar la aplicación en un simulador, estos derechos no están disponibles directamente y los enlaces universales no se reenvían a los controladores del sistema.
Para añadir soporte a las compilaciones del simulador, puedes añadir el archivo `.entitlements` de la aplicación a la fase de compilación _Copiar recursos del paquete_. Consulta la [`forwardUniversalLinks`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/forwarduniversallinks) documentación para más detalles.
{% endalert %}

{% alert note %}
El SDK no consulta el archivo `apple-app-site-association` de tus dominios. Realiza la diferenciación entre enlaces universales y URL normales fijándose sólo en el nombre de dominio. Como resultado, el SDK no respeta ninguna regla de exclusión definida en la página `apple-app-site-association` por [Apoyar dominios asociados](https://developer.apple.com/documentation/xcode/supporting-associated-domains).
{% endalert %}

### Ejemplo de integración: BrazeDelegate

{% tabs %}
{% tab swift %}

```swift
func braze(_ braze: Braze, shouldOpenURL context: Braze.URLContext) -> Bool {
  if context.url.host == "MY-DOMAIN.com" {
    // Custom handle link here
    return false
  }
  // Let Braze handle links otherwise
  return true
}
```

{% endtab %}
{% tab OBJETIVO-C %}

```objc
- (BOOL)braze:(Braze *)braze shouldOpenURL:(BRZURLContext *)context {
  if ([[context.url.host lowercaseString] isEqualToString:@"MY-DOMAIN.com"]) {
    // Custom handle link here
    return NO;
  }
  // Let Braze handle links otherwise
  return YES;
}
```

{% endtab %}
{% endtabs %}

Para más información, consulta [`BrazeDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate).


