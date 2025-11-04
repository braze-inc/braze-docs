{% multi_lang_include developer_guide/prerequisites/android.md %} Sie müssen auch In-App-Nachrichten aktivieren.

## Nachrichtentypen

{% tabs %}
{% multi_lang_include developer_guide/_shared/push_notifications/message_types/android.md %}
{% endtabs %}

## Aktivieren von In-App-Nachrichten

### Schritt 1: Registrieren Sie sich `BrazeInAppMessageManager`

Die Anzeige von In-App-Nachrichten wird von der Klasse [`BrazeInAppMessageManager`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/index.html) verwaltet. Jede Aktivität in Ihrer App muss bei `BrazeInAppMessageManager` registriert sein, damit sie In-App-Nachricht-Ansichten zur Ansichtshierarchie hinzufügen kann. Es gibt zwei Möglichkeiten, dies zu erreichen:

{% tabs local %}
{% tab automatisch %}
Die [Callback-Integration für den Aktivitätslebenszyklus]({{site.baseurl}}/developer_guide/platforms/android/sdk_integration/#android_step-3-enable-user-session-tracking) verarbeitet die Registrierung von In-App-Nachrichten automatisch; eine zusätzliche Integration ist nicht erforderlich. Dies ist die empfohlene Methode für die Registrierung von In-App-Nachrichten.
{% endtab %}

{% tab manuell %}
{% alert warning %}
Wenn Sie den Activity Lifecycle Callback für die automatische Registrierung verwenden, brauchen Sie diesen Schritt nicht auszuführen.
{% endalert %}

In Ihrem [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()), Anruf [`ensureSubscribedToInAppMessageEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/ensure-subscribed-to-in-app-message-events.html):

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

In jeder Aktivität, in der In-App-Nachrichten angezeigt werden können, rufen Sie [`registerInAppMessageManager()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/register-in-app-message-manager.html) in der jeweiligen Aktivität `onResume()` auf:

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

Bei jeder Aktivität, bei der [`registerInAppMessageManager()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/register-in-app-message-manager.html) aufgerufen wurde, rufen Sie [`unregisterInAppMessageManager()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/unregister-in-app-message-manager.html) in der jeweiligen Aktivität `onPause()` auf:

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

### Schritt 2: Update der Blockliste des Managers (optional)

In Ihrer Integration können Sie festlegen, dass bestimmte Aktivitäten in Ihrer App keine In-App-Nachrichten anzeigen sollen. Die [Integration von Callbacks in den Aktivitätslebenszyklus]({{site.baseurl}}/developer_guide/platforms/android/sdk_integration/#android_step-3-enable-user-session-tracking) bietet eine einfache Möglichkeit, dies zu erreichen.

Der folgende Code fügt der Blockliste für die Registrierung von In-App-Nachrichten zwei Aktivitäten hinzu: `SplashActivity` und `SettingsActivity`:

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
