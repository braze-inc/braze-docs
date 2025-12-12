---
nav_title: "キャンバスエントリのプロパティオブジェクト"
article_title: API キャンバスエントリのプロパティオブジェクト
page_order: 2
page_type: reference
tool:
  - Canvas
description: "この記事では、Braze Canvasのエントリー・プロパティ・オブジェクトについて説明する。"

---

# キャンバスエントリー・プロパティ・オブジェクト

> API を通じてキャンバスをトリガーまたはスケジューリングするためのエンドポイントの1つを使用する場合、キャンバスの最初のステップによって送信されるメッセージをカスタマイズするためのキーと値のマップを、`canvas_entry_properties` 名前空間に提供することができます。

{% alert note %}
キャンバスエントリのプロパティオブジェクトの最大サイズは 50 KB に制限されています。
{% endalert %}

## オブジェクト本体

このオブジェクトボディはリクエスト例を含む。

```json
"canvas_entry_properties": {"product_name" : "shoes", "product_price" : 79.99}
```

{% raw %}
例えば、`"canvas_entry_properties": {"product_name" : "shoes", "product_price" : 79.99}` を使ったリクエストの場合、```{{canvas_entry_properties.${product_name}}}``` をリクエストに追加して、「shoes」という単語をメッセージに追加できます。
{% endraw %}
