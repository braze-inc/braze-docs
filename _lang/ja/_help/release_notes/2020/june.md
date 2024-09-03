---
nav_title: 6月
page_order: 7
noindex: true
page_type: update
description: "この記事には2020年6月のリリースノートが含まれています。"
---
# 2020年6月

## リテンションレポート

リテンションレポートは、[キャンペーン][2]および[キャンバス][1]の範囲リテンションを提供するようになりました。範囲リテンションは、特定の時間間隔で選択されたリテンションイベントを実行するために何人のユーザーが戻ってくるかを測定します。 

## ユーザー トラック API 更新

[`users/track`エンドポイント][3]は現在、2020年6月2日以降に作成されたダッシュボード会社に対して、デフォルトのレートとして1分あたり50,000のAPIリクエストを持っています。この日付より前に作成された既存の企業とそのワークスペースは、`users/track`エンドポイントへの無制限のAPIリクエストが引き続き許可されます。

Brazeは、APIおよびインフラの安定性と信頼性の目標に向けたステップとして、最も頻繁に使用される顧客向けエンドポイントにこのデフォルトを課しています。課せられた制限は非常に自由であり、ダッシュボード企業やその通常の運営に影響を与えることはほとんどありません。この制限の引き上げが必要な場合は、顧客成功マネージャーまたはサポートチームに連絡して引き上げをリクエストしてください。

[1]: {{site.baseurl}}/user_guide/engagement_tools/canvas/retention_reports/
[2]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/retention_reports/
[3]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
