---
nav_title: Shopify製品の同期
article_title: Shopify製品の同期
alias: /shopify_catalogs/
page_order: 2
description: "このリファレンス記事では、ShopifyからBrazeカタログに製品をインポートする方法について説明します。"
---

# Shopify製品の同期 

> Shopifyストアの商品をBrazeの[カタログ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs)に同期し、商品データの取り込み方法を自動化して、メッセージをより詳細にパーソナライズできます。 

Shopifyのカタログは、Shopifyストアの商品の編集や変更を行うと、ほぼリアルタイムで更新されます。放棄されたカートや注文確認など、最新の商品詳細や情報を充実させることができます。

## Shopify製品の同期{#setting-up}を設定する

Shopifyストアをインストール済みの場合でも、以下の手順に従って製品を同期できます。 

### ステップ1:同期をオンにする

ShopifyのインストールフローまたはShopifyパートナーページで製品をBrazeカタログに同期できます。 

![「カタログ製品識別子」に「Shopify Variant ID」を使用したセットアップ手順3][1]{: style="max-width:70%;"}

Brazeカタログに同期された製品は、[カタログ制限]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#limits)に貢献します。

### ステップ2:製品識別子を選択してください

カタログIDとして使用する製品識別子を選択します。
\- Shopify バリアント ID
\- SKU

選択した製品識別子のIDとヘッダー値には、文字、数字、ハイフン、アンダースコアのみを含めることができます。製品識別子がこの形式に従っていない場合、Brazeはカタログ同期から除外します。

これは、Brazeカタログ情報を参照するために使用する主要な識別子になります。 

{% alert note %}
カタログIDとしてSKUを選択する場合は、ストア内のすべての製品とバリエーションにSKUセットがあり、それらが一意であることを確認してください。
-商品に不足しているSKUがある場合、Brazeはその商品をカタログに同期できません。
-同じSKUの製品が複数ある場合、予期しない動作が発生したり、製品情報が意図せず重複したSKUによって上書きされる可能性があります。
{% endalert %}

### ステップ3:同期中

ダッシュボードに通知が届き、ステータスが「実行中」と表示されます。同期が終了するまでの時間は、BrazeがShopifyから同期する必要がある製品やバリエーションの数によって異なることに注意してください。この間、このページを離れ、ダッシュボード通知または電子メールで通知されるのを待つことができます。

最初の同期[がカタログ制限](https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/catalogs/catalog/#limits)を超えた場合、Brazeはそれ以降の製品の同期を停止しますのでご注意ください。同期が成功した後、時間の経過とともに新しい製品が追加されたために制限を超えた場合、同期はアクティブではなくなります。いずれの場合も、Shopifyからの製品アップデートはBrazeに反映されなくなります。メンバーシップレベルのアップグレードについては、アカウントマネージャにお問い合わせください。 

### ステップ4:同期が完了しました

同期が成功するとダッシュボード通知とメールが届きます。Shopifyパートナーページでは、Shopifyカタログの下にあるステータスも「同期中」に更新されます。Shopifyパートナーページのカタログ名をクリックすると、製品を表示できます。

カタログデータを活用してメッセージをパーソナライズする方法の詳細については、「[カタログの追加使用](https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/catalogs/catalog/#additional-use-cases)例」を参照してください。

#### Shopifyのカタログデータに対応

{% alert note %}
`product_handle`と`product_url`にアクセスして使用するには、Shopifyカタログを切断して再接続します。
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
Shopifyカタログを何らかの方法で修正すると、意図せずリアルタイムの製品同期に支障をきたす可能性があります。ShopifyカタログはShopifyによって上書きされる可能性があるため、編集を加えないでください。代わりに、Shopifyインスタンスで必要な製品アップデートを行います。<br><br>Shopifyカタログを削除するには、Shopifyページに移動して同期を解除します。カタログページでShopifyカタログを直接削除しないでください。
{% endalert %}

## カタログIDの変更

Shopifyカタログの製品識別子を変更するには、同期を解除する必要があります。まず、このShopifyカタログデータを使用して送信を停止したことを確認します。Shopifyカタログの初期同期を再実行し、[製品同期](#setting-up)の手順に従って目的の製品識別子を選択します。

## 製品の同期{#deactivate}を無効にする

Shopify製品同期機能を無効にすると、カタログ全体と製品が削除されます。これは、このカタログの製品データを積極的に使用している可能性のある送信にも影響する可能性があります。非アクティブ化する前に、これらの送信を更新または一時停止していることを確認してください。製品の詳細が欠落しているメッセージが送信される可能性があります。カタログページでShopifyカタログを直接削除しないでください。

## トラブルシューティング
Shopify製品の同期でエラーが発生した場合は、以下のエラーが考えられます。問題の修正方法および同期の解決方法の指示に従います。

|エラー|原因|解決方法|
| --- | --- | --- |
|サーバーエラー|お客様の製品を同期しようとしたときにShopify側でサーバーエラーが発生した場合に発生します。|[同期を解除](#deactivate)し、製品のインベントリ全体を再同期してください。|
| SKUの重複 | カタログ商品IDにSKUを使用し、同じSKUの商品がある場合に発生します。カタログアイテムIDは一意でなければならないため、すべての製品に一意のSKUが必要です。 | Shopifyで製品とバリエーションの完全なリストを監査し、SKUが重複していないことを確認します。SKUが重複している場合は、Shopifyストアアカウントのみで一意のSKUになるように更新します。これを修正したら、[同期を解除](#deactivate)し、製品のインベントリ全体を再度同期してください。|
|カタログの制限を超えました|カタログの制限を超えた場合に発生します。Brazeは、ストレージの可用性がなくなるため、同期を終了することも、同期をアクティブに維持することもできなくなります。|この問題を解決するには、次の2つの方法があります。<br><br>1. カタログの上限を増やすためにメンバーシップレベルをアップグレードする場合は、アカウントマネージャにお問い合わせください。<br><br>2. 次のいずれかを削除して、ストレージ容量を解放します。<br>-他のカタログのカタログアイテム<br>-その他のカタログ<br>-作成された選択範囲<br><br> いずれかのソリューションを使用した後、同期を無効にしてから再同期する必要があります。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

[1]: {% image_buster /assets/img/Shopify/sync_products_step1.png %}