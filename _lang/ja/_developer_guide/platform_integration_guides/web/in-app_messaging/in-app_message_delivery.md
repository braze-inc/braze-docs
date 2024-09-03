---
nav_title: アプリ内メッセージ配信
article_title: ウェブ向けアプリ内メッセージ配信
platform: Web
channel: in-app messages
page_order: 4
page_type: reference
description: "この記事では、アプリ内メッセージを手動で表示したり、ローカルアプリ内メッセージや終了意図メッセージを送信するなど、Braze SDKを使ったアプリ内メッセージ配信について説明する。"

---

# アプリ内メッセージ配信

> この記事では、アプリ内メッセージを手動で表示したり、ローカルアプリ内メッセージや終了意図メッセージを送信するなど、Braze SDKを使ったアプリ内メッセージ配信について説明する。

## トリガーの種類

当社のアプリ内メッセージ製品では、いくつかの異なるイベントタイプの結果としてアプリ内メッセージ表示をトリガーすることができる：`Any Purchase` `Specific Purchase` 、`Session Start` 、`Custom Event` 、`Push Click` 。さらに、`Specific Purchase` そして `Custom Event` トリガーには堅牢なプロパティフィルターが含まれています。

{% alert note %}
トリガーされたアプリ内メッセージは、Braze SDK を通じて記録されたカスタムイベントでのみ機能します。アプリ内メッセージは、API または API イベント (購入イベントなど) によってトリガーすることはできません。ウェブ・アプリで作業している場合は、[カスタム・イベントのログの]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events/#tracking-custom-events)取り方をチェックしよう。
{% endalert %}

## 配信セマンティクス

ユーザーが受信可能なアプリ内メッセージはすべて、セッション開始イベントと同時にユーザーのデバイスまたはブラウザに自動的にダウンロードされ、メッセージの配信ルールに従ってトリガーされる。SDKのセッション開始セマンティクスの詳細については、[セッション・ライフサイクルのドキュメントを][10]参照のこと。

## トリガー間の最小時間間隔

デフォルトでは、高品質のユーザーエクスペリエンスを確保するために、アプリ内メッセージのレートが 30 秒に 1 回に制限されています。この値をオーバーライドするには、`minimumIntervalBetweenTriggerActionsInSeconds` の設定オプションを [`initialize`][9]関数に渡すことができる：

```javascript
// Sets the minimum time interval between triggered in-app messages to 5 seconds instead of the default 30
braze.initialize('YOUR-API-KEY', { minimumIntervalBetweenTriggerActionsInSeconds: 5 })
```

## 手動によるアプリ内メッセージ表示

新しいアプリ内メッセージがトリガーされたときに即座にサイトに表示させたくない場合は、自動表示を無効にして、自分の表示購読者を登録することができる。 

まず、ローディング・スニペットから`braze.automaticallyShowInAppMessages()` 。そして、アプリ内メッセージがトリガーされた場合、メッセージを表示するかしないかをカスタム処理する独自のロジックを作成する。 

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
`braze.showInAppMessage` を呼び出す際、ウェブサイトから`braze.automaticallyShowInAppMessages()` を削除しないと、メッセージが2回表示されることがある。
{% endalert %}

`inAppMessage` パラメータは [`braze.InAppMessage`][2]サブクラスまたは [`braze.ControlMessage`][8]オブジェクトであり、それぞれが様々なライフサイクルイベント購読メソッドを持っている。完全なドキュメントは[JSDocsを][2]参照のこと。

つだけである。 [`Modal`][17]または [`Full`][41]アプリ内メッセージは一度に一つしか表示できない。すでに1つのモーダルまたはフル・メッセージが表示されているときに、2つ目のモーダルまたはフル・メッセージを表示しようとすると、`braze.showInAppMessage` はfalseを返し、2つ目のメッセージは表示されない。

## ローカルのアプリ内メッセージ

アプリ内メッセージは、サイト内で作成し、リアルタイムでローカルに表示することもできる。ダッシュボードで使用できるすべてのカスタマイズオプションはローカルでも使用できます。これは、アプリ内でトリガーしたいメッセージをリアルタイムで表示する場合に特に便利です。ただし、これらのローカルで作成されたメッセージの分析は、Brazeのダッシュボードでは利用できない。

```javascript
  // Displays a slideup type in-app message.
  var message = new braze.SlideUpMessage("Welcome to Braze! This is an in-app message.");
  message.slideFrom = braze.InAppMessage.SlideFrom.TOP;
  braze.showInAppMessage(message);
```

## 退場を促すメッセージ

アプリ内メッセージは、訪問者がサイトからナビゲートしようとしているときに表示される。ユーザーのサイト体験を邪魔することなく、重要な情報をユーザーに伝えることができる。 

これらのメッセージを送信するには、まず、この[オープンソースライブラリの][50]ような終了インテント・ライブラリをウェブサイトに追加する。次に、以下のコード・スニペットを使って、カスタム・イベントとして「exit intent」を記録する。アプリ内メッセージキャンペーンは、トリガーのカスタムイベントとして「終了インテント」を使用してダッシュボードで作成することができる。

```javascript
  var _ouibounce = ouibounce(false, {
    callback: function() { braze.logCustomEvent('exit intent'); }
  });
```


[2]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html
[8]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.controlmessage.html
[9]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize
[10]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_sessions/#session-lifecycle
[17]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#modal-in-app-messages
[41]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#full-in-app-messages
[50]: https://github.com/carlsednaoui/ouibounce
