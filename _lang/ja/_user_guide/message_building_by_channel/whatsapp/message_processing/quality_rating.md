---
nav_title: 品質評価とメッセージ制限
article_title: 品質評価とメッセージ制限 
description: "この参考記事では、Meta が WhatsApp チャネルの品質評価とメッセージ制限にどのように影響するかについて説明します。"
page_type: partner
search_tag: Partner
page_order: 
channel:
  - WhatsApp
---

# 品質評価とメッセージ制限

> Meta は、WhatsApp チャネルの使用を開始した瞬間から品質評価と [メッセージ制限](https://developers.facebook.com/docs/whatsapp/messaging-limits) に影響を与え、WhatsApp の使用状況に応じて影響を与え続けます。

## 定義

| 単語 | 定義 |
| --- | --- |
| 品質評価 | 過去 7 日間に顧客が受信した最近のメッセージに基づく評価。この評価は、電話番号をブロックする理由やその他の報告の問題など、顧客からのフィードバックによって決定されます。[品質評価の詳細については](https://www.facebook.com/business/help/896873687365001)、Meta のドキュメントを参照してください。|
| メッセージング制限 | 24 時間以内に各電話番号で開始できるビジネス開始の会話の最大数。 |
{: .reset-td-br-1 .reset-td-br-2 }

## オンボーディング  

新しい WhatsApp Business アカウントが作成されると、Meta はさまざまな要素を使用して初期の送信制限を決定します。この制限は WhatsApp ビジネス マネージャーで確認でき、追加の詳細は電話番号インサイト ページに記載されています。 

[制限](https://developers.facebook.com/docs/whatsapp/messaging-limits#checking-your-limit) と [電話番号の要件](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers)を確認する方法の詳細については、Meta のドキュメントをご覧ください。

## スループット

Meta は、登録された各ビジネス電話番号に対して、1 秒あたり 80 件のメッセージのスループットを開始します。1 秒あたり 1,000 件のメッセージへのアップグレードは、自動的に、またはリクエストに応じて実行されます。情報。 

[スループットの](https://developers.facebook.com/docs/whatsapp/cloud-api/overview#throughput)詳細については、Meta のドキュメントを参照してください。

## テンプレートのペース

最近作成されたマーケティング テンプレートと一時停止が解除された一時停止中のマーケティング テンプレートは、ペース調整の対象となる可能性があります。Meta のペース選択基準は、主にテンプレートの品質履歴によって決まります。最近作成されたマーケティング テンプレート、または最近一時停止解除されたマーケティング テンプレートを使用すると、指定されていないしきい値に達するまでメッセージは通常どおり送信されます。このしきい値に達すると、そのテンプレートを使用する後続のメッセージは、顧客からのフィードバックに十分な時間を与えるために保留されます。 

[テンプレートのペース設定](https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/#template-pacing)の詳細については、Meta のドキュメントをご覧ください。