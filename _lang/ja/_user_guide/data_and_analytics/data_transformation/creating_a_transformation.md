---
nav_title: 変換の作成
article_title: 変換の作成
page_order: 1
page_type: reference
description: "このリファレンス記事では、Braze Data Transformation を使用して変換を作成するステップについて説明します。"
---

# 変換の作成

> Braze Data Transformation を使用すると、Webhook 連携の構築および管理を行って、外部プラットフォームから Braze へのデータフローを自動化できます。これらの Webhook 連携により、さらに洗練されたマーケティングユースケースを強化できます。

## 前提条件 

| 要件 | 説明 |
| --- | --- |
| 2 要素認証またはSSO | アカウントで [2 要素認証]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#two-factor-authentication) (2FA) または[シングルサインオン]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#single-sign-on-sso-authentication) (SSO) を有効にする必要があります。 |
| 正しい権限 | アカウント管理者またはワークスペース管理者であるか、または「変換の管理」ユーザー権限が必要です。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## ステップ 1: ソースプラットフォームの特定

Braze に接続する外部プラットフォームを特定し、プラットフォームが Webhook に対応しているか確認します。これらの設定は、「API 通知」や「Web サービスリクエスト」と呼ばれることもあります。

以下に [Typeform webhook](https://www.typeform.com/help/a/webhooks-360029573471/) の例を示します。これは、Typeform のプラットフォームにログインすることで設定できます。

![][9]

## ステップ 2: 変換の作成

{% multi_lang_include create_transformation.md location="default" %}

## ステップ 3: テスト Webhook の送信 (推奨)

このステップは任意ですが、新規に作成した変換にソースプラットフォームからテスト Webhook を送信することをお勧めします。 

1. URL を変換からコピーします。
2. ソースプラットフォームで、この URL に送信するサンプル Webhook を生成する「テスト送信」機能を見つけます。 
- ソースプラットフォームにリクエストタイプを求められた場合は、「**POST**」を選択します。
- ソースプラットフォームに認証オプションがある場合は、「**認証なし**」を選択します。
- ソースプラットフォームにシークレットを求められた場合は、「**シークレットなし**」を選択します。
3. Braze でページを更新して、Webhook を受信したかどうかを確認します。受信した場合は、[最新の Webhook] の下に Webhook のペイロードが表示されるはずです。

Typeform の場合は以下のようになります。<br>![][12]

{% alert note %}
Braze Data Transformation は、Webhook に特別な検証や認証を必要とする外部プラットフォームをまだサポートしていない可能性があります。Braze Data Transformation でこのタイプのプラットフォームを使用することに関心がある場合は、[製品フィードバック]({{site.baseurl}}/user_guide/administrative/access_braze/portal/)を残すことを検討してください。
{% endalert %}

## ステップ 4: 変換コードの記述

JavaScript コードを扱ったことがほとんどないか、より詳しい手順を希望する場合は、変換コードを記述するときに、「**初心者 - POST: ユーザーの追跡**」または「**初心者 - PUT: カタログ項目の更新**」タブの手順に従ってください。

開発者であるか、JavaScript コードの経験が豊富な場合は、「**上級 - POST: ユーザーの追跡**」タブで、変換コードを記述するための大まかな手順を確認できます。

{% alert tip %}
Braze Data Transformation には、デフォルトのテンプレートを使用する代わりに、ChatGPT にコードの作成支援を依頼する AI コパイロットがあります。AI コパイロットにアクセスするには、<i class="fa-solid fa-wand-magic-sparkles"></i> [**変換コードを生成**] をクリックします。これを使用するには、変換に Webhook を送信する必要があります。

![\]({% image_buster /assets/img/data_transformation/data_transformation3.png %})
{% endalert %}

{% tabs %}
{% tab Beginner - POST: Track users %}

ここでは、さまざまな Webhook の値を Braze のユーザープロファイルにマッピングする方法を定義する変換コードを記述します。

1. 新規の変換では、[**変換コード**] セクションに次のデフォルトテンプレートがあります。
    \`\`\`
    // ここでは、`/users/track` リクエストを作成するために、変数「brazecall」を定義します。
    // Everything from the incoming webhook is accessible via the special variable "payload"
// So you can template in desired values in your `/users/track` リクエスト、payload.x.y.z のようなドット表記

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

    // After the/users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
    return brazecall;
    \`\`\`

2. 変換呼び出しに 3 つすべて (カスタム属性、カスタムイベント、購入) が必要な場合は、ステップ 3 に進みます。それ以外の場合は、不要なセクションを削除します。<br><br>
3. 属性、イベント、および購入の各オブジェクトには、`external_id`、`user_alias`、`braze_id`、`email`、または `phone` のいずれかのユーザー識別子が必要です。受信 Webhook のペイロード内でユーザー識別子を見つけ、ペイロード行を介して変換コード内のその値をテンプレート化します。ペイロードオブジェクトのプロパティにアクセスするには、ドット表記を使用します。<br><br>
4. 属性、イベント、または購入として表現する Webhook の値を見つけて、ペイロード行を介して変換コード内のそれらの値をテンプレート化します。ペイロードオブジェクトのプロパティにアクセスするには、ドット表記を使用します。<br><br>
5. 属性、イベント、および購入の各オブジェクトについて、`_update_existing_only` の値を調べます。存在しない可能性のある新規ユーザーを変換で作成する場合は、この値を `false` に設定します。既存のプロファイルのみを更新する場合は、`true` のままにします。<br><br>
6. [**検証**] をクリックして、コードの出力のプレビューを返し、受け入れられる `/users/track` リクエストであるかどうかを確認します。<br><br>
7. 変換をアクティブにします。アクティブにする前のコードに関するその他のサポートについては、Braze アカウントマネージャーにお問い合わせください。<br><br>
7. ソースプラットフォームから Webhook の送信を開始します。Webhook が着信するたびに変換コードが実行され、ユーザープロファイルの更新が開始されます。 

これで Webhook との連携が完了しました。

{% endtab %}
{% tab Beginner - PUT: Update catalog item %}

ここでは、さまざまな Webhook の値を Braze カタログ項目の更新にマッピングする方法を定義する変換コードを記述します。

1. 新規の変換では、[**変換コード**] セクションに次のデフォルトテンプレートがあります。
    \`\`\`
    // This is a default template that you can use as a starting point
// Feel free to delete this entirely to start from scratch, or to edit specific components


    // First, this code defines a variable, "brazecall", to build a PUT /catalogs/{catlalog_name}/items/{item_id} request
    // Everything from the incoming webhook is accessible via the special variable "payload"
// As such, you can template in desired values in your request with JS dot notation, such as payload.x.y.z


    let brazecall = {
// For Braze Data Transformations to update Catalog items, the special variables "catalog_name" and "item_id" are required
// These variables are used to specify the catalog name and item ID which would otherwise go in the request URL
"catalog_name": "catalog_name",
"item_id": payload.item_id,
// After the special variables, construct the Catalogs update request as usual below
"items": [
      {
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

    // リクエスト本文が brazecall に割り当てられた後、出力を作成するために明示的に brazecall を返します
    return brazecall;
    \`\`\`

2. `/catalogs` の送信先の変換には、更新する特定のカタログと項目を定義するための `catalog_name` と `item_id` が必要です。これらの値をハードコードしたり、ペイロード行からの Webhook の値を持つ値の中にテンプレート化したりできます。ペイロードオブジェクトのプロパティにアクセスするには、ドット表記を使用します。<br><br>
3. items 配列を変更して `item_id` を更新する方法を定義します (このセクションのステップ 2 から)。ここでも、これらの値をハードコードしたり、ペイロード行からの Webhook の値の中にテンプレート化したりできます。<br><br> Braze カタログをテーブルと見なす場合、`item_id` はカタログ内の行であり、項目オブジェクト (「catalog_column1」で始まる) はその行の列値です。「catalog\_column1」はプレースホルダーなので、カタログにはこのフィールドがないこともあります。項目オブジェクトには、カタログに存在するフィールドのみを含める必要があります。<br><br>
4. [検証] をクリックして、コード出力のプレビューを返し 、[カタログ項目の更新] エンドポイントで受け入れ可能なリクエストであるかどうかを確認します。<br><br>
5. 変換をアクティブにします。アクティブにする前のコードに関するその他のサポートについては、Braze アカウントマネージャーにお問い合わせください。<br><br>
6. ソースプラットフォームに Webhook の送信を開始する設定があるかどうかを確認してください。Webhook が着信するたびに変換コードが実行され、カタログ項目の更新が開始されます。

これで Webhook との連携が完了しました。

{% endtab %}
{% tab Advanced - POST: Track users %}

このステップでは、ソースプラットフォームからの Webhook ペイロードを、JavaScript オブジェクトの戻り値に変換します。この戻り値は、Brazeの `/users/track` リクエストの本文フォーマットに準拠しなければなりません。

- 変換コードは JavaScript プログラミング言語で受け入れられます。if/else ロジックなど、標準的な JavaScript 制御フローがすべてサポートされています。
- 変換コードは、`payload` 変数を介して Webhook リクエスト本文にアクセスします。この変数は、リクエスト本文の JSON を解析して読み込まれたオブジェクトです。
- `/users/track` エンドポイントでサポートされるすべてのフィーチャーがサポートされています。例を示します。
  - ユーザー属性オブジェクト、イベントオブジェクト、購入オブジェクト
  - 階層化属性と階層化カスタムイベントプロパティ
  - サブスクリプショングループの更新
  - 識別子としてのメールアドレス

[**検証**] をクリックして、コード出力のプレビューを返し、受け入れられる `/users/track` リクエストであるかどうかを確認します。

{% alert note %}
外部ネットワークリクエスト、サードパーティライブラリ、また JSON 以外の Webhook は現在サポートされていません。
{% endalert %}

{% endtab %}
{% endtabs %}

## ステップ 5: 変換の監視

変換をアクティブにしたら、メインの [**変換**] ページの分析を参照して、パフォーマンスの概要を確認します。

* **受信リクエスト:** この変換の URL で受信した Webhook の数です。受信リクエストが 0 の場合、ソースプラットフォームが Webhook を送信していないか、接続を確立できません。
* **配信数:** 受信リクエストをを受け取った後、Data Transformation は変換コードを適用して、選択されている Braze の宛先に送信します。

配信に至る受信リクエストが 100% になることは、良い目標です。配信数が受信リクエスト数を超えることはありません。

詳細な監視とトラブルシューティングについては、特定のログの**ログ**ページを参照してください。ログには、すべてのワークスペースのすべての変換に対する最新 1,000 件の受信リクエストが記録されます。各ログをクリックすると、受信リクエストの本文、変換出力、および変換の送信先からの応答本文を表示できます。これらの詳細を使用して、エラーのトラブルシューティングができます。

### トラブルシューティング

- 配信数が 0 の場合は、変換コードをチェックして構文エラーがないこと、コンパイルされていることを確認してください。次に、出力が有効な宛先リクエストであるかどうかを確認します。
- 配信数が受信リクエスト数より少ない場合は、少なくとも一部の Webhook が正常に配信されていることを示しています。エラー例については変換ログを参照し、変換出力が意図どおりかを確認します。変換コードが、受信した Webhook の個々のバリエーションに対応していない可能性があります。


[4]: {% image_buster /assets/img/data_transformation/data_transformation3.png %}
[5]: {% image_buster /assets/img/data_transformation/data_transformation4.png %}
[6]: {% image_buster /assets/img/data_transformation/data_transformation5.png %}
[7]: {% image_buster /assets/img/data_transformation/data_transformation6.jpg %}
[8]: {% image_buster /assets/img/data_transformation/data_transformation7.png %}
[9]: {% image_buster /assets/img/data_transformation/data_transformation8.png %}
[10]: {% image_buster /assets/img/data_transformation/data_transformation9.png %}
[12]: {% image_buster /assets/img/data_transformation/data_transformation11.png %}
