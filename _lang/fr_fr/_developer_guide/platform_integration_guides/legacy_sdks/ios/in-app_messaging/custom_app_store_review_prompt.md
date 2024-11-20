---
nav_title: Invite de vérification personnalisée d’App Store
article_title: Invite de vérification personnalisée d’App Store
platform: iOS
page_order: 4
description: "Cet article de référence montre comment configurer une invite de vérification personnalisée d’App Store iOS."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Invite de vérification personnalisée d’App Store

{% alert note %}
Une fois que vous avez mis en œuvre cette invite, Braze cesse de suivre automatiquement les impressions, et vous devez enregistrer vos propres [analyses/analytiques]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/handing_in_app_display/#logging-impressions-and-clicks).
{% endalert %}

Créer une campagne pour demander aux utilisateurs un avis sur l’App Store est une utilisation courante des messages in-app.

Commencez par définir le [délégué aux messages in-app](#in-app-message-controller-delegate) dans votre application. Ensuite, implémentez la méthode de délégation suivante pour désactiver le message de vérification par défaut de l’App Store :

{% tabs %}
{% tab OBJECTIF-C %}

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

Dans votre code de traitement de liaison profonde, ajoutez le code suivant pour traiter le lien profond `{YOUR-APP-SCHEME}:appstore-review`. Notez que vous devrez importer `StoreKit` pour utiliser `SKStoreReviewController` :

{% tabs %}
{% tab OBJECTIF-C %}

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

Créez ensuite une campagne de communication in-app avec les éléments suivants :

- La paire clé-valeur `"Appstore Review" : "true"`
- Le comportement en cours défini sur « Deep Link Into App », en utilisant le lien profond `{YOUR-APP-SCHEME}:appstore-review`.

{% endraw %}

{% alert tip %}
Apple limite les invites d’évaluation de l’App Store à un maximum de trois (3) fois par an pour chaque utilisateur. Votre campagne doit donc être [limitée]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/) à trois fois par an et par utilisateur.<br><br>Les utilisateurs peuvent désactiver les invites de commentaires de l’App Store. Par conséquent, votre invite de révision personnalisée ne doit pas promettre qu’une invite de commentaire native de l’App Store s’affichera ou demander directement un commentaire.
{% endalert %}

