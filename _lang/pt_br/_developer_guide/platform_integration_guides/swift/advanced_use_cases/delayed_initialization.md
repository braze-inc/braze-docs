---
nav_title: Inicialização com postergação
article_title: Postergação da inicialização do Braze Swift SDK
platform: Swift
page_order: 6
description: "Este artigo aborda como implementar a inicialização postergada do Swift SDK para preservar o tratamento de notificações por push quando o SDK é inicializado de forma assíncrona."

---

# Postergação da inicialização do Braze Swift SDK

> Saiba como inicializar o SDK do Braze Swift de forma assíncrona e, ao mesmo tempo, garantir que o tratamento de notificações por push seja preservado. Isso pode ser útil quando for necessário configurar outros serviços antes de inicializar o SDK, como buscar dados de configuração de um servidor ou aguardar o consentimento do usuário.

## Configuração da inicialização por postergação

### Etapa 1: Preparando o SDK para inicialização com postergação

Por padrão, se um usuário final abrir a notificação por push enquanto o app estiver em um estado finalizado, a notificação por push não poderá ser processada antes que o SDK seja inicializado.

A partir do [Braze Swift SDK versão 10.1.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/10.1.0) e posteriores, você pode lidar com isso usando o método auxiliar estático: [Braze.prepareForDelayedInitialization(pushAutomation:)](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/preparefordelayedinitialization(pushautomation:)). Esse método preparará o SDK para a inicialização por postergação, configurando o sistema de automação push.

Antes de o SDK ser inicializado, todas as notificações por push originadas do Braze serão capturadas e colocadas em uma fila. Depois que o SDK for inicializado, essas notificações por push serão processadas pelo SDK. Esse método deve ser chamado o mais cedo possível no ciclo de vida do aplicativo, dentro ou antes do método `application(_:didFinishLaunchingWithOptions:)` do seu `AppDelegate`.

{% alert note %}
O SDK do Swift não captura notificações por push que não sejam do Braze - elas continuarão a ser tratadas pelos métodos delegados do sistema.
{% endalert %}

{% tabs %}
{% tab Swift - UIKit %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
  // Prepare the SDK for delayed initialization
  Braze.prepareForDelayedInitialization()

  // ... Additional non-Braze setup code

  return true
}
```
{% endtab %}

{% tab Swift - SwiftUI %}
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

### Etapa 2: Inicializando o SDK do Braze

Depois de preparar o SDK para a inicialização por postergação, você pode inicializá-lo de forma assíncrona a qualquer momento no futuro. Em seguida, o SDK processará todos os eventos de notificações por push enfileirados originados do Braze.

Para inicializar o SDK do Braze, siga o [processo padrão de inicialização do SDK do Swift]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/).

## Considerações

Ao usar `Braze.prepareForDelayedInitialization(pushAutomation:)`, você está configurando o SDK para usar automaticamente os recursos de automação de notificações por push. Os métodos delegados do sistema que manipulam notificações por push não serão chamados para notificações por push originadas do Braze.

O SDK somente processará uma notificação por push do Braze e a ação resultante **depois** que o SDK for inicializado. Por exemplo, se um usuário tocar em uma notificação por push que abre um deep linking, o deep link só será aberto depois que a instância `Braze` for inicializada.

Se você precisar realizar um processamento adicional nas notificações por push do Braze, consulte [Assinatura de atualizações de notificações por push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#subscribing-to-push-notifications-updates). Lembre-se de que, para receber atualizações de notificações por push que foram enfileiradas anteriormente, você deve implementar o manipulador de inscrição diretamente após a inicialização do SDK.
