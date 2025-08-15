---
nav_title: Regal
article_title: Regal
description: "このリファレンス記事では、BrazeとRegalのパートナーシップについて説明しています。Regalは電話およびSMSの販売ソリューションであり、両方のソースからのデータを使用して顧客にパーソナライズされた体験を提供することができます。"
alias: /partners/regal/
page_type: partner
search_tag: Partner

---

# Regal

> [Regal.io](https://regal.io) は、より多くの会話を促進するために構築された電話および SMS セールスソリューションです。これにより、成長目標をより短期間で達成できるようになります。

Regal と Braze の統合により、すべての顧客タッチポイントでより一貫性がありパーソナライズされたエクスペリエンスを作成できます。
- Regal での電話による会話の内容に基づいて、Braze から適切なネクストベストのメールまたはプッシュ通知を送信します。
- 価値の高い顧客が Braze からのマーケティングメールをクリックスルーしたがコンバージョンに至らなかった場合に、Regal でコールをトリガーします。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Regal アカウント | このパートナーシップを活用するには、Regal アカウントが必要です。 |
| リーガル API キー | RegalのAPIキーを使用すると、BrazeからRegalにイベントを送信できます。<br><br>このキーを取得するには、[support@regal.io](mailto:support@regal.io) までメールでご連絡ください。 |
| Braze Data Transformation | Data Transformation は現在早期アクセス段階です。早期アクセスへの参加に興味がある場合は、Braze カスタマーサクセスマネージャーにお問い合わせください。これは、Regal からデータを受信するために必要です。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合:BrazeからRegalにデータを送信する

次のセクションでは、Braze キャンバスまたはキャンペーン Webhook を使用して顧客プロファイルとイベントデータを Regal に送信するためのソースとして Braze を使用する方法について説明します。

### ステップ1:Regalで新しい連絡先を作成する

Braze で作成される新しい連絡先を Regal でのコールやテキストに利用できるようにするには、Braze でこのような連絡先が作成されるたびに Webhook で Regal に通知するキャンバスまたはキャンペーンを作成します。 

1. 「Regalの新しい連絡先を作成」と題されたキャンバスまたはキャンペーンを作成し、エントリタイプとして**アクションベース**を選択します。

2. トリガーロジックを**カスタムイベント**として、電話番号を持つ連絡先が作成されたときに発生するイベントを選択します。Regal では、電話番号が確実に設定されるようにするため、電話番号フィールドにフィルターを追加することも推奨されています。

3. 新しいWebhookテンプレートに、次のフィールドに記入してください:
   - **Webhook URL**: <https://events.regalvoice.com/events>
   - **リクエスト本文**:Raw Text

#### リクエストヘッダと方法

Regal.io には、認証用の HTTP ヘッダーと HTTP メソッドが必要です。次の内容は、**設定**タブのキーと値のペアとして既にテンプレートに含まれています:
{% raw %}
- **HTTPメソッド**：POST
- **リクエストヘッダー**:
    - **Authorization**: `{{<REGAL_API_KEY>}}`
    - **Content-Type**: application/json
{% endraw %}

#### Request body

以下の唯一の必須フィールドは`traits.phone`プロパティです。残りはオプションです。ただし `optIn` を含める場合は、`optIn.channel` と `optIn.subscribed` を含める必要があります。

```json
{
    "userId": "<uniqueIdentifier>", //this is optional
    "traits": {
        "phone": "<phoneNumber>",
        "email": "<email>",
        "firstName": "<firstName>",
        "lastName": "<lastName>",
        "optIn": [
            {
                "channel": "voice",
                "source": "<leadSource>",
                "subscribed": true
            },
            {
                "channel": "sms",
                "source": "<leadSource>",
                "subscribed": true
            }
        ],
        "custom1": "<custom1>",
        "custom2": "<custom2>"
    },
    "eventSource": "braze"
}
```

上記のペイロードの例は、すべての連絡先が音声と SMS のオプトインに同意していることを前提としています。これに該当しない場合は、上記の `optIn` プロパティを削除し、`optIn` が収集されたときに Regal で連絡先を更新する別のキャンバスまたはキャンペーンを設定できます。

### ステップ2:オプトイン情報を更新 

お客様のアプリのユーザーエクスペリエンスのさまざまな部分でオプトインおよびオプトアウトが発生する可能性がある場合、ユーザーがオプトインまたはオプトアウトするたびにRegalを更新することが重要です。以下は、Regalに最新のオプトイン情報を送信するための推奨キャンバスです。これを Braze プロファイルのフィールドとして保存することを前提としていますが、保存されていない場合、トリガーは、Braze アカウントでユーザーがオプトインまたはサブスクリプション解除したことを表すイベントと同じくらい容易です。（以下の例は電話のオプトイン用ですが、キャンバスまたはキャンペーンを設定して、SMSオプトインを別々に収集することもできます）。

1. 新しいキャンバスまたはキャンペーンを作成して「Send Opt In or Out to Regal」というタイトルを付けます。

2. 次のトリガーオプションのいずれかを選択し、ユーザーのオプトインステータスを表すフィールドを選択します。オプトインまたはオプトアウトを表すイベントをBrazeに送信する場合は、そのイベントをトリガーとして使用してください。
    - ユーザープロファイルフィールド更新済み
    - 更新サブスクリプショングループステータス
    - サブスクリプション ステータス

3. 新しいWebhookテンプレートに、次のフィールドに記入してください:
   - **Webhook URL**: <https://events.regalvoice.com/events>
   - **リクエスト本文**:Raw Text

#### リクエストヘッダと方法

Regal.io には、認証用の HTTP ヘッダーと HTTP メソッドが必要です。次の内容は、テンプレート内にキーと値のペアとして既に含まれていますが、**設定**タブにあります:
{% raw %}
- **HTTPメソッド**：POST
- **リクエストヘッダー**:
    - **Authorization**: `{{<REGAL_API_KEY>}}`
    - **Content-Type**: application/json
{% endraw %}

#### Request body

必要に応じて、追加のユーザープロファイル属性をこのペイロードに追加して、複数の属性が同時に最新の状態であることを確認することもできます。

```json
{
    "userId": "<uniqueIdentifier>", //this is optional
    "traits": {
        "phone": "<phoneNumber>",
        "optIn": [
            {
                "channel": "voice",
                "source": "<leadSource>",
                "subscribed": "<voice_optin_subscribed>"
            },
            {
                "channel": "sms",
                "source": "<leadSource>",
                "subscribed": "<voice_optin_subscribed>"
            }
        ]
    },
    "eventSource": "braze"
}
```

### ステップ3:カスタムイベントを送信

最後に、Regal を送信するキーイベントごとにキャンバスまたはキャンペーンを設定します。Regal では、Regal で SMS および通話をトリガーするうえで重要なすべてのイベント (登録フローまたは購入フローの各ステップでのイベントなど) を送信することが推奨されています。このようにしない場合、それは連絡先が Regal キャンペーンの対象外となる終了基準として使用されます。

例えば、以下はユーザーがアプリケーションの最初のステップを完了したときにRegalにイベントを送信するためのワークフローです。

1. 新しいキャンバスまたはキャンペーンを作成して、「Send Application Step 1 Completed Event to Regal」というタイトルを付けます。

2. トリガーノードのロジックを**カスタムイベント**として、Regalに送信したいイベント名を選択します。例えば、「アプリケーションステップ1完了」などです。

3. 新しいWebhookテンプレートに、次のフィールドに記入してください:
   - **Webhook URL**: <https://events.regalvoice.com/events>
   - **リクエスト本文**:Raw Text

#### リクエストヘッダと方法

Regal.io には、認証用の HTTP ヘッダーと HTTP メソッドが必要です。次の内容は、テンプレート内にキーと値のペアとして既に含まれていますが、**設定**タブにあります:
{% raw %}
- **HTTPメソッド**：POST
- **リクエストヘッダー**:
    - **Authorization**: `{{<REGAL_API_KEY>}}`
    - **Content-Type**: application/json
{% endraw %}

#### Request body

必要に応じて、このペイロードに追加のユーザープロファイル属性を追加して、複数の属性が同時に最新であることを確認できます。

```json
{
    "userId": "<uniqueIdentifier>", //this is optional
    "traits": {
        "phone": "<phoneNumber>",
        "firstName": "<firstName>",
        "lastName": "<lastName>",
        "custom1": "<custom1>",
        "custom2": "<custom2>",
        "custom3": "<custom3>"
    },
    "name": "Application Step 1 Completed",
    "properties": {
      "educationalLevel": "<educationalLevel>",
      "preferredLocation": "<preferredLocation>",
      "preferredSubject": "<preferredSubject>",
      "readytoCommit": true
    },
    "eventSource": "braze"
}
```

#### 最新の連絡先属性

これは必須ではありませんが、Regal では、キーイベントが利用可能になった時点で Regal が最新の連絡先属性にアクセスできるようにするために、イベントワークフローのイベントペイロードの主要なユーザープロファイルデータを送信することが推奨されています。

{% alert note %}
Regal に送信する重要なイベント、またはこれらのキャンバスとキャンペーンの設定方法についてご質問がある場合は、support@regal.io にお問い合わせください。
{% endalert %}

## 統合:RegalからBrazeにデータを送信する

このセクションでは、`SMS.sent`や`call.completed`などのRegalレポートイベントをBrazeに取り込み、Brazeプロファイルに表示され、Brazeのセグメンテーションツール、キャンバス、およびキャンペーンで利用できるようにする方法について説明します。この統合では、Regal Reporting Webhook と Braze Data Transformation を使用してデータフローを自動化します。

### ステップ1:Braze で Data Transformation を作成する

{% alert important %}
Data Transformation は現在早期アクセス段階です。早期アクセスへの参加に興味がある場合は、Braze カスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

Brazeは、Brazeに送信する予定のRegal Webhookごとに変換を作成することをお勧めします。 

Data Transformation を作成するには、次のようにします。
1. Braze ダッシュボードの**Transformations**ページに移動します。
2. 変換に名前を付けて、**変換を作成**をクリックします。
3. 変換のリストから、<i class="fa-solid fa-ellipsis-vertical" title="アクションを表示"></i>をクリックし、**Webhook URLをコピー**を選択します。

![]({% image_buster /assets/img/regal/copy_webhook_url.png %})

### ステップ2: Regalでレポートwebhookを有効にする

レポートwebhookを設定するには:
1. Regalアプリに移動して、**設定**ページを開きます。

2. 「**レポートWebhook**」セクションで、「**Webhookを作成**」をクリックします。

3. Webhook エンドポイント入力で、関連付けられたData Transformation の Braze Data Transformation Webhook URL を追加します。

![]({% image_buster /assets/img/regal/edit_webhook.png %}){: style="max-width:60%;"}

#### エンドポイントの更新
エンドポイントを編集すると、キャッシュが更新されて新しいエンドポイントにイベントが送信されるまでに最大で5分かかることがあります。
#### 再試行
現在、これらのイベントに再試行はありません。応答が5秒以内に受信されない場合、イベントは破棄され、再試行されません。Regal は今後のリリースで再試行を追加する予定です。
#### イベント
Regalの [Reporting Webhooks ガイド](https://developer.regal.io/docs/reporting-webhooks#events)には、公開する Reporting イベントの完全なリストが含まれています。そこでは、プロパティの定義やサンプルペイロードも見ることができます。

### ステップ3:Regal イベントを Braze イベントに変換する

Braze の [データ変換]({{site.baseurl}}/data_transformation)機能を使用すると、受信した Regal イベントを、Braze で属性、イベント、または購入として追加するのに必要な形式にマッピングできます。

1. Data Transformation に名前を付けてください。イベント Webhook ごとに Data Transformation を設定することをお勧めします。

2. 接続をテストするには、Regal Agent Desktop から携帯電話への発信コールを作成し、Conversation Summary フォームを送信して call.completed イベントを作成します。

3. Regal の連絡先を Braze プロファイルにマッピングするために使用する識別子を決定します。Regalイベントで利用可能な識別子には以下が含まれます：
   - `userId` - イベントにのみ設定されますが、この識別子を以前に連絡先に送信した場合に限ります
   - `traits.phone`
   - `traits.email` - イベントにのみ設定されますが、この識別子を以前に連絡先に送信した場合に限ります

#### Braze対応の識別子
- Brazeは識別子として電話番号をサポートしていません。これを識別子として使用するには、Braze で電話番号を[ユーザーエイリアス]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)として設定できます。
- Braze Data Transformation を使用する場合、メールアドレスを識別子として使用できます。メールアドレスがBraze内のプロファイルとして存在する場合、既存のプロファイルが更新されます。メールアドレスがBraze内にまだ存在しない場合、メール専用のプロファイルが作成されます。

## ユースケース

{% tabs %}
{% tab メールをトリガーする %}

**Regal でのコール処理に基づいて、Braze からメールをトリガーする**

以下は、Regalの`call.completed`イベントのサンプルペイロードです。 

```json
{
  "userId": "123",
  "traits": {
    "phone": "+17625555555",
    "email": "xxx@gmail.com"
  },
  "name": "call.completed",
  "properties": {
    "agent_firstname": "Rebecca",
    "agent_fullname": "Rebecca Greene",
    "agent_id": "xxxx@yourbrand.com",
    "direction": "OUTBOUND",
    "regal_voice_phone": "+19545558563",
    "regal_voice_phone_internal_name": "Sales Line",
    "contact_phone": "+17625555555",
    "call_id": "WTxxxxx9",
    "type": "Outbound Call",
    "disposition": "Converted During Convo",
    "notes": null,
    "objections": null,
    "campaign_name": "Life Insurance Quote Follow Up",
    "campaign_friendly_id": "445",
    "started_at": 1657855046,
    "ended_at": 1657855053,
    "completed_at": 1657855059,
    "talk_time": 7,
    "wrapup_time": 6,
    "handle_time": 13,
    "journey_uuid": null,
    "journey_name": null,
    "journey_friendly_id": null
  },
  "originalTimestamp": "1657855059",
  "eventSource": "Regal Voice"
}
```

以下は、これをBrazeのカスタムイベントにマッピングするためのサンプルデータ変換です。

```
// The Braze /users/track endpoint expects timestamps in an ISO 8601 format. To use the Unix timestamp within Regal's call.completed event payload as the event timestamp in Braze must first be converted to ISO 8601. This can be done with the following code:
let unixTimestamp = payload.originalTimestamp;
let dateObj = new Date(unixTimestamp * 1000);
let isoString = dateObj.toISOString();

// This is a default template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z

let brazecall = {
 "events": [
   {
     "external_id": payload.userId,
     "name": "Call Completed",
     "time": isoString,
     "_update_existing_only": false,
     "properties": {
       "agent_firstname": payload.properties.agent_firstname,
       "agent_fullname": payload.properties.agent_fullname,
       "agent_id": payload.properties.agent_id,
       "direction": payload.properties.direction,
       "regal_voice_phone": payload.properties.regal_voice_phone,
       "regal_voice_phone_internal_name": payload.properties.regal_voice_phone_internal_name,
       "contact_phone": payload.properties.contact_phone,
       "call_id": payload.properties.call_id,
       "type": payload.properties.type,
       "disposition": payload.properties.disposition,
       "notes": payload.properties.notes,
       "objections": payload.properties.objections,
       "campaign_name": payload.properties.campaign_name,
       "campaign_friendly_id": payload.properties.campaign_friendly_id,
       "started_at": payload.properties.started_at,
       "ended_at": payload.properties.ended_at,
       "completed_at": payload.properties.completed_at,
       "talk_time": payload.properties.talk_time,
       "wrapup_time": payload.properties.wrapup_time,
       "handle_time": payload.properties.handle_time,
       "journey_uuid": payload.properties.journey_uuid,
       "journey_name": payload.properties.journey_name,
       "journey_friendly_id": payload.properties.journey_friendly_id
     }
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{% endtab %}
{% tab プロファイル属性を更新する %}

**Regalからの `contact.attribute.edited` イベントに基づいて、Braze のプロファイル属性を更新する**

以下は、Regalの`contact.attribute.edited`イベントのサンプルペイロードです。このイベントは、いずれかのエージェントが会話で新しい情報を得て、連絡先のプロファイルの属性を更新するたびにトリガーされます。

```json
{
  "userId": "123",
  "traits": {
    "phone": "+17625555555",
    "email": "xxx@gmail.com",
  },
  "name": "contact.attribute.edited",
  "properties": {
    "agent_email": "xxxx@yourbrand.com",
    "contact_phone": "+17625555555",
    "changes": {
      "custom_properties": {
        "annual_income": {
          "old_value": "150,000",
          "new_value": "300,000"
        }
      }
    },
    "created_at": "1657855462"
  },
  "originalTimestamp": "1657855462",
  "eventSource": "Regal Voice"
}
```

以下は、Brazeプロファイルの関連属性に新しいカスタムプロパティ値をマッピングするためのサンプルデータ変換です:

```
// This is an example template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// Capture the key's updated property value within the 'changes' object and store this in an attributes variable that can be used in the /users/track request

const changes = payload.properties.changes.custom_properties;

const attributes = {};
for (const key in changes) {
 attributes[key] = changes[key].new_value;
}

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z

const brazecall = {
 "attributes": [
   {
     "external_id": payload.userId,
     "_update_existing_only": false,
     ...attributes
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{% endtab %}
{% tab 実験の同期を維持する %}

**`contact.experiment.assigned` イベントを使用して Braze と Regal で実験をの同期を維持する**

以下は、Regalの`contact.experiment.assigned`イベントのサンプルペイロードです。

```json
{
  "userId": "123",
  "traits": {
    "phone": "+17625555555",
    "email": "xxx@gmail.com",
  },
  "name": "contact.experiment.assigned",
  "properties": {
    "experiment_name": "Post Call Offer Test",
    "experiment_id": "xxxx-xxxx-xxxx-xxxx",
    "experiment_variant": "Aggressive Offer - 50%",
    "journey_uuid": "xxxx-xxxx-xxxx-xxxx",
    "journey_friendly_id": 220,
    "journey_name": "Post Call Follow Up"
  },
  "originalTimestamp": "1657855118",
  "eventSource": "Regal Voice"
}
```

以下は、これをBrazeのカスタムイベントにマッピングするためのサンプルデータ変換です。

```
// The Braze /users/track endpoint expects timestamps in an ISO 8601 format. To use the Unix timestamp within Regal's call.completed event payload as the event timestamp in Braze, it must first be converted to ISO 8601. This can be done with the following code:
let unixTimestamp = payload.originalTimestamp;
let dateObj = new Date(unixTimestamp * 1000);
let isoString = dateObj.toISOString();

// This is an example template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z
let brazecall = {
 "events": [
   {
     "external_id": payload.userId,
     "_update_existing_only": false,
     "name": "Contact Experiment Assigned",
     "time": isoString,
     "properties": {
       "experiment_name": payload.properties.experiment_name,
       "experiment_id": payload.properties.experiment_id,
       "experiment_variant": payload.properties.experiment_variant,
       "journey_uuid": payload.properties.journey_uuid,
       "journey_friendly_id": payload.properties.journey_friendly_id,
       "journey_name": payload.properties.journey_name
     }
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;

```
{% endtab %}
{% tab 連絡先のサブスクリプションを解除する %}

**Regal の `contact.unsubscribed` に基づいて、Braze で連絡先のサブスクリプションを解除する**

以下は、Regalの`contact.unsubscribed`イベントのサンプルペイロードです。

```json
{
  "userId": "123",
  "traits": {
    "phone": "+17625555555",
    "email": "xxx@gmail.com",
    "ip": "78.97.213.166"
  },
  "name": "contact.unsubscribed",
  "properties": {
    "new_subscription": true,
    "channel": "voice",
    "text": null,
    "ip": "207.38.149.143",
    "source": "regalvoice.agent_desktop",
    "timestamp": "1657855229"
  },
  "originalTimestamp": "1657855230",
  "eventSource": "Regal Voice"
}
```

Braze の連絡先のサブスクリプションを解除するサンプル Data Transformation を以下に示します。

```
// This is an example template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z

let brazecall = {
 "attributes": [
   {
     "external_id": payload.userId,
     "_update_existing_only": true,
     "subscription_groups" : [{
       "subscription_group_id": "YOUR SUBSCRIPTION GROUP ID",
       "subscription_state": "unsubscribed"
     }]
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{% endtab %}
{% endtabs %}

