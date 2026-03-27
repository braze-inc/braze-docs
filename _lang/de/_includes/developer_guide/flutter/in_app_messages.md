{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Nachrichtentypen

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/android.md %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/swift.md %}
{% endtabs %}

## Aktivieren von In-App-Nachrichten

{% tabs %}
{% tab Flutter SDK 18.0.0+ %}

Das Braze Flutter SDK richtet den Standard-Presenter für In-App-Nachrichten auf Android und iOS automatisch ein. In-App-Nachrichten werden ohne zusätzliche Einrichtung angezeigt und an die Dart-Schicht weitergeleitet.

### Anpassen des In-App-Nachrichten-Presenters unter iOS

Um den Standard-Presenter für In-App-Nachrichten unter iOS zu überschreiben, verwenden Sie die `postInitialization`-Closure in `BrazePlugin.configure(_:postInitialization:)`. Ihr angepasster Presenter muss `BrazePlugin.processInAppMessage(message)` aufrufen, um die Daten der In-App-Nachrichten an die Dart-Schicht weiterzuleiten.

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

Rufen Sie in der angepassten Presenter-Klasse `BrazePlugin.processInAppMessage(message)` und `super.present(message: message)` auf, um die Daten an Dart weiterzuleiten und die Standard-UI anzuzeigen.

```swift
class CustomInAppMessagePresenter: BrazeInAppMessageUI {
  override func present(message: Braze.InAppMessage) {
    BrazePlugin.processInAppMessage(message)
    super.present(message: message)
  }
}
```

{% endtab %}
{% tab Flutter SDK 17.1.0 und älter %}

{% alert note %}
Dieser Schritt gilt ausschließlich für iOS. Die Standardimplementierung für In-App-Nachrichten ist auf Android bereits eingerichtet.
{% endalert %}

Um den Standard-Presenter für In-App-Nachrichten unter iOS einzurichten, erstellen Sie eine Implementierung des `BrazeInAppMessagePresenter`-Protokolls und weisen Sie es der optionalen Eigenschaft `inAppMessagePresenter` in Ihrer Braze-Instanz zu. Sie können auch den Standard-UI-Presenter von Braze verwenden, indem Sie ein `BrazeInAppMessageUI`-Objekt instanziieren.

Sie müssen die `BrazeUI`-Bibliothek importieren, um auf die `BrazeInAppMessageUI`-Klasse zugreifen zu können.

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

Weitere Informationen zum Zugriff auf Daten von In-App-Nachrichten finden Sie unter [Protokollierung von In-App-Nachrichten-Daten]({{site.baseurl}}/developer_guide/in_app_messages/logging_message_data?sdktab=flutter).