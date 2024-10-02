---
nav_title: 顧客データAPIに接続する
article_title: Movable Ink Customer Data APIに接続する
description: "この参考記事では、Customer Data APIを使用して、Brazeに保存されている顧客のイベントデータを活性化し、Movable Ink内でパーソナライズされたコンテンツを生成するための接続方法について概説する。"
page_type: partner
search_tag: Partner
---

# Movable Ink Customer Data APIに接続する

> BrazeとMovable Inkの顧客データAPI統合により、マーケティング担当者はBrazeに保存された顧客イベントデータを有効化して、Movable Ink内でパーソナライズされたコンテンツを生成することができる。

ムーバブル・インクは、顧客データAPIを通じてBrazeから行動イベントを取り込むことができる。イベントは、ムーバブルインクに渡される一意のユーザーID（UUID）に基づいてユーザープロファイルに保存される。

ストーリーズ、Movable Ink Customer Data API、およびMovable Inkが行動データをどのように活用しているかについての詳細は、以下のサポートセンターの記事を参照されたい：

- [行動データでコンテンツを強化する](https://support.movableink.com/hc/en-us/sections/360001239453-Power-content-with-behavioral-data)
- [顧客データAPIの紹介とガイド](https://support.movableink.com/hc/en-us/articles/13815957200663-Customer-Data-API-introduction-and-guide)
- [よくある質問顧客データAPI](https://support.movableink.com/hc/en-us/articles/12423178752279-FAQ-Customer-Data-API)

## 前提条件

| 必要条件 | 説明 |
|---|---|
| ムーバブル・インクアカウント | このパートナーシップを利用するには、ムーバブル・インクのアカウントが必要である。 |
| Movable Ink API認証情報 | Movable Inkのソリューション・チームがAPI認証情報を生成する。APIクレデンシャルは以下のものである：{::nomarkdown}<ul><li>エンドポイントURL（データの送信先）</li><li>ユーザー名とパスワード（APIの認証に使用される）</li></ul>{:/} 必要であれば、Movable Inkはユーザー名とパスワードをbase64エンコード値として提供し、基本認証ヘッダー値として使用することができる。 |
| 行動イベント・ペイロード | イベントペイロードをMovable Inkクライアントエクスペリエンスチームと共有する必要がある。詳細については、「Movable Inkと[イベントペイロードを共有する](#event-payloads)」を参照のこと。 |
| クリエイティブ・アセットとビジネス・ロジック | ブロックを構築する方法についてMovable Inkに指示するAdobe Photoshop（PSD）ファイルや予備画像など、クリエイティブ資産をMovable Inkと共有する必要がある。また、パートナーがアクティベートしたコンテンツ・ブロックをいつ、どのように表示するかのビジネス・ロジックを提供する必要がある。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ1:BrazeでWebhookキャンペーンを作成する

#### ステップ 1a: 新しいキャンペーンを作成する

1. Brazeで、[Webhookキャンペーンを作成する][1]。
2. キャンペーン名と任意の説明をつける。
3. テンプレートとして**Blank Templateを**選択する。

#### ステップ 1b: 顧客データAPIの認証情報を追加する

1. **Webhook URL**フィールドに、Movable InkのエンドポイントURLを入力する。

![BrazeのWebhookコンポーザーのComposeタブで、Movable InkのエンドポイントURLとリクエストボディをJSON Key/Value Pairsに設定する。]\[img1]{: style="max-width:75%" }

{:start="2"}
2\.**設定**タブを選択する。
3\.以下のリクエストヘッダーをキーと値のペアとして追加する：

| キー | 価値 |
| --- | --- |
| コンテンツタイプ | application/json |
| 認可 | ムーバブルインクから受け取った基本認証を入力する。 |
{: .reset-td-br-1 .reset-td-br-2}

![BrazeのWebhookコンポーザーの設定タブ。Content-TypeとAuthorizationのキー・バリュー・ペアがある。]\[img2]{: style="max-width:75%" }

#### ステップ1c：ペイロードを設定する

1. **作曲**タブに戻る。
2. **リクエストボディには**、JSONキーと値のペアで独自のリクエストボディを作成するか、生のテキストとしてイベントペイロードを入力する。標準的なeコマースイベントの例については、[サンプルペイロードを](#sample-payloads)参照のこと。

![Brazeのウェブフック・コンポーザーのコンポーズ・タブに、ID、タイムスタンプ、ユーザーID、イベントタイプのJSONキー・バリュー・ペアがある。]\[img3]{: style="max-width:75%" }

#### ステップ1d：ウェブフックをテストする {#step-1d}

ペイロードのサンプルをMovable Inkクライアント・エクスペリエンス・チームと共有する必要がある。このペイロードは、作成したペイロードに基づいて、**Test**タブで生成することができる。

{% alert important %}
Movable Inkでは、Movable Inkクライアントエクスペリエンスチームがマッピングを完了し、テストを受ける準備ができていることを確認するまで、BrazeでのWebhookのテストを待つことを推奨している。このマッピングが完全でない場合、テスト時にエラーが出る可能性が高い。
{% endalert %}

ウェブフックをテストするには、以下のようにする：

1. \[**テスト**] タブを選択します。
2. ユーザーとしてメッセージをプレビューし、そのユーザーのイベントペイロードのサンプルを表示する。プレビューは、ランダムユーザー、特定ユーザー、カスタムユーザーのいずれかを選択できる。
3. 問題がなければ、**Send testを**クリックしてテストリクエストを送信する。

![200OKレスポンスを示すBrazeのWebhookレスポンスメッセージ。]\[img4]{: style="max-width:75%" }

### ステップ2:キャンペーン設定を確定する

#### ステップ 2a: キャンペーンをスケジュールする

ウェブフックの作成とテストが終わったら、[キャンペーンをスケジュールする][2]。 

Brazeは、スケジュール配信、アクションベース配信、APIトリガー配信をサポートしている。[アクション・ベースの配信は][3]通常、ほとんどの行動イベントのユースケースに最適である。お客様のユースケースにとって何が理にかなっているかについてのご質問は、BrazeおよびMovable Inkのカスタマーサクセスマネージャーにお問い合わせいただきたい。

アクション・ベースのデリバリーのために：

1. トリガーアクションを指定する。これは、Movable Inkへのウェブフックをトリガーするイベントである。
2. **Schedule Delayが** **Immediatelyに**設定されていることを確認する。イベントデータは、イベント発生直後に遅延なくムーバブルインクに送信されるべきである。
3. 開始時間を指定してキャンペーン期間を設定する。終了時刻は適用されない可能性が高いが、ユースケースに必要であれば設定できる。

{% alert note %}
データがリアルタイムでMovable Inkにストリーミングされるようにするには、**ローカルタイムゾーンのユーザーにキャンペーンを送信するを**選択しないこと。
{% endalert %}

#### ステップ 2b: 聴衆を特定する

次に、このキャンペーンでターゲットにしたいユーザーを決定する。詳細については、「[ユーザーをターゲットにする][4]」を参照のこと。

**コントロールグループの**チェックボックスをオフにして、キャンペーンでA/Bテストを使用しないことを確認する。コントロールグループが含まれる場合、ユーザーの何割かはMovable Inkにデータが送信されない。聴衆は全員、対照群ではなく変種に行くべきだ。

![BrazeキャンペーンにおけるA/Bテストパネル。100％のバリアント分布がバリアント1に割り当てられ、コントロールグループはない。]\[img5]

#### ステップ 2c: コンバージョンイベントを選択する（オプション）

必要であれば、Braze内でこのキャンペーンにコンバージョンイベントを割り当てることができる。

しかし、Webhookはあくまでデータをストリーミングするためのものであることを考えると、このレベルでのアトリビューションは、Brazeからの行動データがコンテンツのパーソナライズに使用された後、キャンペーンレベルでのアトリビューションを見るよりも役に立たない可能性が高い。

### ステップ3:キャンペーンを開始する

ウェブフックの設定を確認し、キャンペーンを開始する。

## 考慮事項

### 一意のユーザー識別子で整列する

`mi_u` として使用している一意のユーザー識別子（UUID）値がBraze内で利用可能であり、Movable Inkに送信されるイベントペイロードに含めることができることを確認する。

これにより、画像を生成する際にMovable Inkが参照する行動イベントが、行動イベントを受け取ったのと同じ顧客に関連付けられていることが保証される。UUID値がBraze`external_id` と同じでない場合、UUIDを取得し、属性としてBrazeに渡すか、Brazeイベントのイベントプロパティでこの識別子を活用する必要がある。

Brazeは、複数のプラットフォーム（ウェブやモバイルアプリなど）でユーザーの行動を追跡するため、1人のユーザーが複数の異なる匿名IDを持つ可能性がある。`identify` イベントが匿名識別子と単一の既知の識別子の両方を含む限り、これらのIDは、`identify` イベントがMovable Inkに送信されたときに、単一の既知のストーリーズユーザープロファイルにマージすることができる。

一旦Movable Inkが一人のユーザーについて`user_id` を受け取ると、そのユーザーに関する今後のすべてのイベントには、同じ`user_id` を含めなければならない。

### Movable Inkでイベントペイロードを共有する {#event-payloads}

Movable Inkの顧客データAPIへのコネクタを設定する前に、イベントのペイロードをMovable Inkのクライアント・エクスペリエンス・チームと共有しておくこと。これにより、Movable Inkはあなたのイベントを彼らのイベントスキーマにマッピングすることができ、APIコールの拒否や失敗を防ぐことができる。

任意のイベントプロパティを使用して、Braze内でイベントペイロードを生成できる。ランダムなユーザー、または特定のユーザーIDを検索してサンプルペイロードを生成する。詳細は上記の[ステップ1dを](#step-1d)参照のこと。

このサンプルペイロードをMovable Inkクライアントエクスペリエンスチームと共有する。サンプルのペイロードに、個人を特定できる機密情報（電子メールアドレス、電話番号、生年月日など）が含まれていないことを確認する。 

カスタムイベント・プロパティと、プロパティに含まれるデータの期待されるフォーマットの詳細については、[カスタムイベント・プロパティを][5]参照のこと。

### 既知のユーザーと匿名のユーザー

Brazeでは、匿名のユーザープロファイルでイベントを記録することができる。イベントロギング中にどの識別子がユーザープロファイルにリンクされるかは、ユーザーがどのように作成されたか（Braze SDKまたはAPIを通じて）と、ユーザーライフサイクルの現在の段階に依存する。

#### 既知のユーザーのBrazeイベントのみを転送する

ウェブフック・キャンペーンでは、`External User ID` フィルタを使用して、`External User ID` `is not blank` フィルタで`external_id` を持つユーザーのみをターゲットにする。

#### 匿名ユーザーと既知ユーザーのBrazeイベントを転送する

匿名ユーザー（プロファイルに`external_id` が割り当てられる前のユーザー）からのBrazeイベントを転送したい場合、`external_id` が利用可能になるまで、Movable Inkの`anonymous_id` として使用する識別子を決定する必要がある。Brazeユーザープロフィールに常に表示される`anonymous_id` 。Webhook 本体の Liquid ロジックを使って、`anonymous_id` と`user_id` のどちらを渡すかを決めることができる。

詳しくは、[サンプルペイロードの](#sample-payloads)下にあるサンプルウェブフックを参照のこと。

## ペイロードの例

### プロダクト・ビュー・イベント

{% tabs ローカル %}
{% tab ブレイズ・トリガー・イベント例 %}

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
{% tab 予想される可動インク要求ペイロード %}

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
{% tab ブレイズ・トリガー・イベント例 %}

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
{% tab 予想される可動インク要求ペイロード %}

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
{% tab ブレイズ・トリガー・イベント例 %}

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
{% tab 予想される可動インク要求ペイロード %}

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



[1]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/
[2]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types
[3]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/
[4]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/
[5]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties
\[img1] ： {% image_buster /assets/img/movable_ink/cd_api_webhook_url.png %}
\[img2] ： {% image_buster /assets/img/movable_ink/cd_api_webhook_settings.png %}
\[img3] ： {% image_buster /assets/img/movable_ink/cd_api_webhook_kvp.png %}
\[img4] ： {% image_buster /assets/img/movable_ink/cd_api_webhook_response.png %}
\[img5] ： {% image_buster /assets/img/movable_ink/cd_api_webhook_ab.png %}
