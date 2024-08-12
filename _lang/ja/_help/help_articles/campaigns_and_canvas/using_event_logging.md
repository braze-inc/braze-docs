---
nav_title: イベントログを使う
article_title: イベントログを使う
page_order: 6
page_type: solution
description: "このヘルプ記事では、Braze統合の問題をトラブルシューティングするためにイベントロギングを使用する方法について説明する。"
---

# イベントロギングを使用する

Brazeインテグレーションに関する問題のトラブルシューティングを支援するために、匿名ユーザープロファイルと[イベントユーザーログを][1]設定することができる。匿名プロファイルの設定ステップについては、[テストユーザーの追加][2]を参照のこと。

## 伐採について

イベントロギングを使って、匿名ユーザーの行動がどのように見えるかをテストする。これは、テスト対象のアプリがメールを収集していない場合、ユーザーIDを識別するのに特に役立つ。BrazeとデバイスのIPアドレスを使って、そのデバイスをテストユーザーとして追加できる。

これは匿名ユーザーを見つけるのに最適な方法だ。この情報を使って、Brazeにどのようなデータが送られているかをテストし、矛盾がないかをチェックすることもできる。このビューから、データのデルタがBrazeに送信されているかどうかを識別できる。イベントログが記録されるたびにメールアドレスまたはプッシュトークンが送信される場合、すべてのデータがBrazeに送信される。

まだ助けが必要か？[サポートチケットを]({{site.baseurl}}/braze_support/)開封する。

_最終更新日：2022年11月16日_

[1]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab
[2]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users