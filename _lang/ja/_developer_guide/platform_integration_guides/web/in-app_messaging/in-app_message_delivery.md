---
nav_title: アプリ内メッセージ配信
article_title: Web 用アプリ内メッセージ配信
platform: Web
channel: in-app messages
page_order: 4
page_type: reference
description: "この記事では、アプリ内メッセージを手動で表示したり、ローカルのアプリ内メッセージや終了インテントメッセージを送信したりするなど、Braze SDKを介したアプリ内メッセージ配信について説明します。"

---

# アプリ内メッセージ配信

> この記事では、アプリ内メッセージを手動で表示したり、ローカルのアプリ内メッセージや終了インテントメッセージを送信したりするなど、Braze SDKを介したアプリ内メッセージ配信について説明します。

## トリガーの種類

アプリ内メッセージ製品を使用すると、次のようなさまざまなイベントタイプの結果としてアプリ内メッセージ表示をトリガーできます: `Any Purchase`、`Specific Purchase`、`Session Start`、`Custom Event`、および `Push Click`。さらに、`Specific Purchase` そして `Custom Event` トリガーには堅牢なプロパティフィルターが含まれています。

{% alert note %}
トリガーされたアプリ内メッセージは、Braze SDK を通じて記録されたカスタムイベントでのみ機能します。アプリ内メッセージは、API または API イベント (購入イベントなど) によってトリガーすることはできません。ウェブアプリを使用している場合は、[カスタムイベントをログに記録する方法をご覧ください]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events/#tracking-custom-events)。
{% endalert %}

## 配信セマンティクス

ユーザーが対象となるすべてのアプリ内メッセージは、セッション開始イベント時にユーザーのデバイスまたはブラウザーに自動的にダウンロードされ、メッセージの配信ルールに従ってトリガーされます。SDK [のセッション開始セマンティクスの詳細については、セッションライフサイクルのドキュメントをご覧ください][10]。

## トリガー間の最小時間間隔

デフォルトでは、高品質のユーザーエクスペリエンスを確保するために、アプリ内メッセージのレートが 30 秒に 1 回に制限されています。この値をオーバーライドするには、`minimumIntervalBetweenTriggerActionsInSeconds`[`initialize`][9]設定オプションを関数に渡すことができます。

```javascript
// Sets the minimum time interval between triggered in-app messages to 5 seconds instead of the default 30
braze.initialize('YOUR-API-KEY', { minimumIntervalBetweenTriggerActionsInSeconds: 5 })
```

## アプリ内メッセージの手動表示

新しいアプリ内メッセージがトリガーされたときにサイトにすぐに表示されないようにするには、自動表示を無効にして、独自のディスプレイサブスクライバーを登録できます。 

まず、`braze.automaticallyShowInAppMessages()`ロード中のスニペットの中からへの呼び出しを見つけて削除します。次に、トリガーされたアプリ内メッセージをカスタム処理する独自のロジックを作成し、メッセージを表示または非表示にします。 

\`\`\`javascript
braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
// this will log an impression and not show a visible message
  
  if (inAppMessage.isControl) { // v4.5.0+, otherwise use  `inAppMessage instanceof braze.ControlMessage`
     Braze.showinアプリメッセージを返す (アプリメッセージ内);
  ()
  
  // Display the in-app message. You could defer display here by pushing this message to code within your own application.
// If you don't want to use Braze's built-in display capabilities, you could alternatively pass the in-app message to your own display code here.
  
  if ( should\_show\_the\_message\_according\_to\_your\_custom\_logic ) {
      Braze.アプリメッセージを表示 (アプリメッセージ内);
  } else {
      何もしない
  ()
});
\`\`\`

{% alert important %}
`braze.automaticallyShowInAppMessages()`同じく電話をかけているときにWebサイトから削除しないと`braze.showInAppMessage`、メッセージが2回表示されることがあります。
{% endalert %}

`inAppMessage`[`braze.InAppMessage`[`braze.ControlMessage`][8]][2]パラメータはサブクラスまたはオブジェクトで、それぞれにさまざまなライフサイクルイベントサブスクリプションメソッドがあります。詳細なドキュメントについては [JSDocs][2] を参照してください。

[`Modal`[`Full`][41]][17]一度に表示できるメッセージは1つまたはアプリ内メッセージのみです。既に表示されているときに 2 `braze.showInAppMessage` つ目のモーダルメッセージまたはフルメッセージを表示しようとすると、false が返され、2 番目のメッセージは表示されません。

## ローカルのアプリ内メッセージ

アプリ内メッセージをサイト内で作成し、ローカルにリアルタイムで表示することもできます。ダッシュボードで使用できるすべてのカスタマイズオプションはローカルでも使用できます。これは、アプリ内でトリガーしたいメッセージをリアルタイムで表示する場合に特に便利です。ただし、これらのローカルで作成されたメッセージの分析は、Brazeダッシュボードでは使用できません。

```javascript
  // Displays a slideup type in-app message.
  var message = new braze.SlideUpMessage("Welcome to Braze! This is an in-app message.");
  message.slideFrom = braze.InAppMessage.SlideFrom.TOP;
  braze.showInAppMessage(message);
```

## エグジット・インテント・メッセージ

訪問者がサイトから離れようとしているときに、終了意向のアプリ内メッセージが表示されます。これにより、サイトでのユーザー体験を妨げることなく、重要な情報をユーザーに伝える機会が増えます。 

これらのメッセージを送信するには、まず、[このオープンソースライブラリなどの出口インテントライブラリをウェブサイトに追加します][50]。次に、次のコードスニペットを使用して「終了意図」をカスタムイベントとして記録します。その後、「離脱意向」をトリガーカスタムイベントとして使用して、アプリ内メッセージキャンペーンをダッシュボードで作成できます。

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
