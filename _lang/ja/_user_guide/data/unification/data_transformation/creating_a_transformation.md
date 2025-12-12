---
nav_title: 変換の作成
article_title: 変換の作成
page_order: 1
page_type: reference
description: "このリファレンス記事では、Braze Data Transformation を使用して変換を作成するステップについて説明します。"
---

# 変換の作成

> Braze Data Transformation を使用すると、Webhook 連携の構築および管理を行って、外部プラットフォームから Braze へのデータフローを自動化できます。これらの Webhook 連携により、さらに洗練されたマーケティングユースケースを強化できます。データ変換によって、デフォルトのコードからデータ変換を構築したり、専用のテンプレートライブラリを用いて特定の外部プラットフォームの使用を開始したりできます。

## 前提条件 

| 必要条件 | 説明 |
| --- | --- |
| 二要素認証またはSSO | アカウントで[二要素認証]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#two-factor-authentication)（2FA）または[シングルサインオン]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#single-sign-on-sso-authentication)（SSO）を有効にする必要がある。 |
| 正しい許可 | アカウント管理者またはワークスペース管理者であるか、または「変換の管理」ユーザー権限が必要です。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## ステップ 1: ソースプラットフォームの特定

Braze に接続する外部プラットフォームを特定し、プラットフォームが Webhook に対応しているか確認します。これらの設定は、「API 通知」や「Web サービスリクエスト」と呼ばれることもあります。

以下に [Typeform webhook](https://www.typeform.com/help/a/webhooks-360029573471/) の例を示します。これは、Typeform のプラットフォームにログインすることで設定できます。

![]({% image_buster /assets/img/data_transformation/data_transformation8.png %})

## ステップ 2: 変換の作成

{% multi_lang_include create_transformation.md location="default" %}

## ステップ 3: テスト Webhook の送信 (推奨)

このステップは任意ですが、新規に作成した変換にソースプラットフォームからテスト Webhook を送信することをお勧めします。

1. URL を変換からコピーします。
2. ソースプラットフォームで、この URL に送信するサンプル Webhook を生成する「テスト送信」機能を見つけます。 
- ソースプラットフォームにリクエストタイプを求められた場合は、「**POST**」を選択します。
- ソースプラットフォームに認証オプションがある場合は、「**認証なし**」を選択します。
- ソースプラットフォームにシークレットを求められた場合は、「**シークレットなし**」を選択します。
3. Brazeダッシュボードでページを更新し、Webhookが受信されたか確認する。受信した場合は、「**Most recent webhook**」の下にWebhookペイロードが表示されるはずだ。

Typeform の場合は以下のようになります。

![WebhookをBraze ユーザープロファイル s にマップするデータトランスフォーメーションコードの例。]({% image_buster /assets/img/data_transformation/data_transformation11.png %})

{% alert note %}
Braze Data Transformation は、Webhook に特別な検証や認証を必要とする外部プラットフォームをまだサポートしていない可能性があります。Braze Data Transformation でこのタイプのプラットフォームを使用することに関心がある場合は、[製品フィードバック]({{site.baseurl}}/user_guide/administrative/access_braze/portal/)を残すことを検討してください。
{% endalert %}

## ステップ 4: 変換コードの記述

JavaScript コードを扱ったことがほとんどないか、より詳しい手順を希望する場合は、変換コードを記述するときに、「**初心者 - POST: ユーザーの追跡**」または「**初心者 - PUT:複数のカタログ項目を更新する** 変換コードを書くためのタブ。

開発者であるか、JavaScript コードの経験が豊富な場合は、「**上級 - POST: ユーザーの追跡**」タブで、変換コードを記述するための大まかな手順を確認できます。

{% alert tip %}
Braze Data Transformation には、ChatGPT にコードの作成支援を依頼する AI コパイロットが用意されています。AI コパイロットにアクセスするには、<i class="fa-solid fa-wand-magic-sparkles"></i> [**変換コードを生成**] を選択します。これを使用するには、変換に Webhook を送信する必要があります。テンプレートライブラリにアクセスするには、[**コードを挿入**] > [**テンプレートを挿入**] を選択します。

![]({% image_buster /assets/img/data_transformation/data_transformation3.png %})
{% endalert %}

{% tabs %}
{% tab Beginner - Track users %}

ここでは、さまざまなWebhook値をBrazeユーザープロファイルにマッピングする方法を定義する変換コードを記述する。

1. 新しいトランスフォームには、**トランスフォームコードセクションに**このデフォルトテンプレートがある：

```java
// Here, we will define a variable, "brazecall", to build up a `/users/track` request
// Everything from the incoming webhook is accessible via the special variable "payload"
// So you can template in desired values in your `/users/track` request with dot notation, such as payload.x.y.z

let brazecall = {
  "attributes": [
    {
      "external_id": payload.user_id,
      "_update_existing_only": true,
      "attribute_1": payload.attribute_1
    }
  ],
  "events": [
    {
      "external_id": payload.user_id,
      "_update_existing_only": true,
      "name": payload.event_1,
      "time": new Date(),
      "properties": {
        "property_1": payload.event_1.property_1
      }
    }
  ],
  "purchases": [
    {
      "external_id": payload.user_id,
      "_update_existing_only": true,
      "product_id": payload.product_id,
      "currency": payload.currency,
      "price": payload.price,
      "quantity": payload.quantity,
      "time": payload.timestamp,
      "properties": {
        "property_1": payload.purchase_1.property_1
      }
    }
  ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{:start="2"}
2\.変換呼び出しにカスタム属性、カスタムイベント、購入を含めるには、ステップ3に進みます。それ以外の場合は、不要なセクションを削除します。<br><br>
3\.属性、イベント、および購入の各オブジェクトには、`external_id`、`user_alias`、`braze_id`、`email`、または `phone` のいずれかのユーザー識別子が必要です。受信 Webhook のペイロード内でユーザー識別子を見つけ、ペイロード行を介して変換コード内のその値をテンプレート化します。ペイロードオブジェクトのプロパティにアクセスするには、ドット表記を使用します。<br><br>
4. 属性、イベント、または購入として表現する Webhook の値を見つけて、ペイロード行を介して変換コード内のそれらの値をテンプレート化します。ペイロードオブジェクトのプロパティにアクセスするには、ドット表記を使用します。<br><br>
5. 属性、イベント、および購入の各オブジェクトについて、`_update_existing_only` の値を調べます。存在しない可能性のある新規ユーザーを変換で作成する場合は、この値を `false` に設定します。既存のプロファイルのみを更新する場合は、`true` のままにします。<br><br>
6. [**検証**] をクリックして、コードの出力のプレビューを返し、受け入れられる `/users/track` リクエストであるかどうかを確認します。<br><br>
7. 変換をアクティブにします。アクティブにする前のコードに関するその他のサポートについては、Braze アカウントマネージャーにお問い合わせください。<br><br>
7. ソースプラットフォームから Webhook の送信を開始します。Webhook が着信するたびに変換コードが実行され、ユーザープロファイルの更新が開始されます。 

これで Webhook との連携が完了しました。

{% endtab %}
{% tab Beginner - Update catalog items %}

ここでは、さまざまなWebhookの値をBrazeカタログアイテムの更新にどのようにマッピングするかを定義する変換コードを書くことができる。

1. 新規の変換では、[**変換コード**] セクションに次のデフォルトテンプレートがあります。

```java
// This is a default template that you can use as a starting point
// Feel free to delete this entirely to start from scratch, or to edit specific components

// First, this code defines a variable, "brazecall", to build a PUT /catalogs/{catalog_name}/items request
// Everything from the incoming webhook is accessible via the special variable "payload"
// As such, you can template in desired values in your request with JS dot notation, such as payload.x.y.z

let brazecall = {
  // For Braze Data Transformation to update Catalog items, the special variable "catalog_name" is required
  // This variable is used to specify the catalog name which would otherwise go in the request URL
  "catalog_name": "catalog_name",
  
  // After defining "catalog name", construct the Update Multiple Catalog Items request as usual below
  // Documentation for the destination endpoint: https://www.braze.com/docs/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items/
  "items": [
    {
      "id": payload.item_id_1,
      "catalog_column1": "string",
      "catalog_column2": 1,
      "catalog_column3": true,
      "catalog_column4": "2021-09-03T09:03:19.967+00:00",
      "catalog_column5": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      }
    },
    {
      "id": payload.item_id_2,
      "catalog_column1": "string",
      "catalog_column2": 1,
      "catalog_column3": true,
      "catalog_column4": "2021-09-03T09:03:19.967+00:00",
      "catalog_column5": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      }
    },
    {
      "id": payload.item_id_3,
      "catalog_column1": "string",
      "catalog_column2": 1,
      "catalog_column3": true,
      "catalog_column4": "2021-09-03T09:03:19.967+00:00",
      "catalog_column5": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      }
    }
  ]
};

// After the request body is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{:start="2"}
2\.`/catalogs` の宛先の変換には、更新する特定のカタログを定義する `catalog_name` が必要です。このフィールドをハードコードするか、ペイロード行を介して Webhook フィールドでフィールドをテンプレート化することができます。ペイロードオブジェクトのプロパティにアクセスするには、ドット表記を使用します。<br><br>
3\.カタログのどの項目を更新したいかを、items 配列の `id` フィールドで定義します。これらのフィールドはハードコードするか、ペイロード行を介して Webhook フィールドでテンプレート化することもできます。<br><br> `catalog_column` はプレースホルダーの値であることに留意してください。アイテムオブジェクトは、カタログに存在するフィールドのみを含むようにする。<br><br>
4. [**検証**] を選択して、コード出力のプレビューを返し、[「複数のカタログ項目の更新」エンドポイント]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items)で受け入れ可能なリクエストであるかどうかを確認します。<br><br>
5. 変換をアクティブにします。アクティブにする前のコードに関するその他のサポートについては、Braze アカウントマネージャーにお問い合わせください。<br><br>
6. ソースプラットフォームに Webhook の送信を開始する設定があるかどうかを確認してください。Webhook が着信するたびに変換コードが実行され、カタログ項目の更新が開始されます。

これで Webhook との連携が完了しました。

{% endtab %}
{% tab Advanced - Track users %}

このステップでは、WebhookペイロードをソースプラットフォームからJavaScriptオブジェクトの戻り値に変換する。この戻り値は、`/users/track` エンドポイントリクエストの本文の形式に準拠している必要があります。

- 変換コードは JavaScript プログラミング言語で受け入れられます。if/else ロジックなど、標準的な JavaScript 制御フローがすべてサポートされています。
- 変換コードは、`payload` 変数を介して Webhook リクエスト本文にアクセスします。この変数は、リクエスト本文の JSON を解析して読み込まれたオブジェクトです。
- `/users/track` エンドポイントでサポートされるすべてのフィーチャーがサポートされています。例を示します。
  - ユーザー属性オブジェクト、イベントオブジェクト、購入オブジェクト
  - 階層化属性と階層化カスタムイベントプロパティ
  - サブスクリプショングループの更新
  - 識別子としてのメールアドレス

[**検証**] を選択すると、コードの出力のプレビューが返され、`/users/track` リクエストとして受け入れられるかどうかがチェックされます。

{% alert note %}
外部ネットワークリクエスト、サードパーティライブラリ、また JSON 以外の Webhook は現在サポートされていません。
{% endalert %}

{% endtab %}
{% endtabs %}

## ステップ 5: 変換の監視

変換をアクティブにしたら、メインの [**変換**] ページの分析を参照して、パフォーマンスの概要を確認します。

* **受信リクエスト:**この変換の URL で受信した Webhook の数です。受信リクエストが 0 の場合、ソースプラットフォームが Webhook を送信していないか、接続を確立できません。
* **配信数:**受信リクエストをを受け取った後、Data Transformation は変換コードを適用して、選択されている Braze の宛先に送信します。

配信に至る受信リクエストが 100% になることは、良い目標です。配信数が受信リクエスト数を超えることはありません。

### トラブルシューティング

詳細な監視とトラブルシューティングについては、[**ログ**] ページで特定のログを参照してください。このページには、すべてのワークスペースのすべての変換に対する最新 1,000 件の受信リクエストが記録されます。各ログを選択すると、受信リクエストの本文、変換出力、および変換の送信先からの応答本文を表示できます。

配信がない場合は、変換コードに構文エラーがないかチェックし、コードがコンパイルされることを確認する。次に、出力が有効な宛先リクエストであるかどうかを確認します。

受信リクエスト数より少ない配信数は、少なくともいくつかのWebhookが正常に配信されていることを示す。エラー例については変換ログを参照し、変換出力が意図どおりかを確認します。変換コードが、受信した Webhook の個々のバリエーションに対応していない可能性があります。


