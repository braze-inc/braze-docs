---
nav_title: Shopifyの設定
article_title:"Shopifyの設定"
description:"この参考記事では、ShopifyをBraze Web SDKに統合した後の設定方法を概説している。"
page_type: partner
search_tag:Partner
alias: "/shopify_subscription_states/"
alias: "/setting_up_shopify/"
page_order:2
---

# BrazeでShopifyを設定する

> この記事では、ShopifyとBrazeの統合設定を完了する方法を概説する。Shopify Webサイトに[Braze Web SDKを実装]({{site.baseurl}}//partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/#implement-web-sdk)した後は、以下の手順に従ってください。

## BrazeでShopifyとの統合を設定する

### ステップ1:Shopifyストアに接続する

Brazeで、**パートナー連携**>**テクノロジー**パートナーと進み、"Shopify "を検索する。

{% alert note %}
古いナビゲーションをお使いの場合は、「**インテグレーション**」の下に**テクノロジー・パートナーが**ある。
{% endalert %}

Shopifyパートナーページで、**Go to Shopify App Storeを**選択し、連携プロセスを開始する。

![\]({% image_buster /assets/img/Shopify/shop_setup_1.png %}){: style="max-width:70%"}

その後、Shopify App Storeに誘導され、Brazeアプリをインストールする。

{% alert note %}
Shopifyアカウントが複数の店舗と関連している場合、ページの右上にある店舗アイコンを選択し、**店舗を切り替えるを**選択することで、ログインしている店舗を切り替えることができる。
{% endalert %}

![\]({% image_buster /assets/img/Shopify/switch_stores.png %}){: style="max-width:30%"}

希望のストアを選択した後、Brazeアプリのページで**インストールを**選択する。 

![\]({% image_buster /assets/img/Shopify/braze_install.png %}){: style="max-width:70%"}

Brazeアプリをインストールすると、Shopifyに接続するワークスペースを確認するためにBrazeにリダイレクトされる。 

![\]({% image_buster /assets/img/Shopify/confirm_workspace.png %}){: style="max-width:50%"}

正しいワークスペースにいることを確認したら、"**Begin setup**"を選択し、Shopifyとの統合設定を完了する。

![\]({% image_buster /assets/img/Shopify/begin_setup.png %}){: style="max-width:70%"}

{% alert note %}
現在、1つのワークスペースにつき1つのストアしか接続できない。ワークスペースに接続したいShopifyストアが複数ある場合は、カスタマーサクセスマネージャーにShopifyマルチストアベータの詳細を問い合わせる。
{% endalert %}

### ステップ2:選択されたイベントと過去の埋め戻し

Shopifyストアに接続した後、ステップ2に進み、統合の一部として含めるイベントを選択する。少なくとも1つのイベントを選択しなければならない。

![\]({% image_buster /assets/img/Shopify/shopify_step_2_events.png %}){: style="max-width:70%"}

**Product Viewed（商品閲覧**）、**Product Clicked（商品クリック**）、または**Abandoned Carted（カート放棄**）イベントを選択すると、トラッキング追跡にBraze Web SDKが必要となる。BrazeのWeb SDKを[Shopify ScriptTagを通して]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/?tab=shopify%20scripttag#supported-features)、またはShopifyのサイトに直接実装すると、Brazeは自動的にトラッキングスクリプトを生成し、サイトにロードします。 [`theme.liquid`]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/?tab=theme.liquid#supported-features)Brazeが自動的にトラッキングスクリプトを生成し、サイトに読み込む。[Headless Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/#implement-web-sdk)サイトにWeb SDKを実装する場合、これらのイベントのトラッキングを手動でオンにする必要がある。 

#### 過去のデータを埋め戻す（オプション）

オプションで、インストール前の過去90日間の購入履歴をイネーブルメントすることができる。過去の顧客データや購入データを自動的に同期することで、すぐにターゲットを絞り込んでカスタマーエンゲージメントを開始できる。もっと詳しく知りたい方は、Shopifyのヒストリカル・バックフィルをチェックしよう。

![\]({% image_buster /assets/img/Shopify/shop_setup_4.png %}){: style="max-width:70%"}

{% alert warning %}
Order Created EventsとBraze Purchase Eventsをインポートするには、統合の一部として**Order Createdと** **Braze Purchase Eventを**選択する必要がある。
{% endalert %}

### ステップ3:サブスクライバーを集める（オプション）

Shopifyとの統合により、ShopifyストアからBrazeにメールやSMSの購読者を集めることができる。詳しくは、[Shopifyサブスクライバーを同期するを]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_features/shopify_user_identity/#syncing-shopify-subscribers)参照のこと。

![\]({% image_buster /assets/img/Shopify/shopify_step_3_email.png %}){: style="max-width:70%"}

### ステップ 4:Shopifyの商品同期を設定する（オプション）

オプションで、ShopifyストアからBrazeカタログにほぼリアルタイムで商品を同期させることができ、メッセージのパーソナライゼーションを深めるために商品データを取り込むプロセスをオートメーション化できる。詳しくは、[Shopifyの商品同期を]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_features/shopify_catalogs/)チェックしよう。

![\]({% image_buster /assets/img/Shopify/shopify_step_4_catalog.png %}){: style="max-width:70%"}

### ステップ 5: ブラウザ内のメッセージングをイネーブルメントにする 

この機能をオンにすることで、Shopifyストアでブラウザ内メッセージ用の追加チャネルを使用することができる。これにより、スライドアップ、モーダル、フルスクリーン、簡単なアンケート、カスタムHTMLなどの基本的なメッセージタイプを使用することができる。

![\]({% image_buster /assets/img/Shopify/shopify_step_5_channels.png %}){: style="max-width:70%"}

ブラウザ内メッセージを有効にする場合、トラッキングのためにBraze Web SDKを実装する必要がある。BrazeのWeb SDKを[Shopify ScriptTagを通して]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/?tab=shopify%20scripttag#supported-features)、または直接Shopifyのサイトに実装すると、Brazeは自動的に基本的なブラウザ内メッセージ実装スクリプトをお客様のサイトに生成します。 [`theme.liquid`]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/?tab=theme.liquid#supported-features)Brazeは、基本的なインブラウザメッセージ実装スクリプトをお客様のサイトに自動的に生成する。[Headless Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/#implement-web-sdk)サイトにWeb SDKを実装する場合、またはブラウザ内メッセージにカスタマイズを追加する予定の場合は、[開発者ガイドを](/developer_guide/platform_integration_guides/web/in-app_messaging/integration/)使用して手動でブラウザ内メッセージをサイトに追加する必要がある。 

### ステップ 6: セットアップを終える

セットアップが完了したら、**Finish Setupを**選択する。

![\]({% image_buster /assets/img/Shopify/finish_setup.png %}){: style="max-width:70%"}

それだけだ！Connection Pending "のステータスが "Connected "に更新され、接続が確立されたときのタイムスタンプが表示される。また、Shopifyの各機能がページ上で正常にイネーブルメントされているかどうかも確認できる。 

![\]({% image_buster /assets/img/Shopify/shopify_connected_store.png %}){: style="max-width:70%"}

### 詳細設定（オプション） 

#### 放棄カートまたは放棄チェックアウト遅延の更新

デフォルトでは、Brazeは自動的に`shopify_abandoned_checkout` と`shopify_abandoned_cart` イベントをトリガーするディレイを1時間の非アクティブに設定する。Shopifyのパートナーページでドロップダウンを選択し、"**Set Delay "**を選択することで、各イベントに対して5分から24時間の間で**カート放棄ディレイと** **チェックアウト放棄ディレイを**設定することができる。

![\]({% image_buster /assets/img/Shopify/shop_setup_advanced_abandonment.png %}){: style="max-width:30%"}

#### 希望の製品識別子を設定する

Shopifyの統合設定にBrazeの購入イベントを含めた場合、デフォルトでは、BrazeはShopifyの商品IDをBrazeの購入イベント内で使用される`product_id` 。これは、Y日以内に購入された商品をフィルターしたり、Liquidを使ってメッセージの内容をパーソナライズしたときに使用される。

Shopify Product IDの代わりにShopifyのSKUか商品タイトルを設定することもできる。

![\]({% image_buster /assets/img/Shopify/shop_setup_advanced_productid.png %}){: style="max-width:30%"}

## トラブルシューティング

{% details Why is my Shopify app install still pending? %}
以下のいずれかの理由で、インストールがまだ保留になっている可能性がある：
 - BrazeがShopifyのWebhookを設定する場合
 - BrazeがShopifyと通信している場合


アプリのインストールが1時間保留されると、Brazeはインストールに失敗し、セットアップを再試行するよう促される。<br><br>
![Shopify]({% image_buster /assets/img/Shopify/shopify_integration8.png %}){: style="max-width:70%;"}
{% enddetails %}


{% details Why did my Shopify app install fail? %}
以下のいずれかの理由でインストールに失敗した可能性がある：
 - BrazeはShopifyにアクセスできなかった。
 - Brazeはリクエストの処理に失敗した。
 - Shopifyのアクセストークンが無効である。
 - Shopifyの管理画面からBraze Shopifyアプリが削除された


このような場合は、**Retry Setup（セットアップの再試行**）を選択し、インストール・プロセスを再度開始することができる。<br><br>
![Shopify]({% image_buster /assets/img/Shopify/shopify_integration16.png %}){: style="max-width:70%;"}
{% enddetails %}


{% details How do I uninstall the Braze application from my Shopify store? %}

ShopifyストアからBrazeをアンインストールするには、2つの方法がある：

1. Shopifyパートナーページで、**Disconnectを**選択する。<br><br> ![The "Disconnect Integration" section with a link to disconnect.]({% image_buster /assets/img/Shopify/disconnect_integration.png %}){: style="max-width:70%;"}

2. Shopifyの管理画面の「**アプリ**」にアクセスする。すると、Brazeアプリケーションを削除するオプションが表示される。<br><br> ![A modal asking for confirmation you'd like to delete the Braze app.]({% image_buster /assets/img/Shopify/shopify_integration12.png %}){: style="max-width:70%;"}
{% enddetails %}

{% details I am struggling to reconcile my users. What might be the reason? %}

ユーザー照合にどのようなサポートが必要かは、Web SDKをどのように実装したかによって決まる。詳しくは、[Shopifyを始めるを]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/)参照のこと。 

- Shopifyのヘッドレスサイトを利用している場合は、[ヘッドレスの実装を]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/?tab=headless%20shopify%20site#supported-features)チェックし、チェックアウトユーザーの照合がイネーブルメントされていることを確認しよう。
- 同じメールや電話番号のユーザープロファイルが重複している場合は、以下のBrazeツールを使用して、重複を1つのプロファイルに統合することができる： 
    - [`users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) エンドポイント
    - [一括マージ]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users#bulk-merging)
- ScriptTagインテグレーションを使用し、Shopifyストアがカートをスキップする "今すぐ購入 "オプションを提供している場合、Shopifyはスクリプトタグがカートをスキップしたユーザーにイベントをマッピングするための`device_id` を取得することを許可していないため、Brazeはユーザーの照合に苦労する可能性がある。

{% enddetails %}