---
nav_title: eコマースのユースケース
article_title: eコマースのユースケース
alias: /ecommerce_use_cases/
page_order: 4
description: "このリファレンス記事では、e コマースのマーケター向けにカスタマイズされた、事前構築済みのさまざまな Braze テンプレートについて説明し、必要な戦略を簡単に実施できるようにします。"
toc_headers: h2
---

# eコマースのユースケース

> Braze Canvas には、eCommerce マーケター専用にあらかじめ作成されたテンプレートがいくつか用意されています。これにより、必須戦略の実装が容易になります。このページには、カスタマージャーニーを強化するために使用できるいくつかの主要なテンプレートが用意されています。

{% alert important %}
[e コマースの推奨イベント]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events/)は現在、早期アクセス段階です。早期アクセスに参加したい場合は、Braze カスタマーサクセスマネージャーにお問い合わせください。<br><br>新しいShopifyコネクターを使用している場合、eCommerceの推奨イベントは統合によって自動的に利用可能になります。
{% endalert %}

## キャンバステンプレートの使用

キャンバステンプレートを使用するには:
1. [**メッセージング**] > [**キャンバス**] に進みます。
2. [**キャンバスを作成** > [**キャンバステンプレートを使用**] を選択します。
3. 使用するテンプレートの [**Braze テンプレート**] タブを参照します。テンプレートの名前を選択すると、テンプレートをプレビューできます。
4. 使用するテンプレートの [**テンプレートを適用**] を選択します。<br><br>!["Canvas テンプレート s" page 開封は" s" tab で、最近使用したテンプレートと選択可能なBraze テンプレートの一覧を表示します。]({% image_buster /assets/img_archive/apply_template.png %}){: style="max-width:80%;"}

## eコマーステンプレート

- [閲覧の放棄](#abandoned-browse)
- [カート放棄](#abandoned-cart)
- [購入手続き放棄](#abandoned-checkout)
- [注文確認とフィードバック調査](#order-confirmation--feedback-survey)

## 閲覧の放棄

製品を閲覧したが、カートへの追加や注文を行わなかったユーザーにエンゲージするには、**閲覧の放棄**テンプレートを使用します。

![アプリが"Abandoned Browse"拡張された"Entry Rules"を含むキャンバステンプレート。]({% image_buster /assets/img_archive/abandoned_browse.png %})

### 設定

キャンバスページで [**キャンバステンプレートを使用**] > [**Braze テンプレート**] を選択し、**閲覧の放棄**テンプレートを適用します。 

#### デフォルト設定

キャンバスでは、次の設定が事前に行われています。
- 基本情報 
    - キャンバス名:**閲覧の放棄**
    - 変換イベント: `ecommerce.order placed`
        - コンバージョンの期限:3日間 
- エントリスケジュール 
    - ユーザーが `ecommerce.product_viewed` イベントを実行する場合はアクションベース
    - 開始時刻は、キャンバステンプレートを作成するときです<br><br>!["アクションベースのオプションとクォート;キャンバス用。]({% image_buster /assets/img/ecommerce/abandoned_browse_entry.png %})<br><br> 
- ターゲットオーディエンス 
    - エントリオーディエンス 
        - メールが**空白ではない**
        - また、ビジネスニーズを満たすようにエントリオーディエンス基準を変更することもできます
    - 入力コントロール
        - キャンバスの完全な期間が完了した後で、ユーザーはこのキャンバスに再エントリできます。
    - 終了条件 
        - `ecommerce.cart_updated`、`ecommerce.checkout_started`、または `ecommerce.order_placed` を実行する<br><br>![キャンバスの入力コントロールs と終了基準。]({% image_buster /assets/img/ecommerce/abandoned_browse_entry_exit.png %})<br><br> 
- 送信設定 
    - 登録済みまたはオプトイン済みのユーザー 
- 遅延ステップ
    - 1時間遅延
- メッセージステップ 
    - Liquid のテンプレート作成の例を使用して、メールテンプレートと HTML ブロックを確認し、あらかじめ用意されているテンプレートでメッセージに製品を追加します。独自のメールテンプレートを使用する場合は、次のセクションに示すように、[液体変数](#message-personalization) を参照することもできます。

### メール向けの閲覧の放棄の製品パーソナライゼーション 

閲覧の放棄のメール用の HTML 製品ブロックを追加する方法の例を以下に示します。 

{% raw %}
```java
<table style="width:100%">
  <tr>
    <th><img src="{{context.${image_url}}}" width="200" height="200"><img></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{context.${product_name}}}</li>
        <li>Price: ${{context.${price}}}</li>
      </ul>
    </th>
  </tr>
</table>
```
{% endraw %}

#### 製品URL

{% raw %}
```liquid
{{context.${product_url}}}
```
{% endraw %}    

## カート放棄

カートに製品を追加したが、購入手続きまたは注文に進まなかった顧客からの潜在的な売上の損失に対応するには、**カート放棄**テンプレートを使用します。 

![アプリが"Abandoned Cart"拡張された"Entry Rules"を含むキャンバステンプレート。]({% image_buster /assets/img_archive/abandoned_cart.png %})

### 設定

キャンバスページで [**キャンバステンプレートを使用**] > [**Braze テンプレート**] を選択し、**カート放棄**テンプレートを適用します。 

#### デフォルト設定

キャンバスでは、次の設定が事前に行われています。
- 基本情報 
    - キャンバス名:**カート放棄**
    - 変換イベント: `ecommerce.order_placed`
        - コンバージョンの期限:3日間 
- エントリスケジュール 
    - ユーザーが (ドロップダウンにある) [**カート更新済みイベントの実行**] をトリガーしたときのアクションベースのトリガー
    - 開始時刻は、キャンバステンプレートを作成するときです<br><br>!["アクションベースのオプションとクォート;キャンバス用。]({% image_buster /assets/img/ecommerce/abandoned_cart_entry.png %})<br><br> 
- ターゲットオーディエンス 
    - エントリオーディエンス 
        - これらのアプリを**1回以上**使用したことがある 
        - メールが**空白ではない**
    - 入力コントロール
        - ユーザーのキャンバスへのエントリが即時に可能になります。
    - 終了条件 
        - `ecommerce.cart_updated`、`ecommerce.checkout_started`、または `ecommerce.order_placed` を実行する<br><br>![キャンバスの入力コントロールs と終了基準。]({% image_buster /assets/img/ecommerce/abandoned_cart_entry_exit.png %})<br><br> 
- 送信設定 
    - 登録済みまたはオプトイン済みのユーザー 
- 遅延ステップ
     - 4時間遅延
- メッセージステップ 
    - Liquid のテンプレート作成の例を使用して、メールテンプレートと HTML ブロックを確認し、あらかじめ用意されているテンプレートでメッセージに製品を追加します。独自のメールテンプレートを使用する場合は、次のセクションに示すように、[液体変数](#message-personalization) を参照することもできます。

### メール向けのカート放棄の製品パーソナライゼーション {#abandoned-cart-checkout}

カート放棄のユーザージャーニーでは、製品のパーソナライズに特別な Liquid タグ `shopping_cart` が必要です。 

以下の例は、`shopping_cart` Liquid タグを使用してHTML ブロックを追加し、製品をメールに追加する方法を示しています。 

{% raw %}
```java
<table style="width:100%">
  {% shopping_cart {{context.${cart_id}}} %}
  {% for item in shopping_cart.products %}
  {% catalog_items <add_your_catalog_name> {{item.variant_id}} %}
  <tr>
    <th><img src="{{ items[0].variant_image_url }}" width="200" height="200"><img></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{ item.product_name }}</li>
        <li>Price: ${{ item.price }}</li>
        <li>Quantity: ${{ item.quantity }}</li>
        <li>Variant ID: {{ item.variant_id }}</li>
        <li>Product URL:{{ item.product_url }}</li>
        <li>SKU: {{ item.metadata.sku }}</li>
      </ul>
    </th>
  </tr>
  {% endfor %}
</table>
```
{% endraw %}

{% alert note %}
Shopify を使用する場合は、カタログ名を追加してバリアントイメージURL を取得します。
{% endalert %}

#### HTML カート URL

ユーザーをカートに戻す場合は、メタデータオブジェクトの下に次のような階層化イベントプロパティを追加できます。

{% raw %}
```liquid
{{context.${metadata}.cart_url}}
```
{% endraw %}

Shopifyを使用する場合は、次のLiquidテンプレートを使用してカートURLを作成します。

{% raw %}
```liquid
{{context.${source}}}/checkouts/cn/{{context.${cart_id}}} 
```
{% endraw %}

## 購入手続き放棄

**購入手続き放棄**テンプレートを使用して、購入手続きプロセスを開始したが発注前に離脱した顧客をターゲットにします。 

![アプリが"放棄されたCheckout"拡張された"Entry Rules"を含むキャンバステンプレート。]({% image_buster /assets/img_archive/abandoned_checkout.png %})

### 設定

キャンバスページで [**キャンバステンプレートを使用**] > [**Braze テンプレート**] を選択し、**購入手続き放棄**テンプレートを適用します。 

#### デフォルト設定

キャンバスでは、次の設定が事前に行われています。

- 基本情報 
    - キャンバス名:**購入手続き放棄**
    - 変換イベント: `ecommerce.order_placed`
        - コンバージョンの期限:3日間 
- エントリスケジュール 
    - ユーザが`ecommerce.checkout_started` イベントを実行したときのアクションベースのトリガ
    - 開始時刻は、キャンバステンプレートを作成するときです<br><br>!["アクションベースのオプションとクォート;キャンバス用。]({% image_buster /assets/img/ecommerce/abandoned_checkout_entry.png %})
- ターゲットオーディエンス 
    - エントリオーディエンス 
        - これらのアプリを**1回以上**使用したことがある 
        - メールが**空白ではない**
    - 入力コントロール
        - ユーザーのキャンバスへのエントリが即時に可能になります。
        - 終了条件 
            - `ecommerce.order_placed` イベントを実行します<br><br>![キャンバスの入力コントロールs と終了基準。]({% image_buster /assets/img/ecommerce/abandoned_checkout_entry_exit.png %})<br><br>
- 送信設定 
    - 登録済みまたはオプトイン済みのユーザー 
- 遅延ステップ
    - 4時間遅延
- メッセージステップ 
    - Liquid のテンプレート作成の例を使用して、メールテンプレートと HTML ブロックを確認し、あらかじめ用意されているテンプレートでメッセージに製品を追加します。独自のメールテンプレートを使用する場合は、次のセクションに示すように、[液体変数](#message-personalization) を参照することもできます。

### メール向けの購入手続き放棄の製品パーソナライゼーション

購入手続き放棄のユーザージャーニーでは、製品のパーソナライズに特別な Liquid タグ `shopping_cart` が必要です。 

以下の例は、`shopping_cart` Liquid タグを使用してHTML ブロックを追加し、製品をメールに追加する方法を示しています。 

{% raw %}
```java
<table style="width:100%">
  {% shopping_cart {{context.${cart_id}}} :abort_if_not_abandoned false %}
  {% for item in shopping_cart.products %}
  {% catalog_items <add_your_catalog_name> {{item.variant_id}} %}
  <tr>
    <th><img src="{{ items[0].variant_image_url }}" width="200" height="200"><img></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{ item.product_name }}</li>
        <li>Price: ${{ item.price }}</li>
        <li>Quantity: ${{ item.quantity }}</li>
        <li>Variant ID: {{ item.variant_id }}</li>
        <li>Product URL:{{ item.product_url }}</li>
        <li>SKU: {{ item.metadata.sku }}</li>
      </ul>
    </th>
    {% endfor %}
</table>
```
{% endraw %}

#### チェックアウトURL

{% raw %}
```liquid
{{context.${metadata}.checkout_url}}
```
{% endraw %}

## 注文確認とフィードバック調査

**注文確認&フィードバック 調査**テンプレートを使用して、注文の成功を確認し、顧客がアクションを満たすようにします。

![アプリは"Order confirm"Canvas テンプレートは、expanded "Entry Rules"です。]({% image_buster /assets/img_archive/order_confirmation_feedback.png %})

### 設定

キャンバスページで、**キャンバステンプレートを使用**>**Braze テンプレートs**を選択し、**オーダーコンファメーション&フィードバック 調査**をアプリします。 

#### デフォルト設定

キャンバスでは、次の設定が事前に行われています。

- 基本情報 
    - キャンバス名:**注文確認とフィードバック調査**
    - 変換イベント: `ecommerce.session_start`
        - コンバージョンの期限:10日間 
- エントリスケジュール 
    - ユーザが`ecommerce.cart_updated` イベントを実行したときのアクションベースのトリガ
    - 開始時刻は、キャンバステンプレートを作成するときです<br><br>!["アクションベースのオプションとクォート;キャンバス用。]({% image_buster /assets/img/ecommerce/feedback_entry.png %})<br><br>
- ターゲットオーディエンス 
    - エントリオーディエンス 
        - これらのアプリを**1回以上**使用したことがある 
        - メールが**空白ではない**
    - 入力コントロール
        - ユーザーのキャンバスへのエントリが即時に可能になります。
    - 終了条件 
        - 該当しない<br><br>![キャンバスの追加フィルターsとエントリ コントロールs。]({% image_buster /assets/img/ecommerce/feedback_entry_exit.png %})<br><br>
- 送信設定 
    - 登録済みまたはオプトイン済みのユーザー 
- メッセージステップ 
    - Liquid のテンプレート作成の例を使用して、メールテンプレートと HTML ブロックを確認し、あらかじめ用意されているテンプレートでメッセージに製品を追加します。独自のメールテンプレートを使用する場合は、次のセクションに示すように、[液体変数](#message-personalization) を参照することもできます。

### メール向けの注文の確認のパーソナライゼーション

ここでは、注文後に注文確認にHTML 製品ブロックを追加する方法の例を示します。

{% raw %}
```json
<table style="width:100%">
  {% for item in {{context.${products}}} %}
  {% catalog_items <add_your_catalog_name> {{item.variant_id}} %}
  <tr>
    <th><img src="{{ items[0].variant_image_url }}" width="200" height="200" /></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{item.product_name}}</li>
        <li>Price: {{item.price}}</li>
        <li>Quantity: {{item.quantity}}</li>
      </ul>
    </th>
  </tr>
  {% endfor %}
</table>
```
{% endraw %}

#### 注文状況 URL

{% raw %}
```liquid
{{context.${metadata}.order_status_url}}
```
{% endraw %}

## メッセージのパーソナライズ

[Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) は、Braze が使用する強力なテンプレート言語で、お客様のために動的でパーソナライズされたコンテンツを作成できます。Liquidタグを使用することで、顧客データ、製品情報、その他の変数に基づいてメッセージをカスタマイズすることができ、ショッピング体験や運転エンゲージメントを向上させることができます。

### Liquidの主な特徴

- **ダイナミックコンテンツ:**名前、注文の詳細、設定などの顧客固有の情報をメッセージに挿入します。
- **条件付きロジック:**if/else 文を使用して、特定の条件(顧客の場所や購入履歴など) に基づいて異なるコンテンツを表示します。
- **ループ:**製品または顧客データのコレクションを反復処理して、アイテムのリストまたはグリッドを表示します。

### Liquid を使い始める

Liquid タグを使用してメッセージのパーソナライズを開始するには、次のリソースを参照します。

- 事前定義の Liquid タグを使用した [Shopify データ]({{site.baseurl}}/shopify_features/#shopify-data)参照
- [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)

## セグメンテーション

Braze セグメントを使用して、特定の属性と動作に基づいてターゲットを絞った顧客セグメントを作成し、カスタマイズされたメッセージングとキャンペーンを提供します。この強力な機能により、適切なタイミングで適切なメッセージを使って適切なオーディエンスにリーチし、顧客に効果的にエンゲージできます。

セグメントの使用開始の詳細については、「[Braze のセグメントについて]({{site.baseurl}}/user_guide/engagement_tools/segments#about-braze-segments)」を参照してください。

### 推奨イベント

e コマースイベントは、[推奨イベント]({{site.baseurl}}/recommended_events/)に基づいています。
推奨されるイベントはオピニオン化されたカスタムイベントであるため、[カスタムイベントフィルタ]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#segmentation-filters)を選択することで、推奨されるeCommerceイベント名を検索できます。

### eコマースのフィルター

**Ecommerce Source** および**Total Revenue** などのeCommerce フィルタを使用して、セグメンテータ内の**Ecommerce** セクションに移動して、ユーザをeCommerce フィルタでセグメント化します。

![セグメントフィルターは"Ecommerce"フィルター sでドロップダウンします。]({% image_buster /assets/img_archive/ecommerce_filters.png %}){: style="max-width:80%"}

{% alert important %}
購入イベントは最終的に非推奨になり、[eCommerce 推奨イベント]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/) に置き換えられます。この置き換えが行われると、セグメントフィルターでは、購入動作でデータが入力されることがなくなります。購入イベントの完全なリストについては、[購入イベントの記録]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/#logging-purchase-events)を参照してください。
{% endalert %}

## ネストされたイベントプロパティ

階層化イベントプロパティでセグメンテーションを行うには、[セグメントエクステンション]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#why-use-segment-extensions)を利用できます。たとえば、Segment Extensions を使用して、製品「SKU-123」を過去90 日間に購入したユーザーを検索できます。

## 分析

{% alert note %}
現時点では、Shopify 統合は、Braze [購入イベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events#purchase-events) の入力をサポートしていません。そのため、購入フィルターs、液体タグs、アクションベースのトリガーed、および分析はecommerce.order_placedイベントを使用する必要があります。
{% endalert %}

統合でサポートされているイベントを誰が実行したかに基づいて[カスタムイベントレポート]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#analytics) を作成するには、特定の[イベント名]({{site.baseurl}}/shopify_data_features/) を指定します。

開始したキャンバスからの注文に関連するトレンドを把握するには、[コンバージョンダッシュボード]({{site.baseurl}}/user_guide/data_and_analytics/analytics/conversions_dashboard#conversions-dashboard)を設定し、キャンバスを指定する必要があります。

より高度なレポートユースケースでは、Braze [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/)を使用してカスタムレポートを生成できます。 

