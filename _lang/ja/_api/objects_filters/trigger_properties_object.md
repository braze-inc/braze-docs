---
nav_title: "トリガー・プロパティ・オブジェクト"
article_title: APIトリガープロパティオブジェクト
page_order: 11
page_type: reference
description: "この参照記事では、トリガ・プロパティ・オブジェクトの様々な構成要素について説明します。"
tool: Campaigns

---

# トリガー・プロパティ・オブジェクト

> APIトリガー配信でキャンペーンを送信するためにエンドポイントの1つを使用する場合、メッセージをカスタマイズするためにキーと値のマップを提供することができます。

`trigger_properties` のオブジェクトを含む API 要求を行うと、そのオブジェクトの値を、`api_trigger_properties` ネームスペースの下にあるメッセージ・テンプレートで参照できます。例えば、以下のようなリクエストは、{% raw %}`{{api_trigger_properties.${product_name}}}`{% endraw %} を追加することで、`"shoes"` という単語をメッセージに追加することができる。

{% alert note %}
`trigger_properties` オブジェクトと{% raw %}`api_trigger_properties.${product_name}`{% endraw %} 構文はキャンペーンでのみサポートされています。CanvasのAPIトリガーリクエストからのキーと値でメッセージをカスタマイズするには、[Canvasエントリー・プロパティ・オブジェクトを]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/)使用します。`trigger_properties` オブジェクトの最大サイズ制限は50KB。
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


