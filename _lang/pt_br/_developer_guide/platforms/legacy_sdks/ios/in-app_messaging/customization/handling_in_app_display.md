---
nav_title: Manuseio de telas personalizadas
article_title: Personalização do tratamento da exibição de mensagens no app para iOS
platform: iOS
page_order: 4
description: "Este artigo de referência aborda o tratamento de exibição personalizada de mensagens no app para o seu aplicativo iOS."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Exibição personalizada de mensagens no app

Quando o [`ABKInAppMessageControllerDelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessageControllerDelegate.h) é definido, o método delegado a seguir será chamado antes que as mensagens no app sejam exibidas:

{% tabs %}
{% tab OBJECTIVE C %}

```objc
- (ABKInAppMessageDisplayChoice) beforeInAppMessageDisplayed:(ABKInAppMessage *)inAppMessage;
```

{% endtab %}
{% tab swift %}

```swift
func beforeInAppMessageDisplayed(inAppMessage: ABKInAppMessage!) -> ABKInAppMessageDisplayChoice
```

{% endtab %}
{% endtabs %}

Se você tiver implementado apenas [`ABKInAppMessageUIDelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ABKInAppMessageUIDelegate.h)o método delegado da interface do usuário a seguir será chamado em seu lugar:

{% tabs %}
{% tab OBJECTIVE C %}

```objc
- (ABKInAppMessageDisplayChoice) beforeInAppMessageDisplayed:(ABKInAppMessage *)inAppMessage withKeyboardIsUp:(BOOL)keyboardIsUp;
```

{% endtab %}
{% tab swift %}

```swift
func beforeInAppMessageDisplayed(inAppMessage: ABKInAppMessage!, withKeyboardIsUp keyboardIsUp: Bool) -> ABKInAppMessageDisplayChoice
```

{% endtab %}
{% endtabs %}

Você pode personalizar o envio de mensagens no app implementando esse método delegado e retornando um dos seguintes valores para `ABKInAppMessageDisplayChoice`:

| `ABKInAppMessageDisplayChoice` | Comportamento |
| -------------------------- | -------- |
| Objective C: `ABKDisplayInAppMessageNow`<br>Swift: `displayInAppMessageNow` | A mensagem será exibida imediatamente. |
| Objective C: `ABKDisplayInAppMessageLater`<br>Swift: `displayInAppMessageLater` | A mensagem não será exibida e será colocada de volta no topo da pilha. |
| Objective C: `ABKDiscardInAppMessage`<br>Swift: `discardInAppMessage`| A mensagem será descartada e não será exibida. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Você pode usar o método delegado `beforeInAppMessageDisplayed:` para adicionar a lógica de exibição de mensagens no app, personalizar as mensagens no app antes que o Braze as exiba ou aceitar a lógica de exibição de mensagens no app e a interface do usuário completamente.

Confira nosso [aplicativo de amostra](https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/AppDelegate.m) para obter um exemplo de implementação.

## Substituição de mensagens no app antes da exibição

Se quiser alterar o comportamento de exibição das mensagens no app, adicione qualquer lógica de exibição necessária ao método delegado `beforeInAppMessageDisplayed:`. Por exemplo, você pode querer exibir a mensagem no app na parte superior da tela se o teclado estiver sendo exibido no momento, ou pegar o modelo de dados da mensagem no app e exibir a mensagem no app você mesmo.

Se a campanha de mensagens no app não estiver sendo exibida quando a sessão for iniciada, verifique se a lógica de exibição necessária foi adicionada ao método delegado `beforeInAppMessageDisplayed:`. Isso permite que a campanha de mensagens no app seja exibida na parte superior da tela, mesmo que o teclado esteja sendo exibido.

## Desativando o modo escuro

Para evitar que as mensagens no app adotem o estilo do modo escuro quando o dispositivo do usuário tiver o modo escuro ativado, use a propriedade [`ABKInAppMessage.enableDarkTheme`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message.html#ae89df6090bed623099ab0ecc0a74ad5d). No método `ABKInAppMessageControllerDelegate.beforeInAppMessageDisplayed:` ou `ABKInAppMessageUIDelegate.beforeInAppMessageDisplayed:`, defina a propriedade `enableDarkTheme` do parâmetro `inAppMessage` do método como `NO`.

{% tabs %}
{% tab OBJECTIVE C %}

```objc
// ABKInAppMessageControllerDelegate
- (ABKInAppMessageDisplayChoice)beforeInAppMessageDisplayed:(ABKInAppMessage *)inAppMessage {
  ...
  inAppMessage.enableDarkTheme = NO;
  ...
  return ABKDisplayInAppMessageNow;
}

// ABKInAppMessageUIDelegate
- (ABKInAppMessageDisplayChoice)beforeInAppMesssageDisplayed:(ABKInAppMessage *)inAppMessage
                                            withKeyboardIsUp:(BOOL)keyboardIsUp {
  ...
  inAppMessage.enableDarkTheme = NO;
  ...
  return ABKDisplayInAppMessageNow;
}
```

{% endtab %}
{% tab swift %}

```swift
// ABKInAppMessageControllerDelegate
func before(inAppMessageDisplayed inAppMessage: ABKInAppMessage) -> ABKInAppMessageDisplayChoice {
  ...
  inAppMessage.enableDarkTheme = false
  ...
  return ABKInAppMessageDisplayChoice.displayInAppMessageNow
}

// ABKInAppMessageUIDelegate
func before(inAppMessageDisplayed inAppMessage: ABKInAppMessage, withKeyboardIsUp keyboardIsUp: Bool) -> ABKInAppMessageDisplayChoice {
  ...
  inAppMessage.enableDarkTheme = false
  ...
  return ABKInAppMessageDisplayChoice.displayInAppMessageNow
}
```

{% endtab %}
{% endtabs %}

## Ocultação da barra de status durante a exibição

Para mensagens no app `Full` e `HTML`, o SDK tentará colocar a mensagem sobre a barra de status por padrão. No entanto, em alguns casos, a barra de status ainda pode aparecer na parte superior da mensagem no app. A partir da versão [3.21.1](https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#3211) do SDK do iOS, é possível forçar a ocultação da barra de status ao exibir mensagens no app `Full` e `HTML`, definindo `ABKInAppMessageHideStatusBarKey` para `YES` dentro do `appboyOptions` passado para `startWithApiKey:`.

## Registro de impressões e cliques

O registro de impressões e cliques em mensagens no app não é automático quando você implementa um tratamento totalmente personalizado (por exemplo, você contorna a exibição de mensagens no app do Braze retornando `ABKDiscardInAppMessage` no seu `beforeInAppMessageDisplayed:`). Se você optar por implementar sua própria interface do usuário usando nossos modelos de mensagem no app, deverá registrar a análise de dados com os seguintes métodos na classe `ABKInAppMessage`:

{% tabs %}
{% tab OBJECTIVE C %}

```objc
// Registers that a user has viewed an in-app message with the Braze server.
- (void) logInAppMessageImpression;
// Registers that a user has clicked on an in-app message with the Braze server.
- (void) logInAppMessageClicked;
```

{% endtab %}
{% tab swift %}

```swift
// Registers that a user has viewed an in-app message with the Braze server.
func logInAppMessageImpression()
// Registers that a user has clicked on an in-app message with the Braze server.
func logInAppMessageClicked()
```

{% endtab %}
{% endtabs %}

Além disso, você deve registrar os cliques em botões nas subclasses de `ABKInAppMessageImmersive` (*i.e*., `Modal` e mensagens no app `Full`):

{% tabs %}
{% tab OBJECTIVE C %}

```objc
// Logs button click analytics
- (void)logInAppMessageClickedWithButtonID:(NSInteger)buttonID;
```

{% endtab %}
{% tab swift %}

```swift
// Logs button click analytics
func logInAppMessageClickedWithButtonID(buttonId: NSInteger)
```

{% endtab %}
{% endtabs %}

## Declarações de métodos

Para saber mais, consulte os seguintes arquivos de cabeçalho:

- [`ABKInAppMessage.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h)
- [`ABKInAppMessageControllerDelegate.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessageControllerDelegate.h)

## Amostras de implementação

Veja um [`AppDelegate.m`](https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/AppDelegate.m) exemplo de aplicativo de mensagem no app.



