---
nav_title: 品質評価とメッセージング制限
article_title: 品質評価とメッセージング制限 
description: "この参考記事では、WhatsAppチャンネルの品質評価とメッセージ送信制限にMetaがどのように影響するかについて説明する。"
page_type: partner
search_tag: Partner
page_order: 
channel:
  - WhatsApp
---

# 品質評価とメッセージング制限

> MetaはWhatsAppチャンネルのご利用開始時から品質評価と[メッセージ送信制限に](https://developers.facebook.com/docs/whatsapp/messaging-limits)影響を与え、WhatsAppのご利用状況に応じて今後も影響を与え続ける。

## 定義

| 用語 | 定義 |
| --- | --- |
| 品質評価 | 過去 7 日間に顧客が受信した最近のメッセージに基づく評価。この評価は、御社の電話番号をブロックする理由やその他の問題報告など、顧客からのフィードバックによって決定されます。[品質評価](https://www.facebook.com/business/help/896873687365001)の詳細については、Meta のドキュメントを参照してください。|
| メッセージング制限 | 御社の各電話番号で移動期間 24 時間以内に企業側が開始できる会話の最大件数。 |
{: .reset-td-br-1 .reset-td-br-2 }

## オンボーディング  

WhatsAppビジネスアカウントを新規作成する際、Metaは様々な要素から初期送信上限を決定する。この上限はWhatsAppビジネスマネージャーで確認でき、詳細は電話番号インサイトページで確認できる。 

Metaのドキュメントを参照して、[制限の確認](https://developers.facebook.com/docs/whatsapp/messaging-limits#checking-your-limit)と[電話番号の要件](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers)について詳しく学んでください。

## スループット

Meta は、登録された企業の電話番号ごとに、メッセージ 80 件 / 秒のスループットで開始します。メッセージ 1,000 件 / 秒へのアップグレードは、自動的に、あるいはリクエストに応じて実行できます。情報。 

[スループット](https://developers.facebook.com/docs/whatsapp/cloud-api/overview#throughput)の詳細については、Meta のドキュメントを参照してください。

## テンプレートのペース配分

最近作成されたマーケティング・テンプレートや、一時停止していたマーケティング・テンプレートが一時停止されなくなった場合は、ペーシングの対象となる可能性がある。Meta のペーシング選択基準は、主にテンプレートの品質履歴によって決定されます。最近作成されたマーケティングテンプレートまたは最近停止されていないマーケティングテンプレートを使用する場合、指定されていないしきい値に達するまで、メッセージは通常通り送信される。このしきい値に達すると、そのテンプレートを使用する後続のメッセージが保留され、顧客からのフィードバックに十分な時間が与えられます。 

[テンプレートペーシング](https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/#template-pacing)の詳細については、Meta のドキュメントを参照してください。