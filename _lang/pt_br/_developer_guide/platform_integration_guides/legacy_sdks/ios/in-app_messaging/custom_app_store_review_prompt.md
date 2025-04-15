---
nav_title: Solicitação de revisão personalizada da App Store
article_title: Solicitação de revisão personalizada da App Store
platform: iOS
page_order: 4
description: "Este artigo de referência mostra como configurar um prompt de avaliação personalizado da App Store do iOS."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Solicitação de revisão personalizada da App Store

{% alert note %}
Depois de implementar esse prompt, o Braze deixará de rastrear automaticamente as impressões e você deverá registrar sua própria [análise de dados]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/handing_in_app_display/#logging-impressions-and-clicks).
{% endalert %}

Criar uma campanha para pedir aos usuários uma avaliação da App Store é um uso popular de mensagens no app.

Comece definindo o [delegado de mensagens no app](#in-app-message-controller-delegate) em seu aplicativo. Em seguida, implemente o seguinte método delegado para desativar a mensagem padrão de avaliação da App Store.

{% tabs %}
{% tab OBJECTIVE C %}

```objc
- (ABKInAppMessageDisplayChoice)beforeInAppMessageDisplayed:(ABKInAppMessage *)inAppMessage {
  if (inAppMessage.extras != nil && inAppMessage.extras[@"Appstore Review"] != nil) {
    [[UIApplication sharedApplication] openURL:inAppMessage.uri options:@{} completionHandler:nil];
    return ABKDiscardInAppMessage;
  } else {
    return ABKDisplayInAppMessageNow;
  }
}
```

{% endtab %}
{% tab swift %}

```swift
func before(inAppMessageDisplayed inAppMessage: ABKInAppMessage) -> ABKInAppMessageDisplayChoice {
  if inAppMessage.extras?["Appstore Review"] != nil && inAppMessage.uri != nil {
    UIApplication.shared.open(inAppMessage.uri!, options: [:], completionHandler: nil)
    return ABKInAppMessageDisplayChoice.discardInAppMessage
  } else {
    return ABKInAppMessageDisplayChoice.displayInAppMessageNow
  }
}
```

{% endtab %}
{% endtabs %}

No código de tratamento do deep link, adicione o seguinte código para processar o deep link `{YOUR-APP-SCHEME}:appstore-review`. Note que você precisará importar `StoreKit` para usar `SKStoreReviewController`:

{% tabs %}
{% tab OBJECTIVE C %}

```objc
- (BOOL)application:(UIApplication *)app openURL:(NSURL *)url options:(NSDictionary<UIApplicationOpenURLOptionsKey, id> *)options {
  NSString *urlString = url.absoluteString.stringByRemovingPercentEncoding;
  if ([urlString isEqualToString:@"{YOUR-APP-SCHEME}:appstore-review"]) {
    [SKStoreReviewController requestReview];
    return YES;
  }
  // Other deep link handling code…
}
```

{% endtab %}
{% tab swift %}

```swift
func application(_ app: UIApplication, open url: URL, options: [UIApplicationOpenURLOptionsKey : Any] = [:]) -> Bool {
  let urlString = url.absoluteString.removingPercentEncoding
  if (urlString == "{YOUR-APP-SCHEME}:appstore-review") {
    SKStoreReviewController.requestReview()
    return true;
  }
  // Other deep link handling code…
}
```

{% endtab %}
{% endtabs %}

{% raw %}

Em seguida, crie uma campanha de envio de mensagens no app com o seguinte:

- O par chave-valor `"Appstore Review" : "true"`
- O comportamento ao clicar está definido como "Deep Link Into App", utilizando o deep link `{YOUR-APP-SCHEME}:appstore-review`.

{% endraw %}

{% alert tip %}
A Apple limita as solicitações de revisão da App Store a um máximo de três (3) vezes por ano para cada usuário, portanto, sua campanha deve ser [limitada de frequência]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/) a três vezes por ano por usuário.<br><br>Os usuários podem desativar os avisos de revisão da App Store. Como resultado, seu prompt de avaliação personalizado não deve prometer que um prompt de avaliação nativo da App Store aparecerá ou solicitar diretamente uma avaliação.
{% endalert %}

