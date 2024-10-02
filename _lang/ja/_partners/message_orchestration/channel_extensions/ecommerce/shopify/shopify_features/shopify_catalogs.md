---
nav_title: Shopifyプロダクトシンク
article_title: Shopifyプロダクトシンク
alias: /shopify_catalogs/
page_order: 2
description: "このリファレンス記事では、Shopify からBraze カタログ s に商品をインポートする方法について説明します。"
---

# Shopifyプロダクトシンク 

> Shopify ストアからBraze [カタログ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs) に製品を同期することで、より深いパーソナライゼーションのために製品データを取り込む方法を自動化できます。 

Shopify カタログ s は、Shopifyストア内のプロダクトを編集および変更すると、ほぼリアルタイムで更新します。最新の商品詳細とインフォメーションで、放棄カート or カート放棄、オーダーコンファメーションなどを充実させることができます。

## Shopifyプロダクトシンクのセットアップ {#setting-up}

Shopifyストアがすでにインストールされている場合でも、以下の手順に従って商品を同期できます。 

### ステップ1:同期をオンにする

ShopifyのインストールフローまたはShopifyパートナページで、製品をBraze カタログに同期できます。 

![" Shopify Variant ID" as " as the " Catalog product 識別子" で設定された処理の手順3。][1]{: style="max-width:70%;"}

Braze カタログに同期されたプロダクトは、[ カタログ制限]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#limits) に影響します。

### ステップ2:プロダクト識別子の選択

カタログ ID として使用するプロダクト識別子を選択します。
- ShopifyバリアントID
- SKU

選択するプロダクト識別子のID とヘッダーは、文字、数字、ハイフン、アンダースコアのみを含めることができます。プロダクト識別子がこの形式に従わない場合、Braze はカタログの同期からフィルターされます。

これは、Braze カタログのリファレンスに使用する主な識別子です。 

{% alert note %}
カタログ ID としてSKU を選択する場合は、ストア内のすべての製品とバリアントにSKU が設定されており、それらが一意であることを確認してください。 
- アイテムにSKU がない場合、Braze はそのアイテムをカタログに同期できません。 
- 同じSKU を持つ複数の製品がある場合、予期しない動作が発生したり、重複したSKU によって意図せずに製品情報が上書きされる可能性があります。
{% endalert %}

### ステップ3:同期中

ダッシュボード 通知が表示され、ステータスに「実行中」と表示され、最初の同期が開始されていることを示します。シンクが完了するまでの時間は、プロダクト数とバリアントのBrazeがShopifyからシンクオーバーする必要があるかによって異なります。この間、このページから離れて、ダッシュボード 通知またはメールが完了したときに通知するまで待機できます。

最初の同期が[カタログ制限]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#limits)を超えた場合、Brazeはこれ以上のプロダクトの同期を中止します。時間の経過とともに新しい製品が追加されたために同期が成功した後に制限を超えた場合、同期はアクティブではなくなります。いずれの場合も、Shopifyからの商品更新はBrazeに反映されなくなります。アカウントマネージャーに連絡して、階層のアップグレードを検討してください。 

### ステップ4:同期完了

同期が成功すると、ダッシュボード 通知とメールが表示されます。Shopifyパートナページでは、Shopify カタログ s の「同期とクォート;」にステータスも更新されます。Shopifyパートナページでカタログの名前をクリックすると、商品を表示できます。

カタログデータを利用してメッセージをパーソナライズする方法の詳細については、[カタログの追加ユースケースs]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#additional-use-cases)を参照してください。

#### 対応Shopify カタログ

{% alert note %}
`product_handle` および`product_url` にアクセスして使用するには、Shopify カタログを切断してから再接続します。
{% endalert %}

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
Shopify カタログを任意の方法で変更すると、意図せずにリアルタイムのプロダクト同期に干渉する可能性があります。Shopify カタログは、Shopifyによって上書きされる可能性があるため、編集しないでください。代わりに、Shopifyで必要なプロダクト更新を作成します。<br><br>Shopify カタログを削除するには、「Shopify」を選択し、「シンク」をオフにします。カタログ s ページのShopify カタログをそのまま消去しないでください。
{% endalert %}

## バック・イン・ストック、株価下落ユースケース 

バックアップインストック通知s を設定するには、ステップs [ここで]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/back_in_stock_notifications#back-in-stock-notifications) を実行します。

価格低下通知s を設定するには、ステップs [ここで]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/price_drop_notifications) を実行します。

Shopifyインテグレーションでは、ユースケースごとにユーザーのサブスクリプション ステータスをカタログにキャプチャするカスタムイベントを作成する必要があります。カスタムイベントには、Shopifyプロダクトシンクの一部として選択した[SKU またはShopify バリアント ID]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_features/shopify_catalogs#step-2-select-your-product-identifier) のいずれかにマップされるイベントプロパティが必要です。 


## カタログ番号を変更する

Shopify カタログのプロダクト識別子を変更するには、シンクを無効にする必要があります。まず、このShopify カタログデーターを使用して送信を停止したことを確認します。Shopify カタログのイニシャルシンクを再実行し、[product sync](#setting-up) ステップ s に従って目的のプロダクト識別子を選択します。

## 製品の同期を無効にする {#deactivate}

Shopifyプロダクトシンク機能を無効にすると、カタログとプロダクト全体が削除されます。これは、このカタログからのプロダクトデータをアクティブに使用している可能性がある送信にも影響します。更新 d または一時停止した送信が無効になっていることを確認します。これにより、メッセージングが欠落した商品情報を送信する可能性があります。カタログ s ページのShopify カタログをそのまま消去しないでください。

## トラブルシューティング
Shopifyプロダクトの同期がエラーに実行される場合、次のエラーが原因である可能性があります。問題を修正し、同期を解決する方法については、次の手順に従ってください。

| エラー | 理由 | ソリューション |
| --- | --- | --- |
| サーバーエラー | これは、プロダクトを同期しようとしたときに、Shopify側にサーバーエラーがある場合に発生します。 | [sync](#deactivate)を無効にし、製品のインベントリ全体を再同期します。 |
| 重複SKU | これは、カタログアイテムID としてSKU を使用し、同じSKU の製品がある場合に発生します。カタログアイテムID は一意である必要があるため、すべての製品に一意のSKU が必要です。 | Shopify で製品とバリアントの一覧をすべて監査して、重複するSKU がないことを確認します。SKU が重複している場合は、Shopifyストアアカウントでのみ一意のSKU になるように更新します。これが修正された後、[sync](#deactivate) を非アクティブ化し、製品のインベントリ全体を再同期します。 |
| カタログ制限を超過 | これは、カタログ制限を超えた場合に発生します。Brazeは、ストレージの可用性がなくなるため、同期を終了したり、同期を有効にしておくことができません。 | この問題には2 つのソリューションがあります。<br><br>1\.カタログの制限を増やすために、アカウントマネージャーにリーチして階層をアップグレードします。<br><br>2\.次のいずれかを削除して、ストレージ領域を解放します。<br>\- 他のカタログsからのカタログアイテム<br>\- 他のカタログ<br>\- 作成された選択<br><br> いずれかのソリューションs を使用した後、同期を無効にしてから再同期する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

[1]: {% image_buster /assets/img/Shopify/sync_products_step1.png %}