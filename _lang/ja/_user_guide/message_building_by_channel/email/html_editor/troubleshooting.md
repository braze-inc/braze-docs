---
nav_title: トラブルシューティング
article_title: トラブルシューティング
page_order: 9
description: "このヘルプでは、HTMLメールのトラブルシューティング方法を説明する。"
channel: email
---

# トラブルシューティング 

## テストメールでHTMLが正しく表示されない

[テストメールが]({{site.baseurl}}/developer_guide/platform_wide/sending_test_messages/#sending-a-test-push-notification-or-in-app-messages-a-classmargin-fix-namepush-inapp-testa)おかしいと感じたら、まずHTMLの設定をチェックすることをお勧めする。次に、次の問題を確認できます。
* [拡張機能の競合](#check-conflicts)
* [メールレンダリング](#check-rendering)
* [CSSインライン展開](#switch-css-inlining)

### 拡張機能の競合

ブラウザの拡張機能によっては、Eメールエディタに問題が生じる場合がある。その一例が、Google Chromeで使用する[Grammarly](https://chrome.google.com/webstore/detail/grammarly-for-chrome/kbfnbcaeplbcioakkpcpgfkobkghlhen?hl=en)だ。これらの拡張機能のいずれかを使用している場合は、次のいずれかを実行する必要があります。 
- Grammarlyがブラウザ拡張機能としてインストールされていないブラウザでBrazeのメールを編集する
- Brazeのアカウントマネージャーに連絡し、メールエディタをHTMLのみまたはプレーンテキストに切り替えるよう依頼する。 

プレーン・テキスト・ビューでは、```WYSIWYG``` （what you see is what you get）エディターが削除されるので、この要求をする前に、まずチームメンバー全員がHTMLに慣れていることを確認する必要がある。

### メールレンダリング

電子メールはブラウザや電子メールクライアントによってレンダリングが異なるので、どのブラウザや電子メールクライアントで問題が発生しているのか注意してほしい。

- [Inbox Visionを使って]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/#inbox-vision/)メールをプレビューし、さまざまなブラウザやメールクライアントでメールがどのように見えるかを確認できる。
- 問題を引き起こしているブラウザやメールクライアントを特定したら、そのブラウザやメールクライアントに対応するためにHTMLを修正し、編集する必要があることを開発チームに知らせる。

### CSSインライン展開

受信トレイのプレビューとBrazeで送信されるプレビューが一致しないことがある。これは、Brazeや他の工具によって実行されるCSSインライン展開の違いが原因である可能性があります。そのような疑いがある場合は、CSSのインライン化をオフにする。

それでもサポートが必要な場合は、[サポートチケットを]({{site.baseurl}}/braze_support/)を登録してください。
