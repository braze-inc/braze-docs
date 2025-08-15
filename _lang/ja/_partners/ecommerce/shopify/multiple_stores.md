---
nav_title: 複数のストアをつなぐ
article_title: Shopify 複数ストアサポート
alias: /shopify_connecting_multiple_stores/
page_order: 5
description: "この参考記事では、複数のShopifyストアを1つのワークスペースに接続し、設定する方法を取り上げている。"
---

# 複数のShopifyストアを接続する

> 単一のワークスペースに複数の Shopify ストアドメインを接続して、すべての市場における顧客の全体像を把握できます。地域のストア間で作業を重複させることなく、単一のワークスペースでオートメーションプログラムとジャーニーを構築し、起動します。  

{% alert important %}
この機能は Shopify Markets や Markets Pro には対応していません。これらのサポートを希望する場合は、[製品リクエスト]({{site.baseurl}}/user_guide/administrative/access_braze/portal/)を送信してください。
{% endalert %}

## 要件

| 要件 | 説明 |
| ----------- | ----------- |
| 複数のストアを有効にする | カスタマーサクセスマネージャーに連絡して、Shopify の複数ストアサポートを有効にします。 |
| Shopify ストアを設定する | [Braze で少なくとも 1 つの Shopify ストアを設定]({{site.baseurl}}/shopify_overview/)済みであることを確認します。 |
| 各地域の Shopify ストアの独自ドメイン | 複数ストアサポートは、さまざまな地域のストアの一意の Shopify ストアドメインで使用することを目的としています。<br><br>複数のサブブランドをBrazeに接続したい場合は、サブブランドごとに別々のワークスペースを作成することをお勧めする。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## その他のストアをつなぐ
Shopify ストアに Braze アプリをインストールし、最初のストアをインストールしたら、[**\+ 新しいストアの接続**] を選択します。

![Shopifyの統合ページにある「+ Connect New Store」ボタン]({% image_buster /assets/img/Shopify/begin_setup_button.png %}){: style="max-width:80%;"}

Shopifyの地域ストアを追加する場合は、[**セットアップを開始]**を選択する。

![統合設定」セクションに「設定を開始する」ボタンがあります。]({% image_buster /assets/img/Shopify/multiple_stores.png %}){: style="max-width:80%;"}

最初の Shopify ストア統合と同様に、標準またはカスタム設定のいずれかを選択できます。

![「Braze SDK を有効にする」セクションには、標準またはカスタム設定で Braze Web SDK を実装するためのオプションがあります。]({% image_buster /assets/img/Shopify/standard_or_custom.png %}){: style="max-width:80%;"}

あなたのニーズに最も適したオプションを選択します。

{% multi_lang_include shopify.md section='統合タブ' %}

各店舗の統合を表示し、詳細設定を行うには、ドロップダウンメニューから店舗を選択する。

![Shopify ストアを選択するドロップダウンメニュー付きの「統合設定」。]({% image_buster /assets/img/Shopify/store_dropdown_menu.png %})

## ストア間でユーザーを同期させる

### Shopify別名

複数のストアを接続すると、ログインまたは注文をしたShopifyの同期ユーザーは、{% raw %}`shopify_customer_id_{{storename}}`{% endraw %} の形式で新しいエイリアスを受け取る。

### Braze external ID

Braze external ID は以下のオプションから選択できます。

|オプション|説明|
|------|-----------|
|Shopify 顧客 ID|Shopifyの顧客IDをBraze外部IDとして使用する場合、各店舗はユーザーごとに固有の顧客IDを生成する。つまり、ユーザーが複数のストアとやり取りする場合、Braze では別々のプロファイルを持つことになります。|
|メール、ハッシュドメール、またはカスタム外部ID|メール、ハッシュ化されたメール、またはカスタム external ID タイプを使用する場合、複数のストアとエンゲージメントを持つユーザーは、ログインまたは注文時にプロファイルが 1 つの統合プロファイルにマージされます。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### マージされたフィールド

ユーザープロファイルが同期されると、以下のフィールドがマージされます。マージの動作の詳細については、「[マージ動作]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge-behavior)」を参照してください。

- デバイス情報
- 合計セッション数(両プロファイルの合計）
- カスタムイベントと購買データ
- セグメンテーション用のカスタムイベントプロパティ (例えば、「Y日間にX回」(X ≤ 50、Y ≤ 30))。
- イベント数 (両プロファイルの合計)
- 最初と最後のイベントの日付（Brazeは最も古い日付と最も遅い日付を選択する）
- キャンペーンのインタラクションデータ（最新の日付フィールド）
- ワークフローのサマリー（最新の日付フィールド）
- メッセージとエンゲージメントの履歴
- サブスクリプショングループ

### サブスクライバーの収集 (オプション)

Brazeを通して直接（Shopifyコネクターの設定で）サブスクライバーを収集するか、Shopifyからデータを同期するAPIやSDKの代替手段を通してサブスクライバーを収集するかを選択できる。

{% tabs local %}
{% tab Shopify コネクター %}
Shopifyコネクター設定の**ユーザー管理**ステップで、Brazeを使用してメールやSMS購読者のオプトインを収集し、専用のサブスクリプショングループに整理することができる：

1. 接続する各ストアに固有のサブスクリプショングループを作成します。これは、サブスクライバーがどこから来ているかについての正確なデータを維持するのに役立ちます。
2. メールおよび SMS サブスクライバーの収集を有効にします。
{% endtab %}

{% tab Braze API または SDK %}
また、Braze APIやSDKを使って、Shopifyから直接メールやSMSマーケティングのオプトイン情報を同期することもできる。

|オプション|リソース|
|------|---------|
|API |- [統合によってサポートされるものを直接置き換えるサブスクリプショングループエンドポイント]({{site.baseurl}}/api/endpoints/subscription_groups/)<br>\-  購読グループデータまたは [グローバルメールの購読ステータス]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states)を設定する [`Users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#set-subscription-groups)<br>- [Braze ユーザー設定センター]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/)。よりカスタマイズされたマーケティングオプトイン収集オプションを提供します。|
|SDK |- [`NotificationSubscriptionTypes`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#notificationsubscriptiontypes)<br>- [`addToSubscriptionGroup`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup)<br>- [`removeFromSubscriptionGroup`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#removefromsubscriptiongroup)<br>- [`setEmailNotificationSubscriptionType`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype)|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}
{% endtabs %}

## Shopify情報 

### 同期された属性

複数のストアを接続した場合、以下のアトリビューションはShopifyプロファイルの最新の状態と同期される：
- 名
- 姓
- メール
- 性別
- 生年月日
- 国
- 市区町村
- 最後に使用したアプリ
- 言語
- タイムゾーン
- Shopify タグ
- Shopify オーダー数
- Shopify 総支出額

### サポートされているイベント

#### e コマースのおすすめイベント 

複数のストアを接続すると、受信する e コマース推奨イベントにはソースイベントプロパティが含まれます。このプロパティは、イベントがどのストアフロントURLから発生したかを識別子化し、この情報をセグメンテーションや特定のユースケースのトリガーに使用できるようにする。

![アクションベースのキャンバスで、`ecommerce.order_placed` カスタムイベントを実行したユーザーを入力するトリガーがある。]({% image_buster /assets/img/Shopify/ecommerce_order_placed.png %}){: style="max-width:80%;"}

Shopify 統合内でサポートされている e コマース推奨イベントは次のとおりです。

- `ecommerce.product_viewed`
- `ecommerce.cart_updated`
- `ecommerce.checkout_started`
- `ecommerce.order_placed`
- `ecommerce.order_cancelled`
- `ecommerce.order_refunded`

#### Shopify カスタムイベントs 

Shopifyカスタムイベントには、`shopify_storefront` というイベントプロパティがある。このプロパティは、イベントがどのストアフロントURLから来たかを示し、セグメンテーションやユースケースのトリガーに活用できる。

![アクションベースのキャンバスで、`shopify_paid_order` カスタムイベントを実行したユーザーを入力するトリガーがある。]({% image_buster /assets/img/Shopify/shopify_paid_order.png %}){: style="max-width:80%;"}

サポートされているShopifyカスタムイベントは以下の通り：

- `shopify_fulfilled_order`
- `shopify_partially_fulfilled_order`
- `shopify_paid_order`
- `shopify_account_login`

すべてのイベントペイロードの完全な概要については、[Shopifyデータ機能を]({{site.baseurl}}/shopify_data_features/)参照のこと。

### Shopify 製品の同期 

Braze で各 Shopifyストアを接続および設定する際、必要に応じて、統合の一部として Shopify 製品の同期を有効にできます。

各店舗の商品同期を有効にすると、BrazeはShopifyの店舗名をカタログ名に含める。これは、異なる店舗の商品を区別するのに役立ちます。

![名前に Shopify ストアを含む Shopify のカタログ。]({% image_buster /assets/img/Shopify/catalog_store_name.png %})

