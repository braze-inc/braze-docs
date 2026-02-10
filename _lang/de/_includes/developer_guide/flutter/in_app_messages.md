{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Nachrichtentypen

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/android.md %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/swift.md %}
{% endtabs %}

## Aktivieren von In-App-Nachrichten

{% alert note %}
Dieser Schritt gilt nur für iOS. Die Standard-Implementierung für In-App-Nachrichten ist auf Android bereits eingerichtet.
{% endalert %}

Um den Standard-Moderator für In-App-Nachrichten auf iOS einzurichten, erstellen Sie eine Implementierung des `BrazeInAppMessagePresenter` Protokolls und weisen Sie es der optionalen `inAppMessagePresenter` auf Ihrer Braze-Instanz zu. Sie können auch den standardmäßigen UI-Presenter von Braze verwenden, indem Sie ein `BrazeInAppMessageUI`-Objekt instanziieren.

Sie müssen die Bibliothek `BrazeUI` importieren, um auf die Klasse `BrazeInAppMessageUI` zugreifen zu können.

{% tabs %}
{% tab swift %}

```swift
import BrazeUI

override func application(
  _ application: UIApplication,
  didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil
) -> Bool {
  ...

  let braze = BrazePlugin.initBraze(configuration)

  // Initialize and assign the default `BrazeInAppMessageUI` class to the in-app message presenter.
  braze.inAppMessagePresenter = BrazeInAppMessageUI()
  AppDelegate.braze = braze

  return true
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
@import BrazeUI;

- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  ...

  Braze *braze = [BrazePlugin initBraze:configuration];

  // Initialize and assign the default `BrazeInAppMessageUI` class to the in-app message presenter.
  braze.inAppMessagePresenter = [[BrazeInAppMessageUI alloc] init];
  AppDelegate.braze = braze;

  [self.window makeKeyAndVisible];
  return YES;
}
```
{% endtab %}
{% endtabs %}

Wenn Sie Ihre Implementierung weiter anpassen möchten, lesen Sie den Abschnitt [Protokollierung von In-App-Nachricht-Daten]({{site.baseurl}}/developer_guide/in_app_messages/logging_message_data?sdktab=flutter).
