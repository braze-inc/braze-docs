---
nav_title: 顧客データ API への接続
article_title:Movable Ink カスタマーデータ API への接続
description:「この参考記事では、顧客データAPIを使用してBrazeに保存されている顧客イベントデータを接続してアクティブ化し、Movable Ink内でパーソナライズされたコンテンツを生成する方法を概説しています。「
page_type: partner
search_tag:Partner
---

# Movable Ink カスタマーデータ API への接続

> Braze と Movable Ink の顧客データ API の統合により、マーケティング担当者は Braze に保存されている顧客イベントデータを有効にして、Movable Ink 内でパーソナライズされたコンテンツを生成できます。

Movable Ink は、顧客データ API を通じて Braze から行動イベントを取り込むことができます。イベントは、Movable Ink に渡された一意のユーザー ID (UUID) に基づいてユーザープロファイルに保存されます。

ストーリー、Movable Ink顧客データAPI、およびMovable Inkがどのように行動データを活用するかについての詳細は、以下のサポートセンターの記事をご覧ください。

- [行動データでコンテンツを強化](https://support.movableink.com/hc/en-us/sections/360001239453-Power-content-with-behavioral-data)
- [顧客データ API の紹介とガイド](https://support.movableink.com/hc/en-us/articles/13815957200663-Customer-Data-API-introduction-and-guide)
- [FAQ: カスタマーデータ API](https://support.movableink.com/hc/en-us/articles/12423178752279-FAQ-Customer-Data-API)

## 前提条件

| 必要条件 | 説明 |
|---|---|
| ムーバブルインクアカウント | このパートナーシップを利用するには、Movable Inkアカウントが必要です。 |
| ムーバブルインク API 認証情報 | Movable Ink のソリューションチームが API 認証情報を生成します。API 認証情報には次のものが含まれます。{::nomarkdown}<ul><li>エンドポイント URL (データの送信先)</li><li>ユーザー名とパスワード (API の認証に使用)</li></ul>{:/} 必要に応じて、Movable Ink はユーザー名とパスワードを base64 でエンコードされた値として提供し、基本的な認証ヘッダー値として使用できます。 |
| 行動イベントペイロード | イベントペイロードをMovable Inkクライアントエクスペリエンスチームと共有する必要があります。詳細については、「Movable Ink [とのイベントペイロードの共有](#event-payloads)」を参照してください。 |
| クリエイティブアセットとビジネスロジック | Movable Ink でブロックの作成方法を指示するAdobe Photoshop (PSD) ファイルなどのクリエイティブアセットを Movable Ink と共有する必要があります。また、パートナーがアクティベートしたコンテンツブロックをいつどのように表示するかについてのビジネスロジックも提供する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ1:Braze でWebhook キャンペーンを作成する

#### ステップ 1a: 新しいキャンペーンを作成する

1. Braze [でWebhook キャンペーンを作成します][1]。
2. キャンペーンに名前を付けて、必要に応じて説明を入力します。
3. **テンプレートとして \[空白テンプレート**] を選択します。

#### ステップ 1b: 顧客データ API 認証情報を追加

1. 「**ウェブフック URL**」フィールドに、Movable Ink エンドポイント URL を入力します。

![Braze の Webhook コンポーザーの \[作成] タブでは、Movable Ink エンドポイント URL とリクエストボディが JSON キー/値ペアに設定されています。]\[イメージ1]{: style="max-width:75%" }

{:start="2"}
2\.\[**設定**] タブを選択します。
3\.以下のリクエストヘッダーをキーと値のペアとして追加します。

| キー | 価値 |
| --- | --- |
| コンテンツタイプ | アプリケーション/json |
| 認可 | Movable Ink から受け取った基本認証を入力してください。 |
{: .reset-td-br-1 .reset-td-br-2}

![Braze の Webhook コンポーザーの \[設定] タブには、コンテンツタイプと認証のキーと値のペアがあります。]\[イメージ2]{: style="max-width:75%" }

#### ステップ 1c:ペイロードを設定

1. 「**作成**」タブに戻ります。
2. **リクエストボディには**、JSON キーと値のペアを使用して独自のリクエストボディを作成するか、イベントペイロードを未加工のテキストとして入力します。標準の e コマースイベントの例については、[サンプルペイロードを参照してください](#sample-payloads)。

![ID、タイムスタンプ、ユーザー ID、イベントタイプの JSON キーと値のペアを使用して Braze の Webhook コンポーザーの \[作成] タブを作成します。]\[イメージ3]{: style="max-width:75%" }

#### ステップ 1d:Webhook をテストする {#step-1d}

サンプルペイロードを Movable Ink クライアントエクスペリエンスチームと共有する必要があります。このペイロードは、作成したペイロードに基づいて \[**テスト**] タブで生成できます。

{% alert important %}
Movable Ink では、Movable Ink クライアントエクスペリエンスチームがマッピングが完了し、テストを受ける準備ができていることを確認するまで、Webhook を Braze でテストすることを推奨しています。このマッピングが完了していないと、テスト時にエラーする可能性があります。
{% endalert %}

Webhook をテストするには、次の操作を行います。

1. \[**テスト**] タブを選択します。
2. メッセージをユーザーとしてプレビューすると、そのユーザーのサンプルイベントペイロードが表示されます。ランダムユーザー、特定のユーザー、またはカスタムユーザーとしてプレビューするかどうかを選択できます。
3. すべて問題なければ、\[**テストを送信**] をクリックしてテストリクエストを送信します。

![Braze のウェブフックレスポンスメッセージに 200 OK のレスポンスが表示される。]\[イメージ4]{: style="max-width:75%" }

### ステップ2:キャンペーン設定を確定する

#### ステップ 2a: キャンペーンをスケジュールする

Webhook の作成とテストが完了したら、キャンペーン[スケジュールを設定します。][2] 

Braze は、スケジュールされた配信、アクションベースの配信、API トリガーによる配信をサポートしています。[アクションベースの配信は][3]、通常、ほとんどの行動イベントのユースケースに最適です。あなたのユースケースにとって何が理にかなっているかについての質問は、Braze および Movable Ink の顧客サクセスマネージャーにお問い合わせください。

アクションベースの配信の場合:

1. トリガーアクションを指定します。これがMovable Inkへのウェブフックをトリガーするイベントです。
2. \[**スケジュールの遅延**] が \[**即時**] に設定されていることを確認します。イベントデータは、イベントが発生した直後に、遅滞なくMovable Inkに送信する必要があります。
3. 開始時間を指定してキャンペーン期間を設定します。終了時間は適用されない可能性がありますが、ユースケースで必要に応じて設定できます。

{% alert note %}
データがリアルタイムでMovable Inkにストリーミングされるようにするには、「**ローカルタイムゾーンユーザーにキャンペーンを送信**」を選択しないでください。
{% endalert %}

#### ステップ 2b: オーディエンス指定してください

次に、このキャンペーンターゲットにするユーザーを決定します。詳細については、「[ユーザーをターゲットにする][4]」を参照してください。

**コントロールグループのチェックボックスをオフにして**、キャンペーンでA/Bテストを使用しないようにしてください。コントロールグループが含まれている場合、一部のユーザーはMovable Inkにデータを送信できません。すべてのオーディエンス、コントロールグループではなくバリアントに移動する必要があります。

![バリアント1に 100% のバリアント分散を割り当てたBrazeキャンペーン A/Bテストパネルで、コントロールグループはありません。]\[イメージ5]

#### ステップ 2c: コンバージョンイベントの選択 (オプション)

必要に応じて、Braze 内でこのキャンペーンにコンバージョンイベントを割り当てることができます。

ただし、Webhookはデータのストリーミングのみを目的としているため、このレベルでのアトリビューションは、Brazeの行動データを使用してコンテンツをパーソナライズした後にキャンペーンレベルでアトリビューションビューションを見る場合ほど役に立たない可能性があります。

### ステップ3:キャンペーンを開始する

Webhook の設定を確認して、キャンペーンを開始してください。

## 考慮事項

### 一意のユーザーIDによる調整

自分のものとして使用しているユニークユーザー識別子（UUID）値がBraze内で利用可能であり`mi_u`、Movable Inkに送信されるイベントペイロードに含めることができることを確認してください。

これにより、画像, 写真生成時に Movable Ink が参照する行動イベントが、その行動イベントを受け取った顧客と同じものであることが保証されます。UUID値がBrazeと同じでない場合、この識別子を利用するには`external_id`、UUIDをキャプチャして属性として、またはBrazeイベントのイベントプロパティでBrazeに渡す必要があります。

Brazeは複数のプラットフォーム（ウェブやモバイルアプリなど）でのユーザー行動を追跡するため、1人のユーザー複数の異なる匿名IDを持つことがあります。イベントに匿名の識別子と単一の既知の識別子の両方が含まれている限り、`identify`これらのIDはイベントがMovable Inkに送信されたときに単一の既知のStoriesユーザープロファイル統合できます。`identify`

Movable Ink が 1 `user_id` 人のユーザーに対してを受け取ったら、そのユーザー`user_id`今後のすべてのイベントに同じ内容を含める必要があります。

### Movable Ink とのイベントペイロードの共有 {#event-payloads}

Movable Ink の顧客データ API へのコネクタ設定する前に、イベントペイロードを Movable Ink クライアントエクスペリエンスチームと共有してください。これにより、Movable Ink はイベントをイベントスキーマにマッピングできるようになり、API 呼び出しが拒否されたり失敗したりするのを防ぐことができます。

Braze では、任意のイベントプロパティを使用してイベントペイロードを生成できます。ランダムユーザーのサンプルペイロードを生成するか、特定のユーザー ID を検索して生成します。詳細については、[上記のステップ 1d](#step-1d) を参照してください。

このサンプルペイロードを Movable Ink クライアントエクスペリエンスチームと共有してください。サンプルのペイロードには、個人を特定できる機密情報 (メールアドレス、電話番号、生年月日など) が含まれていないことを確認してください。 

カスタムイベントのプロパティと、プロパティに含まれるデータの期待される形式について詳しくは、「[カスタムイベントプロパティ][5]」を参照してください。

### 既知ユーザーと匿名ユーザー

Brazeでは、イベントを匿名のユーザープロファイルで記録できます。イベントロギング中にどの識別子がユーザープロファイルリンクされるかは、ユーザー作成方法（Braze SDKまたはAPIを使用）とユーザーライフサイクルの現在の段階によって異なります。

#### 既知のユーザーのBrazeイベントのみを転送する

Webhookキャンペーンでは、`External User ID`フィルターを使用して、`external_id``External User ID``is not blank`フィルター付きのユーザーのみをターゲットにします。

#### 匿名ユーザーおよび既知のユーザーへのBrazeイベントの転送

匿名ユーザー（プロファイルにAが割り当てられる前のユーザー）からのBrazeイベントを転送する場合は、`external_id``external_id`が利用可能になるまで、Movable Inkにどの識別子を使用するかを決定する必要があります。`anonymous_id`Braze `anonymous_id` ユーザープロファイルで常に変わらないものを選択してください。Webhook 本体のLiquidロジックを使用して、`anonymous_id``user_id`またはaを渡すかどうかを決定できます。

詳細については、[サンプルペイロードの下にあるwebhook](#sample-payloads) 例を参照してください。

## ペイロードの例

### 製品ビューイベント

{% tabs local %}
{% tab Example Braze Trigger Event %}

{% raw %}

```json
{
  "events": [
    {
      "email": "test@braze.com",
      "name": "Product Viewed",
      "time": "2023-12-06T19:20:45+01:00",
      "properties": {
        "categories": [
          {
            "id": "Bathroom",
            "url": "https://example.com/cat/bathroom"
          }
        ],
        "meta": {
          "color": "green"
        },
        "title": "All-Purpose Cleaning Wipes",
        "price": 1.99,
        "id": "56544",
        "url": "https://www.example.com/variants_id/5f08cb918dcc595aa74b0fbc"
      }
    }
  ]
}
```

{% endraw %}

{% endtab %}
{% tab Expected Movable Ink Request Payload %}

{% raw %}

```
curl --location --request POST 'https://collector.movableink-dmz.com/behavioral/{{key}}' \
--header 'Authorization: Basic {{authorization}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "anonymous_id": "123-abc-678",
  "event": "product_viewed",
  "properties": {
    "categories": [
      {
        "id": "Bathroom",
        "url": "https://example.com/cat/bathroom"
      }
    ],
    "meta": {
      "color": "green"
    },
    "title": "All-Purpose Cleaning Wipes",
    "price": 1.99,
    "id": "56544",
    "url": "https://www.example.com/variants_id/5f08cb918dcc595aa74b0fbc"
  },
  "timestamp": 1257894000000,
  "timezone": "America/New_York",
  "type": "track",
  "user_id": "5c3aa83113dd490100d3d8d7"
}'

```

{% endraw %}
{% endtab %}
{% tab Example webhook %}

この例では、ハッシュ化されたメールアドレスが、`anonymous_id``external_id`を持たないユーザー用に使用されます。

{% raw %}

```liquid
// Converts the timestamp of "now" to seconds since 1970 and assigns it to a local variable "timestamp"
{% assign timestamp = "now" | date: "%s" %}

// Example of md5 hashing the email address to use as the anonymous_id
{% assign anon_id = {{${email_address}}} | md5 %}

// Condition logic to determine which identifier to use. If an external_id is available use that, otherwise use the anonymous_id
{% if {{${user_id}}} %}
{% capture user_identifier %}"user_id": "{{${user_id}}}"{% endcapture %}
{% else %}
{% capture user_identifier %}"anonymous_id": "{{anon_id}}"{% endcapture %}
{% endif %}

{
  {{user_identifier}}
  "event": "product_viewed",
  "properties": {
    "categories": [
      {
        "id": "{{event_properties.${categories}[0].id}}",
        "url": "{{event_properties.${categories}[0].url}}"
      }
    ],
    "meta": {
      "color": "{{event_properties.${meta}.color}}"
    },
    "title": "{{event_properties.${title}}}",
    "price": "{{event_properties.${price}}}",
    "id": "{{event_properties.${id}}}",
    "url": "{{event_properties.${url}}}"
  },
  "timestamp": "{{timestamp}}",
  "timezone": "{{${time_zone}}}",
  "type": "track",
}

```

{% endraw %}
{% endtab %}
{% endtabs %}

### カテゴリビューイベント

{% tabs local %}
{% tab Example Braze Trigger Event %}

{% raw %}

```json
{
  "events": [
    {
      "external_id": "123456789",
      "name": "Category Viewed",
      "time": "2023-12-06T19:20:45+01:00",
      "properties": {
        "id": "bathroom-1",
        "title": "Bathroom Stuff",
        "url": "https://www.example.com/categories/bathroom"
      }
    }
  ]
}
```

{% endraw %}

{% endtab %}
{% tab Expected Movable Ink Request Payload %}

{% raw %}

```
curl --location --request POST 'https://collector.movableink-dmz.com/behavioral/{{key}}' \
--header 'Authorization: Basic {{authorization}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "anonymous_id": "123-abc-678",
  "event": "category_viewed",
  "properties": {
    "id": "bathroom-1",
    "title": "Bathroom Stuff",
    "url": "https://www.example.com/categories/bathroom"
  },
  "timestamp": 1257894000000,
  "timezone": "America/New_York",
  "type": "track",
  "user_id": "5c3aa83113dd490100d3d8d7"
}'
```

{% endraw %}

{% endtab %}
{% tab Example webhook %}

この例は、既知のユーザー（がのユーザー`external_id`）のみのイベントトラッキング, 追跡するWebhookを示しています。

{% raw %}

```liquid
// Converts the timestamp of "now" to seconds since 1970 and assigns it to a local variable "timestamp"
{% assign timestamp = "now" | date: "%s" %}

{
  "event": "category_viewed",
  "properties": {
    "id": "{{event_properties.${id}}}",
    "title": "{{event_properties.${title}}}",
    "url": "{{event_properties.${url}}}"
  },
  "timestamp": "{{timestamp}}",
  "timezone": "{{${time_zone}}}",
  "type": "track",
  "user_id": "{{${user_id}}}"
}

```

{% endraw %}

{% endtab %}
{% endtabs %}

### イベントを識別

{% tabs local %}
{% tab Example Braze Trigger Event %}

{% raw %}

```json
{
  "events": [
    {
      "external_id": "123456789",
      "name": "Account Created",
      "time": "2023-12-06T19:20:45+01:00"
    }
  ]
}
```

{% endraw %}
{% endtab %}
{% tab Expected Movable Ink Request Payload %}

{% raw %}

```
curl --location --request POST 'https://collector.movableink-dmz.com/behavioral/{{key}}' \
--header 'Authorization: Basic {{authorization}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "anonymous_id": "jg0iq5gd30dqpwn8zmx05p06mzjmjir4r8",
  "timestamp": 1257894000000,
  "timezone": "America/New_York",
  "type": "identify",
  "user_id": "mycustomerid123"
}'
```

{% endraw %}
{% endtab %}
{% tab Example webhook %}

この例では、ハッシュ化されたメールアドレスが、`anonymous_id``external_id`を持たないユーザー用に使用されます。

{% raw %}

```liquid
// Converts the timestamp of "now" to seconds since 1970 and assigns it to a local variable "timestamp"
{% assign timestamp = "now" | date: "%s" %}

// Example of md5 hashing the email address to use as the anonymous_id
{% assign anon_id = {{${email_address}}} | md5 %}

{
  "anonymous_id": "{{anon_id}}",
  "timestamp": "{{timestamp}}",
  "timezone": "{{${time_zone}}}",
  "type": "identify",
  "user_id": "{{${user_id}}}"
}

```

{% endraw %}

{% endtab %}
{% endtabs %}



[1]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/
[2]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types
[3]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/
[4]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/
[5]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties
\[img1]: {% image_buster /assets/img/movable_ink/cd_api_webhook_url.png %}
\[img2]: {% image_buster /assets/img/movable_ink/cd_api_webhook_settings.png %}
\[img3]: {% image_buster /assets/img/movable_ink/cd_api_webhook_kvp.png %}
\[img4]: {% image_buster /assets/img/movable_ink/cd_api_webhook_response.png %}
\[img5]: {% image_buster /assets/img/movable_ink/cd_api_webhook_ab.png %}
