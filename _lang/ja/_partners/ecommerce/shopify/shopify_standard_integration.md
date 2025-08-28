---
nav_title: Shopify 標準統合設定
article_title: "Shopify 標準統合設定"
description: "このリファレンス記事では、Shopify の標準統合の設定方法の概要を説明します。"
page_type: partner
search_tag: Partner
alias: /shopify_standard_integration/
page_order: 1
---

# Shopify 標準統合設定

> このページでは、Shopify オンラインストアをお持ちのユーザーを対象に、Braze と Shopify の標準的な統合手順を説明します。Shopify ヘッドレスサイトを使用する場合、またはより大きくカスタマイズされたソリューションを実装する場合は、[Shopify カスタム統合設定]({{site.baseurl}}/shopify_custom_integration/)を参照してください。

## ステップ 1: Shopify ストアを接続する

1. Braze で、**Partner Integrations**> **Technology Partners** に移動し、"Shopify" を検索します。

{% alert note %}
古いナビゲーションを使用している場合は、[**統合**] に [**テクノロジーパートナー**] が表示されます。
{% endalert %}

{: start="2"}
2\.Shopify パートナーページで、[**Begin setup**] を選択して、統合プロセスを開始します。<br><br>![Shopify の統合ページ。設定を開始するブタンが表示されている。]({% image_buster /assets/img/Shopify/begin_setup.png %})<br><br> 
3\.Shopify アプリストアで、Braze アプリケーションをインストールします。<br><br>![Braze アプリストアページ。アプリケーションをインストールするボタンが表示されている。]({% image_buster /assets/img/Shopify/shopify_log_in.png %}){: style="max-width:70%;"}

{% alert note %}
Shopify アカウントが複数のストアと関連している場合、ページの右上にあるストアアイコンを選択して、[**Switch stores**] を選択すると、ログイン先のストアを変更できます。
{% endalert %}

{: start="4"}
4\.Braze アプリをインストールすると、Braze にリダイレクトされます。そこで Shopify に接続するワークスペースを確認します。Shopify ストアが接続できるワークスペースは 1 つのみです。切り替えが必要な場合は、正しいワークスペースを選択してください。<br><br>![適切なワークスペースであることを確認するウィンドウ。]({% image_buster /assets/img/Shopify/confirm_workspace1.png %}){: style="max-width:70%;"}

{: start="5"}
5\.[**Begin setup**] を選択します。<br><br>![ドメインを入力するフィールドと設定を開始するボタンが表示された「統合設定」。]({% image_buster /assets/img/Shopify/choose_account.png %})

## ステップ2: Braze Web SDK を有効にする

Shopify オンラインストアでは、標準設定を選択すると、Braze Web SDK と JavaScript SDK を自動的に実装できます。

![標準設定とカスタム設定のどちらで実装するかを選択できるオプションが表示された「Web SDK の有効化」ステップ。]({% image_buster /assets/img/Shopify/sdk_setup.png %})

標準設定のオンボーディングパスを選択すると、次のオプションのいずれかから、Braze が SDK を初期化して読み込むタイミングを選択する必要があります。 
- セッション開始など、サイト訪問の時点
    - 識別済みのユーザーと匿名ユーザーの両方を追跡
- アカウントログインなどのアカウントの登録時
    - 識別されたユーザーのみを追跡
    - サイト訪問者がアカウントの登録やアカウントへのログインを行ったときにデータの追跡を開始します。

## ステップ 3: Shopify のデータを設定する

### 標準データ設定

追跡する Shopify のデータを選択します。

![「Shopify データ追跡」セクション。行動イベントを追跡するためのチェックボックスとユーザー属性が表示されている。]({% image_buster /assets/img/Shopify/tracking_shopify_data.png %})

標準統合のデフォルトでは、以下のイベントが有効化されています。

| Braze おすすめイベント | Shopify カスタムイベントs | Shopifyカスタム属性 |
| --- | --- | --- |
| {::nomarkdown}<ul><li>製品の閲覧</li><li>カートの更新</li><li>チェックアウト開始</li><li>発注</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_account_login</li><li>shopify_paid_order</li><li>shopify_order_canceled</li><li>shopify_order_refunded</li><li>shopify_order_fulfilled</li><li>shopify_order_partially_fulfilled</li></ul>{:/} | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_spent</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li><li>shopify_province</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2  .reset-td-br-3 role="presentation"}

統合を介して追跡されるデータの詳細は、[Shopify データの機能]({{site.baseurl}}/shopify_data_features/)を参照してください。

### 履歴バックフィルの設定

標準設定では、Shopify 統合の接続前の過去 90 日間の Shopify 顧客と注文の初期読み込みを実行するオプションを利用できます。そのためには、統合の一部として初期データの読み込みを含めるチェックボックスを選択します。 

![履歴データのバックフィルの切り替え。]({% image_buster /assets/img/Shopify/historical_data_backfill_sync.png %})

このテーブルには、バックフィルを通して最初に読み込まれるデータが含まれています。

| Braze おすすめイベント | Shopify カスタムイベントs | Braze の標準属性項目 | Braze の購読テータス |
| --- | --- | --- | --- |
| {::nomarkdown}<ul><li>発注</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_spent</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li>shopify_province</li></ul>{:/} | {::nomarkdown}<ul><li>メール</li><li>名</li><li>姓</li><li>電話</li><li>市区町村</li><li>国</li></ul>{:/} | {::nomarkdown}<ul><li>この Shopify ストアに関連するメールマーケティングの購読</li><li>この Shopify ストアに関連する SMS マーケティングの購読</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

Shopify の顧客レコードが Braze に読み込まれるため、Shopify 顧客 ID が Braze external ID として使用されます。 

{% alert note %}
既存の Braze のお客様でアクティブなキャンペーンやキャンバスをご利用の場合は、[Shopify データ機能]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#historical-backfill)で詳細を確認してください。
{% endalert %}

### (高度) カスタムデータ追跡設定

Braze SDK を使用すると、この統合でサポートされている標準イベント以外にもカスタムイベントやカスタム属性を追跡することができます。カスタムイベントは、ストア内に固有のインタラクションをキャプチャーします。

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

カスタムデータを追跡することで、ユーザーの行動についてより詳しいインサイトを得ることができ、さらに体験をパーソナライズすることができます。カスタムイベントを実装するには、`theme.liquid` ファイル内の [storefront's theme code](https://help.shopify.com/en/manual/online-store/themes/theme-structure/extend/edit-theme-code) を編集する必要があります。必要に応じて開発者にサポートを依頼してください。

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

イベントやカスタム属性をログに記録するには、ユーザーのデバイスで SDK を初期化 (アクティビティのリッスン) する必要があります。カスタムデータのロギングについては、[ユーザーオブジェクト](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html)と [logCustomEvent object](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent) を参照してください。

## ステップ 4: ユーザーの管理方法を設定する

ドロップダウンから `external_id` タイプを選択します。 

![「サブスクライバーの収集セクション。]({% image_buster /assets/img/Shopify/external_id_standard.png %})

{% alert important %}
メールアドレスまたはハッシュ化されたメールアドレスを Braze external ID として使用することで、データソース全体での ID 管理を簡素化できます。ただし、ユーザーのプライバシーとデータセキュリティに対する潜在的なリスクを考慮することが重要です。<br><br>

- **推測可能な情報:** メールアドレスは推測されやすく、攻撃されやすい。
- **悪用のリスク:** 悪意のあるユーザーがWebブラウザーを改ざんし、他人のメールアドレスを外部IDとして送信した場合、機密メッセージやアカウント情報にアクセスされる可能性がある。
{% endalert %}

カスタム external ID タイプを選択した場合は、ステップ 4.1 および 4.2 に進んでください。それ以外の場合は、ステップ 4.3 に進みます。

### ステップ4.1：カスタム `external_id` を作成する

まず、Shopify に移動し、`braze.external_id` メタフィールドを作成します。[カスタムのメタフィールド記述を作成する](https://help.shopify.com/en/manual/custom-data/metafields/metafield-definitions/creating-custom-metafield-definitions)のステップを使用することを推奨します。**名前空間とキー**には `braze.external_id` と入力します。**タイプ**については、ID タイプを選択することを推奨します。

メタフィールドを作成したら、[`customer/create`](https://help.shopify.com/en/manual/fulfillment/setup/notifications/webhooks) Webhook をリッスンして、新しい顧客が作成されたときにメタフィールドを書き込むことができるようにします。次に、[Admin API](https://shopify.dev/docs/api/admin-graphql) または [Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) を使用して、すでに作成されているすべての顧客をこのメタフィールドに埋め戻してください。

### ステップ4.2：エンドポイントを作成する

外部 ID を取得するには、パブリックの GET エンドポイントが必要です。Shopify がメタフィールドを提供できない場合、Braze はそのエンドポイントを呼び出して external ID を取得します。

エンドポイントの例: `https://mystore.com/custom_id?shopify_customer_id=1234&email_address=raghav.narain@braze.com&shopify_storefront=dev-store.myshopify.com`

#### 応答

Braze は `200` ステータスコードを待ち受けます。それ以外のコードはエンドポイントの失敗とみなされます。想定されるレスポンスは次のようになります。

{% raw %}
```json
{ "external_id": "my_external_id" }
```
{% endraw %}

Admin API または Customer API を使用して、`shopify_customer_id` とメールアドレスを調べ、パラメーター値が Shopify の顧客値と一致していることを確認します。確認後、API を使って `braze.external_id` メタフィールドを取得し、external ID 値を返すこともできます。

### ステップ4.3：Shopify からメールや SMS のオプトインを収集する (オプション)

Shopify からメールまたは SMS マーケティングのオプトインを収集する選択もできます。 

メールや SMS チャネルを使用している場合、メールや SMS マーケティングのオプトイン状態を Braze に同期させることができます。Shopify からメールマーケティングのオプトインを同期すると、Braze は自動的にその特定のストアに関連するすべてのユーザーのメール購読グループを作成します。この購読グループには一意な名前を付ける必要がある。

![「購読者の収集」セクション。メールまたは SMS マーケティングのオプトインを収集するオプションが表示されている。]({% image_buster /assets/img/Shopify/collect_email_subscribers.png %})

{% alert note %}
[Shopify の概要]({{site.baseurl}}/shopify_overview/)に記載されているように、サードパーティのキャプチャーフォームを使用する場合、開発者は Braze SDK コードを統合する必要があります。これにより、フォーム送信からメールアドレスとグローバルメール購読ステータスを取得できます。具体的には、`theme.liquid` ファイルにこれらのメソッドを実装し、テストする必要があります。<br><br>
- [setEmail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail): ユーザープロファイルのメールアドレスを設定する
- [setEmailNotificationSubscriptionType](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype): グローバルメールの購読ステータスを更新する
{% endalert %}

## ステップ 5: 商品を同期 (オプション)

Shopify ストアの全商品を Braze カタログに同期し、より詳細なメッセージングのパーソナライゼーションを実現できます。自動更新はほぼリアルタイムで行われるため、カタログには常に最新の商品詳細が反映されます。詳しくは、[Shopify product syncs]({{site.baseurl}}/partners/ecommerce/shopify/shopify_catalogs/) を参照してください。

![設定プロセスのステップ 4。「カタログの商品の識別子」に「Shopify バリアント ID」が設定されている。]{% image_buster /assets/img/Shopify/sync_products_step1.png %}{: style="max-width:80%;"}

## ステップ 6: チャネルのアクティブ化

開発者を使用せずにアプリ内メッセージを有効にするには、設定でこの設定を行います。

![使用可能なオプションをブラウザ内メッセージングに設定して、チャネルを有効にする設定手順。]({% image_buster /assets/img/Shopify/activate_channels_standard.png %})

{% alert note %}
Braze は、ブラウザー内メッセージを通じて、メールアドレスや電話番号などの訪問者情報を収集します。この情報は Shopify に送信されます。このデータは、加盟店が来店者を把握し、よりパーソナライズされたショッピング体験を提供するための手がかりとなります。詳細については、[Visitor API](https://shopify.dev/docs/api/web-pixels-api/emitting-data#visitor-api) を参照してください。
{% endalert %}

### 追加 SDK チャネルのサポート

Braze SDK を使用すると、コンテンツカードなど、さまざまなメッセージングチャネルを使用できます。

#### コンテンツカードとフィーチャーフラグ

コンテンツカードやフィーチャーフラグを追加するには、開発者と協力して必要な SDK コードを`theme.liquid` ファイルに直接挿入する必要があります。詳細な手順については、[Braze SDK の統合]({{site.baseurl}}/developer_guide/sdk_integration/)を参照してください。 

#### Web プッシュ通知

現在、Web プッシュは Shopify との統合をサポートしていません。将来的にこの機能のサポートを希望される場合は、[Braze プロダクトポータル]({{site.baseurl}}/user_guide/administrative/access_braze/portal/)から製品リクエストを送信してください。

将来的にこの機能のサポートを希望される場合は、Braze [プロダクトポータル]({{site.baseurl}}/user_guide/administrative/access_braze/portal/)から製品リクエストを送信してください。

## ステップ 7:設定完了

1. 設定後、**Finish Setup**を選択します。
2. Shopify テーマ設定で、Braze アプリの埋め込みを有効にします。ストアのテーマ設定でアプリの埋め込みを有効にするには、[**Shopify を開く**] を選択して、Shopify アカウントにリダイレクトされるようにします。 

![Shopify で Braze アプリの埋め込みを有効にする必要があることを示すバナー。Shopify を開くボタンが含まれている。]({% image_buster /assets/img/Shopify/open_shopify.png %})

{: start="3"}
3\.アプリの埋め込みを有効にすると、セットアップは完了です。
統合設定、初期データ同期のステータス、アクティブな Shopify イベントを表示できることを確認します。<br><br>![連携設定を表示する Shopify のパートナーページ。]({% image_buster /assets/img/Shopify/install_complete.png %})