## Sobre o SDK Flutter da Braze

Depois de integrar o SDK Braze Flutter no Android e iOS, você poderá usar a API da Braze em seus [aplicativos Flutter](https://flutter.dev/) escritos em Dart. Esse plug-in fornece a funcionalidade básica de análise de dados e permite integrar mensagens no app e Cartões de conteúdo para iOS e Android com uma única base de código.

## Integrando o SDK do Flutter

### Pré-requisitos

Antes de integrar o SDK Braze Flutter, você precisará concluir o seguinte:

| Pré-requisito | Descrição |
| --- | --- |
| Identificador do app na API da Braze | Para localizar o identificador do seu app, acesse **Configurações** > **APIs e identificadores** > **Identificadores de apps**. Para saber mais, consulte [Tipos de identificadores de API]({{site.baseurl}}/api/identifier_types/#app-identifier).|
| Endpoint de SDK da Braze | Sua URL de endpoint de SDK (por exemplo, `sdk.<cluster>.braze.com`). Seu endpoint dependerá da [URL da Braze para sua instância]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints).|
| SDK do Flutter | Instale o [SDK oficial do Flutter](https://docs.flutter.dev/get-started/install) e certifique-se de que ele atenda à [versão mínima suportada](https://github.com/braze-inc/braze-flutter-sdk#requirements) pelo SDK Braze Flutter. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Etapa 1: Integrar a biblioteca da Braze

Adicione o pacote Braze Flutter SDK a partir da linha de comando. Isso adicionará a linha adequada ao seu `pubspec.yaml`.

```bash
flutter pub add braze_plugin
```

### Etapa 2: Concluir a configuração do SDK nativo

{% tabs %}
{% tab Flutter SDK 18.0.0+ %}

#### 2.1 Configurar o Android

##### Fornecer credenciais em tempo de compilação

Crie um arquivo `braze.xml` na pasta `android/res/values` do seu projeto. A chave de API e o endpoint são fornecidos em tempo de execução a partir do Dart, portanto não são necessários neste arquivo. Para ativar a inicialização adiada, adicione `com_braze_enable_delayed_initialization` ao arquivo:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <bool name="com_braze_enable_delayed_initialization">true</bool>
  <!-- API key and endpoint are not required here. They are set at runtime via Dart. -->
</resources>
```

##### Fornecer credenciais em tempo de execução

Alternativamente, você pode ativar a inicialização adiada programaticamente no seu `MainActivity.kt`:

```kotlin
import com.braze.Braze

class MainActivity : FlutterActivity() {
  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    Braze.enableDelayedInitialization(context = this)
  }
}
```

Adicione as permissões necessárias ao seu arquivo `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

#### 2.2 Configurar o iOS

Dentro do seu método `application(_:didFinishLaunchingWithOptions:)` existente, adicione uma chamada a `BrazePlugin.configure(_:postInitialization:)` para armazenar sua configuração. A instância da Braze é criada posteriormente quando `initialize()` é chamado a partir do Dart. A chave de API e o endpoint não são definidos aqui.

{% subtabs %}
{% subtab SWIFT %}

Adicione o seguinte código ao seu `AppDelegate.swift`:

```swift
import BrazeKit
import braze_plugin

// ...

override func application(
  _ application: UIApplication,
  didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil
) -> Bool {
  // ... your existing didFinishLaunchingWithOptions setup ...

  BrazePlugin.configure(
    { configuration in
      configuration.logger.level = .info
      // Set other non-API-key configurations here, such as:
      // configuration.push.automation = true
      // configuration.sessionTimeout = 60
    },
    postInitialization: { braze in
      // Optional: Customize the Braze instance after creation.
      // For example, set a custom in-app message presenter:
      // let customPresenter = CustomInAppMessagePresenter()
      // braze.inAppMessagePresenter = customPresenter
    }
  )

  return true
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

Adicione o seguinte código ao seu `AppDelegate.m`:

```objc
@import BrazeKit;
@import braze_plugin;

// ...

- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  [BrazePlugin configure:^(BRZConfiguration *configuration) {
    configuration.logger.level = BRZLoggerLevelInfo;
    // Set other non-API-key configurations here, such as:
    // configuration.push.automation = ...
    // configuration.sessionTimeout = 60;
  } postInitialization:^(Braze *braze) {
    // Optional: customize the Braze instance after creation.
  }];

  return YES;
}
```

{% endsubtab %}
{% endsubtabs %}

{% alert important %}
`BrazePlugin.configure()` apenas armazena sua configuração. Nenhuma instância da Braze existe até que `initialize()` seja chamado a partir do Dart, portanto não chame nenhum método do SDK da Braze no AppDelegate após `configure()`.
{% endalert %}

{% endtab %}
{% tab Flutter SDK 17.1.0 e anteriores %}

#### 2.1 Configurar o Android

Para se conectar aos servidores da Braze, crie um arquivo `braze.xml` na pasta `android/res/values` do projeto. Cole o código a seguir e substitua a chave do identificador da API e o endpoint pelos seus valores:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
  <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

Adicione as permissões necessárias ao seu arquivo `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

#### 2.2 Configurar o iOS

{% subtabs %}
{% subtab SWIFT %}
Adicione a importação do SDK da Braze na parte superior do arquivo `AppDelegate.swift`:
```swift
import BrazeKit
import braze_plugin
```

No mesmo arquivo, crie o objeto de configuração da Braze no método `application(_:didFinishLaunchingWithOptions:)` e substitua a chave de API e o endpoint pelos valores do seu app. Em seguida, crie a instância da Braze usando a configuração e crie uma propriedade estática em `AppDelegate` para facilitar o acesso:

```swift
static var braze: Braze? = nil

override func application(
  _ application: UIApplication,
  didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil
) -> Bool {
  // Setup Braze
  let configuration = Braze.Configuration(
    apiKey: "<BRAZE_API_KEY>",
    endpoint: "<BRAZE_ENDPOINT>"
  )
  // - Enable logging or customize configuration here
  configuration.logger.level = .info
  let braze = BrazePlugin.initBraze(configuration)
  AppDelegate.braze = braze

  return true
}
```
{% endsubtab %}
{% subtab OBJECTIVE-C %}
Importe o SDK da Braze na parte superior do arquivo `AppDelegate.m`:
```objc
@import BrazeKit;
@import braze_plugin;
```

No mesmo arquivo, crie o objeto de configuração da Braze no método `application:didFinishLaunchingWithOptions:` e substitua a chave de API e o endpoint pelos valores do seu app. Em seguida, crie a instância da Braze usando a configuração e crie uma propriedade estática em `AppDelegate` para facilitar o acesso:

```objc
- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Setup Braze
  BRZConfiguration *configuration =
      [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
                                      endpoint:@"<BRAZE_ENDPOINT>"];
  // - Enable logging or customize configuration here
  configuration.logger.level = BRZLoggerLevelInfo;
  Braze *braze = [BrazePlugin initBraze:configuration];
  AppDelegate.braze = braze;

  [self.window makeKeyAndVisible];
  return YES;
}

#pragma mark - AppDelegate.braze

static Braze *_braze = nil;

+ (Braze *)braze {
  return _braze;
}

+ (void)setBraze:(Braze *)braze {
  _braze = braze;
}
```
{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% endtabs %}

### Etapa 3: Configure o plug-in

{% tabs %}
{% tab Flutter SDK 18.0.0+ %}

Importe o plug-in e crie uma única instância de `BrazePlugin`:

```dart
import 'package:braze_plugin/braze_plugin.dart';

final BrazePlugin braze = BrazePlugin();
```

Em seguida, chame `initialize()` com a chave de API do identificador do seu app e o endpoint de SDK para criar a instância da Braze. Veja as opções abaixo para saber onde chamar esse método no seu app.

#### Inicialização padrão

Para inicializar o SDK quando seu app é iniciado, chame `initialize()` em `initState()`:

```dart
@override
void initState() {
  super.initState();
  braze.initialize("<BRAZE_API_KEY>", "<BRAZE_ENDPOINT>");
}
```

#### Inicialização adiada

Para adiar a inicialização do SDK para um momento posterior na sessão — por exemplo, depois que o usuário conceder consentimento ou concluir o login — chame `initialize()` quando estiver pronto:

```dart
// ...
void onUserConsent() {
  braze.initialize("<BRAZE_API_KEY>", "<BRAZE_ENDPOINT>");
}
```

{% alert warning %}
Notificações por push e deep links recebidos antes de `initialize()` ser chamado não são processados no iOS. No Android, deep links de notificações por push não são resolvidos enquanto o SDK aguarda a inicialização. Se o seu app depende de push ou deep links na inicialização, use a [inicialização padrão](#standard-initialization).
{% endalert %}

#### Chaves de API específicas por plataforma

Como seus apps Android e iOS usam chaves de API diferentes, use a detecção de plataforma:

```dart
import 'dart:io' show Platform;

if (Platform.isAndroid) {
  braze.initialize("<ANDROID_API_KEY>", "<BRAZE_ENDPOINT>");
} else if (Platform.isIOS) {
  braze.initialize("<IOS_API_KEY>", "<BRAZE_ENDPOINT>");
}
```

#### Reinicialização

Você pode chamar `initialize()` várias vezes para reinicializar o SDK com uma chave de API e endpoint diferentes durante a sessão. Cada chamada encerra a instância anterior da Braze e cria uma nova.

{% alert important %}
Para evitar comportamentos indefinidos, aloque e utilize apenas uma única instância do `BrazePlugin` em seu código Dart. Todas as chamadas de métodos do SDK feitas antes de `initialize()` são ignoradas no iOS, portanto chame `initialize()` antes de usar qualquer outro método da Braze.
{% endalert %}

{% endtab %}
{% tab Flutter SDK 17.1.0 e anteriores %}

Para importar o plug-in em seu código Dart, use o seguinte:

```dart
import 'package:braze_plugin/braze_plugin.dart';
```

Em seguida, inicialize uma instância do plug-in da Braze chamando `new BrazePlugin()` como em [nosso app de exemplo](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart).

{% alert important %}
Para evitar comportamentos indefinidos, aloque e utilize apenas uma única instância do `BrazePlugin` em seu código Dart.
{% endalert %}

{% endtab %}
{% endtabs %}

## Testando a integração
Você pode verificar se o SDK está integrado conferindo as estatísticas de sessão no dashboard. Se você executar seu aplicativo em qualquer uma das plataformas, deverá ver uma nova sessão no dashboard (na seção **Visão geral**).

Abra uma sessão para um usuário específico chamando o seguinte código no seu app.

{% tabs %}
{% tab Flutter SDK 18.0.0+ %}

```dart
BrazePlugin braze = BrazePlugin();
braze.initialize("<BRAZE_API_KEY>", "<BRAZE_ENDPOINT>");
braze.changeUser("{some-user-id}");
```

{% endtab %}
{% tab Flutter SDK 17.1.0 e anteriores %}

```dart
BrazePlugin braze = BrazePlugin();
braze.changeUser("{some-user-id}");
```

{% endtab %}
{% endtabs %}

Procure o usuário com `{some-user-id}` no dashboard, em **Público** > **Pesquisar usuários**. Lá, é possível verificar se os dados da sessão e do dispositivo foram registrados.