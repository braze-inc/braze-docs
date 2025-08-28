---
nav_title: スクロールバーのオーバーラップ
article_title: スクロールバーのオーバーラップ
page_order: 0

page_type: solution
description: "このヘルプ記事では、Brazeドキュメント内でコンテンツが重なるスクロールバーを解決する方法をMacユーザー向けに説明します。"
---

# スクロールバーのオーバーラップ

Mac を使用していて、スクロールバーがBraze Docs 内の内容とオーバーアプリしていることがわかりました。以下の例を参照してください。

![スクロールバーオーバーラップ]({% image_buster /assets/img/scroll-overlap.png %})の例

スクロールバーが次のコード ブロックと重なっているかどうかを確認します。

```
<your-bucket-prefix>/dataexport.<cluster-identifier>.S3.integration.<integration-id>/event_type=<event-type>/date=<date>/<schema-id>/<zone>/dataexport.<cluster-identifier>.S3.integration.<integration-id>+<partition>+<offset>.avro
```

スクロールバーがコード ブロックと重なる場合は、**スクロールバーを表示する:**設定を**Always**に変更することをお勧めします(**一般設定s**)。この場合、ドキュメントの機能 (コードブロックなど) が拡張され、スクロールバーが常時表示されるため、文字を読みにくくなります。

![MacOS の一般設定]({% image_buster /assets/img/general-on-mac.png %})

更新されたスクロールバーは、以下のように表示されます。

![重複のない固定スクロールバーの例]({% image_buster /assets/img/scroll-bar-on.png %})

_最終更新日: 2019年3月27日_

{% comment %}
問題を引き起こす可能性のある長いコードが1 行ある場合に挿入します。
_スクロールバーのせいでコードが見えませんか？[ここでの修正方法]({{site.baseurl}}/help/help_articles/docs/scroll_bar_overlap/)を参照してください。_
{% endcomment %}

