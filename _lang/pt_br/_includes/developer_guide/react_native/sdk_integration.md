## Sobre o SDK do React Native Braze

A integração do React Native Braze SDK fornece funcionalidade básica de análise de dados e permite integrar mensagens no app e cartões de conteúdo para iOS e Android com apenas uma base de código.

## Compatibilidade com a nova arquitetura

A versão mínima do SDK a seguir é compatível com todos os apps que usam [a nova arquitetura do React Native](https://reactnative.dev/docs/the-new-architecture/landing-page):

{% sdk_min_versions reactnative:2.0.1 %}

A partir da versão 6.0.0 do SDK, o Braze usa um React Native Turbo Module, que é compatível com a Nova Arquitetura e com a arquitetura de ponte herdada, o que significa que não é necessária nenhuma configuração adicional.

{% alert warning %}
Se o seu app para iOS estiver em conformidade com `RCTAppDelegate` e seguir nossa configuração anterior `AppDelegate`, revise os exemplos na [configuração nativa completa](#reactnative_step-2-complete-native-setup) para evitar a ocorrência de falhas ao assinar eventos no Turbo Module.
{% endalert %}

## Integração do SDK do React Native

### Pré-requisitos

Para integrar o SDK, é necessária a versão 0.71 ou posterior do React Native. Para obter a lista completa de versões compatíveis, consulte nosso [repositório do GitHub do React Native SDK](https://github.com/braze-inc/braze-react-native-sdk?tab=readme-ov-file#version-support).

### Etapa 1: Integrar a biblioteca do Braze

{% tabs local %}
{% tab npm %}
```bash
npm install @braze/react-native-sdk
```
{% endtab %}
{% tab yarn %}
```bash
yarn add @braze/react-native-sdk
```
{% endtab %}
{% endtabs %}

### Etapa 2: Escolha uma opção de configuração

Você pode gerenciar o SDK do Braze usando o plug-in Braze Expo ou por meio de uma das camadas nativas. Com o plug-in Expo, você pode configurar determinados recursos do SDK sem escrever código em nenhuma das camadas nativas. Escolha a opção que melhor atenda às necessidades de seu app.

{% tabs %}
{% tab Expo %}
#### Etapa 2.1: Instale o plug-in Braze Expo

Confira se sua versão do SDK da Braze para React Native seja, no mínimo, 1.37.0. Para obter a lista completa das versões suportadas, consulte o [repositório do Braze React Native](https://github.com/braze-inc/braze-expo-plugin?tab=readme-ov-file#version-support).

Para instalar o plug-in Braze Expo, execute o seguinte comando:

```bash
npx expo install @braze/expo-plugin
```

#### Etapa 2.2: Adicione o plug-in ao seu app.json

Em `app.json`, adicione o plug-in Braze Expo. Você pode fornecer as seguintes opções de configuração:

| Método                                        | Tipo    | Descrição                                                                                                                                              |
| --------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `androidApiKey`                               | string  | Necessário. A [chave de API]({{site.baseurl}}/api/identifier_types/) do seu aplicativo Android, localizada no dashboard do Braze em **Manage Settings (Gerenciar configurações)**. |
| `iosApiKey`                                   | string  | Necessário. A [chave de API]({{site.baseurl}}/api/identifier_types/) para seu aplicativo iOS, localizada no dashboard do Braze em **Manage Settings (Gerenciar configurações)**.     |
| `baseUrl`                                     | string  | Necessário. O [endpoint do SDK]({{site.baseurl}}/api/basics/#endpoints) para seu app, localizado no dashboard da Braze em **Gerenciar configurações**.    |
| `enableBrazeIosPush`                          | booleano | Somente iOS. Se deve usar a Braze para lidar com notificações por push no iOS. Introduzido no React Native SDK v1.38.0 e no Expo Plugin v0.4.0.                       |
| `enableFirebaseCloudMessaging`                | booleano | Somente para Android. Define se deve usar o Firebase Cloud Messaging para notificações por push. Introduzido no React Native SDK v1.38.0 e no Expo Plugin v0.4.0.             |
| `firebaseCloudMessagingSenderId`              | string  | Somente para Android. Seu ID de remetente do Firebase Cloud Messaging. Introduzido no React Native SDK v1.38.0 e no Expo Plugin v0.4.0.                                    |
| `sessionTimeout`                              | inteiro | O tempo limite da sessão do Braze para seu aplicativo, em segundos.                                                                                               |
| `enableSdkAuthentication`                     | booleano | Define se deve ativar o recurso de [autenticação do SDK](https://www.braze.com/docs/developer_guide/platform_wide/sdk_authentication#sdk-authentication).      |
| `logLevel`                                    | inteiro | Define o nível de registro para o seu aplicativo. O nível de registro padrão é 8 e registra minimamente as informações. Para ativar o registro detalhado para depuração, use o nível de registro 0.    |
| `minimumTriggerIntervalInSeconds`             | inteiro | O intervalo de tempo mínimo, em segundos, entre os disparos. O padrão é 30 segundos.                                                                           |
| `enableAutomaticLocationCollection`           | booleano | Se a coleta automática de locais está ativada (se o usuário permitir).                                                                                  |
| `enableGeofence`                              | booleano | Se as geofences estão ativadas.                                                                                                                           |
| `enableAutomaticGeofenceRequests`             | booleano | Se as solicitações de geofence devem ser feitas automaticamente.                                                                                                  |
| `dismissModalOnOutsideTap`                    | booleano | Somente iOS. Se uma mensagem modal no app é descartada quando o usuário clica fora da mensagem no app.                                           |
| `androidHandlePushDeepLinksAutomatically`     | booleano | Somente para Android. Se o SDK da Braze deve tratar automaticamente os deep links de push.                                                                         |
| `androidPushNotificationHtmlRenderingEnabled` | booleano | Somente para Android. Define se o conteúdo do texto em uma notificação por push deve ser interpretado e renderizado como HTML usando `android.text.Html.fromHtml`.        |
| `androidNotificationAccentColor`              | string  | Somente para Android. Define a cor de destaque da notificação do Android.                                                                                                |
| `androidNotificationLargeIcon`                | string  | Somente para Android. Define o ícone grande de notificação do Android.                                                                                                  |
| `androidNotificationSmallIcon`                | string  | Somente para Android. Define o ícone pequeno de notificação do Android.                                                                                                  |
| `iosRequestPushPermissionsAutomatically`      | booleano | Somente iOS. Define se o usuário deve ser automaticamente solicitado a fornecer permissões push na inicialização do app.                                                          |
| `enableBrazeIosRichPush`                      | booleano | Somente iOS. Define se deve ativar recursos avançados de push para iOS.                                                                                                  |
| `enableBrazeIosPushStories`                   | booleano | Somente iOS. Se deseja ativar os stories por push da Braze para iOS.                                                                                                  |
| `iosPushStoryAppGroup`                        | string  | Somente iOS. O grupo de app usado para o iOS Push Stories.                                                                                                       |
| `iosUseUUIDAsDeviceId`                        | booleano | Somente iOS. Se o ID do dispositivo usará um UUID gerado aleatoriamente.                                                                                       |
| `iosForwardUniversalLinks`                    | booleano | Somente iOS. Especifica se o SDK deve reconhecer e encaminhar automaticamente os links universais para os métodos do sistema (padrão: `false`). Quando ativada, o SDK encaminhará automaticamente os links universais para os métodos do sistema definidos em [Supporting universal links in your app](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/forwarduniversallinks/). Introduzido no React Native SDK v11.1.0 e no Expo Plugin v3.2.0. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Exemplo de configuração:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "androidApiKey": "YOUR-ANDROID-API-KEY",
          "iosApiKey": "YOUR-IOS-API-KEY",
          "baseUrl": "YOUR-SDK-ENDPOINT",
          "sessionTimeout": 60,
          "enableGeofence": false,
          "enableBrazeIosPush": false,
          "enableFirebaseCloudMessaging": false,
          "firebaseCloudMessagingSenderId": "YOUR-FCM-SENDER-ID",
          "androidHandlePushDeepLinksAutomatically": true,
          "enableSdkAuthentication": false,
          "logLevel": 0,
          "minimumTriggerIntervalInSeconds": 0,
          "enableAutomaticLocationCollection": false,
          "enableAutomaticGeofenceRequests": false,
          "dismissModalOnOutsideTap": true,
          "androidPushNotificationHtmlRenderingEnabled": true,
          "androidNotificationAccentColor": "#ff3344",
          "androidNotificationLargeIcon": "@drawable/custom_app_large_icon",
          "androidNotificationSmallIcon": "@drawable/custom_app_small_icon",
          "iosRequestPushPermissionsAutomatically": false,
          "enableBrazeIosPushStories": true,
          "iosPushStoryAppGroup": "group.com.example.myapp.PushStories",
          "iosForwardUniversalLinks": false
        }
      ],
    ]
  }
}
```

##### Configuração dos ícones de notificação por push do Android {#android-push-icons}

Ao usar os sites `androidNotificationLargeIcon` e `androidNotificationSmallIcon`, siga estas práticas recomendadas para exibir os ícones corretamente:

###### Posicionamento e formato dos ícones

Para usar ícones de notificação por push personalizados com o plug-in Braze Expo:

1. Crie seus arquivos de ícones seguindo os requisitos do Android, conforme detalhado em [Requisitos de ícones](#icon-requirements).
2. Coloque-os nos diretórios nativos do Android de seu projeto em `android/app/src/main/res/drawable-<density>/` (por exemplo, `android/app/src/main/res/drawable-mdpi/`, `drawable-hdpi/`, ou semelhante).
3. Como alternativa, se estiver gerenciando ativos no diretório do React Native, poderá usar a [configuração de ícones](https://docs.expo.dev/versions/latest/config/app/#icon) do Expo [app.json ou criar um](https://docs.expo.dev/versions/latest/config/app/#icon) [plug-in de configuração do Expo](https://docs.expo.dev/config-plugins/introduction/) para copiar os ícones para as pastas drawable do Android durante a pré-compilação.

O plug-in Braze Expo faz referência a esses ícones usando o sistema de recursos desenháveis do Android.

###### Requisitos de ícones

- **Ícone pequeno:** Deve ser uma silhueta branca em um fundo transparente (esse é um requisito da plataforma Android)
- **Ícone grande:** Pode ser uma imagem colorida
- **Formato:** Recomenda-se o formato PNG
- **Nomeação:** Use somente letras minúsculas, números e sublinhados (por exemplo, `my_large_icon.png`)

###### Configuração em app.json

Use o prefixo `@drawable/` seguido do nome do arquivo _sem_ a extensão do arquivo. Por exemplo, se o seu arquivo de ícone tiver o nome `large_icon.png`, faça referência a ele como `@drawable/large_icon`:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "androidNotificationLargeIcon": "@drawable/large_icon",
          "androidNotificationSmallIcon": "@drawable/small_icon"
        }
      ]
    ]
  }
}
```

{% alert important %}
Não use jornadas relativas de arquivos (como `src/assets/images/icon.png`) nem inclua a extensão do arquivo ao fazer referência a ícones. O plug-in Expo requer o prefixo `@drawable/` para localizar corretamente os ícones nas pastas nativas do Android após o processo de pré-compilação.
{% endalert %}

###### Como funciona?

O plug-in Braze Expo faz referência a seus arquivos de ícones nos diretórios do Android `drawable`. Quando você executa `npx expo prebuild`, a Expo gera a estrutura de projeto nativa do Android. Seus ícones devem estar presentes nas pastas do Android `drawable` (colocados manualmente ou copiados por meio de um plug-in de configuração) antes do processo de compilação. O plug-in configura o Braze SDK para usar esses recursos desenháveis por seus nomes (sem jornada ou extensão), e é por isso que o prefixo `@drawable/` é necessário em sua configuração.

Para saber mais sobre os ícones de notificação do Android, consulte [as diretrizes de ícones de notificação do Android](https://developer.android.com/develop/ui/views/notifications#icon).

#### Etapa 2.3: Crie e execute seu aplicativo

A pré-construção de seu aplicativo gera os arquivos nativos necessários para o funcionamento do plug-in Braze Expo.

```bash
npx expo prebuild
```

Execute seu aplicativo conforme especificado nos [documentos da Expo](https://docs.expo.dev/workflow/customizing/). Lembre-se de que, se você fizer alguma alteração nas opções de configuração, será necessário fazer o pré-compilamento e executar o aplicativo novamente.
{% endtab %}

{% tab Android %}

#### Etapa 2.1: Adicionar nosso repositório

Em seu projeto de nível superior `build.gradle`, adicione o seguinte em `buildscript` > `dependencies`:

```groovy
buildscript {
    dependencies {
        ...
        // Choose your Kotlin version
        classpath("org.jetbrains.kotlin:kotlin-gradle-plugin:1.8.10")
    }
}
```

Isso adiciona o Kotlin ao seu projeto.

#### Etapa 2.2: Configurar o SDK do Braze

Para se conectar aos servidores da Braze, crie um arquivo `braze.xml` na pasta `res/values` do projeto. Cole o código a seguir e substitua a [chave]({{site.baseurl}}/api/identifier_types/) de API e o [ponto final]({{site.baseurl}}/api/basics/#endpoints) por seus valores:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOU_APP_IDENTIFIER_API_KEY</string>
  <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

Adicione as permissões necessárias ao seu arquivo `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert tip %}
No Braze SDK versão 12.2.0 ou posterior, você pode obter automaticamente a biblioteca Android-sdk-location definindo `importBrazeLocationLibrary=true` em seu arquivo `gradle.properties`.
{% endalert %}

#### Etapa 2.3: Implemente o rastreamento da sessão do usuário

As chamadas para `openSession()` e `closeSession()` são tratadas automaticamente.
Adicione o seguinte código ao método `onCreate()` de sua classe `MainApplication`:

{% subtabs local %}
{% subtab JAVA %}
```java
import com.braze.BrazeActivityLifecycleCallbackListener;

@Override
public void onCreate() {
    super.onCreate();
    ...
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
}
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
import com.braze.BrazeActivityLifecycleCallbackListener

override fun onCreate() {
    super.onCreate()
    ...
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener())
}
```
{% endsubtab %}
{% endsubtabs %}

#### Etapa 2.4: Lidar com atualizações de intenção

Se sua MainActivity tiver `android:launchMode` definido como `singleTask`, adicione o seguinte código à sua classe `MainActivity`:

{% subtabs local %}
{% subtab JAVA %}
```java
@Override
public void onNewIntent(Intent intent) {
    super.onNewIntent(intent);
    setIntent(intent);
}
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
override fun onNewIntent(intent: Intent) {
    super.onNewIntent(intent)
    setIntent(intent)
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab iOS %}

#### Etapa 2.1: (Opcional) Configurar o Podfile para XCFrameworks dinâmicos

Para importar determinadas bibliotecas Braze, como a BrazeUI, em um arquivo Objective C++, você deve usar a sintaxe `#import`. A partir da versão 7.4.0 do Braze Swift SDK, os binários têm um [canal de distribuição opcional como XCFrameworks dinâmicos](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic), que são compatíveis com essa sintaxe.

Se quiser usar esse canal de distribuição, substitua manualmente os locais de origem do CocoaPods em seu Podfile. Consulte o exemplo abaixo e substitua `{your-version}` pela versão relevante que você deseja importar:

```ruby
pod 'BrazeKit', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeKit.podspec'
pod 'BrazeUI', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeUI.podspec'
pod 'BrazeLocation', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeLocation.podspec'
```

#### Etapa 2.2: Instalar pods

Como o React Native vincula automaticamente as bibliotecas à plataforma nativa, você pode instalar o SDK com a ajuda do CocoaPods.

Na pasta raiz do projeto:

```bash
# To install using the React Native New Architecture
cd ios && pod install

# To install using the React Native legacy architecture
cd ios && RCT_NEW_ARCH_ENABLED=0 pod install
```

#### Etapa 2.3: Configurar o SDK do Braze

{% subtabs local %}
{% subtab SWIFT %}

Importe o SDK da Braze na parte superior do arquivo `AppDelegate.swift`:
```swift
import BrazeKit
import braze_react_native_sdk
```

No método `application(_:didFinishLaunchingWithOptions:)`, substitua a [chave]({{site.baseurl}}/api/identifier_types/) de API e o [endpoint]({{site.baseurl}}/api/basics/#endpoints) pelos valores de seu app. Em seguida, crie a instância da Braze usando a configuração e crie uma propriedade estática em `AppDelegate` para facilitar o acesso:

{% alert note %}
Nosso exemplo pressupõe uma implementação do [RCTAppDelegate](https://github.com/facebook/react-native/blob/e64756ae5bb5c0607a4d97a134620fafcb132b3b/packages/react-native/Libraries/AppDelegate/RCTAppDelegate.h), que fornece várias abstrações na configuração do React Native. Se estiver usando uma configuração diferente para seu app, certifique-se de ajustar sua implementação conforme necessário.
{% endalert %}

```swift
func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil
) -> Bool {
    // Setup Braze
    let configuration = Braze.Configuration(
        apiKey: "{BRAZE_API_KEY}",
        endpoint: "{BRAZE_ENDPOINT}")
    // Enable logging and customize the configuration here.
    configuration.logger.level = .info
    let braze = BrazeReactBridge.perform(
      #selector(BrazeReactBridge.initBraze(_:)),
      with: configuration
    ).takeUnretainedValue() as! Braze

    AppDelegate.braze = braze

    /* Other configuration */

    return true
}

// MARK: - AppDelegate.braze

static var braze: Braze? = nil
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

Importe o SDK da Braze na parte superior do arquivo `AppDelegate.m`:
```objc
#import <BrazeKit/BrazeKit-Swift.h>
#import "BrazeReactBridge.h"
```

No método `application:didFinishLaunchingWithOptions:`, substitua a [chave]({{site.baseurl}}/api/identifier_types/) de API e o [endpoint]({{site.baseurl}}/api/basics/#endpoints) pelos valores de seu app. Em seguida, crie a instância da Braze usando a configuração e crie uma propriedade estática em `AppDelegate` para facilitar o acesso:

{% alert note %}
Nosso exemplo pressupõe uma implementação do [RCTAppDelegate](https://github.com/facebook/react-native/blob/e64756ae5bb5c0607a4d97a134620fafcb132b3b/packages/react-native/Libraries/AppDelegate/RCTAppDelegate.h), que fornece várias abstrações na configuração do React Native. Se estiver usando uma configuração diferente para seu app, certifique-se de ajustar sua implementação conforme necessário.
{% endalert %}

```objc
- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Setup Braze
  BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"{BRAZE_API_KEY}"
                                                                    endpoint:@"{BRAZE_ENDPOINT}"];
  // Enable logging and customize the configuration here.
  configuration.logger.level = BRZLoggerLevelInfo;
  Braze *braze = [BrazeReactBridge initBraze:configuration];
  AppDelegate.braze = braze;

  /* Other configuration */

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

### Etapa 3: Importar a biblioteca

Em seguida, `import` a biblioteca em seu código React Native. Para obter mais detalhes, confira nosso [projeto de exemplo](https://github.com/braze-inc/braze-react-native-sdk/tree/master/BrazeProject). 

```javascript
import Braze from "@braze/react-native-sdk";
```

### Etapa 4: Teste a integração (opcional)

Para testar a integração do SDK, inicie uma nova sessão em qualquer plataforma para um usuário chamando o seguinte código em seu app.

```javascript
Braze.changeUser("userId");
```

Por exemplo, é possível atribuir o ID do usuário na inicialização do app:

```javascript
import React, { useEffect } from "react";
import Braze from "@braze/react-native-sdk";

const App = () => {
  useEffect(() => {
    Braze.changeUser("some-user-id");
  }, []);

  return (
    <div>
      ...
    </div>
  )
```

No dashboard do Braze, acesse [User Search]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search#using-user-search) e procure o usuário com o ID correspondente a `some-user-id`. Aqui, é possível verificar se os dados da sessão e do dispositivo foram registrados.

## Próximos passos

Após a integração do SDK do Braze, você pode começar a implementar recursos comuns de envio de mensagens:

- [Notificações por push]({{site.baseurl}}/developer_guide/push_notifications/): Configure e envie notificações por push para seus usuários
- [Mensagens no app]({{site.baseurl}}/developer_guide/in_app_messages/): Exiba mensagens contextuais em seu aplicativo
- [Banners]({{site.baseurl}}/developer_guide/banners/): Mostre banners persistentes na interface do seu app
