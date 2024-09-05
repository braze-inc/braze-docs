---
nav_title: トラッキングセッション
article_title: Android と FireOS のトラッキングセッション
platform: 
  - Android
  - FireOS
page_order: 0
description: "このリファレンス記事では、Android または FireOS アプリケーションのセッション更新を購読する方法を説明します。"

---

# トラッキングセッション

> Braze SDK では、ユーザーエンゲージメントやユーザーの理解に不可欠なその他の分析を計算するため、Braze ダッシュボードで使用されるセッションデータがレポートされます。SDK では、以下のセッションセマンティクスに基づいて、Braze ダッシュボード内で表示可能なセッションの長さとセッション数を考慮した「セッション開始」と「セッション終了」のデータポイントが生成されます。このリファレンス記事では、Android または FireOS アプリケーションのセッション更新を購読する方法を説明します。

## セッションライフサイクル

推奨される\[アクティビティライフサイクルコールバック統合]\[セッション追跡_8]、`openSession()`および`closeSession()`を使用してBrazeを統合した場合、アプリ内の各アクティビティに対して自動的に呼び出されます。デフォルトでは、Android のセッションは`openSession()`への最初の呼び出し時に開かれ、アプリがフォアグラウンドから10秒以上離れると閉じられます。`closeSession()`を呼び出しても、すぐにセッションを閉じるわけではないことに注意してください。むしろ、ユーザーが途中で`openSession()`を呼び出さないと (別のアクティビティに移動するなど)、10秒でセッションを閉じます。

Android セッションは、ホストアプリケーションからの通信がない状態で10秒後にタイムアウトします。つまり、ユーザーがアプリをバックグラウンドにして9秒後に戻ってきた場合、同じセッションが継続されます。なお、ユーザーがアプリをバックグラウンドで起動している間にセッションが終了してしまうと、アプリを再度開くまでそのデータがサーバーにフラッシュされないことがあります。

{% alert note %}
新しいセッションを強制する必要がある場合、ユーザーを変更することで強制が可能になります。
{% endalert %}

## セッションタイムアウトのカスタマイズ
セッションタイムアウトをカスタマイズするには、`com_braze_session_timeout`を[`braze.xml`][セッション_tracking_3]ファイルに追加します。 の最小値は 1 秒です。

```xml
<!-- The length of time before a session times out in seconds. The session manager will "re-open" otherwise closed sessions if the call to StartSession comes within this interval. (default is 10) -->
<integer name="com_braze_session_timeout">NUMBER_OF_SECONDS_UNTIL_SESSION_TIMEOUT</integer>
```

## セッショントラッキングをテストする

ユーザーを介してセッションを検出するには、ダッシュボードでユーザーを見つけ、ユーザープロファイルの \[**アプリの利用状況**] に移動します。セッション指標が想定どおりに増加していることを確認することで、セッショントラッキングが機能していることを確認できます。

![ユーザープロファイルコンポーネントは、セッションが何回発生したか、アプリが最初に使用された時期、および最後に使用された時期を表示します。]\[session_tracking_7]

## セッション更新の購読

Braze SDK は、セッションの更新をリッスンする[`subscribeToSessionUpdates`][1]サブスクライバーを提供しています。

{% tabs %}
{% tab JAVA %}

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

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(this).subscribeToSessionUpdates { message ->
  if (message.eventType == SessionStateChangedEvent.ChangeType.SESSION_STARTED) {
    // A session has just been started
  }
}
```

{% endtab %}
{% endtabs %}

[1]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/subscribe-to-session-updates.html
\[session_tracking_3]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-2-configure-the-braze-sdk-in-brazexml
\[session_tracking_7]: {% image_buster /assets/img_archive/test_session.png %}
\[session_tracking_8]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android
