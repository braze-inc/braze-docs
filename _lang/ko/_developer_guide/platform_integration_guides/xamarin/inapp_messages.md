---
nav_title: 인앱 메시징
article_title: Xamarin용 인앱 메시징
platform: 
  - Xamarin
  - iOS
  - Android
page_order: 2
description: "이 문서에서는 Xamarin 플랫폼용 iOS, Android 및 FireOS 인앱 메시징을 다룹니다."
channel: in-app messages
toc_headers: h2
---

# 인앱 메시징 통합

> Xamarin 플랫폼용 iOS, Android 및 FireOS 인앱 메시지(IAM)를 설정하는 방법을 알아봅니다.

## 전제 조건

이 기능을 사용하려면 [Xamarin용 Braze SDK를 통합]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/initial_sdk_setup/)해야 합니다.

## 인앱 메시징 통합

{% tabs %}
{% tab android %}

{% alert tip %}
예제를 보려면 [GitHub의 샘플 Xamrin 앱](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp)을 확인하세요.
{% endalert %}

### 1단계: 인앱 메시지 등록 설정

앱의 모든 활동은 [`BrazeInAppMessageManager`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/index.html) 클래스에 등록해야 합니다. [활동 생애주기 콜백 통합]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android)을 사용하여 인앱 메시지를 자동으로 등록하려면 `Application` 클래스의 `onCreate()` 메서드에 다음 코드를 추가합니다.

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
사용 가능한 매개변수의 전체 목록은 [`BrazeActivityLifecycleCallbackListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-activity-lifecycle-callback-listener/index.html)를 참조하세요.
{% endalert %}

### 2단계: 차단 목록 관리자 설정(선택 사항)

특정 활동이 인앱 메시지에 표시되지 않도록 하려면 [활동 생애주기 콜백 통합]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android)을 사용합니다. 다음 샘플 코드에서는 인앱 메시지 등록 차단 목록에 두 가지 활동(`SplashActivity` 및 `SettingsActivity`)을 추가합니다.

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
예제를 보려면 [GitHub의 샘플 Xamrin 앱](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/ios-net-maui/BrazeiOSMauiSampleApp/BrazeiOSMauiSampleApp)을 확인하세요.
{% endalert %}

Braze의 기본 인앱 메시지 UI를 사용하려면 먼저 새 `BrazeInAppMessageUI`를 생성합니다.
```csharp
public static BrazeInAppMessageUI? inAppMessageUI = new BrazeInAppMessageUI();
```

그런 다음, Braze 인스턴스를 설정할 때 `BrazeInAppMessageUI`를 인앱 메시지 프레젠터로 등록합니다.
```csharp
braze.InAppMessagePresenter = inAppMessageUI;
```

이제 Braze의 기본 인앱 메시지 UI를 사용하여 새로운 인앱 메시지를 전달할 수 있습니다.
{% endtab %}
{% endtabs %}

## GIF 지원

{% multi_lang_include wrappers/gif_support/in_app_messaging.md %}
