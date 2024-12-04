---
nav_title: Comportamento personalizado ao clicar
article_title: Personalização do comportamento de cliques em mensagens no app para iOS
platform: Swift
page_order: 5
description: "Este artigo de referência aborda o comportamento personalizado ao clicar em mensagens no app do iOS para o SDK Swift."
channel:
  - in-app messages
---

# Comportamento ao clicar personalizado

> Cada objeto `Braze.InAppMessage` contém um objeto [`ClickAction`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/clickaction)correspondente, que define o comportamento ao clicar. 

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

## Clique nos tipos de ação

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

## Personalização de mensagens no app e cliques em botões

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

