---
nav_title: 6月
page_order: 7
noindex: true
page_type: update
description: "この記事には2020年6月のリリースノートが含まれています。"
---
# 2020年6月

## リテンションレポート

リテンションレポートは、[キャンペーン][2]および[キャンバス][1]の範囲リテンションを提供するようになりました。日付範囲のリテンションは、特定の期間中に戻り、選択したリテンションイベントを実行するユーザーの数を測定します。 

## ユーザートラック API の更新

[`users/track` エンドポイント][3]のデフォルトレートは、2020年6月2日以降に作成されたダッシュボード会社で、1分あたり50,000 API リクエストです。この日付より前に作成された既存の企業とそのワークスペースは、`users/track`エンドポイントへの無制限のAPIリクエストが引き続き許可されます。

Brazeは、APIおよびインフラの安定性と信頼性の目標に向けたステップとして、最も頻繁に使用される顧客向けエンドポイントにこのデフォルトを課しています。課せられる制限は非常に緩やかであり、ダッシュボード会社とその通常業務にはほとんど影響しません。この制限を引き上げる必要がある場合は、カスタマーサクセスマネージャーまたはサポートチームに連絡し、引き上げをリクエストしてください。

[1]: {{site.baseurl}}/user_guide/engagement_tools/canvas/retention_reports/
[2]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/retention_reports/
[3]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
