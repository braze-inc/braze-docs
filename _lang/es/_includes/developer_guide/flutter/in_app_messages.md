{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Tipos de mensajes

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/android.md %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/swift.md %}
{% endtabs %}

## Habilitación de mensajes dentro de la aplicación

{% tabs %}
{% tab Flutter SDK 18.0.0+ %}

El SDK de Braze para Flutter configura automáticamente el presentador predeterminado de mensajes dentro de la aplicación tanto en Android como en iOS. Los mensajes dentro de la aplicación se muestran y se reenvían a la capa Dart sin configuración adicional.

### Personalización del presentador de mensajes dentro de la aplicación en iOS

Para anular el presentador predeterminado de mensajes dentro de la aplicación en iOS, utiliza el closure `postInitialization` en `BrazePlugin.configure(_:postInitialization:)`. Tu presentador personalizado debe llamar a `BrazePlugin.processInAppMessage(message)` para reenviar los datos del mensaje dentro de la aplicación a la capa Dart.

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

En la clase del presentador personalizado, llama a `BrazePlugin.processInAppMessage(message)` y `super.present(message: message)` para reenviar los datos a Dart y mostrar la interfaz de usuario predeterminada.

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
Este paso es solo para iOS. La implementación predeterminada para los mensajes dentro de la aplicación ya está configurada en Android.
{% endalert %}

Para configurar el presentador predeterminado para los mensajes dentro de la aplicación en iOS, crea una implementación del protocolo `BrazeInAppMessagePresenter` y asígnala al opcional `inAppMessagePresenter` en tu instancia de Braze. También puedes utilizar el presentador predeterminado de la interfaz de usuario de Braze instanciando un objeto `BrazeInAppMessageUI`.

Debes importar la biblioteca `BrazeUI` para acceder a la clase `BrazeInAppMessageUI`.

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

Para más información sobre cómo acceder a los datos de los mensajes dentro de la aplicación, consulta [Registro de datos de mensajes dentro de la aplicación]({{site.baseurl}}/developer_guide/in_app_messages/logging_message_data?sdktab=flutter).