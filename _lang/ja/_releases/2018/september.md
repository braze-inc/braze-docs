---
nav_title: 9月
page_order: 5
noindex: true
page_type: update
description: "この記事には2018年9月のリリースノートが含まれている。"
---
# 2018年9月

## iOS 12の通知グループ：その他の能力

Brazeを使って[アップルの通知グループ機能に]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#notification-groups)アクセスできるようになった！概要引数とグループを追加したり、重要なアラートを利用したり、暫定的に認証済みのユーザーをフィルタリングしたり、ユーザープロファイルで暫定的に認証済みのステータスを表示したりできます。

## 静かな時間

キャンバスに[サイレント時間]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-5-select-your-send-settings) (メッセージを送信しない時間帯) を指定できるようになりました。**キャンバスの送信設定で**「静かな時間を有効にする」にチェックを入れるだけだ。次に、ユーザーの現地時間でサイレント時間を選択し、そのサイレント時間内にメッセージがトリガーされた場合の後続のアクションを選択します。

キャンペーンでは、「1日のうち特定の時間帯にこのメッセージを送信する」のではなく、「クワイエットタイム」を使用するようになった。

## 顧客を調整する

[Adjust]({{site.baseurl}}/partners/message_orchestration/attribution/adjust/) を使用している Braze のお客様が、Braze API キーと Braze インスタンス URL を確認できるようになりました。これらは、Adjust プラットフォームで統合に使用できます。

## セグメントフィルターにない

[特定のセグメントに含まれていない]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#retargeting)ユーザーからセグメントを作成できるようになりました。

## キャンバス受信者のCSVエクスポート

キャンバスにエントリーしたユーザーの[データをエクスポート]({{site.baseurl}}/user_guide/data/export_braze_data/export_canvas_data/)できるようになった。生成されるCSVはキャンペーンCSVと同様のものになる。

## iOS12のセグメントフィルターが暫定的に認可される

特定のアプリのiOS 12 で仮承認されているユーザーを見つけることができる[Segment フィルター]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#other) が追加されました。

## アプリ内メッセージ画像アップローダー

アプリ内メッセージ用の画像アップローダーがデザインパネルから作成パネルに移動しました。

## ユーザープロファイルページの読み取り専用パーミッション

このリリースより前は、[読み取り専用権限]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions)を持つユーザープロファイルでサブスクリプションステータスとメールアドレスを変更できました。`import_user` 権限の名前を `import_and_update_user` 権限に変更し、サブスクリプションステータスとメールアドレスの編集アクセスを制限しました。現在、開発者が読み取り専用になりすましたり、このパーミッションを欠いている場合、購読ステータスやメールアドレスを変更することはできない。
