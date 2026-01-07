---
nav_title: 固有の割引コード 
article_title: 固有の割引コードを送信する
alias: /shopify_discount_codes/
page_order: 7
description: "この参考記事では、Shopify の一括割引コードボットで Brazeプロモーションコードを使用し、キャンペーンやCanvasesを通じて独自の割引コードを送信する、コミュニティから投稿されたユースケースを取り上げる。"
---

# Shopifyを通じて独自の割引コードを送信する

> このコミュニティから投稿されたユースケースは、Braze [プロモーションコード]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/)を Shopify 一括割引コードボットとともに使用し、キャンペーンやキャンバス用に固有の割引コードを生成する方法を示します。固有の割引コードは、一般的なプロモーションコードの悪用を避けるのに役立ちます。

{% alert important %}
これはコミュニティから提出された統合であり、Braze は直接サポートしていません。一括割引コードボットは Shopify によって直接サポートされています。Braze がサポートしているのは Braze プロモーションコードのみです。
{% endalert %}

## 要件

| 要件 | 説明 |
| --- | --- |
| Shopify ストアを設定する | [Braze で Shopifyストアを設定]({{site.baseurl}}/shopify_overview/)済みであることを確認します。 |
| 一括割引コードボットアプリをインストールする | Shopify アプリストアで[一括割引コードボット](https://apps.shopify.com/bulk-discount-generator)アプリをダウンロードします。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 固有の割引コードを生成する

### ステップ 1: 割引コードを設定する

一括割引コードボットを使用して、生成するコードの数、コードの長さ、割引額などに基づいて割引コードを設定する。

![割引セットの設定オプション][1]。

### ステップ 2:コードをエクスポートする

一括割引コードボットの検索バーで割引設定を検索し、[**コードのエクスポート**] > [**コードのダウンロード**] を選択し、CSV ファイルをダウンロードフォルダにダウンロードします。

![割引セットを表示するドロップダウンと、選択するためのボタンが並んだ検索バー][2]。{: style="max-width:70%;"}

CSV ファイルの 1 行目を削除し、列ヘッダー「Promo」を削除します。これで「Promo」が Braze の割引コードになるのを防ぐことができます。

![CSVファイルの行ヘッダー "Promo "の削除を示すフローチャート][3]。{: style="max-width:60%;"}

### ステップ 3:Brazeに割引コードを追加する

Brazeの「**データ設定**」>「**プロモーションコード**」>「**プロモーションコード一覧の作成**」で、[割引コード一覧を設定する]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/#creating-a-promotion-code-list)。一括割引コードボットが設定した有効期限と一致していることを確認します。

次に CSV ファイルをアップロードし、[**リストを保存**] を選択します。

### ステップ 4: Brazeキャンペーンまたはキャンバスステップに割引コードを追加する。

固有の割引コードを1回のキャンペーンで使用したい場合、または異なるキャンペーンやキャンバスステップで複数のユニークなコードをユーザーが受け取っても構わない場合は、保存したプロモーションコード一覧からコードのリキッドスニペットをコピーする。

![Liquidのコードスニペットとそれをコピーするボタン][4]。{: style="max-width:60%;"}

キャンペーンまたはキャンバスステップに Liquid スニペットを貼り付けます。 

![キャンバスのステップに追加されるLiquidスニペットを示すGIF][5]。

キャンペーンやキャンバスで割引コードが何度参照されても、ユーザーに一意の割引コードを受け取らせたい場合は、最初のメッセージステップの前に直接[ユーザー更新]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/)ステップを作成し、割引コードを「プロモコード」のようなカスタム属性に割り当てる。

{% alert tip %}
[**データ設定**] ＞ [**カスタム属性**] で[カスタム属性を作成]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/)することもできます。
{% endalert %}

ユーザー更新ステップで、各フィールドに対して以下を行います。
- **属性名**[**プロモーションコード**] を選択します。
- **アクション:**[**更新**] を選択します。
- **キーの値:**Liquid のコードスニペットを貼り付けます。

![リキッドスニペットで "プロモコード "属性を更新するユーザー更新ステップ][6]。

これで、カスタム属性 {% raw %}`{{custom_attribute.${Promo Code}}}`{% endraw %} を任意のメッセージに追加でき、割引コードがテンプレート化されます。

## 割引コードの動作

{% details Multichannel campaign or Canvas step %}

割引コードスニペットがマルチチャネルキャンペーンやキャンバスステップで使用されると、ユーザーは常に固有のコードを受け取ります。ユーザーが複数のチャネルを通じてコードを受け取る資格がある場合、各チャネルを通じて同じコードを受け取ることになります。言い換えれば、対象となるユーザーは、そのキャンペーンまたはキャンバスステップによって送信されたすべてのメッセージで 1 つのコードのみを受け取ります。

{% enddetails %}

{% details Different Canvas steps or separate campaigns %}

割引コードが同じキャンバス内の複数のステップまたは別々のキャンペーンで参照される場合、対象となるユーザーには複数の固有のプロモーションコード (各キャンバスのステップまたはキャンペーンに 1 つのコード) が発行されます。

{% enddetails %}

[1]: {% image_buster /assets/img/Shopify/configure_discount_codes.png %}
[2]: {% image_buster /assets/img/Shopify/export_discount_codes.png %}
[3]: {% image_buster /assets/img/Shopify/edited_codes_csv.png %}
[4]: {% image_buster /assets/img/Shopify/liquid_code_snippet.png %}
[5]: {% image_buster /assets/img/Shopify/liquid_promo_code.gif %}
[6]: {% image_buster /assets/img/Shopify/user_update_step.png %}