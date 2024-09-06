---
nav_title: Shopifyコレクション同期
article_title: Shopifyコレクション同期
permalink: "/shopify_collections_sync/"
description: "この参考記事では、Shopifyのコレクション同期を設定する方法について説明する。コレクションに商品をグループ化することで、顧客がカテゴリー別に商品を見つけられるようになる。"
hidden: true
---

# Shopifyコレクション同期ベータ版

> Shopifyのコレクション同期では、商品をコレクションにグループ化することができ、顧客はカテゴリー別に商品を見つけることができる。よりシームレスな買い物体験のために、ショップのコレクション内のアイテムをBrazeのメッセージに組み込むことができる。

{% alert important %}
Shopifyコレクション同期は現在ベータ版である。ベータ版への参加を希望する場合は、Brazeのアカウントマネージャーに連絡すること。
{% endalert %}

## Shopifyのコレクション同期を設定する

ShopifyストアからBrazeに商品を同期するには、[Shopifyを統合する]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify#setting-up-shopify-in-braze) **商品の同期**ステップで、**Shopifyコレクションを同期**するチェックボックスを選択する。<br><br>![Shopify商品同期のステップ4で、「Shopifyコレクションを同期」チェックボックスを選択する。][1]

商品が同期されると、Shopifyのカタログを見ることで、どの商品がコレクションに関連付けられているかを確認することができる。<br><br>![ベストセラー」と「フロントページ」のコレクションにある商品を示すカタログ・テーブルの行。][2]

Shopifyカタログから、**Selections**タブでShopifyコレクションを見ることができる。<br><br>![セレクション」タブには、「ベストセラー」と「フロントページ」という2つのコレクションが表示されている。][3]

### ベータ版機能

- ブレイズは最大30コレクションをサポートする
- 現時点では、コレクションのソート順は維持・サポートされていない。今のところ、ソート順は以下に基づいている：
    - あなたのコレクションに最近追加されたアイテム。
    - 連続シンク中にアイテムが更新される順序。
    - Shopifyコレクションの選択タブで選択した順序。

## Shopifyのコレクションを使う

Shopifyのコレクションを使って、[Brazeのセレクションを]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/)使うのと同じように、キャンペーンの各ユーザーにメッセージをパーソナライズしよう。

{% alert warning %}
ベータ版では、以下のような挙動に注意すること：<br><br>Shopifyコレクションの説明やフィルター設定を更新すると、Shopifyコレクションの同期が壊れてしまう。その結果、Shopifyコレクションは期待通りに機能しなくなる。
{% endalert %}

### ステップ1:Shopifyコレクションのソート順を設定する

1. Shopifyコレクションの選択タブで**Sort Orderを**選択して、Shopifyコレクションの結果を返す順序を指定する。これにはソート順をランダムにするオプションも含まれている。
2. **リミット番号の**結果の最大数（最大50）を入力する。
3. **Update Selectionを**選択する。

![フィルター設定、ソートタイプ、結果制限を選択できる。][4]

### ステップ2:キャンペーンでコレクションを使用する

1. キャンペーンを作成し、メッセージコンポーザーで**「+パーソナライズ**」を選択する。
2. 以下を選択する：<br>**\- カタログ項目を** **パーソナライズの種類に**する<br>\- カタログ名<br>\- アイテム選択方法<br>\- セレクション名（Shopifyコレクション名） <br>\- メッセージに表示する情報

{: start="3"}
3\.Liquidのスニペットをコピーして、メッセージに表示したい場所に貼り付ける。

![パーソナライゼーションの追加」セクションには、カタログ、アイテムの選択方法、表示する情報を選択するフィールドがある。][5]{: style="max-width:30%;"}

#### 選考結果が流動的

カスタム属性やカスタム・イベントなど、カタログ内の結果を使用すると、選択したユーザーごとに異なる結果が返される可能性がある。

[1]: {% image_buster /assets/img/Shopify/sync_products.png %}
[2]: {% image_buster /assets/img/Shopify/view_catalog.png %}
[3]: {% image_buster /assets/img/Shopify/selections_tab.png %}
[4]: {% image_buster /assets/img/Shopify/edit_selection.png %}
[5]: {% image_buster /assets/img/Shopify/add_personalization.png %}
