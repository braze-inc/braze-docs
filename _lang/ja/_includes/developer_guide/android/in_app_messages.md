{% multi_lang_include developer_guide/prerequisites/android.md %} アプリ内メッセージも有効にする必要がある。

## メッセージの種類

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/android.md %}
{% endtabs %}

## アプリ内メッセージを有効にする

### ステップ 1: 登録する `BrazeInAppMessageManager`

アプリ内メッセージ表示は [`BrazeInAppMessageManager`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/index.html) クラスによって管理されまｓ。アプリ内のすべてのアクティビティを `BrazeInAppMessageManager` に登録して、アプリ内メッセージビューをビュー階層に追加できるようにする必要があります。これを行うには次の 2 つの方法があります。

{% tabs local %}
{% tab 自動的に %}
[アクティビティライフサイクルコールバック統合]({{site.baseurl}}/developer_guide/sdk_integration#android_step-4-enable-user-session-tracking)はアプリ内メッセージ登録を自動的に処理するため、追加の統合は不要です。これはアプリ内メッセージ登録の推奨方法である。
{% endtab %}

{% tab 手動で %}
{% alert warning %}
自動登録にアクティビティ・ライフサイクル・コールバックを使用している場合は、このステップを完了させないこと。
{% endalert %}

あなたの [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate())を呼び出す [`ensureSubscribedToInAppMessageEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/ensure-subscribed-to-in-app-message-events.html):

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

アプリ内メッセージを表示できるすべてのアクティビティで、そのアクティビティの [`registerInAppMessageManager()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/register-in-app-message-manager.html)`onResume()`を呼び出す：

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

がコールされたすべてのアクティビティにおいてである。 [`registerInAppMessageManager()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/register-in-app-message-manager.html)が呼び出されたすべてのアクティビティで、そのアクティビティの [`unregisterInAppMessageManager()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/unregister-in-app-message-manager.html)`onPause()`を呼び出す：

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

### ステップ 2:マネージャーのブロックリストを更新する（オプション）

統合では、アプリ内の特定のアクティビティにアプリ内メッセージを表示しないようにする必要が生じる場合があります。[アクティビティライフサイクルコールバックの統合]({{site.baseurl}}/developer_guide/sdk_integration#android_step-4-enable-user-session-tracking)により、これを簡単に実現できます。

次のサンプルコードでは、アプリ内メッセージ登録禁止リストに `SplashActivity` と `SettingsActivity` という 2 つのアクティビティを追加します。

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
