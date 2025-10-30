{% multi_lang_include developer_guide/prerequisites/android.md %} Vous devrez également activer les messages in-app.

## Types de messages

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/android.md %}
{% endtabs %}

## Activation des messages in-app

### Étape 1 : Registre `BrazeInAppMessageManager`

L’affichage des messages in-app est géré par la classe [`BrazeInAppMessageManager`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/index.html). Chaque activité de votre application doit être enregistrée avec le `BrazeInAppMessageManager` pour lui permettre d’ajouter des vues de messages in-app à la hiérarchie de vues. Il existe deux manières de le faire :

{% tabs local %}
{% tab automatiquement %}
L'[intégration du rappel du cycle de vie de l'activité]({{site.baseurl}}/developer_guide/sdk_integration#android_step-4-enable-user-session-tracking) gère automatiquement l'enregistrement des messages in-app ; aucune intégration supplémentaire n'est nécessaire. C'est la méthode recommandée pour l'envoi de messages in-app.
{% endtab %}

{% tab manuellement %}
{% alert warning %}
Si vous utilisez le rappel du cycle de vie de l'activité pour l'enregistrement automatique, ne terminez pas cette étape.
{% endalert %}

Dans votre [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate())appel [`ensureSubscribedToInAppMessageEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/ensure-subscribed-to-in-app-message-events.html):

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

Dans chaque activité où des messages in-app peuvent être affichés, appelez [`registerInAppMessageManager()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/register-in-app-message-manager.html) dans le site `onResume()` de cette activité :

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

Dans toutes les activités où [`registerInAppMessageManager()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/register-in-app-message-manager.html) a été appelé, appelez [`unregisterInAppMessageManager()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/unregister-in-app-message-manager.html) dans l'activité `onPause()`:

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

### Étape 2 : Mettre à jour la liste de blocage du gestionnaire (facultatif)

Dans votre intégration, vous pouvez exiger que certaines activités de votre application n’affichent pas de messages in-app. L'[intégration du rappel du cycle de vie de l'activité]({{site.baseurl}}/developer_guide/sdk_integration#android_step-4-enable-user-session-tracking) offre un moyen simple d'y parvenir.

L'exemple de code suivant ajoute deux activités à la liste de blocage de l'enregistrement des messages in-app, `SplashActivity` et `SettingsActivity`:

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
