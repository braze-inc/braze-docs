---
nav_title: 7月
page_order: 6
noindex: true
page_type: update
description: "この記事には2016年7月のリリースノートが含まれている。"
---

# 2016年7月

## エラータイプ別にDeveloper Consoleのエラーログをフィルタリングする

このアップグレードにより、Developer Consoleのメッセージエラーログを使用して、Brazeの統合に関する問題のトラブルシューティングが容易になる。これはユーザビリティのアップデートであり、メッセージエラーログをタイプ別にフィルタリングすることができる。

## 最後に送信されたアンインストール追跡プッシュのタイムスタンプを追加した。

Brazeは、顧客のアプリにサイレント・プッシュを送信し、どのデバイスが反応するかを確認することで、アンインストールを検知する。この機能は、アンインストールトラッキングが最後に実行された日時を示すタイムスタンプを控えめに追加する。このタイムスタンプは、アンインストール追跡が設定されている「設定」ページで確認できる。[アンインストール・トラッキングについて]({{site.baseurl}}/user_guide/data_and_analytics/uninstall_tracking/#uninstall-tracking)もっと知る。

![トラッキング・チェックボックスをアンインストールする][6]

## ウェブフック・テストの機能強化

Brazeからライブウェブフックメッセージをテスト送信できるようになった。テスト・メッセージを送信することで、安全なサンドボックス環境で、メッセージとサーバー・エンドポイントが適切に設定されていることを確認することができる。[ウェブフックについて]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#creating-a-webhook)もっと知る。

## キャンペーン受信者のCSVエクスポートに受信メッセージのバリエーションを追加

キャンペーン受信者CSVエクスポートに、受信したメッセージのバリエーションを示すカラムを追加した。Brazeからの[データエクスポートについて]({{site.baseurl}}/user_guide/data_and_analytics/exporting_dashboard_data/#exporting-dashboard-data)詳しく知る。

## インプレッション数のおおよその制限

アプリ内メッセージが一定数のインプレッションを獲得すると、Brazeはユーザーにメッセージを受け取る資格を与えることを停止する。設定 アプリ roximate [インプレッション s]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#setting-a-max-impression-cap) の制限について詳しく説明します。

![IAMインプレッションキャップ][11]

[6]: {% image_buster /assets/img_archive/uninstall_tracking_checkbox.png %}
[11]: {% image_buster /assets/img_archive/approx_limit_for_IAM.png %}
