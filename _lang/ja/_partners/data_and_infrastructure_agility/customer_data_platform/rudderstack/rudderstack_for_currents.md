---
nav_title: RudderStack for Currents
article_title:カレント用RudderStack
description:"この記事では、Braze Currentsと、Android、iOS、WebアプリケーションにシームレスにBraze統合を提供するオープンソースの顧客データインフラであるRudderStackとのパートナーシップについて概説する。"
page_type: partner
tool:Currents
search_tag:Partner

---

# カレント用RudderStack

> [RudderStackは](https://www.rudderstack.com/)、クラウドデータウェアハウスを真実のセントラルソースとして活用し、顧客データを収集、変換、活性化することを可能にする。この記事では、Braze CurrentsとRudderStackの接続設定方法の概要を説明する。

BrazeとRudderStackの統合により、Braze Currentsを活用してBrazeイベントをRudderStackにエクスポートし、より深い分析を推進することができる。

## 前提条件

| 必要条件 | 説明 |
| --- | --- |
| RudderStackアカウント | このパートナーシップを利用するには、[RudderStackアカウントが](https://app.rudderstack.com/login)必要である。 |
| 送信先 | RudderStackの送信[先としてBrazeを]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/rudderstack/rudderstack/#integration)設定しておくことをお勧めする。 |
| Currents | RudderStackにデータをエクスポートするには、アカウントに[Braze Currentsを]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)設定する必要がある。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ1:RudderStack内にBraze用のデータソースを作成する。

まず、RudderStackウェブアプリでBrazeソースを作成する必要がある。データソースの作成方法は、[RudderStackの](https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/braze-currents/)サイトに掲載されている。

完了すると、RudderStackは書き込みキーを含むWebhook URLを提供する。WebhookのURLは、Brazeソースの**設定**タブで確認できる。

### ステップ2:カレントを作成する

Brazeで、**Currents > + Create Currents > RudderStack Exportに**移動する。インテグレーション名、コンタクトメール、RudderStack Webhook URL（キーフィールドに入る）、RudderStackリージョンを入力する。 

### ステップ3:イベントをエクスポートする

次に、エクスポートしたいイベントを選択する。最後に、**Launch Currentsを**クリックする。

RudderStackに送信されるすべてのイベントには、ユーザーの`external_user_id` 。現時点では、Brazeは、`external_user_id` を設定していないユーザーに対しては、RudderStackにイベントデータを送信しない。

## 統合の詳細

Brazeは、[Currentsイベント用語集に]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents)記載されているすべてのデータをRudderStackにエクスポートすることをサポートしている。

エクスポートされたデータのペイロード構造は、カスタムHTTPコネクターのペイロード構造と同じで、[カスタムHTTPコネクターのサンプルリポジトリで](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors)見ることができる。