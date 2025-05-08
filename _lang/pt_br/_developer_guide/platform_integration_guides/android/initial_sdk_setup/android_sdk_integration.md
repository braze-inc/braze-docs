---
nav_title: Integração de SDK para Android
article_title: Integração do SDK do Android para Android e FireOS
page_order: 0
platform: 
  - Android
  - FireOS
description: "Este artigo de referência aborda como integrar o SDK do Android em seu aplicativo Android ou FireOS."
search_rank: 4
---

# Integração do SDK do Android

> Este artigo de referência aborda como integrar o SDK do Android em seu aplicativo Android ou FireOS. A instalação do SDK da Braze fornecerá a funcionalidade básica de análise de dados e mensagens no app com as quais você poderá engajar seus usuários.

{% alert note %}
Para obter o desempenho ideal no Android 12, recomendamos fazer upgrade para o [Braze Android SDK v13.1.2+](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#1312) assim que possível. Para saber mais, consulte nosso [guia de atualização do Android 12]({{site.baseurl}}/android_12/).
{% endalert %}

## Etapa 1: Integrar a biblioteca do Braze

Opcionalmente, o SDK da Braze para Adndroid pode ser integrado sem componentes de interface do usuário. No entanto, os cartões de conteúdo e o envio de mensagens no app ficarão inoperantes, a menos que você passe os dados personalizados para uma interface de usuário exclusivamente de seu projeto. Além disso, as notificações por push não funcionarão porque nosso código de tratamento de push está na biblioteca da interface do usuário. É importante notar que esses elementos da interface do usuário são totalmente personalizáveis. Recomendamos enfaticamente a integração desses recursos. Consulte os [cartões de conteúdo]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/#advantages-of-using-content-cards) e a documentação de [mensagens no app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/) para obter uma lista dos benefícios do uso de cada canal ou ferramenta.

### Integração básica

Para acessar os recursos de envio de mensagens do Braze, você deve integrar a biblioteca da interface do usuário. Consulte as seguintes instruções do Android Studio para integrar a biblioteca da interface do usuário, dependendo do seu IDE:

#### Adicionar dependência de Braze

Adicione a dependência `android-sdk-ui` ao `build.gradle` de seu app. 

Se estiver usando qualquer local ou funcionalidade de geofence da Braze, inclua também `android-sdk-location` no `build.gradle` do seu app.

{% alert important %}
Se estiver usando um SDK não nativo do Android (por exemplo, Flutter, Cordova, Unity, etc.), esse SDK já tem a dependência `android-sdk-ui` para a versão correta do SDK do Android. Não atualize essa versão manualmente.
{% endalert %}

```gradle
dependencies {
  implementation "com.braze:android-sdk-ui:+"
  implementation "com.braze:android-sdk-location:+"
}
```

O exemplo a seguir mostra onde colocar a linha de dependência em seu site `build.gradle`. Note que a versão usada no exemplo usa uma versão antiga. Visite as [versões do Braze Android](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md) SDK para obter a versão mais atualizada do Braze Android SDK.

![O Android Studio está exibindo o arquivo "build.gradle", com o código de dependência adicionado à ponta do arquivo.]({% image_buster /assets/img_archive/androidstudio2.png %})

#### Realizar a sincronização do Gradle

Certifique-se de executar uma sincronização do Gradle para criar seu projeto e incorporar as [adições de dependência](#add-braze-dependency).

![Um banner no Android Studio informando: "Os arquivos do Gradle foram alterados desde a última sincronização do projeto. Pode ser necessária uma sincronização de projeto para que o IDE funcione corretamente. Sync Now."]({% image_buster /assets/img_archive/androidstudio3.png %})

## Etapa 2: Configure o SDK da Braze em braze.xml

{% alert note %}
A partir de dezembro de 2019, os pontos de extremidade personalizados não serão mais fornecidos. Se você tiver um ponto de extremidade personalizado pré-existente, poderá continuar a usá-lo. Para obter mais informações, consulte nossa <a href="{{site.baseurl}}/api/basics/#endpoints">lista de endpoints disponíveis</a>.
{% endalert %}

Agora que as bibliotecas foram integradas, você deve criar um arquivo `braze.xml` na pasta `res/values` do seu projeto. Se estiver em um cluster de dados específico ou tiver um endpoint personalizado pré-existente, também será necessário especificar o endpoint no arquivo `braze.xml`. 

O conteúdo desse arquivo deve se parecer com o seguinte trecho de código. Certifique-se de substituir `YOUR_APP_IDENTIFIER_API_KEY` pelo identificador encontrado na página **Manage Settings (Gerenciar configurações)** do dashboard do Braze. Faça o registro em [dashboard.braze.com](https://dashboard.braze.com) para encontrar seu [endereço de cluster]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints). 

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
<string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

## Etapa 3: Adicione as permissões necessárias para AndroidManifest.xml
Agora que você adicionou sua chave de API, é necessário adicionar as seguintes permissões ao seu site `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert note %}
Com o lançamento do Android M, o Android mudou de um modelo de permissões de tempo de instalação para um modelo de permissões de tempo de execução. No entanto, essas duas permissões são permissões normais e são concedidas automaticamente se estiverem listadas no manifesto do app. Para saber mais, consulte a [documentação de permissões](https://developer.android.com/training/permissions/index.html) do Android.
{% endalert %}

## Etapa 4: Rastreamento de sessões de usuário no Android

### Integração do retorno de chamada do ciclo de vida da atividade

As chamadas para `openSession()`, `closeSession()`, [`ensureSubscribedToInAppMessageEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/ensure-subscribed-to-in-app-message-events.html) e `InAppMessageManager` são opcionalmente tratadas automaticamente.

#### Registrar retornos de chamada do ciclo de vida da atividade

Adicione o seguinte código ao método `onCreate()` de sua classe `Application`:

{% tabs %}
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

{% endtab %}
{% endtabs %}

Consulte nossa documentação de referência do SDK para obter mais informações sobre os parâmetros disponíveis para o [`BrazeActivityLifecycleCallbackListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-activity-lifecycle-callback-listener/index.html).

## Etapa 5: Ativar o monitoramento de localização

Se quiser ativar a coleta de locais da Braze, atualize seu arquivo `braze.xml` para incluir `com_braze_enable_location_collection` e confira se o seu valor esteja definido como `true`:

```xml
<bool name="com_braze_enable_location_collection">true</bool>
```

{% alert important %}
A partir da versão 3.6.0 do Braze Android SDK, a coleta de locais da Braze é desativada por padrão.
{% endalert %}

## Integração completa de SDK

A Braze agora poderá coletar [dados especificados de seu aplicativo]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/) e sua integração básica deverá estar concluída.

Visite os artigos a seguir para ativar [o rastreamento de eventos personalizados, o]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/) [envio de mensagens]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/), [os cartões de conteúdo]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/integration/) e o conjunto completo de recursos do Braze.

