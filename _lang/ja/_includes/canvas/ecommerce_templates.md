{% tabs %}
{% tab Abandoned browse %}

### 閲覧の放棄

製品を閲覧したが、カートへの追加や注文を行わなかったユーザーにエンゲージするには、**閲覧の放棄**テンプレートを使用します。

![アプリはlied & quot;Abandoned Browse" Canvas テンプレートはexpanded & quot;Entry Rules"です。]({% image_buster /assets/img_archive/abandoned_browse.png %})

#### 設定

キャンバスページで [**キャンバステンプレートを使用**] > [**Braze テンプレート**] を選択し、**閲覧の放棄**テンプレートを適用します。 

##### デフォルト設定

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
        - `ecommerce.cart_updated`、`ecommerce.checkout_started`、または `ecommerce.order_placed` を実行する<br><br>![キャンバスのエントリーコントロールs と終了基準。]({% image_buster /assets/img/ecommerce/abandoned_browse_entry_exit.png %})<br><br> 
- 送信設定 
    - 登録済みまたはオプトイン済みのユーザー 
- 遅延ステップ
    - 1時間遅延
- メッセージステップ 
    - Liquid のテンプレート作成の例を使用して、メールテンプレートと HTML ブロックを確認し、あらかじめ用意されているテンプレートでメッセージに製品を追加します。独自のメールテンプレートを使用する場合は、次のセクションに示すように、[液体変数](#message-personalization) を参照することもできます。

#### メール向けの閲覧の放棄の製品パーソナライゼーション 

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

##### 製品URL

{% raw %}
```liquid
{{context.${product_url}}}
```
{% endraw %}    

{% endtab %}
{% tab Abandoned cart %}

### カート放棄

カートに製品を追加したが、購入手続きまたは注文に進まなかった顧客からの潜在的な売上の損失に対応するには、**カート放棄**テンプレートを使用します。 

![アプリはlied & quot;Abandoned Cart" Canvas テンプレート はexpanded & quot;Entry Rules"です。]({% image_buster /assets/img_archive/abandoned_cart.png %})

#### 設定

キャンバスページで [**キャンバステンプレートを使用**] > [**Braze テンプレート**] を選択し、**カート放棄**テンプレートを適用します。 

##### デフォルト設定

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
        - `ecommerce.cart_updated`、`ecommerce.checkout_started`、または `ecommerce.order_placed` を実行する<br><br>![キャンバスのエントリーコントロールs と終了基準。]({% image_buster /assets/img/ecommerce/abandoned_cart_entry_exit.png %})<br><br> 
- 送信設定 
    - 登録済みまたはオプトイン済みのユーザー 
- 遅延ステップ
     - 4時間遅延
- メッセージステップ 
    - Liquid のテンプレート作成の例を使用して、メールテンプレートと HTML ブロックを確認し、あらかじめ用意されているテンプレートでメッセージに製品を追加します。独自のメールテンプレートを使用する場合は、次のセクションに示すように、[液体変数](#message-personalization) を参照することもできます。

#### 放棄カート or カート放棄再エントリロジックの動作

ユーザーがチェックアウト処理を開始すると、そのカートは`checkout_started` としてマークされます。その時点以降、同じカートIDを持つカート更新sは、放棄カート or カート放棄 ユーザーの行程に再び入るユーザーにはなりません。

1. ユーザーがアイテムをカートに追加すると、キャンバスに入ります。
2. 項目を追加または更新するたびに、キャンバスに再入力されます。これにより、カートデータとメッセージングが最新の状態に保たれます。
3. ユーザーがチェックアウト処理を開始すると、カートは`checkout_started` とタグされ、キャンバスを終了します。
4. 同じカートIDを使用する将来のカート更新は、このカートがすでにチェックアウトタグeに移動しているため、再エントリをトリガーしません。

ユーザーがチェックアウトユーザーの行程に移動すると、代わりに[放棄されたチェックアウトキャンバス](#abandoned-checkout)がターゲットになります。これは、購買行程でさらにsをユーザーするように設計されています。

#### メール向けのカート放棄の製品パーソナライゼーション {#abandoned-cart-checkout}

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

##### HTML カート URL

ユーザーをカートに戻すには、次のようにメタデータオブジェクトの下にネストされたイベントプロパティを追加します。

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

{% endtab %}
{% tab Abandoned checkout %}

### 購入手続き放棄

**購入手続き放棄**テンプレートを使用して、購入手続きプロセスを開始したが発注前に離脱した顧客をターゲットにします。 

![アプリはlied & quot;Abandoned Checkout" Canvas テンプレートはexpanded & quot;Entry Rules"です。]({% image_buster /assets/img_archive/abandoned_checkout.png %})

#### 設定

キャンバスページで [**キャンバステンプレートを使用**] > [**Braze テンプレート**] を選択し、**購入手続き放棄**テンプレートを適用します。 

##### デフォルト設定

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
            - `ecommerce.order_placed` イベントを実行します<br><br>![キャンバスのエントリーコントロールs と終了基準。]({% image_buster /assets/img/ecommerce/abandoned_checkout_entry_exit.png %})<br><br>
- 送信設定 
    - 登録済みまたはオプトイン済みのユーザー 
- 遅延ステップ
    - 4時間遅延
- メッセージステップ 
    - Liquid のテンプレート作成の例を使用して、メールテンプレートと HTML ブロックを確認し、あらかじめ用意されているテンプレートでメッセージに製品を追加します。独自のメールテンプレートを使用する場合は、次のセクションに示すように、[液体変数](#message-personalization) を参照することもできます。

#### メール向けの購入手続き放棄の製品パーソナライゼーション

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

##### チェックアウトURL

{% raw %}
```liquid
{{context.${metadata}.checkout_url}}
```
{% endraw %}

{% endtab %}
{% tab Order confirmation and feedback survey %}

### 注文確認とフィードバック調査

**注文確認&フィードバック 調査**テンプレートを使用して、注文の成功を確認し、顧客がアクションを満たすようにします。

![アプリは"Order confirm"Canvas テンプレートは"Entry Rules"と展開されています。]({% image_buster /assets/img_archive/order_confirmation_feedback.png %})

#### 設定

キャンバスページで、**キャンバステンプレートを使用**>**Braze テンプレートs**を選択し、**オーダーコンファメーション&フィードバック 調査**をアプリします。 

##### デフォルト設定

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
        - 該当しない<br><br>![キャンバスの追加フィルターs およびエントリ コントロールs。]({% image_buster /assets/img/ecommerce/feedback_entry_exit.png %})<br><br>
- 送信設定 
    - 登録済みまたはオプトイン済みのユーザー 
- メッセージステップ 
    - Liquid のテンプレート作成の例を使用して、メールテンプレートと HTML ブロックを確認し、あらかじめ用意されているテンプレートでメッセージに製品を追加します。独自のメールテンプレートを使用する場合は、次のセクションに示すように、[液体変数](#message-personalization) を参照することもできます。

#### メール向けの注文の確認のパーソナライゼーション

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

##### 注文状況 URL

{% raw %}
```liquid
{{context.${metadata}.order_status_url}}
```
{% endraw %}

{% endtab %}
{% endtabs %}