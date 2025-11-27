{% multi_lang_include developer_guide/prerequisites/web.md %} [プッシュ通知の設定も]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web)必要だ。

## ソフト・プッシュ・プロンプトについて

多くの場合、サイトでは「ソフト」プッシュプロンプトを実装することをお勧めします。このプロンプトでは、プッシュ許可を要求する前に、ユーザーを「プライム」し、プッシュ通知を送る理由を説明します。これは、ユーザーに直接プロンプトを表示する頻度がブラウザーによって調整され、ユーザーがアクセス許可を拒否した場合は二度とユーザーに求めることができないため便利です。

また、特別なカスタム処理を含めたい場合は、標準の [Web プッシュ統合]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/#step-2-browser-registration)で説明されているように、`requestPushPermission()` を直接呼び出すのではなく、[トリガーされたアプリ内メッセージ]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=web)を使用します。

{% alert tip %}
これは、新しい[ノーコードプッシュプライマー]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/)を使用して、SDK のカスタマイズなしで行うことができます。
{% endalert %}

## ソフト・プッシュ・プロンプトの設定

{% multi_lang_include archive/web-v4-rename.md %}

### ステップ 1: プッシュ・プライマー・キャンペーンを作成する

まず、Braze ダッシュボードで「Prime for Push」アプリ内メッセージングキャンペーンを作成する必要があります。

1. 希望するテキストとスタイリングで**モーダルな**アプリ内メッセージを作成する。 
2. 次に、クリック時の動作を「**メッセージを閉じる**」に設定する。この動作は後でカスタマイズする。
3. メッセージにキーと値のペアを追加する。キーは`msg-id` 、値は`push-primer` 。
4. カスタムイベントトリガーアクション（"prime-for-push "など）をメッセージに割り当てる。必要に応じて、ダッシュボードから手動でカスタムイベントを作成することもできます。

### ステップ2:呼び出しを削除する

Braze SDK 統合で、読み込みスニペット内から `automaticallyShowInAppMessages()` の呼び出しを見つけて削除します。

### ステップ 3:アップデートの統合

最後に、削除したコールを以下のスニペットで置き換える：

```javascript
import * as braze from "@braze/web-sdk";
// Be sure to remove any calls to braze.automaticallyShowInAppMessages()
braze.subscribeToInAppMessage(function(inAppMessage) {
  // check if message is not a control variant
  if (inAppMessage instanceof braze.inAppMessage) {
    // access the key-value pairs, defined as `extras`
    const keyValuePairs = inAppMessage.extras || {};
    // check the value of our key `msg-id` defined in the Braze dashboard
    if (keyValuePairs["msg-id"] === "push-primer") {
      // We don't want to display the soft push prompt to users on browsers
      // that don't support push, or if the user has already granted/blocked permission
      if (
        braze.isPushSupported() === false ||
        braze.isPushPermissionGranted() ||
        braze.isPushBlocked()
      ) {
        // do not call `showInAppMessage`
        return;
      }

      // user is eligible to receive the native prompt
      // register a click handler on one of the two buttons
      if (inAppMessage.buttons[0]) {
        // Prompt the user when the first button is clicked
        inAppMessage.buttons[0].subscribeToClickedEvent(function() {
          braze.requestPushPermission(
            function() {
              // success!
            },
            function() {
              // user declined
            }
          );
        });
      }
    }
  }

  // show the in-app message now
  braze.showInAppMessage(inAppMessage);
});
```

ユーザーにソフトプッシュプロンプトを表示する場合は、このアプリ内メッセージをトリガーする任意のイベント名で `braze.logCustomEvent` を呼び出します。
