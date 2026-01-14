---
nav_title: セッションを追跡する
article_title: Braze SDK を使用したセッションの追跡
page_order: 3.3
description: "Braze SDK を使用してセッションを追跡する方法について説明します。"

---

# セッションを追跡する

> Braze SDK を使用してセッションを追跡する方法について説明します。

{% alert note %}
リストされていないラッパーSDK の場合は、代わりに関連するネイティブAndroid またはSwift メソッドを使用します。
{% endalert %}

{% multi_lang_include developer_guide/_shared/about_session_lifecycle.md %}

## セッション更新の購読

### ステップ1:更新を購読する

セッション更新にサブスクライブするには、`subscribeToSessionUpdates()` メソッドを使用します。

{% tabs %}
{% tab web %}
現時点では、Web Braze SDK のセッション更新のサブスクライブはサポートされていません。
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab java %}

```java
Braze.getInstance(this).subscribeToSessionUpdates(new IEventSubscriber<SessionStateChangedEvent>() {
  @Override
  public void trigger(SessionStateChangedEvent message) {
    if (message.getEventType() == SessionStateChangedEvent.ChangeType.SESSION_STARTED) {
      // A session has just been started
    }
  }
});
```

{% endsubtab %}
{% subtab kotlin %}

```kotlin
Braze.getInstance(this).subscribeToSessionUpdates { message ->
  if (message.eventType == SessionStateChangedEvent.ChangeType.SESSION_STARTED) {
    // A session has just been started
  }
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
セッション終了コールバックを登録すると、アプリがフォアグラウンドに戻ったときに起動します。セッション時間は、アプリが開いたときまたはフォアグラウンドになったときから、アプリが閉じたときまたはバックグラウンドになったときまで測定されます。

{% subtabs %}
{% subtab swift %}
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

非同期ストリームにサブスクライブするには、代わりに[`sessionUpdatesStream`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/sessionupdatesstream) を使用できます。

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
{% endsubtab %}

{% subtab objective-c %}
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
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### ステップ2:セッショントラッキング (オプション) をテストする

セッショントラッキングをテストするには、デバイスでセッションを開始し、Braze ダッシュボードを開き、関連するユーザーを検索します。ユーザープロファイルで、[**セッションの概要**] を選択します。メトリクスが期待どおりに更新された場合、セッション追跡は正常に動作しています。

![セッションは、セッションの数s、最後に使用された日付、および最初に使用された日付を示すユーザープロファイルの概観を示します。]({% image_buster /assets/img_archive/test_session.png %}){: style="max-width:50%;"}

{% alert note %}
アプリ固有の詳細は、複数のアプリを使用したユーザーにのみ表示されます。
{% endalert %}

## デフォルトのセッションタイムアウトの変更 {#change-session-timeout}

セッションが自動的にタイムアウトするまでの時間を変更できます。

{% tabs %}
{% tab web %}
デフォルトでは、セッションタイムアウトは`30` 分に設定されます。これを変更するには、`sessionTimeoutInSeconds` オプションを[`initialize`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize) 関数に渡します。`1` 以上の任意の整数に設定できます。 

```js
// Sets the session timeout to 15 minutes instead of the default 30
braze.initialize('YOUR-API-KEY-HERE', { sessionTimeoutInSeconds: 900 });
```
{% endtab %}

{% tab android %}
デフォルトでは、セッションタイムアウトは`10`秒に設定されます。これを変更するには、`braze.xml` ファイルを開き、`com_braze_session_timeout` パラメータを追加します。`1` 以上の任意の整数に設定できます。

```xml
<!-- Sets the session timeout to 60 seconds. -->
<integer name="com_braze_session_timeout">60</integer>
```
{% endtab %}

{% tab swift %}
デフォルトでは、セッションタイムアウトは`10`秒に設定されます。これを変更するには、`configuration` オブジェクトで[`init(configuration)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class) に渡される`sessionTimeout` を設定します。`1` 以上の任意の整数に設定できます。

{% subtabs %}
{% subtab swift %}
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
{% endsubtab %}
{% subtab objective-c %}

```objc
// Sets the session timeout to 60 seconds
BRZConfiguration *configuration =
  [[BRZConfiguration alloc] initWithApiKey:brazeApiKey
                                  endpoint:brazeEndpoint];
configuration.sessionTimeout = 60;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert note %}
セッションタイムアウトを設定すると、すべてのセッションセマンティクスが設定されたタイムアウトに自動的に拡張されます。
{% endalert %}
