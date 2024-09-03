---
nav_title: セッションを追跡する
article_title: ウェブのセッションをトラッキングする
platform: Web
page_order: 0
description: "このリファレンスでは、ウェブのセッションを追跡する方法について説明する。"

---

# セッションを追跡する

> Braze SDK では、ユーザーエンゲージメントやユーザーの理解に不可欠なその他の分析を計算するため、Braze ダッシュボードで使用されるセッションデータがレポートされます。SDK では、以下のセッションセマンティクスに基づいて、Braze ダッシュボード内で表示可能なセッションの長さとセッション数を考慮した「セッション開始」と「セッション終了」のデータポイントが生成されます。

## セッションライフサイクル

デフォルトでは、セッションは`braze.openSession()` が最初にコールされたときに開始され、少なくとも30分間操作がない限りオープンされたままになる。これは、ユーザーがサイトを離れて30分以内に戻ってきた場合、同じセッションが継続されることを意味する。30分が経過した後に彼らが戻ってきた場合、「セッションを閉じる」データポイントが、彼らが離れて移動した時間のために自動的に生成され、新しいセッションが開かれる。

{% alert note %}
新しいセッションを強制する必要がある場合、ユーザーを変更することで強制が可能になります。
{% endalert %}

## セッションタイムアウトをカスタマイズする

セッションのタイムアウトをカスタマイズするには、`initialize`]\[session_tracking_5] ] 関数に`sessionTimeoutInSeconds` オプションを渡す。`sessionTimeoutInSeconds` の最小値は 1 秒です。

```js
// Sets the session timeout to 15 minutes instead of the default 30
braze.initialize('YOUR-API-KEY-HERE', { sessionTimeoutInSeconds: 900 });
``` 

セッションタイムアウトを設定した場合、セッションセマンティクスの長さはすべてそのカスタマイズされたタイムアウトになります。

## セッショントラッキングをテストする

ユーザーを介してセッションを検出するには、ダッシュボードでユーザーを見つけ、ユーザープロファイルの \[**アプリの利用状況**] に移動します。セッション指標が想定どおりに増加していることを確認することで、セッショントラッキングが機能していることを確認できます。

![] 【session_tracking_7】セッション数、アプリが最初に使われた時間、最後に使われた時間を示すユーザー・プロフィール・コンポーネント。]{: style="max-width:50%"}

\[session_tracking_1] ： {{ site.baseurl }}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overview/#customizing-braze-on-startup
\[session_tracking_3] ： {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-2-configure-the-braze-sdk-in-appboyxml
\[session_tracking_5] ： https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize
\[session_tracking_6] ： http://msdn.microsoft.com/en-us/library/windows/apps/hh464925.aspx
\[session_tracking_7] ： {% image_buster /assets/img_archive/test_session.png %}
\[session_tracking_8] ： {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android
