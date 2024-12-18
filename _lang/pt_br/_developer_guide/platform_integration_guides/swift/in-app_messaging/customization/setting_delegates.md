---
nav_title: Delegado da interface do usuário de mensagens no app
article_title: Delegado da interface do usuário de mensagens no app para iOS
platform: Swift
page_order: 2
description: "Este artigo de referência aborda a configuração de um delegate de envio de mensagens no app do iOS para o Swift SDK."
channel:
  - in-app messages

---

# Delegado da UI de mensagens no app

> Use o opcional [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate) para personalizar a apresentação de mensagens no app e reagir a vários eventos do ciclo de vida. Esse protocolo delegado pode ser usado para receber cargas úteis de mensagens no app disparadas para processamento adicional, receber eventos do ciclo de vida da exibição e controlar o tempo de exibição. 

## Pré-requisitos

Para usar `BrazeInAppMessageUIDelegate`:
* Você precisa estar usando a implementação padrão do [`BrazeInAppMessageUI`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui) padrão como seu `inAppMessagePresenter`. 
* Você deve incluir a biblioteca `BrazeUI` em seu projeto.

## Configuração do delegado de mensagem no app

Defina seu objeto [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate) delegado na instância da Braze seguindo este código de exemplo:

{% tabs %}
{% tab swift %}

Primeiro, implemente o protocolo `BrazeInAppMessageUIDelegate` e os métodos correspondentes que você desejar. Em nosso exemplo abaixo, estamos implementando esse protocolo na classe `AppDelegate` do nosso aplicativo.

```swift
extension AppDelegate: BrazeInAppMessageUIDelegate {
  // Implement your protocol methods here.
}
```

Em seguida, atribua o objeto `delegate` na instância do app `BrazeInAppMessageUI` antes de atribuir essa mensagem no app UI como seu `inAppMessagePresenter`.

```swift
let inAppMessageUI = BrazeInAppMessageUI()
inAppMessageUI.delegate = self
AppDelegate.braze?.inAppMessagePresenter = inAppMessageUI
```

{% endtab %}
{% tab OBJECTIVE C %}

Primeiro, implemente o protocolo `BrazeInAppMessageUIDelegate` e os métodos correspondentes que você desejar. Em nosso exemplo abaixo, estamos implementando esse protocolo na classe `AppDelegate` do nosso aplicativo.

```objc
@interface AppDelegate () <BrazeInAppMessageUIDelegate>

@end

@implementation AppDelegate
  // Implement your protocol methods here.
@end
```

Em seguida, atribua o objeto `delegate` na instância do app `BrazeInAppMessageUI` antes de atribuir essa mensagem no app UI como seu `inAppMessagePresenter`.

```objc
BrazeInAppMessageUI *inAppMessageUI = [[BrazeInAppMessageUI alloc] init];
inAppMessageUI.delegate = self;
AppDelegate.braze.inAppMessagePresenter = inAppMessageUI;
```

Nem todos os métodos delegados estão disponíveis em Objective C devido à incompatibilidade de seus parâmetros com o tempo de execução da linguagem.

{% endtab %}
{% endtabs %}

### Guia passo a passo

Para obter uma implementação passo a passo do delegado da UI de mensagens no app, consulte este [tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).

## Personalização da orientação de mensagens no app para iOS

### Definição de uma orientação preferencial

É possível configurar todas as mensagens no app para serem apresentadas em uma orientação específica, independentemente da orientação do dispositivo. Para definir uma orientação preferencial, use [o método delegado](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) `inAppMessage(_:prepareWith:)` para definir a propriedade `preferredOrientation` no `PresentationContext`. 

{% tabs %}
{% tab swift %}

Por exemplo, para criar uma orientação preferencial de retrato:

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
  context.preferredOrientation = .portrait
}
```

{% endtab %}
{% tab OBJECTIVE C %}

```objc
- (void)inAppMessage:(BrazeInAppMessageUI *)ui
         prepareWith:(BrazeInAppMessageUIPresentationContextRaw *)context {
  context.preferredOrientation = BRZInAppMessageRawOrientationPortrait;
}
```

{% endtab %}
{% endtabs %}

Depois que a mensagem no app for apresentada, qualquer mudança de orientação do dispositivo enquanto a mensagem ainda estiver sendo exibida fará com que a mensagem gire com o dispositivo, desde que isso seja compatível com a configuração `orientation` da mensagem.

Observe que a orientação do dispositivo também deve ser compatível com a propriedade `orientation` da mensagem no app para que a mensagem seja exibida. Além disso, a configuração `preferredOrientation` só será respeitada se estiver incluída nas orientações de interface compatíveis com seu aplicativo na seção **Informações de implementação** das configurações do seu direcionamento no Xcode.

![Orientações suportadas no Xcode.]({% image_buster /assets/img/supported_interface_orientations_xcode.png %})

{% alert note %}
A orientação é aplicada apenas para a apresentação da mensagem. Depois que o dispositivo muda de orientação, a visualização de mensagens adota uma das orientações compatíveis. Em dispositivos menores (iPhones, iPod Touch), definir uma orientação paisagem para uma mensagem modal ou completa no app pode resultar em conteúdo truncado.
{% endalert %}

### Envio de mensagens de orientação

Como alternativa, você pode definir a orientação por mensagem. Essa propriedade define todos os tipos de orientação disponíveis para essa mensagem. Para fazer isso, defina a propriedade `orientation` em um determinado `Braze.InAppMessage`:

{% tabs %}
{% tab swift %}

```swift
// Set inAppMessage orientation to support any configuration
inAppMessage.orientation = .any

// Set inAppMessage orientation to only display in portrait
inAppMessage.orientation = .portrait

// Set inAppMessage orientation to only display in landscape
inAppMessage.orientation = .landscape
```

{% endtab %}
{% tab OBJECTIVE C %}

```objc
// Set inAppMessage orientation to support any configuration
inAppMessage.orientation = BRZInAppMessageRawOrientationAny;

// Set inAppMessage orientation to only display in portrait
inAppMessage.orientation = BRZInAppMessageRawOrientationPortrait;

// Set inAppMessage orientation to only display in landscape
inAppMessage.orientation = BRZInAppMessageRawOrientationLandscape;
```

{% endtab %}
{% endtabs %}

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

## Personalização de cliques em botões

Para acessar as informações do botão de mensagem no app ou substituir o comportamento do clique, implemente [`BrazeInAppMessageUIDelegate.inAppMessage(_:shouldProcess:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:shouldprocess:buttonid:message:view:)-122yi). Retorne `true` para permitir que a Braze processe a ação de clique ou retorne `false` para substituir o comportamento.
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


## Ocultação da barra de status durante a exibição

Para mensagens no app `Full`, `FullImage` e `HTML`, o SDK ocultará a barra de status por padrão. Para outros tipos de mensagens no app, a barra de status não é alterada. Para configurar esse comportamento, use [o método delegado](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) `inAppMessage(_:prepareWith:)` para definir a propriedade `statusBarHideBehavior` em `PresentationContext`. Esse campo assume um dos seguintes valores:

| Comportamento de ocultação da barra de status            | Descrição                                                                           |
| ----------------------------------- | ------------------------------------------------------------------------------------- |
| `.auto`                             | A exibição de mensagens decide o estado oculto da barra de status.                                 |
| `.hidden`                           | Sempre oculte a barra de status.                                                           |
| `.visible`                          | Sempre exibir a barra de status.                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

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

## Amostras de implementação

Consulte `InAppMessageUI` em nossa pasta Examples para ver um exemplo em [Swift](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift/Sources/InAppMessageUI) e [Objective C](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/ObjC/Sources/InAppMessageUI)

