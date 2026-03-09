---
nav_title: "キャンバスコンテキストオブジェクト"
article_title: APIキャンバスコンテキストオブジェクト
page_order: 2
page_type: reference
alias: /api/objects_filters/canvas_entry_properties_object/
tool:
  - Canvas
description: "この記事は、Braze キャンバスのコンテキストオブジェクトについて説明する。"

---

# キャンバスコンテキストオブジェクト

> API を通じてキャンバスをトリガーまたはスケジューリングするためのエンドポイントの1つを使用する場合、キャンバスの最初のステップによって送信されるメッセージをカスタマイズするためのキーと値のマップを、`context` 名前空間に提供することができます。

{% alert note %}
コンテキストオブジェクトの最大サイズ制限は50キロバイトである。
{% endalert %}

## オブジェクト本体

このオブジェクトボディはリクエスト例を含む。

```json
"context": {"product_name" : "shoes", "product_price" : 79.99}
```

{% raw %}
例えば、APIリクエストに`"context": {"product_name" : "shoes", "product_price" : 79.99}`を含めることができる。その後、メッセージテンプレートに```{{context.${product_name}}}```を追加することで、メッセージ内で「靴」という単語を参照できる。
{% endraw %}
