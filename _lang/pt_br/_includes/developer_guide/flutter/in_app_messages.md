{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Tipos de mensagens

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/android.md %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/swift.md %}
{% endtabs %}

## Ativação de mensagens no app

{% alert note %}
Esta etapa é apenas para iOS. A implementação padrão para mensagens no app já está configurada no Android.
{% endalert %}

Para configurar o apresentador padrão para mensagens no app no iOS, crie uma implementação do protocolo `BrazeInAppMessagePresenter` e atribua-a ao `inAppMessagePresenter` opcional na sua instância do Braze. Você também pode usar o apresentador padrão do Braze UI instanciando um objeto `BrazeInAppMessageUI`.

Você deve importar a biblioteca `BrazeUI` para acessar a classe `BrazeInAppMessageUI`.

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

Para personalizar ainda mais sua implementação, consulte [Registro de dados de mensagens no app]({{site.baseurl}}/developer_guide/in_app_messages/logging_message_data?sdktab=flutter).
