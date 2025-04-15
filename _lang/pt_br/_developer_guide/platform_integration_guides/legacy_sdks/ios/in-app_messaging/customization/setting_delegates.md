---
nav_title: Configurando Delegados
article_title: Configuração de delegados de mensagens no app para iOS
platform: iOS
page_order: 2
description: "Este artigo de referência cobre a configuração de envios de mensagens no app para seu app iOS."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Definindo delegados

A exibição e a entrega de mensagem no app podem ser personalizadas no código configurando nossos delegados opcionais.

## Delegado de mensagens no app

O [`ABKInAppMessageUIDelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ABKInAppMessageUIDelegate.h) delegado pode ser usado para receber cargas úteis de mensagens no app acionadas para processamento adicional, receber eventos do ciclo de vida de exibição e controlar o tempo de exibição. 

Defina seu objeto delegado `ABKInAppMessageUIDelegate` na instância da Braze chamando:

{% tabs %}
{% tab OBJECTIVE C %}

```objc
[[Appboy sharedInstance].inAppMessageController.inAppMessageUIController setInAppMessageUIDelegate:self];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.inAppMessageController.inAppMessageUIController?.setInAppMessageUIDelegate?(self)
```

{% endtab %}
{% endtabs %}

Confira um exemplo na nossa mensagem no [app de exemplo](https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/ViewController.m). Nota que se você não estiver incluindo a biblioteca de interface do usuário Braze em seu projeto (incomum), este delegado não estará disponível.

## Delegado principal de mensagem no app

Se você não estiver incluindo a biblioteca de interface do usuário do Braze em seu projeto e quiser receber cargas úteis de mensagens no app acionadas para processamento adicional ou exibição personalizada no seu app, implemente o [`ABKInAppMessageControllerDelegate`]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/) protocolo.

Defina seu objeto delegado `ABKInAppMessageControllerDelegate` na instância da Braze chamando:

{% tabs %}
{% tab OBJECTIVE C %}

```objc
[Appboy sharedInstance].inAppMessageController.delegate = self;
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.inAppMessageController.delegate = self
```

{% endtab %}
{% endtabs %}

Você também pode definir seu delegado principal de mensagem no app no momento da inicialização via `appboyOptions` usando a chave `ABKInAppMessageControllerDelegateKey`:
{% tabs %}
{% tab OBJECTIVE C %}

```objc
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKInAppMessageControllerDelegateKey : self }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKInAppMessageControllerDelegateKey : self ])
```
{% endtab %}
{% endtabs %}

## Declarações de métodos

Para saber mais, consulte os seguintes arquivos de cabeçalho:

- [`ABKInAppMessage.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h)
- [`ABKInAppMessageControllerDelegate.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessageControllerDelegate.h)

## Amostras de implementação

Veja um [`ViewController.m`](https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/ViewController.m) na mensagem no app de amostra.


