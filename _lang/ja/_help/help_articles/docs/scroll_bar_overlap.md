---
nav_title: スクロールバーの重なり
article_title: スクロールバーの重なり
page_order: 0

page_type: solution
description: "このヘルプ記事では、Brazeドキュメント内でコンテンツが重なるスクロールバーを解決する方法をMacユーザー向けに説明します。"
---

# スクロールバーの重なり

Macを使用していて、Braze Docs内でスクロールバーが次の例のようにコンテンツと重なっていることに気づいている？

![スクロールバーの重なりの例][1]

スクロールバーが次のコードブロックに重なっていないか確認する：

```
<your-bucket-prefix>/dataexport.<cluster-identifier>.S3.integration.<integration-id>/event_type=<event-type>/date=<date>/<schema-id>/<zone>/dataexport.<cluster-identifier>.S3.integration.<integration-id>+<partition>+<offset>.avro
```

スクロールバーがコードブロックに重なる場合は、**一般設定の**「**スクロールバーを表示**する」の設定を「**常に**」に変更することをお勧めする。これにより、Docsの機能（コードブロックなど）が拡張され、常にスクロールバーが表示されるようになり、読みづらくなるのを防ぐことができる。

![MacOSの一般設定][2]

更新されたスクロールバーはこんな感じになっているはずだ：

![オーバーラップのない固定スクロールバーの例][3]

_最終更新日：2019年3月27日_

{% comment %}
問題を引き起こす可能性のある1行の長いコードがある場合は、これを挿入する：
_スクロールバーのせいでコードが見えない？修正方法は[こちらを]({{site.baseurl}}/help/help_articles/docs/scroll_bar_overlap/)ご覧いただきたい。_
{% endcomment %}

[1]: {% image_buster /assets/img/scroll-overlap.png %}
[2]: {% image_buster /assets/img/general-on-mac.png %}
[3]: {% image_buster /assets/img/scroll-bar-on.png %}
