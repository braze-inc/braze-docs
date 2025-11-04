## Sobre o SDK do Flutter Braze

Depois de integrar o Braze Flutter SDK no Android e no iOS, você poderá usar a API do Braze em seus [apps Flutter](https://flutter.dev/) escritos em Dart. Esse plug-in fornece a funcionalidade básica de análise de dados e permite integrar mensagens no app e cartões de conteúdo para iOS e Android com uma única base de código.

## Integração do SDK do Flutter

### Pré-requisitos

Antes de integrar o Braze Flutter SDK, você precisará concluir o seguinte:

| Pré-requisito | Descrição |
| --- | --- |
| Identificador de app da Braze API | Para localizar o identificador de seu aplicativo, acesse **Configurações** > **APIs e identificadores** > **Identificadores de aplicativos**. Para saber mais, consulte [Tipos de identificadores da API]({{site.baseurl}}/api/identifier_types/#app-identifier).|
| Endpoint REST  do Braze | Sua URL de endpoint REST. Seu endpoint dependerá da [URL do Braze para sua instância]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints).|
| SDK para Flutter | Instale o [SDK](https://docs.flutter.dev/get-started/install) oficial do Flutter e certifique-se de que ele atenda à [versão mínima suportada](https://github.com/braze-inc/braze-flutter-sdk#requirements) do SDK do Braze Flutter. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Etapa 1: Integrar a biblioteca do Braze

Adicione o pacote Braze Flutter SDK a partir da linha de comando. Isso adicionará a linha adequada a `pubspec.yaml`.

```bash
flutter pub add braze_plugin
```

### Etapa 2: Configuração completa do SDK nativo

{% tabs %}
{% tab Android %}

Para se conectar aos servidores da Braze, crie um arquivo `braze.xml` na pasta `android/res/values` do projeto. Cole o código a seguir e substitua a chave do identificador da API e o ponto final por seus valores:

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

{% endtab %}
{% tab iOS %}
{% subtabs global %}
{% subtab SWIFT %}
Adicione a importação do SDK da Braze na parte superior do arquivo `AppDelegate.swift`:
```swift
import BrazeKit
import braze_plugin
```

No mesmo arquivo, crie o objeto de configuração do Braze no método `application(_:didFinishLaunchingWithOptions:)` e substitua a chave de API e o endpoint pelos valores do seu app. Em seguida, crie a instância da Braze usando a configuração e crie uma propriedade estática em `AppDelegate` para facilitar o acesso:

```swift
static var braze: Braze? = nil

func application(
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
Importar `BrazeKit` na parte superior do arquivo `AppDelegate.m`:
```objc
@import BrazeKit;
```

No mesmo arquivo, crie o objeto de configuração do Braze no método `application:didFinishLaunchingWithOptions:` e substitua a chave de API e o endpoint pelos valores do seu app. Em seguida, crie a instância da Braze usando a configuração e crie uma propriedade estática em `AppDelegate` para facilitar o acesso:

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

### Etapa 3: Configurar o plug-in

Para importar o plug-in em seu código Dart, use o seguinte:

```dart
import 'package:braze_plugin/braze_plugin.dart';
```

Em seguida, inicialize uma instância do plug-in da Braze chamando `new BrazePlugin()` como em [nosso app de amostra](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart).

{% alert important %}
Para evitar comportamentos indefinidos, aloque e use apenas uma única instância do `BrazePlugin` em seu código Dart.
{% endalert %}

## Teste da integração

Você pode verificar se o SDK está integrado verificando as estatísticas da sessão no dashboard. Se você executar seu aplicativo em qualquer uma das plataformas, deverá ver uma nova sessão no dashboard (na seção **Visão geral** ).

Abra uma sessão para um usuário específico chamando o seguinte código em seu app.

```dart
BrazePlugin braze = BrazePlugin();
braze.changeUser("{some-user-id}");
```

Procure o usuário com `{some-user-id}` no dashboard em **Público** > **Pesquisar usuários**. Lá, é possível verificar se os dados da sessão e do dispositivo foram registrados.

