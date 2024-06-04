---
nav_title: イベントログの使用
article_title: イベントログの使用
page_order: 6
page_type: solution
description: "このヘルプ記事では、Braze統合の問題をトラブルシューティングするためにイベントロギングを使用する方法について説明します。"
---

# イベントロギングの使用

Brazeとの統合に関する問題のトラブルシューティングを支援するために、匿名ユーザープロファイルと[イベントユーザーログを][1]設定することができます。匿名プロフィールの設定方法については、[テストユーザーの追加][2]を参照してください。

## 伐採について

イベントロギングを使用して、匿名ユーザーの動作がどのように見えるかをテストします。これは、テスト対象のアプリが電子メールを収集していない場合、ユーザーIDを特定するのに特に役立ちます。BrazeとデバイスのIPアドレスを使用して、そのデバイスをテストユーザーとして追加できます。

これは匿名ユーザーを見つけるのに最適な方法だ。この情報を使って、Brazeにどのようなデータが送信されているかをテストし、不一致がないかをチェックすることもできます。このビューから、データのデルタがBrazeに送信されているかどうかを確認できます。イベントログが記録されるたびに電子メールアドレスまたはプッシュトークンが送信されると、すべてのデータがBrazeに送信されます。

まだ助けが必要ですか？[サポートチケットを]({{site.baseurl}}/braze_support/)開く。

_最終更新日：2022年11月16日_

[1]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab
[2]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users