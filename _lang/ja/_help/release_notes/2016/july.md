---
nav_title: 7月
page_order: 6
noindex: true
page_type: update
description: "この記事には2016年7月のリリースノートが含まれています。"
---

# 2016年7月

## エラータイプによるDeveloper Consoleのエラーログのフィルタリング

このアップグレードにより、Developer Consoleのメッセージエラーログを使用して、Brazeの統合に関する問題のトラブルシューティングが容易になります。これは、メッセージエラーログをタイプ別にフィルタリングできるようにするユーザビリティの更新であり、特定の統合の問題を見つけ、特定することがより簡単になります。

## 最後に送信されたアンインストール追跡プッシュのタイムスタンプを追加

Brazeは、顧客のアプリにサイレントプッシュを送信し、どのデバイスが反応するかを確認することで、アンインストールを検出します。この機能により、アンインストール追跡が最後に実行された日時を示すタイムスタンプが控えめに追加されます。このタイムスタンプは、アンインストール追跡が設定されている設定ページで確認できます。[アンインストール・トラッキングについて]({{site.baseurl}}/user_guide/data_and_analytics/uninstall_tracking/#uninstall-tracking)詳しくはこちらをご覧ください。

トラッキング・チェックボックスのアンインストール][6]。

## ウェブフック・テストの強化

キャンペーンを開始する前に、Brazeからライブウェブフックメッセージをテスト送信できるようになりました。テスト・メッセージを送信することで、メッセージとサーバー・エンドポイントが安全なサンドボックス環境で適切に設定されていることを確認することができます。[ウェブフックについて]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#creating-a-webhook)詳しくはこちら

## キャンペーン受信者のCSVエクスポートに受信メッセージのバリエーションを追加

キャンペーン受信者のCSVエクスポートに、受信したメッセージのバリエーションを示す列を追加しました。Brazeからの[データエクスポートについては]({{site.baseurl}}/user_guide/data_and_analytics/exporting_dashboard_data/#exporting-dashboard-data)こちらをご覧ください。

## インプレッション数のおおよその制限

アプリ内メッセージが一定数のインプレッションを獲得すると、Brazeはユーザーにメッセージを受け取る資格を与えることを停止します。[インプレッションの]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#setting-a-max-impression-cap)おおよその[上限]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#setting-a-max-impression-cap)設定についてはこちらをご覧ください。

IAMインプレッションキャップ][11]。

[6]: {% image_buster /assets/img_archive/uninstall_tracking_checkbox.png %}
[11]: {% image_buster /assets/img_archive/approx_limit_for_IAM.png %}
