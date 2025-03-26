---
nav_title: In-App-Messaging
article_title: In-App-Nachrichten für Xamarin
platform: 
  - Xamarin
  - iOS
  - Android
page_order: 2
description: "Dieser Artikel beschreibt iOS-, Android- und FireOS-In-App-Nachrichten für die Xamarin Plattform."
channel: in-app messages
toc_headers: h2
---

# Integration von In-App-Nachrichten

> Erfahren Sie, wie Sie iOS-, Android- und FireOS-In-App-Nachrichten (IAM) für die Xamarin-Plattform einrichten.

## Voraussetzungen

Um das Feature zu nutzen, müssen Sie [das Braze SDK für Xamarin integrieren]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/initial_sdk_setup/).

## Integration von In-App-Nachrichten

{% tabs %}
{% tab android %}

{% alert tip %}
In unserer [Xamrin-App auf GitHub](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp) können Sie sich ein Beispiel ansehen.
{% endalert %}

### Schritt 1: Registrierung von In-App-Nachrichten einrichten

Jede Aktivität in Ihrer App muss bei der [`BrazeInAppMessageManager`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/index.html) Klasse registriert sein. Um In-App-Nachrichten automatisch über die [Integration von Callbacks für den Lebenszyklus von Aktivitäten]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android) zu registrieren, fügen Sie den folgenden Code zur Methode `onCreate()` in der Klasse `Application` hinzu:

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
Die vollständige Liste der verfügbaren Parameter finden Sie unter [`BrazeActivityLifecycleCallbackListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-activity-lifecycle-callback-listener/index.html).
{% endalert %}

### Schritt 2: Einen Blocklisten-Manager einrichten (optional)

Um zu verhindern, dass bestimmte Aktivitäten In-App-Nachrichten anzeigen, verwenden Sie die [Integration von Callbacks für den Lebenszyklus von Aktivitäten]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android). Der folgende Beispielcode fügt der Blockliste für die Registrierung von In-App-Nachrichten zwei Aktivitäten hinzu: `SplashActivity` und `SettingsActivity`.

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
In unserer [Xamrin-App auf GitHub](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/ios-net-maui/BrazeiOSMauiSampleApp/BrazeiOSMauiSampleApp) können Sie sich ein Beispiel ansehen.
{% endalert %}

Um die standardmäßige In-App-Nachrichten-UI von Braze zu verwenden, erstellen Sie zunächst eine neue `BrazeInAppMessageUI`:
```csharp
public static BrazeInAppMessageUI? inAppMessageUI = new BrazeInAppMessageUI();
```

Registrieren Sie dann die `BrazeInAppMessageUI` als In-App-Nachricht-Presenter, wenn Sie Ihre Braze-Instanz einrichten:
```csharp
braze.InAppMessagePresenter = inAppMessageUI;
```

Jetzt können Sie neue In-App-Nachrichten über die standardmäßige In-App-Nachrichten-Benutzeroberfläche von Braze präsentieren.
{% endtab %}
{% endtabs %}

## GIF-Unterstützung

{% multi_lang_include wrappers/gif_support/in_app_messaging.md %}
