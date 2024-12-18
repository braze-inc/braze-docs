---
nav_title: 遅延初期化
article_title: Braze Swift SDKの初期化の遅延
platform: Swift
page_order: 6
description: "この記事では、SDK が非同期的に初期化されるときにプッシュ通知の処理を保持するために、Swift SDK の遅延初期化を実装する方法について説明します。"

---

# Braze Swift SDKの初期化の遅延

> プッシュ通知の処理が確実に保持されるようにしながら、Braze Swift SDK を非同期的に初期化する方法を学びます。これは、サーバーから構成データを取得したり、ユーザーの同意を待ったりするなど、SDK を初期化する前に他のサービスを設定する必要がある場合に役立ちます。

## 遅延初期化の設定

### ステップ1:SDKの遅延初期化の準備

デフォルトでは、アプリが終了状態にあるときにエンドユーザーがプッシュ通知を開いた場合、SDK が初期化されるまでプッシュ通知を処理できません。

[Braze Swift SDK バージョン 10.1.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/10.1.0) 以降では、静的ヘルパーメソッド [Braze.prepareForDelayedInitialization(pushAutomation:)](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/preparefordelayedinitialization(pushautomation:)) を使用してこれを処理できます。このメソッドは、プッシュオートメーションシステムを設定することで、遅延初期化用に SDK を準備します。

SDKが初期化される前に、Brazeから発信されるすべてのプッシュ通知がキャプチャされ、キューに入れられる。SDK が初期化されると、それらのプッシュ通知は SDK によって処理されます。このメソッドは、アプリケーションのライフサイクルのできるだけ早い段階で、`AppDelegate` の `application(_:didFinishLaunchingWithOptions:)` メソッド内またはその前に呼び出す必要があります。

{% alert note %}
Swift SDK は Braze 以外のプッシュ通知をキャプチャしません。そのような通知は引き続きシステムデリゲートメソッドによって処理されます。
{% endalert %}

{% tabs %}
{% tab Swift - UIKit %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
  // Prepare the SDK for delayed initialization
  Braze.prepareForDelayedInitialization()

  // ... Additional non-Braze setup code

  return true
}
```
{% endtab %}

{% tab Swift - SWIFTUI %}
SwiftUI アプリケーションは`prepareForDelayedInitialization()` メソッドを呼び出すために[@UIApplicationDelegateAdaptor](https://developer.apple.com/documentation/swiftui/uiapplicationdelegateadaptor)プロパティラッパーを実装する必要がある。

```swift
@main
struct MyApp: App {
  @UIApplicationDelegateAdaptor var appDelegate: AppDelegate

  var body: some Scene {
    WindowGroup {
      ContentView()
    }
  }
}

class AppDelegate: NSObject, UIApplicationDelegate {
  
  func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil) -> Bool {
    // Prepare the SDK for delayed initialization
    Braze.prepareForDelayedInitialization()

    // ... Additional non-Braze setup code

    return true
  }
  
}
```
{% endtab %}

{% tab Objective-C %}
```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Prepare the SDK for delayed initialization
  [Braze prepareForDelayedInitialization];
  
  // ... Additional non-Braze setup code

  return YES;
}

```
{% endtab %}
{% endtabs %}

{% alert note %}
[Braze.prepareForDelayedInitialization(pushAutomation:)](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/preparefordelayedinitialization(pushautomation:)) は、プッシュ通知のオートメーション設定を表すオプションの `pushAutomation` パラメータを取ります。[Braze.Configuration.Push.Automation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.class) が `nil` の場合、起動時に承認を要求することを除き、すべてのオートメーション機能が有効になります。
{% endalert %}

### ステップ 2:Braze SDKの初期化

遅延初期化用に SDK を準備したら、将来いつでも SDK を非同期的に初期化できます。次に、SDK は Braze から発信されキューに入れられたすべてのプッシュ通知イベントを処理します。

Braze SDK を初期化するには、[標準の Swift SDK 初期化プロセス]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/)に従います。

## 考慮事項

`Braze.prepareForDelayedInitialization(pushAutomation:)` を使用すると、プッシュ通知のオートメーション機能を自動的に使用するように SDK が構成されます。プッシュ通知を処理するシステムデリゲートメソッドは、Brazeから発信されたプッシュ通知に対しては呼び出されない。

SDK は、SDK が初期化された**後**にのみ、Braze プッシュ通知とその結果のアクションを処理します。例えば、ユーザーがディープリンクを開くプッシュ通知をタップした場合、ディープリンクは `Braze` インスタンスが初期化された後にのみ開きます。

Braze プッシュ通知で追加の処理を実行する必要がある場合は、[[プッシュ通知更新を購読する]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#subscribing-to-push-notifications-updates)] を参照してください。以前にキューに登録されたプッシュ通知の更新を受信するには、SDK を初期化した後、サブスクリプションハンドラを直接実装する必要があることに留意してください。
