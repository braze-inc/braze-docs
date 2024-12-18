---
nav_title: Google Tag Manager
article_title: Google Tag Manager para iOS
platform: iOS
page_order: 7
description: "Este artículo explica cómo inicializar, configurar e implementar Google Tag Manager en tu aplicación para iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Google Tag Manager para iOS

## Inicializar el SDK {#initializing-ios-google-tag-provider}

El SDK Braze para iOS puede inicializarse y controlarse mediante etiquetas configuradas en [Google Tag Manager](https://tagmanager.google.com/).

Antes de utilizar Google Tag Manager, asegúrate de seguir primero nuestra [configuración inicial del SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/).

## Configurar tu Google Tag Manager {#configuring-ios-google-tag-manager}

En este ejemplo, haremos como si fuéramos una aplicación de streaming de música que quiere registrar diferentes eventos a medida que los usuarios escuchan canciones. Mediante Google Tag Manager para iOS, podemos controlar cuáles de nuestros proveedores externos reciben este evento y crear etiquetas específicas para Braze.

### Eventos personalizados

Los eventos personalizados se registran con `actionType` configurado en `logEvent`. El proveedor de etiquetas personalizadas Braze de nuestro ejemplo espera que el nombre del evento personalizado se configure mediante `eventName`.

Para empezar, crea un desencadenador que busque un "Nombre de evento" que sea igual a `played song`

![Un desencadenante personalizado en Google Tag Manager configurado para desencadenar algunos eventos cuando "nombre del evento" es igual a "canción reproducida".]({% image_buster /assets/img/android_google_tag_manager/gtm_android_trigger.png %})

A continuación, crea una nueva etiqueta ("Llamada a función") e introduce la ruta de clase de tu [proveedor de etiquetas personalizado](#adding-ios-google-tag-provider) que se describe más adelante en este artículo. 

Esta etiqueta se desencadenará cuando registres el evento `played song` que acabamos de crear. 

En los parámetros personalizados (par clave-valor) de nuestra etiqueta de ejemplo, hemos establecido `eventName` en `played song`, que será el nombre del evento personalizado registrado en Braze.

{% alert important %}
Cuando envíes un evento personalizado, establece `actionType` en `logEvent`, y fija un valor para `eventName` como se muestra en el siguiente ejemplo. 

El proveedor de etiquetas personalizadas de nuestro ejemplo utilizará estas claves para determinar qué acción realizar y qué nombre de evento enviar a Braze cuando reciba datos de Google Tag Manager.
{% endalert %}

![Una etiqueta en Google Tag Manager con classpath y campos de par clave-valor. Esta etiqueta se configura para desencadenar con el desencadenante "canción reproducida" creado previamente.]({% image_buster /assets/img/android_google_tag_manager/gtm_android_function_call_tag.png %})

También puedes incluir argumentos adicionales de par clave-valor en la etiqueta, que se enviarán como propiedades del evento personalizadas a Braze. `eventName` y `actionType` no se ignorarán para las propiedades del evento personalizadas. En la siguiente etiqueta de ejemplo, pasaremos `genre`, que se definió utilizando una variable de etiqueta en Google Tag Manager, procedente del evento personalizado que registramos en nuestra aplicación.

La propiedad del evento `genre` se envía a Google Tag Manager como una variable "Firebase - Parámetro de evento", ya que Google Tag Manager para iOS utiliza Firebase como capa de datos.

![Una variable en Google Tag Manager donde se añade "género" como parámetro de evento para la etiqueta "Braze - Evento de canción reproducida".]({% image_buster /assets/img/android_google_tag_manager/gtm_android_eventname_variable.png %})

Por último, cuando un usuario reproduzca una canción en nuestra aplicación, registraremos un evento a través de Firebase y Google Tag Manager utilizando el nombre del evento de análisis de Firebase que coincida con el nombre desencadenante de nuestra etiqueta, `played song`:

{% tabs %}
{% tab OBJETIVO-C %}

```obj-c
NSDictionary *parameters = @{@"genre" : @"pop",
                             @"number of times listened" : @42};
[FIRAnalytics logEventWithName:@"played song" parameters:parameters];
```

{% endtab %}
{% endtabs %}

### Registro de atributos personalizados

Los atributos personalizados se establecen a través de un `actionType` configurado en `customAttribute`. El proveedor de etiquetas personalizadas Braze espera que el atributo personalizado clave-valor se establezca a través de `customAttributeKey` y `customAttributeValue`:

{% tabs %}
{% tab OBJETIVO-C %}

```obj-c
NSDictionary *parameters = @{@"customAttributeKey" : @"favorite song",
                             @"customAttributeValue" : @"Private Eyes"};
[FIRAnalytics logEventWithName:@"customAttribute" parameters:parameters];
```

{% endtab %}
{% endtabs %}

### Llamada a changeUser

Las llamadas a `changeUser()` se realizan a través de un `actionType` configurado en `changeUser`. El proveedor de etiquetas personalizadas Braze espera que el ID de usuario Braze se establezca mediante un par clave-valor `externalUserId` dentro de tu etiqueta:

{% tabs %}
{% tab OBJETIVO-C %}

```obj-c
NSDictionary *parameters = @{@"externalUserId" : userId};
[FIRAnalytics logEventWithName:@"changeUser" parameters:parameters];
```

{% endtab %}
{% endtabs %}

## Proveedor de etiquetas personalizadas Braze SDK {#adding-ios-google-tag-provider}

Con las etiquetas y los desencadenantes configurados, también tendrás que implementar Google Tag Manager en tu aplicación para iOS, que puedes encontrar en la [documentación](https://developers.google.com/tag-manager/ios/v5/) de Google.

Una vez que Google Tag Manager esté instalado en tu aplicación, añade un proveedor de etiquetas personalizado para llamar a los métodos del SDK de Braze en función de las etiquetas que hayas configurado en Google Tag Manager. 

Asegúrate de anotar la "Ruta de clase" del archivo: es lo que introducirás cuando configures una etiqueta en la consola de [Google Tag Manager](https://tagmanager.google.com/).

Este ejemplo muestra una de las muchas formas de estructurar tu proveedor de etiquetas personalizado, en el que determinamos a qué método del SDK de Braze llamar en función del par clave-valor `actionType` enviado desde la etiqueta GTM.

Los `actionType` que hemos admitido en nuestro ejemplo son `logEvent`, `customAttribute`, y `changeUser`, pero puede que prefieras cambiar la forma en que tu proveedor de etiquetas gestiona los datos de Google Tag Manager.

Añade el siguiente código a tu archivo `BrazeGTMTagManager.h`:

{% tabs %}
{% tab OBJETIVO-C %}

```obj-c
@import Firebase;
@import GoogleTagManager;

@interface BrazeGTMTagManager : NSObject <TAGCustomFunction>

@end
```

{% endtab %}
{% endtabs %}

Y añade el siguiente código a tu archivo `BrazeGTMTagManager.m`:

{% tabs %}
{% tab OBJETIVO-C %}

```obj-c
#import <Foundation/Foundation.h>
#import "BrazeGTMTagManager.h"
#import "Appboy-iOS-SDK/AppboyKit.h"

static NSString *const ActionTypeKey = @"actionType";

// Custom Events
static NSString *const LogEventActionType = @"logEvent";
static NSString *const LogEventEventName = @"eventName";

// Custom Attributes
static NSString *const CustomAttributeActionType = @"customAttribute";
static NSString *const CustomAttributeKey = @"customAttributeKey";
static NSString *const CustomAttributeValueKey = @"customAttributeValue";

// Change User
static NSString *const ChangeUserActionType = @"changeUser";
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
  
  if ([actionType isEqualToString:LogEventActionType]) {
    [self logEvent:mutableParameters];
  } else if ([actionType isEqualToString:CustomAttributeActionType]) {
    [self logCustomAttribute:mutableParameters];
  } else if ([actionType isEqualToString:ChangeUserActionType]) {
    [self changeUser:mutableParameters];
  } else {
    NSLog(@"Invalid action type. Doing nothing.");
  }
  return nil;
}

- (void)logEvent:(NSMutableDictionary *)parameters {
  NSString *eventName = parameters[LogEventEventName];
  [parameters removeObjectForKey:LogEventEventName];
  [[Appboy sharedInstance] logCustomEvent:eventName withProperties:parameters];
}

- (void)logCustomAttribute:(NSMutableDictionary *)parameters {
  NSString *customAttributeKey = parameters[CustomAttributeKey];
  id customAttributeValue = parameters[CustomAttributeValueKey];
  
  if ([customAttributeValue isKindOfClass:[NSString class]]) {
    [[Appboy sharedInstance].user setCustomAttributeWithKey:customAttributeKey
                                             andStringValue:customAttributeValue];
  } else if ([customAttributeValue isKindOfClass:[NSDate class]]) {
    [[Appboy sharedInstance].user setCustomAttributeWithKey:customAttributeKey
                                               andDateValue:customAttributeValue];
  } else if ([customAttributeValue isKindOfClass:[NSNumber class]]) {
    if (strcmp([customAttributeValue objCType], [@(YES) objCType]) == 0) {
      [[Appboy sharedInstance].user setCustomAttributeWithKey:customAttributeKey
                                                 andBOOLValue:[(NSNumber *)customAttributeValue boolValue]];
    } else if (strcmp([customAttributeValue objCType], @encode(short)) == 0 ||
               strcmp([customAttributeValue objCType], @encode(int)) == 0 ||
               strcmp([customAttributeValue objCType], @encode(long)) == 0) {
      [[Appboy sharedInstance].user setCustomAttributeWithKey:customAttributeKey
                                              andIntegerValue:[(NSNumber *)customAttributeValue integerValue]];
    } else if (strcmp([customAttributeValue objCType], @encode(float)) == 0 ||
               strcmp([customAttributeValue objCType], @encode(double)) == 0) {
      [[Appboy sharedInstance].user setCustomAttributeWithKey:customAttributeKey
                                               andDoubleValue:[(NSNumber *)customAttributeValue doubleValue]];
    } else {
      NSLog(@"Could not map NSNumber value to Appboy custom attribute:%@", customAttributeValue);
    }
  } else if ([customAttributeValue isKindOfClass:[NSArray class]]) {
    [[Appboy sharedInstance].user setCustomAttributeArrayWithKey:customAttributeKey
                                                           array:customAttributeValue];
  }
}

- (void)changeUser:(NSMutableDictionary *)parameters {
  NSString *userId = parameters[ChangeUserExternalUserId];
  [[Appboy sharedInstance] changeUser:userId];
}

@end
```

{% endtab %}
{% endtabs %}

