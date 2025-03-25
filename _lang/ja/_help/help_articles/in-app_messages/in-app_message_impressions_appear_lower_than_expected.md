---
nav_title: アプリ内メッセージのインプレッション数が少ない
article_title: アプリ内メッセージのインプレッション数が少ない
page_order: 2

page_type: solution
description: "このヘルプ記事では、アプリ内メッセージのインプレッションが思ったよりも低い場合に取るべきアクションについて説明する。"
channel: in-app messages
---
# アプリ内メッセージのインプレッションが低い。

インプレッションが思ったより低い場合は、以下をチェックすることをお勧めする：
* [セグメントサイズ](#segment-size)
* [変更ログ](#segment-changelogs)
* [テストを実行する](#run-tests)
* [イベントトリガー](#event-triggers)
* [メッセージインプレッション](#message-impressions)

## セグメントサイズ

キャンペーンにおけるセグメンテーションのサイズが、意図したオーディエンスを反映していることを確認することが重要だ。フィルターが適用されてオーディエンスが制限され、キャンペーンのインプレッションが少なくなっている可能性がある。

## セグメント変更ログ

インプレッション数がかつてと比較して低い場合は、ローンチ後に意図せずセグメントやキャンペーンを変更した人がいないか確認する。セグメンテーションとキャンペーンの変更履歴は、いつ、誰が、どのような変更を行ったかをインサイトしてくれる。

![キャンペーン詳細ページで、ユーザーがキャンペーンを最後に閲覧してからの7つの変更点を含む変更履歴を閲覧するためのリンク][10]

## テストを実行する

明らかな問題を特定する簡単な方法は、キャンペーンを複製し、自分のユーザー ID またはメールをターゲットにして、キャンペーンを開始することです。メッセージトリガー（セッション開始、カスタムイベントなど）を実行した後、メッセージを正しく受信したことを確認する。その後、ダッシュボードに移動し、ページを更新してインプレッションが正しく記録されているかどうかを確認します。そうでない場合、問題はあなたの実装にある可能性が高い。

## イベントトリガー

キャンペーンがセッションの開始やカスタムイベントによってトリガーされる場合、このイベントやセッションがメッセージをトリガーするのに十分な頻度で発生していることを確認する必要があります。このデータを[概要][1]（セッションデータの場合）または[カスタムイベント][2]ページで確認してください。

![カスタムイベントページには、カスタムイベント「お気に入りに追加」が1か月間に発生した回数のグラフが表示されています][11]

## メッセージインプレッション

SDK 内のアプリ内メッセージ UI または配信メカニズムをカスタマイズするには、開発者が Braze のメソッドを使用してアプリ内メッセージインプレッションを手動でログインする必要がある場合があります。開発者に確認し、以下のアプリ内メッセージのカスタマイズを使用しているかどうかを確認してください。
  * [iOS][12] 
  * [Android][13] 

それでもサポートが必要な場合は、[サポートチケット]({{site.baseurl}}/braze_support/)を登録してください。

_最終更新日：2021年5月6日_

[1]: {{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/#understanding-your-app-usage-data
[2]: {{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting
[10]: {% image_buster /assets/img_archive/trouble4.png %}
[11]: {% image_buster /assets/img_archive/trouble5.png %}
[12]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/customization/handling_in_app_display/
[13]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/custom_listeners/
