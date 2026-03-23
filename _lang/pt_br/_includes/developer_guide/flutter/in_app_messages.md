{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Tipos de mensagens

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/android.md %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/swift.md %}
{% endtabs %}

## Ativação de mensagens no app

{% tabs %}
{% tab Flutter SDK 18.0.0+ %}

O SDK Flutter da Braze configura automaticamente o apresentador padrão de mensagens no app tanto no Android quanto no iOS. As mensagens no app são exibidas e encaminhadas para a camada Dart sem configuração adicional.

### Personalizando o apresentador de mensagens no app no iOS

Para substituir o apresentador padrão de mensagens no app no iOS, use o closure `postInitialization` em `BrazePlugin.configure(_:postInitialization:)`. Seu apresentador personalizado deve chamar `BrazePlugin.processInAppMessage(message)` para encaminhar os dados da mensagem no app para a camada Dart.

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

Na classe do apresentador personalizado, chame `BrazePlugin.processInAppMessage(message)` e `super.present(message: message)` para encaminhar os dados para o Dart e exibir a UI padrão.

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
Esta etapa é apenas para iOS. A implementação padrão para mensagens no app já está configurada no Android.
{% endalert %}

Para configurar o apresentador padrão para mensagens no app no iOS, crie uma implementação do protocolo `BrazeInAppMessagePresenter` e atribua-o ao `inAppMessagePresenter` opcional na sua instância da Braze. Você também pode usar o apresentador padrão da Braze UI instanciando um objeto `BrazeInAppMessageUI`.

Você deve importar a biblioteca `BrazeUI` para acessar a classe `BrazeInAppMessageUI`.

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

Para saber mais sobre como acessar dados de mensagens no app, consulte [Registro de dados de mensagens no app]({{site.baseurl}}/developer_guide/in_app_messages/logging_message_data?sdktab=flutter).