{% multi_lang_include developer_guide/prerequisites/web.md %} また、[プッシュ通知s]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web)を設定する必要があります。

## ソフトプッシュプロンプトについて

多くの場合、サイトでは「ソフト」プッシュプロンプトを実装することをお勧めします。このプロンプトでは、プッシュ許可を要求する前に、ユーザーを「プライム」し、プッシュ通知を送る理由を説明します。これは、ユーザーに直接プロンプトを表示する頻度がブラウザーによって調整され、ユーザーがアクセス許可を拒否した場合は二度とユーザーに求めることができないため便利です。

または、標準[ Webプッシュ統合]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/#step-2-browser-registration) で説明されているように、`requestPushPermission()` を直接呼び出す代わりに、特殊なカスタム処理を含める場合は、[ トリガー ed アプリ内メッセージs]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=web) を使用します。

{% alert tip %}
これは、新しい[ノーコードプッシュプライマー]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/)を使用して、SDK のカスタマイズなしで行うことができます。
{% endalert %}

## ソフトプッシュプロンプトの設定

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

最後に、削除された呼び出しを次のスニペットで置き換えます。`openSession()` を呼び出す前に`subscribeToInAppMessage()` を呼び出します。これにより、アプリ内メッセージリスナーがプッシュプライマーメッセージを受信するのに間に合うように登録されます。

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
