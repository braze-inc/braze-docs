---
nav_title: Personalizando Orientação
article_title: Personalizando a orientação da mensagem no app para iOS
platform: iOS
page_order: 3
description: "Este artigo de referência explica como definir a orientação da mensagem no app para seu aplicativo iOS."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Personalizando orientação

## Definindo a orientação para todas as mensagens no app

Para definir uma orientação fixa para todas as mensagens no app, você pode definir a propriedade `supportedOrientationMask` em `ABKInAppMessageUIController`. Adicione o seguinte código após a chamada do seu app para `startWithApiKey:inApplication:withLaunchOptions:`:

{% tabs %}
{% tab OBJECTIVE C %}

```objc
// Set fixed in-app message orientation to portrait.
// Use UIInterfaceOrientationMaskLandscape to display in-app messages in landscape
id<ABKInAppMessageUIControlling> inAppMessageUIController = [Appboy sharedInstance].inAppMessageController.inAppMessageUIController;
((ABKInAppMessageUIController *)inAppMessageUIController).supportedOrientationMask = UIInterfaceOrientationMaskPortrait;
```

{% endtab %}
{% tab swift %}

```swift
// Set fixed in-app message orientation to portrait
// Use .landscape to display in-app messages in landscape
if let controller = Appboy.sharedInstance()?.inAppMessageController.inAppMessageUIController as? ABKInAppMessageUIController {
  controller.supportedOrientationMask = .portrait
}
```

{% endtab %}
{% endtabs %}

A seguir, todas as mensagens no app serão exibidas na orientação suportada, independentemente da orientação do dispositivo. Nota que a orientação do dispositivo também deve ser suportada pela propriedade `orientation` da mensagem no app para que a mensagem seja exibida.

## Como definir a orientação por mensagem no app

Você também pode definir a orientação por mensagem. Para fazer isso, defina um [delegado de mensagem no app]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/). Em seguida, no seu método de delegado `beforeInAppMessageDisplayed:`, defina a propriedade `orientation` no `ABKInAppMessage`:

{% tabs %}
{% tab OBJECTIVE C %}

```objc
// Set inAppMessage orientation to portrait
inAppMessage.orientation = ABKInAppMessageOrientationPortrait;

// Set inAppMessage orientation to landscape
inAppMessage.orientation = ABKInAppMessageOrientationLandscape;
```

{% endtab %}
{% tab swift %}

```swift    
  // Set inAppMessage orientation to portrait
  inAppMessage.orientation = ABKInAppMessageOrientation.portrait

  // Set inAppMessage orientation to landscape
  inAppMessage.orientation = ABKInAppMessageOrientation.landscape
```

{% endtab %}
{% endtabs %}

Mensagens no app não serão exibidas se a orientação do dispositivo não corresponder à propriedade `orientation` na mensagem no app.

{% alert note %}
Para iPads, as mensagens no app aparecerão no estilo de orientação preferido do usuário, independentemente da orientação real da tela.
{% endalert %}

## Declarações de métodos

Para saber mais, consulte o seguinte arquivo de cabeçalho:

- [`ABKInAppMessage.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h)

