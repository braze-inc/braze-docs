---
nav_title: "Canvas エントリ プロパティ オブジェクト"
article_title: API Canvas エントリプロパティオブジェクト
page_order: 2
page_type: reference
tool:
  - Canvas
description: "この記事では、Braze Canvas エントリ プロパティ オブジェクトについて説明します。"

---

# Canvas エントリのプロパティ オブジェクト

> エンドポイントの 1 つを使用して API 経由で Canvas をトリガーまたはスケジュールする場合、Canvas の最初のステップで送信されるメッセージをカスタマイズするためのキーと値のマップを名前空間に `canvas_entry_properties` 指定できます。

{% alert note %}
Canvas エントリのプロパティ オブジェクトの最大サイズ制限は 50 KB です。
{% endalert %}

## オブジェクト本体

このオブジェクト本体には、要求の例が含まれています。

```json
"canvas_entry_properties": {"product_name" : "shoes", "product_price" : 79.99}
```

{% raw %}
たとえば、要求 `"canvas_entry_properties": {"product_name" : "shoes", "product_price" : 79.99}` に追加することで ```{{canvas_entry_properties.${product_name}}}``` 、メッセージに "shoes" という単語を追加できます。
{% endraw %}
