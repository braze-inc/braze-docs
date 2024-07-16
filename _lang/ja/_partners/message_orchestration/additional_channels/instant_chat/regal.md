---
nav_title: Regal
article_title:Regal
description:この記事では、BrazeとRegalの提携について説明します。Regalは電話およびSMSの販売ソリューションであり、両方のソースからのデータを使用して顧客にパーソナライズされた体験を提供することができます。
alias: /partners/regal/
page_type: partner
search_tag:Partner

---

# Regal

> Regal.io][6] は、より多くの会話を促進するために構築された電話およびSMS販売ソリューションであり、成長目標をはるかに速く達成することができます。

RegalとBrazeを統合することで、すべての顧客接点においてより一貫性のあるパーソナライズされた体験を提供できます。
- Brazeからの次の最適なメールまたはプッシュ通知を、Regalの電話会話で言われた内容に基づいて送信します。
- 高価値の顧客がBrazeからのマーケティングメールをクリックしてもコンバージョンしない場合、Regalでコールをトリガーします。

## 前提条件

| 要件 | 説明 |
| ----------- | ----------- |
| リーガルアカウント | このパートナーシップを利用するには、リーガルアカウントが必要です。 |
| リーガルAPIキー | リーガルAPIキーを使用すると、BrazeからRegalにイベントを送信できます。<br><br>このキーを取得するには、[support@regal.io](mailto:support@regal.io) にメールしてください。 |
| Braze データ変換 | データ変換は現在、早期アクセス中です。早期アクセスに参加することに興味がある場合は、Brazeのカスタマーサクセスマネージャーに連絡してください。これはリーガルからデータを受け取るために必要です。 |
{: .reset-td-br-1 .reset-td-br-2}

## Integration: BrazeからRegalにデータを送信する

次のセクションでは、Braze Canvasまたはキャンペーンのウェブフックを使用して、Brazeをソースとして顧客プロファイルおよびイベントデータをRegalに送信する方法について説明します。

### ステップ1:Regalで新しい連絡先を作成する

Brazeで新しい連絡先が作成されるたびに、Regalでの通話やテキストメッセージに利用できるようにするために、Regalにウェブフックするキャンバスまたはキャンペーンを作成します。 

1. 「Regalの新しい連絡先を作成」というタイトルのキャンバスまたはキャンペーンを作成し、エントリータイプとして**アクションベース**を選択します。

2. トリガーロジックを**カスタムイベント**として設定し、電話番号を持つ連絡先が作成されたときに発生するイベントを選択します。リーガルは、電話フィールドに設定されていることを確認するための追加フィルターを追加することも推奨しています。

3. 新しいWebhookテンプレートに、次のフィールドに記入してください:
   - **Webhook URL**: <https://events.regalvoice.com/events>
   - **リクエスト本文**:Raw Text

#### リクエストヘッダーとメソッド

Regal.ioは、認証のためのHTTPヘッダーとHTTPメソッドも必要です。次の内容は、**設定**タブにキーと値のペアとして既に含まれています:
{% raw %}
- **HTTPメソッド**:POST
- **リクエストヘッダー**:
    - **認可**: `{{<REGAL_API_KEY>}}`
    - **Content-Type**: application/json
{% endraw %}

#### Request body

以下で唯一必要なフィールドは`traits.phone`プロパティです。残りはオプションです。しかし、`optIn`を含める場合は、`optIn.channel`と`optIn.subscribed`を含める必要があります。

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

上記のペイロード例は、すべての連絡先が音声およびSMSのオプトインを受け入れたことを前提としています。それが真実でない場合は、上記から`optIn`プロパティを削除し、`optIn`が収集されたときにRegalの連絡先を更新するための別のキャンバスまたはキャンペーンを設定できます。

### ステップ2:オプトイン情報を更新する 

アプリのユーザーエクスペリエンスの異なる部分でオプトインおよびオプトアウトが発生する場合、ユーザーがオプトインまたはオプトアウトするたびにRegalを更新することが重要です。以下は、最新のオプトイン情報をRegalに送信するための推奨キャンバスです。これはBrazeプロファイルフィールドとして保存することを前提としていますが、そうでない場合、トリガーはユーザーがオプトインまたは購読解除することを表すBrazeアカウントのイベントでも同様に簡単に設定できます。（以下の例は電話のオプトイン用ですが、SMSのオプトインを別途収集する場合は、同様のキャンバスやキャンペーンを設定できます）。

1. 「Send Opt In or Out to Regal」というタイトルの新しいキャンバスまたはキャンペーンを作成します。

2. 次のトリガーオプションのいずれかを選択し、ユーザーのオプトインステータスを表すフィールドを選択します。オプトインまたはオプトアウトを表すイベントをBrazeに発行する場合は、そのイベントをトリガーとして使用してください。
    - ユーザープロファイルフィールドが更新されました
    - サブスクリプショングループのステータスを更新
    - サブスクリプションステータス

3. 新しいWebhookテンプレートに、次のフィールドに記入してください:
   - **Webhook URL**: <https://events.regalvoice.com/events>
   - **リクエスト本文**:Raw Text

#### リクエストヘッダーとメソッド

Regal.ioは、認証のためのHTTPヘッダーとHTTPメソッドも必要です。次の内容は、テンプレート内にキーと値のペアとして既に含まれていますが、**設定**タブにあります:
{% raw %}
- **HTTPメソッド**:POST
- **リクエストヘッダー**:
    - **認可**: `{{<REGAL_API_KEY>}}`
    - **Content-Type**: application/json
{% endraw %}

#### Request body

このペイロードに追加のユーザープロファイル属性を追加してもかまいません。また、複数の属性を同時に最新の状態に保つことができます。

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

最後に、Regalに送信したい主要なイベントごとにキャンバスまたはキャンペーンを設定します。Regalは、RegalでSMSや通話をトリガーするために重要なイベント（サインアップや購入フローの各ステップでのイベントなど）や、Regalキャンペーンから連絡先が外れるための終了基準として使用されるイベントを送信することを推奨します。

例えば、以下はユーザーがアプリケーションの最初のステップを完了したときにRegalにイベントを送信するためのワークフローです。

1. 「アプリケーションステップ1完了イベントをRegalに送信」と題された新しいキャンバスまたはキャンペーンを作成します。

2. トリガーノードのロジックを**カスタムイベント**として設定し、Regalに送信したいイベント名を選択します。例えば、「アプリケーションステップ1完了」などです。

3. 新しいWebhookテンプレートに、次のフィールドに記入してください:
   - **Webhook URL**: <https://events.regalvoice.com/events>
   - **リクエスト本文**:Raw Text

#### リクエストヘッダーとメソッド

Regal.ioは、認証のためのHTTPヘッダーとHTTPメソッドも必要です。次の内容は、テンプレート内にキーと値のペアとして既に含まれていますが、**設定**タブにあります:
{% raw %}
- **HTTPメソッド**:POST
- **リクエストヘッダー**:
    - **認可**: `{{<REGAL_API_KEY>}}`
    - **Content-Type**: application/json
{% endraw %}

#### Request body

このペイロードに追加のユーザープロファイル属性を追加して、複数の属性が同時に最新の状態になるようにすることができます。

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

必須ではありませんが、Regalは、主要なイベントが利用可能になった時点で最新の連絡先属性にアクセスできるようにするために、イベントワークフローのイベントペイロードに主要なユーザープロファイルデータフィールドも送信することをお勧めします。

{% alert note %}
ご質問がある場合や、これらのキャンバスやキャンペーンの設定方法についての詳細は、support@regal.ioにお問い合わせください。
{% endalert %}

## Integration: RegalからBrazeにデータを送信する

このセクションでは、`SMS.sent`や`call.completed`のようなRegalレポートイベントをBrazeに取り込む方法について説明します。これにより、Brazeプロファイルに表示され、Brazeのセグメンテーションツール、Canvas、およびキャンペーンで利用できるようになります。この統合は、Regal Reporting WebhooksとBraze Data Transformationを使用してデータフローを自動化します。

### ステップ1:Brazeでデータ変換を作成する

{% alert important %}
データ変換は現在、早期アクセス中です。早期アクセスに参加することに興味がある場合は、Brazeのカスタマーサクセスマネージャーに連絡してください。
{% endalert %}

Brazeは、Brazeに送信する予定のRegal Webhookごとに変換を作成することをお勧めします。 

データ変換を作成するには:
1. Brazeダッシュボードの**Transformations**ページに移動します。
2. 変換に名前を付けて、**変換を作成**をクリックします。
3. 変換リストから、<i class="fa-solid fa-ellipsis-vertical" title="アクションを表示"></i>をクリックし、**Webhook URLをコピー**を選択します。

![][4]

### ステップ2:RegalでレポートのWebhookを有効にする

レポートのウェブフックを設定するには:
1. レガルアプリに移動して、**設定**ページを開きます。

2. 「**レポートウェブフック**」セクションで、「**ウェブフックを作成**」をクリックします。

3. Webhookエンドポイント入力に、関連するデータ変換のためのBrazeデータ変換Webhook URLを追加します。

![][5]{: style="max-width:60%;"}

#### エンドポイントの更新
エンドポイントを編集すると、キャッシュが更新されて新しいエンドポイントにイベントが送信されるまでに最大で5分かかることがあります。
#### リトライ
現在、これらのイベントに再試行はありません。応答が5秒以内に受信されない場合、イベントは破棄され、再試行されません。リーガルは将来のリリースでリトライを追加する予定です。
#### イベント
リーガルの\[レポートウェブフックガイド][7]には、公開されているレポートイベントの完全なリストが含まれています。そこでは、プロパティの定義やサンプルペイロードも見ることができます。

### ステップ3:レガルイベントをBrazeイベントに変換する

Brazeの[データ変換]({{site.baseurl}}/data_transformation)機能を使用すると、受信したRegalイベントをBrazeに属性、イベント、または購入として追加するために必要な形式にマッピングできます。

1. データ変換に名前を付けてください。イベントWebhookごとにデータ変換を設定することをお勧めします。

2. 接続をテストするには、Regal Agent Desktopから携帯電話に発信し、会話の概要フォームを送信して、call.completedイベントを作成します。

3. あなたのRegalの連絡先をBrazeのプロファイルにマッピングするために使用する識別子を決定します。Regalイベントで利用可能な識別子には次のものがあります：
   - `userId` - イベントにのみ設定されますが、以前にこの識別子を連絡先に送信した場合に限ります
   - `traits.phone`
   - `traits.email` - イベントにのみ設定されますが、以前にこの識別子を連絡先に送信した場合に限ります

#### Braze対応の識別子
- Brazeは識別子として電話番号をサポートしていません。これを識別子として使用するには、電話番号をBrazeの\[user alias][8]として設定できます。
- Brazeデータ変換を使用する場合、メールアドレスを識別子として使用できます。メールアドレスがBraze内のプロファイルとして存在する場合、既存のプロファイルが更新されます。メールアドレスがBraze内にまだ存在しない場合、メールのみのプロファイルが作成されます。

## ユースケース

{% tabs %}
{% tab Trigger an email %}

**Regalのコールディスポジションに基づいてBrazeからメールをトリガーする**

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
// Braze's /users/track endpoint expects timestamps in an ISO 8601 format. To use the Unix timestamp within Regal's call.completed event payload as the event timestamp in Braze must first be converted to ISO 8601. This can be done with the following code:
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
{% tab Update profile attributes %}

**Regalの`contact.attribute.edited`イベントに基づいてBrazeのプロファイル属性を更新する**

以下は、Regalの`contact.attribute.edited`イベントのサンプルペイロードです。このイベントは、エージェントの1人が会話の中で新しいことを学び、連絡先のプロファイルの属性を更新するたびに発生します。

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
{% tab Keep your experiments in sync %}

**実験をBrazeとRegalで同期させるには、`contact.experiment.assigned`イベントを使用します**

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
// Braze's /users/track endpoint expects timestamps in an ISO 8601 format. To use the Unix timestamp within Regal's call.completed event payload as the event timestamp in Braze, it must first be converted to ISO 8601. This can be done with the following code:
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
{% tab Unsubscribe a contact %}

**Regalからの`contact.unsubscribed`に基づいてBrazeで連絡先の購読を解除する**

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

以下は、Brazeで連絡先の購読を解除するためのサンプルデータ変換です。

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

[2]: {% image_buster /assets/img/regal/webhook_rawtext.png %}
[3]: {% image_buster /assets/img/regal/request_header.png %}
[4]: {% image_buster /assets/img/regal/copy_webhook_url.png %}
[5]: {% image_buster /assets/img/regal/edit_webhook.png %}
[6]: https://regal.io
[7]: https://developer.regal.io/docs/reporting-webhooks#events
[8]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases