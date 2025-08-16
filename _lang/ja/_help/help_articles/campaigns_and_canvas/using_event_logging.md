---
nav_title: イベントロギングを使用する
article_title: イベントロギングを使用する
page_order: 6
page_type: solution
description: "このヘルプ記事では、イベントログを使用してBrazeインテグレーションの問題をトラブルシューティングする方法について説明します。"
---

# イベント ログの使用

Braze統合の問題のトラブルシューティングを支援するために、匿名のユーザープロファイルと[イベントユーザーログ]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab)を設定できます。匿名プロファイルの設定手順については、[テストユーザーの追加]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users)を参照してください。

## ログについて

イベント ログを使用して、匿名ユーザーの動作がどのように見えるかをテストします。これは、テスト中のアプリがメールを収集しない場合に、ユーザーIDを特定するのに特に役立ちます。BrazeとデバイスのIPアドレスを使用して、そのデバイスをテストユーザーとして追加できます。

これは匿名ユーザーを見つけるための素晴らしい方法です。この情報を使用して、Brazeに送信されているデータをテストし、不一致がないか確認することもできます。このビューから、データのデルタがBrazeに送信されているかどうかを確認できます。メールアドレスまたはプッシュトークンがログに記録されるすべてのイベントと共に送信される場合、すべてのデータがBrazeに送信されます。

サポートが必要な場合は、[サポートチケットを]({{site.baseurl}}/braze_support/)を登録してください。

_最終更新日: 2022年11月16日_

