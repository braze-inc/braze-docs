---
nav_title: "トリガー・プロパティ・オブジェクト"
article_title: APIトリガープロパティオブジェクト
page_order: 11
page_type: reference
description: "このリファレンス記事では、トリガープロパティオブジェクトのさまざまなコンポーネントについて説明します。"
tool: Campaigns

---

# トリガー・プロパティ・オブジェクト

> APIトリガー配信でキャンペーンを送信するためにエンドポイントの1つを使用する場合、メッセージをカスタマイズするためにキーと値のマップを提供することができる。

`trigger_properties` のオブジェクトを含む API リクエストを行った場合、そのオブジェクトの値は、`api_trigger_properties` 名前空間の下のメッセージテンプレートで参照できます。例えば、以下を使ったリクエストの場合、{% raw %}`{{api_trigger_properties.${product_name}}}`{% endraw %} を追加することで、メッセージに `"shoes"` という単語を追加できます。

トリガープロパティは、メッセージにテンプレート化することができますが、デフォルトではユーザープロファイルに自動的には保存されないことに注意してください。

{% alert note %}
`trigger_properties` オブジェクトと{% raw %}`api_trigger_properties.${product_name}`{% endraw %} 構文はキャンペーンでのみサポートされる。キャンバスの API トリガーリクエストからのキーと値でメッセージをカスタマイズするには、[キャンバスエントリープロパティオブジェクト]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/)を使用します。`trigger_properties` オブジェクトの最大サイズ制限は50KBである。
{% endalert %}

## オブジェクト本体

```json
{
  "trigger_properties" : {
    "product_name" : "shoes",
    "product_price" : 79.99,
    "details" : {
      "color" : "red",
      "size" : {
        "numerical" : 10,
        "country" : "US"
      }
    },
    "related_skus": ["123", "456", "789"]
  }
}
```


