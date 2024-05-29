---
nav_title: ソフト・プッシュ・プロンプト
article_title: Web 用ソフト・プッシュ・プロンプト
platform: Web
page_order: 19
page_type: reference
description: "この記事では、Web アプリケーション用のソフトプッシュプロンプトを作成する方法について説明します。"
channel: push

---

# ソフト・プッシュ・プロンプト

> 多くの場合、サイトでは「ソフト」プッシュプロンプトを実装して、ユーザーに「プライミング」を行い、プッシュ許可をリクエストする前にプッシュ通知を送信するように説得するとよいでしょう。これは、ブラウザがユーザーに直接プロンプトを出す頻度を制限し、ユーザーが許可を拒否した場合、二度とユーザーに尋ねることができないので便利です。この記事では、Web SDK統合を変更してWebアプリケーションのプッシュ入門キャンペーンを作成する方法について説明します。

{% alert tip %}
これは、[新しいノーコードプッシュ入門書を使用すれば]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/)、SDK をカスタマイズしなくても実行できます。
{% endalert %} 

または、`requestPushPermission()`[標準のWebプッシュ統合で説明されているように直接呼び出すのではなく]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/#step-2-browser-registration)、特別なカスタム処理を含めたい場合は、[トリガーされたアプリ内メッセージを使用してください]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/)。

{% multi_lang_include archive/web-v4-rename.md %}

## ステップ 1:プッシュ入門キャンペーンを作成する

まず、Braze 管理画面で「Prime for Push」アプリ内メッセージキャンペーンを作成する必要があります。

1. **必要なテキストとスタイルでモーダルアプリ内メッセージを作成します**。 
2. 次に、クリック時の動作を [**メッセージを閉じる**] に設定します。この動作は後でカスタマイズされます。
3. キーと値のペアをメッセージに追加します。キーはあり`msg-id`、値はあります。`push-primer`
4. メッセージにカスタムイベントトリガーアクション (「prime-for-push」など) を割り当てます。必要に応じて、ダッシュボードからカスタムイベントを手動で作成できます。

## ステップ 2: 通話を削除

Braze SDK インテグレーションで、読み込みスニペット内の `automaticallyShowInAppMessages()` from への呼び出しをすべて見つけて削除します。

## ステップ 3: アップデート統合

最後に、削除した呼び出しを次のスニペットに置き換えます。

\`\`\`javascript
「@braze」から* をブレイズとしてインポートする/web-sdk";
// Be sure to remove any calls to braze.automaticallyShowInAppMessages()
braze.subscribeToInAppMessage(function(inAppMessage) {
// check if message is not a control variant
if (inAppMessage instanceof braze.inAppMessage) {
// access the key-value pairs, defined as `extras`
  const keyValuePairs = inAppMessage.extras || {};
  //Braze `msg-id` ダッシュボードで定義されたキーの値を確認します
    if (keyValuePairs["msg-id"] === "push-primer") {
    // We don't want to display the soft push prompt to users on browsers
// that don't support push, or if the user has already granted/blocked permission
    if (
    braze.isPushSupported() === false ||
      braze.isPushPermissionGranted() ||
      braze.isPushBlocked()
      ) {
        //電話しないでください `showInAppMessage`
        return
        ()

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
  ()

  //アプリ内メッセージを今すぐ表示
  braze.showInAppMessage(inAppMessage);
});
\`\`\`


ソフトプッシュプロンプトをユーザーに表示したい場合は、アプリ内メッセージをトリガーするイベント名を指定して `braze.logCustomEvent`-を呼び出します。