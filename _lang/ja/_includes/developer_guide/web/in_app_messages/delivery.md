{% multi_lang_include developer_guide/prerequisites/web.md %}

## メッセージトリガー

## トリガーの種類

アプリ内メッセージは、SDKが以下のカスタムイベントタイプのいずれかを記録すると自動的にトリガーされる：`Any Purchase` `Specific Purchase` 、`Session Start` 、`Custom Event` 、`Push Click` 。`Specific Purchase` 、`Custom Event` のトリガーには、ロバストなプロパティフィルターも含まれている。

{% alert note %}
アプリ内メッセージは、APIやAPIイベントによってトリガーされることはなく、SDKによって記録されるカスタムイベントによってのみトリガーされる。ロギングの詳細については、[カスタムイベントの学習を]({{site.baseurl}}/developer_guide/analytics/logging_events/)参照のこと。
{% endalert %}

### 配信セマンティクス

対象となるアプリ内メッセージはすべて、セッション開始時にユーザーの端末に配信される。SDKは配信時にアセットをプリフェッチするため、トリガー時にアセットを利用でき、表示レイテンシを最小限に抑えることができる。トリガーイベントに複数のアプリ内メッセージがある場合、最も優先度の高いメッセージのみが配信される。

SDKのセッション開始セマンティクスの詳細については、セッション[ライフサイクルを]({{site.baseurl}}/developer_guide/platform_integration_guides/analytics/tracking_sessions/)参照のこと。

### レート制限

デフォルトでは、アプリ内メッセージは30秒に1回送信できる。

これをオーバーライドするには、Brazeインスタンスが初期化される前に、次のプロパティをBraze設定に追加する。任意の正の整数に設定することができ、これは最小時間間隔を秒単位で表す。以下に例を示します。

```javascript
// Sets the minimum time interval between triggered in-app messages to 5 seconds instead of the default 30
braze.initialize('YOUR-API-KEY', { minimumIntervalBetweenTriggerActionsInSeconds: 5 })
```

## キーと値のペア

Brazeでキャンペーンを作成する際、キーと値のペアを`extras` 、アプリ内メッセージングオブジェクトがアプリにデータを送信する際に使用できるように設定できる。以下に例を示します。

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

アプリ内メッセージが自動的にトリガーされないようにする：

読み込むスニペット内の`braze.automaticallyShowInAppMessages()` への呼び出しを削除し、アプリ内メッセージの表示/非表示を処理するカスタムロジックを作成する。

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
Webサイトから`braze.automaticallyShowInAppMessages()` を削除せず、`braze.showInAppMessage` 、メッセージが何度も表示されることがある。
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

## 退団メッセージのトリガー

終了意図メッセージは、サイトを離れる前に訪問者に重要な情報を伝えるために使用される、中断のないアプリ内メッセージである。

これらのメッセージタイプのトリガーを設定するには、Webサイトにexit-intentライブラリ（[ouibounceのオープンソースライブラリなど](https://github.com/carlsednaoui/ouibounce)）を実装し、次のコードを使ってBrazeのカスタムイベントとして`'exit intent'` 。これで、今後のアプリ内メッセージキャンペーンでは、このメッセージタイプをカスタムイベントトリガーとして使うことができる。

```javascript
  var _ouibounce = ouibounce(false, {
    callback: function() { braze.logCustomEvent('exit intent'); }
  });
```
