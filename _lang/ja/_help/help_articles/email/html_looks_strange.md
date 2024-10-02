---
nav_title: テストメールのHTMLレンダリング
article_title: テストメールのHTMLレンダリング
page_order: 2

page_type: solution
description: "このヘルプでは、テストメールのHTMLレンダリングに関する問題のトラブルシューティング方法を説明する。"
channel: email
---

# テストメールのHTMLレンダリングのトラブルシューティング

[テストメールが][37]おかしいと感じたら、まずHTMLの設定をチェックすることをお勧めする。次に、これらの問題をチェックすることができる：
* [エクステンションのコンフリクト](#check-conflicts)
* [メールレンダリング](#check-rendering)
* [CSSのインライン化](#switch-css-inlining)

### エクステンションのコンフリクト

ブラウザの拡張機能によっては、Eメールエディタに問題が生じる場合がある。その一例が、Google Chromeで使用される[Grammarly][38]である）。これらのエクステンションのいずれかを使用しているのであれば、どちらかを選ぶべきである： 
- Grammarlyがブラウザ拡張機能としてインストールされていないブラウザでBrazeのメールを編集する
- Brazeのアカウントマネージャーに連絡し、メールエディタをHTMLのみまたはプレーンテキストに切り替えるよう依頼する。 

プレーン・テキスト・ビューでは、```WYSIWYG``` （what you see is what you get）エディターが削除されるので、この要求をする前に、まずチームメンバー全員がHTMLに慣れていることを確認する必要がある。

### メールレンダリング

電子メールはブラウザや電子メールクライアントによってレンダリングが異なるので、どのブラウザや電子メールクライアントで問題が発生しているのか注意してほしい。

- [Inbox Visionを使って]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/#inbox-vision/)メールをプレビューし、さまざまなブラウザやメールクライアントでメールがどのように見えるかを確認できる。
- 問題を引き起こしているブラウザやメールクライアントを特定したら、そのブラウザやメールクライアントに対応するためにHTMLを修正し、編集する必要があることを開発チームに知らせる。

### CSSのインライン化

Inbox Visionのプレビューが、Brazeで送信されたものとまだ一致しないことがある。これは、Brazeと他のツールで実行されるCSSインライン化の違いによるものと思われる。このような疑いがある場合は、Brazeのアカウントマネージャーに連絡し、CSSのインライン化をオフにするよう依頼してほしい。

まだ助けが必要か？[サポートチケットを]({{site.baseurl}}/braze_support/)開く。

_最終更新日：2021年12月21日_

[37]: {{site.baseurl}}/developer_guide/platform_wide/sending_test_messages/#sending-a-test-push-notification-or-in-app-messages-a-classmargin-fix-namepush-inapp-testa
[38]: https://chrome.google.com/webstore/detail/grammarly-for-chrome/kbfnbcaeplbcioakkpcpgfkobkghlhen?hl=en
[39]: https://www.emailonacid.com/
[40]: https://litmus.com/
