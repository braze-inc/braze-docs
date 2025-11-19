{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Uso de Google Tag Manager para Swift

En el siguiente ejemplo, una aplicación de streaming de música quiere registrar diferentes eventos a medida que los usuarios escuchan canciones. Mediante Google Tag Manager para iOS, pueden controlar qué proveedores externos de Braze reciben este evento y crear etiquetas específicas para Braze.

### Paso 1: Crear un desencadenante para eventos personalizados

Los eventos personalizados se registran con `actionType` configurado en `logEvent`. En este ejemplo, el proveedor de etiquetas personalizadas Braze espera que el nombre del evento personalizado se configure mediante `eventName`.

Primero, crea un desencadenante que busque un `eventName` que sea igual a `played song`.

![Un desencadenante personalizado en Google Tag Manager configurado para desencadenar algunos eventos cuando "eventName" es igual a "canción reproducida".]({% image_buster /assets/img/android_google_tag_manager/gtm_android_trigger.png %})

A continuación, crea una nueva etiqueta (también conocida como "llamada a función") e introduce la ruta de clase de tu [proveedor de etiquetas personalizado](#adding-ios-google-tag-provider) que se describe más adelante en este artículo. Esta etiqueta se desencadenará cuando registres el evento `played song`. Como `eventName` está configurado como `played song`, se utilizará como nombre de evento personalizado que se registra en Braze.

{% alert important %}
Cuando envíes un evento personalizado, configura `actionType` en `logEvent`, y establece un valor para `eventName` para que Braze reciba el nombre correcto del evento y la acción a realizar.
{% endalert %}

![Una etiqueta en Google Tag Manager con classpath y campos de par clave-valor. Esta etiqueta se configura para desencadenar con el desencadenante "canción reproducida" creado previamente.]({% image_buster /assets/img/android_google_tag_manager/gtm_android_function_call_tag.png %})

También puedes incluir argumentos adicionales de par clave-valor en la etiqueta, que se enviarán como propiedades del evento personalizadas a Braze. `eventName` y `actionType` no se ignorarán para las propiedades del evento personalizadas. En la siguiente etiqueta de ejemplo, introduce `genre`, que se definió utilizando una variable de etiqueta en Google Tag Manager y se obtuvo del evento personalizado registrado en la aplicación.

La propiedad del evento `genre` se envía a Google Tag Manager como una variable "Firebase - Parámetro de evento", ya que Google Tag Manager para iOS utiliza Firebase como capa de datos.

![Una variable en Google Tag Manager donde se añade "género" como parámetro de evento para la etiqueta "Braze - Evento de canción reproducida".]({% image_buster /assets/img/android_google_tag_manager/gtm_android_eventname_variable.png %})

Cuando un usuario reproduce una canción en la aplicación, registra un evento a través de Firebase y Google Tag Manager utilizando el nombre del evento de análisis de Firebase que coincida con el nombre desencadenante de la etiqueta, `played song`:

{% tabs %}
{% tab SWIFT %}

```swift
let parameters: [String: Any] = ["genre": "pop",
                                 "number of times listened": 42]
Analytics.logEvent("played song", parameters: parameters)
```

{% endtab %}
{% tab OBJETIVO-C %}

```obj-c
NSDictionary *parameters = @{@"genre" : @"pop",
                             @"number of times listened" : @42};
[FIRAnalytics logEventWithName:@"played song" parameters:parameters];
```

{% endtab %}
{% endtabs %}

### Paso 2: Registro de atributos personalizados

Los atributos personalizados se establecen a través de un `actionType` configurado en `customAttribute`. El proveedor de etiquetas personalizadas Braze espera que el atributo personalizado clave-valor se establezca a través de `customAttributeKey` y `customAttributeValue`:

{% tabs %}
{% tab SWIFT %}
```swift
let parameters: [String: Any] = ["customAttributeKey": "favoriteSong",
                                 "customAttributeValue": "Private Eyes"]
FIRAnalytics.logEvent(withName:"customAttribute", parameters: parameters)
```
{% endtab %}
{% tab OBJETIVO-C %}

```obj-c
NSDictionary *parameters = @{@"customAttributeKey" : @"favoriteSong",
                             @"customAttributeValue" : @"Private Eyes"};
[FIRAnalytics logEventWithName:@"customAttribute" parameters:parameters];
```

{% endtab %}

{% endtabs %}

### Paso 3: Llama a `changeUser()`

Las llamadas a `changeUser()` se realizan a través de un `actionType` configurado en `changeUser`. El proveedor de etiquetas personalizadas Braze espera que el ID de usuario Braze se establezca mediante un par clave-valor `externalUserId` dentro de tu etiqueta:

{% tabs %}
{% tab SWIFT %}
```swift
let parameters: [String: Any] = ["externalUserId": "favorite userId"]
Analytics.logEvent(withName:"changeUser", parameters: parameters)
```
{% endtab %}
{% tab OBJETIVO-C %}

```obj-c
NSDictionary *parameters = @{@"externalUserId" : userId};
[FIRAnalytics logEventWithName:@"changeUser" parameters:parameters];
```

{% endtab %}

{% endtabs %}

### Paso 4: Añadir un proveedor de etiquetas personalizado {#adding-ios-google-tag-provider}

Con las etiquetas y los desencadenantes configurados, también tendrás que implementar Google Tag Manager en tu aplicación para iOS, que puedes encontrar en la [documentación](https://developers.google.com/tag-manager/ios/v5/) de Google.

Una vez instalado Google Tag Manager en tu aplicación, añade un proveedor de etiquetas personalizado para llamar a los métodos del SDK de Braze en función de las etiquetas que hayas configurado en Google Tag Manager.

Asegúrate de anotar la "Ruta de clase" del archivo: es lo que introducirás cuando configures una etiqueta en la consola de [Google Tag Manager](https://tagmanager.google.com/).

Este ejemplo destaca una de las muchas formas en que puedes estructurar tu proveedor de etiquetas personalizado. En concreto, muestra cómo determinar a qué método del SDK de Braze llamar en función del par clave-valor `actionType` enviado desde la etiqueta GTM. Este ejemplo supone que has asignado la instancia de Braze como variable en el AppDelegate.

Los `actionType` admitidos en este ejemplo son `logEvent`, `customAttribute`, y `changeUser`, pero puede que prefieras cambiar la forma en que tu proveedor de etiquetas gestiona los datos de Google Tag Manager.
{% tabs %}
{% tab SWIFT %}

Añade el siguiente código a tu archivo `BrazeGTMTagManager.swift`.
```swift
import FirebaseAnalytics
import GoogleTagManager
import BrazeKit

let ActionTypeKey: String = "actionType"

// Custom Events
let LogEventAction: String = "logEvent"
let LogEventName: String = "eventName"

// Custom Attributes
let CustomAttributeAction: String = "customAttribute"
let CustomAttributeKey: String = "customAttributeKey"
let CustomAttributeValueKey: String = "customAttributeValue"

// Change User
let ChangeUserAction: String = "changeUser"
let ChangeUserExternalUserId: String = "externalUserId"

@objc(BrazeGTMTagManager)
final class BrazeGTMTagManager : NSObject, TAGCustomFunction {
  @objc func execute(withParameters parameters: [AnyHashable : Any]!) -> NSObject! {
    var parameters: [String : Any] = parameters as! [String : Any]
    guard let actionType: String = parameters[ActionTypeKey] as? String else {
      print("There is no Braze action type key in this call. Doing nothing.")
      return nil
    }
    parameters.removeValue(forKey: ActionTypeKey)
    if actionType == LogEventAction {
      logEvent(parameters: parameters)
    } else if actionType == CustomAttributeAction {
      logCustomAttribute(parameters: parameters)
    } else if actionType == ChangeUserAction {
      changeUser(parameters: parameters)
    }
    return nil
  }
  
  func logEvent(parameters: [String : Any]) {
    var parameters: [String : Any] = parameters
    guard let eventName: String = parameters[LogEventName] as? String else { return }
    parameters.removeValue(forKey: LogEventName)
    AppDelegate.braze?.logCustomEvent(name: eventName, properties: parameters)
  }
  
  func logCustomAttribute(parameters: [String: Any]) {
    guard let customAttributeKey = parameters[CustomAttributeKey] as? String else { return }
    let customAttributeValue = parameters[CustomAttributeValueKey]
    
    if let customAttributeValue = customAttributeValue as? String {
      AppDelegate.braze?.user.setCustomAttribute(key: customAttributeKey, value: customAttributeValue)
    } else if let customAttributeValue = customAttributeValue as? Date {
      AppDelegate.braze?.user.setCustomAttribute(key: customAttributeKey, value: customAttributeValue)
    } else if let customAttributeValue = customAttributeValue as? Double {
      AppDelegate.braze?.user.setCustomAttribute(key: customAttributeKey, value: customAttributeValue)
    } else if let customAttributeValue = customAttributeValue as? Bool {
      AppDelegate.braze?.user.setCustomAttribute(key: customAttributeKey, value: customAttributeValue)
    } else if let customAttributeValue = customAttributeValue as? Int {
      AppDelegate.braze?.user.setCustomAttribute(key: customAttributeKey, value: customAttributeValue)
    } else if let customAttibuteValue = customAttributeValue as? [String] {
      AppDelegate.braze?.user.setCustomAttributeArray(key: customAttributeKey, array: customAttibuteValue)
    }
  }
  
  func changeUser(parameters: [String: Any]) {
    guard let userId = parameters[ChangeUserExternalUserId] as? String else { return }
    AppDelegate.braze?.changeUser(userId: userId)
  }
}
```
{% endtab %}
{% tab OBJETIVO-C %}
Añade el siguiente código a tu archivo `BrazeGTMTagManager.h`:

```obj-c
@import Firebase;
@import GoogleTagManager;

@interface BrazeGTMTagManager : NSObject <TAGCustomFunction>

@end
```

Y añade el siguiente código a tu archivo `BrazeGTMTagManager.m`:

```obj-c
#import <Foundation/Foundation.h>
#import "BrazeGTMTagManager.h"
#import "BrazeKit"
#import "AppDelegate.h"

static NSString *const ActionTypeKey = @"actionType";

// Custom Events
static NSString *const LogEventAction = @"logEvent";
static NSString *const LogEventEventName = @"eventName";

// Custom Attributes
static NSString *const CustomAttributeAction = @"customAttribute";
static NSString *const CustomAttributeKey = @"customAttributeKey";
static NSString *const CustomAttributeValueKey = @"customAttributeValue";

// Change User
static NSString *const ChangeUserAction = @"changeUser";
static NSString *const ChangeUserExternalUserId = @"externalUserId";

@implementation BrazeGTMTagManager

- (NSObject *)executeWithParameters:(NSDictionary *)parameters {
  NSMutableDictionary *mutableParameters = [parameters mutableCopy];
  
  NSString *actionType = mutableParameters[ActionTypeKey];
  if (!actionType) {
    NSLog(@"There is no Braze action type key in this call. Doing nothing.", nil);
    return nil;
  }
  
  [mutableParameters removeObjectForKey:ActionTypeKey];
  
  if ([actionType isEqualToString:LogEventAction]) {
    [self logEvent:mutableParameters];
  } else if ([actionType isEqualToString:CustomAttributeAction]) {
    [self logCustomAttribute:mutableParameters];
  } else if ([actionType isEqualToString:ChangeUserAction]) {
    [self changeUser:mutableParameters];
  } else {
    NSLog(@"Invalid action type. Doing nothing.");
  }
  return nil;
}

- (void)logEvent:(NSMutableDictionary *)parameters {
  NSString *eventName = parameters[LogEventEventName];
  [parameters removeObjectForKey:LogEventEventName];
  [AppDelegate.braze logCustomEvent:eventName
                         properties:parameters];
}

- (void)logCustomAttribute:(NSMutableDictionary *)parameters {
  NSString *customAttributeKey = parameters[CustomAttributeKey];
  id customAttributeValue = parameters[CustomAttributeValueKey];
  
  if ([customAttributeValue isKindOfClass:[NSString class]]) {
    [AppDelegate.braze logCustomEvent:customAttributeKey
                           properties:parameters];
  } else if ([customAttributeValue isKindOfClass:[NSDate class]]) {
    [AppDelegate.braze.user setCustomAttributeWithKey:customAttributeKey
                                            dateValue:customAttributeValue];
  } else if ([customAttributeValue isKindOfClass:[NSNumber class]]) {
    if (strcmp([customAttributeValue objCType], [@(YES) objCType]) == 0) {
      [AppDelegate.braze.user setCustomAttributeWithKey:customAttributeKey
                                              boolValue:[(NSNumber *)customAttributeValue boolValue]];
    } else if (strcmp([customAttributeValue objCType], @encode(short)) == 0 ||
               strcmp([customAttributeValue objCType], @encode(int)) == 0 ||
               strcmp([customAttributeValue objCType], @encode(long)) == 0) {
      [AppDelegate.braze.user setCustomAttributeWithKey:customAttributeKey
                                               intValue:[(NSNumber *)customAttributeValue integerValue]];
    } else if (strcmp([customAttributeValue objCType], @encode(float)) == 0 ||
               strcmp([customAttributeValue objCType], @encode(double)) == 0) {
      [AppDelegate.braze.user setCustomAttributeWithKey:customAttributeKey
                                            doubleValue:[(NSNumber *)customAttributeValue doubleValue]];
    } else {
      NSLog(@"Could not map NSNumber value to Braze custom attribute:%@", customAttributeValue);
    }
  } else if ([customAttributeValue isKindOfClass:[NSArray class]]) {
    [AppDelegate.braze.user setCustomAttributeArrayWithKey:customAttributeKey
                                                     array:customAttributeValue];
  }
}

- (void)changeUser:(NSMutableDictionary *)parameters {
  NSString *userId = parameters[ChangeUserExternalUserId];
  [AppDelegate.braze changeUser:userId];
}

@end
```
{% endtab %}
{% endtabs %}
