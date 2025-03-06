---
nav_title: In-App Messages
article_title: In-App Messages for the Braze Xamarin SDK
platform: 
  - Xamarin
  - iOS
  - Android
page_order: 2
description: "This article covers iOS, Android, and FireOS in-app messaging for the Xamarin platform."
channel: in-app messages
toc_headers: h2
---

# In-app messages

> Learn how to set up iOS, Android, and FireOS In-App Messages (IAM) for the Xamarin platform.

{% multi_lang_include developer_guide/prerequisites/xamarin.md %}

## Setting up in-app messages

{% tabs %}
{% tab android %}

{% alert tip %}
To see an example, check out our [sample Xamrin app on GitHub](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp).
{% endalert %}

### Step 1: Set up in-app message registration

Every activity in your app must be registered with the [`BrazeInAppMessageManager`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/index.html) class. To automatically register in-app messages using the [activity lifecycle callback integration]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android), add the following code to the `onCreate()` method in your `Application` class:

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
For the full list of available parameters, see [`BrazeActivityLifecycleCallbackListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-activity-lifecycle-callback-listener/index.html).
{% endalert %}

### Step 2: Set up a blocklist manager (optional)

To prevent certain activities from displaying in-app messages, use the [activity lifecycle callback integration]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android). The following sample code adds two activities to the in-app message registration blocklist: `SplashActivity` and `SettingsActivity`.

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
To see an example, check out our [sample Xamrin app on GitHub](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/ios-net-maui/BrazeiOSMauiSampleApp/BrazeiOSMauiSampleApp).
{% endalert %}

To use Braze's default in-app message UI, first create a new `BrazeInAppMessageUI`:
```csharp
public static BrazeInAppMessageUI? inAppMessageUI = new BrazeInAppMessageUI();
```

Then, register the `BrazeInAppMessageUI` as the in-app message presenter when setting up your Braze instance:
```csharp
braze.InAppMessagePresenter = inAppMessageUI;
```

Now you can present new in-app messages using Braze's default in-app message UI.
{% endtab %}
{% endtabs %}

## GIF Support

{% multi_lang_include wrappers/gif_support/in_app_messaging.md %}
