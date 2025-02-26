---
nav_title: Controlador de visualização personalizado
article_title: mensagem no app em um controlador de visualização personalizado para iOS
platform: iOS
page_order: 7
description: "Este artigo de referência cobre como aproveitar um controlador de visualização de envio de mensagens no app personalizado para seu aplicativo iOS."
channel:
  - in-app messages
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Exibir mensagens no app em um controlador de visualização personalizado

Mensagens no app também podem ser exibidas em um controlador de visualização personalizado, que você passa para a Braze. Braze animará a mensagem no app personalizada para dentro e para fora e lidará com a análise de dados da mensagem no app. O controlador de visualização deve atender aos seguintes requisitos:

- Deve ser uma subclasse ou uma instância de `ABKInAppMessageViewController`.
- A visão do view controller retornado deve ser uma instância de `ABKInAppMessageView` ou sua subclasse.

O seguinte método de delegado de UI é chamado toda vez que uma mensagem no app é oferecida a `ABKInAppMessageViewController` para permitir que o app passe um controlador de visualização personalizado para a Braze exibir a mensagem no app:

{% tabs %}
{% tab OBJECTIVE C %}

```objc
- (ABKInAppMessageViewController *)inAppMessageViewControllerWithInAppMessage:(ABKInAppMessage *)inAppMessage;
```

{% endtab %}
{% tab swift %}

```swift
func inAppMessageViewControllerWithInAppMessage(inAppMessage: ABKInAppMessage!) -> ABKInAppMessageViewController!
```

{% endtab %}
{% endtabs %}

Nossos [controladores de visualização de mensagem no app](https://github.com/Appboy/appboy-ios-sdk/tree/master/AppboyUI/ABKInAppMessage/ViewControllers) são personalizáveis. Você pode usar subclasses ou categorias para personalizar a exibição ou o comportamento das mensagens no app.

## Declarações de métodos

Para saber mais, consulte os seguintes arquivos de cabeçalho:

- [`ABKInAppMessage.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h)

## Amostras de implementação

Veja um [`ViewController.m`](https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/ViewController.m) e [`CustomInAppMessageViewController.m`](https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/) na mensagem no app de amostra.

