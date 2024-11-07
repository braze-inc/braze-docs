---
nav_title: 初期化の遅れ
article_title: Braze Swift SDKの初期化の遅延
platform: Swift
page_order: 6
description: "この記事では、SDKが非同期に初期化されたときにプッシュ通知の処理を維持するために、Swift SDKの遅延初期化を実装する方法を説明する。"

---

# Braze Swift SDKの初期化の遅延

> Braze Swift SDKを非同期で初期化し、プッシュ通知の処理を確実に維持する方法を学習する。これは、SDKを初期化する前に、サーバーから設定データを取得したり、ユーザーの同意を待ったりするなど、他のサービスを設定する必要がある場合に便利である。

## 遅延初期化の設定

### ステップ1:SDKの遅延初期化の準備

デフォルトでは、アプリが終了状態にある間にエンドユーザーがプッシュ通知を開封した場合、SDKが初期化される前にプッシュ通知を処理することはできない。

[Braze Swift SDKバージョン10.1.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/10.1.0)以降では、静的ヘルパーメソッド[Braze.prepareForDelayedInitialization(pushAutomation:)](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/preparefordelayedinitialization(pushautomation:))を使用してこれを処理できる。このメソッドは、プッシュオートメーションシステムを設定することによって、SDKを遅延初期化のために準備する。

SDKが初期化される前に、Brazeから発信されるすべてのプッシュ通知がキャプチャされ、キューに入れられる。SDKが初期化された後、これらのプッシュ通知はSDKによって処理される。このメソッドは、アプリケーションのライフサイクルのなるべく早い段階で、`AppDelegate` の`application(_:didFinishLaunchingWithOptions:)` メソッド内かその前に呼ばれなければならない。

{% alert note %}
Swift SDKは、Braze以外のプッシュ通知を捕捉しない-これらは、システムのデリゲートメソッドによって処理され続ける。
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
[Braze.prepareForDelayedInitialization(pushAutomation:)は](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/preparefordelayedinitialization(pushautomation:))、プッシュ通知のオートメーション設定を表すオプションの`pushAutomation` パラメータを受け取る。の場合 [Braze.Configuration.Push.Automation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/automation-swift.class)が`nil` の場合、起動時に認証を要求する以外は、すべてのオートメーション機能がイネーブルメントになる。
{% endalert %}

### ステップ 2:Braze SDKの初期化

SDKを遅延初期化のために準備した後、将来いつでもSDKを非同期で初期化できる。その後、SDKはBrazeから発信されるキューに入ったすべてのプッシュ通知イベントを処理する。

Braze SDKを初期化するには、[標準的なSwift SDK初期化プロセスに]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/)従う。

## 考慮事項

`Braze.prepareForDelayedInitialization(pushAutomation:)` を使用することで、プッシュ通知のオートメーション機能を自動的に使用するようにSDKを設定することになる。プッシュ通知を処理するシステムデリゲートメソッドは、Brazeから発信されたプッシュ通知に対しては呼び出されない。

SDKは、SDKが初期化された**後にのみ**、Brazeプッシュ通知とその結果のアクションを処理する。例えば、ユーザーがディープリンクを開封するプッシュ通知をタップした場合、ディープリンクは`Braze` インスタンスが初期化された後にのみ開封される。

Brazeプッシュ通知に追加処理を行う必要がある場合は、[プッシュ通知更新のサブスクライバーを]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#subscribing-to-push-notifications-updates)参照。以前にエンキューされたプッシュ通知の更新を受信するには、SDKを初期化した後、サブスクリプションハンドラを直接実装する必要があることに留意されたい。
