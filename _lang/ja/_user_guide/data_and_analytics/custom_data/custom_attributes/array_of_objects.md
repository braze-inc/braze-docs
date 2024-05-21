---
nav_title: オブジェクト配列
article_title: オブジェクト配列
alias: "/array_of_objects/"
page_order: 0
page_type: reference
description: "このリファレンス記事では、オブジェクト配列をカスタム属性のデータ型として使用する方法について、制限事項や使用例も含めて説明します。" 
---

# オブジェクト配列

> 関連する属性をグループ化するには、オブジェクト配列を使用します。例えば、1 人のユーザーに属するペットオブジェクト、曲オブジェクト、アカウントオブジェクトをすべて含むグループがあるとします。これらのオブジェクト配列を使用して、Liquid でメッセージングをパーソナライズしたり、オブジェクト内のいずれかの要素が条件に一致する場合にオーディエンスセグメントを作成したりできます。

## 制限事項

- オブジェクト配列は、API 経由で送信されるカスタム属性を対象としています。CSV アップロードはサポートされていません。この理由は、CSV ファイル内のコンマが列区切り文字として解釈され、値に含まれるコンマにより解析エラーが発生するためです。 
- オブジェクト配列には、項目数の制限はありませんが、最大サイズが 50 KB という制限があります。
- すべての Braze パートナーがオブジェクト配列をサポートしているわけではありません。連携がこの機能をサポートしているかどうかを確認するには、[パートナーのドキュメント]({{site.baseurl}}/partners/home)を参照してください。

配列内の項目の更新または削除を行うには、キーと値を使用して項目を特定する必要があります。したがって、配列内の各項目に一意の識別子を含めることを検討してください。一意性の範囲は配列のみに限定されるため、配列から特定のオブジェクトの更新および削除を行う場合に役立ちます。これは Braze での強制事項ではありません。

## API の例

{% tabs local %}
{% tab Create %}

以下は、`pets` 配列を含む `/users/track` の例です。ペットのプロパティを取得するには、オブジェクトの配列として `pets` をリストする API リクエストを送信します。各オブジェクトには一意の `id` 属性が割り当てられていることに注意してください。この属性は、後で更新するときに参照できます。

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": [
        {
          "id": 1,
          "type": "dog",
          "breed": "beagle",
          "name": "Gus"
        },
        {
          "id": 2,
          "type": "cat",
          "breed": "calico",
          "name": "Gerald"
        }
      ]
    }
  ]
}
```
{% endtab %}
{% tab Add %}

`$add` 演算子を使用して、別の項目を配列に追加します。 次の例は、ユーザーの `pets` 配列にさらに 3 つのペットオブジェクトを追加することを示しています。

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": {
        "$add": [
          {
            "id": 3,
            "type": "dog",
            "breed": "corgi",
            "name": "Doug"
          },
          {
            "id": 4,
            "type": "fish",
            "breed": "salmon",
            "name": "Larry"
          },
           {
            "id": 5,
            "type": "bird",
            "breed": "parakeet",
            "name": "Mary"
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% tab Update %}

`_merge_objects` パラメーターと `$update` 演算子を使用して、配列内の特定オブジェクトの値を更新します。単純な[階層化カスタム属性]({{site.baseurl}}/nested_custom_attribute_support/#api-request-body)オブジェクトの更新と同様に、これは深いレベルでマージを実行します。

次の例は、`id` が `4` のオブジェクトについて、`breed` プロパティを `goldfish` に更新する方法を示します。このリクエスト例では、`id` が `5` に等しいオブジェクトが新しい `name` の `Annette` に更新されます。`_merge_objects` パラメーターが `true` に設定されているため、これら 2 つのオブジェクトの他のフィールドはすべて同じままです。

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "pets": {
        "$update": [
          {
            "$identifier_key": "id",
            "$identifier_value": 4,
            "$new_object": {
              "breed": "goldfish"
            }
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 5,
            "$new_object": {
              "name": "Annette"
            }
          }
        ]
      }
    }
  ]
}
```

{% alert warning %}
`_merge_objects` を true に設定する必要があります。設定しない場合、オブジェクトが上書きされます。`_merge_objects` のデフォルト値は false です。
{% endalert %}

{% endtab %}
{% tab Remove %}

配列からオブジェクトを削除するには、`$remove` 演算子と、一致するキー (`$identifier_key`) と値 (`$identifier_value`) を組み合わせて使用します。

次の例では、`pets` 配列内で、`id` の値が `1`、`id` の値が `2`、また `type` の値が `dog` のオブジェクトをすべて削除する方法を示します。`type` の値が `dog` であるオブジェクトが複数ある場合、一致するすべてのオブジェクトが削除されます。

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": {
        "$remove": [
          // Remove by ID
          {
            "$identifier_key": "id",
            "$identifier_value": 1
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 2
          },
          // Remove any dog
          {
            "$identifier_key": "type",
            "$identifier_value": "dog"
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% endtabs %}

## SDK の例

{% tabs local %}
{% tab Android SDK %}

**作成**
\`\`\`kotlin
val json = JSONArray()
    .put(JSONObject()
        .put("id", 1)
        .put("type", "dog")
        .put("breed", "beagle")
        .put("name", "Gus"))
    .put(JSONObject()
        .put("id", 2)
        .put("type", "cat")
        .put("breed", "calico")
        .put("name", "Gerald")
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json)
}
\`\`\`

**追加**
\`\`\`kotlin
val json = JSONObject()
    .put("\\$add", JSONArray()
        .put(JSONObject()
            .put("id", 3)
            .put("type", "dog")
            .put("breed", "corgi")
            .put("name", "Doug"))
        .put(JSONObject()
            .put("id", 4)
            .put("type", "fish")
            .put("breed", "salmon")
            .put("name", "Larry"))
        .put(JSONObject()
            .put("id", 5)
            .put("type", "bird")
            .put("breed", "parakeet")
            .put("name", "Mary")
        )
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json, true)
}
\`\`\`

**更新**
\`\`\`kotlin
val json = JSONObject()
    .put("\\$update", JSONArray()
        .put(JSONObject()
            .put("\\$identifier\_key", "id")
            .put("\\$identifier\_value", 4)
            .put("\\$new\_object", JSONObject()
                .put("breed", "goldfish")
            )
        )
        .put(JSONObject()
            .put("\\$identifier\_key", "id")
            .put("\\$identifier\_value", 5)
            .put("\\$new\_object", JSONObject()
                .put("name", "Annette")
            )
        )
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json, true)
}
\`\`\`

**削除**
\`\`\`kotlin
val json = JSONObject()
    .put("\\$remove", JSONArray()
        .put(JSONObject()
            .put("\\$identifier\_key", "id")
            .put("\\$identifier\_value", 1)
        )
        .put(JSONObject()
            .put("\\$identifier\_key", "id")
            .put("\\$identifier\_value", 2)
        )
        .put(JSONObject()
            .put("\\$identifier\_key", "type")
            .put("\\$identifier\_value", "dog")
        )
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json, true)
}
\`\`\`

{% endtab %}
{% tab Swift SDK %}

**作成**
\`\`\`swift
let json: [[String:Any?]] = [
  [
      "id":1,
    "type": "dog",
    "breed": "beagle",
    "name":"Gus"
  ],
[
    "id":2,
    "type": "cat",
    "breed": "calico",
    "name":"Gerald"
  ]
]

braze.user.setCustomAttribute(key: "pets", array: json)
\`\`\`

**追加**
\`\`\`swift
let json: [String:Any?] = [
  "$add": [
    [
          "id":3,
          "type": "dog",
        "breed": "corgi",
      "name":"Doug"
    ],
[
      "id":4,
      "type": "fish",
      "breed": "salmon",
      "name":"Larry"
    ],
[
      "id":5,
      "type": "bird",
      "breed": "parakeet",
      "name":"Mary"
    ]
]
]

braze.user.setCustomAttribute(key: "ペット", dictionary: json, merge: true)
\`\`\`

**更新**
\`\`\`swift
let json: [String:Any?] = [
  "$update": [
    [
      "$identifier\_key": "id",
      "$identifier\_value":4,
      "$new\_object": [
            "breed": "goldfish"
          ]
      ],
      [
      "$identifier\_key": "id",
    "$identifier\_value":5,
  "$new\_object": [
        "name":"Annette"
      ]
]
]
]

braze.user.setCustomAttribute(key: "pets", dictionary: json, merge: true)
\`\`\`

**削除**
\`\`\`swift
let json: [String:Any?] = [
  "$remove": [
    [
          "$identifier\_key": "id",
          "$identifier\_value":1,
      ],
[
      "$identifier\_key": "id",
      "$identifier\_value":2,
    ],
[
      "$identifier\_key": "type",
      "$identifier\_value": "dog",
    ]
]
]

braze.user.setCustomAttribute(key: "pets", dictionary: json, merge: true)
\`\`\`

{% alert important %}
階層化カスタム属性は AppboyKit ではサポートされていません。
{% endalert %}

{% endtab %}
{% tab Web SDK %}

**作成**
```javascript
import * as braze from "@braze/web-sdk";
const json = [{
  "id": 1,
  "type": "dog",
  "breed": "beagle",
  "name": "Gus"
}, {
  "id": 2,
  "type": "cat",
  "breed": "calico",
  "name": "Gerald"
}];
braze.getUser().setCustomUserAttribute("pets", json);
```

**追加**
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "$add": [{
    "id":  3,
    "type":  "dog",
    "breed":  "corgi",
    "name":  "Doug",
  }, {
    "id":  4,
    "type":  "fish",
    "breed":  "salmon",
    "name":  "Larry",
  }, {
    "id":  5,
    "type":  "bird",
    "breed":  "parakeet",
    "name":  "Mary",
  }]
};
braze.getUser().setCustomUserAttribute("pets", json, true);
```

**更新**
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "$update": [
    {
      "$identifier_key": "id",
      "$identifier_value": 4,
      "$new_object": {
        "breed": "goldfish"
      }
    },
    {
      "$identifier_key": "id",
      "$identifier_value": 5,
      "$new_object": {
        "name": "Annette"
      }
    }
  ]
};
braze.getUser().setCustomUserAttribute("pets", json, true);
```

**削除**
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "$remove": [
    {
      "$identifier_key": "id",
      "$identifier_value": 1,
    },
    {
      "$identifier_key": "id",
      "$identifier_value": 2,
    },
    {
      "$identifier_key": "type",
      "$identifier_value": "dog",
    }
  ]
};
braze.getUser().setCustomUserAttribute("pets", json, true);
```

{% endtab %}
{% endtabs %}

## Liquid のテンプレート作成

この `pets` 配列を使用して、メッセージをパーソナライズできます。次の Liquid のテンプレート作成例では、前述した API リクエストから保存されたカスタム属性オブジェクトのプロパティを参照し、メッセージングでそれらを使用する方法を示します。

{% raw %}
\`\`\`liquid
{% assign pets = {{custom\_attribute.${pets}}} %} 
 
{% for pet in pets %}
私は {{pet.name}} という名前の {{pet.type}} を飼っています。品種は {{pet.breed}} です。
{% endfor %}
\`\`\`
{% endraw %}

このシナリオでは、Liquid を使用して `pets` 配列全体をループし、各ペット用の分を出力できます。カスタム属性 `pets` に[変数を割り当て]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#assigning-variables)、ドット表記を使用してオブジェクトのプロパティにアクセスします。オブジェクト名を指定し、その後にピリオド `.` を付け、プロパティ名を指定します。

## セグメンテーション

オブジェクト配列に基づいてユーザーをセグメント化する場合、配列内のいずれかのオブジェクトが条件に一致すると、ユーザーはそのセグメントに入れられます。 

新規のセグメントを作成し、フィルターとして [**階層化カスタム属性**] を選択します。次に、オブジェクト配列の名前を検索して選択します。

![オブジェクト配列を基準にしたフィルターの適用][1]

ドット表記を使用して、使用するオブジェクト配列内のフィールドを指定します。テキストフィールドは空の大かっこのセット (`[]`) で始まり、これはオブジェクト配列の内部を見ていることを Braze に伝えます。その後にピリオド (`.`) と、使用するフィールドの名前を入力します。

例えば、`type` フィールドを基準にしてオブジェクト配列 `pets` にフィルターを適用する場合は、`[].type` を選択して、フィルターを適用する `snake` などのペットのタイプを選択します。

![「ペットのタイプがヘビに等しい」のフィルターを適用][3]

または、`type` が `dog` であるペットのフィルターを適用することもできます。ここで、あるユーザーは少なくとも 1 頭の犬を飼っているため、ユーザーは「タイプが犬のペットを少なくとも 1 頭飼っているユーザー」のセグメントに該当します。

![ペットのタイプが犬に等しいフィルターの適用][2]

### 階層化のレベル

最大 1 レベルの配列の階層 (別の配列内の配列) を含むセグメントを作成できます。例えば、次のコードに示す属性がある場合、`Gus` を含む `pets[].name` のセグメントを作成できます。ただし、`Gugu` を含む `pets[].nicknames[]` のセグメントは作成できません。

{% raw %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": [
        {
          "id": 1,
          "type": "dog",
          "breed": "beagle",
          "name": "Gus",
          "nicknames": [
            "Gugu",
            "Gusto"
          ]
        },
        {
          "id": 2,
          "type": "cat",
          "breed": "calico",
          "name": "Gerald",
          "nicknames": [
            "GeGe",
            "Gerry"
          ]
        }
      ]
    }
  ]
}
```
{% endraw %}

## データポイント

データポイントの消費方法は、プロパティの作成、更新、または削除のいずれを実行するかに応じて異なります。

{% tabs local %}
{% tab Create %}

新規の配列を作成すると、オブジェクト内の属性ごとにデータポイントが 1 消費されます。次の例ではデータポイント 8 が必要です。各ペットオブジェクトには属性が 4 つあり、オブジェクトが 2 つあります。

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": [
        {
          "id": 1,
          "type": "dog",
          "breed": "beagle",
          "name": "Gus"
        },
        {
          "id": 2,
          "type": "cat",
          "breed": "calico",
          "name": "Gerald"
        }
      ]
    }
  ]
}
```
{% endtab %}
{% tab Update %}

既存の配列を更新すると、追加されたプロパティごとにデータポイントが 1 消費されます。次の例では、2 つのオブジェクトのそれぞれでプロパティを 1 つのみ更新するため、データポイント 2 を消費します。

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "pets": {
        "$update": [
          {
            "$identifier_key": "id",
            "$identifier_value": 4,
            "$new_object": {
              "breed": "goldfish"
            }
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 5,
            "$new_object": {
              "name": "Annette"
            }
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% tab Remove %}

配列からオブジェクトを削除するときには、送信する削除条件ごとにデータ ポイントが 1 消費されます。次の例では、このステートメントで複数の犬を削除できるにもかかわらず、データポイントが 3 消費されます。

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": {
        "$remove": [
          // Remove by ID
          {
            "$identifier_key": "id",
            "$identifier_value": 1
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 2
          },
          // Remove any dog
          {
            "$identifier_key": "type",
            "$identifier_value": "dog"
          }
        ]
      }
    }
  ]
}
```

{% endtab %}
{% endtabs %}

[1]: {% image_buster /assets/img_archive/array_of_objects_segmenting_1.gif %}
[2]: {% image_buster /assets/img_archive/array_of_objects_segmenting_2.png %}
[3]: {% image_buster /assets/img_archive/array_of_objects_segmenting_3.png %}
