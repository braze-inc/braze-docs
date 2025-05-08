---
nav_title: Exemplo - Prompt de revisão da App Store
article_title: Exemplo - Prompt de revisão da App Store
platform: Swift
page_order: 8
description: "Este artigo de referência fornece um exemplo para iOS de uma mensagem no app personalizada para solicitar que os usuários forneçam uma avaliação do seu aplicativo."
channel:
  - in-app messages

---

# Exemplo - prompt de avaliação da App Store

{% alert note %}
Como este exemplo de prompt substitui o comportamento padrão da Braze, não podemos rastrear impressões automaticamente se ele for implementado. Você deve registrar suas próprias [análises de dados]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/customization/handling_in_app_display/#logging-impressions-and-clicks).
{% endalert %}

> Criar uma campanha para pedir aos usuários uma avaliação da App Store é um uso popular de mensagens no app. Este exemplo o orienta na criação de uma mensagem no app personalizada que solicita aos usuários que revisem seu aplicativo.

## Etapa 1: Defina o delegado de mensagem no app
Primeiro, defina o [`BrazeInAppMessageUIDelegate`]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/customization/setting_delegates/) em seu app. 

## Etapa 2: Desativar a mensagem padrão de avaliação da App Store
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

## Etapa 3: Criar um deep link
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

## Etapa 4: Definir comportamento personalizado ao clicar

Em seguida, crie uma campanha de envio de mensagens no app com o seguinte:

- O par chave-valor `"AppStore Review" : "true"`
- O comportamento ao clicar está definido como "Deep Link Into App", utilizando o deep link `{YOUR-APP-SCHEME}:app-store-review`.

{% endraw %}

{% alert tip %}
A Apple limita os avisos de revisão da App Store a um máximo de três vezes por ano para cada usuário, portanto, sua campanha deve ser [limitada de frequência]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/) a três vezes por ano por usuário.<br><br>Os usuários podem desativar os avisos de revisão da App Store. Como resultado, seu prompt de avaliação personalizado não deve prometer que um prompt de avaliação nativo da App Store aparecerá ou solicitar diretamente uma avaliação.
{% endalert %}

