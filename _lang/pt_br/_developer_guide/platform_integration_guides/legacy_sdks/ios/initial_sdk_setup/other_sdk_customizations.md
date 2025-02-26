---
nav_title: Outras personalizações do SDK
article_title: Outras personalizações do SDK para iOS
platform: iOS
description: "Este artigo de referência aborda a personalização do SDK, como nível de registro, coleta de IDFA e outras personalizações."
page_order: 3

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Outras personalizações do SDK

## Nível de registro da Braze

O nível de registro padrão para o Braze iOS SDK é mínimo, ou `8` no gráfico a seguir. Esse nível suprime a maioria dos registros para que nenhuma informação sensível seja registrada em um aplicativo lançado em produção.

Consulte a seguinte lista de níveis de registro disponíveis:

### Níveis de registro

| Nível    | Descrição |
|----------|-------------|
| 0        | Verbose. Todas as informações de registro serão registradas no console do iOS.  |
| 1        | Depurar. As informações de depuração e de registro superior serão registradas no console do iOS.  |
| 2        | Aviso. As informações de registro de aviso e superiores serão registradas no console do iOS.  |
| 4        | Erro. As informações de erro e de registro superior serão registradas no console do iOS.  |
| 8        | Mínimo. O mínimo de informações será registrado no console do iOS. A configuração padrão do SDK. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Registro detalhado

É possível configurar o nível de registro para qualquer valor disponível. No entanto, definir o nível de registro como detalhado, ou `0`, pode ser muito útil para depurar problemas com a sua integração. Esse nível é destinado apenas a ambientes de desenvolvimento e não deve ser definido em um aplicativo lançado. O registro detalhado não enviará nenhuma informação extra ou nova do usuário para o Braze.

### Definição do nível de registro

O nível de registro pode ser atribuído em tempo de compilação ou em tempo de execução:

{% tabs localização %}
{% tab Tempo de compilação %}

Adicione um dicionário chamado `Braze` ao seu arquivo `Info.plist`. No dicionário `Braze`, adicione a subentrada string `LogLevel` e defina o valor como `0`. 

{% alert note %}
Antes do SDK da Braze para iOS v4.0.2, a chave do dicionário `Appboy` deve ser usada no lugar de `Braze`.
{% endalert %} 

Exemplo do conteúdo de `Info.plist`:

```
<key>Braze</key>
<dict>
  <key>LogLevel</key>
  <string>0</string>
</dict>
```

{% endtab %}
{% tab Tempo de execução %}

Adicione o `ABKLogLevelKey` dentro do parâmetro `appboyOptions` passado para `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`. Defina seu valor como o número inteiro `0`.

{% subtabs %}
{% subtab OBJECTIVE-C %}

```objc
NSMutableDictionary *appboyOptions = [NSMutableDictionary dictionary];
appboyOptions[ABKLogLevelKey] = @(0);
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

{% endsubtab %}
{% subtab swift %}

```swift
let appboyOptions: [AnyHashable: Any] = [
  ABKLogLevelKey : 0
]
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions, withAppboyOptions:appboyOptions)
```

{% endsubtab %}
{% endsubtabs %}

{% alert note %}
O nível de registro só pode ser definido em tempo de execução com o Braze iOS SDK v4.4.0 ou mais recente. Se estiver usando uma versão anterior do SDK, defina o nível de registro no momento da compilação.
{% endalert %} 

{% endtab %}
{% endtabs %}

## Coleta opcional de IDFV - Swift

Nas versões anteriores do Swift SDK da Braze para iOS, o campo IDFV (Identifier for Vendor, identificador do fornecedor) era coletado automaticamente como o ID do dispositivo do usuário. 

A partir do SDK Swift v5.7.0, o campo IDFV pode ser desativado e, em vez disso, a Braze definirá um UUID aleatório como o ID do dispositivo. Para saber mais, consulte [Coleta de IDFV]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/swift_idfv/).

## Coleção IDFA opcional

A coleção IDFA é opcional no SDK da Braze e fica desativada por padrão. A coleta IDFA só é necessária na Braze se você pretender usar nossas [integrações de atribuição de instalação]({{site.baseurl}}/partners/advertising_technologies/attribution/adjust/). Se houver aceitação de armazenar seu IDFA, nós o armazenaremos gratuitamente, para que você possa aproveitar essas opções imediatamente após o lançamento, sem trabalho de desenvolvimento adicional.

Por isso, recomendamos que você continue coletando o IDFA se atender a qualquer um dos critérios a seguir:

- Você está atribuindo a instalação do app a um anúncio veiculado anteriormente
- Você está atribuindo uma ação no aplicativo a um anúncio veiculado anteriormente

### iOS 14.5 AppTrackingTransparency

A Apple exige que os usuários façam a aceitação por meio de um pedido de aceitação para coletar o IDFA.

Para coletar o IDFA, além de implementar nosso protocolo `ABKIDFADelegate`, seu aplicativo precisará solicitar autorização do usuário usando o `ATTrackingManager` da Apple na estrutura de transparência de rastreamento do app. Consulte o [artigo sobre privacidade do usuário](https://developer.apple.com/app-store/user-privacy-and-data-use/) da Apple para saber mais.

A solicitação de autorização de transparência de rastreamento de app requer uma entrada `Info.plist` para explicar o uso do identificador:

```
<key>NSUserTrackingUsageDescription</key>
<string>To retarget ads and build a global profile to better serve you things you would like.</string>
```

### Implementação da coleção IDFA

Siga estas etapas para implementar a Coleção IDFA:

##### Etapa 1: Implementar o ABKIDFADelegate

Crie uma classe que esteja em conformidade com o [`ABKIDFADelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKIDFADelegate.h) protocolo:

{% tabs %}
{% tab OBJECTIVE C %}

```objc
#import "IDFADelegate.h"
#import <AdSupport/ASIdentifierManager.h>
#import <AppTrackingTransparency/AppTrackingTransparency.h>

@implementation IDFADelegate

- (NSString *)advertisingIdentifierString {
  return [[[ASIdentifierManager sharedManager] advertisingIdentifier] UUIDString];
}

- (BOOL)isAdvertisingTrackingEnabledOrATTAuthorized {
  if (@available(iOS 14, *)) {
    return [ATTrackingManager trackingAuthorizationStatus] == ATTrackingManagerAuthorizationStatusAuthorized;
  }
  return [[ASIdentifierManager sharedManager] isAdvertisingTrackingEnabled];
}

@end
```

{% endtab %}
{% tab swift %}

```swift
import Appboy_iOS_SDK
import AdSupport
import AppTrackingTransparency

class IDFADelegate: NSObject, ABKIDFADelegate {
   func advertisingIdentifierString() -> String {
    return ASIdentifierManager.shared().advertisingIdentifier.uuidString
  }

  func isAdvertisingTrackingEnabledOrATTAuthorized() -> Bool {
    if #available(iOS 14, *) {
      return ATTrackingManager.trackingAuthorizationStatus ==  ATTrackingManager.AuthorizationStatus.authorized
    }
    return ASIdentifierManager.shared().isAdvertisingTrackingEnabled
  }
}
```
{% endtab %}
{% endtabs %}

##### Etapa 2: Definir o delegado durante a inicialização do Braze

No dicionário `appboyOptions` passado para `startWithApiKey:inApplication:withAppboyOptions:`, defina a chave `ABKIDFADelegateKey` como uma instância de sua classe em conformidade com `ABKIDFADelegate`.

## Tamanho aproximado do SDK do iOS {#ios-sdk-size}

O tamanho aproximado do arquivo do framework do SDK do iOS é de 30 MB, e o tamanho aproximado do arquivo .ipa (além do arquivo do app) está entre 1 MB e 2 MB.

A Braze mede o tamanho de iOS SDK observando o efeito do SDK no tamanho do arquivo `.ipa`, de acordo com as [recomendações da Apple sobre tamanho de apps](https://developer.apple.com/library/content/qa/qa1795/_index.html). Se estiver calculando a adição de tamanho do SDK do iOS ao seu aplicativo, recomendamos o seguinte [Obter um relatório de tamanho do app](https://developer.apple.com/library/content/qa/qa1795/_index.html) para comparar a diferença de tamanho no seu `.ipa` antes e depois da integração do SDK do Braze para iOS. Ao comparar os tamanhos do relatório de tamanho de afinamento de aplicativos, também recomendamos analisar os tamanhos de aplicativos para arquivos `.ipa` afinados, pois os arquivos `.ipa` universais serão maiores do que os binários baixados da App Store e instalados nos dispositivos dos usuários.

{% alert note %}
Se estiver integrando via CocoaPods com `use_frameworks!`, defina `Enable Bitcode = NO` nas Configurações de construção do alvo para obter um dimensionamento preciso.
{% endalert %}

