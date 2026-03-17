{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Types de messages

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/android.md %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/swift.md %}
{% endtabs %}

## Activation des messages in-app

{% alert note %}
Cette étape concerne uniquement iOS. La configuration par défaut pour les messages in-app est déjà établie sur Android.
{% endalert %}

Pour configurer le présentateur par défaut pour les messages in-app sur iOS, veuillez créer une implémentation du`BrazeInAppMessagePresenter`protocole et l'attribuer à l'option`inAppMessagePresenter`sur votre instance Braze. Vous pouvez également utiliser le présentateur par défaut de Braze UI en instanciant un objet `BrazeInAppMessageUI`.

Il est nécessaire d'importer la`BrazeUI`bibliothèque pour accéder à la`BrazeInAppMessageUI`classe.

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

Pour personnaliser davantage votre implémentation, veuillez vous référer à [la section Enregistrement des données des messages in-app]({{site.baseurl}}/developer_guide/in_app_messages/logging_message_data?sdktab=flutter).
