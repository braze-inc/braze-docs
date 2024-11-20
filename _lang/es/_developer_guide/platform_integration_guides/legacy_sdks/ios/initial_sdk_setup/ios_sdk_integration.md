---
nav_title: Guía de integración de SDK (Opcional)
article_title: Guía de integración de Braze SDK para iOS (Opcional)
alias: "/ios_sdk/"
description: "Esta guía de integración de iOS te lleva paso a paso por las mejores prácticas de configuración a la hora de integrar por primera vez el SDK de iOS y sus componentes principales en tu aplicación. Esta guía te ayudará a crear un archivo de ayuda BrazeManager.swift."
page_order: 10
platform: iOS

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Guía de integración del SDK de Braze para iOS

> Esta guía opcional de integración de iOS te lleva paso a paso por las mejores prácticas de configuración al integrar por primera vez el SDK de iOS y sus componentes principales en tu aplicación. Esta guía te ayudará a crear un archivo de ayuda `BrazeManager.swift` que desacoplará cualquier dependencia del SDK Braze para iOS del resto de tu código de producción, dando como resultado un `import AppboyUI` en toda tu aplicación. Este enfoque limita los problemas que surgen de un exceso de importaciones del SDK, lo que facilita el seguimiento, la depuración y la modificación del código. 

{% alert important %}
Esta guía asume que ya has [añadido el SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/overview/) a tu proyecto Xcode.
{% endalert %}

## Resumen de la integración

Los siguientes pasos te ayudarán a crear un archivo de ayuda `BrazeManager` al que llame tu código de producción. Este archivo de ayuda se ocupará de todas las dependencias relacionadas con Braze añadiendo varias extensiones para los siguientes temas de integración que se enumeran. Cada tema incluirá pasos de pestañas horizontales y fragmentos de código tanto en Swift como en Objective-C. Ten en cuenta que los pasos de la tarjeta de contenido y los mensajes dentro de la aplicación no son necesarios para la integración si no piensas utilizar estos canales en tu aplicación.

- [Crea BrazeManager.swift](#create-brazemanagerswift)
- [Inicializar el SDK](#initialize-the-sdk)
- [Notificaciones push](#push-notifications)
- [Acceder a variables y métodos de usuario](#access-user-variables-and-methods)
- [Análisis de registros](#log-analytics)
- [Mensajes dentro de la aplicación (opcional)](#in-app-messages)
- [Tarjetas de contenido (opcional)](#content-cards)
- [Próximos pasos](#next-steps)

### Crear BrazeManager.swift

{% tabs local %}
{% tab Crear BrazeManager swift %}

##### Crear BrazeManager.swift
Para crear tu archivo `BrazeManager.swift`, crea un nuevo archivo Swift llamado _BrazeManager_ y añádelo a tu proyecto en la ubicación que desees. A continuación, sustituye `import Foundation` por `import AppboyUI` para SPM (`import Appboy_iOS_SDK` para CocoaPods) y luego crea una clase `BrazeManager` que se utilizará para alojar todos los métodos y variables relacionados con Braze. `Appboy_iOS_SDK`

{% alert note %}
- `BrazeManager` es una clase `NSObject` y no una estructura, por lo que puede ajustarse a delegados ABK como el `ABKInAppMessageUIDelegate`.
- El `BrazeManager` es una clase singleton por diseño, de modo que sólo se utilizará una instancia de esta clase. Esto se hace para proporcionar un punto de acceso unificado al objeto.
{% endalert %} 

1. Añade una variable estática llamada _compartida_ que inicialice la clase `BrazeManager`. Se garantiza que se inicie diferidamente solo una vez.
2. A continuación, añade una variable constante privada llamada _apiKey_ y establécela como clave de API-valor de tu espacio de trabajo en el panel de Braze.
3. Añade una variable privada computable llamada _appboyOptions_, que almacenará valores de configuración para el SDK. Por ahora estará vacía.

{% subtabs global %}
{% subtab Swift %}

```swift
class BrazeManager: NSObject {
  // 1
  static let shared = BrazeManager()
  
  // 2
  private let apikey = "YOUR-API-KEY"
  
  // 3
  private var appboyOptions: [String:Any] {
    return [:]
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
@implementation BrazeManager
 
// 1
+ (instancetype)shared {
    static BrazeManager *shared = nil;
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{
        shared = [[BrazeManager alloc] init];
        // Do any other initialisation stuff here
    });
    return shared;
}
 
// 2
- (NSString *)apiKey {
  return @"YOUR-API-KEY";
}
 
// 3
- (NSDictionary *)appboyOptions {
  return [NSDictionary dictionary];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Inicializar el SDK

{% tabs local %}
{% tab Paso 1: Inicializar SDK desde BrazeManager swift %}

##### Inicializar SDK desde BrazeManager.swift
A continuación, debes inicializar el SDK. Esta guía asume que ya has [añadido el SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/overview/) a tu proyecto Xcode. También debes tener el [punto final SDK de tu espacio de trabajo]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/completing_integration/#step-2-specify-your-data-cluster) y [`LogLevel`]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations/#braze-log-level) configurados en tu archivo `Info.plist` o en `appboyOptions`.

Añade el método `didFinishLaunchingWithOptions` del archivo `AppDelegate.swift` sin tipo de retorno en tu archivo `BrazeManager.swift`. Al crear un método similar en el archivo `BrazeManager.swift`, no habrá una declaración `import AppboyUI` en tu archivo `AppDelegate.swift`. 

A continuación, inicializa el SDK utilizando las variables `apiKey` y `appboyOptions` que acabas de declarar.

{% alert important %}
La inicialización debe hacerse en el hilo principal.
{% endalert %}

{% subtabs global %}
{% subtab Swift %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) {
  Appboy.start(withApiKey: apikey, in: application, withLaunchOptions: launchOptions, withAppboyOptions: appboyOptions)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  [Appboy startWithApiKey:[self apiKey] inApplication:application withLaunchOptions:launchOptions withAppboyOptions:[self appboyOptions]];
}
```
{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% tab Paso 2: Manejar la inicialización de Appboy %}

##### Maneja la inicialización de Appboy en la función AppDelegate.swift
A continuación, vuelve al archivo `AppDelegate.swift` y añade el siguiente fragmento de código en el método `didFinishLaunchingWithOptions` del AppDelegate para gestionar la inicialización de Appboy desde el archivo de ayuda `BrazeManager.swift`. Recuerda que no es necesario añadir una declaración `import AppboyUI` en `AppDelegate.swift`.

{% subtabs global %}
{% subtab Swift %}

```swift
func application(
  _ application: UIApplication, 
  didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
) -> Bool {
  // Override point for customization after application launch

  BrazeManager.shared.application(application, didFinishLaunchingWithOptions: launchOptions)

  return true
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Override point for customization after application launch
 
  [[BrazeManager shared] application:application didFinishLaunchingWithOptions:launchOptions];
   
  return YES;
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
Procede a compilar tu código y a ejecutar tu aplicación.<br><br>En este punto, el SDK debería estar funcionando. En tu panel, observa que se están registrando las sesiones antes de seguir avanzando.
{% endalert %}

### Notificaciones push

{% tabs local %}
{% tab Paso 1: Añadir certificado push %}

##### Añadir certificado push

Navega a tu espacio de trabajo existente en el panel de Braze. En **Configuración de notificaciones push**, sube tu archivo de certificado push a tu panel de Braze y guárdalo. 

![]({% image_buster /assets/img/ios_sdk/ios_sdk2.png %}){: style="max-width:60%;"}

{% endtab %}
{% tab Paso 2: Registro para notificaciones %}

{% alert important %}
¡No te pierdas el punto de control dedicado al final de este paso!
{% endalert %}

##### Registro para notificaciones push

A continuación, regístrate para recibir notificaciones push. Esta guía asume que has [configurado correctamente tus credenciales push]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/) en tu portal de desarrollador de Apple y en tu proyecto Xcode. 

El código para registrar las notificaciones push se añadirá en el método `didFinishLaunching...` del archivo `BrazeManager.swift`. Tu código de inicialización debería acabar teniendo el siguiente aspecto:

1. Configura los contenidos para solicitar autorización para interactuar con el usuario. Estas opciones se indican a modo de ejemplo.
2. Solicita autorización para enviar notificaciones push a tus usuarios. La respuesta del usuario para permitir o denegar las notificaciones push se sigue en la variable `granted`.
3. Reenvía los resultados de la autorización push a Braze después de que el usuario interactúe con la solicitud de notificación.
4. Inicia el proceso de registro con los APN; esto debe hacerse en el hilo principal. Si el registro tiene éxito, la aplicación llama al método `didRegisterForRemoteNotificationsWithDeviceToken` de tu objeto `AppDelegate`. 

{% subtabs global %}
{% subtab Swift %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions:[UIApplication.LaunchOptionsKey:Any]?) {
  Appboy.start(withAPIKey: apikey, in: application, withLaunchOptions: launchOptions, withAppboyOptions: appboyOptions)
  // 1 
  let options: UNAuthorizationOptions = [.alert, .sound, .badge]
  // 2 
  UNUserNotificationCenter.current().requestAuthorization(option: options) { (granted, error) in
  // 3 
    Appboy.sharedInstance()?.pushAuthorization(fromUserNotificationCenter: granted)
  }
  
  // 4 
  UIApplications.shared.registerForRemoteNotificiations()
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  [Appboy startWithApiKey:[self apiKey] inApplication:application withLaunchOptions:launchOptions withAppboyOptions:[self appboyOptions]];
   
  // 1
  UNAuthorizationOptions options = (UNAuthorizationOptionSound | UNAuthorizationOptionAlert | UNAuthorizationOptionBadge);
   
  // 2
  [[UNUserNotificationCenter currentNotificationCenter] requestAuthorizationWithOptions:options completionHandler:^(BOOL granted, NSError * _Nullable error) {
  // 3
    [[Appboy sharedInstance] pushAuthorizationFromUserNotificationCenter:granted];
  }];
 
  // 4
  [[UIApplication sharedApplication] registerForRemoteNotifications];
}
```
{% endsubtab %}
{% endsubtabs %}

{% alert checkpoint %}
Procede a compilar tu código y a ejecutar tu aplicación.
- En tu aplicación, confirma que se te solicitan notificaciones push antes de seguir avanzando.
- Si no te lo pide, prueba a borrar y volver a instalar la aplicación para asegurarte de que el aviso de notificación push no aparecía antes.

Observa que se te solicitan notificaciones push antes de seguir avanzando.
{% endalert %}

{% endtab %}
{% tab Paso 3: Métodos de avance %}

##### Métodos de notificación push de avance

A continuación, reenvía los métodos de notificación push del sistema de `AppDelegate.swift` a `BrazeManager.swift` para que los gestione el SDK Braze para iOS.

###### Paso 1: Crear extensión para código de notificación push

Crea una extensión para tu código de notificación push en tu archivo `BrazeManager.swift` para que se lea de forma más organizada en cuanto a la finalidad que se persigue en el archivo de ayuda, así

1. Siguiendo el patrón de no incluir una declaración `import AppboyUI` en tu `AppDelegate`, manejaremos los métodos de notificaciones push en el archivo `BrazeManager.swift`. Los tokens del dispositivo del usuario deberán pasarse a Braze desde el método `didRegisterForRemote...`. Este método es necesario para implementar notificaciones push silenciosas. A continuación, añade el mismo método del `AppDelegate` en tu clase `BrazeManager`.
2. Añade la siguiente línea dentro del método para registrar el token del dispositivo en Braze. Esto es necesario para que Braze asocie el token al dispositivo actual. 

{% subtabs global %}
{% subtab Swift %}

```swift
// MARK - Push Notifications
extension BrazeManager {
  // 1 
  func application(
    _ application: UIApplication,
    didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data
  ) {
    // 2 
    Appboy.sharedInstance().?registerDeviceToken(deviceToken)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
// MARK - Push Notifications
// 1
- (void)application:(UIApplication *)application didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken {
  // 2
  [[Appboy sharedInstance] registerDeviceToken:deviceToken];
}
```
{% endsubtab %}
{% endsubtabs %}

###### Paso 2: Soporte para notificaciones remotas
En la pestaña **Firma y capacidades**, añade la compatibilidad con **Modos en segundo plano** y selecciona **Notificaciones remotas** para empezar a admitir notificaciones push remotas originadas en Braze.<br><br>![Firma y Capacidades]({% image_buster /assets/img/ios_sdk/ios_sdk3.png %})

###### Paso 3: Gestión de notificaciones remotas
El SDK de Braze puede gestionar notificaciones push remotas que se originen en Braze. Reenvía las notificaciones remotas a Braze; el SDK ignorará automáticamente las notificaciones push que no procedan de Braze. Añade el siguiente método a tu archivo `BrazeManager.swift` en la extensión de notificaciones push.

{% subtabs global %}
{% subtab Swift %}
```swift
func application(
  _ application: UIApplication, 
  didReceiveRemoteNotification userInfo: [AnyHashable : Any], 
  fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void
) {
  Appboy.sharedInstance()?.register(
    application, 
    didReceiveRemoteNotification: userInfo, 
    fetchCompletionHandler: completionHandler
  )
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult))completionHandler {
  [[Appboy sharedInstance] registerApplication:application didReceiveRemoteNotification:userInfo fetchCompletionHandler:completionHandler];
}
```
{% endsubtab %}
{% endsubtabs %}

###### Paso 4: Reenvío de respuestas de notificación

El SDK de Braze puede gestionar la respuesta de las notificaciones push que se originan en Braze. Reenvía la respuesta de las notificaciones a Braze; el SDK ignorará automáticamente las respuestas de las notificaciones push que no se originen en Braze. Añade el siguiente método a tu archivo `BrazeManager.swift`:

{% subtabs global %}
{% subtab Swift %}

```swift
func userNotificationCenter(
  _ center: UNUserNotificationCenter, 
  didReceive response: UNNotificationResponse, 
  withCompletionHandler completionHandler: @escaping () -> Void
) {
  Appboy.sharedInstance()?.userNotificationCenter(
    center, 
    didReceive: response, 
    withCompletionHandler: completionHandler
  )
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)userNotificationCenter:(UNUserNotificationCenter *)center
didReceiveNotificationResponse:(UNNotificationResponse *)response 
         withCompletionHandler:(void (^)(void))completionHandler {
  [[Appboy sharedInstance] userNotificationCenter:center 
                   didReceiveNotificationResponse:response 
                            withCompletionHandler:completionHandler];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
Procede a compilar tu código y a ejecutar tu aplicación. <br><br>Prueba a enviarte una notificación push desde el panel de Braze y observa que se registran los análisis de las notificaciones push antes de seguir avanzando.
{% endalert %}

### Acceder a variables y métodos de usuario

{% tabs local %}
{% tab Crear variables y métodos de usuario %}

##### Crear variables y métodos de usuario

A continuación, querrás acceder fácilmente a las variables y métodos de `ABKUser`. Crea una extensión para tu código de usuario en el archivo `BrazeManager.swift` para que se lea de forma más organizada qué propósito tiene en el archivo de ayuda, de esta forma:

1. Un objeto `ABKUser` representa a un usuario conocido o anónimo en tu aplicación iOS. Añade una variable calculada para recuperar la `ABKUser`; esta variable se reutilizará para recuperar variables sobre el usuario.
2. Consulta la variable de usuario para acceder fácilmente a `userId`. Entre otras variables, el objeto `ABKUser` es responsable de (`firstName`, `lastName`, `phone`, `homeCity`, etc.)
3. Configura el usuario llamando a `changeUser()` con un `userId` correspondiente.

{% subtabs global %}
{% subtab Swift %}

```swift
// MARK: - User
extension BrazeManager {
  // 1
  var user: ABKUser? {
    return Appboy.sharedInstance()?.user
  }

  // 2 
  var userId: String? {
    return user?.userID
  }

  // 3
  func changeUser(_ userId: String) {
    Appboy.sharedInstance()?.changeUser(userId)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
// MARK: - User
  // 1
- (ABKUser *)user {
  return [[Appboy sharedInstance] user];
}
   
   // 2 
- (NSString *)userId {
  return [self user].userID;
}
 
  // 3
- (void)changeUser:(NSString *)userId {
  [[Appboy sharedInstance] changeUser:userId];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
Procede a compilar tu código y a ejecutar tu aplicación.<br><br>Intenta identificar a los usuarios que se han registrado correctamente. Asegúrate de que comprendes bien qué es y qué no es un identificador de usuario apropiado. <br><br>En tu panel, observa que el identificador de usuario esté registrado antes de seguir avanzando.
{% endalert %} 

### Análisis de registros

{% tabs local %}
{% tab Paso 1: Eventos personalizados %}

##### Crear método de evento personalizado de registro

Basándote en el siguiente método del SDK de Braze `logCustomEvent`, crea un método de correspondencia. 

**Método de referencia `logCustomEvent` de Braze**<br>
Esto es así porque solo el archivo `BrazeManager.swift` puede acceder directamente a los métodos del SDK de Braze para iOS. Por lo tanto, al crear un método coincidente, el resultado es el mismo y se realiza sin necesidad de depender directamente del SDK Braze iOS en tu código de producción.

```
open func logCustomEvent(_ eventName: String, withProperties properties: [AnyHashable : Any]?)
```

**Método de emparejamiento**<br>
Registra en Braze los eventos personalizados del objeto `Appboy`. `Properties` es un parámetro opcional con valor predeterminado nulo. No es necesario que los eventos personalizados tengan propiedades, pero sí que tengan un nombre. 

{% subtabs global %}
{% subtab Swift %}
```swift
func logCustomEvent(_ eventName: String, withProperties properties: [AnyHashable: Any]? = nil) {
  Appboy.sharedInstance()?.logCustomEvent(eventName, withProperties: properties)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)logCustomEvent:(NSString *)eventName withProperties:(nullable NSDictionary *)properties {
  [[Appboy sharedInstance] logCustomEvent:eventName withProperties:properties];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Paso 2: Atributos personalizados %}

##### Crear método de atributos personalizados de registro 

El SDK puede registrar numerosos tipos como atributos personalizados. No es necesario crear métodos ayudantes para cada tipo de valor que se pueda establecer. En su lugar, sólo expone un método que pueda filtrar hasta el valor adecuado.

```
- (BOOL)setCustomAttributeWithKey:(NSString *)key andBOOLValue:(BOOL)value; 
- (BOOL)setCustomAttributeWithKey:(NSString *)key andIntegerValue:(NSIntenger)value; 
- (BOOL)setCustomAttributeWithKey:(NSString *)key andDoubleValue:(double)value; 
- (BOOL)setCustomAttributeWithKey:(NSString *)key andStringValue:(NSString *)value; 
- (BOOL)setCustomAttributeWithKey:(NSString *)key andDateValue:(NSDate *)value;
```

Los atributos personalizados se registran desde el objeto `ABKUser`. 

Crea **un método** que pueda englobar todos los tipos disponibles que se pueden establecer para un atributo. Añade este método en tu archivo `BrazeManager.swift` en la extensión de análisis. Esto puede hacerse filtrando los tipos de atributos personalizados válidos y llamando al método asociado con el tipo coincidente.

- El parámetro `value` es un tipo genérico que se ajusta al protocolo `Equatable`. Esto se hace explícitamente, de modo que, si el tipo no es el que espera el SDK de Braze para iOS, se producirá un error de compilación.
- Los parámetros `key` y `value` son parámetros opcionales que se desenvolverán condicionalmente en el método. Esta es solo una forma de garantizar que se pasen valores no nulos al SDK de Braze para iOS.

{% subtabs global %}
{% subtab Swift %}

```swift
func setCustomAttributeWithKey<T: Equatable>(_ key: String?, andValue value: T?) {
  guard let key = key, let value = value else { return }
  switch value.self {
  case let value as Date:
    user?.setCustomAttributeWithKey(key, andDateValue: value)
  case let value as Bool:
    user?.setCustomAttributeWithKey(key, andBOOLValue: value)
  case let value as String:
    user?.setCustomAttributeWithKey(key, andStringValue: value)
  case let value as Double:
    user?.setCustomAttributeWithKey(key, andDoubleValue: value)
  case let value as Int:
    user?.setCustomAttributeWithKey(key, andIntegerValue: value)
  default:
   return
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)setCustomAttributeWith:(NSString *)key andValue:(id)value {
  if ([value isKindOfClass:[NSDate class]]) {
    [[self user] setCustomAttributeWithKey:key andDateValue:value];
  } else if ([value isKindOfClass:[NSString class]]) {
    [[self user] setCustomAttributeWithKey:key andStringValue:value];
  } else if ([value isKindOfClass:[NSNumber class]]) {
    if (strcmp([value objCType], @encode(double)) == 0) {
      [[self user] setCustomAttributeWithKey:key andDoubleValue:[value doubleValue]];
    } else if (strcmp([value objCType], @encode(int)) == 0) {
      [[self user] setCustomAttributeWithKey:key andIntegerValue:[value integerValue]];
    } else if ([value boolValue]) {
      [[self user] setCustomAttributeWithKey:key andBOOLValue:[value boolValue]];
    }
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Paso 3: Compras %}

##### Crear método de compra de registro

A continuación, basándote en el siguiente método del SDK de Braze `logPurchase`, crea un método de correspondencia. 

**Método de referencia `logPurchase` de Braze**<br>
Esto es así porque solo el archivo `BrazeManager.swift` puede acceder directamente a los métodos del SDK de Braze para iOS. Por lo tanto, al crear un método coincidente, el resultado es el mismo y se realiza sin necesidad de depender directamente del SDK Braze iOS en tu código de producción. 

```
open func logPurchase(_ productIdentifier: String, inCurrency currency: String, atPrice price: NSDecimalNumber, withoutQuantity quantity: UInt)
```
**Método de emparejamiento**<br>
Registra las compras del objeto `Appboy` en Braze. El SDK tiene múltiples métodos para registrar las compras, y este es solo un ejemplo. Este método también se encarga de crear los objetos `NSDecimal` y `UInt`. Cómo quieras manejar esa parte depende de ti, lo proporcionado es sólo un ejemplo.

{% subtabs global %}
{% subtab Swift %}

```swift
func logPurchase(_ productIdentifier: String, inCurrency currency: String, atPrice price:
String, withQuantity quantity: Int) {

  Appboy.sharedInstance()?.logPurchase(productIdentifier, inCurrency: currency, atPrice: NSDecimalNumber(string: price), withQuantity: UInt(quantity))

}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)logPurchase:(NSString *)productIdentifier inCurrency:(nonnull NSString *)currencyCode atPrice:(nonnull NSDecimalNumber *)price withQuantity:(NSUInteger)quantity {
  [[Appboy sharedInstance] logPurchase:productIdentifier inCurrency:currencyCode atPrice:price withQuantity:quantity];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
Procede a compilar tu código y a ejecutar tu aplicación. <br><br>Prueba a registrar eventos personalizados.<br><br>En tu panel, observa que se registran los eventos personalizados antes de seguir avanzando.
{% endalert %}

### Mensajes dentro de la aplicación

{% tabs local %}
{% tab Paso 1: Cumplimiento con el Delegado %}

{% alert important %}
La siguiente sección de mensajes dentro de la aplicación no es necesaria para la integración si no piensas utilizar este canal en tu aplicación.
{% endalert %}

##### Conforme a ABKInAppMessageUIDelegate

A continuación, habilita el código de tu archivo `BrazeManager.swift` para que se ajuste a `ABKInAppMessageUIDelegate` y pueda manejar directamente los métodos asociados. 

El código para ajustarse al delegado se añadirá en los métodos `didFinishLaunching...` del archivo `BrazeManager.swift`. Tu código de inicialización debería tener este aspecto:

{% subtabs global %}
{% subtab swift %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) {
  Appboy.start(withApiKey: apiKey, in: application, withLaunchOptions: launchOptions, withAppboyOptions: appboyOptions)

  let options: UNAuthorizationOptions = [.alert, .sound, .badge]
  UNUserNotificationCenter.current().requestAuthorization(options: options) { (granted, error) in
    Appboy.sharedInstance()?.pushAuthorization(fromUserNotificationCenter: granted)
  }
  UIApplication.shared.registerForRemoteNotifications()

  Appboy.sharedInstance()?.inAppMessageController.inAppMessageUIController?.setInAppMessageUIDelegate?(self)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  [Appboy startWithApiKey:[self apiKey] inApplication:application withLaunchOptions:launchOptions withAppboyOptions:[self appboyOptions]];
   
  UNAuthorizationOptions options = (UNAuthorizationOptionSound | UNAuthorizationOptionAlert | UNAuthorizationOptionBadge);
  [[UNUserNotificationCenter currentNotificationCenter] requestAuthorizationWithOptions:options completionHandler:^(BOOL granted, NSError * _Nullable error) {
    [[Appboy sharedInstance] pushAuthorizationFromUserNotificationCenter:granted];
  }];
  [[UIApplication sharedApplication] registerForRemoteNotifications];
   
  [[Appboy sharedInstance].inAppMessageController.inAppMessageUIController setInAppMessageUIDelegate:self];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Paso 2: Añadir métodos delegados %}

##### Añadir métodos delegados
A continuación, crea una extensión que se ajuste a `ABKInAppMessageUIDelegate`.

Añade el siguiente fragmento de código a la sección de análisis. Observa que el objeto `BrazeManager.swift` se establece como delegado; será aquí donde el archivo `BrazeManager.swift` gestione todos los métodos de `ABKInAppMessageUIDelegate`. 

{% alert important %}
El sitio `ABKInAppMessageUIDelegate` no incluye ningún método obligatorio, pero el siguiente es un ejemplo de uno.
{% endalert %}

{% subtabs global %}
{% subtab Swift %}
```swift
// MARK: - ABKInAppMessage UI Delegate
extension AppboyManager: ABKInAppMessageUIDelegate{
  func inAppMessageViewControllerWith(_ inAppMessage: ABKInAppMessage) -> ABKInAppMessageViewController {
    switch inAppMessage {
    case is ABKInAppMessageSlideup:
      return ABKInAppMessageSlideupViewController(inAppMessage: inAppMessage)
    case is ABKInAppMessageModal:
      return ABKInAppMessageModalViewController(inAppMessage: inAppMessage)
    case is ABKInAppMessageFull:
      return ABKInAppMessageFullViewController(inAppMessage: inAppMessage)
    case is ABKInAppMessageHTML:
      return ABKInAppMessageHTMLViewController(inAppMessage: inAppMessage)
    default:
      return ABKInAppMessageViewController(inAppMessage: inAppMessage)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
// MARK: - ABKInAppMessage UI Delegate
- (ABKInAppMessageViewController *)inAppMessageViewControllerWithInAppMessage:(ABKInAppMessage *)inAppMessage {
  if ([inAppMessage isKindOfClass:[ABKInAppMessageSlideup class]]) {
    return [[ABKInAppMessageSlideupViewController alloc] initWithInAppMessage:inAppMessage];
  } else if ([inAppMessage isKindOfClass:[ABKInAppMessageModal class]]) {
    return [[ABKInAppMessageModalViewController alloc] initWithInAppMessage:inAppMessage];
  } else if ([inAppMessage isKindOfClass:[ABKInAppMessageFull class]]) {
    return [[ABKInAppMessageFullViewController alloc] initWithInAppMessage:inAppMessage];
  } else if ([inAppMessage isKindOfClass:[ABKInAppMessageHTML class]]) {
    return [[ABKInAppMessageHTMLViewController alloc] initWithInAppMessage:inAppMessage];
  }
  return nil;
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
Procede a compilar tu código y a ejecutar tu aplicación. <br><br>Prueba a enviarte un mensaje dentro de la aplicación. <br><br>En el archivo `BrazeManager.swift`, establece un punto de interrupción en la entrada del método de ejemplo `ABKInAppMessageUIDelegate`. Envíate un mensaje dentro de la aplicación y confirma que se ha alcanzado el punto de interrupción antes de seguir avanzando.
{% endalert %}

### Tarjetas de contenido

{% tabs local %}
{% tab Crear variables y métodos de la tarjeta de contenido %}

{% alert important %}
La siguiente sección Tarjeta de contenido no es necesaria para la integración si no piensas utilizar este canal en tu aplicación.
{% endalert %}

##### Crear variables y métodos de la tarjeta de contenido

Habilita tu código de producción para mostrar el controlador de vista de las tarjetas de contenido sin necesidad de sentencias `import AppboyUI` innecesarias. 

Crea una extensión para el código de tus tarjetas de contenido en tu archivo `BrazeManager.swift`, para que se lea de forma más organizada qué propósito tiene en el archivo de ayuda, como por ejemplo

1. Visualiza la página `ABKContentCardsTableViewController`. Un `navigationController` opcional es el único parámetro necesario para presentar o ver como push nuestro controlador de vista.
2. Inicializa un objeto `ABKContentCardsTableViewController` y, opcionalmente, cambia el título. También debes añadir el controlador de vista inicializado a la pila de navegación.

{% subtabs global %}
{% subtab Swift %}
```swift
// MARK: - Content Cards
extension BrazeManager {

  // 1 
  func displayContentCards(navigationController: UINavigationController?) {
      
    // 2 
    let contentCardsVc = ABKContentCardsTableViewController()
    contentCardsVc.title = "Content Cards"
    navigationController?.pushViewController(contentCardsVc, animated: true)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
// MARK: - Content Cards
  // 1
- (void)displayContentCards:(UINavigationController *)navigationController {
  // 2
  ABKContentCardsTableViewController *contentCardsVc = [[ABKContentCardsTableViewController alloc] init];
  contentCardsVc.title = @"Content Cards";
  [navigationController pushViewController:contentCardsVc animated:YES];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
Procede a compilar tu código y a ejecutar tu aplicación.<br><br>Prueba a mostrar el `ABKContentCardsTableViewController` en tu aplicación antes de seguir avanzando.
{% endalert %}

## Próximos pasos

¡Enhorabuena! ¡Has completado esta guía de buenas prácticas de integración! Puedes encontrar un archivo de ayuda de ejemplo `BrazeManager` en [GitHub](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/BrazeManager.swift).

Ahora que has desacoplado cualquier dependencia del SDK Braze para iOS del resto de tu código de producción, consulta algunas de nuestras guías opcionales de implementación avanzada:
- [Guía de implementación de notificaciones push avanzadas]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/implementation_guide/)
- [Guía avanzada de implementación de mensajes dentro de la aplicación]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/implementation_guide/)
- [Guía de implantación de la tarjeta de contenido avanzado]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/implementation_guide/)

