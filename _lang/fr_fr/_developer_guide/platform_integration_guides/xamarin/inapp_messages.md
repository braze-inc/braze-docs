---
nav_title: in-app Messaging
article_title: Messagerie in-App pour Xamarin
platform: 
  - Xamarin
  - iOS
  - Android
page_order: 2
description: "Cet article couvre la messagerie in-app sur iOS, Android et FireOS pour la plateforme Xamarin."
channel: in-app messages
toc_headers: h2
---

# Intégration de messages in-app

> Découvrez comment configurer les messages in-app (IAM) iOS, Android et FireOS pour la plateforme Xamarin.

## Conditions préalables

Pour utiliser cette fonctionnalité, vous devrez [intégrer le SDK Braze pour Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/initial_sdk_setup/).

## Intégration des messages in-app

{% tabs %}
{% tab android %}

{% alert tip %}
Pour voir un exemple, consultez notre [exemple d’application Xamrin sur GitHub](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp).
{% endalert %}

### Étape 1 : Configurer l'enregistrement des messages in-app

Chaque activité de votre application doit être enregistrée avec la classe [`BrazeInAppMessageManager`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/index.html). Pour enregistrer automatiquement les messages in-app à l'aide de l'[intégration du rappel du cycle de vie de l'activité]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android), ajoutez le code suivant à la méthode `onCreate()` de votre classe `Application`:

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
Pour obtenir la liste complète des paramètres disponibles, voir [`BrazeActivityLifecycleCallbackListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-activity-lifecycle-callback-listener/index.html).
{% endalert %}

### Étape 2 : Configurer un gestionnaire de liste de blocage (facultatif)

Pour empêcher certaines activités d'afficher des messages in-app, utilisez l'[intégration de la fonction de rappel du cycle de vie de l'activité]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android). L'exemple de code suivant ajoute deux activités à la liste de blocage de l'enregistrement des messages in-app : `SplashActivity` et `SettingsActivity`.

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
Pour voir un exemple, consultez notre [exemple d’application Xamrin sur GitHub](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/ios-net-maui/BrazeiOSMauiSampleApp/BrazeiOSMauiSampleApp).
{% endalert %}

Pour utiliser l'interface utilisateur par défaut des messages in-app de Braze, créez d'abord une nouvelle `BrazeInAppMessageUI` :
```csharp
public static BrazeInAppMessageUI? inAppMessageUI = new BrazeInAppMessageUI();
```

Ensuite, enregistrez le site `BrazeInAppMessageUI` en tant que présentateur de messages in-app lors de la configuration de votre instance Braze :
```csharp
braze.InAppMessagePresenter = inAppMessageUI;
```

Vous pouvez désormais présenter de nouveaux messages in-app à l'aide de l'interface utilisateur par défaut des messages in-app de Braze.
{% endtab %}
{% endtabs %}

## Support GIF

{% multi_lang_include wrappers/gif_support/in_app_messaging.md %}
