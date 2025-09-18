---
nav_title: Comportamento personalizado ao clicar
article_title: Personalização do comportamento ao clicar em mensagens no app para iOS
platform: iOS
page_order: 5
description: "Este artigo de referência aborda o comportamento personalizado ao clicar em mensagens no app para seu aplicativo iOS."
channel:
  - in-app messages
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Personalização do comportamento da mensagem no app ao clicar

A propriedade `inAppMessageClickActionType` no `ABKInAppMessage` define o comportamento da ação depois que a mensagem no app é clicada. Essa propriedade é somente leitura. Se quiser alterar o comportamento ao clicar na mensagem no app, você poderá chamar o seguinte método em `ABKInAppMessage`:

{% tabs %}
{% tab OBJECTIVE C %}

```objc
[inAppMessage setInAppMessageClickAction:clickActionType withURI:uri];
```

{% endtab %}
{% tab swift %}

```swift
inAppMessage.setInAppMessageClickAction(clickActionType: clickActionType, withURI: uri)
```

{% endtab %}
{% endtabs %}

O endereço `inAppMessageClickActionType` pode ser definido como um dos seguintes valores:

| `ABKInAppMessageClickActionType` | Comportamento ao clicar |
| -------------------------- | -------- |
| `ABKInAppMessageRedirectToURI` | O URI fornecido será exibido quando a mensagem for clicada, e a mensagem será descartada. Note que o parâmetro `uri` não pode ser nulo. |
| `ABKInAppMessageNoneClickAction` | A mensagem será descartada quando for clicada. Note que o parâmetro `uri` será ignorado e a propriedade `uri` no `ABKInAppMessage` será definida como nula. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Para mensagens no app contendo botões, a mensagem `clickAction` também será incluída na carga útil final se a ação de clique for adicionada antes de adicionar o texto do botão.
{% endalert %}

## Personalização de cliques no corpo de mensagens no app

O seguinte método [`ABKInAppMessageUIDelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ABKInAppMessageUIDelegate.h) é chamado quando uma mensagem no app é clicada:

{% tabs %}
{% tab OBJECTIVE C %}

```objc
- (BOOL) onInAppMessageClicked:(ABKInAppMessage *)inAppMessage;
```

{% endtab %}
{% tab swift %}

```swift
func onInAppMessageClicked(inAppMessage: ABKInAppMessage!) -> Bool
```

{% endtab %}
{% endtabs %}

## Personalização de cliques no botão de mensagens no app

Para cliques em botões de mensagens no app e botões de mensagens HTML no app (como links), [`ABKInAppMessageUIDelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ABKInAppMessageUIDelegate.h) inclui os seguintes métodos delegados:

{% tabs %}
{% tab OBJECTIVE C %}

```objc
- (BOOL)onInAppMessageButtonClicked:(ABKInAppMessageImmersive *)inAppMessage
                             button:(ABKInAppMessageButton *)button;

- (BOOL)onInAppMessageHTMLButtonClicked:(ABKInAppMessageHTML *)inAppMessage
                             clickedURL:(nullable NSURL *)clickedURL
                               buttonID:(NSString *)buttonID;
```

{% endtab %}
{% tab swift %}

```swift
func onInAppMessageButtonClicked(inAppMessage: ABKInAppMessageImmersive!,
                                 button: ABKInAppMessageButton) -> Bool

func onInAppMessageHTMLButtonClicked(inAppMessage: ABKInAppMessageHTML!,
                                     clickedURL: URL, buttonID: String) -> Bool
```

{% endtab %}
{% endtabs %}

Cada método retorna um valor `BOOL` para indicar se a Braze deve continuar a executar a ação de clique.

Para acessar o tipo de ação de clique de um botão em um método delegado, você pode usar o seguinte código:

{% tabs %}
{% tab OBJECTIVE C %}

```objc
if ([inAppMessage isKindOfClass:[ABKInAppMessageImmersive class]]) {
      ABKInAppMessageImmersive *immersiveIAM = (ABKInAppMessageImmersive *)inAppMessage;
      NSArray<ABKInAppMessageButton *> *buttons = immersiveIAM.buttons;
      for (ABKInAppMessageButton *button in buttons) {
         // Button action type is accessible via button.buttonClickActionType
      }
   }
```

{% endtab %}
{% tab swift %}

```swift
if inAppMessage is ABKInAppMessageImmersive {
      let immersiveIAM = inAppMessage as! ABKInAppMessageImmersive;
      for button in inAppMessage.buttons as! [ABKInAppMessageButton]{
        // Button action type is accessible via button.buttonClickActionType
      }
    }
```

{% endtab %}
{% endtabs %}

Quando uma mensagem no app tem botões, as únicas ações de clique que serão executadas são as do modelo `ABKInAppMessageButton`. O corpo da mensagem no app não será clicável, embora o modelo `ABKInAppMessage` tenha a ação de clique padrão atribuída.

## Declarações de métodos

Para saber mais, consulte os seguintes arquivos de cabeçalho:

- [`ABKInAppMessage.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h)

