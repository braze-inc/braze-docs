---
nav_title: Google Tag Manager
article_title: Google Tag Manager para iOS
platform: Swift
page_order: 3
description: "Este artigo ensina a inicializar, configurar e implementar o Google Tag Manager no Swift SDK."

---

# Google Tag Manager

> O Braze Swift SDK pode ser inicializado e controlado por tags configuradas no Google Tag Manager.

Como pré-requisito para essa implementação, sua integração do Swift SDK deve estar concluída.

## Configuração do Google Tag Manager {#configuring-ios-google-tag-manager}

Neste exemplo, vamos fingir que somos um app de streaming de música que deseja fazer o registro de diferentes eventos à medida que os usuários ouvem as músicas. Usando o Google Tag Manager para iOS, podemos controlar quais de nossos fornecedores terceirizados recebem esse evento e criar tags específicas para o Braze.

### Eventos personalizados

Os eventos personalizados são registrados com `actionType` definido como `logEvent`. O provedor de tag personalizada do Braze em nosso exemplo está esperando que o nome do evento personalizado seja definido usando `eventName`.

Para começar, crie um gatilho que procure um `eventName` que seja igual a `played song`.

![Um gatilho personalizado no Google Tag Manager definido para disparar em alguns eventos quando "eventName" for igual a "played song".]({% image_buster /assets/img/android_google_tag_manager/gtm_android_trigger.png %})

Em seguida, crie uma nova tag ("Function Call") e insira a jornada da classe de seu [provedor de tag personalizado](#adding-ios-google-tag-provider) descrito mais adiante neste artigo. 

Essa tag será disparada quando for registrado o evento `played song` que acabamos de criar. 

Nos parâmetros personalizados (pares de valores-chave) da nossa tag de exemplo, definimos `eventName` como `played song`, que será o nome do evento personalizado registrado no Braze.

{% alert important %}
Ao enviar um evento personalizado, defina `actionType` como `logEvent` e defina um valor para `eventName`, conforme mostrado no exemplo a seguir.
<br><br>
O provedor de tag personalizado em nosso exemplo usará essas chaves para determinar qual ação tomar e qual nome de evento enviar à Braze quando receber dados do Google Tag Manager.
{% endalert %}

![Uma tag no Google Tag Manager com classpath e campos de par de valores chave. Essa tag é definida para disparar com o acionador da "música tocada" criada anteriormente.]({% image_buster /assets/img/android_google_tag_manager/gtm_android_function_call_tag.png %})

Você também pode incluir argumentos adicionais de pares de valores-chave na tag, que serão enviados como propriedades de eventos personalizados para o Braze. `eventName` e `actionType` não serão ignorados nas propriedades de eventos personalizados. No exemplo de tag a seguir, passaremos `genre`, que foi definido usando uma variável de tag no Google Tag Manager, proveniente do evento personalizado que registramos em nosso app.

A propriedade do evento `genre` é enviada ao Google Tag Manager como uma variável "Firebase - Event Parameter", pois o Google Tag Manager para iOS usa o Firebase como camada de dados.

![Uma variável no Google Tag Manager em que o "gênero" é adicionado como um parâmetro de evento para a tag "Braze - Played Song Event".]({% image_buster /assets/img/android_google_tag_manager/gtm_android_eventname_variable.png %})

Por fim, quando um usuário reproduzir uma música em nosso app, registraremos um evento por meio do Firebase e do Google Tag Manager usando o nome do evento de análise de dados do Firebase que corresponde ao nome do disparo da nossa tag, `played song`:

{% tabs %}
{% tab SWIFT %}

```swift
let parameters: [String: Any] = ["genre": "pop",
                                 "number of times listened": 42]
Analytics.logEvent("played song", parameters: parameters)
```

{% endtab %}
{% tab OBJECTIVE C %}

```obj-c
NSDictionary *parameters = @{@"genre" : @"pop",
                             @"number of times listened" : @42};
[FIRAnalytics logEventWithName:@"played song" parameters:parameters];
```

{% endtab %}
{% endtabs %}

### Registro de atributos personalizados

Os atributos personalizados são definidos por meio de um `actionType` definido como `customAttribute`. O provedor de tag personalizada da Braze está esperando que o atributo personalizado chave-valor seja definido por meio de `customAttributeKey` e `customAttributeValue`:

{% tabs %}
{% tab SWIFT %}
```swift
let parameters: [String: Any] = ["customAttributeKey": "favoriteSong",
                                 "customAttributeValue": "Private Eyes"]
FIRAnalytics.logEvent(withName:"customAttribute", parameters: parameters)
```
{% endtab %}
{% tab OBJECTIVE C %}

```obj-c
NSDictionary *parameters = @{@"customAttributeKey" : @"favoriteSong",
                             @"customAttributeValue" : @"Private Eyes"};
[FIRAnalytics logEventWithName:@"customAttribute" parameters:parameters];
```

{% endtab %}

{% endtabs %}

### Chamada de changeUser

As chamadas para `changeUser()` são feitas por meio de um `actionType` definido como `changeUser`. O provedor de tags personalizadas do Braze espera que o ID de usuário do Braze seja definido por meio de um par de valores-chave `externalUserId` dentro da sua tag:

{% tabs %}
{% tab SWIFT %}
```swift
let parameters: [String: Any] = ["externalUserId": "favorite userId"]
Analytics.logEvent(withName:"changeUser", parameters: parameters)
```
{% endtab %}
{% tab OBJECTIVE C %}

```obj-c
NSDictionary *parameters = @{@"externalUserId" : userId};
[FIRAnalytics logEventWithName:@"changeUser" parameters:parameters];
```

{% endtab %}

{% endtabs %}

## Provedor de tags personalizadas do Braze SDK {#adding-ios-google-tag-provider}

Com as tags e os disparadores configurados, você também precisará implementar o Google Tag Manager em seu app para iOS, o que pode ser encontrado na [documentação](https://developers.google.com/tag-manager/ios/v5/) do Google.

Depois que o Google Tag Manager estiver instalado em seu app, adicione um provedor de tag personalizado para chamar os métodos do Braze SDK com base nas tags que você configurou no Google Tag Manager. 

Não se esqueça de notar o "Class Path" (caminho da classe) para o arquivo - é isso que você digitará ao configurar uma tag no console do [Google Tag Manager](https://tagmanager.google.com/).

Este exemplo mostra uma das muitas maneiras de estruturar seu provedor de tag personalizado, em que determinamos qual método do Braze SDK deve ser chamado com base no par de valores-chave `actionType` enviado pelo Google Tag Manager. Este exemplo pressupõe que você atribuiu a instância da Braze como uma variável no AppDelegate.

Os `actionType` suportados em nosso exemplo são `logEvent`, `customAttribute` e `changeUser`, mas você pode preferir alterar a forma como seu provedor de tag trata os dados do Google Tag Manager.
{% tabs %}
{% tab SWIFT %}

Adicione o seguinte código ao seu arquivo `BrazeGTMTagManager.swift`.
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
{% tab OBJECTIVO-C %}
Adicione o seguinte código ao seu arquivo `BrazeGTMTagManager.h`:

```obj-c
@import Firebase;
@import GoogleTagManager;

@interface BrazeGTMTagManager : NSObject <TAGCustomFunction>

@end
```

E adicione o seguinte código ao seu arquivo `BrazeGTMTagManager.m`:

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

