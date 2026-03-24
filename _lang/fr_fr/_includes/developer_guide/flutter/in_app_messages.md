{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Types de messages

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/android.md %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/swift.md %}
{% endtabs %}

## Activation des messages in-app

{% tabs %}
{% tab Flutter SDK 18.0.0+ %}

Le SDK Flutter de Braze configure automatiquement le présentateur par défaut des messages in-app sur Android et iOS. Les messages in-app sont affichés et transmis à la couche Dart sans configuration supplémentaire.

### Personnalisation du présentateur de messages in-app sur iOS

Pour remplacer le présentateur par défaut des messages in-app sur iOS, utilisez la closure `postInitialization` dans `BrazePlugin.configure(_:postInitialization:)`. Votre présentateur personnalisé doit appeler `BrazePlugin.processInAppMessage(message)` pour transmettre les données du message in-app à la couche Dart.

```swift
import BrazeUI

BrazePlugin.configure(
  { configuration in
    // Set non-API-key configurations here.
  },
  postInitialization: { braze in
    let customPresenter = CustomInAppMessagePresenter()
    braze.inAppMessagePresenter = customPresenter
  }
)
```

Dans la classe du présentateur personnalisé, appelez `BrazePlugin.processInAppMessage(message)` et `super.present(message: message)` pour transmettre les données à Dart et afficher l'interface par défaut.

```swift
class CustomInAppMessagePresenter: BrazeInAppMessageUI {
  override func present(message: Braze.InAppMessage) {
    BrazePlugin.processInAppMessage(message)
    super.present(message: message)
  }
}
```

{% endtab %}
{% tab Flutter SDK 17.1.0 and earlier %}

{% alert note %}
Cette étape concerne uniquement iOS. La configuration par défaut pour les messages in-app est déjà en place sur Android.
{% endalert %}

Pour configurer le présentateur par défaut des messages in-app sur iOS, créez une implémentation du protocole `BrazeInAppMessagePresenter` et affectez-la à la propriété facultative `inAppMessagePresenter` de votre instance Braze. Vous pouvez également utiliser le présentateur par défaut de Braze UI en instanciant un objet `BrazeInAppMessageUI`.

Vous devez importer la bibliothèque `BrazeUI` pour accéder à la classe `BrazeInAppMessageUI`.

{% subtabs %}
{% subtab swift %}

```swift
import BrazeUI

override func application(
  _ application: UIApplication,
  didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil
) -> Bool {
  ...

  let braze = BrazePlugin.initBraze(configuration)

  braze.inAppMessagePresenter = BrazeInAppMessageUI()
  AppDelegate.braze = braze

  return true
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
@import BrazeUI;

- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  ...

  Braze *braze = [BrazePlugin initBraze:configuration];

  braze.inAppMessagePresenter = [[BrazeInAppMessageUI alloc] init];
  AppDelegate.braze = braze;

  [self.window makeKeyAndVisible];
  return YES;
}
```

{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% endtabs %}

Pour en savoir plus sur l'accès aux données des messages in-app, consultez la section [Enregistrement des données des messages in-app]({{site.baseurl}}/developer_guide/in_app_messages/logging_message_data?sdktab=flutter).