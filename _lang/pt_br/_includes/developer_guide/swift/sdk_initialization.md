{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Usando a inicialização por postergação

Você pode inicializar o SDK do Braze Swift de forma assíncrona e, ao mesmo tempo, garantir que o tratamento das notificações por push seja preservado. Isso pode ser útil quando for necessário configurar outros serviços antes de inicializar o SDK, como buscar dados de configuração de um servidor ou aguardar o consentimento do usuário.

### Considerações

Ao usar `Braze.prepareForDelayedInitialization(pushAutomation:)`, você está configurando o SDK para usar automaticamente os recursos de automação de notificações por push. Os métodos delegados do sistema que manipulam notificações por push não serão chamados para notificações por push originadas do Braze.

O SDK somente processará uma notificação por push do Braze e a ação resultante **depois** que o SDK for inicializado. Por exemplo, se um usuário tocar em uma notificação por push que abre um deep linking, o deep link só será aberto depois que a instância `Braze` for inicializada.

Se você precisar realizar um processamento adicional nas notificações por push do Braze, consulte [Assinatura de atualizações de notificações por push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#subscribing-to-push-notifications-updates). Lembre-se de que, para receber atualizações de notificações por push que foram enfileiradas anteriormente, você deve implementar o manipulador de inscrição diretamente após a inicialização do SDK.

### Etapa 1: Preparar o SDK

Por padrão, se um usuário final abrir a notificação por push enquanto o app estiver em um estado finalizado, a notificação por push não poderá ser processada antes que o SDK seja inicializado.

A partir do [Braze Swift SDK versão 10.1.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/10.1.0) e posteriores, você pode lidar com isso usando o método auxiliar estático: [Braze.prepareForDelayedInitialization(pushAutomation:)](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/preparefordelayedinitialization(pushautomation:)). Esse método preparará o SDK para a inicialização por postergação, configurando o sistema de automação push.

Antes de o SDK ser inicializado, todas as notificações por push originadas do Braze serão capturadas e colocadas em uma fila. Depois que o SDK for inicializado, essas notificações por push serão processadas pelo SDK. Esse método deve ser chamado o mais cedo possível no ciclo de vida do aplicativo, dentro ou antes do método `application(_:didFinishLaunchingWithOptions:)` do seu `AppDelegate`.

{% alert note %}
O SDK do Swift não captura notificações por push que não sejam do Braze - elas continuarão a ser tratadas pelos métodos delegados do sistema.
{% endalert %}

{% tabs %}
{% tab SWIFT %}
{% subtabs local %}
{% subtab UIKit %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
  // Prepare the SDK for delayed initialization
  Braze.prepareForDelayedInitialization()

  // ... Additional non-Braze setup code

  return true
}
```
{% endsubtab %}

{% subtab SwiftUI %}
Os aplicativos SwiftUI exigem a implementação do wrapper da propriedade [@UIApplicationDelegateAdaptor](https://developer.apple.com/documentation/swiftui/uiapplicationdelegateadaptor) para chamar o método `prepareForDelayedInitialization()`.

```swift
@main
struct MyApp: App {
  @UIApplicationDelegateAdaptor var appDelegate: AppDelegate

  var body: some Scene {
    WindowGroup {
      ContentView()
    }
  }
}

class AppDelegate: NSObject, UIApplicationDelegate {
  
  func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil) -> Bool {
    // Prepare the SDK for delayed initialization
    Braze.prepareForDelayedInitialization()

    // ... Additional non-Braze setup code

    return true
  }
  
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Objective C %}
```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Prepare the SDK for delayed initialization
  [Braze prepareForDelayedInitialization];
  
  // ... Additional non-Braze setup code

  return YES;
}

```
{% endtab %}
{% endtabs %}

{% alert note %}
[Braze.prepareForDelayedInitialization(pushAutomation:)](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/preparefordelayedinitialization(pushautomation:)) recebe um parâmetro opcional `pushAutomation` que representa a configuração de automação para notificações por push. Quando [Braze.Configuration.Push.Automation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.class) é `nil`, todos os recursos de automação são ativados, exceto a solicitação de autorização no lançamento.
{% endalert %}

### Etapa 2: Inicializar o SDK

Depois de preparar o SDK para a inicialização por postergação, você pode inicializá-lo de forma assíncrona a qualquer momento no futuro. Em seguida, o SDK processará todos os eventos de notificações por push enfileirados originados do Braze.

Para inicializar o SDK do Braze, siga o [processo padrão de inicialização do SDK do Swift]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sdk_integration/#step-2-update-your-app-delegate).

## Usando o Google Tag Manager

O Braze Swift SDK pode ser inicializado e controlado por tags configuradas no Google Tag Manager.

No exemplo a seguir, um app de streaming de música deseja registrar diferentes eventos à medida que os usuários ouvem as músicas. Usando o Google Tag Manager para iOS, eles podem controlar quais dos fornecedores terceirizados do Braze recebem esse evento e criar tags específicas para o Braze.

### Etapa 1: Criar um disparo para eventos personalizados

Os eventos personalizados são registrados com `actionType` definido como `logEvent`. Neste exemplo, o provedor de tag personalizada do Braze está esperando que o nome do evento personalizado seja definido usando `eventName`.

Primeiro, crie um disparador que procure um `eventName` que seja igual a `played song`.

![Um gatilho personalizado no Google Tag Manager definido para disparar em alguns eventos quando "eventName" for igual a "played song".]({% image_buster /assets/img/android_google_tag_manager/gtm_android_trigger.png %})

Em seguida, crie uma nova tag (também conhecida como "Chamada de função") e insira a jornada da classe de seu [provedor de tag personalizado](#adding-ios-google-tag-provider) descrito mais adiante neste artigo. Essa tag será disparada quando for registrado o evento `played song`. Como `eventName` está definido como `played song`, ele será usado como o nome do evento personalizado que é registrado no Braze.

{% alert important %}
Ao enviar um evento personalizado, defina `actionType` como `logEvent` e defina um valor para `eventName` para que o Braze receba o nome correto do evento e a ação a ser tomada.
{% endalert %}

![Uma tag no Google Tag Manager com classpath e campos de par de valores chave. Esta tag está configurada para disparar com o gatilho "música tocada" criado anteriormente.]({% image_buster /assets/img/android_google_tag_manager/gtm_android_function_call_tag.png %})

Você também pode incluir argumentos adicionais de pares de valores-chave na tag, que serão enviados como propriedades de eventos personalizados para o Braze. `eventName` e `actionType` não serão ignorados nas propriedades de eventos personalizados. Na tag do exemplo a seguir, passe em `genre`, que foi definida usando uma variável de tag no Google Tag Manager e originada do evento personalizado registrado no app.

A propriedade do evento `genre` é enviada ao Google Tag Manager como uma variável "Firebase - Event Parameter", pois o Google Tag Manager para iOS usa o Firebase como camada de dados.

![Uma variável no Google Tag Manager onde "genre" é adicionado como um parâmetro de evento para a tag "Braze - Evento de Música Tocada".]({% image_buster /assets/img/android_google_tag_manager/gtm_android_eventname_variable.png %})

Quando um usuário reproduzir uma música no app, registre um evento no Firebase e no Google Tag Manager usando o nome do evento de análise de dados do Firebase que corresponda ao nome do disparo da tag, `played song`:

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

### Etapa 2: Registrar atributos personalizados

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

### Etapa 3: Chamada `changeUser()`

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

### Etapa 4: Adicionar um provedor de tag personalizado {#adding-ios-google-tag-provider}

Com as tags e os disparadores configurados, você também precisará implementar o Google Tag Manager em seu app para iOS, o que pode ser encontrado na [documentação](https://developers.google.com/tag-manager/ios/v5/) do Google.

Depois que o Google Tag Manager estiver instalado em seu app, adicione um provedor de tag personalizado para chamar os métodos do Braze SDK com base nas tags que você configurou no Google Tag Manager.

Não se esqueça de notar o "Class Path" (caminho da classe) para o arquivo - é isso que você digitará ao configurar uma tag no console do [Google Tag Manager](https://tagmanager.google.com/).

Este exemplo destaca uma das muitas maneiras de estruturar seu provedor de tags personalizadas. Especificamente, ele mostra como determinar qual método do Braze SDK deve ser chamado com base no par de valores-chave `actionType` enviado pela tag GTM. Este exemplo pressupõe que você atribuiu a instância da Braze como uma variável no AppDelegate.

Os `actionType` suportados neste exemplo são `logEvent`, `customAttribute` e `changeUser`, mas você pode preferir alterar a forma como seu provedor de tags trata os dados do Google Tag Manager.
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
