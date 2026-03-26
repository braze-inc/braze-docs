{% multi_lang_include developer_guide/prerequisites/web.md %}

## メッセージトリガー

## トリガーの種類

アプリ内メッセージは、SDKが以下のカスタムイベントタイプを記録した際に自動的にトリガーされる：`Any Purchase`、`Session Start``Specific Purchase`、`Custom Event`、、および`Push Click`なお、および`Custom Event`トリガー`Specific Purchase`には堅牢なプロパティフィルターも含まれている。

{% alert note %}
アプリ内メッセージは、API または API イベントによってトリガーすることはできません。SDK によってログに記録されるカスタムイベントによってのみトリガーされます。ロギングの詳細については、[カスタムイベントのログ記録]({{site.baseurl}}/developer_guide/analytics/logging_events/)を参照してください。
{% endalert %}

### 配信セマンティクス

すべての適格なアプリ内メッセージは、ユーザーのセッション開始時に端末に配信される。SDKが配信されると、アセットを事前に読み込む。これにより、トリガー時にアセットが利用可能となり、表示の遅延を最小限に抑える。トリガーイベントに複数の適格なアプリ内メッセージがある場合、最も優先度の高いメッセージのみが配信されます。

SDKのセッション開始の仕組みについて詳しくは、[セッションのライフサイクルを参照せよ]({{site.baseurl}}/developer_guide/platform_integration_guides/analytics/tracking_sessions/)。

### レート制限

デフォルトでは、アプリ内メッセージは 30 秒に 1 回送信できます。

これを上書きするには、Brazeインスタンスが初期化される前に、Braze設定に次のプロパティを追加する。任意の正の整数に設定できる。これは最小の時間間隔を秒単位で表す。以下に例を示します。

```javascript
// Sets the minimum time interval between triggered in-app messages to 5 seconds instead of the default 30
braze.initialize('YOUR-API-KEY', { minimumIntervalBetweenTriggerActionsInSeconds: 5 })
```

## キーと値のペア

Brazeでキャンペーンを作成する際、キーと値のペアをパラメータとして設定できる。このパラメータは、アプリ内`extras`メッセージングオブジェクトがデータをアプリに送信する際に使用できる。以下に例を示します。

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message
  if (inAppMessage instanceof braze.ControlMessage) {
    return braze.showInAppMessage(inAppMessage);
  }


  if (inAppMessage instanceof braze.InAppMessage) {
    const extras = inAppMessage.extras;
    if (extras) {
      for (const key in extras) {
        console.log("key: " + key + ", value: " + extras[key]);
      }
    }
  }
  braze.showInAppMessage(inAppMessage);
});
```

## 自動トリガーを無効にする

アプリ内メッセージが自動的にトリガーされるのを防ぐには：

読み込みスニペット内の`braze.automaticallyShowInAppMessages()`呼び出しを削除し、アプリ内メッセージの表示・非表示を処理するカスタムロジックを作成せよ。

```javascript
braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message
  
  if (inAppMessage.isControl) { // v4.5.0+, otherwise use  `inAppMessage instanceof braze.ControlMessage`
     return braze.showInAppMessage(inAppMessage);
  }
  
  // Display the in-app message. You could defer display here by pushing this message to code within your own application.
  // If you don't want to use the Braze built-in display capabilities, you could alternatively pass the in-app message to your own display code here.
  
  if ( should_show_the_message_according_to_your_custom_logic ) {
      braze.showInAppMessage(inAppMessage);
  } else {
      // do nothing
  }
});
```

{% alert important %}
Web サイトから`braze.automaticallyShowInAppMessages()`削除しない場合、またはに連絡しない`braze.showInAppMessage`場合、メッセージが複数回表示される可能性がある。
{% endalert %}

`inAppMessage` パラメータは [`braze.InAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html) サブクラスまたは [`braze.ControlMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.controlmessage.html) オブジェクトになり、それぞれにさまざまライフサイクルイベントのサブスクリプション方式があります。完全なドキュメントについては、[JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html) を参照してください。

つだけである。 [`Modal`]({{site.baseurl}}/developer_guide/in_app_messages/?tab=modal&sdktab=web)または [`Full`]({{site.baseurl}}/developer_guide/in_app_messages/?tab=full&sdktab=web)アプリ内メッセージは一度に一つしか表示できない。すでに1つのモーダルまたはフル・メッセージが表示されているときに、2つ目のモーダルまたはフル・メッセージを表示しようとすると、`braze.showInAppMessage` はfalseを返し、2つ目のメッセージは表示されない。

## 手動でメッセージをトリガーする

### リアルタイムでメッセージを表示する

アプリ内メッセージはサイト内で作成し、リアルタイムでローカルに表示することもできます。ダッシュボードで使用できるすべてのカスタマイズオプションはローカルでも使用できます。これは、アプリ内でトリガーしたいメッセージをリアルタイムで表示する場合に特に便利です。ただし、これらのローカルで作成されたメッセージの分析は、Brazeのダッシュボードでは利用できない。

```javascript
  // Displays a slideup type in-app message.
  var message = new braze.SlideUpMessage("Welcome to Braze! This is an in-app message.");
  message.slideFrom = braze.InAppMessage.SlideFrom.TOP;
  braze.showInAppMessage(message);
```

## 退出意図メッセージのトリガー

離脱意図メッセージとは、訪問者がサイトを離れる前に重要な情報を伝えるために使用される、邪魔にならないアプリ内メッセージである。

これらのメッセージタイプにトリガーを設定するには、Web サイトに退出検知ライブラリー（[ouibounceのオープンソースライブラリー](https://github.com/carlsednaoui/ouibounce)など）を実装する。その後、以下のコードを使用して、Brazeでカスタムイベントとして`'exit intent'`ログを記録する。これで、今後のアプリ内メッセージキャンペーンでは、このメッセージタイプをカスタムイベントトリガーとして使うことができる。

```javascript
  var _ouibounce = ouibounce(false, {
    callback: function() { braze.logCustomEvent('exit intent'); }
  });
```
