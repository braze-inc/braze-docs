---
nav_title: Shopify 製品の同期
article_title: Shopify 製品の同期
alias: /shopify_catalogs/
page_order: 4
description: "このリファレンス記事では、Shopify から Braze カタログに製品をインポートする方法について説明します。"
---

# Shopify 製品の同期 

> Shopify ストアの全商品を Braze[ カタログ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs)に同期し、より深いメッセージングパーソナライゼーションを実現できます。 

Shopify ストア内の製品に編集や変更を加えると、Shopify カタログがほぼリアルタイムで更新されます。最新の製品詳細や情報を使用して、カート放棄や注文確認などを強化できます。

## Shopify 製品の同期を設定する {#setting-up}

Shopifyストアがすでにインストールされている場合でも、以下の手順に従って商品を同期できます。 

### ステップ1:同期をオンにする

ShopifyのインストールフローまたはShopifyパートナページで、製品をBraze カタログに同期できます。 

![設定プロセスのステップ3。「カタログの製品の識別子」に「Shopify バリアント ID」が設定されている。][1]{: style="max-width:70%;"}

Braze カタログに同期された製品は、[カタログ制限]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#limits)の対象になります。

### ステップ2:プロダクト識別子の選択

カタログ ID として使用するプロダクト識別子を選択します。
- ShopifyバリアントID
- SKU

選択するプロダクト識別子の ID とヘッダーの値には、文字、数字、ハイフン、アンダースコアのみを使用できます。プロダクト識別子がこの形式に従っていない場合、Braze はカタログの同期からその識別子を除外します。

これは、Braze カタログ情報を参照するときに使用する主要な識別子です。 

{% alert note %}
カタログ ID としてSKU を選択する場合は、ストア内のすべての製品とバリアントにSKU が設定されており、それらが一意であることを確認してください。 
- アイテムに SKU が設定されていない場合、Braze はその製品をカタログに同期できません。 
- 同じSKU を持つ複数の製品がある場合、予期しない動作が発生したり、重複したSKU によって意図せずに製品情報が上書きされる可能性があります。
{% endalert %}

### ステップ3:同期中

ダッシュボード 通知が表示され、ステータスに「実行中」と表示され、最初の同期が開始されていることを示します。同期の完了にかかる時間は、Braze が Shopify から同期する必要がある製品やバリアントの数によって異なることに注意してください。この間、このページから離れて、同期完了を通知するダッシュボード通知またはメールが届くまで待つことができます。

最初の同期が[カタログ制限]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#limits)を超えた場合、Brazeはこれ以上のプロダクトの同期を中止します。時間の経過とともに新しい製品が追加されたために同期が成功した後に制限を超えた場合、同期はアクティブではなくなります。いずれの場合も、Shopifyからの商品更新はBrazeに反映されなくなります。ティアのアップグレードを検討する場合はアカウントマネージャーにご連絡ください。 

### ステップ4:同期完了

同期が成功するとダッシュボード通知とメールが届きます。Shopify パートナーページでも、Shopify カタログの下のステータスが [Syncing] に更新されます。Shopify パートナページでカタログの名前をクリックすると、製品を表示できます。

カタログデータを利用してメッセージをパーソナライズする方法の詳細については、[カタログの追加ユースケースs]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#additional-use-cases)を参照してください。

#### サポートされている Shopify カタログデータ

- `id`
- `store_name`
- `shopify_product_id`
- `shopify_variant_id`
- `product_title`
- `variant_title`
- `status`
- `body_html`
- `product_image_url`
- `variant_image_url`
- `vendor`
- `product_type`
- `product_url`
- `product_handle`
- `published_scope`
- `price`
- `compare_at_price`
- `inventory_quantity`
- `options`
- `option_values`
- `sku`

{% alert warning %}
Shopify カタログを任意の方法で変更すると、意図せずにリアルタイムのプロダクト同期に干渉する可能性があります。Shopify カタログは、Shopifyによって上書きされる可能性があるため、編集しないでください。代わりに、Shopify インスタンスで必要な製品更新を行います。<br><br>Shopify カタログを削除するには、Shopify ページに移動し、同期を非アクティブにします。カタログページで Shopify カタログを直接削除しないでください。
{% endalert %}

##### `product_handle` または `product_url`

`product_handle` と`product_url` にアクセスして使用するには、以下の方法で Shopify カタログを切断し、再接続します。

1. Shopify の統合ページに行き、[**構成を編集**] を選択します。

![Shopifyの統合ページ。]({% image_buster /assets/img/Shopify/edit_config.png %})

{: start="2"}
2\.**カタログを同期する**ステップで、カタログをオフに切り替えてから設定を更新する。
3\.カタログを切り替え、設定を更新する。

![Shopify「カタログを同期」ステップをカタログトグルで切り替える]({% image_buster /assets/img/Shopify/catalog_toggle.png %})

## 再入荷と値下げのユースケース

再入荷通知を設定するには、[こちら]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/back_in_stock_notifications#back-in-stock-notifications)の手順に従ってください。

価格低下通知s を設定するには、ステップs [ここで]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/price_drop_notifications/) を実行します。

Shopifyインテグレーションでは、ユースケースごとにユーザーのサブスクリプション ステータスをカタログにキャプチャするカスタムイベントを作成する必要があります。カスタムイベントには、Shopifyプロダクトシンクの一部として選択した[SKU またはShopify バリアント ID]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_features/shopify_catalogs#step-2-select-your-product-identifier) のいずれかにマップされるイベントプロパティが必要です。 

## カタログ番号を変更する

Shopify カタログのプロダクト識別子を変更するには、シンクを無効にする必要があります。まず、この Shopify カタログデータを使用したメッセージの送信を停止していることを確認します。Shopify カタログの初回同期を再実行し、[製品の同期](#setting-up)の手順に従って目的の製品識別子を選択します。

## 製品の同期の非アクティブ化 {#deactivate}

Shopify 製品の同期機能を非アクティブにすると、カタログと製品がすべて削除されます。この操作は、このカタログの製品データをアクティブに使用している可能性があるすべてのメッセージに影響する可能性もあります。商品詳細のないメッセージが送信される可能性があるため、無効化する前にキャンペーンまたはキャンバスを更新または一時停止していることを確認する。カタログページで Shopify カタログを直接削除しないでください。

## トラブルシューティング
Shopify 製品の同期でエラーが発生した場合は、次のいずれかのエラーが原因である可能性があります。問題を修正し、同期を解決する方法については、次の手順に従ってください。

| エラー | 理由 | ソリューション |
| --- | --- | --- |
| サーバーエラー | これは、プロダクトを同期しようとしたときに、Shopify側にサーバーエラーがある場合に発生します。 | [同期を非アクティブにし](#deactivate)、製品の在庫全体を再同期します。 |
| 重複する SKU | これは、カタログアイテム ID としてSKU を使用している場合に、複数の製品に同じ SKU が設定されていると発生します。カタログアイテム ID は一意でなければならないため、すべての製品に一意の SKU が必要です。 | Shopify で製品とバリアントの一覧をすべて監査して、重複するSKU がないことを確認します。SKU が重複している場合は、Shopifyストアアカウントでのみ一意のSKU になるように更新します。これが修正された後、[sync](#deactivate) を非アクティブ化し、製品のインベントリ全体を再同期します。 |
| カタログ制限の超過 | これは、カタログ制限を超えた場合に発生します。Braze は、利用可能なストレージがないために、同期を終了することや、同期をアクティブな状態で維持することができなくなります。 | この問題には2 つのソリューションがあります。<br><br>1\.アカウントマネージャーに連絡して、ティアをアップグレードしてカタログ制限を引き上げます。<br><br>2\.次のいずれかを削除して、ストレージ領域を解放します。<br>\- 他のカタログsからのカタログアイテム<br>\- 他のカタログ<br>\- 作成されたセレクション<br><br> いずれの解決策を取った場合でも、同期を非アクティブにしてから再同期を実行する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

[1]: {% image_buster /assets/img/Shopify/sync_products_step1.png %}