---
nav_title: 9月
page_order: 4
noindex: true
page_type: update
description: "この記事には、2017 年 9 月のリリースノートが含まれています。"
---

# 2017 年 9 月

## エンゲージメントレポートの新機能

[エンゲージメントレポートを使用して][72]、特定の期間のキャンペーンの指標を集計できるようになりました。たとえば、四半期ごとの開封数の合計や、キャンペーンやキャンバスの全期間におけるクリック数の合計をエクスポートできます。あなたがしなければならないのは、
-データをエクスポートする時間枠を選択し、
-定期的に1人または複数の受信者に送信するエンゲージメントレポートをスケジュールし、
-タグに基づいてキャンペーンとキャンバスをレポートに追加します。

## ユーザープロフィールページの更新

[ユーザープロフィールページが更新されました][73]。

## 却下するにはユーザーアクションが必要な Web プッシュ通知

Chrome ウェブプッシュのメッセージクローズ動作を設定できるようになりました。この動作では、受信者がメッセージを閉じるにはメッセージを操作する必要があります。この機能には、Web SDK バージョン 1.6.13 以降が必要です。

## メールプリヘッダー

Braze でメールメッセージを作成するときに、**送信情報セクションにプリヘッダーを簡単に挿入できるようになりました**。

## 未処理イベントのエクスポート用の新しい API エンドポイント

新しい [API エンドポイントを追加しました][71]。 /raw_data/status, that lets you query to see if a given day has been loaded into the Raw Event Export. You can use it to check if a particular day's raw data is available, to help with debugging and automation.



[71]: {{site.baseurl}}/developer_guide/rest_api/api_network_connectivity_issues/#whitelisting-brazes-api-endpoint-ip-ranges
[72]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#engagement-reports
[73]: {{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#using-user-search
[98]:{{site.baseurl}}/user_guide/onboarding/platform_administrative_features/#authentication-rules
