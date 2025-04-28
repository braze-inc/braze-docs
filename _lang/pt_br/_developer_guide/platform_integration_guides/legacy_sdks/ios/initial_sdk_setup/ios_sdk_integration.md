---
nav_title: Guia de integração de SDK (opcional)
article_title: Guia de integração do SDK do Braze para iOS (opcional)
alias: "/ios_sdk/"
description: "Este guia de integração do iOS leva você a uma jornada passo a passo sobre as práticas recomendadas de configuração ao integrar pela primeira vez o SDK do iOS e seus componentes principais em seu aplicativo. Este guia o ajudará a criar um arquivo auxiliar BrazeManager.swift."
page_order: 10
platform: iOS

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Guia de integração do SDK do Braze para iOS

> Este guia opcional de integração do iOS leva você a uma jornada passo a passo sobre as práticas recomendadas de configuração ao integrar pela primeira vez o SDK do iOS e seus componentes principais em seu aplicativo. Este guia o ajudará a criar um arquivo auxiliar `BrazeManager.swift` que desacoplará todas as dependências do SDK da Braze para iOS do restante do seu código de produção, resultando em um `import AppboyUI` em todo o seu aplicativo. Essa abordagem limita os problemas decorrentes do excesso de importações de SDK, facilitando o rastreamento, a depuração e a alteração do código. 

{% alert important %}
Este guia pressupõe que você já tenha [adicionado o SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/overview/) ao seu projeto Xcode.
{% endalert %}

## Visão geral da integração

As etapas a seguir o ajudam a criar um arquivo auxiliar `BrazeManager` para o qual seu código de produção faz chamadas. Esse arquivo auxiliar tratará de todas as dependências relacionadas ao Braze, adicionando várias extensões para os seguintes tópicos de integração listados. Cada tópico incluirá etapas de guias horizontais e trechos de código em Swift e Objective C. Observe que as etapas do cartão de conteúdo e da mensagem no app não são necessárias para a integração se você não planeja usar esses canais em seu aplicativo.

- [Criar BrazeManager.swift](#create-brazemanagerswift)
- [Inicializar o SDK](#initialize-the-sdk)
- [Notificações por push](#push-notifications)
- [Acessar variáveis e métodos do usuário](#access-user-variables-and-methods)
- [Análise de dados](#log-analytics)
- [Mensagens no app (opcional)](#in-app-messages)
- [Cartões de conteúdo (opcional)](#content-cards)
- [Próximas etapas](#next-steps)

### Criar BrazeManager.swift

{% tabs local %}
{% tab Criar o BrazeManager swift %}

##### Criar BrazeManager.swift
Para construir seu arquivo `BrazeManager.swift`, crie um novo arquivo Swift chamado _BrazeManager_ para adicionar ao seu projeto no local desejado. Em seguida, substitua `import Foundation` por `import AppboyUI` para SPM (`import Appboy_iOS_SDK` para CocoaPods) e crie uma classe `BrazeManager` que será usada para hospedar todos os métodos e variáveis relacionados à Braze. `Appboy_iOS_SDK`

{% alert note %}
- `BrazeManager` é uma classe `NSObject` e não um struct, portanto, pode estar em conformidade com os delegates ABK, como o `ABKInAppMessageUIDelegate`.
- O `BrazeManager` é uma classe singleton por padrão, de modo que apenas uma instância dessa classe será usada. Isso é feito para fornecer um ponto de acesso unificado ao objeto.
{% endalert %} 

1. Adicione uma variável estática chamada _shared_ que inicializa a classe `BrazeManager`. É garantido que isso seja iniciado de forma preguiçosa apenas uma vez.
2. Em seguida, adicione uma variável constante privada chamada _apiKey_ e defina-a como a chave de API de seu espaço de trabalho no dashboard da Braze.
3. Adicione uma variável computada privada chamada _appboyOptions_, que armazenará valores de configuração para o SDK. Ele ficará vazio por enquanto.

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

### Inicializar o SDK

{% tabs localização %}
{% tab Etapa 1: Inicializar o SDK a partir do swift do BrazeManager %}

##### Inicializar o SDK a partir de BrazeManager.swift
Em seguida, você deve inicializar o SDK. Este guia pressupõe que você já tenha [adicionado o SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/overview/) ao seu projeto Xcode. Você também deve ter seu [endpoint de SDK do espaço de trabalho]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/completing_integration/#step-2-specify-your-data-cluster) e [`LogLevel`]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations/#braze-log-level) definidos em seu arquivo `Info.plist` ou em `appboyOptions`.

Adicione o método `didFinishLaunchingWithOptions` do arquivo `AppDelegate.swift` sem um tipo de retorno em seu arquivo `BrazeManager.swift`. Ao criar um método semelhante no arquivo `BrazeManager.swift`, não haverá uma declaração `import AppboyUI` em seu arquivo `AppDelegate.swift`. 

Em seguida, inicialize o SDK usando suas variáveis recém-declaradas `apiKey` e `appboyOptions`.

{% alert important %}
A inicialização deve ser feita na thread principal.
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
{% tab Etapa 2: Manipular a inicialização do Appboy %}

##### Lidar com a inicialização do Appboy no AppDelegate.swift
Em seguida, volte ao arquivo `AppDelegate.swift` e adicione o seguinte trecho de código no método `didFinishLaunchingWithOptions` do AppDelegate para tratar da inicialização do Appboy no arquivo auxiliar `BrazeManager.swift`. Lembre-se de que não há necessidade de adicionar uma declaração `import AppboyUI` no site `AppDelegate.swift`.

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
Prossiga para compilar seu código e executar seu aplicativo.<br><br>Nesse ponto, o SDK deve estar funcionando. No seu dashboard, observe se as sessões estão sendo registradas antes de avançar mais.
{% endalert %}

### Notificações por push

{% tabs localização %}
{% tab Etapa 1: Adicionar certificado push %}

##### Adicionar certificado push

Navegue até seu espaço de trabalho existente no dashboard do Braze. Em **Push Notification Settings (Configurações de notificações por push** ), faça upload do arquivo de certificado push no dashboard do Braze e salve-o. 

![]({% image_buster /assets/img/ios_sdk/ios_sdk2.png %}){: style="max-width:60%;"}

{% endtab %}
{% tab Etapa 2: Registre-se para receber notificações %}

{% alert important %}
Não perca o ponto de controle dedicado no final dessa etapa!
{% endalert %}

##### Registre-se para receber notificações por push

Em seguida, registre-se para receber notificações por push. Este guia pressupõe que você tenha configurado [suas credenciais push corretamente]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/) no portal do desenvolvedor da Apple e no projeto Xcode. 

O código para registrar notificações por push será adicionado ao método `didFinishLaunching...` no arquivo `BrazeManager.swift`. Seu código de inicialização deve ser parecido com o seguinte:

1. Configure o conteúdo para solicitar autorização para interagir com o usuário. Essas opções estão listadas como exemplo.
2. Solicite autorização para enviar notificações por push aos seus usuários. A resposta do usuário para permitir ou negar notificações por push é rastreada na variável `granted`.
3. Encaminhe os resultados da autorização por push para o Braze depois que o usuário interagir com o prompt de notificação.
4. Inicie o processo de registro com APNs; isso deve ser feito no thread principal. Se o registro for bem-sucedido, o app chamará o método `didRegisterForRemoteNotificationsWithDeviceToken` do seu objeto `AppDelegate`. 

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
Prossiga para compilar seu código e executar seu aplicativo.
- No seu app, confirme se está sendo solicitado a receber notificações por push antes de prosseguir.
- Se não for solicitado, tente excluir e reinstalar o app para garantir que o aviso de notificação por push não tenha sido exibido anteriormente.

Observe se está sendo solicitado a receber notificações por push antes de avançar mais.
{% endalert %}

{% endtab %}
{% tab Etapa 3: Métodos avançados %}

##### Encaminhar métodos de notificação por push

Em seguida, encaminhe os métodos de notificações por push do sistema de `AppDelegate.swift` para `BrazeManager.swift` para serem tratados pelo SDK da Braze para iOS.

###### Etapa 1: Criar extensão para o código de notificação por push

Crie uma extensão para o seu código de notificação por push no arquivo `BrazeManager.swift` para que ele seja lido de forma mais organizada quanto à finalidade que está sendo atendida no arquivo auxiliar, da seguinte forma:

1. Seguindo o padrão de não incluir uma instrução `import AppboyUI` em seu arquivo `AppDelegate`, trataremos dos métodos de notificações por push no arquivo `BrazeManager.swift`. Os tokens de dispositivo do usuário precisarão ser passados para o Braze a partir do método `didRegisterForRemote...`. Esse método é necessário para implementar notificações por push silenciosas. Em seguida, adicione o mesmo método do site `AppDelegate` em sua classe `BrazeManager`.
2. Adicione a seguinte linha dentro do método para registrar o token do dispositivo no Braze. Isso é necessário para que a Braze associe o token ao dispositivo atual. 

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

###### Etapa 2: Suporte a notificações remotas
Na guia **Signing & Capabilities (Assinatura e recursos** ), adicione o suporte a **Background Modes (Modos em segundo plano** ) e selecione **Remote notifications (Notificações remotas** ) para iniciar seu suporte a notificações por push remotas originadas do Braze.<br><br>![Fazendo login e capacidades]({% image_buster /assets/img/ios_sdk/ios_sdk3.png %})

###### Etapa 3: Manuseio de notificações remotas
O SDK da Braze pode lidar com notificações por push remotas originadas da Braze. Encaminhe as notificações remotas para a Braze; o SDK ignorará automaticamente as notificações por push que não forem originadas na Braze. Adicione o seguinte método ao seu arquivo `BrazeManager.swift` na extensão de notificação por push.

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

###### Etapa 4: Encaminhar respostas de notificação

O SDK da Braze pode lidar com a resposta de notificações por push originadas na Braze. Encaminhe a resposta das notificações para a Braze; o SDK ignorará automaticamente as respostas das notificações por push que não forem originadas na Braze. Adicione o seguinte método ao seu arquivo `BrazeManager.swift`:

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
Prossiga para compilar seu código e executar seu aplicativo. <br><br>Tente enviar a si mesmo uma notificação por push a partir do dashboard do Braze e observe se as análises de dados estão sendo registradas a partir das notificações por push antes de avançar mais.
{% endalert %}

### Acessar variáveis e métodos do usuário

{% tabs localização %}
{% tab Criar variáveis e métodos do usuário %}

##### Criar variáveis e métodos de usuário

Em seguida, você desejará ter acesso fácil às variáveis e aos métodos do site `ABKUser`. Crie uma extensão para o seu código de usuário no arquivo `BrazeManager.swift` para que ele seja lido de forma mais organizada quanto à finalidade do arquivo auxiliar, da seguinte forma:

1. Um objeto `ABKUser` representa um usuário conhecido ou anônimo no seu aplicativo iOS. Adicione uma variável computada para recuperar o `ABKUser`; essa variável será reutilizada para recuperar variáveis sobre o usuário.
2. Consulte a variável do usuário para acessar facilmente o site `userId`. Entre as outras variáveis, o objeto `ABKUser` é responsável por (`firstName`, `lastName`, `phone`, `homeCity`, etc.)
3. Defina o usuário chamando `changeUser()` com um `userId` correspondente.

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
Prossiga para compilar seu código e executar seu aplicativo.<br><br>Tente identificar os usuários de um login/inscrição bem-sucedido. Certifique-se de ter um sólido entendimento do que é e do que não é um identificador de usuário apropriado. <br><br>No seu dashboard, observe se o identificador do usuário está registrado antes de prosseguir.
{% endalert %} 

### Análise de dados

{% tabs localização %}
{% tab Etapa 1: Eventos personalizados %}

##### Criar método de evento personalizado de registro

Com base no seguinte método do SDK da Braze `logCustomEvent`, crie um método correspondente. 

**Braze `logCustomEvent` método de referência**<br>
Isso foi projetado porque somente o arquivo `BrazeManager.swift` pode acessar diretamente os métodos do SDK da Braze para iOS. Portanto, ao criar um método correspondente, o resultado é o mesmo e é feito sem a necessidade de nenhuma dependência direta do SDK da Braze para iOS em seu código de produção.

```
open func logCustomEvent(_ eventName: String, withProperties properties: [AnyHashable : Any]?)
```

**Método de correspondência**<br>
Registre eventos personalizados do objeto `Appboy` no Braze. `Properties` é um parâmetro opcional com um valor padrão de nil. Não é necessário que os eventos personalizados tenham propriedades, mas é necessário que tenham um nome. 

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
{% tab Etapa 2: Atributos personalizados %}

##### Criar método de atributos personalizados de registro 

O SDK pode registrar vários tipos como atributos personalizados. Não há necessidade de criar métodos auxiliares para cada tipo de valor que pode ser definido. Em vez disso, exponha apenas um método que possa filtrar até o valor apropriado.

```
- (BOOL)setCustomAttributeWithKey:(NSString *)key andBOOLValue:(BOOL)value; 
- (BOOL)setCustomAttributeWithKey:(NSString *)key andIntegerValue:(NSIntenger)value; 
- (BOOL)setCustomAttributeWithKey:(NSString *)key andDoubleValue:(double)value; 
- (BOOL)setCustomAttributeWithKey:(NSString *)key andStringValue:(NSString *)value; 
- (BOOL)setCustomAttributeWithKey:(NSString *)key andDateValue:(NSDate *)value;
```

Os atributos personalizados são registrados a partir do objeto `ABKUser`. 

Crie **um método** que possa abranger todos os tipos disponíveis que podem ser definidos para uma atribuição. Adicione esse método em seu arquivo `BrazeManager.swift` na extensão de análise de dados. Isso pode ser feito filtrando os tipos de atributos personalizados válidos e chamando o método associado ao tipo correspondente.

- O parâmetro `value` é um tipo genérico que está em conformidade com o protocolo `Equatable`. Isso é feito explicitamente, portanto, se o tipo não for o que o SDK da Braze para iOS espera, haverá um erro de tempo de compilação.
- Os parâmetros `key` e `value` são parâmetros opcionais que serão desembrulhados condicionalmente no método. Essa é apenas uma maneira de garantir que valores não nulos sejam passados para o SDK da Braze para iOS.

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
{% tab Etapa 3: Compras %}

##### Criar método de compra de registro

Em seguida, com base no seguinte método do SDK da Braze `logPurchase`, crie um método correspondente. 

**Braze `logPurchase` método de referência**<br>
Isso foi projetado porque somente o arquivo `BrazeManager.swift` pode acessar diretamente os métodos do SDK da Braze para iOS. Portanto, ao criar um método correspondente, o resultado é o mesmo e é feito sem a necessidade de nenhuma dependência direta do SDK da Braze para iOS em seu código de produção. 

```
open func logPurchase(_ productIdentifier: String, inCurrency currency: String, atPrice price: NSDecimalNumber, withoutQuantity quantity: UInt)
```
**Método de correspondência**<br>
Registre as compras do objeto `Appboy` para a Braze. O SDK tem vários métodos para registrar compras, e este é apenas um exemplo. Esse método também lida com a criação dos objetos `NSDecimal` e `UInt`. A maneira como você deseja lidar com essa parte depende de você, este é apenas um exemplo.

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
Prossiga para compilar seu código e executar seu aplicativo. <br><br>Tente registrar eventos personalizados.<br><br>No seu dashboard, observe se os eventos personalizados estão registrados antes de prosseguir.
{% endalert %}

### Mensagem no app

{% tabs localização %}
{% tab Etapa 1: Conformidade com o Delegado %}

{% alert important %}
A seção de mensagens no app a seguir não é necessária para a integração se você não planeja usar esse canal no seu aplicativo.
{% endalert %}

##### Em conformidade com o ABKInAppMessageUIDelegate

Em seguida, ative o código de seu arquivo `BrazeManager.swift` para que esteja em conformidade com o `ABKInAppMessageUIDelegate` e manipule diretamente os métodos associados. 

O código de conformidade com o delegate será adicionado aos métodos `didFinishLaunching...` no arquivo `BrazeManager.swift`. Seu código de inicialização deve ter a seguinte aparência:

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
{% tab Etapa 2: Adicionar métodos delegados %}

##### Adicionar métodos delegados
Em seguida, crie uma extensão que esteja em conformidade com o site `ABKInAppMessageUIDelegate`.

Adicione o seguinte snippet à seção de análise de dados. Note que o objeto `BrazeManager.swift` está definido como o delegate; é nesse objeto que o arquivo `BrazeManager.swift` manipula todos os métodos `ABKInAppMessageUIDelegate`. 

{% alert important %}
O site `ABKInAppMessageUIDelegate` não vem com nenhum método obrigatório, mas o seguinte é um exemplo de um.
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
Prossiga para compilar seu código e executar seu aplicativo. <br><br>Tente enviar uma mensagem no app para você mesmo. <br><br>No arquivo `BrazeManager.swift`, defina um ponto de interrupção na entrada do método de exemplo `ABKInAppMessageUIDelegate`. Envie a si mesmo uma mensagem no app e confirme se o ponto de interrupção foi atingido antes de avançar mais.
{% endalert %}

### Cartões de conteúdo

{% tabs localização %}
{% tab Criar variáveis e métodos do cartão de conteúdo %}

{% alert important %}
A seção do cartão de conteúdo a seguir não é necessária para a integração se você não planeja usar esse canal no seu aplicativo.
{% endalert %}

##### Criar variáveis e métodos do cartão de conteúdo

Ative seu código de produção para exibir o controlador de visualização dos cartões de conteúdo sem a necessidade de instruções `import AppboyUI` desnecessárias. 

Crie uma extensão para o código dos seus cartões de conteúdo no arquivo `BrazeManager.swift`, para que ele seja lido de forma mais organizada quanto à finalidade do arquivo auxiliar, da seguinte forma:

1. Exibir o site `ABKContentCardsTableViewController`. Um `navigationController` opcional é o único parâmetro necessário para apresentar ou fazer um push do controlador de visualizações.
2. Inicializar um objeto `ABKContentCardsTableViewController` e, opcionalmente, alterar o título. Você também deve adicionar o controlador de visualizações inicializado à pilha de navegação.

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
Prossiga para compilar seu código e executar seu aplicativo.<br><br>Tente exibir o endereço `ABKContentCardsTableViewController` em seu aplicativo antes de prosseguir.
{% endalert %}

## Próximas etapas

Parabéns! Você concluiu este guia de práticas recomendadas de integração! Um exemplo de arquivo auxiliar `BrazeManager` pode ser encontrado no [GitHub](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/BrazeManager.swift).

Agora que você desacoplou todas as dependências do SDK da Braze para iOS do restante de seu código de produção, confira alguns de nossos guias de implementação avançada opcionais:
- [Guia de implementação de notificações por push avançadas]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/implementation_guide/)
- [Guia de implementação de mensagens no app avançadas]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/implementation_guide/)
- [Guia de implementação do cartão de conteúdo avançado]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/implementation_guide/)

