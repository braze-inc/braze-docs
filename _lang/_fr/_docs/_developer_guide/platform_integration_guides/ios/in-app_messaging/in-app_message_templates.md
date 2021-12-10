---
nav_title: Modèles de message In-App
article_title: Modèles de messages intégrés pour iOS
platform: iOS
page_order: 4
description: "Cet article de référence montre les modèles de messages dans l'application iOS."
channel:
  - messages intégrés à l'application
---

# Modèles de messages intégrés

## Demande de revue personnalisée de l'App Store

{% alert note %}
Une fois que vous avez mis en œuvre cette prompt, Braze arrête de suivre automatiquement les impressions et vous devez enregistrer les analyses avec les méthodes trouvées [ici]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/#logging-impressions-and-clicks).

{% endalert %}

Créer une campagne pour demander l'avis des utilisateurs de l'App Store est une utilisation populaire des messages dans l'application.

Commencez par [en définissant le délégué de message In-App][30] dans votre application. Ensuite, implémentez la méthode de délégué suivante pour désactiver le message de revue par défaut de l'App Store:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (ABKInAppMessageDisplayChoice)beforeInAppMessageDisplayed:(ABKInAppMessage *)inAppMessage {
  if (inAppMessage. xtras != nil && inAppMessage.extras[@"Appstore Review"] != nil) {
    [[UIApplication sharedApplication] openURL:inAppMessage. ri options :@{} completionHandler:nil];
    return ABKDiscardInAppMessage;
  } else {
    return ABKDisplayInAppMessageNow ;
  }
}
```

{% endtab %}
{% tab swift %}

```swift
func before(inAppMessageDisplayed inAppMessage: ABKInAppMessage) -> ABKInAppMessageDisplayChoice {
  if inAppMessage.extras?["Appstore Review"] != nil && inAppMessage. ri != nil {
    UIApplication.shared.open(inAppMessage.uri!, options: [:], completionHandler: nil)
    return ABKInAppMessageDisplayChoice. iscardInAppMessage
  } else {
    return ABKInAppMessageDisplayChoice.displayInAppMessageNow
  }
}
```

{% endtab %}
{% endtabs %}

Dans votre code de gestion de lien profond, vous pouvez ensuite ajouter le code suivant pour traiter le lien profond `{YOUR-APP-SCHEME}:appstore-review` de </code>. Notez que vous devrez importer `StoreKit` pour utiliser `SKStoreReviewController`:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)application:(UIApplication *)app openURL:(NSURL *)url options:(NSDictionary<UIApplicationOpenURLOptionsKey, id> *)options {
  NSString *urlString = url.absoluteString. tringByRemovingPercentEncoding;
  if ([urlString isEqualToString:@"{YOUR-APP-SCHEME}:appstore-review"]) {
    [SKStoreReviewController requestReview];
    retourner OUI ;
  }
  // Autre code de gestion des liens profonds…
}
```

{% endtab %}
{% tab swift %}

```swift
func application(_ app: UIApplication, open url: URL, options: [UIApplicationOpenURLOptionsKey : Any] = [:]) -> Bool {
  let urlString = url.absoluteString. emovingPercentEncoding
  if (urlString == "{YOUR-APP-SCHEME}:appstore-review") {
    SKStoreReviewController. equestReview()
    retourne true;
  }
  // Autre code de gestion des liens profonds…
}
```

{% endtab %}
{% endtabs %}

{% raw %}

Ensuite, créez une campagne de messagerie In-App avec les éléments suivants :

- ajouter la paire clé-valeur `“Appstore Review” : “true”`
- définissez le "Comportement en clic" à "Lien profond dans l'application", en utilisant le lien profond ci-dessus (par exemple, `{YOUR-APP-SCHEME}:appstore-review`)

{% endraw %}

{% alert tip %}
  Apple limite les demandes de revue de l'App Store à trois (3) fois par an pour chaque utilisateur, donc votre campagne devrait être [limitée au taux]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#user-centric-rate-limiting) à trois fois par an par utilisateur.

  Les utilisateurs peuvent désactiver les invites de revue de l'App Store. Par conséquent, votre demande de revue personnalisée ne devrait pas promettre qu'une invite de revue native de l'App Store apparaîtra ou vous demandera directement un commentaire.
{% endalert %}

[30]: #in-app-message-controller-delegate
