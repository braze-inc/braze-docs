---
nav_title: トラックセッション
article_title: Braze SDKを通じてセッションのトラッキングを行う
page_order: 3.3
description: "Braze SDK を使用してセッションを追跡する方法について説明します。"

---

# トラックセッション

> Braze SDK を使用してセッションを追跡する方法について説明します。

{% alert note %}
リストされていないラッパーSDK の場合は、代わりに関連するネイティブAndroid またはSwift メソッドを使用します。
{% endalert %}

{% multi_lang_include developer_guide/_shared/about_session_lifecycle.md %}

## 非活動状態の定義

Web SDKでセッションライフサイクルを効果的に管理するには、非アクティブ状態の定義と測定方法を理解することが重要だ。非アクティブ状態とは、Braze Web SDKがユーザーからのトラッキングイベントを一切検出しない期間を指す。

### 不活動がどのように測定されるか

Web SDKは[、SDKがトラッキングするイベント]({{site.baseurl}}/user_guide/data/activation/custom_data/events/#events)に基づいて非アクティブ状態を追跡する。SDKは内部タイマーを維持しており、トラッキング対象のイベントが送信されるたびにリセットされる。設定されたタイムアウト期間内にSDKがトラッキングするイベントが発生しない場合、セッションは非アクティブと見なされ終了する。

Web SDKにおけるセッションライフサイクルの実装方法の詳細については、[Braze Web SDK GitHubリポジトリ](https://github.com/braze-inc/braze-web-sdk/blob/master/src/session.ts)内のセッション管理コードを参照のこと。

**デフォルトで活動と見なされるもの：**
- ウェブアプリを開封するか更新する
- Brazeによって駆動されるUI要素（[アプリ内メッセージ]({{site.baseurl}}/developer_guide/in_app_messages/)や[コンテンツカード]({{site.baseurl}}/developer_guide/content_cards/)など）とのやり取り
- 追跡イベント（[カスタムイベント]({{site.baseurl}}/developer_guide/analytics/logging_events/)や[ユーザー属性の更新]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/)など）を送信するSDKメソッドを呼び出す

**デフォルトでは活動としてカウントされないもの：**
- 別のブラウザタブに切り替える
- ブラウザのウィンドウを最小化する
- ブラウザのフォーカスまたはブラーイベント
- ページ上のスクロールやマウスの動き

{% alert note %}
Web SDKは、ブラウザの表示状態の変化、タブの切り替え、またはユーザーのフォーカスを自動的にトラッキングしない。ただし、ブラウザの[Page Visibility API](https://developer.mozilla.org/en-US/docs/Web/API/Page_Visibility_API)を使用してカスタムイベントリスナーを実装し、[カスタムイベントを]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=web)Brazeに送信することで、これらのブラウザレベルのインタラクションをトラッキングできる。実装例については、[カスタム非アクティブ状態のトラッキング](#tracking-custom-inactivity)を参照せよ。
{% endalert %}

### セッションタイムアウトの設定

デフォルトでは、Web SDKは30分間トラッキングイベントが発生しない場合、セッションを非アクティブと見なす。SDKを初期化する際に、この`sessionTimeoutInSeconds`しきい値をパラメータでカスタマイズできる。このパラメータの設定方法の詳細（コード例を含む）については、[「デフォルトのセッションタイムアウトの変更](#changing-the-default-session-timeout)」を参照せよ。

### 例: 非アクティブ状態のシナリオを理解する

次のシナリオを考えてください:

1. ユーザーがあなたのWeb サイトを開くと、SDKはセッションを開始するために呼び出す[`braze.openSession()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#opensession)。
2. ユーザーは別のブラウザタブに切り替えて、30分間別のWeb サイトを閲覧する。
3. この間、Web サイトではSDKがトラッキングするイベントは発生しない。
4. 30分間操作がないと、セッションは自動的に終了する。
5. ユーザーがあなたのWeb サイトのタブに切り替え、SDKイベント（ページ閲覧やコンテンツ操作など）をトリガーすると、新しいセッションが開始される。

### 顧客非アクティブ状態のトラッキング

ブラウザの可視性やタブの切り替えに基づいて非アクティブ状態をトラッキングする必要がある場合、JavaScriptコードにカスタムイベントリスナーを実装せよ。ブラウザのイベント（例：）を使って`visibilitychange`ユーザーがページを離れたタイミングを検知し、必要に応じて[カスタムイベント]({{site.baseurl}}/developer_guide/analytics/logging_events/)を手動で[`braze.openSession()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#opensession)Brazeに送信するか、を呼び出す。

```javascript
// Example: Track when user switches away from tab
document.addEventListener('visibilitychange', function() {
  if (document.hidden) {
    // User switched away - optionally log a custom event
    braze.logCustomEvent('tab_hidden');
  } else {
    // User returned - optionally start a new session and/or log an event
    // braze.openSession();
    braze.logCustomEvent('tab_visible');
  }
});
```

カスタムイベントの記録に関する詳細情報は、[カスタムイベントの記録]({{site.baseurl}}/developer_guide/analytics/logging_events/)を参照せよ。セッションのライフサイクルとタイムアウト設定の詳細については、[「デフォルトのセッションタイムアウトの変更」](#change-session-timeout)を参照せよ。

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

{% tab react native %}
React Native SDKは、セッションの更新を直接購読するためのメソッドを公開していない。セッションのライフサイクルは基盤となるネイティブSDKによって管理される。更新を購読するには、**Android**または**SWIFT**タブのネイティブプラットフォーム向けアプローチを使用する。
{% endtab %}
{% endtabs %}

### ステップ2:セッショントラッキング (オプション) をテストする

セッショントラッキングをテストするには、デバイスでセッションを開始し、Braze ダッシュボードを開き、関連するユーザーを検索します。ユーザープロファイルで、[**セッションの概要**] を選択します。メトリクスが期待どおりに更新された場合、セッション追跡は正常に動作しています。

![ユーザープロファイルのセッション概要セクションには、セッション数、最終利用日、初回利用日が表示される。]({% image_buster /assets/img_archive/test_session.png %}){: style="max-width:50%;"}

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

{% tab react native %}
React Native SDKはセッション管理のためにネイティブSDKに依存している。デフォルトのセッションタイムアウトを変更するには、ネイティブレイヤーで設定する。

- **Android :**ファイル`braze.xml`に`com_braze_session_timeout`設定せよ。詳細は、**Android**タブを選択せよ。
- **iOS:**オブジェクト`Braze.Configuration`に`sessionTimeout`設定せよ。詳細については、**SWIFT**タブを選択せよ。
{% endtab %}
{% endtabs %}

{% alert note %}
セッションタイムアウトを設定すると、すべてのセッションセマンティクスが設定されたタイムアウトに自動的に拡張されます。
{% endalert %}
