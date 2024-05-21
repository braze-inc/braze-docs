---
nav_title: アプリ内メッセージが表示されない
article_title: アプリ内メッセージが表示されない
page_order: 1

page_type: solution
description: "このヘルプでは、アプリ内メッセージが正しく表示されない、またはレンダリングされない問題のトラブルシューティングについて説明します。"
channel: in-app messages
---

# アプリ内メッセージが表示されない

アプリ内メッセージが正しく表示またはレンダリングされていないことがわかった場合は、次の方法を確認します。

* [イベントトリガ](#event-triggers)
* [メッセージインプレッション](#message-impressions)
* [テスト](#run-tests)
* [セッションタイムアウト](#session-timeout)
* [メール送信間隔](#minimum-interval)

## イベントトリガ

キャンペーンがセッション開始またはカスタムイベントによってトリガーされる場合、このイベントまたはセッションがメッセージをトリガーするのに十分な頻度で発生していることを確認する必要があります。[Overview][1](セッションデータの場合)または[カスタムイベント][2]ページでこのデータをチェックします。

![カスタムイベントに追加されたカスタムイベントが1 か月間に発生した回数のグラフを示すカスタムイベントページ][14]

## メッセージインプレッション

SDK 内のアプリ内メッセージUI または配信メカニズムをカスタマイズすると、開発者が当社のメソッドを使用してアプリ内メッセージインプレッションを手動でログインする必要が生じる場合があります。開発者に確認して、アプリ内メッセージのカスタマイズを使用しているかどうかを確認します。

## テストの実行

トリガイベントが発生していないか、メッセージ自体が表示できないかを判断することが重要です。テストするには、別のアクション(セッション開始や別のカスタムイベントなど)を使用してメッセージをトリガし、表示されるかどうかを確認します。これは、これが潜在的にデータの問題であるかどうかを分離するのに役立ちます。

または、別のタイプのアプリ内メッセージテンプレートまたはイメージのサイズを使用してみます。従うべき[アプリ内メッセージの仕様][15]があります。画像が大きすぎると、アプリ内メッセージが表示されないことがあります。

## セッションタイムアウト

セッションタイムアウトをカスタマイズしたかどうかを確認します。デフォルトでは、Braze はサーバーからセッションの開始時にアプリ内メッセージを取得します。

セッションのタイムアウトが延長されている場合は、対象となるアプリ内メッセージを更新できる期間が延長されます。さらに、キャンペーンがセッション開始をトリガーするように設定されている場合は、新しいセッションが登録されるまでに適切な時間が経過していることを確認する必要があります。たとえば、セッションタイムアウトが30 秒にカスタマイズされている場合があります。30 秒以内にアプリを開閉した場合、セッション開始時にトリガーされた別のアプリ内メッセージを受信する資格はありません。 

以下のプラットフォームのセッションタイムアウトのカスタマイズについて詳しく説明します。
\* [iOS][16]
\* [Android][17]
\* [Web][18]

## 最小間隔

アプリ内のメッセージを連続的にトリガーできる最小間隔があるため、あまりにも早くトリガーしようとしている可能性があります。以下のプラットフォームの最小間隔について詳しく説明します。
\* [iOS][19]
\* [Android][20]
\* [Web][21]

間隔はカスタマイズ可能ですが、ユーザーに過剰なメッセージが送られないようにするために、間隔はまだ設定されています。

それでも助けが必要ですか?[サポートチケット]({{site.baseurl}}/braze_support/)を開きます。

_最終更新日2021年7月15日_

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
