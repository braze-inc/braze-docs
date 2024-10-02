---
nav_title: 品質評価とメッセージ送信の制限
article_title: 品質評価とメッセージ送信の制限 
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

| 単語 | 定義 |
| --- | --- |
| 品質評価 | 過去7日間にあなたの顧客が受け取った最近のメッセージに基づく評価。この評価は、あなたの電話番号をブロックする理由やその他の報告事項など、顧客からのフィードバックによって決定される。[品質評価の](https://www.facebook.com/business/help/896873687365001)詳細については、Metaのドキュメントを参照のこと。|
| メッセージ送信制限 | 24時間以内に各電話番号で開始できる業務上の会話の最大数。 |
{: .reset-td-br-1 .reset-td-br-2 }

## オンボーディング  

WhatsAppビジネスアカウントを新規作成する際、Metaは様々な要素から初期送信上限を決定する。この上限はWhatsAppビジネスマネージャーで確認でき、詳細は電話番号インサイトページで確認できる。 

Metaのドキュメントを参照して、[制限の確認](https://developers.facebook.com/docs/whatsapp/messaging-limits#checking-your-limit)と[電話番号の要件](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers)について詳しく学んでください。

## スループット

Metaは、登録されたビジネス電話番号ごとに、1秒間に80通のスループットで開始する。毎秒1,000メッセージへのアップグレードは、自動的に、あるいはリクエストに応じて行われる。情報だ。 

[スループットの](https://developers.facebook.com/docs/whatsapp/cloud-api/overview#throughput)詳細については、Metaのドキュメントを参照のこと。

## テンプレートのペース配分

最近作成されたマーケティング・テンプレートや、一時停止していたマーケティング・テンプレートが一時停止されなくなった場合は、ペーシングの対象となる可能性がある。メタのペース選択基準は、主にテンプレートの品質履歴によって決定される。最近作成されたマーケティングテンプレートまたは最近停止されていないマーケティングテンプレートを使用する場合、指定されていないしきい値に達するまで、メッセージは通常通り送信される。この閾値に達した後、そのテンプレートを使用した以降のメッセージは、顧客からのフィードバックを得るための十分な時間を確保するために保留される。 

[テンプレートのペーシングの](https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/#template-pacing)詳細については、Metaのドキュメントを参照のこと。