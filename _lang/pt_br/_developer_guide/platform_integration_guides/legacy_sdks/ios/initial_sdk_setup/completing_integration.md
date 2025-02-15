---
nav_title: Conclusão da integração
article_title: Conclusão da integração do SDK do iOS
platform: iOS
description: "Este artigo de referência mostra como concluir a integração do SDK do Braze depois de instalá-lo por meio de uma das opções de integração."
page_order: 2

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Conclusão da integração

Antes de seguir estas etapas, é preciso já ter integrado o SDK usando [Carthage]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/carthage_integration/), [CocoaPods]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/cocoapods/), [o Swift Package Manager]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/swift_package_manager/) ou uma integração [manual]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/manual_integration_options/).

## Etapa 1: Atualize seu arquivo AppDelegate

{% tabs %}
{% tab OBJECTIVE C %}

Se estiver fazendo a integração do SDK da Braze com CocoaPods, Carthage ou com uma [integração manual dinâmica]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/manual_integration_options/), adicione a seguinte linha de código ao seu arquivo `AppDelegate.m`:

```objc
#import "Appboy-iOS-SDK/AppboyKit.h"
```

Se estiver fazendo a integração com o Swift Package Manager ou com uma [integração manual estática]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/manual_integration_options/), use esta linha de código:

```objc
#import "AppboyKit.h"
```

Em seguida, no arquivo `AppDelegate.m`, adicione o seguinte snippet no método `application:didFinishLaunchingWithOptions:`:

```objc
[Appboy startWithApiKey:@"YOUR-APP-IDENTIFIER-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions];
```

Atualize `YOUR-APP-IDENTIFIER-API-KEY` com o valor correto em sua página **Manage Settings (Gerenciar configurações** ). Consulte nossa [documentação da API]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key) para saber mais sobre onde encontrar a chave de API do identificador do app.

{% endtab %}
{% tab swift %}

Se estiver fazendo a integração do SDK da Braze com CocoaPods, Carthage ou com uma [integração manual dinâmica]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/manual_integration_options/), adicione a seguinte linha de código ao seu arquivo `AppDelegate.swift`:

```swift
import Appboy_iOS_SDK
```

Se estiver fazendo a integração com o Swift Package Manager ou com uma [integração manual estática]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/installation_methods/manual_integration_options/), use esta linha de código:

```swift
import AppboyKit
```
Consulte os [documentos para desenvolvedores da Apple](https://developer.apple.com/library/ios/documentation/swift/conceptual/buildingcocoaapps/MixandMatch.html) para saber mais sobre o uso da linguagem Objective-C em projetos Swift.

Em seguida, em `AppDelegate.swift`, adicione o seguinte snippet a `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool`:

```swift
Appboy.start(withApiKey: "YOUR-APP-IDENTIFIER-API-KEY", in:application, withLaunchOptions:launchOptions)
```

Atualize `YOUR-APP-IDENTIFIER-API-KEY` com o valor correto em sua página **Manage Settings (Gerenciar configurações** ). Consulte nossa [documentação da API]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key) para saber mais sobre onde encontrar a chave de API do identificador do app.

{% endtab %}
{% endtabs %}

{% alert note %}
O singleton `sharedInstance` será nulo antes de `startWithApiKey:` ser chamado, pois esse é um pré-requisito para usar qualquer funcionalidade da Braze.
{% endalert %}

{% alert warning %}
Inicialize a Braze na thread principal do seu app. A inicialização de forma assíncrona pode levar a uma funcionalidade interrompida.
{% endalert %}


## Etapa 2: Especifique seu cluster de dados

{% alert note %}
A partir de dezembro de 2019, os endpoints personalizados não serão mais fornecidos. Você poderá continuar usando eventuais endpoints personalizados pré-existentes. Para saber mais, consulte nossa <a href="{{site.baseurl}}/api/basics/#endpoints">lista de endpoints disponíveis</a>.
{% endalert %}

### Configuração do endpoint em tempo de compilação (recomendado)

Se for fornecido um ponto de extremidade personalizado pré-existente:
- A partir do SDK da Braze para iOS v3.0.2, você pode definir um endpoint personalizado usando o arquivo `Info.plist`. Adicione o dicionário `Braze` ao seu arquivo `Info.plist`. Dentro do dicionário `Braze`, adicione a subentrada string `Endpoint` e defina o valor da autoridade do seu URL de endpoint personalizado (por exemplo, `sdk.iad-01.braze.com`, não `https://sdk.iad-01.braze.com`). Antes do Braze iOS SDK v4.0.2, deve-se utilizar a chave do dicionário `Appboy` no lugar de `Braze`.

Seu representante Braze já deve ter informado sobre o [endpoint correto]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/).

### Configuração do endpoint em tempo de execução

Se for fornecido um ponto de extremidade personalizado pré-existente:
- A partir do Braze iOS SDK v3.17.0+, você pode substituir a definição do seu endpoint pela chave `ABKEndpointKey` dentro do parâmetro `appboyOptions` passado para `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`. Defina o valor como a autoridade do URL do seu endpoint personalizado (por exemplo, `sdk.iad-01.braze.com`, não `https://sdk.iad-01.braze.com`).

## Integração completa de SDK

Agora, a Braze deve estar coletando dados do seu app, e sua integração básica deve estar concluída. Consulte os artigos a seguir para ativar [o rastreamento de eventos personalizados]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/), o [envio de mensagens push]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/) e o conjunto completo de recursos do Braze.

## Personalização do Braze na inicialização

Se desejar personalizar a Braze na inicialização, você poderá usar o método de inicialização da Braze `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:` e passar um `NSDictionary` opcional de chaves de inicialização da Braze.
{% tabs %}
{% tab OBJECTIVE C %}

Em seu arquivo `AppDelegate.m`, no método `application:didFinishLaunchingWithOptions:`, adicione o seguinte método da Braze:

```objc
[Appboy startWithApiKey:@"YOUR-APP-IDENTIFER-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

Note que esse método substituiria o método de inicialização `startWithApiKey:inApplication:withLaunchOptions:`.

{% endtab %}
{% tab swift %}

Em `AppDelegate.swift`, no método `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool`, adicione o seguinte método da Braze, em que `appboyOptions` é um `Dictionary` de valores de configuração de inicialização:

```swift
Appboy.start(withApiKey: "YOUR-APP-IDENTIFIER-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:appboyOptions)
```

Note que esse método substituiria o método de inicialização `startWithApiKey:inApplication:withLaunchOptions:`.

{% endtab %}
{% endtabs %}

Esse método é chamado com os seguintes parâmetros:

- `YOUR-APP-IDENTIFIER-API-KEY` - Sua chave de API do [identificador do app]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key) no dashboard do Braze.
- `application` - O app atual.
- `launchOptions` - As opções `NSDictionary` que você obtém em `application:didFinishLaunchingWithOptions:`.
- `appboyOptions` - Um `NSDictionary` opcional com valores de configuração de inicialização para a Braze.

Consulte uma lista das chaves de inicialização da Braze em [Appboy.h](https://github.com/braze-inc/braze-ios-sdk/blob/master/AppboyKit/include/Appboy.h).

## Appboy.sharedInstance() e a anulabilidade do Swift
Diferentemente da prática comum, o singleton `Appboy.sharedInstance()` é opcional. Isso ocorre porque `sharedInstance` é `nil` antes da chamada de `startWithApiKey:`, e há algumas implementações não padronizadas, mas ainda válidas, nas quais uma inicialização postergada pode ser utilizada.

Se você chamar `startWithApiKey:` em seu delegado `didFinishLaunchingWithOptions:` antes de qualquer acesso ao `sharedInstance` do Appboy (a implementação padrão), poderá usar o encadeamento opcional, como `Appboy.sharedInstance()?.changeUser("testUser")`, para evitar verificações complicadas. Isso terá paridade com uma implementação em Objective-C que assume um `sharedInstance` não nulo.

## Recursos adicionais

[Documentação completa da classe iOS A ](http://appboy.github.io/appboy-ios-sdk/docs/annotated.html "documentação completa da classe iOS") está disponível para fornecer orientação adicional sobre qualquer método do SDK.

