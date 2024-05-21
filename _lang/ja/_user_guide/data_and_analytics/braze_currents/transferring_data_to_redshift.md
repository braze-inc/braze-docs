---
nav_title: Redshift へのデータ転送
article_title: Redshift へのデータ転送
page_order: 8
page_type: tutorial
description: "このハウツー記事では、ETL プロセス経由で Amazon S3 から Redshift にデータを転送する方法を順に説明します。"
tool: Currents

---

# Redshift へのデータ転送

> [Amazon Redshift](https://aws.amazon.com/redshift/) は、Amazon S3 と並んでAmazon Web Services 上で動作する、評判の良いデータウェアハウスです。Currents の Braze データは Redshift に直接転送しやすい構造になっています。

ETL プロセス経由で Amazon S3 から Redshift にデータを転送する方法の詳細については、Currents の例がある [GitHub リポジトリ](https://github.com/Appboy/currents-examples)を参照してください。

{% alert important %}
これは、最も有利な場所にデータを転送するという観点で、選択できる多くのオプションの単なる 1 つに過ぎないことに注意してください。
{% endalert %}

{% markdown_embed https://raw.githubusercontent.com/Appboy/currents-examples/master/redshift-s3-loader/README.md %}
