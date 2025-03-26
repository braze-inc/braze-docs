---
nav_title: Angepasste App Store-Bewertungsaufforderung
article_title: Angepasste App Store-Bewertungsaufforderung
platform: iOS
page_order: 4
description: "Dieser Referenzartikel zeigt, wie Sie eine angepasste Bewertungsaufforderung für den App Store einrichten."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Angepasste App Store-Bewertungsaufforderung

{% alert note %}
Sobald Sie diese Aufforderung implementieren, hört Braze auf, Impressionen automatisch zu tracken, und Sie müssen Ihre eigenen [Analytics]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/handing_in_app_display/#logging-impressions-and-clicks) protokollieren.
{% endalert %}

Eine Kampagne zu erstellen, um Nutzer:innen um eine Bewertung im App Store zu bitten, ist eine beliebte Verwendung von In-App-Nachrichten.

Beginnen Sie damit, den [Delegat für In-App-Nachrichten](#in-app-message-controller-delegate) in Ihrer App festzulegen. Als Nächstes implementieren Sie die folgende Delegatmethode, um die Standardnachricht des App Store zu deaktivieren:

{% tabs %}
{% tab OBJECTIVE-C %}

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
{% tab schnell %}

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

Fügen Sie in Ihrem Code zur Behandlung von Deeplinks den folgenden Code hinzu, um den Deeplink `{YOUR-APP-SCHEME}:appstore-review` zu verarbeiten. Beachten Sie, dass Sie `StoreKit` importieren müssen, um `SKStoreReviewController` zu verwenden:

{% tabs %}
{% tab OBJECTIVE-C %}

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
{% tab schnell %}

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

Als Nächstes erstellen Sie eine In-App-Nachricht-Kampagne mit den folgenden Elementen:

- Das Schlüssel-Wert-Paar `"Appstore Review" : "true"`
- Das Klickverhalten ist auf "Deep Link Into App" gesetzt, unter Verwendung des Deeplinks `{YOUR-APP-SCHEME}:appstore-review`.

{% endraw %}

{% alert tip %}
Apple begrenzt die Anzahl der App Store-Bewertungsaufforderungen auf maximal drei (3) Mal pro Jahr und Nutzer:innen. Ihre Kampagne sollte also auf drei Mal pro Jahr und Nutzer:innen [begrenzt]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/) sein.<br><br>Nutzer:innen können die Aufforderungen zur Überprüfung im App Store deaktivieren. Daher sollte Ihre angepasste Bewertungsaufforderung nicht versprechen, dass eine native App Store-Bewertungsaufforderung erscheint oder direkt um eine Bewertung bitten.
{% endalert %}

