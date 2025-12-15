---
nav_title: 6月
page_order: 7
noindex: true
page_type: update
description: "この記事には2020年6月のリリースノートが含まれています。"
---
# 2020年6月

## リテンションレポート

リテンションレポートは、[キャンペーン]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/retention_reports/)および[キャンバス]({{site.baseurl}}/user_guide/engagement_tools/canvas/retention_reports/)の範囲リテンションを提供するようになりました。日付範囲のリテンションは、特定の期間中に戻り、選択したリテンションイベントを実行するユーザーの数を測定します。 

## ユーザートラック API の更新

[`users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)のデフォルトレートは、2020年6月2日以降に作成されたダッシュボード会社で、1分あたり50,000 API リクエストです。この日付より前に作成された既存の企業とそのワークスペースは、`users/track`エンドポイントへの無制限のAPIリクエストが引き続き許可されます。

 Brazeは、APIおよびインフラの安定性と信頼性の目標に向けたステップとして、最も頻繁に使用される顧客向けエンドポイントにこのデフォルトを課しています。課せられる制限は非常に緩やかであり、ダッシュボード会社とその通常業務にはほとんど影響しません。この限度額の増額が必要な場合は、カスタマーサクセスマネージャーまたはサポートチームに連絡して増額を申請する。

