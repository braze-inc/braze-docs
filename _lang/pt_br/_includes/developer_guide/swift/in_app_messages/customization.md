{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Configuração do delegado da interface do usuário (obrigatório)

Para personalizar a apresentação das mensagens no app e reagir a vários eventos do ciclo de vida, você precisará configurar o [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate). Esse é um protocolo delegado usado para receber e processar cargas úteis de mensagens no app disparadas, receber eventos do ciclo de vida da tela e controlar o tempo de exibição. Para usar o `BrazeInAppMessageUIDelegate`, você deve:
- Use a implementação padrão [`BrazeInAppMessageUI`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui) como sua `inAppMessagePresenter`. 
- Inclua a biblioteca `BrazeUI` em seu projeto.

### Etapa 1: Implementar o protocolo `BrazeInAppMessageUIDelegate`  

Primeiro, implemente o protocolo `BrazeInAppMessageUIDelegate` e os métodos correspondentes que você desejar. Em nosso exemplo abaixo, estamos implementando esse protocolo na classe `AppDelegate` do nosso aplicativo.

{% tabs %}
{% tab swift %}
```swift
extension AppDelegate: BrazeInAppMessageUIDelegate {
  // Implement your protocol methods here.
}
```
{% endtab %}
{% tab OBJECTIVE C %}
```objc
@interface AppDelegate () <BrazeInAppMessageUIDelegate>

@end

@implementation AppDelegate
  // Implement your protocol methods here.
@end
```
{% endtab %}
{% endtabs %}

### Etapa 2: Atribuir o objeto `delegate`  

Atribua o objeto `delegate` na instância do app `BrazeInAppMessageUI` antes de atribuir essa mensagem no app UI como seu `inAppMessagePresenter`.

{% tabs %}
{% tab swift %}
```swift
let inAppMessageUI = BrazeInAppMessageUI()
inAppMessageUI.delegate = self
AppDelegate.braze?.inAppMessagePresenter = inAppMessageUI
```
{% endtab %}
{% tab OBJECTIVE C %}
```objc
BrazeInAppMessageUI *inAppMessageUI = [[BrazeInAppMessageUI alloc] init];
inAppMessageUI.delegate = self;
AppDelegate.braze.inAppMessagePresenter = inAppMessageUI;
```

{% alert important %}
Nem todos os métodos delegados estão disponíveis em Objective C devido à incompatibilidade de seus parâmetros com o tempo de execução da linguagem.
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert tip %}
Para obter uma implementação passo a passo do delegado da UI de mensagens no app, consulte este [tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).
{% endalert %}

## Comportamento ao clicar

Cada objeto `Braze.InAppMessage` contém um objeto [`ClickAction`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/clickaction)correspondente, que define o comportamento ao clicar. 

### Clique nos tipos de ação

A propriedade `clickAction` em seu `Braze.InAppMessage` tem como padrão `.none`, mas pode ser definida como um dos seguintes valores:

| `ClickAction` | Comportamento ao clicar |
| -------------------------- | -------- |
| `.url(URL, useWebView: Bool)` | Abre o URL fornecido em um navegador externo. Se `useWebView` estiver definido como `true`, ele será aberto em uma visualização da Web. |
| `.newsFeed` | O feed de notícias será exibido quando a mensagem for clicada, e a mensagem será descartada.<br><br>**Nota:** O Feed de notícias está sendo descontinuado. Consulte o [guia de migração]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) para obter mais detalhes. |
| `.none` | A mensagem será descartada quando for clicada. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Para mensagens no app contendo botões, a mensagem `clickAction` também será incluída na carga útil final se a ação de clique for adicionada antes de adicionar o texto do botão.
{% endalert %}

### Personalização do comportamento ao clicar

Para personalizar esse comportamento, você pode modificar a propriedade `clickAction` consultando o exemplo a seguir:

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI, 
  prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
  if let newUrl = URL(string: "{your-url}") {
    context.message.clickAction = .url(newUrl, useWebView: true)
  }
}
```

{% endtab %}
{% tab OBJECTIVE C %}

O método `inAppMessage(_:prepareWith:)` não está disponível em Objective C.

{% endtab %}
{% endtabs %}

### Manipulação do comportamento personalizado

O seguinte método [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate) é chamado quando uma mensagem no app é clicada. Para cliques em botões de mensagens no app e botões de mensagens no app em HTML (links), um ID de botão é fornecido como um parâmetro opcional.

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  shouldProcess clickAction: Braze.InAppMessage.ClickAction,
  buttonId: String?,
  message: Braze.InAppMessage,
  view: InAppMessageView
) -> Bool
```

{% endtab %}
{% tab OBJECTIVE C %}

```objc
- (BOOL)inAppMessage:(BrazeInAppMessageUI *)ui
       shouldProcess:(enum BRZInAppMessageRawClickAction)clickAction
                 url:(NSURL *)uri
            buttonId:(NSString *)buttonId
             message:(BRZInAppMessageRaw *)message
                view:(UIView *)view;
```

{% endtab %}
{% endtabs %}

Esse método retorna um valor booleano para indicar se o Braze deve continuar a executar a ação de clique.

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI, shouldProcess clickAction: Braze.InAppMessage.ClickAction,
  buttonId: String?, message: Braze.InAppMessage, view: InAppMessageView
) -> Bool {
    guard let buttonId,
      let idInt = Int(buttonId)
    else { return true }
    var button: BrazeKit.Braze.InAppMessage.Button? = nil

    switch message {
    case .modal(let modal):
      button = modal.buttons[idInt]

    case .modalImage(let modalImage):
      button = modalImage.buttons[idInt]

    case .full(let full):
      button = full.buttons[idInt]

    case .fullImage(let fullImage):
      button = fullImage.buttons[idInt]

    default:
      break
    }
    
    print(button?.id)
    print(button?.text)
    print(button?.clickAction)

    return true
  }
```

{% endtab %}
{% tab OBJECTIVE C %}
```objc
- (BOOL)inAppMessage:(BrazeInAppMessageUI *)ui
       shouldProcess:(enum BRZInAppMessageRawClickAction)clickAction
                 url:(NSURL *)uri
            buttonId:(NSString *)buttonId
             message:(BRZInAppMessageRaw *)message
                view:(UIView *)view {
  NSInteger buttonInt = [buttonId integerValue];

  if (message.type == BRZInAppMessageRawTypeFull || message.type == BRZInAppMessageRawTypeModal) {
    BRZInAppMessageRawButton *button = message.buttons[buttonInt];
    NSLog(@"%ld", (long)button.identifier);
    NSLog(@"%@", button.text);
    NSLog(@"%ld", (long)button.clickAction);
  }
  return YES;
}
```

{% endtab %}
{% endtabs %}

## Personalização de dispensas modais

Para ativar a dispensa por toques externos, você pode modificar a propriedade `dismissOnBackgroundTap` na estrutura `Attributes` do tipo de mensagem no app que deseja personalizar. 

Por exemplo, se quiser ativar esse recurso para mensagens no app com imagens modais, você pode configurar o seguinte:

{% tabs %}
{% tab swift %}

```swift
BrazeInAppMessageUI.ModalImageView.Attributes.defaults.dismissOnBackgroundTap = true
```

{% endtab %}
{% tab OBJECTIVE C %}

A personalização via `Attributes` não está disponível em Objective C.

{% endtab %}
{% endtabs %}

O valor padrão é `false`. Isso determina se o modal será descartado quando o usuário tocar fora da mensagem no app.

| `DismissModalOnOutsideTap` | Descrição |
|----------|-------------|
| `true`         | Os modais de mensagens no app serão descartados com um toque externo.     |
| `false`        | Por padrão, as mensagens modais no app não serão descartadas com um toque externo. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para saber mais sobre a personalização de mensagens no app, consulte este [artigo](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/in-app-message-customization).

## Personalização da orientação das mensagens

Você pode personalizar a orientação de suas mensagens no app. Você pode definir uma nova orientação padrão para todas as mensagens ou definir uma orientação personalizada para uma única mensagem.

{% tabs local %}
{% tab todos os envios de mensagens %}
Para escolher uma orientação padrão para todas as mensagens no app, use o método [`inAppMessage(_:prepareWith:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) para definir a propriedade `preferredOrientation` no site `PresentationContext`. 

Por exemplo, para definir retrato como a orientação padrão:

{% subtabs %}
{% subtab swift %}
```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
  context.preferredOrientation = .portrait
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
- (void)inAppMessage:(BrazeInAppMessageUI *)ui
         prepareWith:(BrazeInAppMessageUIPresentationContextRaw *)context {
  context.preferredOrientation = BRZInAppMessageRawOrientationPortrait;
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab mensagem única %}
Para definir a orientação de uma única mensagem, modifique a propriedade `orientation` de `Braze.InAppMessage`:

{% subtabs %}
{% subtab swift %}

```swift
// Set inAppMessage orientation to support any configuration
inAppMessage.orientation = .any

// Set inAppMessage orientation to only display in portrait
inAppMessage.orientation = .portrait

// Set inAppMessage orientation to only display in landscape
inAppMessage.orientation = .landscape
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
// Set inAppMessage orientation to support any configuration
inAppMessage.orientation = BRZInAppMessageRawOrientationAny;

// Set inAppMessage orientation to only display in portrait
inAppMessage.orientation = BRZInAppMessageRawOrientationPortrait;

// Set inAppMessage orientation to only display in landscape
inAppMessage.orientation = BRZInAppMessageRawOrientationLandscape;
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

Depois que a mensagem no app for exibida, qualquer mudança de orientação do dispositivo enquanto a mensagem ainda estiver sendo exibida fará com que a mensagem gire com o dispositivo (desde que seja compatível com a configuração `orientation` da mensagem).

A orientação do dispositivo também deve ser compatível com a propriedade `orientation` da mensagem no app para que a mensagem seja exibida. Além disso, a configuração `preferredOrientation` só será respeitada se estiver incluída nas orientações de interface compatíveis com seu aplicativo na seção **Informações de implementação** das configurações do seu direcionamento no Xcode.

![Orientações suportadas no Xcode.]({% image_buster /assets/img/supported_interface_orientations_xcode.png %})

{% alert note %}
A orientação é aplicada apenas para a apresentação da mensagem. Depois que o dispositivo muda de orientação, a visualização de mensagens adota uma das orientações compatíveis. Em dispositivos menores (iPhones, iPod Touch), definir uma orientação paisagem para uma mensagem modal ou completa no app pode resultar em conteúdo truncado.
{% endalert %}

## Personalização do tempo de exibição 

É possível controlar se uma mensagem no app disponível será exibida durante determinados pontos da experiência do usuário. Se houver situações em que você não queira que a mensagem no app seja exibida, como durante um jogo em tela cheia ou em uma tela de carregamento, é possível postergar ou descartar mensagens pendentes de mensagens no app. Para controlar o tempo da mensagem no app, use o [método delegado](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) `inAppMessage(_:displayChoiceForMessage:)` para definir a propriedade `BrazeInAppMessageUI.DisplayChoice`. 

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  displayChoiceForMessage message: Braze.InAppMessage
) -> BrazeInAppMessageUI.DisplayChoice
```

{% endtab %}
{% tab OBJECTIVE C %}

```objc
- (enum BRZInAppMessageUIDisplayChoice)inAppMessage:(BrazeInAppMessageUI *)ui displayChoiceForMessage:(BRZInAppMessageRaw *)message
```

{% endtab %}
{% endtabs %}

Configure o site `BrazeInAppMessageUI.DisplayChoice` para retornar um dos seguintes valores:

| Opção de exibição                      | Comportamento                                                                                                                    |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `.now`                              | A mensagem será exibida imediatamente. Esse é o valor padrão.                                                       |
| `.reenqueue`                        | A mensagem não será exibida e será colocada de volta no topo da pilha.                                       |
| `.later`                            | A mensagem não será exibida e será colocada de volta no topo da pilha. (Descontinuado, use `.reenqueue`) |
| `.discard`                          | A mensagem será descartada e não será exibida.                                                                    |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Para obter um exemplo do site `InAppMessageUI`, consulte nosso [repositório Swift Braze SDK](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift/Sources/InAppMessageUI) e [Objective C](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/ObjC/Sources/InAppMessageUI).
{% endalert %}

## Ocultação da barra de status

Para mensagens no app `Full`, `FullImage` e `HTML`, o SDK ocultará a barra de status por padrão. Para outros tipos de mensagens no app, a barra de status não é alterada. Para configurar esse comportamento, use [o método delegado](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) `inAppMessage(_:prepareWith:)` para definir a propriedade `statusBarHideBehavior` em `PresentationContext`. Esse campo assume um dos seguintes valores:

| Comportamento de ocultação da barra de status            | Descrição                                                                           |
| ----------------------------------- | ------------------------------------------------------------------------------------- |
| `.auto`                             | A exibição de mensagens decide o estado oculto da barra de status.                                 |
| `.hidden`                           | Sempre oculte a barra de status.                                                           |
| `.visible`                          | Sempre exibir a barra de status.                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Desativar o modo escuro

Para evitar que as mensagens no app adotem o estilo do modo escuro quando o dispositivo do usuário tiver o modo escuro ativado, implemente o método `inAppMessage(_:prepareWith:)` [delegate method](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog). O `PresentationContext` passado para o método contém uma referência ao objeto `InAppMessage` a ser apresentado. Cada `InAppMessage` tem uma propriedade `themes` que contém um tema de modo `dark` e `light`. Se você definir a propriedade `themes.dark` como `nil`, a Braze apresentará automaticamente a mensagem no app usando seu tema claro.

Os tipos de mensagens no app com botões têm um objeto `themes` adicional em sua propriedade `buttons`. Para evitar que os botões adotem o estilo do modo escuro, você pode usar [`map(_:)`](https://developer.apple.com/documentation/swift/array/map(_:)-87c4d) para criar uma nova matriz de botões com um tema `light` e nenhum tema `dark`.

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
  switch context.message {
    case .slideup:
      guard var slideup = context.message.slideup else { return }
      slideup.themes.dark = nil
      context.message.slideup = slideup
    
    case .modal:
      guard var modal = context.message.modal else { return }
      modal.themes.dark = nil
      modal.buttons = modal.buttons.map {
        var newButton = $0
        newButton.themes = .init(themes: ["light": $0.themes.light])
        return newButton
      }
      context.message.modal = modal
    
    case .modalImage:
      guard var modalImage = context.message.modalImage else { return }
      modalImage.themes.dark = nil
      modalImage.buttons = modalImage.buttons.map {
        var newButton = $0
        newButton.themes = .init(themes: ["light": $0.themes.light])
        return newButton
      }
      context.message.modalImage = modalImage
    
    case .full:
      guard var full = context.message.full else { return }
      full.themes.dark = nil
      full.buttons = full.buttons.map {
        var newButton = $0
        newButton.themes = .init(themes: ["light": $0.themes.light])
        return newButton
      }
      context.message.full = full
    
    case .fullImage:
      guard var fullImage = context.message.fullImage else { return }
      fullImage.themes.dark = nil
      fullImage.buttons = fullImage.buttons.map {
        var newButton = $0
        newButton.themes = .init(themes: ["light": $0.themes.light])
        return newButton
      }
      context.message.fullImage = fullImage
    
    default:
      break
  }
}
```

{% endtab %}
{% tab OBJECTIVE C %}

```objc
- (void)inAppMessage:(BrazeInAppMessageUI *)ui
         prepareWith:(BrazeInAppMessageUIPresentationContextRaw *)context {
  switch (context.message.type) {
    case BRZInAppMessageRawTypeSlideup: {
      NSMutableDictionary *updatedThemes = [context.message.themes mutableCopy];
      [updatedThemes removeObjectForKey:@"dark"];
      context.message.themes = updatedThemes;
      break;
    }
    case BRZInAppMessageRawTypeModal:
    case BRZInAppMessageRawTypeFull:
    {
      NSMutableDictionary *updatedThemes = [context.message.themes mutableCopy];
      [updatedThemes removeObjectForKey:@"dark"];
      context.message.themes = updatedThemes;

      NSMutableArray *updatedButtons = [NSMutableArray arrayWithCapacity:context.message.buttons.count];
      for (BRZInAppMessageRawButton *button in context.message.buttons) {
        BRZInAppMessageRawButtonTheme *lightTheme = BRZInAppMessageRawButtonTheme.defaultLight;
        BRZInAppMessageRawButton *newButton = [button mutableCopy];
        newButton.textColor = lightTheme.textColor;
        newButton.backgroundColor = lightTheme.backgroundColor;
        newButton.borderColor = lightTheme.borderColor;
        [updatedButtons addObject:newButton];
      }
      context.message.buttons = updatedButtons;
      break;
    }
    default:
      break;
  }
}
```

{% endtab %}
{% endtabs %}

## Personalização do prompt de revisão da loja de aplicativos

É possível usar mensagens no app em uma campanha para solicitar aos usuários uma avaliação da App Store.

{% alert note %}
Como este exemplo de prompt substitui o comportamento padrão da Braze, não podemos rastrear impressões automaticamente se ele for implementado. Você deve [registrar suas próprias análises de dados]({{site.baseurl}}/developer_guide/analytics/).
{% endalert %}

### Etapa 1: Defina o delegado de mensagem no app

Primeiro, defina o [`BrazeInAppMessageUIDelegate`]({{site.baseurl}}/developer_guide/in_app_messages/customization/#swift_setting-up-the-ui-delegate-required) em seu app. 

### Etapa 2: Desativar a mensagem padrão de avaliação da App Store

Em seguida, implemente o [método delegado](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) `inAppMessage(_:displayChoiceForMessage:)` para desativar a mensagem padrão de revisão da App Store.

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(_ ui: BrazeInAppMessageUI, displayChoiceForMessage message: Braze.InAppMessage) -> BrazeInAppMessageUI.DisplayChoice {
  if message.extras["AppStore Review"] != nil,
    let messageUrl = message.clickAction.url {
      UIApplication.shared.open(messageUrl, options: [:], completionHandler: nil)
      return .discard
  } else {
    return .now
  }
}
```

{% endtab %}
{% tab OBJECTIVE C %}

```objc
- (enum BRZInAppMessageUIDisplayChoice)inAppMessage:(BrazeInAppMessageUI *)ui
                            displayChoiceForMessage:(BRZInAppMessageRaw *)message {
  if (message.extras != nil && message.extras[@"AppStore Review"] != nil) {
    [[UIApplication sharedApplication] openURL:message.url options:@{} completionHandler:nil];
    return BRZInAppMessageUIDisplayChoiceDiscard;
  } else {
    return BRZInAppMessageUIDisplayChoiceNow;
  }
}
```

{% endtab %}
{% endtabs %}

### Etapa 3: Criar um deep link

No código de tratamento do deep link, adicione o seguinte código para processar o deep link `{YOUR-APP-SCHEME}:app-store-review`. Note que você precisará importar `StoreKit` para usar `SKStoreReviewController`:

{% tabs %}
{% tab swift %}

```swift
func application(_ app: UIApplication, open url: URL, options: [UIApplicationOpenURLOptionsKey : Any] = [:]) -> Bool {
  let urlString = url.absoluteString.removingPercentEncoding
  if (urlString == "{YOUR-APP-SCHEME}:app-store-review") {
    SKStoreReviewController.requestReview()
    return true;
  }
  // Other deep link handling code…
}
```

{% endtab %}
{% tab OBJECTIVE C %}

```objc
- (BOOL)application:(UIApplication *)app openURL:(NSURL *)url options:(NSDictionary<UIApplicationOpenURLOptionsKey, id> *)options {
  NSString *urlString = url.absoluteString.stringByRemovingPercentEncoding;
  if ([urlString isEqualToString:@"{YOUR-APP-SCHEME}:app-store-review"]) {
    [SKStoreReviewController requestReview];
    return YES;
  }
  // Other deep link handling code…
}
```

{% endtab %}
{% endtabs %}

{% raw %}

### Etapa 4: Definir comportamento personalizado ao clicar

Em seguida, crie uma campanha de envio de mensagens no app com o seguinte:

- O par chave-valor `"AppStore Review" : "true"`
- O comportamento ao clicar está definido como "Deep Link Into App", utilizando o deep link `{YOUR-APP-SCHEME}:app-store-review`.

{% endraw %}

{% alert tip %}
A Apple limita os avisos de revisão da App Store a um máximo de três vezes por ano para cada usuário, portanto, sua campanha deve ser [limitada de frequência]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/) a três vezes por ano por usuário.<br><br>Os usuários podem desativar os avisos de revisão da App Store. Como resultado, seu prompt de avaliação personalizado não deve prometer que um prompt de avaliação nativo da App Store aparecerá ou solicitar diretamente uma avaliação.
{% endalert %}
