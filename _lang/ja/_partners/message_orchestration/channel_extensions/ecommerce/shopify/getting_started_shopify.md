---
nav_title: はじめに
article_title:「Shopifyを使い始める」
description:「この参考記事では、Braze Web SDKをShopifyWeb サイト実装する方法の概要を説明しています。「
page_type: partner
search_tag:Partner
alias: /getting_started_shopify/
page_order:1
---

# Shopifyを使い始める

> この記事では、Braze Web SDKをShopifyWeb サイト実装する方法を概説します。実装後、[ShopifyとBrazeの統合の設定を完了する方法については]({{site.baseurl}}//partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify)、「Shopifyの設定」を参照してください。

## 統合設定チェックリスト

1. [Braze Web SDK を実装する](#implement-web-sdk)
2. [Braze でShopifyをセットアップする]({{site.baseurl}}//partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify)
3. Shopifyインテグレーションをテストする

## ShopifyWeb サイトへのWeb SDKの実装 {#implement-web-sdk}

[Braze Web SDKは]({{site.baseurl}}/user_guide/onboarding_with_braze/web_sdk/)、Shopifyストアのお客様の行動を追跡するために使用される強力なツールです。Web SDKを使用すると、セッションデータを収集し、ユーザーを識別し、Webまたはモバイルブラウザーからユーザー行動データを記録できます。ブラウザ内メッセージなどのネイティブメッセージングチャネルのロックを解除することもできます。

Shopifyインテグレーションには強力なデフォルト機能が用意されていますが、[Shopifyインテグレーションでサポートされていないイベントのオンサイトトラッキング, 追跡を追加するユースケースがある場合や、[コンテンツカードなどのチャネルを追加したい場合は]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards)、Web SDKをShopifyサイトに直接実装する必要があることに注意してください]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_data_in_braze/)。

統合のオンボーディングを始める前に、Web SDKを実装するためにどのパスを進むべきかについて、チームと以下を確認してください。

### サポートされている機能

|アイコン| 定義 
|-------------|-------------
|<i aria-hidden="true" class="fas fa-check" title="サポート対象"></i> | サポート対象
|<i aria-hidden="true" class="fas fa-times" title="サポート対象外サポート対象"></i> | サポートされていません
{: .reset-td-br-1 .reset-td-br-2} 

| 特徴 | Shopify スクリプトタグ経由のWeb SDK | テーマ.liquidによるウェブ SDK のダイレクトインテグレーション | Shopify Hydrogenによるウェブ SDK の直接統合
|-------------|-------------|-------------|------------
| デフォルトのオンサイトトラッキング, 追跡      | <i class="fas fa-check" title="サポート対象"></i> | <i class="fas fa-times" title="サポートされていません"></i> | <i class="fas fa-times" title="サポートされていません"></i>          
| ユーザー照合フォームをキャプチャ (開発の労力が少なくて済む)   | <i class="fas fa-check" title="サポート対象"></i> | <i class="fas fa-check" title="サポート対象"></i> | <i class="fas fa-times" title="サポートされていません"></i> 
| チェックアウトユーザー調整     | <i class="fas fa-check" title="サポート対象"></i>  | <i class="fas fa-check" title="サポート対象"></i>   | <i class="fas fa-times" title="サポートされていません"></i>                                        
| 閲覧した商品<br> 商品がクリックされました<br> 放棄されたカート   | <i class="fas fa-check" title="サポート対象"></i> |<i class="fas fa-check" title="サポート対象"></i> | <i class="fas fa-times" title="サポートされていません"></i> 
| チェックアウト放棄<br> 注文を作成しました<br> Braze 購入<br> 注文は支払われました<br> 一部出荷された注文<br> 出荷済みの注文<br> キャンセルされた注文<br> 払い戻しを作成しました<br> お客様による作成と更新 | <i class="fas fa-check" title="サポート対象"></i> | <i class="fas fa-check" title="サポート対象"></i> | <i class="fas fa-check" title="サポート対象"></i>
| ヒストリカル・バックフィル | <i class="fas fa-check" title="サポート対象"></i>  | <i class="fas fa-check" title="サポート対象"></i>  | <i class="fas fa-check" title="サポート対象"></i>  
| カタログ同期  |<i class="fas fa-check" title="サポート対象"></i> |<i class="fas fa-check" title="サポート対象"></i>  |<i class="fas fa-check" title="サポート対象"></i>
| E メールと SMS サブスクライバー収集    | <i class="fas fa-check" title="サポート対象"></i>| <i class="fas fa-check" title="サポート対象"></i>  | <i class="fas fa-check" title="サポート対象"></i>     
| デフォルトのアプリ内メッセージサポート   | <i class="fas fa-check" title="サポート対象"></i>  | <i class="fas fa-check" title="サポート対象"></i>  | <i class="fas fa-times" title="サポートされていません"></i>     
| デフォルトコンテンツカードのサポート   | <i class="fas fa-times" title="サポートされていません"></i> | <i class="fas fa-times" title="サポートされていません"></i> | <i class="fas fa-times" title="サポートされていません"></i>   
| デフォルトWeb プッシュサポート     | <i class="fas fa-times" title="サポートされていません"></i> | <i class="fas fa-times" title="サポートされていません"></i> | <i class="fas fa-times" title="サポートされていません"></i>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}    

{% tabs %}
{% tab Shopify ScriptTag %}

### Shopify スクリプトタグによる Braze Web SDK の実装

[Shopify ScriptTagは](https://shopify.dev/api/admin-rest/2021-10/resources/scripttag#top)、ストアのページまたはチェックアウトの注文ステータスページに読み込まれるリモートJavaScriptコードです。ストアページが読み込まれると、Shopifyはサイトページにスクリプトタグを読み込む必要があるかどうかを確認します。 

Brazeをすぐに使い始めたい場合は、BrazeがBraze Web SDK用の定義済みスクリプトをShopifyストアサイトに直接読み込むことを許可するオプションがあります。

{% alert important %}
この統合方法用の Braze Web SDK の事前定義済みスクリプトはカスタマイズできません。
{% endalert %}

#### Shopifyインテグレーションとの連携の仕組み

Shopifyサイトが読み込まれると、Shopifyはページにスクリプトタグを読み込む必要があるかどうかを確認します。処理中に、Braze Web SDKスクリプトがストアのページまたはチェックアウトの注文ステータスページに読み込まれます。 

また、チャネルとしてShopify ScriptTagまたはアプリ内メッセージングを必要とする商品の閲覧、クリックされた商品、放棄カート or カート放棄のイベントを選択した場合は、定義済みのスクリプトも追加されます。  

#### 有効にする方法

[統合の一環としてBraze Web SDKスクリプトを自動的に有効にするには、サポートされているShopify ScriptTagイベントを選択するか、Shopify統合の設定時にチャネルとしてアプリ内メッセージングを有効にします。]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/) 

Shopifyの設定ウィザードから、アスタリスク (\*) で示されたイベントはWeb SDKでサポートされています。これらのイベントを選択するか、ブラウザ内メッセージングを含めると、Brazeは設定の一部としてShopify ScriptTagを介したWeb SDK実装をShopifyストアに追加します。

#### Shopify メールキャプチャフォームとユーザー調整 

キャプチャフォームは、顧客のライフサイクルの早い段階で識別可能な顧客情報を取得し、ダウンストリームのメッセージングとエンゲージメントに役立てます。 

Web SDKは、を使用してShopifyのオンサイト行動と匿名ユーザーを追跡します。`device_id`Braze Shopify ScriptTagインテグレーションは、ニュースレターの登録などのShopifyメールキャプチャフォームからのメールをユーザーのメールに割り当てます。`device_id`

一般的なメール・キャプチャ・フォームには次のものがあります。 
- アカウントログインページ 
- アカウント登録ページ 
- メールキャプチャフォーム 
- ニュースレター登録フォーム

ユーザーのメールを照合する方法と、次の 2 つの方法があります。`device_id` 
- Braze 自動メールキャプチャスクリプトを使用する 
- Braze `reconcileEmail()` スクリプトに独自の呼び出しを追加します。

##### 自動メールキャプチャスクリプト (早期アクセス)

自動メールキャプチャスクリプトは、顧客メール入力をユーザーのメール入力と照合します。`device_id`正しく動作するにはいくつかの要件があります。

- 顧客電子メールを入力するテキストボックスは、「メール」という名前のフォームHTML要素の下の入力HTML要素でなければなりません。
- メールは、Web サービスではなく、HTML フォーム送信を通じて入力する必要があります。
- すべてのメール入力フィールドは、顧客自分のメールアドレスを入力するために使用する必要があります。そうしないと、間違ったメールが割り当てられる可能性があります`device_id`。たとえば、友人や家族への紹介メールは、誤って顧客のメールとして扱われ、Brazeユーザープロファイルで更新されます。

{% alert important %}
自動メールキャプチャスクリプトは、現在早期アクセス中です。この早期アクセスへ参加することに興味がある場合は、カスタマーサクセスマネージャーにお問い合わせください。<br><br> インテグレーションがすでにインストールされている場合は、アクティベーションを完了するためにこの時点で再インストールする必要があります。
{% endalert %}

##### 通話照合メール ()

ShopifyストアフロントWeb サイトに電話を追加すると、顧客メールを割り当てるためにどの入力フィールドを使用するかを正確にコントロールできます。`reconcileEmail()` `device_id`ストアフロントが自動メールキャプチャスクリプトの要件を満たしていない場合は、この方法を使用することをお勧めします。

`reconcileEmail``theme.liquid`メソッドをShopifyコードに実装する方法の例は次のとおりです。 

**アカウントと登録**

1. ユーザー Shopifyにログインすると、顧客オブジェクトが定義されます。`theme.liquid`ファイルに、次のスニペットを追加します。`head tag`

{% raw %}
```javascript
   <script>
      const customerPoller = setInterval(()=>{
        {% if customer %}
          reconcileEmail("{{customer.email}}");
        {% endif %}{}
        clearInterval(customerPoller)
      }, 2000)
    </script>
```
{% endraw %}

{: start="2"}
2\.まず、BrazesDK `setInterval` が最初に読み込まれるように呼び出します。
3\.Liquidを使用して、顧客オブジェクトがページに設定されているかどうかを確認します
4\.顧客いる場合は、電話します `reconcileEmail`
5. Liquidフォームでメールの値を取得します `customer.email`
6. スクリプトがロードされたら、`clearInterval`一度だけロードされるように呼び出します。
7. コンソールをチェックして、メールが調整されたことを確認できます。

**ニュースレターとメールキャプチャフォーム**

1. で`theme.liquid`、次のスニペットをにコピーします。`head tag`

{% raw %}
```javascript
    <script>
         const emailInputPoller = setInterval(()=>{
      if (document.getElementById('{FORM_ID}')) {
        document.getElementById('{FORM_ID}').addEventListener("submit",
          function() {  
            var email = document.getElementById('{INPUT_EMAIL_ID}').value
            reconcileEmail(email)
          }
        );
      }
      clearInterval(emailInputPoller)
        }, 2000)
    </script>
```
{% endraw %}

{: start="2"}
2\.`setInterval`最初に呼び出して、スクリプトが最初に読み込まれるようにします。
3\.キャプチャしたいフォームの要素 ID `{FORM_ID}` に置き換えます
(「連絡先フッター」など)
4\.フォーム内のメール入力フィールド要素 ID `{INPUT_EMAIL_ID}` に置き換えます
5. フォームが送信されると、スクリプトはメール`reconcileEmail`の入力値で呼び出されます
6. スクリプトがロードされたら、`clearInterval`一度だけロードされるように呼び出します。
7. コンソールをチェックして、メールが調整されたことを確認できます。

{% alert note %}
現時点では、BrazeのメールキャプチャフォームではShopifyの顧客を作成できません。その結果、顧客チェックアウトを行うかアカウントを作成するまで、Shopifyユーザープロファイルが関連付けられていないBrazeユーザープロファイルが残っている可能性があります。
{% endalert %}

#### 導入後に期待できること

**Braze Web SDK 初期化**

Web SDK はセッション開始時に初期化されます。Shopifyの顧客 ID、電子メール、電話番号などの他の識別子は、Shopifyストアのゲスト訪問者がすぐに利用できない可能性があるため、Brazeは匿名ユーザーデータトラッキング, 追跡するために情報を収集する必要があります。`device_id`

また`device_id`、チェックアウトプロセス中およびチェックアウト後に顧客識別可能な情報（メールアドレスや電話番号など）を提供したときに、ユーザーデータ匿名ユーザープロファイルに照合するためにも使用されます。

**Braze Web SDK バージョン**

Shopify ScriptTag統合によるBraze Web SDK 現在のバージョンはv4.2です。

**1 か月あたりのアクティブユーザー数 (MAU)**

Web SDKは、Shopifyのお客様とゲストのセッションを追跡します。その結果、これはBrazeダッシュボードのレポートにMAUとして加算され、MAUの割り当てに充てられます。匿名ユーザーもMAUにカウントされることに注意してください。モバイルデバイスの場合、匿名ユーザーはデバイスによって決まります。Web ユーザーの場合、匿名ユーザーはブラウザーのキャッシュによって決まります。

{% endtab %}

{% tab theme.liquid %}

### Web SDKをShopifyサイトのテーマに直接実装します。リキッド

Braze では、次のような複数の方法で Web SDK を実装できます。
- Web `theme.liquid` SDKをShopifyファイルに直接追加する
- Google Tag Manager 

Web SDKがShopifyストアに既にインストールされている場合でも、オンボーディングプロセスでShopify スクリプトタグ設定に進むことができます。 

インストールプロセス中に、BrazeはWeb SDK インスタンスがShopifyストアですでに利用可能かどうかを確認します。既存の実装がある場合、Braze は Web SDK を有効にするための定義済みスクリプトを読み込むしません。次に、必要なスクリプトを追加して、選択したイベントを追跡したり、ブラウザ内メッセージングを有効にしたりできるようにします。

#### 有効にする方法

Web SDK を手動で実装するには、「[初期 SDK セットアップ」を参照してください]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/)。Google タグマネージャーを使用して Web SDK を実装するには、[ウェブ用 Google タグマネージャーをご覧ください]({{site.baseurl}}/developer_guide/platform_integration_guides/web/google_tag_manager#google-tag-manager)。 

どちらの実装方法でも、Web SDK統合に以下が含まれていることを確認してください。含まれていない場合、Shopify統合はサポートされません。 
- v4.0以降のWeb SDK バージョン
- Web SDK はセッション開始時に初期化されます

#### Shopify メールキャプチャフォームとユーザー調整 

キャプチャフォームは、顧客のライフサイクルの早い段階で識別可能な顧客情報を取得し、ダウンストリームのメッセージングとエンゲージメントに役立てます。 

Web SDKは、を使用してShopifyのオンサイト行動と匿名ユーザーを追跡します。`device_id`Braze Shopify ScriptTagインテグレーションは、ニュースレターの登録などのShopifyメールキャプチャフォームからのメールをユーザーのメールに割り当てます。`device_id`

一般的なメール・キャプチャ・フォームには次のものがあります。 
- アカウントログインページ 
- アカウント登録ページ 
- メールキャプチャフォーム 
- ニュースレター登録フォーム

ユーザーのメールを照合する方法と、次の 2 つの方法があります。`device_id` 
- Braze 自動メールキャプチャスクリプトを使用する 
- Braze `reconcileEmail()` スクリプトに独自の呼び出しを追加します。

##### 自動メールキャプチャスクリプト (早期アクセス)

自動メールキャプチャスクリプトは、顧客メール入力をユーザーのメール入力と照合します。`device_id`正しく動作するにはいくつかの要件があります。

- 顧客電子メールを入力するテキストボックスは、「メール」という名前のフォームHTML要素の下の入力HTML要素でなければなりません。
- メールは、Web サービスではなく、HTML フォーム送信を通じて入力する必要があります。
- すべてのメール入力フィールドは、顧客自分のメールアドレスを入力するために使用する必要があります。そうしないと、間違ったメールが割り当てられる可能性があります`device_id`。たとえば、友人や家族への紹介メールは、誤って顧客のメールとして扱われ、Brazeユーザープロファイルで更新されます。

{% alert important %}
自動メールキャプチャスクリプトは、現在早期アクセス中です。この早期アクセスへ参加することに興味がある場合は、カスタマーサクセスマネージャーにお問い合わせください。<br><br> インテグレーションがすでにインストールされている場合は、アクティベーションを完了するためにこの時点で再インストールする必要があります。
{% endalert %}

##### 通話照合メール ()

ShopifyストアフロントWeb サイトに電話を追加すると、顧客メールを割り当てるためにどの入力フィールドを使用するかを正確にコントロールできます。`reconcileEmail()` `device_id`ストアフロントが自動メールキャプチャスクリプトの要件を満たしていない場合は、この方法を使用することをお勧めします。

`reconcileEmail``theme.liquid`メソッドをShopifyコードに実装する方法の例は次のとおりです。 

**アカウントと登録**

1. ユーザー Shopifyにログインすると、顧客オブジェクトが定義されます。`theme.liquid`ファイルに、次のスニペットを追加します。`head tag`

{% raw %}
```javascript
   <script>
      const customerPoller = setInterval(()=>{
        {% if customer %}
          reconcileEmail("{{customer.email}}");
        {% endif %}{}
        clearInterval(customerPoller)
      }, 2000)
    </script>
```
{% endraw %}

{: start="2"}
2\.まず、BrazesDK `setInterval` が最初に読み込まれるように呼び出します。
3\.Liquidを使用して、顧客オブジェクトがページに設定されているかどうかを確認します
4\.顧客いる場合は、電話します `reconcileEmail`
5. Liquidフォームでメールの値を取得します `customer.email`
6. スクリプトがロードされたら、`clearInterval`一度だけロードされるように呼び出します。
7. コンソールをチェックして、メールが調整されたことを確認できます。

**ニュースレターとメールキャプチャフォーム**

1. で`theme.liquid`、次のスニペットをにコピーします。`head tag`

{% raw %}
```javascript
    <script>
         const emailInputPoller = setInterval(()=>{
      if (document.getElementById('{FORM_ID}')) {
        document.getElementById('{FORM_ID}').addEventListener("submit",
          function() {  
            var email = document.getElementById('{INPUT_EMAIL_ID}').value
            reconcileEmail(email)
          }
        );
      }
      clearInterval(emailInputPoller)
        }, 2000)
    </script>
```
{% endraw %}

{: start="2"}
2\.`setInterval`最初に呼び出して、スクリプトが最初に読み込まれるようにします。
3\.キャプチャしたいフォームの要素 ID `{FORM_ID}` に置き換えます
(「連絡先フッター」など)
4\.フォーム内のメール入力フィールド要素 ID `{INPUT_EMAIL_ID}` に置き換えます
5. フォームが送信されると、スクリプトはメール`reconcileEmail`の入力値で呼び出されます
6. スクリプトがロードされたら、`clearInterval`一度だけロードされるように呼び出します。
7. コンソールをチェックして、メールが調整されたことを確認できます。

{% alert note %}
現時点では、BrazeのメールキャプチャフォームではShopifyの顧客を作成できません。その結果、顧客チェックアウトを行うかアカウントを作成するまで、Shopifyユーザープロファイルが関連付けられていないBrazeユーザープロファイルが残っている可能性があります。
{% endalert %}

#### 統合後に期待できること

**Braze Web SDK 初期化**

Web SDK はセッション開始時に初期化されます。Shopifyの顧客 ID、電子メール、電話番号などの他の識別子は、Shopifyストアのゲスト訪問者がすぐに利用できない可能性があるため、Brazeは匿名ユーザーデータトラッキング, 追跡するために情報を収集する必要があります。`device_id`

また`device_id`、チェックアウトプロセス中およびチェックアウト後に顧客識別可能な情報（メールや電話番号など）を提供したときに、ユーザーデータ匿名ユーザープロファイルに照合するためにも使用されます。

**Braze Web SDK バージョン**

Braze Web SDK の現在のバージョンは v4.0 以降である必要があります。

**1 か月あたりのアクティブユーザー数 (MAU)**

Web SDKは、Shopifyのお客様とゲストのセッションを追跡します。その結果、これはBrazeダッシュボードのレポートにMAUとして加算され、MAUの割り当てに充てられます。匿名ユーザーもMAUにカウントされることに注意してください。モバイルデバイスの場合、匿名ユーザーはデバイスによって決まります。Web ユーザーの場合、匿名ユーザーはブラウザーのキャッシュによって決まります。

{% endtab %}
{% tab Headless Shopify site %}

### Web SDKをヘッドレスShopifyサイトに直接実装する {#headless-site}

Braze Shopify ScriptTag インテグレーションは、ヘッドレスのShopifyサイトと互換性がありません。その結果、商品の閲覧、商品のクリック、放棄カート or カート放棄のイベントに対するデフォルトサポートを受けることも、事前定義済みのスクリプトを使用してアプリ内メッセージングを有効にすることもできなくなります。 

#### 有効にする方法

Web SDKをヘッドレスShopifyサイトに直接統合するには、「Web [用の初期SDKセットアップ]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/)」を参照してください。

Web SDK インテグレーションに以下が含まれていることを確認してください。 
- Web SDK のバージョンは v4.0 以降である必要があります
- Web SDK はセッション開始時に初期化されます

#### ユーザー調整のためのShopifyフォームの設定

Eコマースブランドは、Shopifyサイトで、メールキャプチャフォームなど、チェックアウト前に顧客から識別可能な情報を取得する経験があるでしょう。

Web SDKは、を使用してShopifyのオンサイト行動と匿名ユーザーを追跡します。`device_id`匿名ユーザープロファイルファイルにメールアドレスが追加されたことを確認するには、ニュースレターまたはメールキャプチャフォームに以下を追加します。 
- [Eメールを設定](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail) 
  - メールキャプチャまたはニュースレターの登録用
- [エイリアスを追加](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addalias) 
  - 「エイリアスラベル」:「ショップメール」 
  - 「エイリアス名」: "」example@email.com

ユーザーがアカウントを登録またはログインするときに、[ユーザープロファイル外部 ID で識別したい場合があります]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#identified-user-profiles)。ユーザー登録してログインしたら、[changeUser](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser) メソッドを追加して、ユーザーがアカウントを作成したりログインしたりした場合に外部 ID を割り当てます。 

{% alert note %}
ユーザープロファイル一時的なエイリアスを設定すると、[後でユーザーを識別するようにユーザー/マージエンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_users_merge)にリクエストを送信できます。
{% endalert %}

#### チェックアウトユーザー調整の設定 {#headless-checkout}

チェックアウト放棄イベントを有効にすると、BrazeはShopifyのチェックアウトを受け取る/Webhook を作成します。Brazeは、メールアドレス、電話番号、またはShopifyの顧客 IDのいずれかを使用して、既存のユーザープロファイルとの照合を試みます。一致するものがない場合、Braze はエイリアスプロファイル作成します。 

[オンサイトで追跡されたユーザープロファイルが、Shopify webhook によって作成されたShopifyエイリアスのユーザープロファイルと確実に統合されるようにするには、以下の手順に従ってエンドポイントを使用できます。`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) 

{% alert tip %}
`theme.liquid`ファイルに対して行われたSDKまたはAPI呼び出しを介してカスタムイベントログに記録し、`users/merge`エンドポイントへのリクエストを含むCanvasをトリガーできます。これらの方法の概要を以下に示します。
{% endalert %}

顧客 Shopifyサイトにアクセスするとすぐに、匿名ユーザー作成されます。このユーザーには自動的に Braze `device_id` が割り当てられます。 

1. 新しいセッション時に、[サイト訪問者に固有のユーザーエイリアスをランダムに割り当てます]({{site.baseurl}}/api/objects_filters/user_alias_object#user-alias-object-specification)。

2. ユーザーがサイトでアクションを実行すると、[それをカスタムイベントとして記録するか]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events)、[ユーザー属性を取得します]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_custom_attributes/)。ユーザーチェックアウトに進み、Shopifyフォームにメールを入力すると、Shopifyの顧客 IDが作成されます。メール、電話、またはShopifyエイリアスが既存のユーザーと一致しない場合、BrazeはShopify webhook を処理し、新しいユーザープロファイルを作成します。

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
3\.ユーザープロファイルの重複を防ぐには、`device_id` Brazeを含むユーザープロファイルとShopifyエイリアスプロファイルを含むユーザープロファイルを統合する必要があります。[遅延を設定したり、`do_not_merge`属性でユーザー更新したり、エンドポイントにリクエストを送信したりする API トリガーキャンバスを作成できます。`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)`merge_user`Canvasをトリガーするようなカスタムイベントログに記録することもできます。 


{% endsubtab %}
{% subtab Non-API approach %}

{: start="3"}
3\.ユーザーがフローを終了したりチェックアウトを完了したりすると、キャンバスをトリガーして遅延を設定し`merge_user`、`do_not_merge`属性でユーザー更新し、[`/users/merge`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)にリクエストを送信するなどのカスタムイベントログに記録できます。

{% endsubtab %}
{% endsubtabs %}

{: start="4"}
4\.Canvasのエントリ条件では、正体不明のユーザープロファイルのみをターゲットにします。つまり、そのユーザーには外部IDがなく、`do_not_merge`そうではないということです。<br><br>![The "Entry Audience" step in the Canvas composer with `do_not_merge` as a filter.]({% image_buster /assets/img/Shopify/shop_usermerge_canvas_entrycriteria.png %})

{: start="5"}
5. キャンバスのエントリ条件を設定したら、キャンバスフローを作成できます。Canvas の最初のステップを **Delay** ステップにして、処理中に発生する可能性のある競合状態を防止します。<br><br>![Delay step in the Canvas composer.]({% image_buster /assets/img/Shopify/shop_usermerge_canvas_delay.png %})

{: start="6"}
6. **これらのユーザーは次のステップで統合されるため**、`do_not_merge`ユーザー更新ステップを作成してカスタム属性を「true」に更新できます。<br><br>![User update step in the Canvas composer with `do_not_merge` selected as an attribute.]({% image_buster /assets/img/Shopify/shop_usermerge_canvas_userupdate.png %})

{: start="7"}
7. 次に、Webhook **を使用してメッセージステップを作成します**。<br><br>![Message step in the Canvas composer with a Webhook messaging channel.]({% image_buster /assets/img/Shopify/shop_usermerge_canvas_webhook.png %}) 

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
`merge_users`動作について詳しくは、「[POST:ユーザーの結合]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge_updates-behavior)」を参照してください。
{% endalert %}

{: start="8"}
8. ユーザーがフローを終了するかチェックアウトを完了すると、それ以降のShopify webhook は、メールまたは電話番号、またはShopifyエイリアスを使用して照合されます。

{% endtab %}
{% endtabs %}
