---
nav_title: アプリ内メッセージのインプレッション数が低い
article_title: アプリ内メッセージのインプレッション数が低い
page_order: 2

page_type: solution
description: "このヘルプ記事では、アプリ内メッセージのインプレッションが希望よりも低い場合に実行できるアクションについて説明します。"
channel: in-app messages
---
# アプリ内メッセージのインプレッション数が低い

インプレッション数が希望よりも低い場合は、次の点を確認することをおすすめします。
* [セグメントサイズ ](#segment-size)
* [変更ログ](#segment-changelogs)
* [テストを実行する](#run-tests)
* [イベントトリガー](#event-triggers)
* [メッセージインプレッション](#message-impressions)

## セグメントサイズ

キャンペーンのセグメントサイズが、対象とするオーディエンスを反映していることを確認することが重要です。フィルターが適用されていると、オーディエンスが制限され、キャンペーンのインプレッションが減少する可能性があります。

## セグメント変更ログ

インプレッション数が以前と比べて少ない場合は、ローンチ後にセグメントやキャンペーンを意図せず変更していないことを確認してください。セグメントとキャンペーンの変更ログから、変更が行われたか、誰が変更を行ったか、いつ変更が行われたかを把握できます。

![キャンペーンの詳細ページの変更履歴を表示するリンク。ユーザーが最後にキャンペーンを閲覧してから7件変更されています] [10]

## テストを実行する

明らかな問題をすばやく特定するには、キャンペーンを複製し、自分のユーザーIDまたはメールアドレスをターゲットにして、キャンペーンを開始します。メッセージトリガー (セッション開始、カスタムイベントなど) を実行したら、メッセージを正しく受信したことを確認します。次に、ダッシュボードに移動してページを更新し、インプレッションが正しく記録されているかどうかを確認します。そうでない場合は、実装に問題がある可能性があります。

## イベントトリガー

キャンペーンがセッション開始またはカスタムイベントによってトリガーされる場合、このイベントまたはセッションがメッセージをトリガーするのに十分な頻度で発生していることを確認する必要があります。[概要][1] (セッションデータ用) [またはカスタムイベントページで次のデータを確認してください][2]。

![お気に入りに追加されたカスタムイベントが 1 か月間に発生した回数のグラフを表示するカスタムイベントページ] [11]

## メッセージインプレッション

SDK内のアプリ内メッセージUIまたは配信メカニズムをカスタマイズするには、開発者が当社の方法を利用してアプリ内メッセージのインプレッションを手動で記録する必要がある場合があります。以下の目的でアプリ内メッセージのカスタマイズを使用するかどうかは、開発者に確認してください。
  \* [iOS] [12]
  \* [アンドロイド] [13] 

まだ助けが必要ですか？[サポートチケットを開きます]({{site.baseurl}}/braze_support/)。

_最終更新日は2021年5月6日です_

[1]: {{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/#understanding-your-app-usage-data
[2]: {{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting
[10]: {% image_buster /assets/img_archive/trouble4.png %}
[11]: {% image_buster /assets/img_archive/trouble5.png %}
[12]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/customization/handling_in_app_display/
[13]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/custom_listeners/
