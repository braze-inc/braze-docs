---
nav_title: Shopifyのセットアップ
article_title: "Shopifyのセットアップ"
description: "このリファレンス記事では、Braze Web SDKに統合した後にShopifyを設定する方法について説明します。"
page_type: partner
search_tag: Partner
alias: "/shopify_subscription_states/"
alias: "/setting_up_shopify/"
page_order: 2
---

# Braze でのShopifyのセットアップ

> BrazeとのShopifyインテグレーションの設定を終了する方法について概説した。[ Braze Web SDK]({{site.baseurl}}//partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/#implement-web-sdk) をShopify Web サイトに実装した後は、次の手順に従います。

## BrazeでのShopifyインテグレーションの設定

### ステップ1:Shopifyストアを接続する

Braze で、**Partner Integrations**> **Technology Partners** に移動し、"Shopify" を検索します。

{% alert note %}
古いナビゲーションを使用している場合は、**Technology Partners** の下に**Integrations** があります。
{% endalert %}

Shopifyパートナページで、**Shopify App Store**に移動してインテグレーション処理を開始します。

![]({% image_buster /assets/img/Shopify/shop_setup_1.png %}){: style="max-width:70%"}

その後、Shopify アプリストアに移動し、Braze アプリをインストールします。

{% alert note %}
Shopify アカウントが複数のストアに関連付けられている場合は、ページの右上にあるストアアイコンを選択し、** 切り替える stores** を選択することで、ログインしているストアを切り替えるできます。
{% endalert %}

![]({% image_buster /assets/img/Shopify/switch_stores.png %}){: style="max-width:30%"}

お好みのストアを選択したら、Braze アプリ画面で**Install**を選択します。 

![]({% image_buster /assets/img/Shopify/braze_install.png %}){: style="max-width:70%"}

Braze アプリをインストールした後、Braze にリダイレクトされ、Shopify に接続するワークスペースが確認されます。 

![]({% image_buster /assets/img/Shopify/confirm_workspace.png %}){: style="max-width:50%"}

正しいワークスペースになっていることを確認したら、**セットアップを開始**を選択してShopifyインテグレーションの設定を完了できます。

![]({% image_buster /assets/img/Shopify/begin_setup.png %}){: style="max-width:70%"}

{% alert note %}
この時点では、1 つのワークスペースにつき 1 つのストアのみ接続できます。複数のShopifyストアをワークスペースに接続したい場合は、マルチストアベータのShopifyについて詳しくは、顧客のサクセスマネージャーにお問い合わせください。
{% endalert %}

### ステップ2:イベントと履歴バックフィルの選択

Shopifyストアを接続した後、手順2に進み、統合の一部として含めるイベントを選択します。少なくとも1つのイベントを選択する必要があります。

![]({% image_buster /assets/img/Shopify/shopify_step_2_events.png %}){: style="max-width:70%"}

**Product Viewed**、**Product Clicked**、または**Abandoned Cart**イベントを選択すると、"トラッキングのBraze Web SDKが必要になります。Braze Web SDKを[ Shopify ScriptTag]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/?tab=shopify%20scripttag#supported-features) またはShopifyのサイト[`theme.liquid`]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/?tab=theme.liquid#supported-features) のいずれかで実装すると、Braze は自動的に"トラッキング スクリプトと読み込むをサイトに生成します。[ヘッドレスShopifyサイト]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/#implement-web-sdk)にWeb SDKを実装する場合は、これらのイベントの"トラッキングを手動で有効にする必要があります。 

#### 履歴データのバックフィル(オプション)

オプションで、インストール前の過去90 日間の購入のバックフィルを有効にすることができます。以前の顧客と購買データを自動的に同期することで、すぐにターゲットを設定し、顧客s に参加することができます。詳細については、Shopify履歴バックフィルを確認してください。

![]({% image_buster /assets/img/Shopify/shop_setup_4.png %}){: style="max-width:70%"}

{% alert warning %}
オーダー作成イベントおよびBraze購入イベントをインポートするには、**Order Created**および**Braze購入イベント**を選択し、統合の一部として含める必要があります。
{% endalert %}

### ステップ3:サブスクライバーの収集(オプション)

Shopifyインテグレーションを使用すると、ShopifyストアからメールおよびSMSサブスクライバーをBrazeに収集できます。詳細については、[同期Shopify サブスクライバーs]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_features/shopify_user_identity/#syncing-shopify-subscribers)を参照してください。

![]({% image_buster /assets/img/Shopify/shopify_step_3_email.png %}){: style="max-width:70%"}

### ステップ 4:Shopifyプロダクトシンクの設定(オプション)

オプションで、ShopifyストアからBraze カタログに製品をほぼリアルタイムで同期することができます。これにより、メッセージをより深くパーソナライゼーションできるように製品データを取り込むプロセスが自動化されます。詳しくは、[Shopify product syncs]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_features/shopify_catalogs/) を参照してください。

![]({% image_buster /assets/img/Shopify/shopify_step_4_catalog.png %}){: style="max-width:70%"}

### ステップ 5: ブラウザ内メッセージングを有効にする 

オプションで、この機能を有効にすることで、Shopifyストアの追加チャネルをブラウザー内で使用することができます。これにより、スライドアップ、モーダル、フルスクリーン、シンプルなアンケート、カスタムHTMLなどの基本的なメッセージタイプを使用できます。

![]({% image_buster /assets/img/Shopify/shopify_step_5_channels.png %}){: style="max-width:70%"}

ブラウザ内メッセージを有効にする場合は、Braze Web SDKを"トラッキング用に実装する必要があります。[ Shopify ScriptTag]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/?tab=shopify%20scripttag#supported-features) またはShopifyのサイト[`theme.liquid`]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/?tab=theme.liquid#supported-features) のいずれかでBraze Web SDKを実装すると、Braze は基本的なブラウザ内メッセージ実装スクリプトを自動的にサイトに生成します。[ヘッドレスShopifyサイト]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/#implement-web-sdk)にWeb SDKを実装する場合、またはブラウザ内メッセージにカスタマイズを追加する場合は、[開発者ガイド](/developer_guide/platform_integration_guides/web/in-app_messaging/integration/)を使用して、手動でブラウザ内メッセージをサイトに追加する必要があります。 

### ステップ 6: 設定完了

設定後、**Finish Setup**を選択します。

![]({% image_buster /assets/img/Shopify/finish_setup.png %}){: style="max-width:70%"}

そうです!「Connection Pending」ステータスが「Connected」に更新され、接続が確立されたときのタイムスタンプが表示されます。また、それぞれのShopify機能が正常に有効になっているかどうかも確認します。 

![]({% image_buster /assets/img/Shopify/shopify_connected_store.png %}){: style="max-width:70%"}

### 詳細設定(オプション) 

#### 放棄カート or カート放棄のアップデートとチェックアウトの遅延

デフォルトでは、Braze は`shopify_abandoned_checkout` および`shopify_abandoned_cart` イベントを1 時間非アクティブにトリガーする遅延を自動的に設定します。Shopifyパートナページでドロップダウンを選択し、**Abandoned Cart Delay**と**Abandoned Checkout Delay**を5分～24時間の範囲で設定できます。

![]({% image_buster /assets/img/Shopify/shop_setup_advanced_abandonment.png %}){: style="max-width:30%"}

#### 希望のプロダクト識別子を設定する

Brazeの購入イベントをShopifyインテグレーション設定に含めた場合、Brazeは、ShopifyのProduct IDをBrazeの購入イベント内で使用する`product_id`としてデフォルトで設定します。これは、Y日間に購入した商品をフィルターする場合や、リキッドを使用してメールの内容をカスタマイズする場合に使用されます。

ShopifyのプロダクトIDの代わりに、SKUまたはプロダクトタイトルをShopifyから設定することもできます。

![]({% image_buster /assets/img/Shopify/shop_setup_advanced_productid.png %}){: style="max-width:30%"}

## トラブルシューティング

{% details Shopify アプリのインストールがまだ保留中の理由 %}
次のいずれかの理由で、インストールがまだ保留中である可能性があります。
 - BrazeがShopify webhookに設定されている場合
 - BrazeがShopifyと通信しているとき


アプリ のインストールが1 時間保留中の場合、Braze はインストールに失敗し、セットアップを再試行するように求められます。<br><br>
![Shopify]({% image_buster /assets/img/Shopify/shopify_integration8.png %}){: style="max-width:70%;"}
{% enddetails %}


{% details Shopify アプリのインストールが失敗した理由 %}
次のいずれかの理由で、インストールが失敗した可能性があります。
 - BrazeがShopifyに到達できなかった
 - Brazeがリクエストの処理に失敗しました
 - Shopify接続トークンが不正です
 - Braze Shopify アプリがShopifyの管理ページから削除された


この h アプリが表示された場合は、**Retry Setup**を選択し、インストール処理を再開することができます。<br><br>
![Shopify]({% image_buster /assets/img/Shopify/shopify_integration16.png %}){: style="max-width:70%;"}
{% enddetails %}


{% details ShopifyストアからBraze アプリライセンスをアンインストールするにはどうすればよいですか? %}

ShopifyストアからBrazeをアンインストールするには、次の2 つの方法があります。

1. Shopifyパートナページで、**Disconnect**を選択します。<br><br> !["Disconnect Integration" セクション。disconnect.] ({% image_buster /assets/img/Shopify/disconnect_integration.png %}) へのリンクがあります。{: style="max-width:70%;"}

2. **Apps**にあるShopifyの管理者ページに移動します。その後、Braze アプリのライケーションを削除することができます。<br><br> ![Braze アプリ.]({% image_buster /assets/img/Shopify/shopify_integration12.png %})を削除するかどうかを確認するモーダル{: style="max-width:70%;"}
{% enddetails %}

{% details 私はユーザーの和解に苦労している。その理由は何でしょうか。 %}

ユーザー調整に必要な支援の種類は、Web SDKの実装方法によって決まります。詳細については、[Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/)の使用開始を参照してください。 

- Shopifyのヘッドレスサイトにいる場合は、[ヘッドレス実装]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/?tab=headless%20shopify%20site#supported-features)をチェックして、チェックアウトユーザーの調整が有効になっていることを確認します。
- 同じメールまたは電話番号の重複するユーザープロファイルs が発生した場合は、次のBrazeを使用して、重複を1 つのプロファイルにマージできます。 
    - [`users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) エンドポイント
    - [一括マージ]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users#bulk-merging)
- スクリプトタグインテグレーションを使用し、Shopifyストアで"Buy Now"カートをスキップするオプションが提供されている場合、Shopify でスクリプトタグs が`device_id` を取得してカートをスキップするユーザーにイベントをマップできないため、Braze はユーザーs の調整に苦労する可能性があります。

{% enddetails %}