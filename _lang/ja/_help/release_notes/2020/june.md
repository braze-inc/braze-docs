---
nav_title: "6"
page_order: 7
noindex: true
page_type: update
description: "この記事には、2020 年 6 月のリリース ノートが含まれています。"
---
# 2020年6月

## 保持レポート

保持レポートでは、 [キャンペーン][2] と [キャンバス][1]の範囲保持が提供されるようになりました。範囲保持は、特定の時間間隔内に戻って選択した保持イベントを実行するユーザーの数を測定します。 

## ユーザートラックAPIの更新

の [`users/track`][3] 2020 年 6 月 2 日以降に作成されたダッシュボード会社の場合、エンドポイントのデフォルト レートは 1 分あたり 50,000 件の API リクエストになりました。この日付より前に作成された既存の会社とそのワークスペースには、無制限のAPIリクエストが引き続き許可されます。 `users/track` 終点。

Braze は、API とインフラストラクチャの安定性と信頼性の目標に向けた一歩として、最も頻繁に使用される顧客向けエンドポイントにこのデフォルトを適用しています。課せられた制限は非常に緩やかであり、ダッシュボード企業とその通常業務に影響を及ぼすのはごくわずかです。この制限を増やす必要がある場合は、カスタマー サクセス マネージャーまたはサポート チームに連絡して、増加をリクエストしてください。

[1]: {{site.baseurl}}/user_guide/engagement_tools/canvas/retention_reports/
[2]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/retention_reports/
[3]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
