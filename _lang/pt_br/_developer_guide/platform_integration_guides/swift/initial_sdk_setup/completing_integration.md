---
nav_title: Concluindo a Integração
article_title: Concluindo a integração de SDK SWIFT
platform: Swift
description: "Este artigo de referência mostra como finalizar a integração do SDK da Braze para SWIFT após instalá-lo por meio de uma das opções de integração."
page_order: 2

---

# Concluindo a integração

> Antes de seguir estas etapas, integre o SDK do Swift para iOS usando [Swift Package Manager]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/swift_package_manager/) ou [CocoaPods]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/cocoapods/).

## Atualize seu delegado do app

{% tabs %}
{% tab swift %}

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

{% endtab %}
{% tab OBJECTIVE C %}

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

{% endtab %}
{% endtabs %}


## Integração completa de SDK

Neste ponto, sua integração básica deve estar completa. Braze deve agora estar coletando dados do seu aplicativo. Siga os outros artigos neste guia de integração para implementar e personalizar toda a gama de recursos e canais de envio de mensagens da Braze.

## Recursos adicionais

Nossa [documentação de referência do SDK - ](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/ "documentação completa da classe iOS") \- fornece informações e orientações adicionais sobre cada símbolo do SDK.

