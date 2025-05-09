---
nav_title: データフィードからプロモーションコードへの移行
article_title: データフィードからプロモーションコードへの移行
page_order: 0
description: "この参考文献は、データフィードからプロモーションコードsへの移行に関する指針を提供します。"
---

# データフィードから昇格コードへの移行

{% alert note %}
データフィードは廃止されます。データフィードをご使用のお客様は、プロモーションコードリストに移行することを推奨します。
{% endalert %}

> このページでは、データフィードからプロモーションコードへの移行について説明します。これは簡単なプロセスで、データフィードの情報を使ってプロモーションコードのリストを手動で作成し、それに応じてメッセージ参照を更新します。

## 特長と機能

プロモーションコードリストとデータフィードには、いくつかの違いがあります。

| 機能          | プロモーションコード | データフィード   |
|------------------|-----------------|--------------|
| 説明     | はい             | いいえ           |
| 有効期限 | はい             | いいえ           |
| 作成方法  | CSVを読み込むする | テキストを貼り付ける |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 移行方法

データフィードをプロモーションコードリストに置き換えるには、次の手順を実行します。 

1. [**データ設定**] に移動し、[**プロモーションコードリストの作成**] を選択します。
2. [プロモーションコードリストを設定]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes)します。
3. 以前にデータフィードを参照したメッセージに移動し、プロモーションコードリストを使用するように更新します。