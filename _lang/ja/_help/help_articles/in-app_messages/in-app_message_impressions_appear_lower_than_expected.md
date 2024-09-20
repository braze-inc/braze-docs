---
nav_title: 低アプリ内メッセージインプレッション
article_title: 低アプリ内メッセージインプレッション
page_order: 2

page_type: solution
description: "このヘルプ記事では、アプリ内メッセージのインプレッションが希望よりも少ない場合に取ることができるアクションについて説明します。"
channel: in-app messages
---
# アプリ内メッセージのインプレッションが少ない

インプレッションが希望よりも少ない場合は、次の点を確認することをお勧めします:
* [セグメントサイズ](#segment-size)
* [変更履歴](#segment-changelogs)
* [テストを実行する](#run-tests)
* [イベントトリガー](#event-triggers)
* [メッセージインプレッション](#message-impressions)

## セグメントサイズ

あなたのキャンペーンのセグメントサイズが意図したオーディエンスを反映していることを確認することが重要です。フィルターが適用されている可能性があり、オーディエンスが制限され、キャンペーンのインプレッションが少なくなっている可能性があります。

## セグメントの変更履歴

インプレッション数が以前と比べて少ない場合、セグメントやキャンペーンが開始以来意図せず変更されていないか確認してください。私たちのSegmentおよびキャンペーンの変更履歴は、行われた変更、その変更を行った人物、およびその変更が行われた時期についてのインサイトを提供します。

![ユーザーが最後にキャンペーンを見てから7つの変更があったキャンペーン詳細ページの変更履歴を見るためのリンク][10]

## テストを実行する

明らかな問題を特定する迅速な方法は、キャンペーンを複製し、自分のユーザー ID またはメールをターゲットにして、キャンペーンを開始することです。メッセージ{トリガー}（{セッション}開始、{カスタムイベント}など）を実行した後、メッセージを正しく受信したことを確認してください。次に、ダッシュボードに移動し、ページを更新してインプレッションが正しく記録されているか確認します。それがそうでない場合、問題はおそらくあなたの実装内にあります。

## イベントトリガー

キャンペーンがセッション開始またはカスタムイベントによってトリガーされる場合、このイベントまたはセッションがメッセージをトリガーするのに十分な頻度で発生していることを確認する必要があります。セッションデータについては[概要][1]または[カスタムイベント][2]ページでこのデータを確認してください。

![カスタムイベントページには、カスタムイベント「お気に入りに追加」が1か月間に発生した回数のグラフが表示されています][11]

## メッセージインプレッション

SDK内でのアプリ内メッセージUIや配信メカニズムのカスタマイズには、開発者がアプリ内メッセージのインプレッションを手動でログに記録するために当社のメソッドを利用する必要があるかもしれません。開発者に確認して、アプリ内メッセージのカスタマイズを使用しているかどうかを確認してください。
  * \[iOS][12] 
  * \[Android][13] 

まだ助けが必要ですか？[サポートチケット]({{site.baseurl}}/braze_support/)を開封する。

_最終更新日: 2021年5月6日_

[1]: {{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/#understanding-your-app-usage-data
[2]: {{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting
[10]: {% image_buster /assets/img_archive/trouble4.png %}
[11]: {% image_buster /assets/img_archive/trouble5.png %}
[12]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/customization/handling_in_app_display/
[13]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/custom_listeners/
