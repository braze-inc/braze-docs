---
nav_title: Beispiel - App Store Review Aufforderung
article_title: Beispiel - App Store Review Aufforderung
platform: Swift
page_order: 8
description: "Dieser Artikel referenziert ein iOS-Beispiel für eine angepasste In-App-Nachricht, mit der Sie Nutzer:innen auffordern, eine Bewertung für Ihre App abzugeben."
channel:
  - in-app messages

---

# Beispiel - Aufforderung zur Bewertung im App Store

{% alert note %}
Da diese Beispielabfrage das Standardverhalten von Braze außer Kraft setzt, können wir Impressionen nicht automatisch tracken. Sie müssen Ihre eigenen [Analytics]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/customization/handling_in_app_display/#logging-impressions-and-clicks) protokollieren.
{% endalert %}

> Eine Kampagne zu erstellen, um Nutzer:innen um eine Bewertung im App Store zu bitten, ist eine beliebte Verwendung von In-App-Nachrichten. Dieses Beispiel zeigt Ihnen, wie Sie eine angepasste In-App-Nachricht erstellen, die Nutzer:innen dazu auffordert, Ihre App zu bewerten.

## Schritt 1: Legen Sie den Delegaten für In-App-Nachrichten fest
Setzen Sie zunächst die [`BrazeInAppMessageUIDelegate`]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/customization/setting_delegates/) in Ihrer App ein. 

## Schritt 2: Deaktivieren Sie die standardmäßige Review-Mitteilung des App Store
Als Nächstes implementieren Sie die [Delegate-Methode](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) `inAppMessage(_:displayChoiceForMessage:)`, um die Standard Nachrichten des App Store zu deaktivieren.

{% tabs %}
{% tab schnell %}

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
{% tab OBJECTIVE-C %}

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

## Schritt 3: Setzen Sie einen Deeplink
Fügen Sie in Ihrem Code zur Behandlung von Deeplinks den folgenden Code hinzu, um den `{YOUR-APP-SCHEME}:app-store-review`-Deeplink zu verarbeiten. Beachten Sie, dass Sie `StoreKit` importieren müssen, um `SKStoreReviewController` zu verwenden:

{% tabs %}
{% tab schnell %}

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
{% tab OBJECTIVE-C %}

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

## Schritt 4: Angepasstes Verhalten beim Klicken einstellen

Als Nächstes erstellen Sie eine In-App-Nachricht-Kampagne mit den folgenden Elementen:

- Das Schlüssel-Wert-Paar `"AppStore Review" : "true"`
- Das Klickverhalten ist auf "Deep Link Into App" gesetzt, unter Verwendung des Deeplinks `{YOUR-APP-SCHEME}:app-store-review`.

{% endraw %}

{% alert tip %}
Apple begrenzt die Aufforderungen zur Überprüfung im App Store auf maximal drei Mal pro Jahr und Nutzer:innen. Daher sollte Ihre Kampagne auf drei Mal pro Jahr und Nutzer:innen [begrenzt]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/) sein.<br><br>Nutzer:innen können die Aufforderungen zur Überprüfung im App Store deaktivieren. Daher sollte Ihre angepasste Bewertungsaufforderung nicht versprechen, dass eine native App Store-Bewertungsaufforderung erscheint oder direkt um eine Bewertung bitten.
{% endalert %}

