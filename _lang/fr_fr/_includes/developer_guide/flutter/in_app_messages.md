{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Types de messages

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/android.md %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/swift.md %}
{% endtabs %}

## Activation des messages in-app

{% alert note %}
Cette étape est réservée à iOS. L'implémentation par défaut des messages in-app est déjà mise en place sur Android.
{% endalert %}

Pour configurer le présentateur par défaut pour les messages in-app sur iOS, créez une implémentation du protocole `BrazeInAppMessagePresenter` et affectez-la à l'option `inAppMessagePresenter` sur votre instance Braze. Vous pouvez également utiliser le présentateur par défaut de Braze UI en instanciant un objet `BrazeInAppMessageUI`.

Vous devez importer la bibliothèque `BrazeUI` pour accéder à la classe `BrazeInAppMessageUI`.

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

Pour personnaliser davantage votre mise en œuvre, reportez-vous à la section [Enregistrement des données des messages in-app]({{site.baseurl}}/developer_guide/in_app_messages/logging_message_data?sdktab=flutter).
