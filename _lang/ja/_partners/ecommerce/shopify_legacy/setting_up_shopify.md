---
nav_title: Shopifyのセットアップ
article_title: "Shopifyのセットアップ"
description: "このリファレンス記事では、Braze Web SDKに統合した後にShopifyを設定する方法について説明します。"
page_type: partner
search_tag: Partner
alias: "/shopify_subscription_states/"
alias: "/setting_up_shopify_legacy/"
page_order: 2
---

# Braze でのShopifyのセットアップ

> この記事では、Shopify と Braze の統合を設定する方法を説明します。[ Braze Web SDK]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/#implement-web-sdk) をShopify Web サイトに実装した後は、次の手順に従います。

{% multi_lang_include alerts.md alert='Shopify deprecation' %}

## BrazeでのShopifyインテグレーションの設定

### ステップ1:Shopify ストアを接続する

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
この時点では、ワークスペースあたり1つのストアだけを接続できます。複数のShopifyストアをワークスペースに接続したい場合は、マルチストアベータのShopifyについて詳しくは、顧客のサクセスマネージャーにお問い合わせください。
{% endalert %}

### ステップ2:イベントと履歴バックフィルの選択

Shopify ストアを接続したら、ステップ2に進み、統合の一部として含めるイベントを選択します。少なくとも1つのイベントを選択する必要があります。

![]({% image_buster /assets/img/Shopify/shopify_step_2_events.png %}){: style="max-width:70%"}

[**製品の表示**]、[**製品のクリック**]、または [**カート放棄**] イベントを選択する場合、トラッキングのために Braze Web SDKが必要になります。[Shopify ScriptTag]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/?tab=shopify%20scripttag#supported-features) を使用して Braze Web SDK を実装するか、または Shopify サイト [`theme.liquid`]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/?tab=theme.liquid#supported-features) に直接実装すると、Braze によりトラッキングスクリプトが自動的に生成され、サイトに読み込まれます。Web SDK を[ヘッドレス Shopifyサイト]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/#implement-web-sdk)に実装する場合は、これらのイベントのトラッキングを手動でオンにする必要があります。 

#### 履歴データのバックフィル(オプション)

必要に応じて、インストール前の過去90日間の購入のバックフィルを有効にできます。過去の顧客データと購入データを自動的に同期することで、顧客のターゲティングや顧客とのエンゲージメントをすぐに開始できます。詳細については、Shopify 履歴バックフィルを確認してください。

![]({% image_buster /assets/img/Shopify/shop_setup_4.png %}){: style="max-width:70%"}

{% alert warning %}
バックフィルで注文作成イベントと Braze 購入イベントをインポートするには、[**注文作成イベント**] と [**Braze 購入イベント**] を選択し、統合の一部として含める必要があります。
{% endalert %}

### ステップ3:サブスクライバーの収集(オプション)

Shopifyインテグレーションを使用すると、ShopifyストアからメールおよびSMSサブスクライバーをBrazeに収集できます。詳細については、[同期Shopify サブスクライバーs]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_features/shopify_user_identity/#syncing-shopify-subscribers)を参照してください。

![]({% image_buster /assets/img/Shopify/shopify_step_3_email.png %}){: style="max-width:70%"}

### ステップ4:Shopify 製品の同期を設定する (オプション)

必要に応じて、Shopify ストアから Braze カタログに製品をほぼリアルタイムで同期できます。これにより、メッセージのより細かなパーソナライゼーションのために製品データを取り込むプロセスが自動化されます。詳しくは、[Shopify product syncs]({{site.baseurl}}/partners/ecommerce/shopify/shopify_catalogs/) を参照してください。

![]({% image_buster /assets/img/Shopify/shopify_step_4_catalog.png %}){: style="max-width:70%"}

### ステップ 5: ブラウザ内メッセージングを有効にする 

必要に応じて、この機能を有効にすることで、Shopify ストアの追加チャネルをブラウザー内メッセージで使用することができます。これにより、スライドアップ、モーダル、フルスクリーン、シンプルなアンケート、カスタムHTMLなどの基本的なメッセージタイプを使用できます。

![]({% image_buster /assets/img/Shopify/shopify_step_5_channels.png %}){: style="max-width:70%"}

ブラウザー内メッセージを有効にする場合は、トラッキングのために Braze Web SDKを実装する必要があります。[Shopify ScriptTag]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/?tab=shopify%20scripttag#supported-features) を使用して Braze Web SDK を実装するか、または Shopify サイト [`theme.liquid`]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/?tab=theme.liquid#supported-features)に直接実装すると、Braze により基本的なブラウザー内メッセージ実装スクリプトが自動的に生成され、サイトに読み込まれます。[ヘッドレスShopifyサイト]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/#implement-web-sdk)にWeb SDKを実装する場合、またはブラウザ内メッセージにカスタマイズを追加する場合は、[開発者ガイド]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=web)を使用して、手動でブラウザ内メッセージをサイトに追加する必要があります。 

### ステップ 6: 設定完了

設定後、**Finish Setup**を選択します。

![]({% image_buster /assets/img/Shopify/finish_setup.png %}){: style="max-width:70%"}

以上で操作完了です。[接続保留中] ステータスが [接続済み] に更新され、接続が確立された日時のタイムスタンプが表示されます。また、それぞれのShopify機能が正常に有効になっているかどうかも確認します。 

![]({% image_buster /assets/img/Shopify/shopify_connected_store.png %}){: style="max-width:70%"}

### 高度な設定 (オプション) 

#### 放棄カート or カート放棄のアップデートとチェックアウトの遅延

デフォルトでは、Braze は `shopify_abandoned_checkout` および`shopify_abandoned_cart` イベントのトリガーの遅延時間を、(何も操作が行われなかった) 1時間に自動的に設定します。[**カート放棄の遅延**] と [**チェックアウト放棄遅延**] は、イベントごとに5分から最大24時間までの範囲で設定できます。設定するには、Shopify パートナーページでドロップダウンから時間を選択してから、[**遅延を設定**] を選択します。

![]({% image_buster /assets/img/Shopify/shop_setup_advanced_abandonment.png %}){: style="max-width:30%"}

#### 希望のプロダクト識別子を設定する

Braze 購入イベントを Shopify 統合設定に含めた場合、Braze では、Shopify 製品 ID が、Braze 購入イベント内で使用する `product_id` としてデフォルトで設定されます。これは、Y 日間内に購入した製品をフィルタリングする場合や、Liquid を使用してメッセージのコンテンツをパーソナライズする場合に使用されます。

Shopify 製品 ID の代わりに、SKU または製品タイトルを Shopify から設定することもできます。

![]({% image_buster /assets/img/Shopify/shop_setup_advanced_productid.png %}){: style="max-width:30%"}

## トラブルシューティング

{% details Shopify アプリのインストールがまだ保留中の理由 %}
次のいずれかの理由で、インストールがまだ保留中である可能性があります。
 - BrazeがShopify webhookに設定されている場合
 - BrazeがShopifyと通信しているとき


アプリのインストールが1時間にわたり保留されている場合、Braze はインストールに失敗し、設定を再試行するように求められます。<br><br>
![Shopify]({% image_buster /assets/img/Shopify/shopify_integration8.png %}){: style="max-width:70%;"}
{% enddetails %}


{% details Shopify アプリのインストールが失敗した理由 %}
次のいずれかの理由で、インストールが失敗した可能性があります。
 - Braze が Shopify にアクセスできなかった
 - Brazeがリクエストの処理に失敗しました
 - Shopify接続トークンが不正です
 - Braze Shopify アプリがShopifyの管理ページから削除された


その場合は、[**設定を再試行**] を選択して、インストールプロセスをやり直すことができます。<br><br>
![Shopify]({% image_buster /assets/img/Shopify/shopify_integration16.png %}){: style="max-width:70%;"}
{% enddetails %}


{% details Shopify ストアから Braze アプリライセンスをアンインストールするにはどうすればよいですか? %}

ShopifyストアからBrazeをアンインストールするには、次の2 つの方法があります。

1. Shopifyパートナページで、**Disconnect**を選択します。<br><br> ![接続解除のリンクが表示されている「統合の接続を解除」セクション。]({% image_buster /assets/img/Shopify/disconnect_integration.png %}){: style="max-width:70%;"}

2. **Apps**にあるShopifyの管理者ページに移動します。その後、Braze アプリケーションを削除するオプションが表示されます。<br><br> ![Braze アプリの削除操作の確認を求めるモーダル。]({% image_buster /assets/img/Shopify/shopify_integration12.png %}){: style="max-width:70%;"}
{% enddetails %}

{% details ユーザー照合がうまくできません。その理由は何でしょうか? %}

ユーザー照合に必要なサポートの種類は、Web SDK の実装方法によって異なります。詳細については、[Shopify]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/)の使用開始を参照してください。 

- Shopify ヘッドレスサイトでは、[ヘッドレス実装]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/?tab=headless%20shopify%20site#supported-features)をチェックして、チェックアウトユーザーの照合が有効になっていることを確認します。
- 同じメールや電話番号のユーザープロファイルが重複している場合、以下の Braze ツールを使用して、重複するプロファイルを1つのプロファイルに統合できます。 
    - [`users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) エンドポイント
    - [一括マージ]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users#bulk-merging)
- ScriptTag 統合を使用しており、Shopify ストアでカートをスキップする 「Buy Now」オプションが提供されている場合、Shopify ではカートをスキップしたユーザーにイベントをマッピングするための `device_id` をスクリプトタグが取得できないため、Braze ではユーザーの照合が難しいことがあります。

{% enddetails %}
