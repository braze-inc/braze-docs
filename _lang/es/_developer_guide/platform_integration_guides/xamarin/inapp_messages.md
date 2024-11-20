---
nav_title: Enviar mensajes dentro de la aplicación
article_title: Mensajería dentro de la aplicación para Xamarin
platform: 
  - Xamarin
  - iOS
  - Android
page_order: 2
description: "En este artículo se cubre la mensajería dentro de la aplicación de iOS, Android y FireOS para la plataforma Xamarin."
channel: in-app messages
toc_headers: h2
---

# Integración de mensajería dentro de la aplicación

> Aprende a configurar los mensajes dentro de la aplicación (IAM) de iOS, Android y FireOS para la plataforma Xamarin.

## Requisitos previos

Para utilizar esta característica, tendrás que [integrar el SDK de Braze para Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/initial_sdk_setup/).

## Integración de la mensajería dentro de la aplicación

{% tabs %}
{% tab Android %}

{% alert tip %}
Para ver un ejemplo, consulta nuestra [aplicación Xamarin de muestra en GitHub](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp).
{% endalert %}

### Paso 1: Configurar el registro de mensajes dentro de la aplicación

Cada actividad de tu aplicación debe estar registrada en la clase [`BrazeInAppMessageManager`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/index.html). Para registrar automáticamente mensajes dentro de la aplicación mediante la [integración de la devolución de llamada del ciclo de vida de la actividad]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android), añade el siguiente código al método `onCreate()` de tu clase `Application`:

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
Para ver la lista completa de parámetros disponibles, consulta [`BrazeActivityLifecycleCallbackListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-activity-lifecycle-callback-listener/index.html).
{% endalert %}

### Paso 2: Configura un administrador de listas de bloqueo (opcional)

Para evitar que ciertas actividades muestren mensajes dentro de la aplicación, utiliza la [integración de devolución de llamada del ciclo de vida de la actividad]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android). El siguiente código de ejemplo añade dos actividades a la lista de bloqueo de registro de mensajes dentro de la aplicación: `SplashActivity` y `SettingsActivity`.

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
Para ver un ejemplo, consulta nuestra [aplicación Xamarin de muestra en GitHub](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/ios-net-maui/BrazeiOSMauiSampleApp/BrazeiOSMauiSampleApp).
{% endalert %}

Para utilizar la interfaz predeterminada de mensajes dentro de la aplicación de Braze, primero crea una nueva `BrazeInAppMessageUI`:
```csharp
public static BrazeInAppMessageUI? inAppMessageUI = new BrazeInAppMessageUI();
```

A continuación, registra `BrazeInAppMessageUI` como presentador de mensajes dentro de la aplicación cuando configures tu instancia de Braze:
```csharp
braze.InAppMessagePresenter = inAppMessageUI;
```

Ahora puedes presentar nuevos mensajes dentro de la aplicación utilizando la interfaz predeterminada de mensajes dentro de la aplicación de Braze.
{% endtab %}
{% endtabs %}

## Soporte de GIF

{% multi_lang_include wrappers/gif_support/in_app_messaging.md %}
