---
nav_title: Configuração inicial do SDK
article_title: Configuração inicial do SDK para o Flutter
platform: Flutter
page_order: 1
description: "Esta referência apresenta o Flutter SDK e explica como integrá-lo nativamente no Android e no iOS."
search_rank: 1
---

# Configuração inicial do SDK

> Este artigo de referência aborda como instalar o SDK da Braze para o Flutter. Siga estas instruções para instalar o [Braze Flutter SDK](https://pub.dev/packages/braze_plugin) que contém um pacote para permitir que os integradores usem as APIs da Braze em [apps Flutter](https://flutter.dev/) escritos em Dart.

Esse plug-in fornece a funcionalidade básica de análise de dados e permite integrar mensagens no app e cartões de conteúdo para iOS e Android com uma única base de código.

{% alert note %}
Você precisará concluir as etapas de instalação em ambas as plataformas separadamente.
{% endalert %}

## Pré-requisitos

Para concluir a instalação, você precisará da [chave de API do identificador do app]({{site.baseurl}}/api/identifier_types/), bem como do [endpoint do SDK]({{site.baseurl}}/api/basics/#endpoints). Ambas estão localizadas em **Manage Settings (Gerenciar configurações** ) no dashboard.

Antes de seguir estas etapas, instale e configure o [Flutter SDK](https://docs.flutter.dev/get-started/install). Sua máquina e seu projeto devem estar executando as versões mínimas necessárias do Flutter e do Dart, [notadas aqui](https://github.com/braze-inc/braze-flutter-sdk#readme).

## Etapa 1: Integrar a biblioteca do Braze

Adicione o pacote Braze Flutter SDK a partir da linha de comando.

```bash
flutter pub add braze_plugin
```

Isso adicionará a linha adequada a `pubspec.yaml`.

## Etapa 2: Configuração nativa completa

{% tabs %}
{% tab Android %}

Para se conectar aos servidores da Braze, crie um arquivo `braze.xml` na pasta `android/res/values` do projeto. Cole o código a seguir e substitua a chave do identificador da API e o ponto final por seus valores:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
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

## Etapa 3: Uso

Para importar o plug-in em seu código Dart, use o seguinte:

```dart
import 'package:braze_plugin/braze_plugin.dart';
```

Em seguida, inicialize uma instância do plug-in da Braze chamando `new BrazePlugin()` como em [nosso app de amostra](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart).

## Teste sua integração básica

Nesse ponto, você pode verificar se o SDK está integrado verificando as estatísticas da sessão no dashboard. Se você executar seu aplicativo em qualquer uma das plataformas, deverá ver uma nova sessão no dashboard (na seção **Visão geral** ).

Você pode abrir uma sessão para um usuário específico chamando o seguinte código em seu app.

```dart
BrazePlugin braze = BrazePlugin();
braze.changeUser("{some-user-id}");
```

Em seguida, procure o usuário com `{some-user-id}` no dashboard em **Público** > **Pesquisar usuários**. Lá, é possível verificar se os dados da sessão e do dispositivo foram registrados.

{% alert note %}
Se você estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), poderá pesquisar usuários em **Users** > **User Search**.
{% endalert %}

