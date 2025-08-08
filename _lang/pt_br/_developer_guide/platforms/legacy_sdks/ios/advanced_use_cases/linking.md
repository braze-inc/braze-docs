---
nav_title: Deep linking
article_title: deep linking para iOS
platform: iOS
page_order: 0
description: "Este artigo cobre como implementar o delegado de deep linking universal para seu app iOS e exemplos de como fazer deep link para as configurações do app."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Deep linking para iOS

Para obter informações introdutórias sobre links profundos, consulte nosso [artigo do Guia do Usuário]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking). Se você está procurando implementar links profundos pela primeira vez no seu app da Braze, os passos abaixo te ajudarão a começar.

## Etapa 1: Registrar um esquema

Você deve declarar um esquema personalizado no arquivo `Info.plist`. A estrutura de navegação é definida por um vetor de dicionários. Cada um desses dicionários contém um vetor de strings.

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
        <string>{YOUR.SCHEME}</string>
        <key>CFBundleURLSchemes</key>
        <array>
            <string>{YOUR.SCHEME}</string>
        </array>
    </dict>
</array>
```

## Etapa 2: Permitir a lista de permissões do esquema personalizado (iOS 9+)

A partir do iOS 9, os apps devem ter uma lista de permissões de esquemas personalizados que o app tem permissão para abrir. Tentar chamar esquemas fora desta lista fará com que o sistema registre um erro nos logs do dispositivo, e o deep link não abrirá. Um exemplo desse erro se parece com isso:

```
<Warning>: -canOpenURL: failed for URL: "yourapp://deeplink" – error: "This app is not allowed to query for scheme yourapp"
```

Por exemplo, se uma mensagem no app deve abrir o app do Facebook quando tocada, o app precisa ter o esquema personalizado do Facebook (`fb`) na lista de permissões. Caso contrário, o sistema rejeitará o deep link. Links diretos que direcionam para uma página ou visualização dentro do seu próprio app ainda exigem que o esquema personalizado do seu app esteja listado no `Info.plist` do seu app.

Você deve adicionar todos os esquemas que o app precisa para fazer deep linking em uma lista de permissões no `Info.plist` do seu app com a chave `LSApplicationQueriesSchemes`. Por exemplo:

```html
<key>LSApplicationQueriesSchemes</key>
<array>
    <string>myapp</string>
    <string>facebook</string>
    <string>twitter</string>
</array>
```

Para saber mais, consulte [a documentação da Apple](https://developer.apple.com/library/content/documentation/General/Reference/InfoPlistKeyReference/Articles/LaunchServicesKeys.html#//apple_ref/doc/uid/TP40009250-SW14) sobre a tecla `LSApplicationQueriesSchemes`.

## Etapa 3: Implementar um manipulador

Depois de ativar seu app, o iOS chamará o método [`application:openURL:options:`](https://developer.apple.com/reference/uikit/uiapplicationdelegate/1623112-application?language=objc). O argumento importante é o objeto [NSURL](https://developer.apple.com/library/ios/DOCUMENTATION/Cocoa/Reference/Foundation/Classes/NSURL_Class/Reference/Reference.html#//apple_ref/doc/c_ref/NSURL).

{% tabs %}
{% tab OBJECTIVE C %}

```objc
- (BOOL)application:(UIApplication *)app openURL:(NSURL *)url options:(NSDictionary<UIApplicationOpenURLOptionsKey, id> *)options {
  NSString *path  = [url path];
  NSString *query = [url query];
  // Here you should insert code to take some action based upon the path and query.
  return YES;
}
```

{% endtab %}
{% tab swift %}

```swift
func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
  let path = url.path
  let query = url.query
  // Here you should insert code to take some action based upon the path and query.
  return true
}
```

{% endtab %}
{% endtabs %}

![]({% image_buster /assets/img_archive/deep_link.png %})

# Links universais

Para usar links universais, certifique-se de que você adicionou um domínio registrado às capacidades do seu app e fez o upload de um `apple-app-site-association` arquivo. Em seguida, implemente o método `application:continueUserActivity:restorationHandler:` no seu `AppDelegate`. Por exemplo:

{% tabs %}
{% tab OBJECTIVE C %}

```objc
- (BOOL)application:(UIApplication *)application
continueUserActivity:(NSUserActivity *)userActivity
  restorationHandler:(void (^)(NSArray *restorableObjects))restorationHandler {
  if ([userActivity.activityType isEqualToString:NSUserActivityTypeBrowsingWeb]) {
    NSURL *url = userActivity.webpageURL;
    // Handle url
  }
  return YES;
}
```

{% endtab %}
{% tab swift %}

```swift
func application(_ application: UIApplication, continue userActivity: NSUserActivity, restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {
  if (userActivity.activityType == NSUserActivityTypeBrowsingWeb) {
    let url = userActivity.webpageURL
    // Handle url
  }
  return true
}
```

{% endtab %}
{% endtabs %}

Para saber mais, consulte a [Apple](https://developer.apple.com/library/content/documentation/General/Conceptual/AppSearch/UniversalLinks.html).

{% alert note %}
A integração de link universal padrão não é compatível com notificações por push da Braze ou mensagens no app. Consulte [personalização de links](#linking-handling-customization) para lidar com links universais dentro do seu aplicativo. Alternativamente, recomendamos o uso de [links profundos baseados em esquema](#step-1-registering-a-scheme) com notificações por push e mensagens no app.
{% endalert%}

## Segurança de transporte de app (ATS)
O iOS 9 introduziu uma mudança significativa que afeta URLs da web incorporadas em mensagens no app e notificações por push.

### Requisitos ATS
Da [documentação da Apple](https://developer.apple.com/library/prerelease/ios/releasenotes/General/WhatsNewIniOS/Articles/iOS9.html#//apple_ref/doc/uid/TP40016198-SW14): "O App Transport Security é um recurso que melhora a segurança das conexões entre um app e os serviços da Web. O recurso consiste em requisitos de conexão padrão que estão em conformidade com as melhores práticas para conexões seguras. Os aplicativos podem substituir esse comportamento padrão e desativar a segurança de transporte.

ATS é aplicado por padrão no iOS 9+. Requer que todas as conexões usem HTTPS e sejam criptografadas usando TLS 1.2 com sigilo direto. Consulte [Requisitos para Conexão Usando ATS](https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW35) para saber mais. Todas as imagens servidas pela Braze para dispositivos finais são gerenciadas por uma rede de entrega de conteúdo ("CDN") que suporta TLS 1.2 e é compatível com ATS.

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

#### Confirme se todos os links estão em conformidade com ATS (recomendado)
Sua integração com a Braze pode atender aos requisitos do ATS garantindo que quaisquer links existentes que você direcione os usuários (através de mensagens no app e campanhas de push) atendam aos requisitos do ATS. Embora existam maneiras de contornar as restrições do ATS, recomendamos verificar se todos os URLs vinculados estão em conformidade com o ATS. Dada a ênfase crescente da Apple à segurança de aplicativos, as seguintes abordagens para permitir exceções ATS podem não ser compatíveis.

Uma ferramenta SSL pode ajudá-lo a identificar problemas de segurança do servidor web. Esse [teste de servidor SSL](https://www.ssllabs.com/ssltest/index.html) da Qualys, Inc. fornece um item de linha especificamente para a conformidade com o Apple ATS 9 e o iOS 9.

#### Desativar parcialmente ATS
Você pode permitir que um subconjunto de links com determinados domínios ou esquemas sejam tratados como exceções às regras do ATS. Sua integração com a Braze atenderá aos requisitos do ATS se cada link que você usar em um canal de envio de mensagens da Braze for compatível com o ATS ou tratado por uma exceção.

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

Você pode desativar o ATS completamente. Nota que isso não é uma prática recomendada, devido tanto à perda de proteções de segurança quanto à compatibilidade futura com o iOS. Para desativar o ATS, insira o seguinte no arquivo `Info.plist` do seu app:

```html
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>
</dict>
```

Consulte [Envio de um app com App Transport Security](http://timekl.com/blog/2015/08/21/shipping-an-app-with-app-transport-security/?utm_campaign=iOS+Dev+Weekly&utm_medium=email&utm_source=iOS_Dev_Weekly_Issue_213) para obter mais informações sobre como depurar falhas de ATS.

## Codificação de URL

A partir do SDK da Braze para iOS v2.21.0, o SDK codifica percentualmente os links para criar `NSURL`s válidos. Todos os caracteres de link que não são permitidos em um URL devidamente formado, como caracteres Unicode, serão escapados por porcentagem.

Para decodificar um link codificado, use o `NSString` método [`stringByRemovingPercentEncoding`](https://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Classes/NSString_Class/index.html#//apple_ref/occ/instm/NSString/stringByRemovingPercentEncoding). Nota que você também precisa retornar `YES` no `ABKURLDelegate` e que uma chamada para ação é necessária para disparar o manuseio do URL pelo app. Por exemplo:

{% tabs %}
{% tab OBJECTIVE C %}

```objc
- (BOOL)application:(UIApplication *)application openURL:(NSURL *)url options:(NSDictionary<NSString *, id> *)options {
  NSString *urlString = url.absoluteString.stringByRemovingPercentEncoding;
  // Handle urlString
  return YES;
}
```

{% endtab %}
{% tab swift %}

```swift
  func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
    let urlString = url.absoluteString.removingPercentEncoding
    // Handle urlString
    return true
  }
```

{% endtab %}
{% endtabs %}

## Personalização {#linking-customization}

### Personalização padrão do WebView

A classe personalizável `ABKModalWebViewController` exibe URLs da web abertas pelo SDK, normalmente quando "Abrir URL da Web Dentro do App" é selecionado para um deep link da web.

Você pode declarar uma categoria para, ou modificar diretamente, a classe `ABKModalWebViewController` para aplicar a personalização à visualização da web. Verifique o arquivo [.h](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKModalWebViewController.h) e o arquivo [.m](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/ABKModalWebViewController.m) para mais detalhes.

### Personalização de manuseio de links

O protocolo `ABKURLDelegate` pode ser usado para personalizar o tratamento de URLs, como deep links, URLs da web e links universais. Para definir o delegado durante a inicialização do Braze, passe um objeto delegado para o `ABKURLDelegateKey` no `appboyOptions` de [`startWithApiKey:inApplication:withAppboyOptions:`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24). Braze chamará a implementação do seu delegado de `handleAppboyURL:fromChannel:withExtras:` antes de lidar com qualquer URI.

#### Exemplo de integração: ABKURLDelegate

{% tabs %}
{% tab OBJECTIVE C %}

```objc
- (BOOL)handleAppboyURL:(NSURL *)url fromChannel:(ABKChannel)channel withExtras:(NSDictionary *)extras {
  if ([[url.host lowercaseString] isEqualToString:@"MY-DOMAIN.com"]) {
    // Custom handle link here
    return YES;
  }
  // Let Braze handle links otherwise
  return NO;
}
```

{% endtab %}
{% tab swift %}

```swift
func handleAppboyURL(_ url: URL?, from channel: ABKChannel, withExtras extras: [AnyHashable : Any]?) -> Bool {
  if (url.host == "MY-DOMAIN.com") {
    // Custom handle link here
    return true;
  }
  // Let Braze handle links otherwise
  return false;
}
```

{% endtab %}
{% endtabs %}

Para saber mais, consulte [`ABKURLDelegate.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKURLDelegate.h).

## Casos de uso frequentes

### Deep linking para as configurações do app

O iOS pode levar os usuários do seu app para a sua página no aplicativo de configurações do iOS. Você pode aproveitar `UIApplicationOpenSettingsURLString` para fazer deep link de usuários para configurações a partir de notificações por push e mensagens no app.

1. Primeiro, confira se o seu aplicativo está configurado para [[links profundos baseados em esquema](#deep-links) ou [[links universais](#universal-links).
2. Decida sobre um URI para deep linking para a página de **Configurações** (por exemplo, `myapp://settings` ou `https://www.braze.com/settings`).
3. Se você estiver usando links profundos baseados em esquemas personalizados, adicione o seguinte código ao seu método `application:openURL:options:`:

{% tabs %}
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
{% tab swift %}

```swift
func application(_ app: UIApplication, open url: URL, options: [UIApplicationOpenURLOptionsKey : Any] = [:]) -> Bool {
  let path = url.path
  if (path == "settings") {
    UIApplication.shared.openURL(URL(string:UIApplicationOpenSettingsURLString)!)
  }
  return true
}
```

{% endtab %}
{% endtabs %}

