---
nav_title: RudderStack と Currents
article_title: RudderStack と Currents
description: "この記事では、Braze Currents と RudderStack のパートナーシップについて説明します。RudderStack は、Android、iOS、および Web アプリケーション向けのシームレスな Braze 統合を提供するオープンソースの顧客データインフラストラクチャです。"
page_type: partner
tool: Currents
search_tag: Partner

---

# RudderStack と Currents

> [RudderStack](https://www.rudderstack.com/) では、スタック全体で顧客データを収集、変換、アクティブ化し、クラウドデータウェアハウスを一元的な信頼できる情報源として活用することができます。この記事では、Braze Currents と RudderStack 間の接続を設定する方法の概要を説明します。

Braze と RudderStack の統合により、Braze Currents を利用して Braze イベントを RudderStack にエクスポートし、より深い分析を促進できます。

## 前提条件

| 必要条件 | 説明 |
| --- | --- |
| RudderStackアカウント | このパートナーシップを活用するには、[RudderStack アカウント](https://app.rudderstack.com/login)が必要です。 |
| Braze 宛先 | RudderStack で [Braze を宛先として設定する]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/rudderstack/rudderstack/#integration)ことをお勧めします。 |
| Currents | RudderStack にデータを再度エクスポートするには、アカウントに [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) を設定する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

### ステップ1:RudderStack 内でのBrazeのデータソースの作成

まず、RudderStack Web アプリで Braze ソースを作成する必要があります。データソースの作成手順は、[RudderStack](https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/braze-currents/) サイトにあります。

この作業が完了すると、Rudderstack から Webhook URL が提供されます。この URL に含まれている書き込みキーは、次のステップで使用する必要があります。WebhookのURLは、Braze元の**Settings**タブにあります。

### ステップ2:現在の作成

Braze で **[Currents] > [+ Currents を作成] > [RudderStack のエクスポート]** に移動します。統合名、連絡先メール、RudderStack Webhook URL (キーフィールドに表示されます)、およびRudderStack リージョンを指定します。 

### ステップ3:イベントのエクスポート

次に、書き出すイベントを選択します。最後に、**Launch Current**をクリックします。

RudderStack に送信されるすべてのイベントには、ユーザーの`external_user_id` が含まれます。この時点では Braze は、`external_user_id` が設定されていないユーザーのイベントデータを RudderStack に送信しません。

## 統合の詳細

Braze は、[Currents のイベント用語集]({{site.baseurl}}/user_guide/data/braze_currents/)に記載されているすべてのデータを RudderStack にエクスポートする操作をサポートしています。

エクスポートされたデータのペイロードの構造は、カスタム HTTP コネクターのペイロード構造と同じです。これは、[カスタム HTTP コネクターのサンプルリポジトリ](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors)で確認できます。