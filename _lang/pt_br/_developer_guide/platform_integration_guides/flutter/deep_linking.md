---
nav_title: Deep linking
article_title: Deep linking para o Flutter
platform: Flutter
page_order: 6
description: "Este artigo aborda como implementar o deep linking em seus apps Flutter no Android e no iOS."

---

# Deep linking

> Saiba como implementar deep links em seu app para iOS ou Android usando o Flutter. Se quiser dar uma olhada em um app de amostra, consulte [GitHub: Exemplo do Braze Flutter SDK](https://github.com/braze-inc/braze-flutter-sdk/tree/master/example). Para obter informações gerais sobre deep linking, consulte nossas [Perguntas frequentes sobre deep linking]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking).

## Pré-requisitos

Antes de implementar o deep linking em seu app Flutter, você precisará configurar o deep linking na camada nativa do [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/deep_linking/) ou [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/linking/).

## Implementação de deep linking

### Etapa 1: Configurar o manuseio integrado do Flutter

{% tabs %}
{% tab iOS %}
1. Em seu projeto Xcode, abra o arquivo `Info.plist`.
2. Adicionar um novo par chave-valor.
3. Coloque a tecla em `FlutterDeepLinkingEnabled`.
4. Defina o tipo como `Boolean`.
5. Defina o valor para `YES`.
    ![Um exemplo de arquivo `Info.plist` do projeto com o par chave-valor adicionado.]({% image_buster /assets/img/flutter/flutter-ios-deep-link-info-plist.png %} "Xcode Project Info.plist File")
{% endtab %}

{% tab Android %}
1. Em seu projeto do Android Studio, abra o arquivo `AndroidManifest.xml`.
2. Localize `.MainActivity` em suas tags `activity`.
3. Na tag `activity`, adicione a seguinte tag `meta-data`:
    ```xml
    <meta-data android:name="flutter_deeplinking_enabled" android:value="true" />
    ```
{% endtab %}
{% endtabs %}

### Etapa 2: Encaminhar dados para a camada Dart (opcional)

É possível usar o tratamento de links nativos, próprios ou de terceiros para casos de uso complexos, como enviar um usuário para um local específico em seu app ou chamar uma função específica.

#### Exemplo: Deep linking para uma caixa de diálogo de alerta

{% alert note %}
Embora o exemplo a seguir não dependa de pacotes adicionais, você pode usar uma abordagem semelhante para implementar pacotes nativos, próprios ou de terceiros, como [`go_router`](https://pub.dev/packages/go_router). Pode ser necessário um código Dart adicional.
{% endalert %}

Primeiro, um canal de método é usado na camada nativa para encaminhar os dados da string de URL do deep link para a camada Dart.

{% tabs %}
{% tab iOS %}
```swift
extension AppDelegate {
  
  // Delegate method for handling custom scheme links.
  override func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
    forwardURL(url)
    return true
  }
  
  // Delegate method for handling universal links.
  override func application(_ application: UIApplication, continue userActivity: NSUserActivity, restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {
    guard userActivity.activityType == NSUserActivityTypeBrowsingWeb,
        let url = userActivity.webpageURL else {
      return false
    }
    forwardURL(url)
    return true
  }

  private func forwardURL(_ url: URL) {
    guard let controller: FlutterViewController = window?.rootViewController as? FlutterViewController else { return }
    let deepLinkChannel = FlutterMethodChannel(name: "deepLinkChannel", binaryMessenger: controller.binaryMessenger)
    deepLinkChannel.invokeMethod("receiveDeepLink", arguments: url.absoluteString)
  }

}
```
{% endtab %}

{% tab Android %}
```kotlin
class MainActivity : FlutterActivity() {

  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    handleDeepLink(intent)
  }

  override fun onNewIntent(intent: Intent) {
      super.onNewIntent(intent)
    handleDeepLink(intent)
  }

  private fun handleDeepLink(intent: Intent) {
    val binaryMessenger = flutterEngine?.dartExecutor?.binaryMessenger
    if (intent?.action == Intent.ACTION_VIEW && binaryMessenger != null) {
      MethodChannel(binaryMessenger, "deepLinkChannel")
        .invokeMethod("receivedDeepLink", intent?.data.toString())
    }
  }

}
```
{% endtab %}
{% endtabs %}

Em seguida, uma função de retorno de chamada é usada na camada Dart para exibir um diálogo de alerta usando os dados da string de URL enviados anteriormente.

```dart
MethodChannel('deepLinkChannel').setMethodCallHandler((call) async {
  deepLinkAlert(call.arguments, context);
});

void deepLinkAlert(String link, BuildContext context) {
  showDialog(
    context: context,
    builder: (BuildContext context) {
      return AlertDialog(
        title: Text("Deep Link Alert"),
        content: Text("Opened with deep link: $link"),
        actions: <Widget>[
          TextButton(
            child: Text("Close"),
            onPressed: () {
              Navigator.of(context).pop();
            },
          ),
        ],
      );
    },
  );
}
```

