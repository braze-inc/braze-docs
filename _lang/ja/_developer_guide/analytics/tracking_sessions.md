---
nav_title: トラックセッション
article_title: Braze SDKを通じてセッションのトラッキングを行う
page_order: 3.3
description: "Braze SDK を使用してセッションを追跡する方法について説明します。"

---

# トラックセッション

> Braze SDK を使用してセッションを追跡する方法について説明します。

{% alert note %}
リストされていないラッパー SDK の場合は、代わりに関連するネイティブ Android または Swift メソッドを使用してください。
{% endalert %}

{% multi_lang_include developer_guide/_shared/about_session_lifecycle.md %}

## 非アクティブ状態の定義

Web SDK でセッションライフサイクルを効果的に管理するには、非アクティブ状態の定義と測定方法を理解することが重要です。非アクティブ状態とは、Braze Web SDK がユーザーからのトラッキングイベントを一切検出しない期間を指します。

### 非アクティブ状態の測定方法

Web SDK は [SDK がトラッキングするイベント]({{site.baseurl}}/user_guide/data/activation/custom_data/events/#events)に基づいて非アクティブ状態を追跡します。SDK は内部タイマーを維持しており、トラッキング対象のイベントが送信されるたびにリセットされます。設定されたタイムアウト期間内に SDK がトラッキングするイベントが発生しない場合、セッションは非アクティブと見なされ終了します。

Web SDK におけるセッションライフサイクルの実装方法の詳細については、[Braze Web SDK GitHub リポジトリ](https://github.com/braze-inc/braze-web-sdk/blob/master/src/session.ts)内のセッション管理ソースコードを参照してください。

**デフォルトでアクティビティと見なされるもの：**
- Web アプリを開くか更新する
- Braze が提供する UI 要素（[アプリ内メッセージ]({{site.baseurl}}/developer_guide/in_app_messages/)や[コンテンツカード]({{site.baseurl}}/developer_guide/content_cards/)など）とのインタラクション
- トラッキングイベント（[カスタムイベント]({{site.baseurl}}/developer_guide/analytics/logging_events/)や[ユーザー属性の更新]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/)など）を送信する SDK メソッドの呼び出し

**デフォルトではアクティビティとしてカウントされないもの：**
- 別のブラウザタブへの切り替え
- ブラウザウィンドウの最小化
- ブラウザのフォーカスまたはブラーイベント
- ページ上のスクロールやマウスの動き

{% alert note %}
Web SDK は、ブラウザの表示状態の変化、タブの切り替え、またはユーザーのフォーカスを自動的にトラッキングしません。ただし、ブラウザの [Page Visibility API](https://developer.mozilla.org/en-US/docs/Web/API/Page_Visibility_API) を使用してカスタムイベントリスナーを実装し、[カスタムイベント]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=web)を Braze に送信することで、これらのブラウザレベルのインタラクションをトラッキングできます。実装例については、[カスタム非アクティブ状態のトラッキング](#tracking-custom-inactivity)を参照してください。
{% endalert %}

### セッションタイムアウトの設定

デフォルトでは、Web SDK は30分間トラッキングイベントが発生しない場合、セッションを非アクティブと見なします。SDK を初期化する際に、`sessionTimeoutInSeconds` パラメータを使用してこのしきい値をカスタマイズできます。このパラメータの設定方法の詳細（コード例を含む）については、[デフォルトのセッションタイムアウトの変更](#changing-the-default-session-timeout)を参照してください。

### 例：非アクティブ状態のシナリオを理解する

次のシナリオを考えてみましょう：

1. ユーザーが Web サイトを開くと、SDK は [`braze.openSession()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#opensession) を呼び出してセッションを開始します。
2. ユーザーは別のブラウザタブに切り替えて、30分間別の Web サイトを閲覧します。
3. この間、Web サイトでは SDK がトラッキングするイベントは発生しません。
4. 30分間操作がないと、セッションは自動的に終了します。
5. ユーザーが Web サイトのタブに戻り、SDK イベント（ページ閲覧やコンテンツ操作など）をトリガーすると、新しいセッションが開始されます。

### カスタム非アクティブ状態のトラッキング

ブラウザの可視性やタブの切り替えに基づいて非アクティブ状態をトラッキングする必要がある場合は、JavaScript コードにカスタムイベントリスナーを実装してください。`visibilitychange` などのブラウザイベントを使用してユーザーがページを離れたタイミングを検知し、必要に応じて[カスタムイベント]({{site.baseurl}}/developer_guide/analytics/logging_events/)を手動で Braze に送信するか、[`braze.openSession()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#opensession) を呼び出してください。

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

カスタムイベントの記録に関する詳細は、[カスタムイベントの記録]({{site.baseurl}}/developer_guide/analytics/logging_events/)を参照してください。セッションのライフサイクルとタイムアウト設定の詳細については、[デフォルトのセッションタイムアウトの変更](#change-session-timeout)を参照してください。

## セッション更新のサブスクライブ

### ステップ 1:更新をサブスクライブする

セッション更新をサブスクライブするには、`subscribeToSessionUpdates()` メソッドを使用します。

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
セッション終了コールバックを登録すると、アプリがフォアグラウンドに戻ったときに発火します。セッション時間は、アプリが開かれたときまたはフォアグラウンドになったときから、閉じられたときまたはバックグラウンドになったときまで測定されます。

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

非同期ストリームをサブスクライブするには、代わりに [`sessionUpdatesStream`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/sessionupdatesstream) を使用できます。

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
React Native SDK は、セッション更新を直接サブスクライブするためのメソッドを公開していません。セッションのライフサイクルは基盤となるネイティブ SDK によって管理されます。更新をサブスクライブするには、**Android** または **Swift** タブのネイティブプラットフォーム向けアプローチを使用してください。
{% endtab %}
{% endtabs %}

### ステップ 2:セッショントラッキングをテストする（オプション）

セッショントラッキングをテストするには、デバイスでセッションを開始し、Braze ダッシュボードを開いて関連するユーザーを検索します。ユーザープロファイルで、[**セッションの概要**] を選択します。指標が期待どおりに更新された場合、セッショントラッキングは正常に動作しています。

![ユーザープロファイルのセッション概要セクションには、セッション数、最終利用日、初回利用日が表示されます。]({% image_buster /assets/img_archive/test_session.png %}){: style="max-width:50%;"}

{% alert note %}
アプリ固有の詳細は、複数のアプリを使用したユーザーにのみ表示されます。
{% endalert %}

## デフォルトのセッションタイムアウトの変更 {#change-session-timeout}

セッションが自動的にタイムアウトするまでの時間を変更できます。

{% tabs %}
{% tab web %}
デフォルトでは、セッションタイムアウトは `30` 分に設定されています。これを変更するには、`sessionTimeoutInSeconds` オプションを [`initialize`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize) 関数に渡します。`1` 以上の任意の整数に設定できます。 

```js
// Sets the session timeout to 15 minutes instead of the default 30
braze.initialize('YOUR-API-KEY-HERE', { sessionTimeoutInSeconds: 900 });
```
{% endtab %}

{% tab android %}
デフォルトでは、セッションタイムアウトは `10` 秒に設定されています。これを変更するには、`braze.xml` ファイルを開き、`com_braze_session_timeout` パラメータを追加します。`1` 以上の任意の整数に設定できます。

```xml
<!-- Sets the session timeout to 60 seconds. -->
<integer name="com_braze_session_timeout">60</integer>
```
{% endtab %}

{% tab swift %}
デフォルトでは、セッションタイムアウトは `10` 秒に設定されています。これを変更するには、[`init(configuration)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class) に渡される `configuration` オブジェクトで `sessionTimeout` を設定します。`1` 以上の任意の整数に設定できます。

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
React Native SDK はセッション管理のためにネイティブ SDK に依存しています。デフォルトのセッションタイムアウトを変更するには、ネイティブレイヤーで設定してください。

- **Android：**`braze.xml` ファイルで `com_braze_session_timeout` を設定します。詳細は、**Android** タブを選択してください。
- **iOS：**`Braze.Configuration` オブジェクトで `sessionTimeout` を設定します。詳細は、**Swift** タブを選択してください。
{% endtab %}
{% endtabs %}

{% alert note %}
セッションタイムアウトを設定すると、すべてのセッションセマンティクスが設定されたタイムアウトに自動的に拡張されます。
{% endalert %}

## トラブルシューティング

### ユーザープロファイルのセッション数が0件

SDK の外部でユーザーが作成された場合、ユーザープロファイルのセッション数が0件になることがあります。

- **REST API で作成された場合：**[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) エンドポイントを通じてリクエストに `app_id` を含めてユーザーが作成された場合、プロファイルはそのアプリに関連付けられて表示されますが、そのユーザーに対して SDK が初期化されていないため、セッションデータはありません。
- **CSV インポートで作成された場合：**初回セッションまたは最終セッションのフィールドに値を含めずに [CSV]({{site.baseurl}}/user_guide/data/unification/user_data/import_users/csv/) でユーザーがインポートされた場合、プロファイルはセッション数0件で存在します。