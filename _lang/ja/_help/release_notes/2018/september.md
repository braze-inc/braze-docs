---
nav_title: 9月
page_order: 5
noindex: true
page_type: update
description: "この記事には2018年9月のリリースノートが含まれている。"
---
# 2018年9月

## iOS 12の通知グループ：その他の能力

Brazeを使って[Appleの通知グループ機能に]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#notification-groups)アクセスできるようになった！Summary ArgumentsおよびGroupsの追加、Critical Alertsの利用、Provisionally Authenticatedユーザーのフィルター、ユーザープロファイルのProvisionally Authenticatedステータスの表示ができる。

## 静かな時間

顧客はキャンバスに[クワイエットアワー]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-5-select-your-send-settings)（メッセージを送信しない時間帯）を指定できるようになった。**キャンバスの送信設定から**「クワイエットアワーを有効にする」にチェックを入れるだけだ。次に、ユーザーの現地時間でサイレント時間を選択し、そのサイレント時間内にメッセージがトリガーされた場合の後続のアクションを選択します。

キャンペーンでも、「1日のうち特定の時間帯にこのメッセージを送信する」のではなく、「クワイエットタイム」を使用するようになった。

## 顧客を調整する

[Adjustを]({{site.baseurl}}/partners/advertising_technologies/attribution/adjust/)使用しているBraze顧客は、Braze APIキーとBrazeインスタンスURLを確認できるようになりました。

## セグメンテーションフィルターにない

顧客は、[特定のセグメントに含まれない]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#retargeting)ユーザーからセグメンテーションを作成できるようになった。

## キャンバス受信者のCSVエクスポート

顧客はキャンバスに入ったユーザーの[データをエクスポート]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_canvas_data/)できるようになった。生成されるCSVはキャンペーンCSVと同様のものになる。

## iOS12のセグメンテーションフィルターが暫定的に認可される

指定したアプリのiOS 12で仮承認されたユーザーを検索できる[セグメンテーションフィルターが]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#other)追加された。

## アプリ内メッセージ画像アップロード機能

アプリ内メッセージの画像アップロードがデザインパネルからメッセージ作成画面に移動した。

## ユーザープロファイルのページの読み取り専用権限

このリリース以前は、顧客は[読み取り専用権限で]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions)ユーザープロファイルのサブスクリプションステータスとメールアドレスを変更することができた。私たちは、`import_user` 権限を`import_and_update_user` 権限に改名し、サブスクリプションステータスとメールアドレスの編集アクセスを制限した。現在、開発者が読み取り専用の偽装なりすましをしているか、この権限がない場合、サブスクリプションのステータスやメールアドレスを変更することはできない。
