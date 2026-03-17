## Integrando o SDK do Android

### Etapa 1: Atualize sua configuração de build do Gradle

Na configuração do repositório do seu projeto (por exemplo, `settings.gradle`, `settings.gradle.kts` ou `build.gradle` de nível superior), adicione [`mavenCentral()`](https://docs.gradle.org/current/kotlin-dsl/gradle/org.gradle.api.artifacts.dsl/-repository-handler/maven-central.html) à sua lista de repositórios. Essa sintaxe é a mesma para Groovy e Kotlin DSL.

```groovy
repositories {
  mavenCentral()
}
```

Em seguida, adicione o Braze às suas dependências. Nos exemplos a seguir, substitua `SDK_VERSION` pela versão atual do seu SDK do Android Braze. Para a lista completa de versões, veja [Changelogs]({{site.baseurl}}/developer_guide/changelogs/?sdktab=android).

{% alert note %}
- Para Kotlin DSL (`build.gradle.kts`), use a sintaxe `implementation("...")`.
- Para Groovy (`build.gradle`), use a sintaxe `implementation '...'`.
- Para [catálogos de versão](https://developer.android.com/build/migrate-to-catalogs), adicione entradas ao seu arquivo `gradle/libs.versions.toml` e faça referência a elas usando os acessores gerados.
{% endalert %}

{% tabs local %}
{% tab base only %}
Se você não planeja usar componentes de UI do Braze, adicione o seguinte às suas dependências.

{% subtabs local %}
{% subtab Groovy %}
```groovy
dependencies {
    implementation 'com.braze:android-sdk-base:SDK_VERSION' // (Required) Adds dependencies for the base Braze SDK.
    implementation 'com.braze:android-sdk-location:SDK_VERSION' // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% subtab Kotlin DSL %}
```kotlin
dependencies {
    implementation("com.braze:android-sdk-base:SDK_VERSION") // (Required) Adds dependencies for the base Braze SDK.
    implementation("com.braze:android-sdk-location:SDK_VERSION") // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% subtab Version catalog %}
No seu arquivo `gradle/libs.versions.toml`:

```toml
[versions]
braze = "SDK_VERSION"

[libraries]
braze-android-sdk-base = { group = "com.braze", name = "android-sdk-base", version.ref = "braze" }
braze-android-sdk-location = { group = "com.braze", name = "android-sdk-location", version.ref = "braze" }
```

Então, no seu arquivo `build.gradle` ou `build.gradle.kts`, adicione as seguintes dependências. Essa sintaxe é a mesma para Groovy e Kotlin DSL.

```groovy
dependencies {
    implementation(libs.braze.android.sdk.base) // (Required) Adds dependencies for the base Braze SDK.
    implementation(libs.braze.android.sdk.location) // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab with ui components %}
Se você planeja usar componentes de UI do Braze, adicione o seguinte às suas dependências.

{% subtabs local %}
{% subtab Groovy %}
```groovy
dependencies {
    implementation 'com.braze:android-sdk-ui:SDK_VERSION' // (Required) Adds dependencies for the Braze SDK and Braze UI components.
    implementation 'com.braze:android-sdk-location:SDK_VERSION' // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% subtab Kotlin DSL %}
```kotlin
dependencies {
    implementation("com.braze:android-sdk-ui:SDK_VERSION") // (Required) Adds dependencies for the Braze SDK and Braze UI components.
    implementation("com.braze:android-sdk-location:SDK_VERSION") // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% subtab Version catalog %}
No seu arquivo `gradle/libs.versions.toml`:

```toml
[versions]
braze = "SDK_VERSION"

[libraries]
braze-android-sdk-ui = { group = "com.braze", name = "android-sdk-ui", version.ref = "braze" }
braze-android-sdk-location = { group = "com.braze", name = "android-sdk-location", version.ref = "braze" }
```

Então, no seu arquivo `build.gradle` ou `build.gradle.kts`, adicione as seguintes dependências. Essa sintaxe é a mesma para Groovy e Kotlin DSL.

```groovy
dependencies {
    implementation(libs.braze.android.sdk.ui) // (Required) Adds dependencies for the Braze SDK and Braze UI components.
    implementation(libs.braze.android.sdk.location) // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Etapa 2: Configure seu `braze.xml`

{% alert note %}
A partir de dezembro de 2019, os pontos de extremidade personalizados não serão mais fornecidos. Se você tiver um ponto de extremidade personalizado pré-existente, poderá continuar a usá-lo. Para obter mais informações, consulte nossa <a href="{{site.baseurl}}/api/basics/#endpoints">lista de endpoints disponíveis</a>.
{% endalert %}

Crie um arquivo `braze.xml` na pasta `res/values` do seu projeto. Se estiver em um cluster de dados específico ou tiver um endpoint personalizado pré-existente, também será necessário especificar o endpoint no arquivo `braze.xml`. 

O conteúdo desse arquivo deve se parecer com o seguinte trecho de código. Certifique-se de substituir `YOUR_APP_IDENTIFIER_API_KEY` pelo identificador encontrado na página **Manage Settings (Gerenciar configurações)** do dashboard do Braze. Faça o registro em [dashboard.braze.com](https://dashboard.braze.com) para encontrar seu [endereço de cluster]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints). 

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
  <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

### Etapa 3: Adicione permissões a `AndroidManifest.xml`

Em seguida, adicione as seguintes permissões ao seu `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert note %}
Com o lançamento do Android M, o Android mudou de um modelo de permissões de tempo de instalação para um modelo de permissões de tempo de execução. No entanto, essas duas permissões são permissões normais e são concedidas automaticamente se estiverem listadas no manifesto do app. Para saber mais, consulte a [documentação de permissões](https://developer.android.com/training/permissions/index.html) do Android.
{% endalert %}

### Etapa 4: Ativar inicialização atrasada (opcional)

Para usar a inicialização atrasada, a versão mínima do SDK do Braze é necessária:

{% sdk_min_versions android:38.0.0 %}

{% alert note %}
Enquanto a inicialização atrasada está ativada, todas as conexões de rede são canceladas, impedindo que o SDK envie dados para os servidores da Braze.
{% endalert %}

#### Etapa 4.1: Atualize seu `braze.xml`

A inicialização atrasada está desativada por padrão. Para ativar, use uma das seguintes opções:

{% tabs %}
{% tab Braze XML file %}
No arquivo `braze.xml` do seu projeto, defina `com_braze_enable_delayed_initialization` como `true`.

```xml
<bool name="com_braze_enable_delayed_initialization">true</bool>
```
{% endtab %}

{% tab At runtime %}
Para ativar a inicialização atrasada em tempo de execução, use o seguinte método.

{% subtabs %}
{% subtab JAVA %}

```java
Braze.enableDelayedInitialization(context);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.enableDelayedInitialization(context)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert note %}
Quando a inicialização atrasada está ativada e uma notificação por push contém uma ação de deep link, o deep link não é resolvido.
{% endalert %}

#### Etapa 4.2: Configurar análise de push (opcional)

Quando a inicialização atrasada está ativada, as análises de push são enfileiradas por padrão. No entanto, você pode optar por [enfileirar explicitamente](#explicitly-queue-push-analytics) ou [descartar](#drop-push-analytics) as análises de push.

##### Enfileirar explicitamente {#explicitly-queue-push-analytics}

Para enfileirar explicitamente as análises de push, escolha uma das seguintes opções:

{% tabs %}
{% tab Braze XML file %}
No seu arquivo `braze.xml`, defina `com_braze_delayed_initialization_analytics_behavior` como `QUEUE`:

```xml
<string name="com_braze_delayed_initialization_analytics_behavior">QUEUE</string>
```
{% endtab %}

{% tab At runtime %}
Adicione `QUEUE` ao seu método [`Braze.enableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-delayed-initialization.html):

{% subtabs %}
{% subtab JAVA %}

```java
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.QUEUE);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.QUEUE)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

##### Descartar {#drop-push-analytics}

Para descartar as análises de push, escolha uma das seguintes opções:

{% tabs %}
{% tab Braze XML file %}
No seu arquivo `braze.xml`, defina `com_braze_delayed_initialization_analytics_behavior` como `DROP`: 

```xml
<string name="com_braze_delayed_initialization_analytics_behavior">DROP</string>
```
{% endtab %}

{% tab At runtime %}
Adicione `DROP` ao método [`Braze.enableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-delayed-initialization.html):

{% subtabs %}
{% subtab JAVA %}

```java
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.DROP);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.DROP)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### Etapa 4.3: Inicializar manualmente o SDK

Após o período de atraso escolhido, use o método [`Braze.disableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-delayed-initialization.html) para inicializar manualmente o SDK.

{% tabs local %}
{% tab JAVA %}

```java
Braze.disableDelayedInitialization(context);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.disableDelayedInitialization(context)
```

{% endtab %}
{% endtabs %}

### Etapa 5: Ativar o rastreamento de sessão do usuário

Quando você ativa o rastreamento de sessão do usuário, chamadas para `openSession()`, `closeSession()`, [`ensureSubscribedToInAppMessageEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/ensure-subscribed-to-in-app-message-events.html) e `InAppMessageManager` podem ser tratadas automaticamente.

Para registrar callbacks do ciclo de vida da atividade, adicione o seguinte código ao método `onCreate()` da sua classe `Application`. 

{% tabs local %}
{% tab JAVA %}

```java
public class MyApplication extends Application {
  @Override
  public void onCreate() {
    super.onCreate();
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class MyApplication : Application() {
  override fun onCreate() {
    super.onCreate()
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener())
  }
}
```

Para a lista de parâmetros disponíveis, veja [`BrazeActivityLifecycleCallbackListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-activity-lifecycle-callback-listener/index.html).

{% endtab %}
{% endtabs %}

## Teste de rastreamento de sessão

{% alert tip %}
Você também pode usar o [SDK Debugger]({{site.baseurl}}/developer_guide/debugging) para diagnosticar problemas do SDK.
{% endalert %}

Se você encontrar problemas durante os testes, ative [logging detalhado](#android_enabling-logs), depois use logcat para detectar chamadas ausentes de `openSession` e `closeSession` em suas atividades.

1. No Braze, acesse **Visão Geral**, selecione seu app e, no dropdown **Exibir Dados Para**, escolha **Hoje**.
    ![A página "Visão Geral" no Braze, com o campo "Exibir Dados Para" definido como "Hoje".]({% image_buster /assets/img_archive/android_sessions.png %})
2. Abra seu app e, em seguida, atualize o dashboard do Braze. Verifique se suas métricas aumentaram em 1.
3. Navegue pelo seu app e verifique se apenas uma sessão foi registrada no Braze.
4. Envie o app para o segundo plano por pelo menos 10 segundos e, em seguida, traga-o para o primeiro plano. Verifique se uma nova sessão foi registrada.

## Configurações opcionais

### Configuração do tempo de execução

Para definir suas opções do Braze no código em vez do seu arquivo `braze.xml`, use [configuração em tempo de execução](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html). Se um valor existir em ambos os lugares, o valor em tempo de execução será usado em vez disso. Depois que todas as configurações necessárias forem fornecidas em tempo de execução, você pode excluir seu arquivo `braze.xml`.

No exemplo a seguir, um [objeto builder](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html) é criado e, em seguida, passado para [`Braze.configure()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html). Observe que apenas algumas das opções de tempo de execução disponíveis são mostradas—consulte nosso [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html) para a lista completa.

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
        .setApiKey("api-key-here")
        .setCustomEndpoint("YOUR_CUSTOM_ENDPOINT_OR_CLUSTER")
        .setSessionTimeout(60)
        .setHandlePushDeepLinksAutomatically(true)
        .setGreatNetworkDataFlushInterval(10)
        .build();
Braze.configure(this, brazeConfig);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
        .setApiKey("api-key-here")
        .setCustomEndpoint("YOUR_CUSTOM_ENDPOINT_OR_CLUSTER")
        .setSessionTimeout(60)
        .setHandlePushDeepLinksAutomatically(true)
        .setGreatNetworkDataFlushInterval(10)
        .build()
Braze.configure(this, brazeConfig)
```

{% endtab %}
{% endtabs %}

{% alert tip %}
Procurando outro exemplo? Confira nosso [app de exemplo Hello Braze](https://github.com/braze-inc/braze-android-sdk/blob/master/samples/hello-braze/src/main/java/com/braze/helloworld/CustomApplication.java).
{% endalert %}

### ID de publicidade do Google

O [ID de Publicidade do Google (GAID)](https://support.google.com/googleplay/android-developer/answer/6048248/advertising-id?hl=en) é um ID opcional, específico do usuário, anônimo, único e redefinível para publicidade, fornecido pelos serviços do Google Play. O GAID permite que os usuários redefinam seu identificador, aceitem anúncios baseados em interesses nos aplicativos do Google Play e fornece aos desenvolvedores um sistema simples e padrão para continuar a monetizar seus apps.

O ID de publicidade do Google não é coletado automaticamente pelo SDK da Braze e deve ser definido manualmente por meio do método [`Braze.setGoogleAdvertisingId()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html).

{% tabs local %}
{% tab JAVA %}

```java
new Thread(new Runnable() {
  @Override
  public void run() {
    try {
      AdvertisingIdClient.Info idInfo = AdvertisingIdClient.getAdvertisingIdInfo(getApplicationContext());
      Braze.getInstance(getApplicationContext()).setGoogleAdvertisingId(idInfo.getId(), idInfo.isLimitAdTrackingEnabled());
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}).start();
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
suspend fun fetchAndSetAdvertisingId(
  context: Context,
  scope: CoroutineScope = GlobalScope
) {
  scope.launch(Dispatchers.IO) {
    try {
      val idInfo = AdvertisingIdClient.getAdvertisingIdInfo(context)
      Braze.getInstance(context).setGoogleAdvertisingId(
        idInfo.id,
        idInfo.isLimitAdTrackingEnabled
      )
    } catch (e: Exception) {
      e.printStackTrace()
    }
  }
}
```

{% endtab %}
{% endtabs %}

{% alert important %}
O Google exige que o ID de publicidade seja coletado em um thread que não seja da UI.
{% endalert %}


### monitoramento de localização

Para ativar a coleta de localização da Braze, defina `com_braze_enable_location_collection` como `true` no seu arquivo `braze.xml`:

```xml
<bool name="com_braze_enable_location_collection">true</bool>
```

{% alert important %}
A partir da versão 3.6.0 do Braze Android SDK, a coleta de locais da Braze é desativada por padrão.
{% endalert %}

### Registro

Por padrão, o nível de registro do Braze Android SDK é definido como `INFO`. Você pode [suprimir esses registros](#android_suppressing-logs) ou [definir um nível de registro diferente](#android_enabling-logs), como `VERBOSE`, `DEBUG` ou `WARN`.

#### Ativando registros

Para ajudar a solucionar problemas no seu app, ou reduzir os tempos de resposta com o suporte da Braze, você pode ativar registros detalhados para o SDK. Quando você enviar registros detalhados para o suporte da Braze, certifique-se de que eles comecem assim que você lançar seu aplicativo e terminem muito depois que seu problema ocorrer. Para uma visão centralizada, veja [Registro detalhado]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging). Para aprender a interpretar a saída do registro, veja [Lendo registros detalhados]({{site.baseurl}}/developer_guide/sdk_integration/reading_verbose_logs).

Lembre-se de que registro detalhados são destinados apenas para o seu ambiente de desenvolvimento, então é interessante desativá-los antes de lançar seu app.

{% alert important %}
Ativar registros detalhados antes de qualquer outra chamada em `Application.onCreate()` para garantir que seus registros sejam o mais completos possível.
{% endalert %}

{% tabs local %}
{% tab Application %}
Para ativar logs diretamente no seu app, adicione o seguinte ao método `onCreate()` do seu aplicativo antes de qualquer outro método.

{% subtabs local %}
{% subtab JAVA %}
```java
BrazeLogger.setLogLevel(Log.MIN_LOG_LEVEL);
```
{% endsubtab %}

{% subtab KOTLIN %}
```kotlin
BrazeLogger.logLevel = Log.MIN_LOG_LEVEL
```
{% endsubtab %}
{% endsubtabs %}

Substitua `MIN_LOG_LEVEL` pelo **Constante** do nível de registro que você gostaria de definir como seu nível de registro mínimo. Quaisquer registro em um nível `>=` para o seu conjunto `MIN_LOG_LEVEL` serão encaminhados para o método padrão do Android [`Log`](https://developer.android.com/reference/android/util/Log). Qualquer registro `<` que você definir como `MIN_LOG_LEVEL` será descartado.

| Constante    | Valor          | Descrição                                                               |
|-------------|----------------|---------------------------------------------------------------------------|
| `VERBOSE`   | 2              | Registra as mensagens mais detalhadas para depuração e desenvolvimento.            |
| `DEBUG`     | 3              | Registra mensagens descritivas para depuração e desenvolvimento.                  |
| `INFO`      | 4              | Registra mensagens informativas para destaques gerais.                       |
| `WARN`      | 5              | Registra mensagens de aviso para identificar situações potencialmente prejudiciais.     |
| `ERROR`     | 6              | Registra mensagens de erro para indicar falha no aplicativo ou problemas sérios. |
| `ASSERT`    | 7              | Registra mensagens de asserção quando as condições são falsas durante o desenvolvimento.     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Por exemplo, o código a seguir encaminhará os níveis de registro `2`, `3`, `4`, `5`, `6` e `7` para o método `Log`.

{% subtabs local %}
{% subtab JAVA %}
```java
BrazeLogger.setLogLevel(Log.VERBOSE);
```
{% endsubtab %}

{% subtab KOTLIN %}
```kotlin
BrazeLogger.logLevel = Log.VERBOSE
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab xml %}
Para ativar registros no `braze.xml`, adicione o seguinte ao seu arquivo:

```xml
<integer name="com_braze_logger_initial_log_level">MIN_LOG_LEVEL</integer>
```

Substitua `MIN_LOG_LEVEL` pelo **Valor** do nível de registro que você gostaria de definir como seu nível de registro mínimo. Quaisquer registro em um nível `>=` para o seu conjunto `MIN_LOG_LEVEL` serão encaminhados para o método padrão do Android [`Log`](https://developer.android.com/reference/android/util/Log). Qualquer registro `<` que você definir como `MIN_LOG_LEVEL` será descartado.

| Constante    | Valor          | Descrição                                                               |
|-------------|----------------|---------------------------------------------------------------------------|
| `VERBOSE`   | 2              | Registra as mensagens mais detalhadas para depuração e desenvolvimento.            |
| `DEBUG`     | 3              | Registra mensagens descritivas para depuração e desenvolvimento.                  |
| `INFO`      | 4              | Registra mensagens informativas para destaques gerais.                       |
| `WARN`      | 5              | Registra mensagens de aviso para identificar situações potencialmente prejudiciais.     |
| `ERROR`     | 6              | Registra mensagens de erro para indicar falha no aplicativo ou problemas sérios. |
| `ASSERT`    | 7              | Registra mensagens de asserção quando as condições são falsas durante o desenvolvimento.     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Por exemplo, o código a seguir encaminhará os níveis de registro `2`, `3`, `4`, `5`, `6` e `7` para o método `Log`.

```xml
<integer name="com_braze_logger_initial_log_level">2</integer>
```
{% endtab %}
{% endtabs %}

#### Verificação de registros detalhados

Para verificar se seus registros estão definidos para `VERBOSE`, verifique se `V/Braze` ocorre em algum lugar nos seus registros. Se isso acontecer, os registros detalhados foram ativados com sucesso. Por exemplo:

```
2077-11-19 16:22:49.591 ? V/Braze v9.0.01 .bo.app.d3: Request started
```

#### Supressão de registros

Para suprimir todos os registros do SDK Android da Braze, defina o nível de registro como `BrazeLogger.SUPPRESS` no método `onCreate()` da sua aplicação _antes_ de qualquer outro método.

{% tabs local %}
{% tab JAVA %}
```java
BrazeLogger.setLogLevel(BrazeLogger.SUPPRESS);
```
{% endtab %}

{% tab KOTLIN %}
```kotlin
BrazeLogger.setLogLevel(BrazeLogger.SUPPRESS)
```
{% endtab %}
{% endtabs %}

### Múltiplas chaves de API

O caso de uso mais comum para várias chaves de API é separar chaves de API para variantes de build de depuração e release.

Para alternar facilmente entre várias chaves de API em suas compilações, recomendamos criar um arquivo `braze.xml` separado para cada [variante de compilação](https://developer.android.com/studio/build/build-variants.html) relevante. Uma variante de compilação é uma combinação de tipo de compilação e sabor do produto. Por padrão, novos projetos Android são configurados com [`debug` e `release` tipos de build](https://developer.android.com/reference/tools/gradle-api/8.3/null/com/android/build/api/dsl/BuildType) e sem sabores de produto.

Para cada variante de build relevante, crie um novo `braze.xml` no diretório `src/<build variant name>/res/values/`. Quando a variante de compilação for compilada, ela usará o nova chave de API.

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">REPLACE_WITH_YOUR_BUILD_VARIANT_API_KEY</string>
</resources>
```

{% alert tip %}
Para aprender a configurar a chave de API no seu código, veja [Configuração em tempo de execução]({{site.baseurl}}/developer_guide/sdk_initalization/?sdktab=android).
{% endalert %}

### Mensagem no app exclusiva TalkBack

Em conformidade com as [diretrizes de acessibilidade do Android](https://developer.android.com/guide/topics/ui/accessibility), o SDK Android da Braze oferece TalkBack por padrão. Para garantir que apenas o conteúdo das mensagens no app seja lido em voz alta—sem incluir outros elementos da tela, como a barra de título do app ou a navegação—você pode ativar o modo exclusivo para o TalkBack.

Para ativar o modo exclusivo para mensagens no app:

{% tabs local %}
{% tab Braze XML %}
```xml
<bool name="com_braze_device_in_app_message_accessibility_exclusive_mode_enabled">true</bool>
```
{% endtab %}

{% tab Kotlin %}
```kotlin
val brazeConfigBuilder = BrazeConfig.Builder()
brazeConfigBuilder.setIsInAppMessageAccessibilityExclusiveModeEnabled(true)
Braze.configure(this, brazeConfigBuilder.build())
```
{% endtab %}

{% tab Java %}
```java
BrazeConfig.Builder brazeConfigBuilder = new BrazeConfig.Builder()
brazeConfigBuilder.setIsInAppMessageAccessibilityExclusiveModeEnabled(true);
Braze.configure(this, brazeConfigBuilder.build());
```
{% endtab %}
{% endtabs %}

### R8 e ProGuard

A configuração de [redução de código](https://developer.android.com/build/shrink-code) é incluída automaticamente com sua integração Braze.

Os aplicativos do cliente que ofuscam o código da Braze devem armazenar arquivos de mapeamento de versão para que a Braze interprete os rastreamentos de pilha. Se você quiser manter todo o código da Braze, adicione o seguinte ao seu arquivo ProGuard:

```
-keep class bo.app.** { *; }
-keep class com.braze.** { *; }
```
