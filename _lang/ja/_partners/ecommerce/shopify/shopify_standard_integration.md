---
nav_title: Shopify標準統合セットアップ
article_title: "Shopify標準統合セットアップ"
description: "このリファレンス記事では、標準のShopify統合を設定する方法について説明します。"
page_type: partner
search_tag: Partner
alias: /shopify_standard_integration/
page_order: 1
---

# Shopify標準統合セットアップ

> このページでは、Shopifyオンラインストアを使用するユーザー向けの標準統合を使用して、BrazeとShopifyを統合する方法について説明します。Shopifyヘッドレスサイトを使用する場合、またはよりカスタマイズされたソリューションを実装する場合は、[Shopifyカスタム統合セットアップ]({{site.baseurl}}/shopify_custom_integration/)を参照してください。

## ステップ 1:Shopifyストアを接続する

1. Brazeで、**Partner Integrations** > **Technology Partners** に移動し、「Shopify」を検索します。

{% alert note %}
古いナビゲーションを使用している場合は、**Technology Partners** は **Integrations** の下にあります。
{% endalert %}

{: start="2"}
2. Shopifyパートナーページで、**Begin setup** を選択して統合プロセスを開始します。<br><br>![セットアップを開始するボタンが表示されたShopify統合ページ。]({% image_buster /assets/img/Shopify/begin_setup.png %})<br><br> 
3. Shopifyアプリストアで、Brazeアプリケーションをインストールします。<br><br>![アプリケーションをインストールするボタンが表示されたBrazeアプリストアページ。]({% image_buster /assets/img/Shopify/shopify_log_in.png %}){: style="max-width:70%;"}

{% alert note %}
Shopifyアカウントが複数のストアに関連付けられている場合は、ページの右上にあるストアアイコンを選択し、**Switch stores** を選択することで、ログインしているストアを変更できます。
{% endalert %}

{: start="4"}
4. Brazeアプリをインストールした後、Brazeにリダイレクトされ、Shopifyに接続するワークスペースを確認します。Shopifyストアが接続できるワークスペースは1つのみです。切り替える必要がある場合は、正しいワークスペースを選択してください。<br><br>![適切なワークスペースにいることを確認するウィンドウ。]({% image_buster /assets/img/Shopify/confirm_workspace1.png %}){: style="max-width:70%;"}

{: start="5"}
5. **Begin setup** を選択します。<br><br>![ドメインを入力するフィールドとセットアップを開始するボタンが表示された「統合設定」。]({% image_buster /assets/img/Shopify/choose_account.png %})

## ステップ 2:Braze Web SDKを有効にする

Shopifyオンラインストアでは、標準設定を選択すると、Braze Web SDKとJavaScript SDKを自動的に実装できます。

![標準設定とカスタム設定のどちらで実装するかを選択できるオプションが表示された「Web SDKの有効化」ステップ。]({% image_buster /assets/img/Shopify/sdk_setup.png %})

標準設定のオンボーディングパスを選択すると、次のオプションのいずれかから、BrazeがSDKを初期化して読み込むタイミングを選択する必要があります。 
- セッション開始など、サイト訪問の時点
    - 識別されたユーザーと匿名ユーザーの両方を追跡します
- アカウントログインなどのアカウント登録時
    - 識別されたユーザーのみを追跡します
    - サイト訪問者がアカウントの登録やアカウントへのログインを行ったときにデータの追跡を開始します

## ステップ 3:Shopifyデータの設定

### 標準データ設定

{% multi_lang_include alerts/important_alerts.md alert='Shopify cart token alias' %}

次に、追跡するShopifyデータを選択します。

![行動イベントとユーザー属性を追跡するチェックボックスが表示された「Shopifyデータの追跡」セクション。]({% image_buster /assets/img/Shopify/tracking_shopify_data.png %})

標準統合では、次のイベントがデフォルトで有効になります。

| Brazeおすすめイベント | Shopifyカスタムイベント | Shopifyカスタム属性 |
| --- | --- | --- |
| {::nomarkdown}<ul><li>製品の閲覧</li><li>カート更新</li><li>チェックアウト開始</li><li>注文完了</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_account_login</li><li>shopify_paid_order</li><li>shopify_order_canceled</li><li>shopify_order_refunded</li><li>shopify_order_fulfilled</li><li>shopify_order_partially_fulfilled</li></ul>{:/} | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_spent</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li><li>shopify_province</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2  .reset-td-br-3 role="presentation"}

統合によって追跡されるデータの詳細については、[Shopify Data Features]({{site.baseurl}}/shopify_data_features/)を参照してください。

{% multi_lang_include alerts/important_alerts.md alert='Shopify customer create' %}

### 履歴バックフィルの設定

標準設定では、Shopify統合の接続前の過去90日間のShopify顧客と注文の初期読み込みを実行するオプションを利用できます。初期データ読み込みを含めるには、チェックボックスを選択してください。 

{% alert note %}
履歴バックフィルデータは収益レポートには含まれません。バックフィルされた注文完了イベントは、セグメンテーションにのみ使用できます。
{% endalert %}

![履歴データのバックフィルの切り替え。]({% image_buster /assets/img/Shopify/historical_data_backfill_sync.png %})

この表には、バックフィルによって最初に読み込まれるデータが含まれています。

| Brazeおすすめイベント | Shopifyカスタムイベント | Braze標準属性項目 | Brazeサブスクリプションステータス |
| --- | --- | --- | --- |
| {::nomarkdown}<ul><li>注文完了</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_spent</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li>shopify_province</li></ul>{:/} | {::nomarkdown}<ul><li>メール</li><li>名</li><li>姓</li><li>電話</li><li>市区町村</li><li>国</li></ul>{:/} | {::nomarkdown}<ul><li>このShopifyストアに関連付けられたメールマーケティングサブスクリプション</li><li>このShopifyストアに関連付けられたSMSマーケティングサブスクリプション</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

Shopifyの顧客レコードがBrazeに読み込まれると、Shopifyの顧客IDがBrazeのexternal IDとして使用されます。 

{% alert note %}
アクティブなキャンペーンまたはキャンバスを持つ既存のBrazeユーザーの場合は、[Shopifyデータ機能]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#historical-backfill)を参照して詳細を確認してください。 
{% endalert %}

### (詳細) カスタムデータトラッキング設定

Braze SDKを使用すると、この統合の標準イベントを超えるカスタムイベントまたはカスタム属性を追跡できます。カスタムイベントは、ストア内の固有のインタラクションをキャプチャーします。例:

<style>
#custom-data td {
    word-break: break-word;
    width: 50%;
}
</style>

<table style="width: 100%;">
  <thead>
    <tr>
      <th style="width: 50%;">カスタムイベント</th>
      <th style="width: 50%;">カスタム属性</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <ul>
          <li>カスタム割引コードの使用</li>
          <li>パーソナライズされたおすすめ商品とのインタラクション</li>
          <li>注文へのギフトメッセージの追加</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>お気に入りのブランドまたは製品</li>
          <li>優先ショッピングカテゴリ</li>
          <li>メンバーシップまたはロイヤルティステータス</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

カスタムデータの追跡は、ユーザーの動作に関するより深いインサイトを提供し、追加のパーソナライゼーションをサポートします。カスタムイベントを実装するには、`theme.liquid`ファイルで[ストアフロントのテーマコード](https://help.shopify.com/en/manual/online-store/themes/theme-structure/extend/edit-theme-code)を編集する必要があります。開発者の協力が必要な場合があります。

たとえば、次のJavaScriptスニペットは、現在のユーザーがニュースレターを購読しているかどうかを追跡し、その情報をBrazeのプロファイルにカスタムイベントとして記録します。

```javascript
braze.logCustomEvent(
  “subscribed_to_newsletter”,
  {
    newsletterName: ‘News and Offers’,
    customerEmail: ‘customer_1@gmail.com’,
    sendOffers: true
  }
);

```

イベントやカスタム属性をログに記録するには、ユーザーのデバイスでSDKが初期化（アクティビティをリッスン）されている必要があります。カスタムデータのロギングの詳細については、[User object](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html)および[logCustomEvent object](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent)を参照してください。

## ステップ 4:ユーザーの管理方法を設定する {#step-4}

ドロップダウンから`external_id`タイプを選択します。 

![「サブスクライバーの収集」セクション。]({% image_buster /assets/img/Shopify/external_id_standard.png %})

{% alert important %}
メールアドレスまたはハッシュされたメールアドレスをBrazeのexternal IDとして使用すると、データソース間のID管理が簡素化されます。ただし、ユーザーのプライバシーとデータセキュリティに対する潜在的なリスクを考慮することが重要です。<br><br>

- **推測可能な情報:** メールアドレスは推測されやすく、攻撃に対して脆弱です。
- **悪用のリスク:** 悪意のあるユーザーがWebブラウザーを改ざんし、他人のメールアドレスをexternal IDとして送信した場合、機密メッセージやアカウント情報にアクセスされる可能性があります。
{% endalert %}

デフォルトでは、BrazeはShopifyからのメールを自動的に小文字に変換してから、external IDとして使用します。メールまたはハッシュメールをexternal IDとして使用している場合は、メールアドレスも小文字に変換されていることを確認してから、external IDとして割り当てるか、他のデータソースからハッシュしてください。これにより、external IDの不一致を防ぎ、Brazeでの重複ユーザープロファイルの作成を回避できます。

{% alert note %}
次に表示されるステップは、external IDの選択によって異なります。<br><br>
- **カスタムexternal IDタイプを選択した場合:** ステップ4.1〜4.3を実行して、カスタムexternal IDの設定を行います。
- **Shopify顧客ID、メール、またはハッシュメールを選択した場合:** ステップ4.1〜4.3をスキップし、ステップ4.4に直接進みます。
{% endalert %}

### ステップ 4.1:`braze.external_id`メタフィールドを作成する

1. Shopifyの管理パネルで、**Settings** > **Metafields and metaobjects** に移動します。
2. **Customers** > **Add definition** を選択します。
3. **Name** には`braze.external_id`と入力します。 
4. 自動生成されたネームスペースとキー（`custom.braze_external_id`）を選択して編集し、`braze.external_id`に変更します。
5. **Type** には **ID Type** を選択します。

メタフィールドが作成されたら、顧客に対して入力します。次のアプローチをお勧めします。

- **顧客作成Webhookをリッスンする:** [`customer/create`イベント](https://help.shopify.com/en/manual/fulfillment/setup/notifications/webhooks)をリッスンするWebhookを設定します。これにより、新しい顧客の作成時にメタフィールドを書き込むことができます。
- **既存の顧客をバックフィルする:** [Admin API](https://shopify.dev/docs/api/admin-graphql)または[Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer)を使用して、以前に作成した顧客のメタフィールドをバックフィルします。

### ステップ 4.2:external IDを取得するエンドポイントを作成する

Brazeが呼び出してexternal IDを取得できる公開エンドポイントを作成する必要があります。これにより、Shopifyが`braze.external_id`メタフィールドを直接提供できないシナリオでも、BrazeがIDを取得できます。

#### エンドポイント仕様

**メソッド:** GET

Brazeは、次のパラメーターをエンドポイントに送信します。

| パラメーター            | 必須 | データタイプ | 説明                                                      |
|----------------------|----------|-----------|------------------------------------------------------------------|
| shopify_customer_id  | はい      | 文字列    | Shopify顧客ID。                                         |
| shopify_storefront   | はい      | 文字列    | リクエストのストアフロント名。例: `<storefront_name>.myshopify.com` |
| email_address        | いいえ       | 文字列    | ログインユーザーのメールアドレス。<br><br>このフィールドは、特定のWebhookシナリオでは欠落している場合があります。エンドポイントロジックでは、ここでのnull値を考慮する必要があります（たとえば、内部ロジックで必要な場合は、shopify_customer_idを使用してメールを取得します）。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

#### サンプルエンドポイント

```http
GET https://mystore.com/custom_id?shopify_customer_id=1234&email_address=bob@braze.com&shopify_storefront=dev-store.myshopify.com
```

#### 期待される応答
Brazeは、external IDのJSONを返す`200`ステータスコードを期待します。
```json
{
  "external_id": "my_external_id"
}
```

#### 検証
`shopify_customer_id`と`email_address`（存在する場合）がShopifyの顧客値と一致することを検証することが重要です。[Shopify Admin API](https://shopify.dev/docs/api/admin-graphql)または[Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer)を使用してこれらのパラメーターを検証し、正しい`braze.external_id`メタフィールドを取得できます。

#### 障害時の動作とマージ
`200`以外のステータスコードは失敗と見なされます。

- **マージへの影響:** エンドポイントが失敗した場合（`200`以外を返す、またはタイムアウトした場合）、Brazeはexternal IDを取得できません。そのため、ShopifyユーザーとBrazeユーザープロファイルの間のマージは、その時点では行われません。
- **再試行ロジック:** Brazeは標準の即時ネットワーク再試行を試みますが、障害が継続する場合、マージは次の該当するイベントまで延期されます（たとえば、次回ユーザーがプロファイルを更新するか、チェックアウトを完了したとき）。
- **サポート性:** タイムリーなユーザーマージに対応するには、エンドポイントが高可用性であり、オプションの`email_address`フィールドを適切に処理できるようにしてください。

### ステップ 4.3:external IDを入力する

[ステップ4](#step-4)を繰り返し、Brazeのexternal IDタイプとしてカスタムexternal IDを選択した後、エンドポイントURLを入力します。

#### 考慮事項

- Brazeがエンドポイントにリクエストを送信したときにexternal IDが生成されていない場合、`changeUser`関数が呼び出されると、統合はデフォルトでShopify顧客IDを使用します。このステップは、匿名ユーザープロファイルと識別されたユーザープロファイルをマージするために重要です。そのため、一時的にワークスペース内にさまざまなタイプのexternal IDが存在する場合があります。
- external IDが`braze.external_id`メタフィールドで使用可能な場合、統合はこのexternal IDを優先して割り当てます。 
    - 以前にShopify顧客IDがBraze external IDとして設定されていた場合は、`braze.external_id`メタフィールドの値に置き換えられます。 

### ステップ 4.4:ShopifyからメールやSMSのオプトインを収集する（オプション）

ShopifyからメールまたはSMSマーケティングのオプトインを収集するオプションもあります。 

メールやSMSチャネルを使用している場合、メールやSMSマーケティングのオプトイン状態をBrazeに同期できます。Shopifyからメールマーケティングのオプトインを同期すると、Brazeはその特定のストアに関連付けられているすべてのユーザーのメールサブスクリプショングループを自動的に作成します。このサブスクリプショングループに一意の名前を作成する必要があります。

![メールまたはSMSマーケティングのオプトインを収集するオプションが表示された「サブスクライバーの収集」セクション。]({% image_buster /assets/img/Shopify/collect_email_subscribers.png %})

{% alert note %}
[Shopify概要]({{site.baseurl}}/shopify_overview/)で説明されているように、サードパーティ製のキャプチャフォームを使用する場合は、開発者がBraze SDKコードを統合する必要があります。これにより、フォーム送信からメールアドレスとグローバルメールサブスクリプションステータスをキャプチャできます。具体的には、`theme.liquid`ファイルに以下のメソッドを実装してテストする必要があります。<br><br>
- [setEmail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail): ユーザープロファイルのメールアドレスを設定します
- [setEmailNotificationSubscriptionType](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype): グローバルメールサブスクリプションステータスを更新します
{% endalert %}

## ステップ 5:商品を同期する（オプション）

Shopifyストアの全商品をBrazeカタログに同期し、より詳細なメッセージングのパーソナライゼーションを実現できます。自動更新はほぼリアルタイムで行われるため、カタログには最新の商品情報が反映されます。詳しくは、[Shopify product sync]({{site.baseurl}}/partners/ecommerce/shopify/shopify_catalogs/)を参照してください。

![「Shopify Variant ID」を「カタログ製品識別子」としたセットアッププロセスのステップ4。]({% image_buster /assets/img/Shopify/sync_products_step1.png %}){: style="max-width:80%;"}

## ステップ 6:チャネルを有効にする（オプション）

開発者を使用せずにアプリ内メッセージを有効にするには、セットアップで設定します。

![使用可能なオプションとしてブラウザ内メッセージングが表示された、チャネルを有効にするセットアップステップ。]({% image_buster /assets/img/Shopify/activate_channels_standard.png %})

{% alert note %}
Brazeは、ブラウザ内メッセージを通じて、メールアドレスや電話番号などの訪問者情報を収集します。この情報はShopifyに送信されます。このデータにより、ストアオーナーは訪問者を認識し、よりパーソナライズされた買い物体験を提供できます。詳細については、[Visitor API](https://shopify.dev/docs/api/web-pixels-api/emitting-data#visitor-api)を参照してください。
{% endalert %}

### 追加SDKチャネルのサポート

Braze SDKを使用すると、コンテンツカードなど、さまざまなメッセージングチャネルを利用できます。

#### コンテンツカードとフィーチャーフラグ

コンテンツカードまたはフィーチャーフラグを追加するには、開発者と協力して、必要なSDKコードを`theme.liquid`ファイルに直接挿入する必要があります。詳細な手順については、[Braze SDKの統合]({{site.baseurl}}/developer_guide/sdk_integration/)を参照してください。 

#### Webプッシュ通知

現在、WebプッシュはShopify統合ではサポートされていません。サポートをリクエストするには、[Brazeプロダクトポータル]({{site.baseurl}}/user_guide/administrative/access_braze/portal/)からプロダクトリクエストを送信してください。

## ステップ 7:セットアップを完了する

1. セットアップの設定後、**Finish Setup** を選択します。
2. Shopifyテーマ設定で、Brazeアプリの埋め込みを有効にします。**Open Shopify** を選択すると、Shopifyアカウントにリダイレクトされ、ストアのテーマ設定でアプリの埋め込みを有効にできます。 

![ShopifyでBrazeアプリの埋め込みを有効にする必要があることを示すバナーと、Shopifyを開くためのボタン。]({% image_buster /assets/img/Shopify/open_shopify.png %})

{: start="3"}
3. アプリの埋め込みを有効にすると、セットアップが完了します。
統合設定、初期データ同期のステータス、およびアクティブなShopifyイベントを確認できることをご確認ください。<br><br>![統合設定を表示するShopifyパートナーページ。]({% image_buster /assets/img/Shopify/install_complete.png %})