{% multi_lang_include developer_guide/prerequisites/android.md %} 인앱 메시지를 활성화해야 합니다.

## 메시지 유형

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/android.md %}
{% endtabs %}

## 인앱 메시지 활성화

### 1단계: 등록 `BrazeInAppMessageManager`

인앱 메시지 표시는 [`BrazeInAppMessageManager`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/index.html) 클래스에 의해 관리됩니다. 앱의 모든 활동을 `BrazeInAppMessageManager`에 등록해야 인앱 메시지 보기를 보기 계층 구조에 추가할 수 있습니다. 이를 달성하는 방법에는 두 가지가 있습니다:

{% tabs local %}
{% tab 자동으로 %}
[활동 수명 주기 콜백 통합]({{site.baseurl}}/developer_guide/sdk_integration#android_step-4-enable-user-session-tracking)은 인앱 메시지 등록을 자동으로 처리하므로 추가 통합이 필요하지 않습니다. 이것은 인앱 메시지 등록을 처리하는 권장 방법입니다.
{% endtab %}

{% tab 수동으로 %}
{% alert warning %}
자동 등록을 위한 활동 생명주기 콜백을 사용하는 경우, 이 단계를 완료하지 마십시오.
{% endalert %}

당신의 [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate())에서, [`ensureSubscribedToInAppMessageEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/ensure-subscribed-to-in-app-message-events.html)를 호출하십시오:

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

인앱 메시지를 표시할 수 있는 모든 활동에서, 해당 활동의 `onResume()`에서 [`registerInAppMessageManager()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/register-in-app-message-manager.html)을 호출하십시오:

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

[`registerInAppMessageManager()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/register-in-app-message-manager.html)이 호출된 모든 활동에서, 해당 활동의 `onPause()`에서 [`unregisterInAppMessageManager()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/unregister-in-app-message-manager.html)을 호출하십시오:

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

### 2단계: 매니저의 블록리스트를 업데이트하십시오 (선택 사항)

통합 시 앱의 특정 활동이 인앱 메시지를 표시하지 않도록 요구할 수 있습니다. [활동 수명 주기 콜백 통합]({{site.baseurl}}/developer_guide/sdk_integration#android_step-4-enable-user-session-tracking)은 이를 쉽게 수행할 수 있는 방법을 제공합니다.

다음 샘플 코드에서는 인앱 메시지 등록 차단 목록에 두 가지 활동(`SplashActivity` 및 `SettingsActivity`)을 추가합니다.

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
