---
nav_title: Shopify標準統合セットアップ
article_title: "Shopify標準統合セットアップ"
description: "このリファレンス記事では、標準のShopify 統合を設定する方法について説明します。"
page_type: partner
search_tag: Partner
alias: /shopify_standard_integration/
page_order: 1
---

# Shopify標準統合セットアップ

> このページでは、Shopifyオンラインストアを使用するユーザー向けの標準統合を使用して、BrazeとShopifyを統合する方法について説明します。Shopify ヘッドレスサイトを使用する場合、またはより大きくカスタマイズされたソリューションを実装する場合は、[Shopify カスタム統合設定]({{site.baseurl}}/shopify_custom_integration/)を参照してください。

## ステップ 1: Shopify ストアを接続する

1. Braze で、**Partner Integrations**> **Technology Partners** に移動し、"Shopify" を検索します。

{% alert note %}
古いナビゲーションを使用している場合は、**Technology Partners** の下に**Integrations** があります。
{% endalert %}

{: start="2"}
2\.Shopifyパートナーページで、**セットアップ**を開始して統合プロセスを開始します。<br><br>![Shopify統合ページとボタンでセットアップを開始します。]({% image_buster /assets/img/Shopify/begin_setup.png %})<br><br> 
3\.Shopify アプリストアで、Braze アプリケーションをインストールします。<br><br>![アプリケーションをインストールするボタンの付いたBraze アプリストアページ。]({% image_buster /assets/img/Shopify/shopify_log_in.png %}){: style="max-width:70%;"}

{% alert note %}
Shopifyアカウントが複数のストアに関連付けられている場合は、ページの右上にあるストアアイコンを選択し、**Switch stores**を選択することで、ログインしているストアを変更できます。
{% endalert %}

{: start="4"}
4\.Braze アプリをインストールした後、Braze にリダイレクトされ、Shopify に接続するワークスペースが確認されます。Shopify ストアが接続できるワークスペースは 1 つのみです。切り替える必要がある場合は、正しいワークスペースを選択します。<br><br>![適切なワークスペースにいることを確認するウィンドウ。]({% image_buster /assets/img/Shopify/confirm_workspace1.png %}){: style="max-width:70%;"}

{: start="5"}
5\.**セットアップ開始**を選択します。<br><br>![ドメインを入力するフィールドと設定を開始するボタンが表示された「統合設定」。]({% image_buster /assets/img/Shopify/choose_account.png %})

## ステップ2:Braze Web SDK を有効にする

Shopify オンラインストアでは、標準設定を選択すると、Braze Web SDK と JavaScript SDK を自動的に実装できます。

![標準設定とカスタム設定のどちらで実装するかを選択できるオプションが表示された「Web SDK の有効化」ステップ。]({% image_buster /assets/img/Shopify/sdk_setup.png %})

標準設定のオンボーディングパスを選択すると、次のオプションのいずれかから、Braze が SDK を初期化して読み込むタイミングを選択する必要があります。 
- セッション開始など、サイト訪問の時点
    - 識別されたユーザと匿名ユーザの両方を追跡します
- アカウントログインなどのアカウントの登録時
    - 識別されたユーザーのみを追跡
    - サイト訪問者がアカウントの登録やアカウントへのログインを行ったときにデータの追跡を開始します。

## ステップ 3: Shopify データの設定

### 標準データ設定

次に、追跡するShopifyデータを選択します。

![「Shopifyデータの追跡」セクションには、行動イベントとユーザー属性を追跡するチェックボックスがあります。]({% image_buster /assets/img/Shopify/tracking_shopify_data.png %})

標準統合では、次のイベントがデフォルトで有効になります。

| Braze おすすめイベント | Shopify カスタムイベントs | Shopifyカスタム属性 |
| --- | --- | --- |
| {::nomarkdown}<ul><li>製品の閲覧</li><li>カート更新</li><li>チェックアウト開始</li><li>発注</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_account_login</li><li>shopify_paid_order</li><li>shopify_order_canceled</li><li>shopify_order_refunded</li><li>shopify_order_fulfilled</li><li>shopify_order_partially_fulfilled</li></ul>{:/} | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_spent</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li><li>shopify_province</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2  .reset-td-br-3 role="presentation"}

統合によって追跡されるデータの詳細については、[Shopify Data Features]({{site.baseurl}}/shopify_data_features/)を参照してください。

{% multi_lang_include alerts/important_alerts.md alert='Shopify customer create' %}

### 履歴バックフィルの設定

標準設定では、Shopify 統合の接続前の過去 90 日間の Shopify 顧客と注文の初期読み込みを実行するオプションを利用できます。そのためには、チェックボックスを選択して、統合の一部として初期データロードを含めます。 

![履歴データのバックフィルの切り替え。]({% image_buster /assets/img/Shopify/historical_data_backfill_sync.png %})

この表には、バックフィルによって最初にロードされるデータが含まれています。

| Brazeおすすめイベント | Shopify カスタムイベントs | Braze の標準属性項目 | Braze サブスクリプションステータス |
| --- | --- | --- | --- |
| {::nomarkdown}<ul><li>行われた注文</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_spent</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li>shopify_province</li></ul>{:/} | {::nomarkdown}<ul><li>メール</li><li>名</li><li>姓</li><li>電話</li><li>市区町村</li><li>国</li></ul>{:/} | {::nomarkdown}<ul><li>このShopifyストアに関連付けられたメールマーケティングサブスクリプション</li><li>Shopifyストアに関連付けられたSMSマーケティングサブスクリプション</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

Shopifyの顧客レコードがBrazeにロードされると、Shopifyの顧客IDがBrazeの外部IDとして使用されます。 

{% alert note %}
アクティブなキャンペーンまたはキャンバスを持つ既存のBraze カスタマーの場合は、[Shopify データ機能]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#historical-backfill) を参照して詳細を確認してください。
{% endalert %}

### (詳細)カスタムデータトラッキング設定

Braze SDK を使用すると、この統合の標準イベントを超えるカスタムイベントまたはカスタム属性を追跡できます。カスタムイベントは、ストア内に固有のインタラクションをキャプチャーします。

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

カスタムデータの追跡は、ユーザーの振る舞いに関するより深いインサイトを提供し、追加のパーソナライゼーションをサポートします。カスタムイベントを実装するには、`theme.liquid` ファイルで[storefront のテーマコード](https://help.shopify.com/en/manual/online-store/themes/theme-structure/extend/edit-theme-code) を編集する必要があります。開発者からのヘルプが必要な場合があります。

たとえば、次の JavaScript スニペットは、現在のユーザーがニュースレターを購読しているかどうかを追跡し、その情報を Braze のプロファイルにカスタムイベントとして記録します。

```json
braze.logCustomEvent(
  “subscribed_to_newsletter”,
  {
    newsletterName: ‘News and Offers’,
    customerEmail: ‘customer_1@gmail.com’,
    sendOffers: true
  }
);

```

イベントやカスタム属性をログに記録するには、ユーザーのデバイスで SDK を初期化 (アクティビティのリッスン) する必要があります。カスタムデータのロギングの詳細については、[User object](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html)および[logCustomEvent object](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent)を参照してください。

## ステップ 4: ユーザーの管理方法を設定する {#step-4}

ドロップダウンから `external_id` タイプを選択します。 

![「サブスクライバーの収集」セクション。]({% image_buster /assets/img/Shopify/external_id_standard.png %})

{% alert important %}
メールアドレスまたはハッシュされたメールアドレスをBrazeの外部ID として使用すると、データソース間のID 管理が簡素化されます。ただし、ユーザーのプライバシーとデータセキュリティに対する潜在的なリスクを考慮することが重要です。<br><br>

- **推測可能な情報:**メールアドレスは推測されやすく、攻撃されやすい。
- **悪用のリスク:**悪意のあるユーザーがWebブラウザーを改ざんし、他人のメールアドレスを外部IDとして送信した場合、機密メッセージやアカウント情報にアクセスされる可能性がある。
{% endalert %}

デフォルトでは、BrazeはメールsをShopifyから小文字に自動的に変換してから、外部IDとして使用します。メールまたはハッシュメールを外部IDとして使用している場合は、メールアドレスも小文字に変換されていることを確認してから、外部IDとして割り当てるか、他のデータソースからハッシュする必要があります。これにより、外部ID の不一致を防ぎ、Braze での重複ユーザープロファイルの作成を回避できます。

{% alert note %}
次に表示されるステップは、外部ID の選択によって異なります。<br><br>
- **カスタム外部ID タイプを選択した場合:**ステップ4.1-4.3を実行して、カスタム外部ID設定を設定します。
- **Shopify 顧客 ID、メール、またはハッシュメールを選択した場合:**ステップ 4.1～4.3をスキップし、ステップ 4.4に進みます。
{% endalert %}

### ステップ4.1：`braze.external_id` メタフィールドを作成する

1. Shopifyの管理パネルで、**Settings**> **Meta フィールド s and metaobjects** に移動します。
2. **Customers**> **定義を追加**を選択します。
3. **Name**には`braze.external_id`と入力します。 
4. 自動生成されたネームスペースとキー(`custom.braze_external_id`) を選択して編集し、`braze.external_id` に変更します。
5. **Type**には**ID Type**を選択します。

メタフィールドが作成されたら、顧客s に入力します。次のアプリ侵害をお勧めします。

- **顧客作成webhookを聴く:**[`customer/create` events](https://help.shopify.com/en/manual/fulfillment/setup/notifications/webhooks) をリッスンするWebhookを設定します。これにより、新しい顧客の作成時にメタフィールドを書き込むことができます。
- **顧客を埋め戻す:**[Admin API](https://shopify.dev/docs/api/admin-graphql)または[顧客 API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer)を使用して、以前に作成した顧客sのメタフィールドを埋め戻します。

### ステップ4.2：外部ID を取得するエンドポイントを作成する

外部ID を取得するためにBraze が呼び出すことができる公開エンドポイントを作成する必要があります。これは、Shopify が`braze.external_id` メタフィールドを提供できない場合に必須です。 

#### エンドポイント仕様

**方法:** `GET`

| パラメータ | 説明 |
| --- | --- |
| `shopify_customer_id` | Shopify 顧客 ID。 |
| `email_address` | ログインユーザーのメールの住所。 |
| `shopify_storefront` | リクエストのストアフロント。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### サンプルエンドポイント

```
GET 
https://mystore.com/custom_id?shopify_customer_id=1234&email_address=bob@braze.com&shopify_storefront=dev-store.myshopify.com
```

#### 期待される反応

Braze は `200` ステータスコードを待ち受けます。それ以外のコードは障害とみなされます。

{% raw %}
```json
{ 
    "external_id": "my_external_id" 
}
```
{% endraw %}

{% alert important %}
`shopify_customer_id` と`email_address` がShopify の顧客に一致することを検証することが大切です。[Admin API](https://shopify.dev/docs/api/admin-graphql)または[Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer)を使用して、これらのパラメータを検証し、`braze.external_id`メタフィールドを取得できます。
{% endalert %}

### ステップ4.3：外部IDを入力

[手順4](#step-4)を繰り返し、Brazeの外部ID 種別としてカスタム外部ID を選択した後、エンドポイント URL を入力します。

#### 考慮事項

- Braze がエンドポイントにリクエストを送信したときに外部ID が生成されない場合、`changeUser` 関数が呼び出されると、インテグレーションはShopify 顧客 ID の使用をデフォルトします。このステップは、特定されたユーザープロファイルと匿名ユーザープロファイルをマージするために重要です。そのため、一時的にワークスペース内にさまざまなタイプの外部ID が存在する場合があります。
- 外部ID が`braze.external_id` メタフィールドで使用可能な場合、この外部ID が優先され、割り当てられます。 
    - 以前にShopify 顧客 ID がBraze 外部ID として設定されていた場合は、`braze.external_id` メタフィールドに置き換えられます。 

### ステップ4.4:Shopify からメールや SMS のオプトインを収集する (オプション)

Shopify からメールまたは SMS マーケティングのオプトインを収集する選択もできます。 

メールや SMS チャネルを使用している場合、メールや SMS マーケティングのオプトイン状態を Braze に同期させることができます。Shopify からメールマーケティングオプトインを同期すると、Braze はその特定のストアに関連付けられているすべてのユーザのメールサブスクリプションググループを自動的に作成します。このサブスクリプショングループに一意の名前を作成する必要があります。

![「サブスクライバの収集」セクションで、電子メールまたはSMS マーケティングのオプトインを収集するオプションがあります。]({% image_buster /assets/img/Shopify/collect_email_subscribers.png %})

{% alert note %}
[Shopify概要]({{site.baseurl}}/shopify_overview/)で説明されているように、サードパーティ製のキャプチャフォームを使用する場合は、開発者がBraze SDK コードを統合する必要があります。これにより、フォーム送信からメールアドレスとグローバルメール購読ステータスを取得できます。具体的には、`theme.liquid` ファイルにこれらのメソッドを実装してテストする必要があります。<br><br>
- [setEmail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail):ユーザープロファイルのメールアドレスを設定します
- [setEmailNotificationSubscriptionType](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype):グローバルメールサブスクリプションステータスを更新します
{% endalert %}

## ステップ 5: 同期製品(オプション)

Shopify ストアの全商品を Braze カタログに同期し、より詳細なメッセージングのパーソナライゼーションを実現できます。自動更新はほぼリアルタイムで行われるため、カタログには最新の商品情報が反映されます。詳しくは、[Shopify product sync]({{site.baseurl}}/partners/ecommerce/shopify/shopify_catalogs/)を参照してください。

!["Shopify Variant ID"を"カタログ製品識別子"として、セットアッププロセスのステップ4。]({% image_buster /assets/img/Shopify/sync_products_step1.png %}){: style="max-width:80%;"}

## ステップ 6: チャンネルを有効にする(オプション)

開発者を使用せずにアプリ内メッセージを有効にするには、設定でこの設定を行います。

![使用可能なオプションをブラウザ内メッセージングに設定して、チャネルを有効にする設定手順。]({% image_buster /assets/img/Shopify/activate_channels_standard.png %})

{% alert note %}
Braze は、ブラウザー内メッセージを通じて、メールアドレスや電話番号などの訪問者情報を収集します。この情報はShopifyに送信されます。このデーターにより、商店主は自分の店舗への訪問者を認識し、よりパーソナライズされたな買い物体験を作ることができる。詳細については、[Visitor API](https://shopify.dev/docs/api/web-pixels-api/emitting-data#visitor-api) を参照してください。
{% endalert %}

### 追加 SDK チャネルのサポート

Braze SDK を使用すると、コンテンツカードなど、さまざまなメッセージングチャネルを使用できます。

#### コンテンツカードとフィーチャーフラグ

コンテンツカードまたは機能フラグを追加するには、開発者と協力して、必要なSDK コードを`theme.liquid` ファイルに直接挿入する必要があります。詳細な手順については、[Braze SDK の統合]({{site.baseurl}}/developer_guide/sdk_integration/)を参照してください。 

#### Webプッシュ通知

現在、WebプッシュはShopifyインテグレーションではサポートされていません。サポートをリクエストするには、[ Braze プロダクトポータル]({{site.baseurl}}/user_guide/administrative/access_braze/portal/) からプロダクトリクエストを送信します。

## ステップ 7:設定完了

1. 設定後、**Finish Setup**を選択します。
2. Shopify テーマ設定で、Braze アプリの埋め込みを有効にします。ストアのテーマ設定でアプリの埋め込みを有効にするには、[**Shopify を開く**] を選択して、Shopify アカウントにリダイレクトされるようにします。 

![Shopifyに組み込まれたBrazeアプリをアクティブにする必要があり、Shopifyを開くためのボタンが含まれていると言うバナー。]({% image_buster /assets/img/Shopify/open_shopify.png %})

{: start="3"}
3\.アプリの埋め込みを有効にすると、セットアップが完了します。
統合設定、初期データ同期のステータス、およびアクティブなShopifyイベントを確認できます。<br><br>![統合設定を表示するShopify パートナーページ。]({% image_buster /assets/img/Shopify/install_complete.png %})