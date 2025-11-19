{% multi_lang_include developer_guide/prerequisites/android.md %} Você também precisará ativar mensagens no app.

## Tipos de mensagens

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/android.md %}
{% endtabs %}

## Ativação de mensagens no app

### Etapa 1: Registrar `BrazeInAppMessageManager`

A exibição de mensagens no app é gerenciada pela classe [`BrazeInAppMessageManager`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/index.html). Todas as atividades do seu app devem ser registradas no site `BrazeInAppMessageManager` para permitir que ele adicione visualizações de mensagens no app à hierarquia de visualizações. Há duas maneiras de fazer isso:

{% tabs local %}
{% tab automaticamente %}
A [integração do retorno de chamada do ciclo de vida da atividade]({{site.baseurl}}/developer_guide/sdk_integration#android_step-4-enable-user-session-tracking) lida automaticamente com o registro de mensagens no app; não é necessária nenhuma integração extra. Este é o método recomendado para lidar com o registro de mensagens no app.
{% endtab %}

{% tab manualmente %}
{% alert warning %}
Se você estiver usando retorno de chamada do ciclo de vida da atividade para registro automático, não complete esta etapa.
{% endalert %}

Em seu [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()), chame [`ensureSubscribedToInAppMessageEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/ensure-subscribed-to-in-app-message-events.html):

{% subtabs %}
{% subtab JAVA %}

```java
BrazeInAppMessageManager.getInstance().ensureSubscribedToInAppMessageEvents(context);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
BrazeInAppMessageManager.getInstance().ensureSubscribedToInAppMessageEvents(context)
```

{% endsubtab %}
{% endsubtabs %}

Em cada atividade onde mensagens no app podem ser exibidas, chame [`registerInAppMessageManager()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/register-in-app-message-manager.html) no `onResume()` dessa atividade:

{% subtabs %}
{% subtab JAVA %}

```java
@Override
public void onResume() {
  super.onResume();
  // Registers the BrazeInAppMessageManager for the current Activity. This Activity will now listen for
  // in-app messages from Braze.
  BrazeInAppMessageManager.getInstance().registerInAppMessageManager(activity);
}
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
public override fun onResume() {
  super.onResume()
  // Registers the BrazeInAppMessageManager for the current Activity. This Activity will now listen for
  // in-app messages from Braze.
  BrazeInAppMessageManager.getInstance().registerInAppMessageManager(this)
}
```

{% endsubtab %}
{% endsubtabs %}

Em cada atividade onde [`registerInAppMessageManager()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/register-in-app-message-manager.html) foi chamado, chame [`unregisterInAppMessageManager()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/unregister-in-app-message-manager.html) no `onPause()` dessa atividade:

{% subtabs %}
{% subtab JAVA %}

```java
@Override
public void onPause() {
  super.onPause();
  // Unregisters the BrazeInAppMessageManager for the current Activity.
  BrazeInAppMessageManager.getInstance().unregisterInAppMessageManager(activity);
}
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
public override fun onPause() {
  super.onPause()
  // Unregisters the BrazeInAppMessageManager.
  BrazeInAppMessageManager.getInstance().unregisterInAppMessageManager(this)
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Etapa 2: Atualize a lista de bloqueio do gerente (opcional)

Em sua integração, você pode exigir que determinadas atividades em seu app não mostrem mensagens no app. A [integração do retorno de chamada do ciclo de vida da atividade]({{site.baseurl}}/developer_guide/sdk_integration#android_step-4-enable-user-session-tracking) oferece uma maneira fácil de fazer isso.

O código de exemplo a seguir adiciona duas atividades à lista de bloqueio de registro de mensagens no app: `SplashActivity` e `SettingsActivity`.

{% subtabs local %}
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
