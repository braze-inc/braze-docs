---
nav_title: 7月
page_order: 6
noindex: true
page_type: update
description: "この記事には2016年7月のリリースノートが含まれている。"
---

# 2016年7月

## 開発者コンソールのエラーログをエラーの種類でフィルターする

このアップグレードにより、開発者コンソールのメッセージエラーログを使用して、Braze統合の問題のトラブルシューティングが容易になる。これはユーザビリティの更新であり、メッセージエラーログをタイプ別にフィルターすることができる。

## 最後に送信されたアンインストール追跡プッシュのタイムスタンプを追加した。

Brazeは、顧客のアプリにサイレントプッシュを送信し、どのデバイスが反応するかを確認することで、アンインストールを検出する。この機能により、アンインストール追跡が最後に実行された時刻を示すタイムスタンプが控えめに追加される。このタイムスタンプは、アンインストール追跡が設定されている設定ページで確認できる。[アンインストール追跡について]({{site.baseurl}}/user_guide/data_and_analytics/uninstall_tracking/#uninstall-tracking)もっと知る。

![アンインストール追跡チェックボックス][6]

## Webhookテストの機能強化

キャンペーンをライブ設定する前に、BrazeからライブWebhookメッセージをテスト送信できるようになった。テスト・メッセージを送信することで、安全なサンドボックス環境で、メッセージングとサーバー・エンドポイントが適切に設定されていることを確認することができる。[Webhookについて]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#creating-a-webhook)もっと学習しよう。

## キャンペーン受信者のCSVエクスポートにメッセージのバリエーションを追加した。

キャンペーン受信者CSVエクスポートに、受信したメッセージのバリエーションを示すカラムを追加した。Brazeからの[データエクスポートについて]({{site.baseurl}}/user_guide/data_and_analytics/exporting_dashboard_data/#exporting-dashboard-data)学習する。

## インプレッション数の制限の目安

アプリ内メッセージのインプレッション数が一定数を超えると、Brazeはユーザーにメッセージを受け取る資格を与えなくなる。[インプレッションの]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#setting-a-max-impression-cap)おおよその[上限]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#setting-a-max-impression-cap)設定について学習する。

![IAMインプレッションキャップ][11]

[6]: {% image_buster /assets/img_archive/uninstall_tracking_checkbox.png %}
[11]: {% image_buster /assets/img_archive/approx_limit_for_IAM.png %}
