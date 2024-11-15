---
nav_title: Shopifyコレクション同期
article_title: Shopifyコレクション同期
permalink: "/shopify_collections_sync/"
description: "この参考記事では、Shopifyのコレクション同期を設定する方法について説明する。コレクションに商品をグループ化することで、顧客がカテゴリー別に商品を見つけられるようになる。"
hidden: true
---

# Shopifyコレクション同期ベータ版

> Shopify のコレクション同期では、製品をコレクションにグループ化することができ、顧客はカテゴリー別に商品を見つけることができます。よりシームレスなショッピング体験のために、ショップのコレクション内のアイテムを Braze メッセージングに組み込むことができます。

{% alert important %}
Shopify コレクション同期は現在ベータ版です。ベータ版に参加したい場合は、Braze アカウントマネージャーにお問い合わせください。
{% endalert %}

## Shopifyのコレクション同期を設定する

Shopify ストアから Braze に製品を同期するには、[Shopify の統合]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify#setting-up-shopify-in-braze)の [**製品の同期**] ステップで [**Shopify コレクションを同期する**] チェックボックスをオンにします。<br><br>![[Shopify コレクションを同期する] チェックボックスがオンの状態の Shopify 製品同期のステップ4。][1]

製品が同期されると、Shopify カタログを見ることで、どの製品がコレクションに関連付けられているかを確認することができます。<br><br>![ベストセラー」と「フロントページ」のコレクションにある商品を示すカタログ・テーブルの行。][2]

Shopifyカタログから、**Selections**タブでShopifyコレクションを見ることができる。<br><br>![「ベストセラー」と「フロントページという2つのコレクションのリストが表示された [選択] タブ][3]

### ベータ版機能

- Braze は最大30のコレクションをサポート予定
- 現時点では、コレクションのソート順は維持・サポートされていない。今のところ、ソート順は以下に基づいています。
    - コレクションに最近追加されたアイテム。
    - 連続シンク中にアイテムが更新される順序。
    - Shopify コレクションの選択タブで選択した順序。

## Shopifyのコレクションを使う

Shopify コレクションを使用して、[Braze セレクション]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/)を使用する場合と同様に、キャンペーンの各ユーザーに合わせてメッセージをパーソナライズします。

{% alert warning %}
ベータ版では、以下のような挙動に注意すること：<br><br>Shopifyコレクションの説明やフィルター設定を更新すると、Shopifyコレクションの同期が壊れてしまう。その結果、Shopifyコレクションは期待通りに機能しなくなる。
{% endalert %}

### ステップ1:Shopifyコレクションのソート順を設定する

1. Shopify コレクションの [選択] タブで [**ソート順**] を選択して、Shopify コレクションの結果が返される順序を指定します。これにはソート順をランダムにするオプションも含まれている。
2. [**上限数**] に結果の最大数 (50まで) を入力します。
3. [**選択の更新**] を選択します。

![フィルター設定、ソートタイプ、結果の制限を選択できる [選択の編集] ページ。][4]

### ステップ2:キャンペーンでコレクションを使用する

1. キャンペーンを作成し、メッセージコンポーザーで**「+パーソナライズ**」を選択する。
2. 以下を選択します。<br>- **カタログ項目**を**パーソナライゼーションタイプ**として選択<br>\- カタログ名<br>\- アイテム選択方法<br>\- セレクション名（Shopifyコレクション名） <br>\- メッセージに表示する情報

{: start="3"}
3\.Liquid スニペットをコピーして、メッセージ内で情報を表示する場所に貼り付けます。

![カタログ、項目選択方法、表示する情報を選択するフィールドがある「パーソナライゼーションの追加」セクション。][5]{: style="max-width:30%;"}

#### セレクション結果内の Liquid

カスタム属性やカスタム・イベントなど、カタログ内の結果を使用すると、選択したユーザーごとに異なる結果が返される可能性がある。

[1]: {% image_buster /assets/img/Shopify/sync_products.png %}
[2]: {% image_buster /assets/img/Shopify/view_catalog.png %}
[3]: {% image_buster /assets/img/Shopify/selections_tab.png %}
[4]: {% image_buster /assets/img/Shopify/edit_selection.png %}
[5]: {% image_buster /assets/img/Shopify/add_personalization.png %}
