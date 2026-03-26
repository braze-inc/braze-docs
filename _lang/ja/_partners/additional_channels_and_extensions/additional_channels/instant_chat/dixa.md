---
nav_title: Dixa
article_title: Dixa
description: "この記事では、Braze と Dixa のパートナーシップについて概説します。"
alias: /partners/dixa/
page_type: partner
search_tag: Partner

---

# Dixa

> [Dixa](https://www.dixa.com/) は、チャット、メール、電話、ソーシャルメディアなどのコミュニケーションチャネルを単一のインターフェイスに統合することで、サポート体験を向上させるように設計された顧客サービスプラットフォームです。インテリジェントなルーティング、オートメーション、リアルタイムのパフォーマンスインサイトを通じて、企業が顧客満足度と効率性を向上させるのを支援します。

Braze と Dixa の統合により、カスタマーサービス担当者にリアルタイムの Braze データを提供することで、すべてのユーザーをより良く把握することができます。

## 前提条件

開始する前に、以下が必要です。

| 前提条件          | 説明                                                                                                                                                       |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Dixa のアカウント        | このパートナーシップを活用するには、Dixa 管理者アカウントが必要です。                                                                                           |
| Braze REST API キー  | `users.export.ids` および `email.status` 権限を持つ Braze REST API キー。<br><br> これは、Braze ダッシュボードの [**設定**] > [**API キー**] から作成できます。 |
| Braze REST エンドポイント | [REST エンドポイントの URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。エンドポイントは、お客様のインスタンスの Braze URL に依存します。              |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ユースケース

メール、Messenger、チャットなどのさまざまな通信チャネルでユーザーとコミュニケーションしている間に、Braze データをカスタマーサービスエージェントビューに表示します。さらに、Braze のデータ変換を使用して Dixa から Braze にデータを送信し、ユーザーの問題を解決している間はマーケティングを一時停止することもできます。

## 統合

Dixa 内で統合を設定するには、Dixa 管理者である必要があります。Braze との統合は、Dixa で [**設定**] > [**統合**] > [**Braze**] に移動します。

![Dixa の Braze ウィジェット作成ページ。ウィジェット名、API URL、API キーを入力します。]({% image_buster /assets/img/dixa/dixa-create-integration.png %}){: style="width:450px;"}

### ステップ 1:Dixa で統合を作成する

**Braze ウィジェットの作成**ページで、以下の必須フィールドに入力して統合を作成します。

- **ウィジェット名:**これは、後に会話サイドバーでタイトルとして使用される統合の名前です。
- **API URL:**インスタンスの Braze REST API エンドポイント URL です。
- **API キー:**これは、前提条件で作成した Braze API キーです。

### ステップ 2:統合を設定する

次に、Braze と Dixa の統合を設定します。会話サイドバーの Braze ウィジェットの表示を調整するには、以下のオプションから選択します。

#### 会話サイドバーにウィジェットを表示する

この設定は、Dixa の会話サイドバー内の統合全体を表示または非表示にします。 

統合の設定を行っている場合は、必須フィールドに入力する間、これをオフにすることをお勧めします。設定が完了したら、再びオンにすることで、Dixa のエージェントが統合を使用できるようになります。

#### 顧客の詳細を表示する

ユーザーの詳細を表示するか非表示にするかを選択します。詳細には、ロケーション、メール、電話番号、メールサブスクリプションの状態、プッシュ通知サブスクリプションの状態、Braze の会員期間に関するデータが含まれます。 

#### メールサブスクリプションの状態を変更するボタンを表示する

ボタンは、`subscribed`、`opted-in`、`unsubscribed` という Braze の3つのサブスクリプション状態のいずれかに基づいています。ユーザーが `subscribed` の場合、エージェントは `opt-in` または `unsubscribe` を選択できます。ユーザーが `opted-in` または `unsubscribed` の場合、エージェントはこの2つの間でのみ切り替えることができます。

#### カスタム属性のリストを表示する

ユーザーのカスタム Braze 属性の表示・非表示を選択します。

#### カスタムイベントのリストを表示する

ユーザーのカスタム Braze イベントの表示・非表示を選択します。

#### 購入リストを表示する

ユーザーが購入した製品リストの表示・非表示を選択します。ここでは、ユーザーがその製品を何回購入したかを確認できます。最初の購入日と最後の購入日を表示するには、アイテムにカーソルを合わせます。 

### 統合の例

以下に統合の例を示します。

![ユーザーのメールサブスクリプション状態、カスタム属性、カスタムイベント、購入を表示する Dixa での Braze と Dixa の統合。]({% image_buster /assets/img/dixa/dixa-braze-integration.png %}){: style="width:350px;"}

## データ変換ツール

Dixa は Webhook を使用して Braze にデータを送信します。Webhook を設定するには、Dixa 管理者である必要があります。

最初のステップは、Braze でデータ変換を作成することです。 

1. [**データ設定**] > [**データ変換**] > [**変換を作成**] に移動します。
2. [**ゼロから開始**] を選択し、送信先として **POST: Track Users** を選択して、[**変換を作成**] を選択します。
3. 変換エディターで、以下の**データ変換ツールの例**からコードをコピーし、[**変換コード**] フィールドに挿入します。[**保存**] を選択し、**Webhook URL** をコピーして、Dixa を開きます。
4. Dixa で、[**設定**] > [**統合**] > [**Webhooks**] > [**+ アウトバウンド Webhook**] に移動します。
5. Webhook 設定ページで、Braze からコピーした URL を貼り付け、追跡したいイベントをトグルで有効にします。**Conversation created** は、顧客の会話を追跡するための良い出発点です。 
6. [**保存**] を選択して Dixa のセットアップを完了します。

### データ変換ツールの例

```js
// Transforming the provided payload to match Braze /users/track endpoint specifications.

// Extracting necessary details from the payload
const requester = payload.data.conversation.requester;
const event = payload.data.conversation;

// Defining user attributes based on the provided payload, prioritizing email if available.
const userAttributes = {
  email: requester.email, // Prioritizing email over external_id and user_alias
  _update_existing_only: false, // Set to false to create or update user profiles when identified by email
  organization: payload.organization.name, // Including an additional attribute for demonstration
};

// Defining event attributes based on the provided payload.
const eventAttributes = {
  email: requester.email, // Prioritizing email over external_id and user_alias
  name: payload.event_fqn, // The name of the event
  time: event.created_at, // ISO 8601 datetime format
  properties: { // Including additional event properties
    event_version: payload.event_version,
    conversation_status: event.status,
    conversation_channel: event.channel
  },
  _update_existing_only: false // Set to false to create or update user profiles when identified by email
};

// Constructing the final object to match Braze /users/track endpoint schema
const brazecall = {
  attributes: [userAttributes], // Wrapping userAttributes in an array as per specifications
  events: [eventAttributes] // Wrapping eventAttributes in an array as per specifications
};

// Returning the transformed data
return brazecall;
```
