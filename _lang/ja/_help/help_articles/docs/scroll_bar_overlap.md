---
nav_title: スクロールバーオーバーラップ
article_title: スクロールバーオーバーラップ
page_order: 0

page_type: solution
description: "このヘルプ記事では、Brazeドキュメント内でコンテンツが重なるスクロールバーを解決する方法をMacユーザー向けに説明します。"
---

# スクロールバーのオーバーラップ

Macを使用していて、次の例のように、スクロールバーがBraze Docs内のコンテンツと重なっていることに気づきましたか？

![スクロールバーのオーバーラップの例] [1]

スクロールバーが次のコードブロックと重なっていないか確認してください。

```
<your-bucket-prefix>/dataexport.<cluster-identifier>.S3.integration.<integration-id>/event_type=<event-type>/date=<date>/<schema-id>/<zone>/dataexport.<cluster-identifier>.S3.integration.<integration-id>+<partition>+<offset>.avro
```

スクロールバーがコードブロックと重なっている場合は、**一般設定の**「**スクロールバーを表示:**」設定を「**常に**」に変更することをお勧めします。これにより、ドキュメントの機能 (コードブロックなど) が拡張され、常にスクロールバーが表示されるようになり、読みにくくなることがなくなります。

![macOS の一般設定] [2]

これで、更新されたスクロールバーは次のようになります。

![オーバーラップのない固定スクロールバーの例] [3]

_2019年3月27日に最終更新されました_

{% comment %}
問題を引き起こす可能性のある長いコードが 1 行ある場所にこれを挿入してください。
_スクロールバーが原因でコードが表示されませんか？この問題を解決する方法については、[こちらをご覧ください]({{site.baseurl}}/help/help_articles/docs/scroll_bar_overlap/)。_
{% endcomment %}

[1]: {% image_buster /assets/img/scroll-overlap.png %}
[2]: {% image_buster /assets/img/general-on-mac.png %}
[3]: {% image_buster /assets/img/scroll-bar-on.png %}
