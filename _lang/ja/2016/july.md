---
nav_title: 7月
page_order: 6
noindex: true
page_type: update
description: "この記事には2016年7月のリリースノートが含まれている。"
---

# 2016年7月

## エラータイプによる開発者コンソールのエラーログのフィルタリング

このアップグレードにより、開発者コンソールのメッセージエラーログを使用して、Braze 統合の問題をトラブルシューティングしやすくなります。これは、ユーザビリティ更新で、メッセージエラーログを種類別にフィルターし、具体的なインテグレーションの問題を簡単に見つけて特定することができます。

## 最後に送信されたアンインストール追跡プッシュのタイムスタンプを追加した。

Brazeは、顧客のアプリにサイレント・プッシュを送信し、どのデバイスが反応するかを確認することで、アンインストールを検知する。この機能により、アアンインストール追跡が最後に実行された日時を示す、目立たないタイムスタンプが追加されます。このタイムスタンプは、アンインストール追跡が設定されている「設定」ページで確認できる。詳細については、[トラッキングのアンインストール]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking)を参照してください。

![トラッキング・チェックボックスをアンインストールする]({% image_buster /assets/img_archive/uninstall_tracking_checkbox.png %})

## ウェブフック・テストの機能強化

キャンペーンを本番に設定する前に、Braze からライブ Webhook をテスト送信できるようになりました。テスト・メッセージを送信することで、安全なサンドボックス環境で、メッセージとサーバー・エンドポイントが適切に設定されていることを確認することができる。[webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#creating-a-webhook) について詳しく説明します。

## キャンペーン受信者のCSVエクスポートに受信メッセージのバリエーションを追加

キャンペーン受信者CSVエクスポートに、受信したメッセージのバリエーションを示すカラムを追加した。Brazeからの[データエクスポートについて]({{site.baseurl}}/user_guide/data/export_braze_data/)詳しく知る。

## インプレッション数のおおよその制限

アプリ内メッセージが一定数のインプレッションを獲得すると、Brazeはユーザーにメッセージを受け取る資格を与えることを停止する。インプレッションのおおよその制限の設定について詳しくは、[こちら]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#setting-a-max-impression-cap)をご覧ください。

![IAM インプレッション上限]({% image_buster /assets/img_archive/approx_limit_for_IAM.png %})

