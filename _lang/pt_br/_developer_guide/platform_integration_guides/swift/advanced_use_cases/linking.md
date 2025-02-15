---
nav_title: Deep linking
article_title: Deep linking para iOS
platform: Swift
page_order: 1
description: "Este artigo cobre como implementar o delegado de deep linking universal para seu app iOS e exemplos de como fazer deep link para as configurações do app do Swift SDK."

---

# Deep linking

> O deep linking é uma forma de fornecer um link que inicia um app nativo, mostra conteúdo específico ou executa alguma ação específica. Para implementar deep links em seu app iOS pela primeira vez, siga estas etapas.

Para obter informações gerais sobre o que são deep links, consulte nosso [artigo de perguntas frequentes]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking). 

## Etapa 1: Registro de um esquema

Para lidar com o deep linking, um esquema personalizado deve ser declarado em seu arquivo `Info.plist`. A estrutura de navegação é definida por uma matriz de dicionários. Cada um desses dicionários contém um vetor de strings.

Use o Xcode para editar seu `Info.plist` arquivo:

1. Adicione uma nova chave, `URL types`. O Xcode fará automaticamente disso um vetor contendo um dicionário chamado `Item 0`.
2. Dentro de `Item 0`, adicione uma chave `URL identifier`. Defina o valor para seu esquema personalizado.
3. Dentro de `Item 0`, adicione uma chave `URL Schemes`. Isso será automaticamente um vetor contendo uma `Item 0` string.
4. Defina `URL Schemes` >> `Item 0` para seu esquema personalizado.

Alternativamente, se você deseja editar seu arquivo`Info.plist` diretamente, siga esta especificação:

```html
<key>CFBundleURLTypes</key>
<array>
    <dict>
        <key>CFBundleURLName</key>
        <string>YOUR.SCHEME</string>
        <key>CFBundleURLSchemes</key>
        <array>
            <string>YOUR.SCHEME</string>
        </array>
    </dict>
</array>
```

## Etapa 2: Adição de uma lista de permissões de esquema

Você deve declarar os esquemas de URL que deseja passar para `canOpenURL(_:)` adicionando a chave `LSApplicationQueriesSchemes` ao arquivo Info.plist do seu app. Tentar chamar esquemas fora desta lista de permissão fará com que o sistema registre um erro nos logs do dispositivo, e o deep link não abrirá. Um exemplo desse erro é o seguinte:

```
<Warning>: -canOpenURL: failed for URL: "yourapp://deeplink" – error: "This app is not allowed to query for scheme yourapp"
```

Por exemplo, se uma mensagem no app deve abrir o aplicativo do Facebook ao ser tocada, o app deve ter o esquema personalizado do Facebook (`fb`) em sua lista de permissões. Caso contrário, o sistema rejeitará o deep link. Os deep linkings que direcionam para uma página ou exibição dentro do seu próprio aplicativo ainda exigem que o esquema personalizado do seu aplicativo seja listado no site `Info.plist`.

Seu exemplo de lista de permissões pode ser algo como:

```html
<key>LSApplicationQueriesSchemes</key>
<array>
    <string>myapp</string>
    <string>fb</string>
    <string>twitter</string>
</array>
```

Para saber mais, consulte [a documentação da Apple](https://developer.apple.com/library/content/documentation/General/Reference/InfoPlistKeyReference/Articles/LaunchServicesKeys.html#//apple_ref/doc/uid/TP40009250-SW14) sobre a tecla `LSApplicationQueriesSchemes`.

## Etapa 3: Implementar um manipulador

Depois de ativar seu app, o iOS chamará o método [`application:openURL:options:`](https://developer.apple.com/reference/uikit/uiapplicationdelegate/1623112-application?language=objc). O argumento importante é o objeto [NSURL](https://developer.apple.com/library/ios/DOCUMENTATION/Cocoa/Reference/Foundation/Classes/NSURL_Class/Reference/Reference.html#//apple_ref/doc/c_ref/NSURL).

{% tabs %}
{% tab swift %}

```swift
func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
  let path = url.path
  let query = url.query
  // Insert your code here to take some action based upon the path and query.
  return true
}
```

{% endtab %}
{% tab OBJECTIVE C %}

```objc
- (BOOL)application:(UIApplication *)app openURL:(NSURL *)url options:(NSDictionary<UIApplicationOpenURLOptionsKey, id> *)options {
  NSString *path  = [url path];
  NSString *query = [url query];
  // Insert your code here to take some action based upon the path and query.
  return YES;
}
```

{% endtab %}
{% endtabs %}

## Segurança de transporte de aplicativos (ATS)

### Requisitos do ATS
Da [documentação da Apple](https://developer.apple.com/library/prerelease/ios/releasenotes/General/WhatsNewIniOS/Articles/iOS9.html#//apple_ref/doc/uid/TP40016198-SW14): "O App Transport Security é um recurso que melhora a segurança das conexões entre um app e os serviços da Web. O recurso consiste em requisitos de conexão padrão que estão em conformidade com as melhores práticas para conexões seguras. Os apps podem substituir esse comportamento padrão e desativar a segurança de transporte."

O ATS é aplicado por padrão. Requer que todas as conexões usem HTTPS e sejam criptografadas usando TLS 1.2 com sigilo direto. Consulte [Requisitos para Conexão Usando ATS](https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW35) para saber mais. Todas as imagens servidas pela Braze para dispositivos finais são gerenciadas por uma rede de entrega de conteúdo ("CDN") que suporta TLS 1.2 e é compatível com ATS.

A menos que sejam especificadas como exceções em seu `Info.plist`, as conexões que não seguirem esses requisitos falharão com erros que se parecem com isto:

```
CFNetwork SSLHandshake failed (-9801)
Error Domain=NSURLErrorDomain Code=-1200 "An SSL error has occurred, and a secure connection to the server cannot be made."
```

```
NSURLSession/NSURLConnection HTTP load failed (kCFStreamErrorDomainSSL, -9802)
```

A conformidade com ATS é aplicada para links abertos dentro do app móvel (nosso tratamento padrão de links clicados) e não se aplica a sites abertos externamente por meio de um navegador da web.

### Atendendo aos requisitos do ATS

Você pode lidar com ATS de uma das três maneiras a seguir:

#### Certifique-se de que todos os links estejam em conformidade com o ATS (recomendado)
Sua integração com a Braze pode atender aos requisitos do ATS, garantindo que todos os links existentes para os quais você direciona os usuários (por exemplo, por meio de mensagens no app e campanhas de mensagens) atendam aos requisitos do ATS. Embora existam maneiras de contornar as restrições do ATS, nossa recomendação é garantir que todos os URLs vinculados estejam em conformidade com o ATS. Dada a crescente ênfase da Apple na segurança dos aplicativos, as seguintes abordagens para permitir exceções de ATS não têm garantia de suporte da Apple.

#### Desativar parcialmente o ATS
Você pode permitir que um subconjunto de links com determinados domínios ou esquemas sejam tratados como exceções às regras do ATS. Sua integração com o Braze atenderá aos requisitos do ATS se todos os links usados em um canal de envio de mensagens do Braze estiverem em conformidade com o ATS ou forem tratados por uma exceção.

Para adicionar um domínio como exceção do ATS, adicione o seguinte ao arquivo `Info.plist` do seu app:

```html
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>
    <key>NSExceptionDomains</key>
    <dict>
        <key>example.com</key>
        <dict>
            <key>NSExceptionAllowsInsecureHTTPLoads</key>
            <false/>
            <key>NSIncludesSubdomains</key>
            <true/>
        </dict>
    </dict>
</dict>
```

Consulte o artigo da Apple sobre [[chaves de segurança de transporte de app](https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW33) para saber mais.

#### Desativar totalmente o ATS

Você pode desativar o ATS completamente. Note que essa não é uma prática recomendada, devido à perda de proteções de segurança e à compatibilidade futura com o iOS. Para desativar o ATS, insira o seguinte no arquivo `Info.plist` do seu app:

```html
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>
</dict>
```

## Codificação de URL

O SDK codifica os links em porcentagem para criar `URL`s válidos. Todos os caracteres de link que não são permitidos em um URL devidamente formado, como caracteres Unicode, serão escapados por porcentagem.

Para decodificar um link codificado, use a propriedade `String` [`removingPercentEncoding`](https://developer.apple.com/documentation/swift/stringprotocol/removingpercentencoding). Você também deve retornar `true` em `BrazeDelegate.braze(_:shouldOpenURL:)`. Uma chamada para ação é necessária para disparar o tratamento da URL pelo seu aplicativo. 

Por exemplo:

{% tabs %}
{% tab swift %}

```swift
  func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
    let urlString = url.absoluteString.removingPercentEncoding
    // Handle urlString
    return true
  }
```

{% endtab %}
{% tab OBJECTIVE C %}

```objc
- (BOOL)application:(UIApplication *)application openURL:(NSURL *)url options:(NSDictionary<NSString *, id> *)options {
  NSString *urlString = [url.absoluteString stringByRemovingPercentEncoding];
  // Handle urlString
  return YES;
}
```

{% endtab %}
{% endtabs %}


## Deep links para as configurações do app

Você pode aproveitar o `UIApplicationOpenSettingsURLString` para fazer um deep linking entre os usuários e as configurações do seu app a partir de notificações por push do Braze, mensagens no app e feed de notícias.

Para levar os usuários do seu app para as configurações do iOS:
1. Primeiro, confira se o seu aplicativo está configurado para [[links profundos baseados em esquema](##step-1-registering-a-scheme) ou [[links universais](#universal-links).
2. Decida sobre um URI para deep linking para a página de **Configurações** (por exemplo, `myapp://settings` ou `https://www.braze.com/settings`).
3. Se você estiver usando links profundos baseados em esquemas personalizados, adicione o seguinte código ao seu método `application:openURL:options:`:

{% tabs %}
{% tab swift %}

```swift
func application(_ app: UIApplication, open url: URL, options: [UIApplicationOpenURLOptionsKey : Any] = [:]) -> Bool {
  let path = url.path
  if (path == "settings") {
    UIApplication.shared.openURL(URL(string:UIApplication.openSettingsURLString)!)
  }
  return true
}
```

{% endtab %}
{% tab OBJECTIVE C %}

```objc
- (BOOL)application:(UIApplication *)app
            openURL:(NSURL *)url
            options:(NSDictionary<UIApplicationOpenURLOptionsKey,id> *)options {
  NSString *path  = [url path];
  if ([path isEqualToString:@"settings"]) {
    NSURL *settingsURL = [NSURL URLWithString:UIApplicationOpenSettingsURLString];
    [[UIApplication sharedApplication] openURL:settingsURL];
  }
  return YES;
}
```

{% endtab %}
{% endtabs %}

## Personalização {#linking-customization}

### Personalização padrão do WebView

A classe `Braze.WebViewController` exibe URLs da web abertas pelo SDK, normalmente quando "Abrir URL da Web Dentro do App" é selecionado para um deep link da web.

Você pode personalizar `Braze.WebViewController` por meio do método delegado [`BrazeDelegate.braze(_:willPresentModalWithContext:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate/braze(_:willpresentmodalwithcontext:)-12sqy/).

### Personalização do manuseio de links

O protocolo `BrazeDelegate` pode ser usado para personalizar o tratamento de URLs, como deep links, URLs da web e links universais. Para definir o delegado durante a inicialização da Braze, defina um objeto delegado na instância `Braze`. A Braze chamará a implementação de seu delegado em `shouldOpenURL` antes de manipular quaisquer URIs.

#### Links universais

O Braze oferece suporte a links universais em notificações por push, mensagens no app e cartões de conteúdo. Para ativar o suporte a links universais, [`configuration.forwardUniversalLinks`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/forwarduniversallinks) deve ser definido como `true`.

Quando ativada, a Braze encaminhará links universais para o `AppDelegate` do seu app por meio do método [`application:continueUserActivity:restorationHandler:`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623072-application). 

Seu aplicativo também precisa ser configurado para lidar com links universais. Consulte a [documentação da Apple](https://developer.apple.com/documentation/xcode/supporting-universal-links-in-your-app) para garantir que seu aplicativo esteja configurado corretamente para links universais.

{% alert warning %}
O encaminhamento de links universais requer acesso aos direitos do aplicativo. Ao executar o aplicativo em um simulador, esses direitos não estão diretamente disponíveis e os links universais não são encaminhados para os manipuladores do sistema.
Para adicionar suporte às compilações do simulador, você pode adicionar o arquivo `.entitlements` do aplicativo à fase de compilação _Copy Bundle Resources_. Para saber mais, consulte a documentação [`forwardUniversalLinks`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/forwarduniversallinks).
{% endalert %}

{% alert note %}
O SDK não consulta o arquivo `apple-app-site-association` de seus domínios. Ele realiza a diferenciação entre links universais e URLs regulares observando apenas o nome do domínio. Como resultado, o SDK não respeita nenhuma regra de exclusão definida em `apple-app-site-association` conforme [Suporte a domínios associados](https://developer.apple.com/documentation/xcode/supporting-associated-domains).
{% endalert %}

### Exemplo de integração: BrazeDelegate

{% tabs %}
{% tab swift %}

```swift
func braze(_ braze: Braze, shouldOpenURL context: Braze.URLContext) -> Bool {
  if context.url.host == "MY-DOMAIN.com" {
    // Custom handle link here
    return false
  }
  // Let Braze handle links otherwise
  return true
}
```

{% endtab %}
{% tab OBJECTIVE C %}

```objc
- (BOOL)braze:(Braze *)braze shouldOpenURL:(BRZURLContext *)context {
  if ([[context.url.host lowercaseString] isEqualToString:@"MY-DOMAIN.com"]) {
    // Custom handle link here
    return NO;
  }
  // Let Braze handle links otherwise
  return YES;
}
```

{% endtab %}
{% endtabs %}

Para saber mais, consulte [`BrazeDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate).


