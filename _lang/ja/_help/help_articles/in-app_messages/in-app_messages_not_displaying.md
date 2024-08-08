---
nav_title: アプリ内メッセージが表示されない
article_title: アプリ内メッセージが表示されない
page_order: 1

page_type: solution
description: "このヘルプ記事では、アプリ内メッセージが表示されない、または正しくレンダリングされない問題のトラブルシューティングについて説明する。"
channel: in-app messages
---

# アプリ内メッセージが表示されない

アプリ内メッセージが正しく表示されない、またはレンダリングされない場合、チェックする方法はいくつかある：

* [イベントのトリガー](#event-triggers)
* [メッセージインプレッション](#message-impressions)
* [テスト](#run-tests)
* [セッションタイムアウト](#session-timeout)
* [メッセージング間隔](#minimum-interval)

## イベントのトリガー

キャンペーンがセッション開始またはカスタムイベントによってトリガーされる場合、このイベントまたはセッションがメッセージをトリガーするのに十分な頻度で起こっていることを確認したい。[概要][1]（セッションデータ用）または[カスタムイベントページで][2]このデータを確認する：

![カスタムイベントのページでは、「お気に入りに追加」されたカスタムイベントの1ヶ月間の発生回数がグラフで表示される。][14]

## メッセージインプレッション

SDK内でアプリ内メッセージのUIや配信メカニズムをカスタマイズする場合、開発者がアプリ内メッセージのインプレッションを手動で記録するために当社の方法を利用する必要がある場合がある。アプリ内メッセージのカスタマイズを使用しているかどうかは、開発者に確認すること。

## テストを実行する

トリガーイベントが発生しないのか、メッセージ自体が表示できないのかを判断することが重要である。テストするには、別のアクション（セッション開始や別のカスタムイベントなど）を使ってメッセージをトリガーし、それが表示されるかどうかを検証する。これは、データの問題の可能性があるかどうかの切り分けに役立つ。

または、アプリ内メッセージのテンプレートや画像のサイズを変えてみる。アプリ内メッセージには\[従わなければならない仕様][15] がある。画像写真が大きすぎると、アプリ内メッセージが表示されないことがある。

## セッションタイムアウト

セッションのタイムアウトをカスタマイズしたかどうかを確認する。デフォルトでは、Brazeはセッション開始時にアプリ内メッセージをサーバーから取得する。

セッションタイムアウトを延長した場合、アプリ内メッセージの受信可能期間が延長される。さらに、キャンペーンがセッション開始をトリガーとして設定されている場合、新しいセッションが登録されるのに適切な時間が経過していることを確認する必要がある。例えば、セッションのタイムアウトは30秒にカスタマイズされているかもしれない。30秒以内にアプリを開封・終了した場合は、セッション開始時にトリガーされるアプリ内メッセージを受け取る資格がない。 

以下のプラットフォームのセッションタイムアウトのカスタマイズについて学習する：
* \[iOS][16]
* \[Android][17]
* \[Web][18]

## 最小間隔

アプリ内メッセージの連続トリガーを許可する最小間隔があるため、トリガーを早くしようとしている可能性がある。以下のプラットフォームの最小間隔について学習する： 
* \[iOS][19]
* \[Android][20]
* \[Web][21]

間隔はカスタマイズ可能だが、ユーザーへの過剰なメッセージングを避けるため、間隔を設けている。

まだ助けが必要か？[サポートチケットを]({{site.baseurl}}/braze_support/)開封する。

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
