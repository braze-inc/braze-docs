---
nav_title: テストメールでのHTMLレンダリング
article_title: テストメールでのHTMLレンダリング
page_order: 2

page_type: solution
description: "このヘルプ記事では、テストメールでのHTMLレンダリングの問題をトラブルシューティングする方法について説明します。"
channel: email
---

# テストメールでのHTMLレンダリングのトラブルシューティング

テストメールがオフに見える場合は、まずHTML設定を確認することをお勧めします。次に、これらの問題を確認できます:
* [拡張機能の競合](#check-conflicts)
* [メールレンダリング](#check-rendering)
* [CSSのインライン化](#switch-css-inlining)

### 拡張機能の競合

特定のブラウザー拡張機能が、当社のメールエディターに問題を引き起こす可能性があります。一例は[Grammarly<1>}がGoogle Chromeで使用される場合です。これらの拡張機能のいずれかを使用している場合は、次のいずれかを行う必要があります: 
- ブラウザ拡張機能としてGrammarlyがインストールされていないブラウザでBrazeのメールを編集する
- Brazeのアカウントマネージャーに連絡して、メールエディターをHTMLのみに切り替えるか、プレーンテキストに切り替えるよう依頼してください。 

プレーンテキストビューでは```WYSIWYG```（WYSIWYG）エディタが削除されるため、このリクエストを行う前に、すべてのチームメンバーがHTMLに慣れていることを確認する必要があります。

### メールレンダリング

メールはブラウザやメールクライアントによって異なる表示がされるため、どのブラウザやメールクライアントで問題が発生しているかに注意してください。

- [受信トレイビジョン]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/#inbox-vision/)を使用してメールをプレビューし、さまざまなブラウザやメールクライアントでメールがどのように表示されるかを確認します。
- どのブラウザやメールクライアントが問題を引き起こしているかを特定したら、開発者チームに知らせて、これらのブラウザやメールクライアントに対応するためにHTMLを修正する必要があることを伝えてください。

### CSSインライン化

受信トレイビジョンのプレビューがBrazeで送信されたものと一致しない場合があります。これは、Brazeと他のツールによって実行されるCSSインライン化の違いによって引き起こされる可能性があります。このような場合は、Brazeのアカウントマネージャーに連絡して、CSSインライン化をオフにするよう依頼してください。

まだ助けが必要ですか？[サポートチケット]({{site.baseurl}}/braze_support/)を開封する。

_最終更新日：2021年12月21日_

[37]: {{site.baseurl}}/developer_guide/platform_wide/sending_test_messages/#sending-a-test-push-notification-or-in-app-messages-a-classmargin-fix-namepush-inapp-testa
[38]: https://chrome.google.com/webstore/detail/grammarly-for-chrome/kbfnbcaeplbcioakkpcpgfkobkghlhen?hl=en
[39]: https://www.emailonacid.com/
[40]: https://litmus.com/
