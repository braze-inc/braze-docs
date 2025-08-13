---
nav_title: はじめに
article_title: "Shopifyを使い始める"
description: "このリファレンス記事では、Shopify Web サイトにBraze Web SDK を実装する方法について説明します。"
page_type: partner
search_tag: Partner
alias: /getting_started_shopify_legacy/
page_order: 1
---

# Shopifyを使い始める

> この記事では、ShopifyウェブサイトにBraze Web SDKを実装する方法を概説する。実装が完了したら、「[Shopify の設定]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview)」を参照して、Braze と Shopify の統合を設定する方法を確認してください。

{% multi_lang_include alerts.md alert='Shopify deprecation' %}

## 統合設定チェックリスト

1. [Braze Web SDKを実装する](#implement-web-sdk)
2. [BrazeでShopifyをセットアップする]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview)
3. Shopifyとの統合をテストする

## ShopifyウェブサイトにWeb SDKを実装する {#implement-web-sdk}

[Braze Web SDK]({{site.baseurl}}/user_guide/getting_started/web_sdk/) は、Shopify ストアの顧客の行動を追跡するために使用される強力なツールです。Web SDK を使用すると、セッションデータを収集し、ユーザーを識別し、Web ブラウザーまたはモバイルブラウザーからユーザーの動作データを記録できます。また、ブラウザー内メッセージのようなネイティブメッセージングチャネルを利用することもできます。

Shopifyとの統合は、デフォルトで堅牢な機能を提供しているが、[Shopifyとの統合でサポートされていないイベントの]({{site.baseurl}}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/)オンサイトトラッキングを追加したり、[コンテンツカードの]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards)ようなチャネルを追加したりするユースケースがある場合は、Web SDKをShopifyサイトに直接実装する必要があることを覚えておいてほしい。

統合のオンボーディングを開始する前に、Web SDKを実装するための方法について、チームと以下の点を確認してください。

### サポートされている機能

|アイコン| 定義 
|-------------|-------------
|<i aria-hidden="true" class="fas fa-check" title="サポート"></i><span class="sr-only">対応</span> | サポートされている
|<i aria-hidden="true" class="fas fa-times" title="未対応"></i><span class="sr-only">対応</span> | サポートされていない
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

| 特徴 | Shopify ScriptTag経由のWeb SDK | theme.liquid による Web SDK 直接統合 | Shopify Hydrogenを介したWeb SDKの直接統合
|-------------|-------------|-------------|------------
| デフォルトのオンサイトトラッキング      | <i class="fas fa-check" title="サポートされている"></i> | <i class="fas fa-times" title="サポートされていない"></i> | <i class="fas fa-times" title="サポートされていない"></i>          
| キャプチャフォームのユーザーの照合 (必要なエンジニアリング作業は少ない)   | <i class="fas fa-check" title="サポートされている"></i> | <i class="fas fa-check" title="サポートされている"></i> | <i class="fas fa-times" title="サポートされていない"></i> 
| チェックアウトユーザーの照合     | <i class="fas fa-check" title="サポートされている"></i>  | <i class="fas fa-times" title="サポートされていない"></i>   | <i class="fas fa-times" title="サポートされていない"></i>                                        
| 製品の閲覧<br> 製品クリック<br> カート放棄   | <i class="fas fa-check" title="サポートされている"></i> |<i class="fas fa-check" title="サポートされている"></i> | <i class="fas fa-times" title="サポートされていない"></i> 
| 購入手続き放棄<br> 注文の作成<br> Braze 購入<br> 注文の支払い<br> 部分的に履行された注文<br> フルフィルメントが完了した注文<br> 注文のキャンセル<br> 払い戻しの作成<br> 顧客の作成と更新 | <i class="fas fa-check" title="サポートされている"></i> | <i class="fas fa-check" title="サポートされている"></i> | <i class="fas fa-check" title="サポートされている"></i>
| 歴史的埋め戻し | <i class="fas fa-check" title="サポートされている"></i>  | <i class="fas fa-check" title="サポートされている"></i>  | <i class="fas fa-check" title="サポートされている"></i>  
| カタログ同期  |<i class="fas fa-check" title="サポートされている"></i> |<i class="fas fa-check" title="サポートされている"></i>  |<i class="fas fa-check" title="サポートされている"></i>
| メールおよび SMS サブスクライバーの収集    | <i class="fas fa-check" title="サポートされている"></i>| <i class="fas fa-check" title="サポートされている"></i>  | <i class="fas fa-check" title="サポートされている"></i>     
| デフォルトのアプリ内メッセージのサポート   | <i class="fas fa-check" title="サポートされている"></i>  | <i class="fas fa-check" title="サポートされている"></i>  | <i class="fas fa-times" title="サポートされていない"></i>     
| デフォルトのコンテンツカードをサポート   | <i class="fas fa-times" title="サポートされていない"></i> | <i class="fas fa-times" title="サポートされていない"></i> | <i class="fas fa-times" title="サポートされていない"></i>   
| デフォルトのWeb プッシュのサポート     | <i class="fas fa-times" title="サポートされていない"></i> | <i class="fas fa-times" title="サポートされていない"></i> | <i class="fas fa-times" title="サポートされていない"></i>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }    

{% tabs %}
{% tab Shopify ScriptTag %}

### Shopify ScriptTagでBraze Web SDKを実装する

[ShopifyのScriptTagは](https://shopify.dev/api/admin-rest/2021-10/resources/scripttag#top)リモートJavaScriptコードで、お店のページやチェックアウトの注文状況ページに読み込まれる。ストアページがロードされると、Shopifyはサイトページにスクリプトタグをロードする必要があるかどうかをチェックする。 

Brazeをすぐに使い始めたい場合は、BrazeがBraze Web SDK用の定義済みスクリプトをShopifyストアサイトに直接ロードするオプションがある。

{% alert important %}
この統合方法では、あらかじめ定義されているBraze Web SDK のスクリプトはカスタマイズできません。
{% endalert %}

#### Shopifyとの統合の仕組み

Shopifyサイトがロードされると、Shopifyはスクリプトタグをページにロードする必要があるかどうかをチェックする。処理中に、Braze Web SDK スクリプトがストアのページまたはチェックアウトの注文ステータスページに読み込まれます。 

また、Shopify ScriptTagやアプリ内メッセージングをチャネルとして必要とする商品閲覧、商品クリック、カート放棄イベントを選択した場合は、事前に定義されたスクリプトを追加する。  

#### 有効化する方法

統合の一部としてBraze Web SDKスクリプトを自動的に有効にするには、[Shopify統合のセットアップ]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview)中に、サポートされているShopify ScriptTagイベントを選択するか、チャネルとしてアプリ内メッセージを有効にする。 

Shopifyセットアップコンポーザーから、アスタリスク(\*)で示されたイベントは、Web SDKによってサポートされている。これらのイベントを選択するか、ブラウザ内メッセージングを含めると、BrazeはShopify ScriptTag経由でWeb SDKの実装をShopifyストアにセットアップの一部として追加する。

#### Shopifyのメールキャプチャフォームとユーザー照合 

キャプチャフォームにより、顧客のライフサイクルの早期段階で、ダウンストリームのメッセージングとエンゲージメントのために特定可能な顧客情報が取得されます。 

Web SDK は `device_id` を使用して、Shopify のオンサイト行動と匿名ユーザーを追跡します。BrazeのShopify ScriptTagインテグレーションは、ニュースレター登録などのShopifyのメール取り込みフォームからのメールを、ユーザーの`device_id` 。

典型的なメール・キャプチャ・フォームには以下のようなものがある： 
- 電子メール・キャプチャ・フォーム 
- ニュースレター登録フォーム

ユーザーのメールと `device_id` を照合するには、次の2つの方法があります。 
- Braze自動メールキャプチャスクリプトを使用する 
- `setEmail` または`setPhoneNumber` メソッドを呼び出す

##### メールや電話での登録のキャプチャ

Brazeを使えば、[Eメールや]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/email_capture_form/#step-1-create-an-in-app-message-campaign) [SMS、WhatsAppの]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture)登録フォームを使って、Web SDKやアプリ内メッセージを活用できる。 

ShopifyのEメールや電話番号のキャプチャ、またはサードパーティのキャプチャフォームを使用する場合は、Braze Web SDKで追跡されるユーザーに直接設定することができる。たとえば、顧客のメールアドレスを取得した場合、そのメールアドレスを顧客のユーザープロファイルに次のように設定できます。

{% raw %}
```javascript
braze.getUser().setEmail(<email address>);
```
{% endraw %}

これらの値の設定の詳細については、以下のJavascriptリソースを参照のこと：

- ユーザーの[メール](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail)を設定する
- ユーザーの[電話番号](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setphonenumber)を設定する

次のように、ユーザーのメールまたは電話番号を収集するときに、ユーザーのサブスクリプションの状態を設定することもできます。

{% raw %}
```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.SUBSCRIBED);
```
{% endraw %}

これらの値の設定の詳細については、以下のJavascriptリソースを参照のこと：

- ユーザーの[メール通知サブスクリプションタイプ](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype)を設定する
- [サブスクリプショングループ](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup)にユーザーを追加する

**サードパーティキャプチャフォームの実装例**

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
2\.まず、スクリプトが最初に読み込まれるようにするため、`setInterval` を呼び出します。
3\.`{FORM_ID}` を、キャプチャするフォームの要素 ID に置き換えます
(「ContactFooter」など)。
4\.`{INPUT_EMAIL_ID}` 、フォーム内のEメール入力フィールドの要素IDに置き換える。
5. フォームが送信されると、スクリプトはメール入力値を使用して `setEmail` を呼び出します。
6. スクリプトが読み込まれたら、スクリプトの読み込みが1回だけであるようにするため、`clearInterval` を呼び出します。

{% alert note %}
現時点では、BrazeのメールキャプチャフォームはShopifyの顧客を作成しない。その結果、顧客がチェックアウトを通過するか、アカウントを作成するまで、Shopifyのユーザープロファイルが関連付けられていないBrazeのユーザープロファイルを持つことができる。
{% endalert %}

#### 実装後に予期されること

**Braze Web SDKの初期化**

Web SDKはセッション開始時に初期化される。Brazeは、Shopifyの顧客ID、Eメール、電話番号などの他の識別子がShopifyストアのゲスト訪問者から容易に入手できない可能性があるため、匿名ユーザーデータを追跡するために`device_id` を収集する必要がある。

また、チェックアウトプロセス後に顧客からさらに識別可能な情報 (メールアドレスや電話番号など) が提供されるため、ユーザーデータを匿名ユーザープロファイルと照合するために `device_id` が使用されます。

**Braze Web SDKバージョン**

Shopify ScriptTag統合によるBraze Web SDKの現在のバージョンはv4.2である。

**1 か月あたりのアクティブユーザー数 (MAU)**

Web SDKはShopifyの顧客やゲストのセッションを追跡する。その結果、これは Braze ダッシュボードのレポート内で MAU にカウントされ、MAU 割り当ての対象となります。匿名ユーザーも MAU にカウントされることに注意してください。モバイルデバイスの場合、匿名ユーザーはデバイスによって決まります。Web ユーザーの場合、匿名ユーザーはブラウザーのキャッシュによって決まります。

{% endtab %}

{% tab テーマリキッド %}

### WebSDKをShopifyサイトに直接実装する theme.liquid

Braze には、Web SDK を実装する方法が複数あります。
- Web SDKをShopify`theme.liquid` ファイルに直接追加する。
- Google Tag Manager 

すでにShopifyストアにWeb SDKをインストールしている場合でも、オンボーディングプロセス内でShopify ScriptTagのセットアップを進めることができる。 

インストールプロセス中、BrazeはWeb SDKのインスタンスがShopifyストアですでに利用可能かどうかをチェックする。既存の実装がある場合、Braze はWeb SDK を有効にするために事前定義スクリプトを読み取りません。その後、必要なスクリプトを追加して、選択したイベントをトラッキングできるようにしたり、ブラウザ内のメッセージングを有効にしたりする。

#### 有効化する方法

Web SDK を手動で実装するには、「[SDK の初期セットアップ]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web)」を参照してください。Google Tag Manager を使用して Web SDK を実装するには、「[Google Tag Manager for Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/google_tag_manager#google-tag-manager)」を参照してください。 

どちらの実装方法でも、Web SDK 統合に以下が含まれているか、または Shopify 統合がサポートされない予定であることを確認します。 
- Web SDKバージョン v4.0+
- セッション開始時にWeb SDKが初期化される

#### Shopifyのメールキャプチャフォームとユーザー照合 

キャプチャフォームにより、顧客のライフサイクルの早期段階で、ダウンストリームのメッセージングとエンゲージメントのために特定可能な顧客情報が取得されます。 

Web SDK は `device_id` を使用して、Shopify のオンサイト行動と匿名ユーザーを追跡します。BrazeのShopify ScriptTagインテグレーションは、ニュースレター登録などのShopifyのメール取り込みフォームからのメールを、ユーザーの`device_id` 。

典型的なメール・キャプチャ・フォームには以下のようなものがある： 
- 電子メール・キャプチャ・フォーム 
- ニュースレター登録フォーム

ユーザーのメールと `device_id` を照合するには、次の2つの方法があります。 
- Braze自動メールキャプチャスクリプトを使用する 
- `setEmail` または`setPhoneNumber` メソッドを呼び出す

##### メールや電話での登録のキャプチャ

Brazeを使えば、[Eメールや]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/email_capture_form/#step-1-create-an-in-app-message-campaign) [SMS、WhatsAppの]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture)登録フォームを使って、Web SDKやアプリ内メッセージを活用できる。 

Shopifyの電子メールや電話番号のキャプチャ、またはサードパーティのキャプチャフォームを使用する場合は、Braze Web SDKで追跡されるユーザーオブジェクトに直接設定することができる。たとえば、顧客のメールアドレスを取得した場合、そのメールアドレスを顧客のユーザープロファイルに次のように設定できます。

{% raw %}
```javascript
braze.getUser().setEmail(<email address>);
```
{% endraw %}

これらの値の設定の詳細については、以下のJavascriptリソースを参照のこと：

- ユーザーの[メール](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail)を設定する
- ユーザーの[電話番号](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setphonenumber)を設定する

次のように、ユーザーのメールまたは電話番号を収集するときに、ユーザーのサブスクリプションの状態を設定することもできます。

{% raw %}
```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.SUBSCRIBED);
```
{% endraw %}

これらの値の設定の詳細については、以下のJavascriptリソースを参照のこと：

- ユーザーの[メール通知サブスクリプションタイプ](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype)を設定する
- [サブスクリプショングループ](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup)にユーザーを追加する

**サードパーティキャプチャフォームの実装例**

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
2\.まず、スクリプトが最初に読み込まれるようにするため、`setInterval` を呼び出します。
3\.`{FORM_ID}` を、キャプチャするフォームの要素 ID に置き換えます
(「ContactFooter」など)。
4\.`{INPUT_EMAIL_ID}` 、フォーム内のEメール入力フィールドの要素IDに置き換える。
5. フォームが送信されると、スクリプトはメール入力値を使用して `setEmail` を呼び出します。
6. スクリプトが読み込まれたら、スクリプトの読み込みが1回だけであるようにするため、`clearInterval` を呼び出します。

{% alert note %}
現時点では、BrazeのメールキャプチャフォームはShopifyの顧客を作成しない。その結果、顧客がチェックアウトを通過するか、アカウントを作成するまで、Shopifyのユーザープロファイルが関連付けられていないBrazeのユーザープロファイルを持つことができる。
{% endalert %}

#### 統合後に予期されること

**Braze Web SDKの初期化**

Web SDKはセッション開始時に初期化される。Brazeは、Shopifyの顧客ID、Eメール、電話番号などの他の識別子がShopifyストアのゲスト訪問者から容易に入手できない可能性があるため、匿名ユーザーデータを追跡するために`device_id` を収集する必要がある。

また、チェックアウトプロセス中およびこのプロセスの後に顧客からさらに識別可能な情報 (メールアドレスや電話番号など) が提供されるため、ユーザーデータを匿名ユーザープロファイルと照合するために `device_id` が使用されます。

**Braze Web SDKバージョン**

Braze Web SDK の現在のバージョンは v4.0 以上である必要があります。

**1 か月あたりのアクティブユーザー数 (MAU)**

Web SDKはShopifyの顧客やゲストのセッションを追跡する。その結果、これは Braze ダッシュボードのレポート内で MAU にカウントされ、MAU 割り当ての対象となります。匿名ユーザーも MAU にカウントされることに注意してください。モバイルデバイスの場合、匿名ユーザーはデバイスによって決まります。Web ユーザーの場合、匿名ユーザーはブラウザーのキャッシュによって決まります。

{% endtab %}
{% tab ヘッドレス Shopify サイト %}

### Web SDK をヘッドレス Shopify サイトに直接実装する {#headless-site}

Braze Shopify ScriptTag 統合には、ヘッドレス Shopify サイトとの互換性があません。その結果、閲覧された商品、クリックされた商品、放棄されたカートのイベントをデフォルトでサポートしたり、あらかじめ定義されたスクリプトを使ってアプリ内メッセージを有効にしたりすることはできない。 

#### 有効化する方法

Web SDK をヘッドレス Shopify サイトに直接統合するには、「[ウェブ用SDKの初期セットアップ]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web)」を参照してください。

Web SDK 統合に以下が含まれていることを確認します。 
- Web SDK バージョンは v4.0+ である必要があります。
- セッション開始時にWeb SDKが初期化される

#### ユーザー照合のためにShopifyフォームを設定する

多くの場合、e コマースブランドは、Shopify のサイトにある自社ブランド上で、チェックアウトの前にメールキャプチャーフォームなどを使用して顧客から識別可能な情報を取得する機能を備えています。

Web SDK は、Shopify のサイト上での行動と匿名ユーザーを`device_id` で追跡する。メールアドレスが匿名ユーザープロフィールに追加されていることを確認するには、ニュースレターまたはメール収集フォームのいずれかに以下を追加する： 
- [setEmail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail) 
  - Eメール・キャプチャやニュースレターの登録
- [addAlias](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addalias) 
  - "alias_label": "shopify_email" 
  - "alias_name": "example@email.com"

ユーザーがアカウントに登録またはログインする際、外部IDで[ユーザー・プロファイルを識別]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#identified-user-profiles)したい場合がある。ユーザーが登録しログインした後、[changeUser](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser)メソッドを追加し、ユーザーがアカウントを作成したりログインした場合に外部IDを割り当てる。 

{% alert note %}
ユーザープロファイルに一時エイリアスを設定した場合は、[users/merge エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_users_merge)へのリクエストを実行して、後でユーザーを識別できます。
{% endalert %}

#### チェックアウトユーザーの照合を設定する {#headless-checkout}

放棄されたチェックアウトイベントを有効にすると、BrazeはShopifyのチェックアウト/作成ウェブフックを受信する。Brazeは、メールアドレス、電話番号、またはShopifyの顧客IDのいずれかによって、既存のユーザープロファイルとのマッチングを試みる。一致するプロファイルがない場合、Brazeはエイリアスのプロファイルを作成する。 

Shopifyウェブフックによって作成されたShopifyエイリアスユーザープロファイルと現場で追跡されたユーザプロファイルがマージされることを確認するには、以下の手順で[`/users/merge` エンドポイントを]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)使用することができる。 

{% alert tip %}
`users/merge` エンドポイントへのリクエストを含むキャンバスをトリガーするために、`theme.liquid` ファイルに対して行われる SDK または API 呼び出しでカスタムイベントをログに記録できます。これらの方法については以下で説明します。
{% endalert %}

顧客がShopifyサイトを訪問すると、すぐに匿名ユーザーが作成される。このユーザーには自動的にBraze`device_id` が割り当てられる。 

1. 新しいセッションで、サイト訪問者に一意の[ユーザーエイリアス]({{site.baseurl}}/api/objects_filters/user_alias_object#user-alias-object-specification)をランダムに割り当てます。

2. ユーザーがサイト上でアクションを実行すると、[カスタム・イベントとして]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=web)ログに記録するか、[ユーザー属性をキャプチャする]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=web)。ユーザーがチェックアウトに進み、ShopifyのフォームにEメールを入力すると、Shopifyの顧客IDが作成される。Brazeは、Shopifyのウェブフックを処理し、Eメール、電話、Shopifyのエイリアスが既存のユーザーと一致しない場合は、新しいユーザープロファイルを作成する。

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
3\.ユーザープロファイルの重複を防ぐには、Braze`device_id` を含むユーザープロファイルとShopifyエイリアスプロファイルを含むユーザープロファイルをマージする必要がある。遅延を設定し、`do_not_merge` 属性を使用してユーザーを更新し、[`/users/merge` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) へのリクエストを行う API トリガーキャンバスを作成できます。また、`merge_user` のようなカスタム・イベントを記録して、キャンバスをトリガーすることもできる。 


{% endsubtab %}
{% subtab Non-API approach %}

{: start="3"}
3\.ユーザーがフローを終了するか、チェックアウトを完了すると、`merge_user` のようなカスタムイベントをログに記録して、遅延を設定するCanvasをトリガーし、`do_not_merge` 属性でユーザーを更新し、[`/users/merge` エンドポイントに]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)リクエストすることができる。

{% endsubtab %}
{% endsubtabs %}

{: start="4"}
4\.キャンバスのエントリ条件で、識別されていないユーザープロファイルのみをターゲットにします。つまり、external ID がなく、`do_not_merge` は真ではありません。<br><br>![Canvas 作成画面で `do_not_merge` をフィルターとして使用している「エントリオーディエンス」ステップ。]({% image_buster /assets/img/Shopify/shop_usermerge_canvas_entrycriteria.png %})

{: start="5"}
5. キャンバスの入力条件を設定したら、キャンバスフローを作成する。キャンバスの最初のステップを**Delay**ステップにして、処理中に起こりうるレースコンディションを防ぐ。<br><br>![キャンバス作成画面の「遅延」ステップ。]({% image_buster /assets/img/Shopify/shop_usermerge_canvas_delay.png %})

{: start="6"}
6. これらのユーザーは次のステップでマージされるため、[**ユーザー更新**] ステップを作成して、`do_not_merge` カスタム属性を「true」に更新できます。<br><br>![`do_not_merge` が属性として選択されているキャンバス作成画面の「ユーザー更新」ステップ。]({% image_buster /assets/img/Shopify/shop_usermerge_canvas_userupdate.png %})

{: start="7"}
7. 次に、ウェブフックを使って**メッセージ・**ステップを作成する。<br><br>![Webhook メッセージングチャネルが使用されているキャンバス作成画面の「メッセージ」ステップ。]({% image_buster /assets/img/Shopify/shop_usermerge_canvas_webhook.png %}) 

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
`merge_users` の動作については、[POSTを参照のこと：ユーザーをマージする]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge_updates-behavior)」を参照してください。
{% endalert %}

{: start="8"}
8. ユーザーがフローを抜けるか、チェックアウトを完了すると、後続のShopifyウェブフックはメールアドレスや電話番号、またはShopifyのエイリアスを使用して照合される。

{% endtab %}
{% endtabs %}
