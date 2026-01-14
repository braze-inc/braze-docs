---
nav_title: "接続オーディエンスフィルターとオブジェクト"
article_title: API接続オーディエンス・オブジェクト
page_order: 3
page_type: reference
description: "この記事では、接続オーディエンスオブジェクトのさまざまなコンポーネントと、それを作成するフィルターについて説明します。"

---

# 接続されたオーディエンスオブジェクト

> 接続されたオーディエンス・オブジェクトは、あなたのメッセージのオーディエンスを識別する。例えば、カスタム属性配列を使ってユーザーがお気に入りしたすべてのカテゴリーとテレビ番組をトラッキングすれば、コネクテッドオーディエンスを使用して、新しいエピソードがリリースされるたびに、その番組をお気に入りした人にプッシュ通知やメールを自動的に送ることができる。

このオブジェクトは、`AND` または `OR` 演算子を使用した論理式で、1つの接続オーディエンスフィルター、または複数の接続オーディエンスフィルターで構成されます。

**複数フィルターの例：**

```json
{
  "AND":
    [
      Connected Audience Filter,
      {
        "OR" :
          [
            Connected Audience Filter,
            Connected Audience Filter
          ]
      },
      Connected Audience Filter
    ]
}
```

## 接続オーディエンスフィルター

複数のカスタム属性フィルターを`AND` および`OR` 演算子と組み合わせることで、接続されたオーディエンスフィルターが作成される。

### カスタム属性フィルター

このフィルターによって、ユーザーのカスタム属性に基づいてセグメント化することができる。これらのフィルターには最大3つのフィールドが含まれる：

```json
{
  "custom_attribute":
    {
      "custom_attribute_name": (String) the name of the custom attribute to filter on,
      "comparison": (String) one of the allowed comparisons to make against the provided value,
      "value": (String, Numeric, Boolean) the value to be compared using the provided comparison
    }
}
```

#### データ型による比較を許可する

カスタム属性のデータ型は、与えられたフィルターで有効な比較を決定する。

| カスタム属性タイプ | 許容される比較 |
| ---------------------| --------------- |
| 文字列 | `equals``not_equal`,`matches_regex`,`does_not_match_regex`,`exists` 、 `does_not_exist` |
| 配列 | `includes_value``does_not_include_value`,`exists` 、 `does_not_exist` |
| 数値 | `equals``not_equal`,`greater_than`,`greater_than_or_equal_to`,`less_than`,`less_than_or_equal_to`,`exists` 、 `does_not_exist` |
| ブール値 | `equals``does_not_equal`,`exists` 、 `does_not_exist` |
| 時刻 | `less_than_x_days_ago``greater_than_x_days_ago`,`less_than_x_days_in_the_future`,`greater_than_x_days_in_the_future`,`after`,`before`,`exists` 、 `does_not_exist` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### 属性比較の注意点

| 比較 | その他の考慮事項 |
| --- | --- |
| `value` | `exists` または `does_not_exist` の比較を使用する場合、`value` は必要ありません。`before` および `after` の比較を使用する場合、`value` は ISO 8601 日時文字列である必要があります。 |
|`matches_regex` | `matches_regex` 比較を使う場合、渡される値は文字列でなければならない。Braze での正規表現の使用については、[正規表現]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/#regex-with-braze)と[カスタム属性のデータ型]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#custom-attribute-data-types)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### カスタム属性の例

```json
{
  "custom_attribute":
    {
      "custom_attribute_name": "eye_color",
      "comparison": "equals",
      "value": "blue"
    }
}

{
  "custom_attribute":
  {
    "custom_attribute_name": "favorite_foods",
    "comparison": "includes_value",
    "value": "pizza"
  }
}

{
  "custom_attribute":
  {
    "custom_attribute_name": "last_purchase_time",
    "comparison": "less_than_x_days_ago",
    "value": 2
  }
}
```
### プッシュ通知のサブスクリプションのフィルター

このフィルターによって、ユーザーのプッシュ通知のサブスクリプションステータスに基づいてセグメント化することができます。

#### フィルター本文

```json
{
  "push_subscription_status":
  {
    "comparison": (String) one of the following allowed comparisons,
    "value": (String) one of the following allowed values
  }
}
```

- **許容される比較：** `is`, `is_not`
- **許容される値** `opted_in` `subscribed` 、 `unsubscribed`

### メール通知のサブスクリプションのフィルター

このフィルターによって、ユーザーのメール通知のサブスクリプションステータスに基づいてセグメント化することができます。

#### フィルター本文

```json
{
  "email_subscription_status":
  {
    "comparison": (String) one of the following allowed comparisons,
    "value": (String) one of the following allowed values
  }
}
```

- **許容される比較：** `is`, `is_not`
- **許容される値** `opted_in` `subscribed` 、 `unsubscribed`

### 最後に使用したアプリフィルター

このフィルターにより、ユーザーが最後にアプリを使用した時期に基づいてセグメンテーションすることができる。これらのフィルターには2つのフィールドがある：

#### フィルター本文
```json
{
  "last_used_app":
  {
    "comparison": (String) one of the allowed comparisons listed,
    "value": (String) the value to be compared using the provided comparison
  }
}
```

- **許容される比較：** `after`, `before`
- **許容される値:**datetime (ISO 8601 文字列)

### 考慮事項

接続オーディエンスは、デフォルト属性、カスタムイベント、セグメント、またはメッセージエンゲージメントイベントによってユーザーをフィルターすることはできません。これらのフィルターを使用するには、それらをオーディエンスセグメントに組み込み、[`/messages/send` エンド]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#request-parameters)ポイントの`segment_id` パラメーターでそのセグメントを指定することを推奨する。他のエンドポイントを使用する場合は、まずBrazeダッシュボードでAPIトリガーキャンペーンまたはキャンバスにセグメンテーションを追加する必要がある。
