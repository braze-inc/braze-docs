---
nav_title: eコマース利用事例
article_title: eコマース利用事例
alias: /ecommerce_use_cases/
page_order: 4
description: "このリファレンス記事では、eコマース・マーケター向けに特別にカスタマイズされた、いくつかのあらかじめ構築されたBrazeテンプレートを取り上げ、必須戦略の実行を容易にします。"
toc_headers: h2
---

# eコマースのユースケース

> Braze Canvas には、eCommerce マーケター専用にあらかじめ作成されたテンプレートがいくつか用意されています。これにより、必須戦略の実装が容易になります。このページには、カスタマージャーニーを強化するために使用できるいくつかの主要なテンプレートが用意されています。

{% alert note %}
ろう付けは、データ計画に時間がかかることを認識します。私たちは、お客様に開発チームを熟知してもらい、今すぐeコマースイベントの送付を始めることを奨励しています。eコマースのおすすめイベントではすぐに利用できない機能もありますが、2025年を通して新しい製品が導入され、あなたのeコマース機能が強化されるのを楽しみにしています。
{% endalert %}

## キャンバステンプレートの使用

キャンバステンプレートを使用するには:
1. [**メッセージング**] > [**キャンバス**] に進みます。
2. **Create Canvas**> **Use a Canvas Template**を選択します。
3. 使用するテンプレートの**ろう付けテンプレート**タブを参照します。テンプレートの名前を選択すると、テンプレートをプレビューできます。
4. 使用するテンプレートの**Apply Template**を選択します。<br><br>![" Canvas templates" " Page opened to " Braze templates" タブと、最近使用したテンプレートと選択可能なBraze テンプレートのリストが表示されます。][2]{: style="max-width:80%;"}

## eコマーステンプレート

- [ブラウズ放棄](#abandoned-browse)
- [カート放棄](#abandoned-cart)
- [購入手続き放棄](#abandoned-checkout)
- [注文確認・フィードバック調査](#order-confirmation--feedback-survey)

## ブラウズ放棄

**放棄されたブラウズ**テンプレートを使用して、製品をブラウズしたが、カートに追加したり注文したりしなかったユーザーをエンゲージします。

![適用された"Abandoned Browse"拡張された"Entry Rules"を含むキャンバステンプレート。][3]

### セットアップ

キャンバスページで、**キャンバステンプレートを使用** > **ブレーズテンプレート**を選択し、**放棄ブラウズ**テンプレートを適用します。 

#### デフォルト設定

キャンバスでは、次の設定が事前に設定されています。
- 基本情報 
    - キャンバス名:**ブラウズ放棄**
    - 変換イベント: `ecommerce.order placed`
        - 変換期限:3日間 
- エントリスケジュール 
    - ユーザが`ecommerce.product_viewed` イベントを実行したときのアクションベース
    - 開始時刻は、キャンバステンプレートを作成するときです<br><br>!["Action Based Options" for the Canvas.]({% image_buster /assets/img/ecommerce/abandoned_browse_entry.png %})<br><br> 
- ターゲットオーディエンス 
    - エントリオーディエンス 
        - メール**が空白ではありません**
        - また、ビジネスニーズを満たすようにエントリオーディエンス基準を変更することもできます
    - 入力コントロール
        - ユーザは、キャンバスの完全な継続時間が完了した後、このキャンバスに再び入る資格があります
    - 終了条件 
        - `ecommerce.cart_updated`、`ecommerce.checkout started`、または `ecommerce.order_placed`<br><br>![Canvas.]({% image_buster /assets/img/ecommerce/abandoned_browse_entry_exit.png %})のエントリコントロールと終了条件<br><br> 
- 送信設定 
    - 登録または選択されているユーザー 
- 遅延ステップ
    - 1時間遅れ
- メッセージステップ 
    - Liquid templating の例を使用して、メールテンプレートとHTML ブロックを確認し、あらかじめ構築されたテンプレートでメッセージに製品を追加します。独自のメールテンプレートを使用する場合は、次のセクションに示すように、[液体変数](#message-personalization) を参照することもできます。

### 電子メール用ブラウズ製品のパーソナライズを放棄 

ここでは、放棄されたブラウズメールのHTML 製品ブロックを追加する方法の例を示します。 

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

**放棄されたカート**テンプレートを使用して、カートに製品を追加したが、チェックアウトや注文を継続しなかった顧客からの潜在的な売上の損失をカバーします。 

![適用された"放棄されたCart"拡張された"Entry Rules"を含むキャンバステンプレート。][4]

### セットアップ

キャンバスページで、**キャンバステンプレートを使用**> **ブライズテンプレート**を選択し、**放棄されたカート**テンプレートを適用します。 

#### デフォルト設定

キャンバスでは、次の設定が事前に設定されています。
- 基本情報 
    - キャンバス名:**カート放棄**
    - 変換イベント: `ecommerce.order_placed`
        - 変換期限:3日間 
- エントリスケジュール 
    - ユーザが**カート更新イベントを実行**をトリガしたときのアクションベースのトリガ(ドロップダウンにあります)
    - 開始時刻は、キャンバステンプレートを作成するときです<br><br>!["Action Based Options" for the Canvas.]({% image_buster /assets/img/ecommerce/abandoned_cart_entry.png %})<br><br> 
- ターゲットオーディエンス 
    - エントリオーディエンス 
        - これらのアプリを使用したことがある**0**回以上 
        - メール**が空白ではありません**
    - 入力コントロール
        - ユーザは、すぐにキャンバスのエントリに再適用されます
    - 終了条件 
        - `ecommerce.cart_updated`、`ecommerce.checkout_started`、または `ecommerce.order_placed`<br><br>![Canvas.]({% image_buster /assets/img/ecommerce/abandoned_cart_entry_exit.png %})のエントリコントロールと終了条件<br><br> 
- 送信設定 
    - 登録または選択されているユーザー 
- 遅延ステップ
     - 4時間遅れ
- メッセージステップ 
    - Liquid templating の例を使用して、メールテンプレートとHTML ブロックを確認し、あらかじめ構築されたテンプレートでメッセージに製品を追加します。独自のメールテンプレートを使用する場合は、次のセクションに示すように、[液体変数](#message-personalization) を参照することもできます。

### 放棄されたカート製品の電子メールのパーソナライズ {#abandoned-cart-checkout}

放棄されたカートユーザージャーニーには、製品のパーソナライズに特別な`shopping_cart` 液体タグが必要です。 

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

#### HTMLカートURL

ユーザをカートに戻す場合は、medata オブジェクトの下に次のようなネストされたイベントプロパティを追加できます。

{% raw %}
```liquid
{{context.${metadata}.cart_url}}
```
{% endraw %}

Shopifyを使用する場合は、次のLiquidテンプレートを使用してカートURLを作成します。

{% raw %}
```liquid
{{context.source}}/checkouts/cn/{{context.cart_id}}
```
{% endraw %}

## 購入手続き放棄

**放棄されたチェックアウト**テンプレートを使用して、チェックアウトプロセスを開始したが発注前に残された顧客をターゲットにします。 

![適用された"放棄されたチェックアウト&クォート;拡張された&クォートを含むキャンバステンプレート;エントリルール&クォート;][5]

### セットアップ

キャンバスページで、**キャンバステンプレートを使用**> **ブレーズテンプレート**を選択し、**放棄されたチェックアウト**テンプレートを適用します。 

#### デフォルト設定

キャンバスでは、次の設定が事前に設定されています。

- 基本情報 
    - キャンバス名:**購入手続き放棄**
    - 変換イベント: `ecommerce.order_placed`
        - 変換期限:3日間 
- エントリスケジュール 
    - ユーザが`ecommerce.checkout_started` イベントを実行したときのアクションベースのトリガ
    - 開始時刻は、キャンバステンプレートを作成するときです<br><br>!["Action Based Options" for the Canvas.]({% image_buster /assets/img/ecommerce/abandoned_checkout_entry.png %})
- ターゲットオーディエンス 
    - エントリオーディエンス 
        - これらのアプリを使用したことがある**0**回以上 
        - メール**が空白ではありません**
    - 入力コントロール
        - ユーザは、すぐにキャンバスのエントリに再適用されます
        - 終了条件 
            - `ecommerce.order_placed` イベントを実行します<br><br>![Canvas.]({% image_buster /assets/img/ecommerce/abandoned_checkout_entry_exit.png %})のエントリコントロールと終了条件<br><br>
- 送信設定 
    - 登録または選択されているユーザー 
- 遅延ステップ
    - 4時間遅れ
- メッセージステップ 
    - Liquid templating の例を使用して、メールテンプレートとHTML ブロックを確認し、あらかじめ構築されたテンプレートでメッセージに製品を追加します。独自のメールテンプレートを使用する場合は、次のセクションに示すように、[液体変数](#message-personalization) を参照することもできます。

### 電子メール用のチェックアウトパーソナライゼーションを放棄

放棄されたチェックアウトユーザージャーニーには、製品のパーソナライゼーションのために特別な`shopping_cart` 液体タグが必要です。 

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

## 注文確認・フィードバック調査

**注文確認&アンプ;フィードバック調査**テンプレートを使用して、注文の成功を確認し、顧客満足度を高める。

![適用された"注文確認"拡張された"Entry Rules"を含むキャンバステンプレート。][6]

### セットアップ

キャンバスページで、**キャンバステンプレートを使用**> **ブレーズテンプレート**を選択し、**注文確認&アンプ;フィードバック調査**テンプレートを適用します。 

#### デフォルト設定

キャンバスでは、次の設定が事前に設定されています。

- 基本情報 
    - キャンバス名:**フィードバック調査による注文確認**
    - 変換イベント: `ecommerce.session_start`
        - 変換期限:10日間 
- エントリスケジュール 
    - ユーザが`ecommerce.cart_updated` イベントを実行したときのアクションベースのトリガ
    - 開始時刻は、キャンバステンプレートを作成するときです<br><br>!["Action Based Options" for the Canvas.]({% image_buster /assets/img/ecommerce/feedback_entry.png %})<br><br>
- ターゲットオーディエンス 
    - エントリオーディエンス 
        - これらのアプリを使用したことがある**0**回以上 
        - メール**が空白ではありません**
    - 入力コントロール
        - ユーザは、すぐにキャンバスのエントリに再適用されます
    - 終了条件 
        - 該当しない<br><br>![Canvas.]({% image_buster /assets/img/ecommerce/feedback_entry_exit.png %})の追加のフィルタと入力コントロール<br><br>
- 送信設定 
    - 登録または選択されているユーザー 
- メッセージステップ 
    - Liquid templating の例を使用して、メールテンプレートとHTML ブロックを確認し、あらかじめ構築されたテンプレートでメッセージに製品を追加します。独自のメールテンプレートを使用する場合は、次のセクションに示すように、[液体変数](#message-personalization) を参照することもできます。

### メールのオーダー確認パーソナライズ

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

#### 注文状況URL

{% raw %}
```liquid
{{context.${metadata}.order_status_url}}
```
{% endraw %}

## メッセージのパーソナライズ

[Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) は、Braze が使用する強力なテンプレート言語で、お客様のために動的でパーソナライズされたコンテンツを作成できます。Liquidタグを使用することで、顧客データ、製品情報、その他の変数に基づいてメッセージをカスタマイズすることができ、ショッピング体験や運転エンゲージメントを向上させることができます。

### Liquidの主な特徴

- **動的コンテンツ:**名前、注文の詳細、設定などの顧客固有の情報をメッセージに挿入します。
- **条件付きロジック:**if/else 文を使用して、特定の条件(顧客の場所や購入履歴など) に基づいて異なるコンテンツを表示します。
- **ループ:**製品または顧客データのコレクションを反復処理して、リストまたはアイテムのグリッドを表示します。

### Liquid の使用開始

Liquid タグを使用してメッセージのパーソナライズを開始するには、次のリソースを参照します。

- [定義済みの液体タグを含むShopifyデータ]({{site.baseurl}}/shopify_features/#shopify-data)参照
- [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)

## セグメンテーション

Braze セグメントを使用して、特定の属性と動作に基づいてターゲットを絞った顧客セグメントを作成し、カスタマイズされたメッセージングとキャンペーンを提供します。このパワフルな機能を使えば、適切な時間に適切なメッセージで適切な視聴者に到達することで、効果的に顧客を引きつけることができます。

セグメントの使用開始の詳細については、[ブレーズセグメントについて]({{site.baseurl}}/user_guide/engagement_tools/segments#about-braze-segments)を参照してください。

### おすすめイベント

eコマースイベントは、[推奨イベント]({{site.baseurl}}/recommended_events/)に基づきます。
推奨されるイベントはオピニオン化されたカスタムイベントであるため、[カスタムイベントフィルタ]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#segmentation-filters)を選択することで、推奨されるeCommerceイベント名を検索できます。

## ネストされたイベントプロパティ

ネストされたイベントプロパティでセグメント化するには、[Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#why-use-segment-extensions) を利用できます。たとえば、Segment Extensions を使用して、製品「SKU-123」を過去90 日間に購入したユーザーを検索できます。

## 分析

{% alert note %}
現時点では、Shopify 統合は、Braze [購入イベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events#purchase-events) の入力をサポートしていません。その結果、購入フィルタ、Liquid タグ、アクションベースのトリガ、およびアナリティクスでは、ecommerce.order_placed イベントを使用する必要があります。
{% endalert %}

統合でサポートされているイベントを誰が実行したかに基づいて[カスタムイベントレポート]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#analytics) を作成するには、特定の[イベント名]({{site.baseurl}}/shopify_data_features/) を指定します。

起動したキャンバスからの注文に関連するトレンドを把握するには、[Conversions Dashboard]({{site.baseurl}}/user_guide/data_and_analytics/analytics/conversions_dashboard#conversions-dashboard)を設定し、キャンバスを指定する必要があります。

より高度なレポートユースケースでは、Braze [Query Builder]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/)を使用してカスタムレポートを生成できます。 

[2]: {% image_buster /assets/img_archive/apply_template.png %}
[3]: {% image_buster /assets/img_archive/abandoned_browse.png %}
[4]: {% image_buster /assets/img_archive/abandoned_cart.png %}
[5]: {% image_buster /assets/img_archive/abandoned_checkout.png %}
[6]: {% image_buster /assets/img_archive/order_confirmation_feedback.png %}