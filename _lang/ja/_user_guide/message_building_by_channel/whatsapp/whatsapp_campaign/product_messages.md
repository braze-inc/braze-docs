---
nav_title: 製品メッセージ
article_title: 製品メッセージ
page_order: 2
page_order: 2
description: "このページでは、WhatsApp 製品メッセージを使用して、メタカタログから製品を表示するインタラクティブなWhatsApp メッセージを送信する方法について説明します。"
page_type: reference
alias: "/whatsapp_product_messages/"
tool:
 - Campaigns
channel:
 - WhatsApp
---

# 製品メッセージ

> 製品メッセージを使用すると、Meta カタログから直接製品を表示するインタラクティブな WhatsApp メッセージを送信できます。

ユーザーにWhatsApp 製品メッセージを送信すると、ユーザーは次のカスタマージャーニーに進みます。

1. ユーザーは、WhatsApp で製品またはカタログメッセージを受け取ります。
2. ユーザーは WhatsApp から直接製品をカートに追加します。
3. ユーザーは WhatsApp で [**Place order**] をタップします。
4. ウェブサイトまたはアプリは、Braze からカートデータを受信し、チェックアウトリンクを生成します。
5. ユーザーは、ウェブサイトまたはアプリのチェックアウトを完了するように指示されます。

ユーザーがカタログメッセージを介してカートにアイテムを追加すると、Braze はフォローアップアクションのためのWebhook データを受け取ります。

## 要件

| 要件 | 説明 |
| --- | --- |
| WhatsApp Business アカウント | WhatsApp 製品メッセージを使用するには、WhatsApp Business Account をBraze に接続している必要があります。 |
| メタカタログ | Commerce Manager でMeta カタログを設定する必要があります。 |
| 利用規約の遵守 | [Meta Commerce Terms and Policies](https://www.facebook.com/policies_center/commerce) を遵守します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 製品メッセージタイプ

{% alert note %}
[製品メッセージのセットアップ](#setting-up-product-messages)のステップ 4時にアクセスされる統合製品セレクターを使用して、製品メッセージエクスペリエンスを強化します。
{% endalert %}
## 製品メッセージタイプ

{% alert note %}
[製品メッセージのセットアップ](#setting-up-product-messages)のステップ 4時にアクセスされる統合製品セレクターを使用して、製品メッセージエクスペリエンスを強化します。
{% endalert %}

{% tabs local %}
{% tab Catalog messages %}

カタログメッセージには、製品カタログ全体が対話形式で表示されます。[テンプレートとレスポンスメッセージ](#building-a-product-message)として利用できます。

[setup](#setting-up-product-messages) 中にBrazeするカタログ権限を有効にした場合、ユーザーs に表示するサムネールを選択できます。 
カタログメッセージには、製品カタログ全体が対話形式で表示されます。[テンプレートとレスポンスメッセージ](#building-a-product-message)として利用できます。

[setup](#setting-up-product-messages) 中にBrazeするカタログ権限を有効にした場合、ユーザーs に表示するサムネールを選択できます。 

{% alert note %}
カタログ接続は Meta によって管理され、製品カタログに継承されるため、Braze で追加の製品選択を行う必要はありません。
{% endalert %}


{% endtab %}
{% tab Multi-product messages %}

複数製品メッセージでは、カタログ内の特定の製品が強調表示されます。メッセージあたり最大30個の項目が強調表示されます。[テンプレートとレスポンスメッセージ](#building-a-product-message)として利用できます。

ID を使用して製品を手動で選択するか、[setup](#setting-up-product-messages) 中にカタログ権限を有効にした場合は、ドロップダウン製品セレクターを使用します。
ID を使用して製品を手動で選択するか、[setup](#setting-up-product-messages) 中にカタログ権限を有効にした場合は、ドロップダウン製品セレクターを使用します。

{% alert important %}
Meta で複数製品メッセージテンプレートを使用する際のヘッダーの表示に関する既知の問題があります。Meta はこの問題を認識しており、修正に取り組んでいます。
{% endalert %}

{% endtab %}
{% tab Single product %}

単一の製品メッセージでは、製品カタログの特定の製品が強調表示されます。[response messages](#building-a-product-message)として利用できます。

ID を使用して製品を手動で選択するか、[setup](#setting-up-product-messages) 中にカタログ権限を有効にした場合は、ドロップダウン製品セレクターを使用します。

{% endtab %}
{% endtabs %}

## 製品メッセージのセットアップ

1. [Meta Commerce Manager](https://business.facebook.com/business/loginpage/?next=https%3A%2F%2Fbusiness.facebook.com%2Fcommerce_manager%2F#) で、[Meta の指示](https://www.facebook.com/business/help/1275400645914358?id=725943027795860&ref=search_new_1) に従ってMeta カタログを作成します。Braze 接続のWhatsApp Business Accont が存在するのと同じMeta Business Portfolio にいることを確認します。
2. Meta の指示に従って、[ Meta Business Manager で"Manage Catalog" パーミッションを割り当てて、Meta カタログ](https://www.facebook.com/business/help/1953352334878186?id=2042840805783715) をBraze に接続されたWhatsApp ビジネスアカウントに接続します。 

![Meta " カタログ s" " " Assign partner" "sweeney_catalog".]({% image_buster /assets/img/whatsapp/meta_catalog.png %}){: style="max-width:90%;"}

必ず、Braze Business Manager ID `332231937299182` をパートナーのビジネスID として使用してください。

![パートナーの取引先ID を入力し、権限&割当て;カタログ&割当ての管理;を割り当てるためのフィールドs を含むパートナーとカタログを共有するウィンドウ。]({% image_buster /assets/img/whatsapp/share_meta_catalog.png %}){: style="max-width:70%;"}

{: start="3"}
3\.メタカタログ設定を選択します。カタログメッセージを送信するには、**チャットヘッダーのカタログアイコンを表示**を選択する必要があります。

![WhatsAppマネージャ設定の"Catalog_products" カタログのs ページ。]({% image_buster /assets/img/whatsapp/meta_catalog_settings.png %}){: style="max-width:90%;"}

{: start="4"}
4\.Braze では、[埋め込みサインアップ]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/) プロセスを実行して権限を付与します。必ず、**all**に権限を付与するカタログを選択してください。これにより、Braze 連携製品セレクターが利用可能になります。

![5つのカタログが選択されたウィンドウでは、権限が提供されます。]({% image_buster /assets/img/whatsapp/select_catalogs.png %}){: style="max-width:50%;"}

{% alert tip %}
メタカタログを作成する際のベストプラクティスについては、[Commerce Manager で高品質なカタログを作成するためのヒント](https://www.facebook.com/business/help/2086567618225367?id=725943027795860)を参照してください。
{% endalert %}

## 製品メッセージの作成

WhatsApp テンプレートメッセージまたはレスポンスメッセージを使用して、製品メッセージを作成できます。

{% tabs local %}
{% tab WhatsApp message template %}

1. Meta Business マネージャーで [**Message Templates**] に移動します。
2. フォーマットとして [**Catalog**] を選択し、[**Catalog message**] (カタログ全体を表示) または [**Multi-product catalog message**] (特定の項目を強調表示) を選択します。
3. Braze で WhatsApp キャンペーンまたはキャンバスメッセージステップを作成します。
4. テンプレートを送信した場所に一致するサブスクリプショングループを選択します。
5. [**WhatsApp テンプレートメッセージ**] を選択します。
5. [**WhatsApp テンプレートメッセージ**] を選択します。
6. 使用するテンプレートを選択します。
    - 複数製品テンプレートを選択した場合は、強調表示する製品のセクションタイトルとコンテンツID を指定します。Meta Commerce Manager からコンテンツID を直接コピーするか、統合製品セレクタの権限を有効にした場合は、アイテムを選択します。

![項目一覧フィールドsで、項目名と内容IDを入力します。]({% image_buster /assets/img/whatsapp/multi_product_template.png %}){: style="max-width:60%;"}

![選択する項目のドロップダウンを含む項目リスト。]({% image_buster /assets/img/whatsapp/content_id_items.png %}){: style="max-width:60%;"}

{: start="7"}
7. メッセージの作成を続行します。

{% endtab %}
{% tab Response message %}

1. Braze で WhatsApp キャンペーンまたはキャンバスメッセージステップを作成します。
2. サブスクリプショングループを選択する。
3. **レスポンスメッセージ**を選択します。
4. **Meta Product Messages**を選択します。

![メッセージタイプとレスポンスメッセージレイアウトを選択するためのオプション。"Response Message"および"Meta Product Messages"を強調表示します。]({% image_buster /assets/img/whatsapp/response_message_layouts.png %}){: style="max-width:90%;"}

{: start="5"}
5. 使用する[メッセージタイプ](#product-message-types)を選択します。

!["Multi-product"のMesageレイアウト選択。]({% image_buster /assets/img/whatsapp/multi-product_message_layout.png %}){: style="max-width:90%;"}

{: start="6"}
6. メッセージの作成を続行します。

![例:製品の情報が記入されたメタ製品メッセージ。]({% image_buster /assets/img/whatsapp/example_response_message.png %}){: style="max-width:90%;"}

{% endtab %}
{% endtabs %}

## 製品の管理

### Commerce Manager へのアクセス

Meta Business Manager で、**Commerce Manager**に移動し、組織を選択します。ここでは、以下のようなカタログアセットを管理できます。
- 新しいカタログの作成
- 既存のカタログへの製品の追加
- 製品情報の更新
- 提供終了項目の削除

{% alert important %}
カタログから参照されている製品を削除すると、関連するメッセージの送信に失敗します。
{% endalert %}

## インバウンド製品の質問の受信 

ユーザは、製品に関する質問に応答したり、製品に関するカタログを送信したりできます。これらは受信メッセージとして到着し、[Action Path]({{site.baseurl}}/action_paths/) でソートできます。 

さらに、Brazeはこれらの質問から製品IDとカタログ IDを抽出します。そのため、回答を自動化したり、他のチーム(顧客サポートなど)に質問を送信したりする場合は、それらの詳細を含めることができます。たとえば、`inbound_product_id` または`inbound_catalog_id` のWhatsAppプロパティーを使用して、レスポンスをパーソナライズできます。

!["パーソナライゼーション&quot を追加; パーソナライゼーション型が" WhatsApp Properties" とハイライトされた属性が"inbound_product_id".]({% image_buster /assets/img/whatsapp/inbound_product_questions.png %}){: style="max-width:60%;"}

## チェックアウト:カートの処理と Webhook

ユーザーがWhatsApp製品メッセージを操作すると、製品をブラウズしたり、製品をカートに追加したりできます。しかし、現在、発送情報や支払い処理のための組み込みのチェックアウト機能はありません。代わりに、独自のアプリまたはウェブサイト内にカートを作成し、カスタムリンクを使用してそのカートにユーザーを誘導することをお勧めします。

### 考慮事項

- **アプリ内チェックアウトがない:**ユーザーはWhatsApp内で直接購入を完了できません。すべてのトランザクションはウェブサイトまたはアプリにリダイレクトする必要があります。
- **カスタムリンクが必要:**ユーザーに対してプラットフォームのカートを表示するカスタムリンクを作成する必要があります。
- **手動での設定:**設定プロセスでは、カートとメッセージングワークフローを手動で設定する必要があります。

{% alert note %}
現在、WhatsAppで直接発生する支払いをサポートしておらず、今後のサポートは国別となります(現在、Metaはインド、ブラジル、シンガポールのユーザーに拠点を置いて直接働いている企業にのみ提供しています)。
{% endalert %}

### カートイベントトリガーの設定

顧客が WhatsApp で注文すると、Braze で自動的に次の処理が行われます。
1. WhatsApp(製品ID、数量、その他の注文データ)からカートコンテンツを受け取ります。
2. `source = whats_app` を含むすべての関連データを使用して `ecommerce.cart_update` e コマースイベントを作成します。
3. 応答をトリガーします。これにより、注文に応答する自動キャンペーンを設定できます。

`ecommerce.cart_update` e コマースイベントは、イベントの送信後にのみ Braze に表示されます。イベントを送信するには、Braze からテスト製品メッセージを生成し、カートイベントを送信します。
カートイベントには以下が含まれます。

- **カート ID:**カートの一意の識別子
- **製品:**製品ID、数量、価格が記載されている品目のリスト
- **総額:**すべての項目の合計
- **通貨:**カートの通貨
- **出典:**マーク "whats_app"
- **出典:**マーク "whats_app"
- **メタデータ:**カタログIDやメッセージテキストなどの追加データ

その他の Braze カートイベント情報は、「[e コマースの推奨イベントのタイプ]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events#types-of-ecommerce-recommended-events)」にあります。

### トリガー応答の設定

1. `ecommerce.cart_updated` のカスタムイベントトリガーを作成します。
2. `source = "whats_app"` のプロパティフィルタを追加します。

![`ecommerce.cart_updated` カスタムイベント トリガーのキャンバスステップ、基本プロパティは"source" equaling `whats_app`.]({% image_buster /assets/img/whatsapp/product_message_canvas_step.png %})

{: start="3"}
3\.カートデータに基づいてフォローアップアクションを設定します。

### 推奨されるチェックアウト実装 

{% tabs local %}
{% tab Simple Liquid-based cart links %}

Liquid を使用して、応答メッセージにカート URL を直接作成します。これは、WhatsAppとeCommerceプラットフォーム間で一貫した製品IDを持っている場合に最適です。

#### Liquid の例

{% raw %}
```liquid
{% assign cart_link = "http://alejandro-test-new.myshopify.com/cart/" %}
{% for product in event_properties.products %}
 {% assign variant_id = product.product_id %}
 {% assign quantity = product.quantity %}
 {% if forloop.first %}
   {% assign cart_link = cart_link | append: variant_id | append: ":" | append: quantity %}
 {% else %}
   {% assign cart_link = cart_link | append: "," | append: variant_id | append: ":" | append: quantity %}
 {% endif %}
{% endfor %}
{{ cart_link }}
```
{% endraw %}

#### 設定

1. `ecommerce.cart_update` eCommerce イベントのトリガを使用してWhatsApp 応答メッセージキャンペーンを作成します。
2. カート URL を使用して後続のメッセージを作成します。
3. Liquid を使用してカート URL を作成します。Shopify を使用する場合は、前の Liquid の例を使用して[カートのパーマリンクを作成](https://shopify.dev/docs/apps/build/checkout/create-cart-permalinks)できます。

![液体カートのチェックアウト体験ワークフローを示す図:Meta はオーダー受信メッセージをBraze に送信します。これはトリガー がアクション ベースのトリガーを送信し、カートリンクを含むメッセージを作成してWhatsApp メッセージを送信します。]({% image_buster /assets/img/whatsapp/liquid_generated_cart_link_checkout.png %})

{% endtab %}
{% tab Connected Content %}

e コマースシステムに対する API 呼び出しを実行し、パーソナライズされたチェックアウト URL を生成します。これは、ダイナミックなカート URL の生成または複雑な製品マッピングが必要な場合に最適です。

#### 設定

1. [`ecommerce.cart_update`]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events/?tab=ecommerce.cart_updated)eCommerceイベントによってトリガーされるWebhookキャンペーンまたはキャンバスステップを作成します。これにより、eCommerceシステムにカートデータが送信されます。
2. 同じ e コマースイベントによってトリガーされる WhatsApp キャンペーンまたはキャンバスねっセージステップを作成して、カート URL を含む WhatsApp 応答メッセージをユーザーに送信します。後続の応答メッセージの指示に従って[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content)を使用します。

![Connected Content コールのチェックアウトエクスペリエンスワークフローを示す図:Metaは、注文受領メッセージをBrazeに送信します。これは、eコマースプラットフォームとの往復コールがあり、WhatsAppメッセージを送信します。]({% image_buster /assets/img/whatsapp/connected_content_checkout.png %})

{% endtab %}
{% tab Webhook and custom events %}

Webhooks を使用してカートデータをシステムに送信し、カスタムイベントを使用してフォローアップメッセージをトリガーします。これは、大規模なカート処理またはマルチステップワークフローを必要とする複雑な連携に最適です。

#### 設定

`ecommerce.cart_update` eCommerce イベントによってトリガーされるWebhook キャンペーンまたはキャンバスステップを作成します。これにより、eCommerce システムにカートデータが送信されます。その後 API が次の処理を行います。
1. カートデータを受信する
2. システムでカートを作成する
3. チェックアウトURL の生成
4. `checkout_started` イベントをBraze に送信し、WhatsApp メッセージをチェックアウトリンクとともに送信するようにトリガーします

![webhook およびカスタムイベント s のチェックアウトエクスペリエンスワークフローを示す図:Metaは、eコマースプラットフォームとの往復通話を持つBrazeにオーダー受信メッセージを送信し、その後、カートURLを含むWhatsAppメッセージを送信します。]({% image_buster /assets/img/whatsapp/webhooks_custom_events_checkout.png %})

{% endtab %}
{% endtabs %}

## テストと検証

### テストメッセージの要件

カート機能はテストメッセージ間で引き継がれますが、インバウンド結果の処理は引き継がれません。

### メッセージのプレビュー

- 製品の画像と詳細は Meta カタログから取得されます。
- インタラクティブプレビューでは、統合が完了するまでプレースホルダが表示されます。

### エラーコード 

- 製品ID がカタログに存在しない場合は、エラー`product not found for product_retailer_id, fake-product-id, in catalog_id, 1903196950214359` が返されます。
- カタログがWABA から切断された場合、エラー`Check if catalog is linked to the WhatsApp Business Account and the catalog is enabled in the WhatsApp Commerce Settings` が返されます。
