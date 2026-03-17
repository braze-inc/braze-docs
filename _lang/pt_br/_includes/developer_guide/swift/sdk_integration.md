## Integrando o SDK Swift

Você pode integrar e personalizar o SDK Swift da Braze usando o Swift Package Manager (SPM), CocoaPods ou métodos de integração manual. Para mais informações sobre os vários símbolos do SDK, consulte [documentação de referência do Braze Swift](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/).

### Pré-requisitos

Antes de começar, verifique se seu ambiente é compatível com a [última versão do SDK Swift da Braze](https://github.com/braze-inc/braze-swift-sdk#version-information).

### Etapa 1: Instale o SDK Swift da Braze

Recomendamos usar o [Swift Package Manager (SwiftPM)](https://swift.org/package-manager/) ou [CocoaPods](http://cocoapods.org/) para instalar o SDK Swift da Braze. Alternativamente, você pode instalar o SDK manualmente.

{% tabs local %}
{% tab Swift Package Manager %}
#### Etapa 1.1: Importar versão do SDK

Abra seu projeto e navegue até as configurações do seu projeto. Selecione a guia **SWIFT Packages** e clique no botão adicionar <i class="fas fa-plus"></i> abaixo da lista de pacotes.

![]({% image_buster /assets/img/swiftpackages.png %})

{% alert note %}
A partir da versão 7.4.0, o SDK Braze SWIFT tem canais de distribuição adicionais como [XCFrameworks estáticos](https://github.com/braze-inc/braze-swift-sdk-prebuilt-static) e [XCFrameworks dinâmicos](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic). Se você quiser usar qualquer um desses formatos, siga as instruções de instalação do respectivo repositório.
{% endalert %}

Digite o URL do nosso repositório iOS SWIFT SDK `https://github.com/braze-inc/braze-swift-sdk` no campo de texto. Embaixo da seção **Regra de Dependência**, selecione a versão do SDK. Finalmente, clique em **Adicionar Pacote**.

![]({% image_buster /assets/img/importsdk_example.png %})

#### Etapa 1.2: Selecione seus pacotes

O SDK Braze SWIFT separa os recursos em bibliotecas independentes para fornecer aos desenvolvedores mais controle sobre quais recursos importar para seus projetos.

| Pacote         | Informações                                                                                                                                                         |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `BrazeKit`      | Biblioteca principal do SDK que fornece suporte para análise de dados e notificações por push.                                                                                        |
| `BrazeLocation` | Biblioteca de local fornecendo suporte para análise de dados de local e monitoramento de geofence.                                                                              |
| `BrazeUI`       | Biblioteca de interface do usuário fornecida pela Braze para mensagens no aplicativo, Cartões de Conteúdo e Banners. Importe esta biblioteca se você pretende usar os componentes de UI padrão. |

{: .ws-td-nw-1}

##### Sobre bibliotecas de extensão

{% alert warning %}
[Serviço de Notificação Braze](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications) e [História de Push Braze](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories) são módulos de extensão que fornecem funcionalidade adicional e não devem ser adicionados diretamente ao alvo principal do seu aplicativo. Em vez disso, siga os guias vinculados para integrá-los separadamente em suas respectivas extensões de destino.
{% endalert %}

| Pacote                    | Informações                                                                               |
| -------------------------- | ------------------------------------------------------------------------------------- |
| `BrazeNotificationService` | Biblioteca de extensão de serviço de notificação que fornece suporte para notificações por push avançadas. |
| `BrazePushStory`           | Biblioteca de extensão de conteúdo de notificação que fornece suporte para push Stories.            |

{: .ws-td-nw-1}

Selecione o pacote que melhor atenda às suas necessidades e clique **Adicionar Pacote**. Certifique-se de selecionar `BrazeKit` no mínimo.

![]({% image_buster /assets/img/add_package.png %})
{% endtab %}

{% tab CocoaPods %}
#### Etapa 1.1: Instalar o CocoaPods

Para um guia completo, consulte o [Guia de Introdução do CocoaPods](https://guides.cocoapods.org/using/getting-started.html). Caso contrário, você pode executar o seguinte comando para começar rapidamente:

```bash
$ sudo gem install cocoapods
```

Se você ficar preso, confira o [Guia de Solução de Problemas do CocoaPods](http://guides.cocoapods.org/using/troubleshooting.html).

#### Etapa 1.2: Construindo o arquivo de pod

Em seguida, crie um arquivo no diretório do seu projeto Xcode chamado `Podfile`.

{% alert note %}
A partir da versão 7.4.0, o SDK Braze SWIFT tem canais de distribuição adicionais como [XCFrameworks estáticos](https://github.com/braze-inc/braze-swift-sdk-prebuilt-static) e [XCFrameworks dinâmicos](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic). Se você quiser usar qualquer um desses formatos, siga as instruções de instalação do respectivo repositório.
{% endalert %}

Adicione a seguinte linha ao seu Podfile:

```
target 'YourAppTarget' do
  pod 'BrazeKit'
end
```

`BrazeKit` contém a biblioteca principal do SDK que oferece suporte a análises de dados e notificações por push.

Sugerimos que você faça uma versão da Braze para que as atualizações do pod capturem automaticamente qualquer coisa menor que uma atualização de versão secundária. Fica assim: `pod 'BrazeKit' ~> Major.Minor.Build`. Se quiser integrar automaticamente a versão mais recente do SDK da Braze, mesmo com grandes alterações, você poderá usar `pod 'BrazeKit'` em seu Podfile.

##### Sobre bibliotecas adicionais

O SDK Braze SWIFT separa os recursos em bibliotecas independentes para fornecer aos desenvolvedores mais controle sobre quais recursos importar para seus projetos. Além de `BrazeKit`, você pode adicionar as seguintes bibliotecas ao seu Podfile:

| Biblioteca               | Informações                                                                                                                                                         |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `pod 'BrazeLocation'` | Biblioteca de local fornecendo suporte para análise de dados de local e monitoramento de geofence.                                                                              |
| `pod 'BrazeUI'`       | Biblioteca de interface do usuário fornecida pela Braze para mensagens no aplicativo, Cartões de Conteúdo e Banners. Importe esta biblioteca se você pretende usar os componentes de UI padrão. |

{: .ws-td-nw-1}

###### Bibliotecas de extensão

[BrazeNotificationService](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications) e [BrazePushStory](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories) são módulos de extensão que fornecem funcionalidade adicional e não devem ser adicionados diretamente ao direcionamento de seu aplicativo principal. Em vez disso, será necessário criar direcionamentos de extensão separados para cada um desses módulos e importar os módulos Braze para seus direcionamentos correspondentes.

| Biblioteca                          | Informações                                                                               |
| -------------------------------- | ------------------------------------------------------------------------------------- |
| `pod 'BrazeNotificationService'` | Biblioteca de extensão de serviço de notificação que fornece suporte para notificações por push avançadas. |
| `pod 'BrazePushStory'`           | Biblioteca de extensão de conteúdo de notificação que fornece suporte para push Stories.            |

{: .ws-td-nw-1}

#### Etapa 1.3: Instalar o SDK

Para instalar o Braze SDK CocoaPods, navegue até o diretório do seu projeto de app do Xcode em seu terminal e execute o seguinte comando:
```
pod install
```

Nesse ponto, você deve conseguir abrir o novo espaço de trabalho do projeto Xcode criado pelo CocoaPods. Use esse espaço de trabalho do Xcode em vez de seu projeto do Xcode.

![Uma pasta de Exemplo da Braze expandida para mostrar o novo \`BrazeExample.workspace\`.]({% image_buster /assets/img/braze_example_workspace.png %})

#### Atualizando o SDK usando CocoaPods

Para atualizar um CocoaPod, basta executar o seguinte comando no diretório do projeto:

```
pod update
```
{% endtab %}

{% tab Manual %}
#### Etapa 1.1: Baixar o SDK da Braze

Acessar a [página de lançamento do SDK da Braze no GitHub](https://github.com/braze-inc/braze-swift-sdk/releases), então baixar `braze-swift-sdk-prebuilt.zip`.

!["A página de lançamento do SDK da Braze no GitHub."]({% image_buster /assets/img/swift/sdk_integration/download-braze-swift-sdk-prebuilt.png %})

#### Etapa 1.2: Escolha seus frameworks

O SDK Braze SWIFT contém uma variedade de XCFrameworks independentes, o que lhe dá a liberdade de integrar os recursos que você deseja—sem precisar integrá-los todos. Consulte a tabela a seguir para escolher seus XCFrameworks:

| Pacote                    | Necessário? | Descrição                                                                                                                                                                                                                                                                                                                          |
| -------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `BrazeKit`                 | Sim       | Biblioteca principal do SDK que fornece suporte para análise de dados e notificações por push.                                                                                                                                                                                                                                                         |
| `BrazeLocation`            | Não        | Biblioteca de local que fornece suporte para análise de dados de local e monitoramento de geofence.                                                                                                                                                                                                                                               |
| `BrazeUI`                  | Não        | Biblioteca de interface do usuário fornecida pela Braze para mensagens no aplicativo, Cartões de Conteúdo e Banners. Importe esta biblioteca se você pretende usar os componentes de UI padrão.                                                                                                                                                                      |
| `BrazeNotificationService` | Não        | Biblioteca de extensão de serviço de notificação que fornece suporte para notificações por push avançadas. Não adicione esta biblioteca diretamente ao seu alvo principal do aplicativo, em vez disso [adicione a biblioteca `BrazeNotificationService` separadamente](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications).                 |
| `BrazePushStory`           | Não        | Biblioteca de extensão de conteúdo de notificação que fornece suporte para Push Stories. Não adicione esta biblioteca diretamente ao seu alvo principal do aplicativo, em vez disso [adicione a biblioteca `BrazePushStory` separadamente](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories).                                                 |
| `BrazeKitCompat`           | Não        | Biblioteca de compatibilidade contendo todas as classes e métodos `Appboy` e `ABK*` que estavam disponíveis na versão `Appboy-iOS-SDK` 4.X.X. Para obter mais informações sobre o uso, consulte o cenário de migração mínima no [guia de migração](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/).            |
| `BrazeUICompat`            | Não        | Biblioteca de compatibilidade contendo todas as `ABK*` classes e métodos que estavam disponíveis na biblioteca `AppboyUI` da versão `Appboy-iOS-SDK` 4.X.X. Para obter mais informações sobre o uso, consulte o cenário de migração mínima no [guia de migração](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/). |
| `SDWebImage`               | Não        | Dependência usada apenas por `BrazeUICompat` no cenário de migração mínima.                                                                                                                                                                                                                                                           |

{: .ws-td-nw-1 .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Etapa 1.3: Prepare seus arquivos

Decida se você quer usar **Estático** ou **Dinâmico** XCFrameworks, então prepare seus arquivos:

1. Crie um diretório temporário para seus XCFrameworks.
2. No `braze-swift-sdk-prebuilt`, abra o diretório `dynamic` e mova `BrazeKit.xcframework` para o seu diretório. Seu diretório deve ser semelhante ao seguinte:
    ```bash
    temp_dir
    └── BrazeKit.xcframework
    ```
3. Mova cada um dos seus [XCFrameworks escolhidos](#swift_step-2-choose-your-frameworks) para o seu diretório temporário. Seu diretório deve ser semelhante ao seguinte:
    ```bash
    temp_dir
    ├── BrazeKit.xcframework
    ├── BrazeKitCompat.xcframework
    ├── BrazeLocation.xcframework
    └── SDWebImage.xcframework
    ```

#### Etapa 1.4: Integre seus frameworks

Em seguida, integre as **Dinâmicas** ou **Estáticas** XCFrameworks que você [preparou anteriormente](#swift_step-3-prepare-your-files):

No seu projeto Xcode, selecione seu alvo de build, então **Geral**. Em **Frameworks, Bibliotecas e Conteúdo Incorporado**, arraste e solte os [arquivos que você preparou anteriormente](#swift_step-3-prepare-your-files).

!["Um projeto de exemplo do Xcode com cada biblioteca da Braze configurada para 'Incluir & Assinatura.'"]({% image_buster /assets/img/swift/sdk_integration/embed-and-sign.png %})

{% alert note %}
A partir do SDK Swift 12.0.0, você deve sempre selecionar **Incorporar & Assinatura** para os XCFrameworks do Braze, tanto para as variantes estáticas quanto dinâmicas. Isso garante que os recursos dos frameworks sejam devidamente incorporados no pacote do seu app.
{% endalert %}

{% alert tip %}
Para ativar o suporte a GIF, adicione `SDWebImage.xcframework`, localizado em `braze-swift-sdk-prebuilt/static` ou `braze-swift-sdk-prebuilt/dynamic`.
{% endalert %}

#### Erros comuns para projetos Objective-C

Se o seu projeto Xcode contiver apenas arquivos Objective-C, você poderá receber erros de "símbolo ausente" ao tentar compilar seu projeto. Para corrigir esses erros, abra seu projeto e adicione um arquivo Swift vazio à sua árvore de arquivos. Isso forçará sua cadeia de ferramentas a incorporar [SWIFT Runtime](https://support.apple.com/kb/dl1998) e vincular aos frameworks apropriados durante o período em questão.

```bash
FILE_NAME.swift
```

Substitua `FILE_NAME` por qualquer string sem espaços. Seu arquivo deve ser semelhante ao seguinte:

```bash
empty_swift_file.swift
```
{% endtab %}
{% endtabs local %}

### Etapa 2: Configurar inicialização atrasada (opcional)

Você pode optar por atrasar quando o SDK Swift do Braze é inicializado, o que é útil se seu app precisar carregar uma configuração ou esperar pelo consentimento do usuário antes de iniciar o SDK. A inicialização atrasada garante que as notificações por push do Braze e os tokens de push recebidos antes da inicialização do SDK sejam enfileirados e processados assim que o SDK for inicializado.

Para usar a inicialização atrasada, a versão mínima do SDK do Braze é necessária:
{% sdk_min_versions swift:11.2.0 %}

#### Etapa 2.1: Prepare-se para a inicialização atrasada

Chame `Braze.prepareForDelayedInitialization()` o mais cedo possível no ciclo de vida do seu app, idealmente em ou antes de `application(_:didFinishLaunchingWithOptions:)`. Isso garante que as notificações por push recebidas antes da inicialização do SDK sejam devidamente capturadas e processadas posteriormente.

{% alert note %}
Isso se aplica apenas às notificações por push do Braze. Outras notificações por push são tratadas normalmente pelos delegados do sistema.
{% endalert %}

{% tabs %}
{% tab Swift %}
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

{% tab Objective-C %}
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

Ao usar a inicialização atrasada, a automação de notificações por push é implicitamente ativada. Você pode [personalizar a automação de push](#swift_step-23-customize-push-automation-optional) passando um parâmetro `pushAutomation`.

#### Etapa 2.2: Configurar o comportamento da análise de push (opcional)

Quando a inicialização atrasada está ativada, as análises de push são enfileiradas por padrão. No entanto, você pode optar por enfileirar ou descartar explicitamente as análises de push.

##### Enfileirar explicitamente

Para enfileirar explicitamente as análises de push (comportamento padrão), passe `.queue` para o parâmetro `analyticsBehavior`. Eventos de análises de push que são enfileirados antes da inicialização serão processados e enviados ao servidor na inicialização.

{% tabs local %}
{% tab Swift %}
```swift
Braze.prepareForDelayedInitialization(analyticsBehavior: .queue)
```
{% endtab %}
{% tab Objective-C %}
```objc
[Braze prepareForDelayedInitializationWithAnalyticsBehavior:BRZPushEnqueueBehaviorQueue];
```
{% endtab %}
{% endtabs %}

##### Remover

Para remover a análise de push recebida antes da inicialização do SDK, passe `.drop` para o parâmetro `analyticsBehavior`. Com esta opção, qualquer evento de análise de push que ocorrer enquanto o SDK não estiver inicializado será ignorado.

{% tabs local %}
{% tab Swift %}
```swift
Braze.prepareForDelayedInitialization(analyticsBehavior: .drop)
```
{% endtab %}
{% tab Objective-C %}
```objc
[Braze prepareForDelayedInitializationWithAnalyticsBehavior:BRZPushEnqueueBehaviorDrop];
```
{% endtab %}
{% endtabs %}

#### Etapa 2.3: Personalizar automação de push (opcional)

Você pode personalizar a configuração da automação de push passando um parâmetro `pushAutomation`. Por padrão, todos os recursos de automação estão habilitados, exceto `requestAuthorizationAtLaunch`.

{% tabs local %}
{% tab SWIFT %}
```swift
// Enable all push automation
featuresBraze.prepareForDelayedInitialization(pushAutomation: true)

// Or customize specific automation options
let automation = Braze.Configuration.Push.Automation()
automation.automaticSetup = true
automation.requestAuthorizationAtLaunch = false
Braze.prepareForDelayedInitialization(pushAutomation: automation)
```
{% endtab %}

{% tab OBJECTIVE-C %}
```objc
// Enable all push automation features
[Braze prepareForDelayedInitializationWithPushAutomation:[[BRZConfigurationPushAutomation alloc] initWithAutomationEnabled:YES]];

// Or customize specific automation options
BRZConfigurationPushAutomation *automation = [[BRZConfigurationPushAutomation alloc] init];
automation.automaticSetup = YES;
automation.requestAuthorizationAtLaunch = NO;
[Braze prepareForDelayedInitializationWithPushAutomation:automation analyticsBehavior:BRZPushEnqueueBehaviorQueue];
```
{% endtab %}
{% endtabs %}

#### Etapa 2.4: Inicializar o SDK

Após o período de postergação escolhido (por exemplo, após buscar a configuração de um servidor ou após o consentimento do usuário), inicialize o SDK normalmente:

{% tabs local %}
{% tab SWIFT %}
```swift
func initializeBraze() {  
  let configuration = Braze.Configuration(apiKey: "YOUR-API-KEY", endpoint: "YOUR-ENDPOINT")    
  
  // Enable push automation to match the delayed initialization configuration  
  configuration.push.automation = true    
  let braze = Braze(configuration: configuration)    
  
  // Store the Braze instance for later use 
  AppDelegate.braze = braze
}
```
{% endtab %}
{% tab OBJECTIVE-C %}
```objc
- (void)initializeBraze {
  BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"YOUR-API-KEY" endpoint:@"YOUR-ENDPOINT"];
  
  // Enable push automation to match the delayed initialization configuration
  configuration.push.automation = [[BRZConfigurationPushAutomation alloc] initWithAutomationEnabled:YES];
  Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
  
  // Store the Braze instance for later use
  AppDelegate.braze = braze;
}
```
{% endtab %}
{% endtabs %}

{% alert note %}
Quando o SDK estiver inicializado, todas as notificações push enfileiradas, tokens de push e links profundos são processados automaticamente.
{% endalert %}

### Etapa 3: Atualize seu delegado do app

{% alert important %}
O seguinte assume que você já adicionou um `AppDelegate` ao seu projeto (que não são gerados por padrão) e que você não está usando o recurso de inicialização atrasada. Se você não planeja usar um `AppDelegate`, certifique-se de inicializar o SDK Braze o mais cedo possível, como durante o lançamento do app. Se você estiver usando o recurso de inicialização atrasada, consulte [Etapa 2.4](#swift_step-24-initialize-the-sdk) para inicializar o SDK e ignore esta etapa.
{% endalert %}

{% subtabs local %}
{% subtab swift %}
Adicione a seguinte linha de código ao seu `AppDelegate.swift` arquivo para importar os recursos incluídos no SDK da Braze para Swift:

```swift
import BrazeKit
```

Em seguida, adicione uma propriedade estática à sua classe `AppDelegate` para manter uma referência forte à instância da Braze durante toda a vida útil do seu aplicativo:

```swift
class AppDelegate: UIResponder, UIApplicationDelegate {
  static var braze: Braze? = nil
}
```

Finalmente, em `AppDelegate.swift`, adicione o seguinte trecho ao seu método `application:didFinishLaunchingWithOptions:`:

```swift
let configuration = Braze.Configuration(
    apiKey: "YOUR-APP-IDENTIFIER-API-KEY",
    endpoint: "YOUR-BRAZE-ENDPOINT"
)
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```

Atualize `YOUR-APP-IDENTIFIER-API-KEY` e `YOUR-BRAZE-ENDPOINT` com o valor correto da sua página de **Configurações do App**. Confira nossos [tipos de identificadores de API]({{site.baseurl}}/api/identifier_types/?tab=app%20ids) para saber mais sobre onde encontrar a chave de API do seu identificador de app.

{% endsubtab %}
{% subtab OBJECTIVE-C %}

Adicione a seguinte linha de código ao seu arquivo `AppDelegate.m`:

```objc
@import BrazeKit;
```

Em seguida, adicione uma variável estática ao seu arquivo `AppDelegate.m` para manter uma referência à instância da Braze durante toda a vida útil do seu aplicativo:

```objc
static Braze *_braze;

@implementation AppDelegate
+ (Braze *)braze {
  return _braze;
}

+ (void)setBraze:(Braze *)braze {
  _braze = braze;
}
@end
```

Finalmente, dentro do seu arquivo`AppDelegate.m`, adicione o seguinte trecho dentro do seu método `application:didFinishLaunchingWithOptions:`:

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:"YOUR-APP-IDENTIFIER-API-KEY"
                                                                  endpoint:"YOUR-BRAZE-ENDPOINT"];
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

Atualize `YOUR-APP-IDENTIFIER-API-KEY` e `YOUR-BRAZE-ENDPOINT` com o valor correto da sua página **Gerenciar Configurações**. Confira nossa [documentação da API]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key) para saber mais sobre onde encontrar a chave de API do seu identificador de app.

{% endsubtab %}
{% endsubtabs local %}

## Configurações opcionais

### Registro

Para uma visão centralizada em todas as plataformas, veja [Registro detalhado]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging). Para aprender a interpretar a saída do log, veja [Lendo logs detalhados]({{site.baseurl}}/developer_guide/sdk_integration/reading_verbose_logs).

#### Níveis de registro

O nível de log padrão para o SDK Braze Swift é `.error`—é também o nível mínimo suportado quando os logs estão habilitados. Esta é a lista completa de níveis de log:

| Swift       | Objective C              | Descrição                                                  |
| ----------- | ------------------------ | ------------------------------------------------------------ |
| `.debug`    | `BRZLoggerLevelDebug`    | Registrar informações de depuração + `.info` + `.error`.              |
| `.info`     | `BRZLoggerLevelInfo`     | Registre informações gerais do SDK (alterações de usuário, etc.) + `.error`. |
| `.error`    | `BRZLoggerLevelError`    | Erros de registro.                                                  |
| `.disabled` | `BRZLoggerLevelDisabled` | Não ocorre nenhum registro.                                           |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Definindo o nível de log

Você pode atribuir o nível de log em tempo de execução no seu objeto `Braze.Configuration`. Para detalhes completos de uso, veja [`Braze.Configuration.Logger`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/logger-swift.class).

{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)
// Enable logging of general SDK information (such as user changes, etc.)
configuration.logger.level = .info
let braze = Braze(configuration: configuration)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:self.APIKey
                                                                  endpoint:self.apiEndpoint];
// Enable logging of general SDK information (such as user changes, etc.)
[configuration.logger setLevel:BRZLoggerLevelInfo];
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
```

{% endtab %}
{% endtabs %}
