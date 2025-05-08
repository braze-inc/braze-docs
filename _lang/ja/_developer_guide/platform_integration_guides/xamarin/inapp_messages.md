---
nav_title: アプリ内メッセージング
article_title: Xamarinのアプリ内メッセージング
platform: 
  - Xamarin
  - iOS
  - Android
page_order: 2
description: "この記事では、Xamarin プラットフォームの iOS、Android、および FireOS のアプリ内メッセージングについて説明します。"
channel: in-app messages
toc_headers: h2
---

# アプリ内メッセージング統合

> Xamarin プラットフォームの iOS、Android、および FireOS アプリ内メッセージ (IAM) を設定する方法について説明します。

## 前提条件

この機能を使用するには、[Xamarin 用のBraze SDK を統合する]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/initial_sdk_setup/)必要があります。

## アプリ内メッセージングの統合

{% tabs %}
{% tab Android %}

{% alert tip %}
例を確認するには、[GitHub でサンプルの Xamrin アプリ](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp)を確認してください。
{% endalert %}

### ステップ 1:アプリ内メッセージレジストレーションの設定

アプリ内のすべてのアクティビティーは、[`BrazeInAppMessageManager`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/index.html) クラスに登録する必要があります。[アクティビティライフサイクルコールバック統合]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android)を使用してアプリ内メッセージを自動的に登録するには、`Application` クラスの `onCreate()` メソッドに次のコードを追加します。

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
使用可能なパラメータ＝の完全なリストについては、[`BrazeActivityLifecycleCallbackListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-activity-lifecycle-callback-listener/index.html) を参照してください。
{% endalert %}

### ステップ2:ブロック一覧マネージャーの設定(オプション)

特定のアクティビティがアプリ内メッセージs を表示しないようにするには、[アクティビティライフサイクルコールバック統合]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android) を使用します。次のコード例では、アプリ内メッセージ レジストレーションブロックリストに`SplashActivity` と`SettingsActivity` の2 つのアクティビティを追加しています。

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
例を確認するには、[GitHub でサンプルの Xamrin アプリ](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/ios-net-maui/BrazeiOSMauiSampleApp/BrazeiOSMauiSampleApp)を確認してください。
{% endalert %}

Braze のデフォルト アプリ内メッセージユーザーインターフェイスを使用するには、最初に新しい`BrazeInAppMessageUI` を作成します。
```csharp
public static BrazeInAppMessageUI? inAppMessageUI = new BrazeInAppMessageUI();
```

次に、Brazeインスタンスを設定するときに、`BrazeInAppMessageUI` をアプリ内メッセージプレゼンタとして登録します。
```csharp
braze.InAppMessagePresenter = inAppMessageUI;
```

これで、Braze のデフォルト アプリ内メッセージユーザーインターフェイスを使用して新しいアプリ内メッセージを表示できます。
{% endtab %}
{% endtabs %}

## GIFサポート

{% multi_lang_include wrappers/gif_support/in_app_messaging.md %}
