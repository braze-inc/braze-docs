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

## ステップ1:Shopify ストアを接続する

1. Braze で、**Partner Integrations**> **Technology Partners** に移動し、"Shopify" を検索します。

{% alert note %}
古いナビゲーションを使用している場合は、**Technology Partners** の下に**Integrations** があります。
{% endalert %}

{: start="2"}
2\.Shopifyパートナーページで、**セットアップ**を開始して統合プロセスを開始します。<br><br>![Shopify統合ページとボタンでセットアップを開始します。][1]<br><br> 
3\.Shopify アプリストアで、Braze アプリケーションをインストールします。<br><br>![アプリケーションをインストールするボタンの付いたBraze アプリストアページ。][5]{: style="max-width:70%;"}

{% alert note %}
Shopifyアカウントが複数のストアに関連付けられている場合は、ページの右上にあるストアアイコンを選択し、**Switch stores**を選択することで、ログインしているストアを変更できます。
{% endalert %}

{: start="4"}
4\.Braze アプリをインストールした後、Braze にリダイレクトされ、Shopify に接続するワークスペースが確認されます。Shopify ストアが接続できるワークスペースは 1 つのみです。切り替える必要がある場合は、正しいワークスペースを選択します。<br><br>![適切なワークスペースにいることを確認するウィンドウ。][2]{: style="max-width:70%;"}

{: start="5"}
5\.**セットアップ開始**を選択します。<br><br>![ドメインを入力するフィールドと設定を開始するボタンが表示された「統合設定」。][9]

## ステップ2:Braze Web SDK を有効にする

Shopify オンラインストアでは、標準設定を選択すると、Braze Web SDK と JavaScript SDK を自動的に実装できます。

![標準設定とカスタム設定のどちらで実装するかを選択できるオプションが表示された「Web SDK の有効化」ステップ。][3]

標準設定のオンボーディングパスを選択すると、次のオプションのいずれかから、Braze が SDK を初期化して読み込むタイミングを選択する必要があります。 
- セッション開始など、サイト訪問の時点
    - 識別されたユーザと匿名ユーザの両方を追跡します
- アカウントログインなどのアカウントの登録時
    - 識別されたユーザーのみを追跡
    - サイト訪問者がアカウントの登録やアカウントへのログインを行ったときにデータの追跡を開始します。

## ステップ 3:Shopify データの設定

### 標準データ設定

次に、追跡するShopifyデータを選択します。

![「Shopifyデータの追跡」セクションには、行動イベントとユーザー属性を追跡するチェックボックスがあります。][6]

標準統合では、次のイベントがデフォルトで有効になります。

| Braze おすすめイベント | Shopify カスタムイベントs | Shopifyカスタム属性 |
| --- | --- | --- |
| {::nomarkdown}<ul><li>製品の閲覧</li><li>カート更新</li><li>チェックアウト開始</li><li>発注</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_account_login</li><li>shopify_paid_order</li><li>shopify_order_canceled</li><li>shopify_order_refunded</li><li>shopify_order_fulfilled</li><li>shopify_order_partially_fulfilled</li></ul>{:/} | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_spent</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li><li>shopify_province</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2  .reset-td-br-3 role="presentation"}

統合によって追跡されるデータの詳細については、[Shopify Data Features]({{site.baseurl}}/shopify_data_features/)を参照してください。

### 履歴バックフィルの設定

標準設定では、Shopify 統合の接続前の過去 90 日間の Shopify 顧客と注文の初期読み込みを実行するオプションを利用できます。そのためには、チェックボックスを選択して、統合の一部として初期データロードを含めます。 

![履歴データのバックフィルの切り替え。][4]

この表には、バックフィルによって最初にロードされるデータが含まれています。

| Braze おすすめイベント | Shopify カスタムイベントs | Braze の標準属性項目 | Braze サブスクリプションステータス |
| --- | --- | --- | --- |
| {::nomarkdown}<ul><li>発注</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_spent</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li>shopify_province</li></ul>{:/} | {::nomarkdown}<ul><li>メール</li><li>名</li><li>姓</li><li>電話</li><li>市区町村</li><li>国</li></ul>{:/} | {::nomarkdown}<ul><li>このShopifyストアに関連付けられたメールマーケティングサブスクリプション</li><li>Shopifyストアに関連付けられたSMSマーケティングサブスクリプション</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

Shopifyの顧客レコードがBrazeにロードされると、Shopifyの顧客IDがBrazeの外部IDとして使用されます。 

{% alert note %}
アクティブなキャンペーンまたはキャンバスを持つ既存のBraze カスタマーの場合は、[Shopify データ機能]({{site.baseurl}}/shopify_data_features/#historical-backfill) を参照して詳細を確認してください。
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

カスタムデータを追跡することで、ユーザーの行動についてより詳しいインサイトを得ることができ、さらに体験をパーソナライズすることができます。カスタムイベントを実装するには、`theme.liquid` ファイルで[storefront のテーマコード](https://help.shopify.com/en/manual/online-store/themes/theme-structure/extend/edit-theme-code) を編集する必要があります。開発者からのヘルプが必要な場合があります。

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

## ステップ4:ユーザーの管理方法を設定する

まず、ドロップダウンから`external_id` を選択します。 

![「購読者の収集」セクション。][10]

{% alert important %}
メールアドレスまたはハッシュ化されたメールアドレスを Braze external ID として使用することで、データソース全体での ID 管理を簡素化できます。ただし、ユーザーのプライバシーとデータセキュリティに対する潜在的なリスクを考慮することが重要です。<br><br>

- **推測可能な情報:** メールアドレスは推測されやすく、攻撃されやすい。
- **悪用のリスク:** 悪意のあるユーザーがWebブラウザーを改ざんし、他人のメールアドレスを外部IDとして送信した場合、機密メッセージやアカウント情報にアクセスされる可能性がある。
{% endalert %}

次に、ShopifyからメールまたはSMSマーケティングのオプトインを収集するオプションがあります。 

メールまたはSMS チャネルを使用する場合は、メールおよびSMS マーケティングのオプトイン状態をBraze に同期できます。Shopify からメールマーケティングオプトインを同期すると、Braze はその特定のストアに関連付けられているすべてのユーザのメールサブスクリプションググループを自動的に作成します。このサブスクリプショングループに一意の名前を作成する必要があります。

![「サブスクライバの収集」セクションで、電子メールまたはSMS マーケティングのオプトインを収集するオプションがあります。][13]

{% alert note %}
[Shopify概要]({{site.baseurl}}/shopify_overview/)で説明されているように、サードパーティ製のキャプチャフォームを使用する場合は、開発者がBraze SDK コードを統合する必要があります。これにより、フォーム送信からメールアドレスとグローバルメール購読ステータスを取得できます。具体的には、`theme.liquid` ファイルにこれらのメソッドを実装してテストする必要があります。<br><br>
- [setEmail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail):ユーザープロファイルのメールアドレスを設定します
- [setEmailNotificationSubscriptionType](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype):グローバルメールサブスクリプションステータスを更新します
{% endalert %}

## ステップ 5: 同期製品(オプション)

Shopify ストアの全商品を Braze カタログに同期し、より詳細なメッセージングのパーソナライゼーションを実現できます。自動更新はほぼリアルタイムで行われるため、カタログには常に最新の商品詳細が反映されます。詳しくは、[Shopify product sync]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_catalogs/)を参照してください。

!["Shopify Variant ID"を"カタログ製品識別子"として、セットアッププロセスのステップ4。][11]{: style="max-width:80%;"}

## ステップ 6: チャンネルを有効にする(オプション)

開発者を使用せずにアプリ内メッセージを有効にするには、設定でこの設定を行います。

![使用可能なオプションをブラウザ内メッセージングに設定して、チャネルを有効にする設定手順。][13]

### 追加のSDK チャネルのサポート

Braze SDK を使用すると、アプリ内メッセージやコンテンツカードなど、さまざまなメッセージングチャネルを使用できます。

#### コンテンツカードと機能フラグ

コンテンツカードまたは機能フラグを追加するには、開発者と協力して、必要なSDK コードを`theme.liquid` ファイルに直接挿入する必要があります。詳細な手順については、[Braze SDKの統合]({{site.baseurl}}/developer_guide/sdk_integration/)を参照してください。 

#### Webプッシュ通知

Web プッシュは現在、Shopify 統合ではサポートされていません。今後、これがサポートされるようにするには、[Braze product portal]({{site.baseurl}}/user_guide/administrative/access_braze/portal/) で製品リクエストを送信します。

今後、このサポートが必要な場合は、Braze [ product portal]({{site.baseurl}}/user_guide/administrative/access_braze/portal/) から製品リクエストを送信します。

## ステップ 7:設定完了

1. 設定後、**Finish Setup**を選択します。
2. Shopify テーマ設定で、Braze アプリの埋め込みを有効にします。ストアのテーマ設定でアプリの埋め込みを有効にするには、[**Shopify を開く**] を選択して、Shopify アカウントにリダイレクトされるようにします。 

![Shopifyに組み込まれたBrazeアプリをアクティブにする必要があり、Shopifyを開くためのボタンが含まれていると言うバナー。][7]

{: start="3"}
3\.アプリの埋め込みを有効にすると、セットアップが完了します。
統合設定、初期データ同期のステータス、およびアクティブなShopifyイベントを確認できます。<br><br>![統合設定を表示するShopify パートナーページ。][8]

[1]: {% image_buster /assets/img/Shopify/begin_setup.png %}
[2]: {% image_buster /assets/img/Shopify/confirm_workspace1.png %}
[3]: {% image_buster /assets/img/Shopify/sdk_setup.png %}
[4]: {% image_buster /assets/img/Shopify/historical_data_backfill_sync.png %}
[5]: {% image_buster /assets/img/Shopify/shopify_log_in.png %}
[6]: {% image_buster /assets/img/Shopify/tracking_shopify_data.png %}
[7]: {% image_buster /assets/img/Shopify/open_shopify.png %}
[8]: {% image_buster /assets/img/Shopify/install_complete.png %}
[9]: {% image_buster /assets/img/Shopify/choose_account.png %}
[10]: {% image_buster /assets/img/Shopify/collect_email_subscribers.png %}
[11]: {% image_buster /assets/img/Shopify/sync_products_step1.png %}
[12]: {% image_buster /assets/img/Shopify/configure_settings.png %}
[13]: {% image_buster /assets/img/Shopify/collect_email_subscribers_2.png %}