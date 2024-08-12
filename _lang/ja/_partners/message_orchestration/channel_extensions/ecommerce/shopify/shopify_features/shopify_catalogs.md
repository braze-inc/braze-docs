---
nav_title: Shopify商品同期
article_title: Shopify商品同期
alias: /shopify_catalogs/
page_order: 2
description: "この参考記事では、ShopifyからBrazeカタログに商品をインポートする方法を説明します。"
---

# Shopify商品同期 

> ShopifyストアからBraze[カタログに]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs)商品を同期し、商品データを取り込む方法を自動化することで、メッセージのパーソナライゼーションを深めることができます。 

Shopifyカタログは、Shopifyストアの商品に編集や変更を加えると、ほぼリアルタイムで更新されます。カート放棄、注文確認など、最新の商品詳細や情報を充実させることができます。

## Shopify商品同期の設定 {#setting-up}

すでにShopifyストアをインストールしている場合でも、以下の手順で商品を同期することができます。 

### ステップ1:同期をオンにする

ShopifyのインストールフローまたはShopifyのパートナーページから、商品をBrazeカタログに同期することができます。 

ShopifyバリアントID "を "カタログ商品識別子 "としたセットアッププロセスのステップ3][1]。{: style="max-width:70%;"}

Brazeカタログに同期された製品は、[カタログの上限に]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#limits)貢献します。

### ステップ2:製品識別子を選択

カタログIDとして使用する製品識別子を選択します：
Shopify バリアント ID
SKU

選択した製品識別子のIDおよびヘッダー値には、文字、数字、ハイフン、アンダースコアのみを含めることができます。製品識別子がこの形式に従っていない場合、Brazeはカタログ同期から除外します。

これは、Brazeのカタログ情報を参照する際に使用する主要な識別子となります。 

{% alert note %}
カタログIDとしてSKUを選択する場合、ストア内のすべての商品とバリアントにSKUが設定され、それらが一意であることを確認してください。
\- 商品にSKUがない場合、Brazeはその商品をカタログに同期することができません。
\- 同じSKUを持つ商品が複数ある場合、予期せぬ動作を引き起こしたり、重複したSKUによって意図せず商品情報が上書きされたりする可能性があります。
{% endalert %}

### ステップ3:同期中

ダッシュボードに通知が届き、ステータスが「進行中」と表示され、最初の同期が開始されることを示します。同期が完了するまでの時間は、BrazeがShopifyから同期する必要のある商品やバリエーションの数によって異なります。この間、このページから離れ、ダッシュボードの通知またはEメールによる完了通知を待つことができます。

最初の同期が[カタログの上限を](https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/catalogs/catalog/#limits)超えた場合、Brazeはそれ以上の商品の同期を停止しますのでご注意ください。シンクが成功した後、時間の経過とともに新しい商品が追加され、制限を超えた場合、シンクは無効になります。どちらの場合も、Shopifyからの商品アップデートはBrazeに反映されなくなります。アカウント・マネージャーにご連絡の上、アップグレードをご検討ください。 

### ステップ4:同期完了

同期が成功すると、ダッシュボードに通知とメールが届きます。Shopifyパートナーページでは、Shopifyカタログのステータスが「同期中」に更新されます。Shopifyのパートナーページでカタログ名をクリックすると商品を見ることができます。

[カタログ](https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/catalogs/catalog/#additional-use-cases)データを活用してメッセージをパーソナライズする方法については、[カタログのその他の使用](https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/catalogs/catalog/#additional-use-cases)例を参照してください。

#### 対応Shopifyカタログデータ

{% alert note %}
`product_handle` と`product_url` にアクセスして使用するには、Shopify カタログを切断して再接続してください。
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
Shopifyカタログを何らかの方法で変更すると、意図せずリアルタイムの商品同期に支障をきたす可能性があります。Shopifyカタログを編集しないでください。Shopifyによって上書きされる可能性があります。代わりに、Shopifyインスタンスで必要な商品アップデートを行う。<br><br>Shopifyカタログを削除するには、Shopifyのページに行き、同期を停止します。カタログページでShopifyカタログを直接削除しないでください。
{% endalert %}

## カタログIDの変更

Shopifyカタログの商品識別子を変更するには、同期を解除する必要があります。まず、このShopifyカタログデータを使用した送信を停止していることを確認してください。Shopifyカタログの初期同期を再実行し、[商品同期の](#setting-up)ステップに従って希望の商品識別子を選択します。

## 製品同期の停止 {#deactivate}

Shopifyの商品同期機能を無効にすると、カタログと商品がすべて削除されます。また、このカタログの製品データを積極的に使用しているセンドにも影響を与える可能性がある。無効化する前に、これらの送信を更新または一時停止していることを確認してください。カタログページでShopifyカタログを直接削除しないでください。

## トラブルシューティング
Shopifyの商品同期でエラーが発生した場合、以下のエラーの可能性があります。問題を修正し、同期を解決する方法の指示に従ってください：

| Error | Reason | Solution |
| --- | --- | --- |
| サーバーエラー｜商品の同期を行おうとした際に、Shopify側でサーバーエラーが発生した場合に発生します。[| 同期を解除](#deactivate)し、全商品を再度同期してください。|
| SKUの重複｜SKUをカタログアイテムIDとして使用し、同じSKUを持つ商品がある場合に発生します。カタログのアイテムIDは一意でなければならないので、すべての商品は一意のSKUを持たなければなりません。| SKUが重複していないことを確認するために、Shopifyで商品とバリアントの全リストを監査してください。SKUが重複している場合は、ShopifyストアアカウントでのみユニークなSKUに更新してください。これが修正されたら、[同期を解除](#deactivate)し、全在庫商品を再度同期してください。|
| カタログの上限を超えると発生します。Brazeは、ストレージの空き容量がないため、同期を終了することも、同期をアクティブに保つこともできません。| この問題には2つの解決策があります：<br><br>1. カタログの上限を増やすには、アカウントマネージャーまでご連絡ください。<br><br>2. 以下のいずれかを削除して、ストレージの空き容量を確保する：<br>\- 他のカタログのカタログ商品<br>\- その他のカタログ<br>\- セレクション<br><br> いずれかの解決策を使用した後、同期を一旦解除し、再度同期する必要があります。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

[1]: {% image_buster /assets/img/Shopify/sync_products_step1.png %}