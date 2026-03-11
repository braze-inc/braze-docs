{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Tipos de mensajes

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/android.md %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/swift.md %}
{% endtabs %}

## Habilitación de mensajes dentro de la aplicación

{% alert note %}
Este paso es solo para iOS. La implementación predeterminada para los mensajes dentro de la aplicación ya está configurada en Android.
{% endalert %}

Para configurar el presentador predeterminado para los mensajes dentro de la aplicación en iOS, crea una implementación del`BrazeInAppMessagePresenter`protocolo y asigna-lo al opcional`inAppMessagePresenter`en tu instancia de Braze. También puedes utilizar el presentador predeterminado de la interfaz de usuario Braze instanciando un objeto `BrazeInAppMessageUI`.

Debes importar la`BrazeUI`biblioteca para acceder a la`BrazeInAppMessageUI`clase.

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

Para personalizar aún más tu implementación, consulta [Registro]({{site.baseurl}}/developer_guide/in_app_messages/logging_message_data?sdktab=flutter) de [datos de mensajes dentro de la aplicación]({{site.baseurl}}/developer_guide/in_app_messages/logging_message_data?sdktab=flutter).
