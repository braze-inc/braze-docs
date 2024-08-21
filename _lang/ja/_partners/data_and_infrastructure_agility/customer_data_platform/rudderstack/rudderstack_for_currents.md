---
nav_title: Currents用ラダースタック
article_title: Currents用ラダースタック
description: "本稿では、Android、iOS、およびウェブアプリのライセンスにシームレスなBrazeインテグレーションを提供する開封ソース顧客データ インフラであるBraze CurrentsとRudderStackの提携について概説します。"
page_type: partner
tool: Currents
search_tag: Partner

---

# Currents用ラダースタック

> [RudderStack](https://www.rudderstack.com/) では、クラウドデータウェアハウスを真理の中心的な源泉として活用することで、スタック全体で顧客データを収集、変換、アクティブ化することができます。ここでは、Braze Currents とRudderStack 間のコネクションの設定方法について説明します。

Braze とRudderStack の統合により、BrazeイベントをRudderStack にエクスポートするBraze Currentsを活用して、より深い分析を促進できます。

## 前提条件

| 要件 | 説明 |
| --- | --- |
| RudderStackアカウント | この提携の前倒しタグを行うには、[RudderStackアカウント](https://app.rudderstack.com/login)が必要です。 |
| Braze 送信先 | RudderStack では、[ Brazeを送信先]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/rudderstack/rudderstack/#integration) として設定することをお勧めします。 |
| Currents | RudderStack にデータをエクスポートするには、アカウントに[Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) を設定する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ1:RudderStack 内でのBrazeのデータソースの作成

まず、RudderStack ウェブアプリでBraze送信元を作成する必要があります。データソースの作成手順は、[RudderStack](https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/braze-currents/) サイトにあります。

完了すると、書き込みキーを含むWebhook URL が提供されます。これは、次回のステップで使用する必要があります。WebhookのURLは、Braze元の**Settings**タブにあります。

### ステップ2:現在の作成

Braze で、**Currents > + Create Current > RudderStack Export** に移動します。統合名、連絡先メール、RudderStack Webhook URL (キーフィールドに表示されます)、およびRudderStack リージョンを指定します。 

### ステップ3:イベントのエクスポート

次に、書き出すイベントを選択します。最後に、**Launch Current**をクリックします。

RudderStack に送信されるすべてのイベントには、ユーザーの`external_user_id` が含まれます。このとき、Braze は`external_user_id` が設定されていないユーザーに対して、イベントデータをRudderStack に送信しません。

## 統合の詳細

Braze は、[ Currentsイベント用語集]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents) にリストされているすべてのデータのRudderStack へのエクスポートをサポートしています。

エクスポートされたデータの給与読み込む構成は、カスタムHTTP コネクターの給与読み込む構成と同じです。カスタムHTTP コネクターの[サンプルリポジトリーで表示できます](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors)。