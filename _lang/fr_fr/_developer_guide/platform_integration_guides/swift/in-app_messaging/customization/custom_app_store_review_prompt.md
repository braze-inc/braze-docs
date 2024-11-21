---
nav_title: "Exemple : invite d’évaluation de l'App Store"
article_title: "Exemple : invite d’évaluation de l'App Store"
platform: Swift
page_order: 8
description: "Cet article de référence fournit un exemple iOS de message in-app personnalisé pour inviter les utilisateurs à fournir un avis sur votre application."
channel:
  - in-app messages

---

# Exemple - Demande d'évaluation sur l'App Store

{% alert note %}
Étant donné que cet exemple d'invite remplace le comportement par défaut de Braze, nous ne pouvons pas assurer automatiquement le suivi des impressions en cas de mise en œuvre. Vous devez consigner vos propres [analyses]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/customization/handling_in_app_display/#logging-impressions-and-clicks).
{% endalert %}

> Créer une campagne pour demander aux utilisateurs un avis sur l’App Store est une utilisation courante des messages in-app. Cet exemple vous guide dans la création d'un message in-app personnalisé qui invite les utilisateurs à évaluer votre application.

## Étape 1 : Définir le délégué du message in-app
Tout d'abord, définissez l'élément [`BrazeInAppMessageUIDelegate`]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/customization/setting_delegates/) dans votre application. 

## Étape 2 : Désactiver le message par défaut d’évaluation de l’App Store
Ensuite, implémentez la `inAppMessage(_:displayChoiceForMessage:)` [méthode de délégation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) pour désactiver le message par défaut d'évaluation de l'App Store.

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
{% tab OBJECTIF-C %}

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

## Étape 3 : Créer un lien profond
Dans votre code de traitement de liaison profonde, ajoutez le code suivant pour traiter le lien profond `{YOUR-APP-SCHEME}:app-store-review`. Notez que vous devrez importer `StoreKit` pour utiliser `SKStoreReviewController` :

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
{% tab OBJECTIF-C %}

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

## Étape 4 : Définir un comportement personnalisé au clic

Créez ensuite une campagne de communication in-app avec les éléments suivants :

- La paire clé-valeur `"AppStore Review" : "true"`
- Le comportement en cours défini sur « Deep Link Into App », en utilisant le lien profond `{YOUR-APP-SCHEME}:app-store-review`.

{% endraw %}

{% alert tip %}
Apple limite les demandes d’évaluation de l’App Store à un maximum de trois fois par an pour chaque utilisateur. Votre campagne doit donc être [limitée]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/) à trois fois par an et par utilisateur.<br><br>Les utilisateurs peuvent désactiver les invites de commentaires de l’App Store. Par conséquent, votre invite de révision personnalisée ne doit pas promettre qu’une invite de commentaire native de l’App Store s’affichera ou demander directement un commentaire.
{% endalert %}

