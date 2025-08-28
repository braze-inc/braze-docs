---
nav_title: Customer Data API への接続
article_title: Movable Ink Customer Data API への接続
description: "このリファレンス記事では、Braze に保存されている顧客イベントデータをアクティブ化して、Movable Ink 内でパーソナライズされたコンテンツを生成するために、Customer Data API を使用して接続する方法について説明します。"
page_type: partner
search_tag: Partner
---

# Movable Ink Customer Data API への接続

> Braze と Movable Ink Customer Data API の統合により、マーケターは Braze に保存されている顧客イベントデータをアクティブ化して、Movable Ink 内でパーソナライズされたコンテンツを生成できます。

Movable Ink は、Customer Data API を介して Braze から行動イベントを取り込むことができます。イベントは、Movable Ink に渡されるユニークユーザー ID (UUID) に基づいてユーザープロファイルに保存されます。

ストーリー、Movable Ink Customer Data API、および Movable Ink がどのように行動データを活用するかの詳細については、以下のサポートセンターの記事を参照してください。

- [行動データでコンテンツを強化する](https://support.movableink.com/hc/en-us/sections/360001239453-Power-content-with-behavioral-data)
- [Customer Data API の概要およびガイド](https://support.movableink.com/hc/en-us/articles/13815957200663-Customer-Data-API-introduction-and-guide)
- [FAQ:Customer Data API](https://support.movableink.com/hc/en-us/articles/12423178752279-FAQ-Customer-Data-API)

## 前提条件

| 必要条件 | 説明 |
|---|---|
| Movable Ink アカウント | このパートナーシップを活用するには、Movable Ink アカウントが必要です。 |
| Movable Ink API 認証情報 | Movable Ink のソリューションチームが API 認証情報を生成します。API 認証情報は、以下で構成されます。{::nomarkdown}<ul><li>エンドポイントURL（データの送信先）</li><li>ユーザー名とパスワード（APIの認証に使用される）</li></ul>{:/} 必要に応じて、Movable Ink はユーザー名とパスワードを、基本認証ヘッダー値として使用される base64 でエンコードされた値として指定できます。 |
| 行動イベント・ペイロード | イベントペイロード をMovable Ink クライアントエクスペリエンスチームと共有する必要があります。詳細については、「Movable Inkと[イベントペイロードを共有する](#event-payloads)」を参照のこと。 |
| クリエイティブ・アセットとビジネス・ロジック | Movable Ink とクリエイティブアセットを共有する必要があります。これには、ブロックとフォールバックイメージの作成方法を Movable Ink に指示する Adobe Photoshop (PSD) ファイルも含まれます。また、パートナーによってアクティブ化されたコンテンツブロックをいつどのように表示するかについてのビジネスロジックを提供する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

### ステップ1:BrazeでWebhookキャンペーンを作成する

#### ステップ 1a: 新しいキャンペーンを作成する

1. Brazeで、[Webhookキャンペーンを作成する]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)。
2. キャンペーン名と任意の説明をつける。
3. テンプレートとして [**空白のテンプレート**] を選択します。

#### ステップ 1b: Customer Data API 認証情報を追加する

1. **Webhook URL**フィールドに、Movable InkのエンドポイントURLを入力する。

![Braze の Webhook コンポーザーの「作成」タブ。Movable Ink エンドポイントのURL と、「JSON キーと値のペア」が設定された「リクエスト本文」が表示されている。]({% image_buster /assets/img/movable_ink/cd_api_webhook_url.png %}){: style="max-width:75%" }

{:start="2"}
2\.[**設定**] タブを選択します。
3\.以下のリクエストヘッダーをキーと値のペアとして追加する：

| キー | 値 |
| --- | --- |
| コンテンツタイプ | application/json |
| Authorization | Movable Ink から受け取った基本認証を入力します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![BrazeのWebhookコンポーザーの設定タブ。Content-TypeとAuthorizationのキー・バリュー・ペアがある。]({% image_buster /assets/img/movable_ink/cd_api_webhook_settings.png %}){: style="max-width:75%" }

#### ステップ1c: ペイロードを設定する

1. [**作成**] タブに戻ります。
2. **リクエスト本文**として、JSON キーと値のペアを使用して独自のリクエスト本文を作成するか、イベントペイロードを生のテキストとして入力します。標準的な e コマースイベントの例については、[サンプルペイロード](#sample-payloads)を参照してください。

![ID、タイムスタンプ、ユーザー ID、およびイベントタイプの JSON キーと値のペアが指定されている、Braze の Webhook コンポーザーの「作成」タブ。]({% image_buster /assets/img/movable_ink/cd_api_webhook_kvp.png %}){: style="max-width:75%" }

#### ステップ1d: Webhook をテストする {#step-1d}

サンプルペイロード をMovable Ink クライアントエクスペリエンスチームと共有する必要があります。このペイロードは、作成したペイロードに基づいて、**Test**タブで生成することができる。

{% alert important %}
Movable Ink は、Movable Ink クライアントエクスペリエンスチームがマッピングを完了し、テストを受ける準備ができていることを確認するまでは、Braze での Webhook のテストを行わないようにすることが推奨されています。このマッピングが完全でない場合、テスト時にエラーが出る可能性が高い。
{% endalert %}

ウェブフックをテストするには、以下のようにする：

1. [**テスト**] タブを選択します。
2. ユーザーとしてメッセージをプレビューし、そのユーザーのイベントペイロードのサンプルを表示する。ランダムユーザー、特定のユーザー、またはカスタムユーザーとしてのプレビューのいずれかを選択できます。
3. 問題がなければ、**Send testを**クリックしてテストリクエストを送信する。

![200OK レスポンスを示す Braze の Webhook レスポンスメッセージ。]({% image_buster /assets/img/movable_ink/cd_api_webhook_response.png %}){: style="max-width:75%" }

### ステップ2: キャンペーン設定を確定する

#### ステップ 2a: キャンペーンをスケジュールする

ウェブフックの作成とテストが終わったら、[キャンペーンをスケジュールする]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types)。 

Braze では、スケジュールされたアクションベースのAPI トリガー配信がサポートされています。[アクション・ベースの配信は]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/)通常、ほとんどの行動イベントのユースケースに最適である。お客様のユースケースにとって何が理にかなっているかについてのご質問は、BrazeおよびMovable Inkのカスタマーサクセスマネージャーにお問い合わせいただきたい。

アクションベースの配信の場合:

1. トリガーアクションを指定する。これは、Movable Inkへのウェブフックをトリガーするイベントである。
2. [**スケジュールの遅延**] が [**すぐに実行**] に設定されていることを確認します。イベント発生直後にイベントデータが遅滞なく Movable Ink に送信される必要があります。
3. 開始時間を指定してキャンペーン期間を設定する。終了時刻を適用できない可能性がありますが、ユースケースに必要な場合は設定できます。

{% alert note %}
データが Movable Ink にリアルタイムでストリーミングされるようにするには、[**ユーザーのローカルタイムゾーンにあわせてキャンペーンを送信**]を選択しないでください。
{% endalert %}

#### ステップ 2b: オーディエンスを指定する

次に、このキャンペーンでターゲットにしたいユーザーを決定する。詳細については、「[ユーザーをターゲットにする]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/)」を参照のこと。

**コントロールグループの**チェックボックスをオフにして、キャンペーンでA/Bテストを使用しないことを確認する。コントロールグループが含まれている場合、一定の割合のユーザーのデータが Movable Ink に送信されません。オーディエンス全体を、コントロールグループではなくバリアントに移動する必要があります。

![Braze キャンペーンにおける AB テストパネル。100％ のバリアント分布がバリアント 1 に割り当てられ、コントロールグループはない。]({% image_buster /assets/img/movable_ink/cd_api_webhook_ab.png %})

#### ステップ 2c: コンバージョンイベントを選択する（オプション）

必要であれば、Braze内でこのキャンペーンにコンバージョンイベントを割り当てることができる。

ただし、Webhook がデータのストリーミングのみを目的としている場合、このレベルでのアトリビューションは、Braze の行動データを使用してコンテンツをパーソナライズした後にキャンペーンレベルでアトリビューションを確認するよりも、有用性が低い可能性があります。

### ステップ3:キャンペーンを開始する

ウェブフックの設定を確認し、キャンペーンを開始する。

## 考慮事項

### 一意のユーザー識別子で整列する

`mi_u` として使用しているユニークユーザー識別子 (UUID) 値が Braze 内で使用可能であり、Movable Ink に送信されるイベントペイロードに含めることができることを確認します。

これにより、イメージを生成するときに Movable Ink が参照する動作イベントが、その動作イベントを受信した同一の顧客に関連付けられます。UUID 値がBraze `external_id` と同じではない場合、UUID はキャプチャされ、属性として Braze に渡されるか、またはこの ID を利用するために Braze イベントのイベントプロパティに入れて渡される必要があります。

Braze は複数のプラットフォーム (Web やモバイルアプリなど) にわたってユーザーの動作を追跡するため、1人のユーザーが複数の異なる匿名 ID を持つことがあります。`identify` イベントに匿名 ID と既知の単一 ID の両方が含まれている限り、`identify` イベントが Movable Ink に送信される時点で、これらの匿名 ID を単一の既知のストーリーズユーザープロファイルにマージできます。

Movable Ink が単一ユーザーの`user_id` を受信したら、そのユーザーの今後のすべてのイベントには同じ `user_id` が含まれている必要があります。

### Movable Ink でのイベントペイロードの共有 {#event-payloads}

Movable Ink の Customer Data API へのコネクターを設定する前に、イベントペイロードを Movable Ink クライアントエクスペリエンスチームと共有してください。これにより、Movable Ink がお客様のイベントを Movable Ink のイベントスキーマにマッピングでき、API 呼び出しの拒否や失敗を防ぐことができます。

任意のイベントプロパティを使用して、Braze内でイベントペイロードを生成できる。ランダムなユーザー、または特定のユーザーIDを検索してサンプルペイロードを生成する。詳細については上記の「[ステップ 1d](#step-1d)」を参照してください。

このサンプルペイロードをMovable Inkクライアントエクスペリエンスチームと共有する。サンプルペイロードに、機密性の高い個人識別情報 (メールアドレス、電話番号、誕生日全体など) が含まれていないことを確認します。 

カスタムイベントプロパティと、プロパティに含まれるデータに必要な形式について詳しくは、「[カスタムイベントプロパティ]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties)」を参照してください。

### 既知のユーザーと匿名のユーザー

Brazeでは、匿名のユーザープロファイルでイベントを記録することができる。イベントロギング中にどの識別子がユーザープロファイルにリンクされるかは、ユーザーがどのように作成されたか（Braze SDKまたはAPIを通じて）と、ユーザーライフサイクルの現在の段階に依存する。

#### 既知のユーザーのBrazeイベントのみを転送する

Webhook キャンペーンで `External User ID` フィルターを使用して、フィルター `External User ID` `is not blank` に一致する `external_id` を持つユーザーのみをターゲットにします。

#### 匿名ユーザーと既知ユーザーのBrazeイベントを転送する

匿名ユーザー（プロファイルに`external_id` が割り当てられる前のユーザー）からのBrazeイベントを転送したい場合、`external_id` が利用可能になるまで、Movable Inkの`anonymous_id` として使用する識別子を決定する必要がある。Brazeユーザープロフィールに常に表示される`anonymous_id` 。Webhook 本文で Liquid ロジックを使用して、`anonymous_id` または `user_id` を渡すかどうかを決定できます。

詳細については、[サンプルペイロード](#sample-payloads)にある Webhook の例を参照してください。

## ペイロードの例

### プロダクト・ビュー・イベント

{% tabs ローカル %}
{% tab Braze トリガーイベントの例 %}

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
{% tab 必要な Movable Ink リクエストペイロード %}

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
{% tab ウェブフックの例 %}

この例では、`external_id` を持たないユーザーのために、`anonymous_id` としてハッシュ化されたメールアドレスが使われている。

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

### カテゴリー表示イベント

{% tabs ローカル %}
{% tab Braze トリガーイベントの例 %}

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
{% tab 必要な Movable Ink リクエストペイロード %}

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
{% tab ウェブフックの例 %}

この例では、既知のユーザー（`external_id` を持つユーザー）のみのイベントを追跡するウェブフックを示している。

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

### イベントを特定する

{% tabs ローカル %}
{% tab Braze トリガーイベントの例 %}

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
{% tab 必要な Movable Ink リクエストペイロード %}

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
{% tab ウェブフックの例 %}

この例では、`external_id` を持たないユーザーのために、`anonymous_id` としてハッシュ化されたメールアドレスが使われている。

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



