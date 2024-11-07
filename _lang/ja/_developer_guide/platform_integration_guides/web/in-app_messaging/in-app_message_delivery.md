---
nav_title: アプリ内メッセージ配信
article_title: Web 向けアプリ内メッセージ配信
platform: Web
channel: in-app messages
page_order: 4
page_type: reference
description: "この記事では、アプリ内メッセージを手動で表示したり、ローカルアプリ内メッセージや終了意図メッセージを送信するなど、Braze SDK を使ったアプリ内メッセージ配信について説明します。"

---

# アプリ内メッセージ配信

> この記事では、アプリ内メッセージを手動で表示したり、ローカルアプリ内メッセージや終了意図メッセージを送信するなど、Braze SDK を使ったアプリ内メッセージ配信について説明します。

## トリガーの種類

アプリ内メッセージ製品を使用すると、次のようなさまざまなイベントタイプの結果としてアプリ内メッセージ表示をトリガーできます: `Any Purchase`、`Specific Purchase`、`Session Start`、`Custom Event`、および `Push Click`。さらに、`Specific Purchase` そして `Custom Event` トリガーには堅牢なプロパティフィルターが含まれています。

{% alert note %}
トリガーされたアプリ内メッセージは、Braze SDK を通じて記録されたカスタムイベントでのみ機能します。アプリ内メッセージは、API または API イベント (購入イベントなど) によってトリガーすることはできません。Web アプリで作業している場合は、[カスタムイベントをログに記録する]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events/#tracking-custom-events)方法を確認してください。
{% endalert %}

## 配信セマンティクス

ユーザーが受信可能なアプリ内メッセージはすべて、セッション開始イベントと同時にユーザーのデバイスまたはブラウザに自動的にダウンロードされ、メッセージの配信ルールに従ってトリガーされる。SDK のセッション開始セマンティクスの詳細については、[セッションライフサイクルのドキュメント]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_sessions/#session-lifecycle)を参照してください。

## トリガー間の最小時間間隔

デフォルトでは、高品質のユーザーエクスペリエンスを確保するために、アプリ内メッセージのレートが 30 秒に 1 回に制限されています。この値をオーバーライドするには、`minimumIntervalBetweenTriggerActionsInSeconds` の設定オプションを [`initialize`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize)関数に渡すことができる：

```javascript
// Sets the minimum time interval between triggered in-app messages to 5 seconds instead of the default 30
braze.initialize('YOUR-API-KEY', { minimumIntervalBetweenTriggerActionsInSeconds: 5 })
```

## 手動によるアプリ内メッセージ表示

新しいアプリ内メッセージがトリガーされたときに、即時にそれらをサイトに表示させたくない場合は、自動表示を無効にして、独自の表示自分の表示サブスクライバーを登録できます。 

まず、読み込んでいるスニペット内から `braze.automaticallyShowInAppMessages()` への呼び出しを見つけて削除します。そして、アプリ内メッセージがトリガーされた場合、メッセージを表示するかしないかをカスタム処理する独自のロジックを作成する。 

```javascript
braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message
  
  if (inAppMessage.isControl) { // v4.5.0+, otherwise use  `inAppMessage instanceof braze.ControlMessage`
     return braze.showInAppMessage(inAppMessage);
  }
  
  // Display the in-app message. You could defer display here by pushing this message to code within your own application.
  // If you don't want to use Braze's built-in display capabilities, you could alternatively pass the in-app message to your own display code here.
  
  if ( should_show_the_message_according_to_your_custom_logic ) {
      braze.showInAppMessage(inAppMessage);
  } else {
      // do nothing
  }
});
```

{% alert important %}
`braze.showInAppMessage` 呼び出しているときにも Web サイトから `braze.automaticallyShowInAppMessages()` を削除しなければ、メッセージが2回表示される可能性があります。
{% endalert %}

`inAppMessage` パラメータは [`braze.InAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html) サブクラスまたは [`braze.ControlMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.controlmessage.html) オブジェクトになり、それぞれにさまざまライフサイクルイベントのサブスクリプション方式があります。完全なドキュメントについては、[JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html) を参照してください。

つだけである。 [`Modal`]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#modal-in-app-messages)または [`Full`]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#full-in-app-messages)アプリ内メッセージは一度に一つしか表示できない。すでに1つのモーダルまたはフル・メッセージが表示されているときに、2つ目のモーダルまたはフル・メッセージを表示しようとすると、`braze.showInAppMessage` はfalseを返し、2つ目のメッセージは表示されない。

## ローカルのアプリ内メッセージ

アプリ内メッセージはサイト内で作成し、リアルタイムでローカルに表示することもできます。ダッシュボードで使用できるすべてのカスタマイズオプションはローカルでも使用できます。これは、アプリ内でトリガーしたいメッセージをリアルタイムで表示する場合に特に便利です。ただし、これらのローカルで作成されたメッセージの分析は、Brazeのダッシュボードでは利用できない。

```javascript
  // Displays a slideup type in-app message.
  var message = new braze.SlideUpMessage("Welcome to Braze! This is an in-app message.");
  message.slideFrom = braze.InAppMessage.SlideFrom.TOP;
  braze.showInAppMessage(message);
```

## Exit-intent メッセージ

Exit-intent アプリ内メッセージは、訪問者がそのサイトから移動しようとしているときに表示されます。ユーザーのサイト体験を邪魔することなく、重要な情報をユーザーに伝えることができます。 

これらのメッセージを送信するには、まず、この[オープンソースライブラリー](https://github.com/carlsednaoui/ouibounce)のような exit intent ライブラリーを Web サイトに追加します。次に、以下のコード・スニペットを使って、カスタム・イベントとして「exit intent」を記録する。アプリ内メッセージキャンペーンは、トリガーのカスタムイベントとして「exit intent」を使用し、ダッシュボードで作成することができます。

```javascript
  var _ouibounce = ouibounce(false, {
    callback: function() { braze.logCustomEvent('exit intent'); }
  });
```


