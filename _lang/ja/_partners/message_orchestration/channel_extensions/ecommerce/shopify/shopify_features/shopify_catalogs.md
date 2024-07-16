---
nav_title: Shopify商品同期
article_title:Shopify商品同期
alias: /shopify_catalogs/
page_order:2
description:"この参考記事では、ShopifyからBrazeカタログに商品をインポートする方法について説明する。"
---

# Shopify商品同期 

> ShopifyストアからBraze[カタログに]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs)商品を同期させることができ、メッセージのパーソナライゼーションを深めるために商品データを取り込む方法をオートメーション化できる。 

Shopifyカタログは、あなたがShopifyストアの商品に編集や変更を加えると、ほぼリアルタイムで更新される。放棄カート、注文確認書などを最新の商品詳細や情報で充実させることができる。

## Shopify商品同期の設定 {#setting-up}

すでにShopifyストアをインストールしている場合でも、以下の手順で商品を同期することができる。 

### ステップ1:同期をオンにする

Shopifyのインストールフロー、またはShopifyのパートナーページから、商品をBrazeカタログに同期することができる。 

![カタログ商品識別子」に「ShopifyバリアントID」を指定した設定ステップ3。][1]{: style="max-width:70%;"}

Brazeカタログに同期された製品は、[カタログの上限に]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#limits)貢献する。

### ステップ2:製品識別子を選択する

カタログIDとして使用する製品識別子を選択する：
- ShopifyバリアントID
- SKU

選択した製品識別子のIDおよびヘッダー値には、文字、数字、ハイフン、アンダースコアのみを含めることができる。製品識別子がこの形式に従っていない場合、Brazeはカタログ同期からフィルターをかける。

Brazeカタログ情報を参照する際に使用する主要識別子となる。 

{% alert note %}
カタログIDとしてSKUを設定する場合、ストアのすべての商品とバリアントにSKUが設定され、それらが一意であることを確認すること。 
- 商品にSKUがない場合、Brazeはその商品をカタログに同期できない。 
- 同じSKUを持つ商品が複数ある場合、予期せぬ動作を引き起こしたり、重複したSKUによって意図せず商品情報が上書きされたりする可能性がある。
{% endalert %}

### ステップ3:同期中

ダッシュボードに通知が届き、ステータスが "In Progress "と表示され、最初の同期が開始される。同期が完了するまでにかかる時間は、BrazeがShopifyから同期する必要がある商品やバリアントの数によって異なる。この間は、このページから離れ、ダッシュボード通知やメールで完了が通知されるのを待つことができる。

最初の同期が[カタログの上限を](https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/catalogs/catalog/#limits)超えた場合、Brazeはそれ以上の商品の同期を停止するので注意すること。同期が成功した後、時間の経過とともに新しい製品が追加されたために制限を超えた場合、同期はもはや有効ではない。いずれの場合も、Shopifyからの商品更新はBrazeに反映されなくなる。アカウントマネージャーに連絡して、アップグレードを検討しよう。 

### ステップ 4:同期が完了した

同期が成功すると、ダッシュボード通知とメールが届く。Shopifyのパートナーページでも、Shopifyカタログのステータスが「同期中」に更新される。Shopifyのパートナーページでカタログ名をクリックすると商品を見ることができる。

[カタログ](https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/catalogs/catalog/#additional-use-cases)データを活用してメッセージをパーソナライズする方法については、[カタログの追加ユースケースを](https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/catalogs/catalog/#additional-use-cases)参照されたい。

#### 対応Shopifyカタログデータ

{% alert note %}
`product_handle` と`product_url` にアクセスして使用するには、Shopify カタログを切断して再接続する。
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
Shopifyのカタログを何らかの方法で変更すると、意図せずリアルタイムの商品同期に支障をきたす可能性がある。Shopifyによって上書きされる可能性があるため、Shopifyカタログに編集を加えないこと。代わりに、Shopifyインスタンスで必要な商品更新を行う。<br><br>Shopifyカタログを削除するには、Shopifyのページに行き、同期を解除する。Shopifyカタログをカタログページで直接削除しないこと。
{% endalert %}

## カタログIDを変更する

Shopifyカタログの商品識別子を変更するには、同期を解除する必要がある。まず、このShopifyカタログデータを使用した送信を停止していることを確認する。Shopifyカタログの初期同期を再実行し、[製品同期の](#setting-up)ステップに従って希望の製品識別子を選択する。

## 製品同期を停止する {#deactivate}

Shopifyの商品同期機能を無効にすると、カタログと商品がすべて削除される。また、このカタログの製品データを積極的に使用しているセンズにも影響を与える可能性がある。無効化する前に、これらの送信を更新または一時停止していることを確認する。これにより、メッセージングで商品詳細が送信されなくなる可能性がある。Shopifyカタログをカタログページで直接削除しないこと。

## トラブルシューティング
Shopifyの商品同期がエラーになった場合、以下のようなエラーの可能性がある。問題を修正し、同期を解決する方法の指示に従う：

| エラー | 理由 | ソリューション |
| --- | --- | --- |
| サーバーエラー | これは、Shopify側で商品の同期を試みた際にサーバーエラーが発生した場合に発生する。 | [同期を解除](#deactivate)し、全在庫商品を再度同期する。 |
| 重複SKU | これは、SKUをカタログアイテムIDとして使用し、同じSKUを持つ商品がある場合に発生する。カタログのアイテムIDはユニークでなければならないので、すべての商品はユニークなSKUを持たなければならない。 | Shopifyで商品とバリアントの全リストを監査し、SKUの重複がないことを確認する。SKUが重複している場合は、ShopifyストアアカウントでのみユニークなSKUに更新する。これが修正されたら、[同期を解除](#deactivate)し、全在庫商品を再度同期する。 |
| カタログの上限を超えた | これは、カタログの上限を超えた場合に発生する。Brazeは、ストレージの空き容量がなくなったため、同期を終了したり、同期をアクティブに保つことができなくなる。 | この問題には2つのソリューションがある：<br><br>1\.アカウントマネージャーに連絡して、カタログの上限を増やすためにティアをアップグレードする。<br><br>2\.以下のいずれかを削除して、ストレージの空き容量を確保する：<br>\- 他のカタログに掲載されている商品をカタログに掲載する。<br>\- その他のカタログ<br>\- セレクションの作成<br><br> いずれかのソリューションを使用した後、同期を一旦解除し、再度同期する必要がある。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

[1]: {% image_buster /assets/img/Shopify/sync_products_step1.png %}