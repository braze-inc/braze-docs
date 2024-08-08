---
nav_title: "コネクテッド・オーディエンス フィルター＆オブジェクト"
article_title: API接続オーディエンス・オブジェクト
page_order: 3
page_type: reference
description: "この記事では、コネクテッドオーディエンスオブジェクトのさまざまなコンポーネントと、それを作成するフィルターについて説明します。"

---

# 接続された観客オブジェクト

> 接続されたオーディエンスオブジェクトは、メッセージを送信するオーディエンスを特定するセレクタです。 

このオブジェクトは、`AND` または`OR` 演算子を使用した論理式で、1つの接続された視聴者フィルタ、または複数の接続された視聴者フィルタで構成されます。

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

## 接続された視聴者フィルター

複数のカスタム属性フィルタを組み合わせると、連結オーディエンスフィルタが作成されます。`AND` および`OR` 演算子と組み合わせると、連結オーディエンスフィルタが作成されます。

### カスタム属性フィルター

このフィルターを使用すると、ユーザーのカスタム属性に基づいてセグメント化することができます。これらのフィルターには最大3つのフィールドが含まれる：

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

#### データ型による比較

カスタム属性のデータ型は、与えられたフィルターで有効な比較を決定します。

| カスタム属性タイプ｜許可される比較
| ---------------------| --------------- |
| 文字列｜`equals`,`not_equal`,`matches_regex`,`does_not_match_regex`,`exists`,`does_not_exist` |
| 配列｜`includes_value`,`does_not_include_value`,`exists`,`does_not_exist` |
| 数値｜`equals`,`not_equal`,`greater_than`,`greater_than_or_equal_to`,`less_than`,`less_than_or_equal_to`,`exists`,`does_not_exist` |
| ブーリアン｜`equals`,`does_not_equal`,`exists`,`does_not_exist` |
| 時間｜`less_than_x_days_ago`,`greater_than_x_days_ago`,`less_than_x_days_in_the_future`,`greater_than_x_days_in_the_future`,`after`,`before`,`exists`,`does_not_exist` |
{: .reset-td-br-1 .reset-td-br-2}

#### 属性比較の注意点

| 比較
| --- | --- |
|`value` |`exists` または`does_not_exist` の比較を使用する場合、`value` は必須ではありません。`before` および`after` の比較を使用する場合、`value` は ISO 8601 の日付文字列でなければなりません。|
|`matches_regex` ｜`matches_regex` ｜比較を使用する場合、渡される値は文字列でなければならない。Brazeでの正規表現の使用については、[正規表現と]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/#regex-with-braze) [カスタム属性データタイプを]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#custom-attribute-data-types)参照してください。|
{: .reset-td-br-1 .reset-td-br-2}

#### カスタム属性の例

\`\`\`json
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
  \`\`\`
### プッシュ購読フィルター

このフィルターを使用すると、ユーザーのプッシュ購読状況に基づいてセグメント化することができます。

#### フィルター本体

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
- **許可された値** `opted_in` `subscribed` 、 `unsubscribed`

### メール購読フィルター

このフィルターは、ユーザーのメール購読状況に基づいてセグメントすることができます。

#### フィルター本体

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
- **許可された値** `opted_in` `subscribed` 、 `unsubscribed`

### 最後に使用したアプリフィルター

このフィルターにより、ユーザーが最後にアプリを使用した時間に基づいてセグメントすることができます。これらのフィルターには2つのフィールドがある：

#### フィルター本体
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

