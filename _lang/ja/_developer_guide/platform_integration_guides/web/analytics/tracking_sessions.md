---
nav_title: セッションを追跡する
article_title: Web のセッションの追跡
platform: Web
page_order: 0
description: "このリファレンス記事では、Web のセッションを追跡する方法について説明します。"

---

# セッションを追跡する

> Braze SDK では、ユーザーエンゲージメントやユーザーの理解に不可欠なその他の分析を計算するため、Braze ダッシュボードで使用されるセッションデータがレポートされます。SDK では、以下のセッションセマンティクスに基づいて、Braze ダッシュボード内で表示可能なセッションの長さとセッション数を考慮した「セッション開始」と「セッション終了」のデータポイントが生成されます。

## セッションライフサイクル

デフォルトでは、セッションは最初に呼び出されたときに `braze.openSession()` 開始され、少なくとも 30 分間非アクティブになるまで開いたままになります。つまり、ユーザーがサイトから移動し、30 分以内に戻ってきた場合、同じセッションが続行されます。30 分が経過した後にユーザーが戻ると、移動した時間に対して「セッションを閉じる」データポイントが自動的に生成され、新しいセッションが開きます。

{% alert note %}
新しいセッションを強制する必要がある場合、ユーザーを変更することで強制が可能になります。
{% endalert %}

## セッションタイムアウトをカスタマイズする

セッションタイムアウトをカスタマイズするには、このオプションを `sessionTimeoutInSeconds` ['initialize'][session_tracking_5] 関数に渡します。`sessionTimeoutInSeconds` の最小値は 1 秒です。

```js
// Sets the session timeout to 15 minutes instead of the default 30
braze.initialize('YOUR-API-KEY-HERE', { sessionTimeoutInSeconds: 900 });
``` 

セッションタイムアウトを設定した場合、セッションセマンティクスの長さはすべてそのカスタマイズされたタイムアウトになります。

## セッショントラッキングをテストする

ユーザーを介してセッションを検出するには、ダッシュボードでユーザーを見つけ、ユーザープロファイルの [**アプリの利用状況**] に移動します。セッション指標が想定どおりに増加していることを確認することで、セッショントラッキングが機能していることを確認できます。

![発生したセッション数、アプリが最初に使用された日時、最後に使用された日時を示すユーザープロファイルコンポーネント。][session\_tracking\_7]

[session\_tracking\_3]: {{ site.baseurl }}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overview/#customizing-braze-on-startup
[session\_tracking\_3]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-2-configure-the-braze-sdk-in-appboyxml
[session\_tracking\_5]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize
[session\_tracking\_6]: http://msdn.microsoft.com/en-us/library/windows/apps/hh464925.aspx
[session\_tracking\_7]: {% image_buster /assets/img_archive/test_session.png %}
[session\_tracking\_8]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android
