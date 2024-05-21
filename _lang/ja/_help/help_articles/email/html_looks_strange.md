---
nav_title: テストメールでのHTML レンダリング
article_title: テストメールでのHTML レンダリング
page_order: 2

page_type: solution
description: "このヘルプ記事では、テストメールでのHTML レンダリングに関する問題のトラブルシューティング方法について説明します。"
channel: email
---

# テストメールでのHTML レンダリングのトラブルシューティング

[test email][37]がオフになっている場合は、まずHTML設定を確認することをお勧めします。次に、次の問題を確認できます。
* [拡張競合](#check-conflicts)
* [電子メールレンダリング](#check-rendering)
* [CSS インライン化](#switch-css-inlining)

### 拡張機能の競合

一部のブラウザ拡張機能では、電子メールエディタに問題が発生する場合があります。1 つの例は、Google Chrome で使用する場合の[Grammarly][38]) です。これらの拡張機能のいずれかを使用している場合は、次のいずれかを実行する必要があります。
\- ブラウザ拡張としてGrammarly を持たないブラウザでBraze メールを編集する
\- Braze アカウントマネージャに連絡し、電子メールエディタをHTML のみまたはプレーンテキストに切り替えるように依頼してください。 

プレーンテキストビューでは、```WYSIWYG``` (表示されているものは取得されたもの) エディタが削除されます。このリクエストを実行する前に、まずすべてのチームメンバーがHTML で快適であることを確認する必要があります。

### メールレンダリング

メールのレンダリングは、ブラウザとメールクライアントによって異なります。そのため、問題が発生しているブラウザとメールクライアントに注意してください。

- [Inbox Vision]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/#inbox-vision/)を使用してメールをプレビューし、異なるブラウザとメールクライアントでメールがどのように見えるかを確認します。
- 問題の原因となっているブラウザまたはメールクライアントを特定したら、開発者チームにHTML を変更し、それらのブラウザまたはメールクライアントに対応するように編集する必要があることを知らせます。

### CSSインライン展開

受信トレイビジョンのプレビューが、ブレーズで送信されたプレビューと一致しないことがあります。これは、Braze および他のツールによって実行されるCSS インライン展開の違いが原因である可能性があります。このような状況が疑われる場合は、Braze アカウントマネージャに連絡して、CSS インライン展開をオフにするように依頼してください。

それでも助けが必要ですか?[サポートチケット]({{site.baseurl}}/braze_support/)を開きます。

_最終更新日2021年12月21日_

[37]: {{site.baseurl}}/developer_guide/platform_wide/sending_test_messages/#sending-a-test-push-notification-or-in-app-messages-a-classmargin-fix-namepush-inapp-testa
[38]: https://chrome.google.com/webstore/detail/grammarly-for-chrome/kbfnbcaeplbcioakkpcpgfkobkghlhen?hl=en
[39]: https://www.emailonacid.com/
[40]: https://litmus.com/
