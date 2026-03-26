---
nav_title: "POST:カタログセレクションを作成する"
article_title: "POST:カタログセレクションを作成する"
search_tag: エンドポイント
page_order: 2

layout: api_page
page_type: reference
description: "この記事では、「カタログセレクションの作成」Braze エンドポイントの詳細について説明します。"

---
{% api %}
# カタログセレクションを作成する
{% apimethod post %}
/catalogs/{catalog_name}/selections
{% endapimethod %}

> このエンドポイントを使用して、カタログにセレクションを作成する。

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`catalogs.create_selection`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog selections' %}

## パスパラメーター

| パラメータ      | 必須かどうか | データ型 | 説明          |
| -------------- | -------- | --------- | -------------------- |
| `catalog_name` | 必須かどうか | 文字列    | カタログ名。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## リクエストパラメーター

| パラメーター   | 必須かどうか | データ型 | 説明                                                                                                                                                        |
| ----------- | -------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `selection` | 必須 | オブジェクト    | 選択基準を含むオブジェクト。オブジェクトとそのフィールドの詳細な内訳については、[カタログ選択オブジェクトを]({{site.baseurl}}/api/objects_filters/catalog_selection_object/)参照せよ。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### 選択オブジェクトのパラメータ

| パラメーター        | 必須かどうか | データ型 | 説明                                                                                                                                                        |
| ---------------- | -------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `name`           | 必須かどうか | string    | カタログ選択の名前。 |
| `description`    | オプション | string    | カタログ選択の説明。 |
| `external_id`    | 必須かどうか | string    | 選択範囲の固有識別子。 |
| `source`         | 必須かどうか | string    | カタログデータの出典。Shopifyカタログには、. を使用する`"Shopify"`。カスタムカタログには、. を使用する`"custom"`。 |
| `filters`        | オプション | 配列    | カタログアイテムに適用するフィルターオブジェクトの配列。リクエストごとに最大4つのフィルターを指定できる。フィルターが指定されていない場合、カタログ内の全アイテムが含まれる。 |
| `results_limit`  | オプション | 整数   | 返す結果の最大数。1から50までの数字でなければならない。 |
| `sort_field`     | オプション | string    | 結果を並べ替えるためのフィールド。これはと組み合わせなければならない`sort_order`。と`sort_order``sort_field`の両方が存在しない場合、結果はランダム化される。 |
| `sort_order`     | オプション | string    | 結果を並べ替える順序だ。有効な値は (昇順) `"asc"`または`"desc"`(降順) である。これはと組み合わせなければならない`sort_field`。と`sort_order``sort_field`の両方が存在しない場合、結果はランダム化される。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert note %}
と`sort_order``sort_field`パラメータは必ず一緒に使わなければならない。一方のパラメータだけを提供した場合、あるいは両方のパラメータを省略した場合、選択結果はランダムな順序で返される。
{% endalert %}

## リクエスト例

```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs/restaurants/selections' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "selection": {
    "name": "favorite-restaurants",
    "description": "Favorite restaurants in NYC",
    "external_id": "favorite-nyc-restaurants",
    "source": "custom",
    "filters": [
      {
        "field": "City",
        "operator": "equals",
        "value": "NYC"
      },
      {
        "field": "Rating",
        "operator": "greater than",
        "value": 7
      }
    ],
    "results_limit": 10,
    "sort_field": "Rating",
    "sort_order": "desc"
  }
}'
```

### フィルター演算子

| フィールドタイプ | 対応オペレーター                                     |
| ---------- | ------------------------------------------------------- |
| `string`   | `equals`, `does not equal`                              |
| `number`   | `equals``does not equal`,`greater than` 、 `less than` |
| `boolean`  | `is`                                                    |
| `time`     | `before`, `after`                                       |
| `array`    | `includes value`, `does not include value`              |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
APIは、1回の選択リクエストにつき最大4つのフィルターをサポートする。Brazeのダッシュボードでは、各選択項目につき最大10個のフィルターを追加できる。フィルターは配列に現れる順序で適用される。
{% endalert %}

## 応答

このエンドポイントには、`202`、`400`、`404` という 3 つのステータスコード応答があります。

### 成功応答の例

ステータスコード `202` は、次の応答本文を返す可能性があります。

```json
{
  "message": "success"
}
```

### エラー応答例

ステータスコード `400` は、次の応答本文を返す可能性があります。遭遇する可能性のあるエラーの詳細については、「[トラブルシューティング](#troubleshooting)」を参照のこと。

```json
{
  "errors": [
    {
      "id": "catalog-not-found",
      "message": "Could not find catalog",
      "parameters": [
        "catalog_name"
      ],
      "parameter_values": [
        "restaurants"
      ]
    }
  ],
  "message": "Invalid Request"
}
```

## トラブルシューティング

次のテーブルに、返される可能性のあるエラーと、関連するトラブルシューティングステップを示します。

| エラー                                | トラブルシューティング                                                                               |
|--------------------------------------|-----------------------------------------------------------------------------------------------|
| `catalog-not-found`                  | カタログ名が有効であることを確認する。                                                         |
| `company-size-limit-already-reached` | カタログのストレージサイズの上限に達しています。                                                    |
| `selection-limit-reached`            | カタログの選択数が制限に達した。                                                      |
| `invalid-selection`                  | 選択が有効であることを確認する。                                                            |
| `too-many-filters`                   | 選択範囲にフィルターが多すぎないかチェックする。                                                  |
| `selection-name-already-exists`      | 選択名がカタログにすでに存在するかどうかをチェックする。                                    |
| `selection-has-invalid-filter`       | 選択フィルターが有効かどうかをチェックする。                                                       |
| `selection-invalid-results-limit`    | 選考結果の上限が有効かどうかをチェックする。                                                |
| `invalid-sorting`                    | 選択ソートが有効かどうかをチェックする。                                                      |
| `invalid-sort-field`                 | 選択ソートフィールドが有効かどうかをチェックする。                                                   |
| `invalid-sort-order`                 | 選択のソート順が有効かどうかをチェックする。                                                   |
| `selection-contains-too-many-arrays` | 選択範囲に`array` 型のフィールドが複数含まれているかどうかをチェックする。サポートされているのは1つのみです。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
