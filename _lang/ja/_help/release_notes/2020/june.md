---
nav_title: 6月
page_order: 7
noindex: true
page_type: update
description: "この記事には2020年6月のリリースノートが含まれている。"
---
# 2020年6月

## リテンションレポート

リテンションレポートが[キャンペーンと][2] [キャンバスの][1]リテンション範囲を提供するようになった。レンジ・リテンションは、特定の時間間隔の間に、何人のユーザーが戻ってきて、選択したリテンション・イベントを実行したかを測定する。 

## ユーザートラックAPIの更新

[`users/track` エンドポイントでは][3]、2020年6月2日以降に設立されたダッシュボード企業に対して、1分あたり50,000APIリクエストのデフォルトレートが設定された。この日以前に作成された既存の企業とそのワークスペースは、`users/track` エンドポイントへのAPIリクエストが無制限で許可されている。

Brazeは、当社のAPIとインフラの安定性と信頼性の目標に向けたステップとして、最も多用される顧客向けエンドポイントにこのデフォルトを課している。課される制限は非常に自由で、ダッシュボード会社とその通常業務に影響を与えるのはごくわずかだ。この限度額の増額が必要な場合は、カスタマーサクセスマネージャーまたはサポートチームまでご連絡ください。

[1]: {{site.baseurl}}/user_guide/engagement_tools/canvas/retention_reports/
[2]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/retention_reports/
[3]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
