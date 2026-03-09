---
nav_title: "カタログ選択オブジェクト"
article_title: APIカタログ選択オブジェクト
page_order: 12
page_type: reference
description: "この参照記事は、カタログ選択オブジェクトの構成要素について説明する。"
tool: Catalogs

---

# カタログ選択オブジェクト

> カタログ選択を作成する際には、選択オブジェクトを提供することで、カタログから返されるアイテムに対するフィルター、ソート、および制限の基準を定義できる。

この`selection`オブジェクトは、フィルターに基づいてカタログから選択対象とするアイテムを指定し、それらの並べ替え方法や返す結果の数を設定することを可能にする。このオブジェクトは、APIを通じてカタログ選択を作成する際に使用する。

## オブジェクト本体

```json
{
  "selection": {
    "name": "Sale",
    "description": "Sales Collection",
    "external_id": "12345678",
    "source": "Shopify",
    "filters": [
      {
        "field": "collection",
        "operator": "includes value",
        "value": "Best Seller"
      },
      {
        "field": "collection",
        "operator": "does not include value",
        "value": "Sale"
      }
    ],
    "results_limit": 5,
    "sort_field": "id",
    "sort_order": "asc"
  }
}
```

## オブジェクトの詳細

| キー | 必須かどうか | データ型 | 説明 |
| --- | -------- | --------- | ----------- |
| `name` | 必須かどうか | string | カタログ選択の名前。 |
| `description` | オプション | string | カタログ選択の説明。 |
| `external_id` | 必須かどうか | string | 選択範囲の固有識別子。 |
| `source` | 必須かどうか | string | カタログデータの出典。Shopifyカタログについては、これを.`"Shopify"`に設定する。Shopify以外のカタログについては、説明的な文字列（例：）`"custom"`または統合の名前を使用する。 |
| `filters` | オプション | オブジェクト配列 | カタログアイテムに適用するフィルターオブジェクトの配列。リクエストごとに最大4つのフィルターを指定できる。フィルターが指定されていない場合、カタログ内の全アイテムが含まれる。 |
| `results_limit` | オプション | 整数 | 返す結果の最大数。1から50までの数字でなければならない。 |
| `sort_field` | オプション | string | 結果を並べ替えるためのフィールド。これはと組み合わせなければならない`sort_order`。と`sort_order`の`sort_field`両方が指定されていない場合、結果はランダムな順序で返される。 |
| `sort_order` | オプション | string | 結果を並べ替える順序だ。有効な値は (昇順) `"asc"`または`"desc"`(降順) である。これはと組み合わせなければならない`sort_field`。と`sort_order`の`sort_field`両方が指定されていない場合、結果はランダムな順序で返される。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### フィルターオブジェクト

配列`filters`内の各フィルターオブジェクトは、以下の表で説明されているフィールドを含む。

| キー | 必須かどうか | データ型                                   | 説明 |
| --- | -------- | ------------------------------------------- | ----------- |
| `field`    | 必須かどうか | string                                      | フィルタリング対象のカタログフィールド。 |
| `operator` | 必須かどうか | string                                      | フィルターに使用する比較演算子。例としては`"includes value"`、とがある`"does not include value"`。 |
| `value`    | 必須かどうか | 異なる（文字列、数値、ブール値、時刻）     | 比較対象となる値。これは基となるカタログフィールドのデータ型（例：文字列、数値、ブール値、時刻）と一致しなければならない。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert note %}
APIは、1回の選択リクエストにつき最大4つのフィルターをサポートする。Brazeのダッシュボードでは、各選択項目につき最大10個のフィルターを追加できる。フィルターは配列に現れる順序で適用される。
{% endalert %}
