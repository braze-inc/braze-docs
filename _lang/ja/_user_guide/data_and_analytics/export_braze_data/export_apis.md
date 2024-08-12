---
nav_title: エクスポート API
article_title: エクスポート API
page_order: 8
page_type: reference
description: "このリファレンス記事では、ダッシュボードから CSV を直接エクスポートするのではなく、ダッシュボードデータの JSON ファイルをプログラムでエクスポートする理由について説明します。"
platform: API

---

# エクスポート API

> Braze のエクスポート API を使用すると、ダッシュボードデータの JSON ファイルをプログラムでエクスポートできます。アクセスできるデータのリスト、エクスポートの手順とサンプルコードについては、「[エクスポートエンドポイント][24]」を参照してください。

ダッシュボードから CSV を直接エクスポートするよりもこの方法が望ましい理由がいくつかあります。

 - 非常に大きいファイルを扱うことができます。ダッシュボードからエクスポートできる CSV は、最大 500,000 行です。ユーザー数が 500,000 人を超えるセグメントのデータをエクスポートする場合は、エクスポートできる量に制限のないエクスポート API を使用する必要があります。
 -  プログラムでデータを操作できます。

{% alert tip %}
CSV および API のエクスポートに関するヘルプについては、「[エクスポートのトラブルシューティング]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/)」の記事を参照してください。
{% endalert %}

[24]: {{site.baseurl}}/api/endpoints/export/
