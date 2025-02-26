---
nav_title: セッショントラッキング
article_title: iOS のセッショントラッキング
platform: Swift
page_order: 0
search_rank: 1
description: "このリファレンス記事では、Swift SDK のセッション更新を購読する方法を説明します。"

---

# セッショントラッキング

> Braze SDK では、ユーザーエンゲージメントやユーザーの理解に不可欠なその他の分析を計算するため、Braze ダッシュボードで使用されるセッションデータがレポートされます。 

SDK では、以下のセッションセマンティクスに基づいて、Braze ダッシュボード内で表示可能なセッションの長さとセッション数を考慮した「セッション開始」と「セッション終了」のデータポイントが生成されます。

## セッションライフサイクル

`Braze.init(configuration:)` を呼び出すと、セッションが開始されます。デフォルトでは、`UIApplicationWillEnterForegroundNotification` 通知の発行時 (アプリがフォアグラウンドになった時点) にこの動作が発生します。セッション終了は、アプリがフォアグラウンドでなくなった時点 (`UIApplicationDidEnterBackgroundNotification` 通知の発行時やアプリの終了時など) に発生します。

{% alert note %}
新しいセッションを強制する必要がある場合、ユーザーを変更することで強制が可能になります。
{% endalert %}

## セッションタイムアウトのカスタマイズ

[`init(configuration)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class) に渡された `configuration` オブジェクトで、`sessionTimeout` を希望する整数値に設定できます。

{% tabs %}
{% tab SWIFT %}

```swift
// Sets the session timeout to 60 seconds
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)
configuration.sessionTimeout = 60;
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endtab %}
{% tab objective-c %}

```objc
// Sets the session timeout to 60 seconds
BRZConfiguration *configuration =
  [[BRZConfiguration alloc] initWithApiKey:brazeApiKey
                                  endpoint:brazeEndpoint];
configuration.sessionTimeout = 60;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endtab %}
{% endtabs %}

セッションタイムアウトを設定した場合、セッションセマンティクスの長さはすべてそのカスタマイズされたタイムアウトになります。

{% alert note %}
`sessionTimeout` の最小値は 1 秒です。デフォルト値は 10 秒です。
{% endalert %}

## セッショントラッキングをテストする

ユーザー経由でセッションを検出するには、ダッシュボードでユーザーを見つけ、ユーザープロファイルの「**セッションの概要**」に移動する。「セッション」指標が想定どおりに増加していることを確認することで、セッショントラッキングが機能していることを確認できます。アプリ固有の詳細は、ユーザーが複数のアプリを使用した後に表示されます。

![セッション数、最終使用日、初回使用日が表示されるユーザープロファイルのセッション概要セクション。]({% image_buster /assets/img_archive/test_session.png %}){: style="max-width:40%;"}

アプリ別の詳細は、ユーザーが複数のアプリを使用した場合にのみ表示されます。

## セッション更新の購読

セッションの更新をリッスンするには、[`subscribeToSessionUpdates(_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/subscribetosessionupdates(_:)) メソッドを使用します。セッション開始と終了のイベントは、アプリがフォアグラウンドで実行されているときのみ記録される。セッション終了イベントにコールバックを登録し、アプリがバックグラウンドになった場合、アプリが再びフォアグラウンドになったときにコールバックが起動する。ただし、セッションの継続時間は、アプリを開くかフォアグラウンドにしてから、アプリを閉じるかバックグラウンドにするまでの時間として測定されます。

{% tabs %}
{% tab SWIFT %}
```swift
// This subscription is maintained through a Braze cancellable, which will observe changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
let cancellable = AppDelegate.braze?.subscribeToSessionUpdates { event in
  switch event {
  case .started(let id):
    print("Session \(id) has started")
  case .ended(let id):
    print("Session \(id) has ended")
  }
}
```
{% endtab %}

{% tab objective-c %}
```objc
// This subscription is maintained through a Braze cancellable, which will observe changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
BRZCancellable *cancellable = [AppDelegate.braze subscribeToSessionUpdates:^(BRZSessionEvent * _Nonnull event) {
  switch (event.state) {
    case BRZSessionStateStarted:
      NSLog(@"Session %@ has started", event.sessionId);
      break;
    case BRZSessionStateEnded:
      NSLog(@"Session %@ has ended", event.sessionId);
      break;
    default:
      break;
  }
}];
```
{% endtab %}
{% endtabs %}

また、Swift では [`sessionUpdatesStream`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/sessionupdatesstream)`AsyncStream` を使用して非同期変更を監視できます。

```swift
for await event in braze.sessionUpdatesStream {
  switch event {
  case .started(let id):
    print("Session \(id) has started")
  case .ended(let id):
    print("Session \(id) has ended")
  }
}
```

