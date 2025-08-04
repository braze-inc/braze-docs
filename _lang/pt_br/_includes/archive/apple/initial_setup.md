A instalação do SDK da Braze  fornecerá a você a funcionalidade básica de análise de dados{% if include.platform == 'iOS' %}, bem como mensagens no app com as quais você pode engajar seus usuários{% endif %}.

O SDK {{include.platform}} da Braze deve ser instalado ou atualizado usando o [CocoaPods](http://cocoapods.org/), um gerenciador de dependências para projetos Objective C e Swift. O CocoaPods oferece mais simplicidade para integração e atualização.

## {{include.platform}} Integração de SDK CocoaPods

### Etapa 1: Instalar o CocoaPods

A instalação do SDK por meio do {{include.platform}} [CocoaPods](http://cocoapods.org/) automatiza a maior parte do processo de instalação para você. Antes de iniciar esse processo, verifique se você está usando a [versão 2.0.0](https://www.ruby-lang.org/en/installation/) ou superior do Ruby. Note que não é necessário ter conhecimento da sintaxe do Ruby para instalar esse SDK.

Para começar, basta executar o seguinte comando:

```bash
$ sudo gem install cocoapods
```

**Nota**: Se for solicitado que você substitua o executável `rake`, consulte as [instruções de introdução em CocoaPods.org](http://guides.cocoapods.org/using/getting-started.html) para obter mais detalhes.

**Nota**: Se você tiver problemas com o CocoaPods, consulte o [Guia de solução de problemas do CocoaPods](http://guides.cocoapods.org/using/troubleshooting.html).

### Etapa 2: Construindo o arquivo de pod

Agora que você instalou o CocoaPods Ruby Gem, precisará criar um arquivo no diretório do projeto Xcode chamado `Podfile`.

Adicione a seguinte linha ao seu arquivo de pod:

```
target 'YourAppTarget' do
  pod 'Appboy-{{include.platform}}-SDK'
end
```

**Nota**: Sugerimos que você faça uma versão da Braze para que as atualizações do pod capturem automaticamente qualquer coisa menor que uma atualização de versão secundária. Isso se parece com 'pod 'Appboy-{{include.platform}}-SDK' ~> Major.Minor.Build'. Se quiser integrar a versão mais recente do SDK da Braze automaticamente, mesmo com grandes alterações, você poderá usar `pod 'Appboy-{{include.platform}}-SDK'` em seu podfile.
{% if include.platform == 'iOS' %}
**Nota**: Se você não usar nenhuma UI padrão da Braze e não quiser introduzir a dependência SDWebImage, aponte a dependência da Braze em seu Podfile para nossa subespécie Core, como `pod 'Appboy-iOS-SDK/Core'` em seu Podfile. {% endif %}.

### Etapa 3: Instalação do SDK da Braze

Para instalar o SDK da Braze CocoaPods, navegue até o diretório do seu projeto de app do Xcode em seu terminal e execute o seguinte comando:
```
pod install
```

Nesse ponto, você deve conseguir abrir o novo espaço de trabalho do projeto Xcode criado pelo CocoaPods. Use esse espaço de trabalho do Xcode em vez de seu projeto do Xcode. 

![Novo espaço de trabalho]({% image_buster /assets/img_archive/podsworkspace.png %})

### Etapa 4: Atualização do delegate do seu app

{% tabs %}
{% tab OBJECTIVE C %}

Adicione a seguinte linha de código ao seu arquivo `AppDelegate.m`:

```objc
{% if include.platform == 'iOS' %}#import "Appboy-iOS-SDK/AppboyKit.h"{% else %}#import <AppboyTVOSKit/AppboyKit.h>{% endif %}
```

No arquivo `AppDelegate.m`, adicione o seguinte snippet no método `application:didFinishLaunchingWithOptions`:

```objc
[Appboy startWithApiKey:@"YOUR-API-KEY"
         inApplication:application
     withLaunchOptions:launchOptions];
```

{% endtab %}
{% tab swift %}

Se estiver integrando o SDK da Braze com o CocoaPods ou o Carthage, adicione a seguinte linha de código ao seu arquivo `AppDelegate.swift`:

```swift
{% if include.platform == 'iOS' %}import Appboy_iOS_SDK{% else %}import AppboyTVOSKit{% endif %}
```

Para saber mais sobre o uso de código Objective C em projetos Swift, consulte os [documentos para desenvolvedores da Apple](https://developer.apple.com/library/ios/documentation/swift/conceptual/buildingcocoaapps/MixandMatch.html).

Em `AppDelegate.swift`, adicione o seguinte snippet ao seu `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool`:

```swift
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions)
```

**Nota**: O singleton do Braze `sharedInstance` será nulo antes de `startWithApiKey:` ser chamado, pois esse é um pré-requisito para usar qualquer funcionalidade do Braze.

{% endtab %}
{% endtabs %}

{% alert important %}
Atualize `YOUR-API-KEY` com o valor correto em sua página "Gerenciar configurações".
{% endalert %}

{% alert warning %}
Não de esqueça de inicializar a Braze na thread principal de seu aplicativo. A inicialização de forma assíncrona pode levar a uma funcionalidade interrompida.
{% endalert %}


### Etapa 5: Especifique seu endpoint personalizado ou cluster de dados

{% alert note %}
Observe que, a partir de dezembro de 2019, os pontos de extremidade personalizados não serão mais fornecidos. Se você tiver um ponto de extremidade personalizado pré-existente, poderá continuar a usá-lo. Para obter mais informações, consulte nossa <a href="{{site.baseurl}}/api/basics/#endpoints">lista de endpoints disponíveis</a>.
{% endalert %}

Seu representante da Braze já deve ter informado sobre o [endpoint correto]({{ site.baseurl }}/user_guide/administrative/access_braze/sdk_endpoints/).

#### Configuração do endpoint em tempo de compilação (recomendado)
Se for fornecido um ponto de extremidade personalizado pré-existente...
- A partir do SDK da Braze para iOS v3.0.2, você pode definir um endpoint personalizado usando o arquivo `Info.plist`. Adicione o dicionário `Appboy` ao seu arquivo Info.plist. Dentro do dicionário `Appboy`, adicione a subentrada `Endpoint` string e defina o valor para a autoridade do url de seu endpoint personalizado (por exemplo, `sdk.iad-01.braze.com`, não `https://sdk.iad-01.braze.com`).

#### Configuração do endpoint em tempo de execução

Se for fornecido um ponto de extremidade personalizado pré-existente...
- A partir da Braze iOS SDK v3.17.0+, você pode substituir a definição do seu endpoint por meio do `ABKEndpointKey` dentro do parâmetro `appboyOptions` passado para `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`. Defina o valor como a autoridade do url do seu endpoint personalizado (por exemplo, `sdk.iad-01.braze.com`, não `https://sdk.iad-01.braze.com`).

{% alert note %}
O suporte da configuração de endpoints em tempo de execução usando `ABKAppboyEndpointDelegate` foi removido no Braze iOS SDK v3.17.0. Se você já usa `ABKAppboyEndpointDelegate`, note que nas versões v3.14.1 a v3.16.0 da Braze iOS SDK, qualquer referência a `dev.appboy.com` em seu método `getApiEndpoint()` deve ser substituída por uma referência a `sdk.iad-01.braze.com`.
{% endalert %}

{% alert important %}
Para saber qual é o seu cluster específico, pergunte ao seu gerente de sucesso do cliente ou entre em contato com a nossa equipe de suporte.
{% endalert %}

### Integração completa de SDK

A Braze agora deve estar coletando dados do seu aplicativo e sua integração básica deve estar concluída. {% if include.platform == 'iOS' %}Consulte as seções a seguir para ativar o rastreamento de eventos personalizados, o envio de mensagens no app, o feed de notícias e o conjunto completo de recursos do Braze.{% else %}Observe que, ao compilar seu app para tvOS e quaisquer outras bibliotecas de terceiros, o Bitcode deve estar ativado.{% endif %}

### Atualizando o SDK do Braze via CocoaPods

Para atualizar um Cocoapod, basta executar os seguintes comandos no diretório do projeto:

```
pod update
```

## Personalização do Braze na inicialização

Se desejar personalizar a Braze na inicialização, você poderá usar o método de inicialização da Braze `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions` e passar um `NSDictionary` opcional de chaves de inicialização da Braze.
{% tabs %}
{% tab OBJECTIVE C %}

Em seu arquivo `AppDelegate.m`, no método `application:didFinishLaunchingWithOptions`, adicione o seguinte métoda Braze:

```objc
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

{% endtab %}
{% tab swift %}

Em `AppDelegate.swift`, em seu método `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool`, adicione o seguinte método Braze:

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:appboyOptions)
```

em que `appboyOptions` é um `Dictionary` de valores de configuração de inicialização.

{% endtab %}
{% endtabs %}

**Nota**: Esse método substituiria o método de inicialização `startWithApiKey:inApplication:withLaunchOptions:`.

Esse método é chamado com os seguintes parâmetros:

- `YOUR-API-KEY` - A chave de API de seu aplicativo no dashboard da Braze
- `application` - O app atual
- `launchOptions` - As opções `NSDictionary` que você obtém de `application:didFinishLaunchingWithOptions:`
- `appboyOptions` - Um site opcional `NSDictionary` com valores de configuração de inicialização para a Braze

Veja [Appboy.h](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h) para obter uma lista das teclas de inicialização da Braze.

## Appboy.sharedInstance() e a anulabilidade do Swift
Diferentemente da prática comum, o singleton `Appboy.sharedInstance()` é opcional. Isso ocorre porque `sharedInstance` é `nil` antes da chamada de `startWithApiKey:`, e há algumas implementações não padronizadas, mas ainda válidas, nas quais uma inicialização postergada pode ser utilizada.

Se você chamar `startWithApiKey:` em seu delegado `didFinishLaunchingWithOptions:` antes de qualquer acesso ao `sharedInstance` do Appboy (a implementação padrão), poderá usar o encadeamento opcional, como `Appboy.sharedInstance()?.changeUser("testUser")`, para evitar verificações complicadas. Isso terá paridade com uma implementação em Objective-C que assume um `sharedInstance` não nulo.

