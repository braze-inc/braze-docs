---
nav_title: アプリ内メッセージが表示されない
article_title: アプリ内メッセージが表示されない
page_order: 1

page_type: solution
description: "このヘルプ記事では、アプリ内メッセージが正しく表示またはレンダリングされない問題のトラブルシューティングについて説明します。"
channel: in-app messages
---

# アプリ内メッセージが表示されない

アプリ内メッセージが正しく表示またはレンダリングされない場合、確認するためのいくつかのアプローチがあります:

* [イベントトリガー](#event-triggers)
* [メッセージインプレッション](#message-impressions)
* [テスト](#run-tests)
* [セッション timeout](#session-timeout)
* [メッセージング間隔](#minimum-interval)

## イベントトリガー

キャンペーンがセッションの開始やカスタムイベントによってトリガーされる場合、このイベントやセッションがメッセージをトリガーするのに十分な頻度で発生していることを確認する必要があります。このデータを[概要][1]（セッションデータの場合）または[カスタムイベント][2]ページで確認してください。

![カスタムイベントページには、カスタムイベント「お気に入りに追加」が1か月間に発生した回数のグラフが表示されています][14]

## メッセージのインプレッション

SDK内でのアプリ内メッセージUIや配信メカニズムのカスタマイズには、開発者がアプリ内メッセージのインプレッションを手動でログに記録するために当社のメソッドを利用する必要があるかもしれません。開発者に確認して、アプリ内メッセージのカスタマイズを使用しているかどうかを確認してください。

## テストを実行する

トリガーイベントが発生しないのか、それともメッセージ自体が表示できないのかを判断することが重要です。テストするには、異なるアクション（例えば、セッション開始や異なるカスタムイベント）を使用してメッセージをトリガーし、それが表示されるかどうかを確認します。これにより、これが潜在的にデータの問題であるかどうかを特定するのに役立ちます。

あるいは、異なる種類のアプリ内メッセージテンプレートや画像のサイズを試してみてください。アプリ内メッセージ][15]の仕様が守られなければなりません。場合によっては、画像が大きすぎると、アプリ内メッセージの表示を妨げることがあります。

## セッションタイムアウト

セッションタイムアウトをカスタマイズしたかどうかを確認してください。デフォルトでは、Brazeはセッションの開始時にサーバーからアプリ内メッセージを取得します。

セッションタイムアウトを延長した場合、対象となるアプリ内メッセージを更新できる期間が延長されます。さらに、キャンペーンがセッション開始時にトリガーされるように設定されている場合、新しいセッションが登録されるために適切な時間が経過していることを確認する必要があります。例えば、セッションタイムアウトは30秒にカスタマイズされているかもしれません。アプリを開封してから30秒以内に閉じた場合、セッション開始時にトリガーされる別のアプリ内メッセージを受信する資格はありません。 

次のプラットフォームのセッションタイムアウトのカスタマイズについて詳しく学びましょう:
* \[iOS][16]
* \[Android][17]
* \[Web][18]

## 最小間隔

アプリ内メッセージが連続してトリガーされることを許可する最小間隔があるため、トリガーが早すぎる可能性があります。次のプラットフォームの最小間隔について詳しく学びます: 
* \[iOS][19]
* \[Android][20]
* \[Web][21]

インターバルはカスタマイズ可能ですが、ユーザーへの過剰なメッセージングを避けるために設定されています。

まだ助けが必要ですか？開封 a [support ticket]({{site.baseurl}}/braze_support/).

_最終更新日：2021年7月15日_

[1]: {{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/#understanding-your-app-usage-data
[2]: {{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting
[14]: {% image_buster /assets/img_archive/trouble5.png %}
[15]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/
[16]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_sessions/
[17]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/#customizing-session-timeout
[18]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_sessions/#customizing-session-timeout
[19]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers
[20]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers
[21]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#in-app-message-delivery
