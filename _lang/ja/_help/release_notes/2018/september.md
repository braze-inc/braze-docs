---
nav_title: 9月
page_order: 5
noindex: true
page_type: update
description: "この記事には2018年9月のリリースノートが含まれている。"
---
# 2018年9月

## iOS 12の通知グループ：その他の能力

Brazeを使って[アップルの通知グループ機能に]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#notification-groups)アクセスできるようになった！サマリー引数およびグループの追加、クリティカルアラートの利用、仮認証ユーザのフィルタリング、ユーザプロファイルの仮認証ステータスの表示ができる。

## 静かな時間

顧客は、キャンバスの[Quiet Hours]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-5-select-your-send-settings)(メッセージが送信されない時間)を指定できるようになりました。**キャンバスの送信設定で**「静かな時間を有効にする」にチェックを入れるだけだ。次に、ユーザーの現地時間でサイレント時間を選択し、そのサイレント時間内にメッセージがトリガーされた場合の後続のアクションを選択します。

キャンペーンでは、「1日のうち特定の時間帯にこのメッセージを送信する」のではなく、「クワイエットタイム」を使用するようになった。

## 顧客を調整する

[Adjustを]({{site.baseurl}}/partners/advertising_technologies/attribution/adjust/)使用しているBrazeのお客様は、Braze APIキーとBrazeインスタンスURLを確認できるようになり、Adjustプラットフォームで統合に使用できるようになった。

## セグメントフィルターにない

顧客は、[特定のセグメントに含まれない]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#retargeting)ユーザーからセグメントを作成できるようになった。

## キャンバス受信者のCSVエクスポート

キャンバスにエントリーしたユーザーの[データをエクスポート]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_canvas_data/)できるようになった。生成されるCSVはキャンペーンCSVと同様のものになる。

## iOS12のセグメントフィルターが暫定的に認可される

指定したアプリのiOS 12で仮承認されたユーザーを見つけることができる[セグメントフィルターが]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#other)追加された。

## アプリ内メッセージ画像アップローダー

アプリ内メッセージの画像アップローダーがデザインパネルからメール作成パネルに移動した。

## ユーザープロファイルページの読み取り専用パーミッション

このリリース以前は、顧客は[読み取り専用権限で]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions)ユーザープロファイルの購読ステータスとメールアドレスを変更することができた。私たちは、`import_user` パーミッションの名前を`import_and_update_user` パーミッションに変更し、購読ステータスとメールアドレスの編集アクセスを制限した。現在、開発者が読み取り専用になりすましたり、このパーミッションを欠いている場合、購読ステータスやメールアドレスを変更することはできない。
