---
nav_title: ソフト・プッシュ・プロンプト
article_title: ウェブ用ソフト・プッシュ・プロンプト
platform: Web
page_order: 19
page_type: reference
description: "この記事では、Webアプリケーション用にソフトプッシュプロンプトを作成する方法を説明する。"
channel: push

---

# ソフト・プッシュ・プロンプト

> プッシュ許可を要求する前に、ユーザーを "プライム "し、プッシュ通知を送信するケースを説明する "ソフト "プッシュ・プロンプトを実装するのは、サイトにとって良いアイデアだ。ブラウザは、ユーザーに直接プロンプトを表示する頻度を制限しているため、これは便利である。この記事では、Webアプリケーションのプッシュプライマーキャンペーンを作成するために、Web SDKインテグレーションを修正することについて説明する。

{% alert tip %}
これは、私たちの新しい[コードプッシュ不要の入門書を]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/)使えば、SDKをカスタマイズすることなく行うことができる。
{% endalert %} 

また、特別なカスタム処理を含めたい場合は、標準の[ウェブプッシュ統合で]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/#step-2-browser-registration)説明されているように、`requestPushPermission()` を直接呼び出す代わりに、[アプリ内メッセージのトリガーを]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/)使用する：

{% multi_lang_include archive/web-v4-rename.md %}

## ステップ 1:プッシュ・プライマー・キャンペーンを作成する

まず、Brazeダッシュボードで「Prime for Push」アプリ内メッセージングキャンペーンを作成する必要がある：

1. 希望するテキストとスタイリングで**モーダルな**アプリ内メッセージを作成する。 
2. 次に、クリック時の動作を「**メッセージを閉じる**」に設定する。この動作は後でカスタマイズする。
3. メッセージにキーと値のペアを追加する。キーは`msg-id` 、値は`push-primer` 。
4. カスタムイベントトリガーアクション（"prime-for-push "など）をメッセージに割り当てる。必要に応じて、ダッシュボードから手動でカスタムイベントを作成することもできる。

## ステップ2:コールを削除する

Braze SDKインテグレーションで、ローディングスニペット内の`automaticallyShowInAppMessages()` 。

## ステップ 3:アップデートの統合

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


ユーザーにソフトプッシュプロンプトを表示したい場合は、`braze.logCustomEvent` - このアプリ内メッセージをトリガーするイベント名で呼び出す。