---
nav_title: はじめに
article_title: "Shopifyを使い始める"
description: "この参考記事では、ShopifyウェブサイトにBraze Web SDKを実装する方法を概説している。"
page_type: partner
search_tag: Partner
alias: /getting_started_shopify/
page_order: 1
---

# Shopifyを使い始める

> この記事では、ShopifyウェブサイトにBraze Web SDKを実装する方法を概説する。実装後、[Shopifyと]({{site.baseurl}}//partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify)Brazeの統合設定を完了する方法については、[Shopifyを設定するを]({{site.baseurl}}//partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify)参照のこと。

## 統合セットアップ・チェックリスト

1. [Braze Web SDKを実装する](#implement-web-sdk)
2. [BrazeでShopifyをセットアップする]({{site.baseurl}}//partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify)
3. Shopifyとの統合をテストする

## ShopifyウェブサイトにWeb SDKを実装する {#implement-web-sdk}

[Braze Web SDKは]({{site.baseurl}}/user_guide/onboarding_with_braze/web_sdk/)、Shopifyストアの顧客の行動を追跡するための強力なツールである。Web SDKを使用すると、Webまたはモバイルブラウザからセッションデータを収集し、ユーザーを識別し、ユーザーの行動データを記録することができる。また、インブラウザ・メッセージのようなネイティブ・メッセージング・チャンネルのロックを解除することもできる。

Shopifyとの統合は、デフォルトで堅牢な機能を提供しているが、[Shopifyとの統合でサポートされていないイベントの]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_data_in_braze/)オンサイトトラッキングを追加したり、[コンテンツカードの]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards)ようなチャネルを追加したりするユースケースがある場合は、Web SDKをShopifyサイトに直接実装する必要があることを覚えておいてほしい。

統合のオンボーディングを開始する前に、Web SDKを実装するためにどのようなパスを取るかについて、チームと以下を確認してほしい。

### サポートされている機能

|アイコン| 定義 
|-------------|-------------
|<i aria-hidden="true" class="fas fa-check" title="サポート"></i><span class="sr-only">対応</span> | サポート
|<i aria-hidden="true" class="fas fa-times" title="未対応"></i><span class="sr-only">対応</span> | サポートされていない
{: .reset-td-br-1 .reset-td-br-2} 

| 特徴 | Shopify ScriptTag経由のWeb SDK | ウェブSDKとの直接統合 theme.liquid | Shopify Hydrogenを介したWeb SDKの直接統合
|-------------|-------------|-------------|------------
| デフォルトの現場追跡      | <i class="fas fa-check" title="サポート"></i> | <i class="fas fa-times" title="サポートされていない"></i> | <i class="fas fa-times" title="サポートされていない"></i>          
| キャプチャーフォームのユーザー照合（低いエンジニアリングリフトが必要）   | <i class="fas fa-check" title="サポート"></i> | <i class="fas fa-check" title="サポート"></i> | <i class="fas fa-times" title="サポートされていない"></i> 
| チェックアウト・ユーザーの照合     | <i class="fas fa-check" title="サポート"></i>  | <i class="fas fa-times" title="サポートされていない"></i>   | <i class="fas fa-times" title="サポートされていない"></i>                                        
| 製品を見た<br> 製品クリック<br> 放置されたカート   | <i class="fas fa-check" title="サポート"></i> |<i class="fas fa-check" title="サポート"></i> | <i class="fas fa-times" title="サポートされていない"></i> 
| 放棄されたチェックアウト<br> オーダー作成<br> ブレイズ購入<br> 注文は支払われた<br> 部分的に履行された注文<br> 履行された注文<br> 注文のキャンセル<br> 払い戻し<br> 顧客の作成と更新 | <i class="fas fa-check" title="サポート"></i> | <i class="fas fa-check" title="サポート"></i> | <i class="fas fa-check" title="サポート"></i>
| 歴史的埋め戻し | <i class="fas fa-check" title="サポート"></i>  | <i class="fas fa-check" title="サポート"></i>  | <i class="fas fa-check" title="サポート"></i>  
| カタログ同期  |<i class="fas fa-check" title="サポート"></i> |<i class="fas fa-check" title="サポート"></i>  |<i class="fas fa-check" title="サポート"></i>
| EメールとSMSの購読者収集    | <i class="fas fa-check" title="サポート"></i>| <i class="fas fa-check" title="サポート"></i>  | <i class="fas fa-check" title="サポート"></i>     
| デフォルトのアプリ内メッセージのサポート   | <i class="fas fa-check" title="サポート"></i>  | <i class="fas fa-check" title="サポート"></i>  | <i class="fas fa-times" title="サポートされていない"></i>     
| デフォルトのコンテンツカードをサポート   | <i class="fas fa-times" title="サポートされていない"></i> | <i class="fas fa-times" title="サポートされていない"></i> | <i class="fas fa-times" title="サポートされていない"></i>   
| デフォルトのウェブ・プッシュ対応     | <i class="fas fa-times" title="サポートされていない"></i> | <i class="fas fa-times" title="サポートされていない"></i> | <i class="fas fa-times" title="サポートされていない"></i>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}    

{% tabs %}
{% tab Shopifyスクリプトタグ %}

### Shopify ScriptTagでBraze Web SDKを実装する

[ShopifyのScriptTagは](https://shopify.dev/api/admin-rest/2021-10/resources/scripttag#top)リモートJavaScriptコードで、お店のページやチェックアウトの注文状況ページに読み込まれる。ストアページがロードされると、Shopifyはサイトページにスクリプトタグをロードする必要があるかどうかをチェックする。 

Brazeをすぐに使い始めたい場合は、BrazeがBraze Web SDK用の定義済みスクリプトをShopifyストアサイトに直接ロードするオプションがある。

{% alert important %}
この統合方法のためのBraze Web SDKの事前定義スクリプトはカスタマイズできない。
{% endalert %}

#### Shopifyとの統合の仕組み

Shopifyサイトがロードされると、Shopifyはスクリプトタグをページにロードする必要があるかどうかをチェックする。このプロセスの間、Braze Web SDKスクリプトは、ストアのページまたはチェックアウトの注文状況ページに読み込まれる。 

また、Shopify ScriptTagやアプリ内メッセージングをチャネルとして必要とする商品閲覧、商品クリック、カート放棄イベントを選択した場合は、事前に定義されたスクリプトを追加する。  

#### 有効化する方法

統合の一部としてBraze Web SDKスクリプトを自動的に有効にするには、[Shopify統合のセットアップ]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/)中に、サポートされているShopify ScriptTagイベントを選択するか、チャネルとしてアプリ内メッセージを有効にする。 

Shopifyセットアップコンポーザーから、アスタリスク(\*)で示されたイベントは、Web SDKによってサポートされている。これらのイベントを選択するか、ブラウザ内メッセージングを含めると、BrazeはShopify ScriptTag経由でWeb SDKの実装をShopifyストアにセットアップの一部として追加する。

#### Shopifyのメールキャプチャフォームとユーザー照合 

キャプチャー・フォームは、顧客のライフサイクルの初期段階で、特定可能な顧客情報を取得し、下流のメッセージングやエンゲージメントに役立てる。 

Web SDK は、`device_id` を使用することにより、Shopify の現場での行動と匿名ユーザーを追跡する。BrazeのShopify ScriptTagインテグレーションは、ニュースレター登録などのShopifyのメール取り込みフォームからのメールを、ユーザーの`device_id` 。

典型的なメール・キャプチャ・フォームには以下のようなものがある： 
- 電子メール・キャプチャ・フォーム 
- ニュースレター登録フォーム

ユーザーのEメールと`device_id` を照合する方法は2つある： 
- Braze自動メールキャプチャスクリプトを使用する 
- `setEmail` または`setPhoneNumber` メソッドを呼び出す

##### Eメールや電話でのサインアップを獲得する

Brazeを使えば、[Eメールや]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/email_capture_form/#step-1-create-an-in-app-message-campaign) [SMS、WhatsAppの]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture)登録フォームを使って、Web SDKやアプリ内メッセージを活用できる。 

ShopifyのEメールや電話番号のキャプチャ、またはサードパーティのキャプチャフォームを使用する場合は、Braze Web SDKで追跡されるユーザーに直接設定することができる。例えば、顧客のEメールアドレスを取得した場合、それをユーザー・プロフィールに次のように設定することができる：

{% raw %}
```javascript
braze.getUser().setEmail(<email address>);
```
{% endraw %}

これらの値の設定の詳細については、以下のJavascriptリソースを参照のこと：

- ユーザーの[Eメールを](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail)設定する
- ユーザーの[電話番号を](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setphonenumber)設定する

Eメールや電話番号を収集する際に、このようにユーザーの購読状態を設定することもできる：

{% raw %}
```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.SUBSCRIBED);
```
{% endraw %}

これらの値の設定の詳細については、以下のJavascriptリソースを参照のこと：

- ユーザーの[電子メール通知購読タイプを](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype)設定する
- ユーザーを[購読グループに](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup)追加する

**第三者キャプチャ・フォームの実装例**

1. `theme.liquid` で、以下のスニペットを`head tag` にコピーする：

{% raw %}
```javascript
<script>
  const emailInputPoller = setInterval(()=>{
    if (document.getElementById('{FORM_ID}')) {
      document.getElementById('{FORM_ID}').addEventListener("submit",
        function() {  
          var email = document.getElementById('{INPUT_EMAIL_ID}').value
          braze.getUser().setEmail(email)
        }
      );
    }
    clearInterval(emailInputPoller)
  }, 2000)
</script>
```
{% endraw %}

{: start="2"}
2\.まず、スクリプトが最初にロードされるように、`setInterval` 。
3\.`{FORM_ID}` 、キャプチャしたいフォームの要素IDに置き換える。
(ContactFooter "など）。
4\.`{INPUT_EMAIL_ID}` 、フォーム内のEメール入力フィールドの要素IDに置き換える。
5. フォームが送信されると、スクリプトは電子メールの入力値で`setEmail` 。
6. スクリプトがロードされた後、`clearInterval` 。

{% alert note %}
現時点では、BrazeのメールキャプチャフォームはShopifyの顧客を作成しない。その結果、顧客がチェックアウトを通過するか、アカウントを作成するまで、Shopifyのユーザープロファイルが関連付けられていないBrazeのユーザープロファイルを持つことができる。
{% endalert %}

#### 導入後に期待されること

**Braze Web SDKの初期化**

Web SDKはセッション開始時に初期化される。Brazeは、Shopifyの顧客ID、Eメール、電話番号などの他の識別子がShopifyストアのゲスト訪問者から容易に入手できない可能性があるため、匿名ユーザーデータを追跡するために`device_id` を収集する必要がある。

また、`device_id` 、チェックアウト後に顧客がより多くの特定可能な情報（電子メールアドレスや電話番号など）を提供した場合、匿名ユーザープロファイルとユーザーデータを照合するために使用される。

**Braze Web SDKバージョン**

Shopify ScriptTag統合によるBraze Web SDKの現在のバージョンはv4.2である。

**1 か月あたりのアクティブユーザー数 (MAU)**

Web SDKはShopifyの顧客やゲストのセッションを追跡する。その結果、これはBrazeダッシュボードのレポート内でMAUとして計上され、MAU割り当ての対象となる。匿名ユーザーもMAUにカウントされることに注意することが重要だ。モバイルデバイスの場合、匿名ユーザーはデバイスによって決まります。Web ユーザーの場合、匿名ユーザーはブラウザーのキャッシュによって決まります。

{% endtab %}

{% tab theme.liquid %}

### WebSDKをShopifyサイトに直接実装する theme.liquid

Brazeは、Web SDKを実装するための複数の方法を提供している：
- Web SDKをShopify`theme.liquid` ファイルに直接追加する。
- Google Tag Manager 

すでにShopifyストアにWeb SDKをインストールしている場合でも、オンボーディングプロセス内でShopify ScriptTagのセットアップを進めることができる。 

インストールプロセス中、BrazeはWeb SDKのインスタンスがShopifyストアですでに利用可能かどうかをチェックする。既存の実装がある場合、BrazeはWeb SDKを有効にするための定義済みスクリプトを読み込まない。その後、必要なスクリプトを追加して、選択したイベントをトラッキングできるようにしたり、ブラウザ内のメッセージングを有効にしたりする。

#### 有効化する方法

手動でWeb SDKを実装するには、[初期SDKセットアップを]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/)参照のこと。Google Tag Manager経由でWeb SDKを実装するには、[Google Tag Manager for Webを]({{site.baseurl}}/developer_guide/platform_integration_guides/web/google_tag_manager#google-tag-manager)参照のこと。 

どちらの実装パスでも、Web SDKインテグレーションに以下が含まれていることを確認すること： 
- Web SDKのバージョンはv4.0+である。
- セッション開始時にWeb SDKが初期化される

#### Shopifyのメールキャプチャフォームとユーザー照合 

キャプチャー・フォームは、顧客のライフサイクルの初期段階で、特定可能な顧客情報を取得し、下流のメッセージングやエンゲージメントに役立てる。 

Web SDK は、`device_id` を使用することにより、Shopify の現場での行動と匿名ユーザーを追跡する。BrazeのShopify ScriptTagインテグレーションは、ニュースレター登録などのShopifyのメール取り込みフォームからのメールを、ユーザーの`device_id` 。

典型的なメール・キャプチャ・フォームには以下のようなものがある： 
- 電子メール・キャプチャ・フォーム 
- ニュースレター登録フォーム

ユーザーのEメールと`device_id` を照合する方法は2つある： 
- Braze自動メールキャプチャスクリプトを使用する 
- `setEmail` または`setPhoneNumber` メソッドを呼び出す

##### Eメールや電話でのサインアップを獲得する

Brazeを使えば、[Eメールや]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/email_capture_form/#step-1-create-an-in-app-message-campaign) [SMS、WhatsAppの]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture)登録フォームを使って、Web SDKやアプリ内メッセージを活用できる。 

Shopifyの電子メールや電話番号のキャプチャ、またはサードパーティのキャプチャフォームを使用する場合は、Braze Web SDKで追跡されるユーザーオブジェクトに直接設定することができる。例えば、顧客のEメールアドレスを取得した場合、それをユーザー・プロフィールに次のように設定することができる：

{% raw %}
```javascript
braze.getUser().setEmail(<email address>);
```
{% endraw %}

これらの値の設定の詳細については、以下のJavascriptリソースを参照のこと：

- ユーザーの[Eメールを](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail)設定する
- ユーザーの[電話番号を](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setphonenumber)設定する

また、このようにEメールや電話番号を収集しながら、ユーザーの購読状態を設定することもできる：

{% raw %}
```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.SUBSCRIBED);
```
{% endraw %}

これらの値の設定の詳細については、以下のJavascriptリソースを参照のこと：

- ユーザーの[電子メール通知購読タイプを](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype)設定する
- ユーザーを[購読グループに](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup)追加する

**第三者キャプチャ・フォームの実装例**

1. `theme.liquid` で、以下のスニペットを`head tag` にコピーする：

{% raw %}
```javascript
<script>
  const emailInputPoller = setInterval(()=>{
    if (document.getElementById('{FORM_ID}')) {
      document.getElementById('{FORM_ID}').addEventListener("submit",
        function() {  
          var email = document.getElementById('{INPUT_EMAIL_ID}').value
          braze.getUser().setEmail(email)
        }
      );
    }
    clearInterval(emailInputPoller)
  }, 2000)
</script>
```
{% endraw %}

{: start="2"}
2\.まず、スクリプトが最初にロードされるように、`setInterval` 。
3\.`{FORM_ID}` 、キャプチャしたいフォームの要素IDに置き換える。
(ContactFooter "など）。
4\.`{INPUT_EMAIL_ID}` 、フォーム内のEメール入力フィールドの要素IDに置き換える。
5. フォームが送信されると、スクリプトは電子メールの入力値で`setEmail` 。
6. スクリプトがロードされた後、`clearInterval` 。

{% alert note %}
現時点では、BrazeのメールキャプチャフォームはShopifyの顧客を作成しない。その結果、顧客がチェックアウトを通過するか、アカウントを作成するまで、Shopifyのユーザープロファイルが関連付けられていないBrazeのユーザープロファイルを持つことができる。
{% endalert %}

#### 統合後に期待されること

**Braze Web SDKの初期化**

Web SDKはセッション開始時に初期化される。Brazeは、Shopifyの顧客ID、Eメール、電話番号などの他の識別子がShopifyストアのゲスト訪問者から容易に入手できない可能性があるため、匿名ユーザーデータを追跡するために`device_id` を収集する必要がある。

また、`device_id` は、顧客がチェックアウト・プロセスの間やその後に、より多くの特定可能な情報（Eメールや電話番号など）を提供する際に、匿名ユーザー・プロフィールとユーザー・データを照合するためにも使用される。

**Braze Web SDKバージョン**

Braze Web SDKの現在のバージョンはv4.0以上であること。

**1 か月あたりのアクティブユーザー数 (MAU)**

Web SDKはShopifyの顧客やゲストのセッションを追跡する。その結果、これはBrazeダッシュボードのレポート内でMAUとして計上され、MAU割り当ての対象となる。匿名ユーザーもMAUにカウントされることに注意することが重要だ。モバイルデバイスの場合、匿名ユーザーはデバイスによって決まります。Web ユーザーの場合、匿名ユーザーはブラウザーのキャッシュによって決まります。

{% endtab %}
{% tab ヘッドレスShopifyサイト %}

### ヘッドレスShopifyサイトに直接Web SDKを実装する {#headless-site}

BrazeのShopify ScriptTagインテグレーションは、Shopifyのヘッドレスサイトとは互換性がない。その結果、閲覧された商品、クリックされた商品、放棄されたカートのイベントをデフォルトでサポートしたり、あらかじめ定義されたスクリプトを使ってアプリ内メッセージを有効にしたりすることはできない。 

#### 有効化する方法

Web SDKを直接ヘッドレスShopifyサイトに統合するには、[Inital SDK Setup for Webを]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/)参照のこと。

Web SDKの統合に以下が含まれていることを確認する： 
- Web SDKのバージョンはv4.0以上でなければならない。
- セッション開始時にWeb SDKが初期化される

#### ユーザー照合のためにShopifyフォームを設定する

Eコマースブランドは、Shopifyのサイト上で、Eメールキャプチャフォームのように、チェックアウトの前に顧客から識別可能な情報を取得するエクスペリエンスを持っている可能性が高い。

Web SDK は、Shopify のサイト上での行動と匿名ユーザーを`device_id` で追跡する。メールアドレスが匿名ユーザープロフィールに追加されていることを確認するには、ニュースレターまたはメール収集フォームのいずれかに以下を追加する： 
- [セットEメール](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail) 
  - Eメール・キャプチャやニュースレターの登録
- [エイリアスを追加する](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addalias) 
  - "alias_label": "shopify_email" 
  - "alias_name": "example@email.com"

ユーザーがアカウントに登録またはログインする際、外部IDで[ユーザー・プロファイルを識別]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#identified-user-profiles)したい場合がある。ユーザーが登録しログインした後、[changeUser](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser)メソッドを追加し、ユーザーがアカウントを作成したりログインした場合に外部IDを割り当てる。 

{% alert note %}
ユーザー・プロファイルに一時的なエイリアスを設定すれば、[users/mergeエンドポイント・エンドポイントへの]({{site.baseurl}}/api/endpoints/user_data/post_users_merge)リクエストを進め、後の時点でユーザーを特定することができる。
{% endalert %}

#### チェックアウトのユーザー照合を設定する {#headless-checkout}

放棄されたチェックアウトイベントを有効にすると、BrazeはShopifyのチェックアウト/作成ウェブフックを受信する。Brazeは、メールアドレス、電話番号、またはShopifyの顧客IDのいずれかによって、既存のユーザープロファイルとのマッチングを試みる。一致するプロファイルがない場合、Brazeはエイリアスのプロファイルを作成する。 

Shopifyウェブフックによって作成されたShopifyエイリアスユーザープロファイルと現場で追跡されたユーザプロファイルがマージされることを確認するには、以下の手順で[`/users/merge` エンドポイントを]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)使用することができる。 

{% alert tip %}
SDKまたは`theme.liquid` ファイル上で行われるAPIコールによってカスタムイベントをログに記録し、`users/merge` エンドポイントへのリクエストを含むキャンバスをトリガーすることができる。これらの方法の概要は以下の通りである。
{% endalert %}

顧客がShopifyサイトを訪問すると、すぐに匿名ユーザーが作成される。このユーザーには自動的にBraze`device_id` が割り当てられる。 

1. 新規セッション時に、サイト訪問者に一意の[ユーザーエイリアスを]({{site.baseurl}}/api/objects_filters/user_alias_object#user-alias-object-specification)ランダムに割り当てる。

2. ユーザーがサイト上でアクションを実行すると、[カスタム・イベントとして]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events)ログに記録するか、[ユーザー属性をキャプチャする]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_custom_attributes/)。ユーザーがチェックアウトに進み、ShopifyのフォームにEメールを入力すると、Shopifyの顧客IDが作成される。Brazeは、Shopifyのウェブフックを処理し、Eメール、電話、Shopifyのエイリアスが既存のユーザーと一致しない場合は、新しいユーザープロファイルを作成する。

{% raw %}
```javascript
{
  "user_alias": {
    "alias_name": 1234,
    "alias_label": "temp_user_id"
  }
}
```
{% endraw %}

{% subtabs %}
{% subtab API approach %}

{: start="3"}
3\.ユーザープロファイルの重複を防ぐには、Braze`device_id` を含むユーザープロファイルとShopifyエイリアスプロファイルを含むユーザープロファイルをマージする必要がある。遅延を設定し、`do_not_merge` 属性でユーザーを更新し、[`/users/merge` エンドポイントに]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)リクエストを行う API トリガーキャンバスを作成できる。また、`merge_user` のようなカスタム・イベントを記録して、キャンバスをトリガーすることもできる。 


{% endsubtab %}
{% subtab Non-API approach %}

{: start="3"}
3\.ユーザーがフローを終了するか、チェックアウトを完了すると、`merge_user` のようなカスタムイベントをログに記録して、遅延を設定するCanvasをトリガーし、`do_not_merge` 属性でユーザーを更新し、[`/users/merge` エンドポイントに]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)リクエストすることができる。

{% endsubtab %}
{% endsubtabs %}

{: start="4"}
4\.キャンバスの入力条件では、未確認のユーザー・プロファイルのみを対象とする。つまり、外部IDを持たず、`do_not_merge` 。<br><br>![`do_not_merge` 、キャンバスコンポーザーの「エントリー観客」ステップをフィルターとして使用する。]({% image_buster /assets/img/Shopify/shop_usermerge_canvas_entrycriteria.png %})

{: start="5"}
5. キャンバスの入力条件を設定したら、キャンバスフローを作成する。キャンバスの最初のステップを**Delay**ステップにして、処理中に起こりうるレースコンディションを防ぐ。<br><br>![] （{% image_buster /assets/img/Shopify/shop_usermerge_canvas_delay.png %} ）。

{: start="6"}
6. これらのユーザーは次のステップでマージされるため、`do_not_merge` カスタム属性を "true "に更新する**ユーザー更新**ステップを作成できる。<br><br>![キャンバスのコンポーザーで、`do_not_merge` を属性として選択したユーザーによる更新ステップ。]({% image_buster /assets/img/Shopify/shop_usermerge_canvas_userupdate.png %})

{: start="7"}
7. 次に、ウェブフックを使って**メッセージ・**ステップを作成する。<br><br>![Webhookメッセージングチャンネルを持つキャンバスコンポーザーのメッセージステップ。]({% image_buster /assets/img/Shopify/shop_usermerge_canvas_webhook.png %}) 

{% raw %}
```javascript
{
  "merge_updates": [
    {
      "identifier_to_merge": {
           "user_alias": {
                "alias_label": "temp_user_id",
                "alias_name": "{{canvas_entry_properties.${temp_user_id}}}"
            }
      },
      "identifier_to_keep": {
           "user_alias": {
                "alias_label": "shopify_customer_id",
                "alias_name": "{{canvas_entry_properties.${shopify_customer_id}}}"
            }
      }
    }
  ]
}
```
{% endraw %}

{% alert tip %}
`merge_users` の動作については、[POSTを参照のこと：ユーザーをマージする]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge_updates-behavior).
{% endalert %}

{: start="8"}
8. ユーザーがフローを抜けるか、チェックアウトを完了すると、後続のShopifyウェブフックはメールアドレスや電話番号、またはShopifyのエイリアスを使用して照合される。

{% endtab %}
{% endtabs %}
