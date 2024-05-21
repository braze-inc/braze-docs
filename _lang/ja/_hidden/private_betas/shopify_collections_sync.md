---
nav_title: Shopifyコレクション同期
article_title: Shopifyコレクション同期
permalink: "/shopify_collections_sync/"
description: "この参考記事では、Shopifyのコレクション同期を設定する方法を説明します。これにより、商品をコレクションにグループ化することができ、顧客はカテゴリー別に商品を見つけることができます。"
hidden: true
---

# Shopifyコレクション同期ベータ版

> Shopifyのコレクション同期を使用すると、製品をコレクションにグループ化することができ、顧客はカテゴリ別に製品を見つけることができます。よりシームレスなショッパーエクスペリエンスのために、ショップのコレクション内のアイテムをBrazeメッセージに組み込むことができます。

{% alert important %}
Shopifyコレクション同期は現在ベータ版です。ベータ版への参加をご希望の方は、Brazeのアカウントマネージャーにご連絡ください。
{% endalert %}

## Shopifyコレクション同期の設定

ShopifyストアからBrazeに商品を同期するには、[Shopifyを統合する]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify#setting-up-shopify-in-braze) **商品の同期**ステップで、**Shopifyコレクションを同期**するチェックボックスを選択します。<br><br>Shopifyコレクションを同期」チェックボックスを選択した状態で、Shopify商品同期のステップ4][1]。

商品が同期されると、Shopifyカタログを見ることで、どの商品がコレクションに関連付けられているかを確認することができます。<br><br>![「ベストセラー」と「フロントページ」のコレクションにある商品を示すカタログ・テーブルの行][2]。

Shopifyカタログから、**Selections**タブでShopifyコレクションを見ることができます。<br><br>ベストセラー "と "フロントページ "という2つのコレクションのリストを表示する[セレクション]タブ][3]。

### ベータ版機能

- Brazeは最大30コレクションをサポート
- 現時点では、コレクションのソート順は維持またはサポートされていません。今のところ、以下のようなソート順になっている：
    - コレクションに追加された最新のアイテム。
    - 連続同期中にアイテムが更新される順序。
    - Shopifyコレクションの選択タブで選択した順序。

## Shopifyコレクションの使用

Shopifyのコレクションを使用して、[Brazeのセレクションを]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/)使用する方法と同様に、キャンペーンの各ユーザーにメッセージをパーソナライズします。

{% alert warning %}
ベータ版では以下のような挙動があるので注意：<br><br>Shopifyコレクションの説明やフィルター設定を更新すると、Shopifyコレクションの同期が壊れてしまいます。その結果、Shopifyコレクションは期待通りに動作しません。
{% endalert %}

### ステップ 3:Shopifyコレクションのソート順を設定する

1. Shopifyコレクションの結果を返す順序を指定するには、Shopifyコレクションの選択タブで**ソート順序を**選択します。これにはソート順をランダムにするオプションも含まれている。
2. **リミット番号**の結果の最大数（最大50件）を入力します。
3. **選択を更新を**選択する。

フィルター設定、ソートタイプ、結果制限を選択できる選択項目の編集ページ][4]。

### ステップ 3:キャンペーンでコレクションを使用する

1. キャンペーンを作成し、メッセージコンポーザーで**「+パーソナライズ**」を選択します。
2. 以下を選択する：<br>**\- パーソナライズタイプとしての** **カタログアイテム**<br>\- カタログ名<br>\- アイテム選択方法<br>\- セレクション名（Shopifyコレクション名） <br>\- メッセージに表示する情報

{: start="3"}
3\.Liquidのスニペットをコピーし、メッセージ内の表示したい場所に貼り付けます。

![カタログ、アイテムの選択方法、表示する情報を選択するフィールドがある「パーソナライズの追加」セクション][5]。{: style="max-width:30%;"}

#### 選考結果の流動性

カスタム属性やカスタムイベントなど、カタログ内の結果を使用すると、選択したユーザーごとに異なる結果が返されることがあります。

[1]: {% image_buster /assets/img/Shopify/sync_products.png %}
[2]: {% image_buster /assets/img/Shopify/view_catalog.png %}
[3]: {% image_buster /assets/img/Shopify/selections_tab.png %}
[4]: {% image_buster /assets/img/Shopify/edit_selection.png %}
[5]: {% image_buster /assets/img/Shopify/add_personalization.png %}
