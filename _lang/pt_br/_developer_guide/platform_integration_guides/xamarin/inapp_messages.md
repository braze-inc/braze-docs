---
nav_title: Mensagem no app
article_title: Envio de mensagens no app para Xamarin
platform: 
  - Xamarin
  - iOS
  - Android
page_order: 2
description: "Este artigo aborda o envio de mensagens no app para iOS, Android e FireOS para a plataforma Xamarin."
channel: in-app messages
toc_headers: h2
---

# Integração de envio de mensagens no app

> Saiba como configurar mensagens no app (IAM) para iOS, Android e FireOS na plataforma Xamarin.

## Pré-requisitos

Para usar esse recurso, você precisará [integrar o SDK da Braze para Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/initial_sdk_setup/).

## Integração de mensagens no app

{% tabs %}
{% tab Android %}

{% alert tip %}
Para ver um exemplo, confira nosso [app Xamrin de amostra no GitHub](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp).
{% endalert %}

### Etapa 1: Configure o registro de mensagens no app

Todas as atividades do seu app devem ser registradas com a classe [`BrazeInAppMessageManager`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/index.html) classe. Para registrar automaticamente as mensagens no app usando a [integração do retorno de chamada do ciclo de vida da atividade]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android), adicione o seguinte código ao método `onCreate()` na sua classe `Application`:

{% subtabs %}
{% subtab JAVA %}
```java
public class MyApplication extends Application {
  @Override
  public void onCreate() {
    super.onCreate();
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
  }
}
```
{% endsubtab %}

{% subtab KOTLIN %}
```kotlin
class MyApplication : Application() {
  override fun onCreate() {
    super.onCreate()
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener())
  }
}
```
{% endsubtab %}
{% endsubtabs %}

{% alert note %}
Para obter a lista completa dos parâmetros disponíveis, consulte [`BrazeActivityLifecycleCallbackListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-activity-lifecycle-callback-listener/index.html).
{% endalert %}

### Etapa 2: Configurar um gerenciador de listas de bloqueio (opcional)

Para evitar que determinadas atividades exibam mensagens no app, use a [integração do retorno de chamada do ciclo de vida da atividade]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android). O código de exemplo a seguir adiciona duas atividades à lista de bloqueio de registro de mensagens no app: `SplashActivity` e `SettingsActivity`.

{% subtabs %}
{% subtab JAVA %}
```java
public class MyApplication extends Application {
  @Override
  public void onCreate() {
    super.onCreate();
    Set<Class> inAppMessageBlocklist = new HashSet<>();
    inAppMessageBlocklist.add(SplashActivity.class);
    inAppMessageBlocklist.add(SettingsActivity.class);
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener(inAppMessageBlocklist));
  }
}
```
{% endsubtab %}

{% subtab KOTLIN %}
```kotlin
class MyApplication : Application() {
  override fun onCreate() {
    super.onCreate()
    val inAppMessageBlocklist = HashSet<Class<*>>()
    inAppMessageBlocklist.add(SplashActivity::class.java)
    inAppMessageBlocklist.add(SettingsActivity::class.java)
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener(inAppMessageBlocklist))
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab ios %}
{% alert tip %}
Para ver um exemplo, confira nosso [app Xamrin de amostra no GitHub](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/ios-net-maui/BrazeiOSMauiSampleApp/BrazeiOSMauiSampleApp).
{% endalert %}

Para usar a interface de mensagens no app padrão da Braze, primeiro crie um novo `BrazeInAppMessageUI`:
```csharp
public static BrazeInAppMessageUI? inAppMessageUI = new BrazeInAppMessageUI();
```

Em seguida, registre o `BrazeInAppMessageUI` como o apresentador de mensagens no app ao configurar sua instância do Braze:
```csharp
braze.InAppMessagePresenter = inAppMessageUI;
```

Agora você pode apresentar novas mensagens no app usando a interface de usuário padrão de mensagens no app do Braze.
{% endtab %}
{% endtabs %}

## Suporte a GIF

{% multi_lang_include wrappers/gif_support/in_app_messaging.md %}
