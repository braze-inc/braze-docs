{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Nachrichtentypen

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/android.md %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/swift.md %}
{% endtabs %}

## Aktivieren von In-App-Nachrichten

{% alert note %}
Dieser Schritt gilt ausschließlich für iOS. Die Standardimplementierung für In-App-Nachrichten ist auf Android bereits eingerichtet.
{% endalert %}

Um den Standard-Präsentator für In-App-Nachrichten unter iOS einzurichten, erstellen Sie bitte eine Implementierung des`BrazeInAppMessagePresenter`Protokolls und weisen Sie es der optionalen Funktion`inAppMessagePresenter` in Ihrer Braze-Instanz zu. Sie können auch den standardmäßigen UI-Presenter von Braze verwenden, indem Sie ein `BrazeInAppMessageUI`-Objekt instanziieren.

Sie müssen die`BrazeUI`Bibliothek importieren, um auf die`BrazeInAppMessageUI`Klasse zugreifen zu können.

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

Um Ihre Implementierung weiter anzupassen, lesen Sie bitte den Abschnitt [Protokollierung von In-App-Nachrichten-Daten]({{site.baseurl}}/developer_guide/in_app_messages/logging_message_data?sdktab=flutter).
