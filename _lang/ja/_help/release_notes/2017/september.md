---
nav_title: 9月
page_order: 4
noindex: true
page_type: update
description: "この記事には2017年9月のリリースノートが含まれています。"
---

# 2017年9月

## エンゲージメントレポートの新機能

特定の期間にわたってキャンペーンの指標を集計するために[エンゲージメントレポート][72]を使用できるようになりました。例えば、四半期の開封総数や、キャンペーンまたはキャンバスの全期間のクリック総数をエクスポートできます。あなたがしなければならないのは:
- データをエクスポートする期間を選択してください。
- スケジュール an エンゲージメント レポート that sends to one or more recipients on a regular basis, and
- タグに基づいてキャンペーンとキャンバスをレポートに追加します。

## ユーザープロファイルページの更新

[ユーザープロファイルページ][73]が更新されました。

## ユーザーのアクションが必要なWebプッシュ通知

Chrome Web プッシュのメッセージ終了動作を設定できるようになり、受信者がメッセージを閉じるためにメッセージと対話する必要があります。この機能にはWeb SDKバージョン1.6.13以上が必要です。

## メールのプリアンカー

Braze内でメールメッセージを作成する際、**送信情報**セクションにプレヘッダーを簡単に挿入できるようになりました。

## 生のイベントエクスポート用の新しいAPIエンドポイント

新しい[APIエンドポイント][71]、/raw_data/ステータスを追加しました。これにより、指定された日がRaw Event Exportにロードされているかどうかをクエリで確認できます。デバッグとオートメーションを支援するために、特定の日の生データが利用可能かどうかを確認するために使用できます。



[71]: {{site.baseurl}}/developer_guide/rest_api/api_network_connectivity_issues/#whitelisting-brazes-api-endpoint-ip-ranges
[72]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#engagement-reports
[73]: {{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#using-user-search
[98]:{{site.baseurl}}/user_guide/onboarding/platform_administrative_features/#authentication-rules
