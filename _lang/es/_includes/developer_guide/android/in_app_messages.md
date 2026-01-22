{% multi_lang_include developer_guide/prerequisites/android.md %} También tendrás que habilitar los mensajes dentro de la aplicación.

## Tipos de mensajes

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/android.md %}
{% endtabs %}

## Habilitación de mensajes dentro de la aplicación

### Paso 1: Registro `BrazeInAppMessageManager`

La visualización de mensajes dentro de la aplicación es gestionada por la clase [`BrazeInAppMessageManager`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/index.html). Cada actividad de tu aplicación debe registrarse en `BrazeInAppMessageManager` para que pueda añadir vistas de mensajes dentro de la aplicación a la jerarquía de vistas. Hay dos formas de conseguirlo:

{% tabs local %}
{% tab automáticamente %}
La [integración de la devolución de llamada del ciclo de vida de la actividad]({{site.baseurl}}/developer_guide/sdk_integration#android_step-4-enable-user-session-tracking) gestiona automáticamente el registro de mensajes dentro de la aplicación; no se requiere ninguna integración adicional. Este es el método recomendado para gestionar el registro de mensajes dentro de la aplicación.
{% endtab %}

{% tab manualmente %}
{% alert warning %}
Si utilizas la devolución de llamada del ciclo de vida de la actividad para el registro automático, no completes este paso.
{% endalert %}

En tu [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate())llamada [`ensureSubscribedToInAppMessageEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/ensure-subscribed-to-in-app-message-events.html):

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

En cada actividad en la que se puedan mostrar mensajes dentro de la aplicación, llama a [`registerInAppMessageManager()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/register-in-app-message-manager.html) en la página `onResume()` de esa actividad:

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

En cada actividad en la que [`registerInAppMessageManager()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/register-in-app-message-manager.html) se ha llamado, llama a [`unregisterInAppMessageManager()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/unregister-in-app-message-manager.html) en la página `onPause()` de esa actividad:

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

### Paso 2: Actualizar la lista de bloqueo del administrador (opcional)

En tu integración, puedes requerir que ciertas actividades de tu aplicación no muestren mensajes dentro de la aplicación. La [integración de la devolución de llamada del ciclo de vida de la actividad]({{site.baseurl}}/developer_guide/sdk_integration#android_step-4-enable-user-session-tracking) proporciona una forma sencilla de conseguirlo.

El siguiente código de ejemplo añade dos actividades a la lista de bloqueo de registro de mensajes dentro de la aplicación, `SplashActivity` y `SettingsActivity`:

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
