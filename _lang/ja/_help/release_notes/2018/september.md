---
nav_title: 9 月
page_order: 5
noindex: true
page_type: update
description: "この記事には、2018 年 9 月のリリース ノートが含まれています。"
---
# 2018年9月発売

## iOS 12 通知グループ:追加アビリティ

Brazeを使用して [Appleの通知グループ機能]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#notification-groups) にアクセスできるようになりました。サマリー引数とグループの追加、クリティカルアラートの利用、暫定認証ユーザのフィルタリング、およびユーザプロファイルの暫定認証ステータスの表示を行うことができます。

## クワイエットタイム

顧客は、Canvas の [待機時間]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-5-select-your-send-settings) (メッセージが送信されない時間) を指定できるようになりました。**Canvasの送信設定**に移動し、「クワイエットアワーを有効にする」にチェックを入れるだけです。次に、ユーザーの現地時間での待機時間を選択し、その待機時間内にメッセージがトリガーされた場合に実行されるアクションを選択します。

また、キャンペーンでは、「一日の特定の時間帯にこのメッセージを送信する」代わりに、クワイエットタイムを使用するようになりました。

## 顧客を調整する

Brazeのお客様は、 [Adjust]({{site.baseurl}}/partners/advertising_technologies/attribution/adjust/) を使用しているBraze APIキーとBrazeインスタンスのURLを確認できるようになり、Adjustプラットフォームで連携することができます。

## セグメントフィルターにない

お客様は、 [特定のセグメントに含まれていない]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#retargeting)ユーザーからセグメントを作成できるようになりました。

## キャンバス受信者のCSVエクスポート

お客様は、キャンバスに入ったユーザーの [データをエクスポート]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_canvas_data/) できるようになりました。生成されるCSVは、キャンペーンCSVと似ています。

## 暫定的に承認された iOS 12 セグメント フィルター

特定のアプリに対して iOS 12 で暫定的に承認されたユーザーを検索できる [セグメント フィルター]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#other) が追加されました。

## アプリ内メッセージ画像アップローダー

アプリ内メッセージの画像アップローダーは、デザインパネルから作成パネルに移動しました。

## [ユーザー プロファイル] ページでの読み取り専用アクセス許可

このリリースより前は、読み取り専用 [のアクセス許可]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions)を持つユーザー プロファイルのサブスクリプション ステータスとメール アドレスを変更できました。アクセス許可の名前を `import_user` アクセス許可に変更し `import_and_update_user` 、サブスクリプションの状態とメール アドレスへの編集アクセスを制限しました。これで、開発者が読み取り専用になりすますか、この権限がない場合、サブスクリプションのステータスやメールアドレスを変更できなくなります。
