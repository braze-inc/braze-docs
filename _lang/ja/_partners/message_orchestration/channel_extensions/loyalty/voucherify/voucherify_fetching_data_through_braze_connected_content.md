---
nav_title: Fetching data through Connected Content
article_title:Voucherifyでコネクテッドコンテンツからデータを取得する
page_order:2
alias: /partners/voucherify/connected_content/
description:"この参考記事では、Brazeコネクテッドコンテンツを通じてVoucherify APIからデータを取得し、特定のBrazeセグメンテーションにメッセージを送信する方法を概説している。"
page_type: partner
search_tag:Partner
---

# コネクテッド・コンテンツを通じてデータを取得する

> コネクテッドコンテンツを使えば、Voucherify APIからデータを取得し、特定のBrazeセグメンテーションにメッセージを送ることができる。この参考記事では、Voucherifyクーポンの発行、新しい紹介者の招待、ロイヤルティカード残高の取得などを行うコネクテッドコンテンツスクリプトの設定方法を紹介する。

スクリプトの基本スキーマは以下のようになる：
{% raw %}
```json
{% connected content
  "voucherify-API-ENDPOINT-url"
  :method post
  :headers {
    "X-App-Id": "Voucherify-API-key",
    "X-App-Token": "Voucherify-Secret-key",
  }
  :content_type application/json
  :retry
  :save {{result_variable}}
}
```
{% endraw %}

Voucherify[GitHubリポジトリで](https://github.com/voucherifyio/braze-connected-content)コネクテッド・コンテンツ・スクリプトの例を見ることができる。

## セキュリティ設定

以下の設定を行わないと、コネクテッドコンテンツメッセージがトリガーされるたびに、Voucherify APIが少なくとも2回呼び出される。これらの設定は、Brazeに請求されるAPIコールの数を減らし、メッセージ配信が壊れる可能性のあるハードブロッキングAPI制限にぶつかるリスクを減らす。

{% tabs %}
{% tab Rate Limiter %}

**レート制限器**

Brazeが1分間に送信する[メッセージ数を制限]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting)するようにする。これにより、BrazeとVoucherify両方のAPIは、キャンペーンからのトラフィックが多すぎることを防ぐことができる。キャンペーン設定中にユーザーをターゲットにする場合、送信レートを1分あたり500メッセージに制限する。

![\]({% image_buster /assets/img/voucherify/voucherify_cc_limiter.png %})

{% endtab %}
{% tab Caching %}

**POSTコールのキャッシュ**

HTTP POSTによるコネクテッド・コンテンツの呼び出しはデフォルトではキャッシュされず、各公開コードごとに2回のAPIリクエストを行う。この動作はAPIの限界に負担をかける可能性がある。キャッシング・メカニズムによって、バウチャーの発行ごとにAPIコールを1回に制限することができる。 

{% alert important %}
このチュートリアルのコネクテッドコンテンツのすべての例には、BrazeによってトリガーされるAPIコールの数を減らすためのデフォルトのキャッシュが含まれている。
{% endalert %}

POST呼び出しにキャッシュを追加する：

1. {% raw %}`:cache_max_age`{% endraw %} 属性を追加する。デフォルトでは、キャッシュ時間は5分である。持続時間は秒単位でカスタマイズできる。5分から4時間の間で設定できる。Example: {% raw %}`:cache_max_age 3600`{% endraw %} は1時間キャッシュされる。
2. Brazeが一意のパブリケーションを識別できるように、送信先エンドポイントクエリパラメータにキャッシュキー{% raw %}`cache_id={{cache_id}}`{% endraw %} 。まず、変数を定義し、ユニークなクエリー文字列をエンドポイントに追加する。これにより、各出版物は{% raw %}`source_id`{% endraw %} によって区別される。

![\]({% image_buster /assets/img/voucherify/voucherify_cc_cache.png %})

_その結果に注目してほしい：_Brazeは、URLに基づいてAPIコールをキャッシュする。クエリーパラメーターとして使用されるユニークな文字列は、Voucherifyでは無視されるが、Brazeに対する異なるAPIリクエストを区別し、各ユニークな試みを個別にキャッシュすることができる。このクエリーパラメーターがないと、すべての顧客がキャッシュ期間中、同じクーポンコードを受け取ることになる。

{% endtab %}
{% tab Retry attribute %}

**リトライ属性**

コネクテッド・コンテンツはVoucherifyレスポンスを検証しないので、コネクテッド・コンテンツ・スクリプトに[リトライ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries)属性を追加することを追加で推奨する。コネクテッドコンテンツロジックは、メッセージを中止する前に5回リトライを試みる（レート制限を尊重する）。この方法は、Voucherifyからデータを取得するのに少し時間がかかる場合に、コード発行に失敗するケースを防ぐのに役立つ。

{% raw %}`:retry`{% endraw %} を使用しない場合、Voucherifyから返されるレスポンシブに関係なく、Brazeは配信を送信しようとするため、公開コードのないメールが生成される可能性がある。

![\]({% image_buster /assets/img/voucherify/voucherify_cc_retry.png %})

{% endtab %}
{% tab Unique publications %}

**顧客ごとのユニークな出版物**

スクリプト本体の{% raw %}`source_id`{% endraw %} パラメータは、各顧客が1つのBrazeキャンペーンで一意のコードのみを受け取ることができることを提供する。その結果、Brazeが意図せずリクエストを多重化してしまったとしても、各ユーザーは最初のメッセージで公開されたのと同じ固有のコードを受け取ることになる。

![\]({% image_buster /assets/img/voucherify/voucherify_cc_sourceId_unique_publication.png %})

以下の設定により、{% raw %}`{{source_id}}`{% endraw %} 、出版物への影響を変更することができる：

| 構成 | 効果 |
| ------------- | ------ |
| {% raw %}`{{campaign.${dispatch_id}}}`{% endraw %} | 1回の発送に含まれる顧客は、同じ出版物を使用する。 |
| {% raw %}`{{campaign.${api_id}}}`{% endraw %} | 1つのキャンペーン内の顧客はすべて同じ出版物を使用する。 |
| {% raw %}`{{${user_id}}}`{% endraw %} または {% raw %}`{{${braze_id}}}`{% endraw %} | どのキャンペーンが送信されても、すべての顧客が同じパブリケーションを使用することを確認する（{% raw %}`external_id`{% endraw %} である{% raw %}`${user_id}`{% endraw %} と、内部 ID である{% raw %}`${braze_id}`{% endraw %} を使用できる）。 |
| {% raw %}`{{campaign.${dispatch_id}}}`{% endraw %} そして {% raw %}`{{campaign.${user_id}}}`{% endraw %} | 1つの送信に含まれる各顧客は、同じ一意の出版物を使用する。 |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Join-once %}

**ジョイン・ワンス**

Voucherifyキャンペーンに_顧客が一度しか参加_できない制限がある場合、スクリプト本体から発行元IDを削除する。Voucherifyは、同じ顧客への各Brazeメッセージが、最初に公開された同じコードを配信することを確認する。

![\]({% image_buster /assets/img/voucherify/voucherify_cc_join_once.png %}){: style="max-width:50%;"}

コネクテッド・コンテンツのスクリプトは以下のようにする：

{% raw %}

```liquid
{% assign braze_campaign_id = {{campaign.${api_id}}} %}
{% assign customer_id = {{${user_id}}} %}
{% assign cache_id = braze_campaign_id | append: customer_id %}
{% assign voucherify_campaign_id = "VOUCHERIFY-CAMPAIGN_ID" %}

{% connected_content
   https://api.voucherify.io/v1/publications?cache_id={{cache_id}}
   :method post
   :headers {
    "X-App-Id": "VOUCHERIFY-APP-ID",
    "X-App-Token": "VOUCHERIFY-APP-TOKEN"
   }
   :body campaign={{voucherify_campaign_id}}&customer={{customer_id}}&channel=Braze
   :content_type application/json
   :cache_max_age
   :retry
   :save publication
 %}
```

{% endraw %}
{% endtab %}
{% endtabs %}

## ユースケース

以下のユースケースはすべて、Brazeキャンペーンによって呼び出されるAPIコールを制限するために、Voucherify発行元IDとBrazeキャッシュおよびリトライパラメータを使用していることに留意されたい。以下の結果に注意しなければならない：

- 1つのBrazeキャンペーンで、同じ顧客に異なるコードを発行して送信することはできない。
- Voucherifyキャンペーンが_一度だけ参加する機能を_使用している場合、上記の一度だけ参加するタブで説明したように、コネクテッドコンテンツ本体から`source_id` を削除する必要がある。

Voucherify[GitHubリポジトリで](https://github.com/voucherifyio/braze-connected-content)コネクテッド・コンテンツ・スクリプトの例を見ることができる。

### ユニークなクーポンコードを発行して送信する

このユースケースでは、コネクテッドコンテンツスクリプトがVoucherify APIを呼び出し、ユニークなクーポンコードを発行し、Brazeメッセージで送信する。Brazeユーザーには、一人一個だけ固有のコードが与えられる。

{% raw %}

```liquid
{% assign braze_campaign_id = {{campaign.${api_id}}} %}
{% assign customer_id = {{${user_id}}} %}
{% assign source_id = braze_campaign_id | append: customer_id %}
{% assign voucherify_campaign_id = "VOUCHERIFY-CAMPAIGN_ID" %}
{% assign cache_id = source_id %}

{% connected_content
   YOUR API ENDPOINT/v1/publications?cache_id={{cache_id}}
   :method post
   :headers {
        "X-App-Id": "VOUCHERIFY-APP-ID",
        "X-App-Token": "VOUCHERIFY-APP-TOKEN"
   }
   :body campaign={{voucherify_campaign_id}}&customer={{customer_id}}&channel=Braze&source_id={{source_id}}
   :content_type application/json
   :cache_max_age
   :retry
   :save publication
 %}
```

{% endraw %}

### 新しい紹介者を招待する

顧客を紹介プログラムに参加させたい場合、その顧客に紹介コードを割り当てる必要がある。コネクテッドコンテンツは先の例と変わらない。このコネクテッドコンテンツスクリプトを使用すると、選択したBrazeユーザーに固有の紹介コードを発行して送信することができる。各ユーザーは、他のユーザーと共有し、新たな紹介者を獲得するための紹介コードを1つだけ受け取る。 

{% raw %}

```liquid
{% assign braze_campaign_id = {{campaign.${api_id}}} %}
{% assign customer_id = {{${user_id}}} %}
{% assign source_id = braze_campaign_id | append: customer_id %}
{% assign voucherify_campaign_id = "VOUCHERIFY-CAMPAIGN_ID" %}
{% assign cache_id = source_id %}

{% connected_content
   YOUR API ENDPOINT/v1/publications?cache_id={{cache_id}}
   :method post
   :headers {
        "X-App-Id": "VOUCHERIFY-APP-ID",
        "X-App-Token": "VOUCHERIFY-APP-TOKEN"
   }
   :body campaign={{voucherify_campaign_id}}&customer={{customer_id}}&channel=Braze&source_id={{source_id}}
   :content_type application/json
   :cache_max_age
   :retry
   :save publication
 %}
```

{% endraw %}

### ロイヤルティカードの残高を確認する

以下は、カスタム属性としてBrazeに事前に送信されたロイヤルティカードコードに基づいて、現在のロイヤルティ残高を引き出すコネクテッドコンテンツスクリプトのユースケースである。このスクリプトを使用する前に、Brazeユーザープロファイルにカスタム属性としてロイヤルティカードコードを保存する必要があることに注意。

{% raw %}

```liquid
{% assign braze_campaign_id = {{campaign.${api_id}}} %}
{% assign customer_id = {{${user_id}}} %}
{% assign source_id = braze_campaign_id | append: customer_id %}
{% assign voucherify_campaign_id = "VOUCHERIFY-CAMPAIGN_ID" %}
{% assign cache_id = source_id %}

{% connected_content
   YOUR API ENDPOINT/v1/loyalties/members/{{custom_attribute.${loyalty.card}}}?cache_id={{cache_id}}
   :method get
   :headers {
        "X-App-Id": "VOUCHERIFY-APP-ID",
        "X-App-Token": "VOUCHERIFY-APP-TOKEN"
   }
   :content_type application/json
   :cache_max_age
   :retry
   :save member
 %}
```

{% endraw %}

### カスタムコードを作成する

コネクテッド・コンテンツは、クリエイティブなシナリオを導入できる強力なツールだ。顧客のプロファイル情報に基づいてカスタムクーポンコードを作成できる。

ユニークなコードを生成するために顧客の電話番号を考慮するコード・スニペットである。このユースケースでは、コネクテッドコンテンツスクリプトがVoucherify APIを呼び出し、カスタムクーポンコードを発行する。

1.  まず、必要な変数をすべて定義する。次に、"SummerTime-"という接頭辞で始まるクーポンコードを作成し、残りのコードは顧客の電話番号とする。クーポンコードのベースとなるカスタム属性を決めることができる。  
    
    {% raw %}
    
    ```liquid
    {% assign braze_campaign_id = {{campaign.${dispatch_id}}} %}
    {% assign customer_id = {{${user_id}}} %}
    {% assign phoneNumber = {{${phone_number}}} %}
    {% assign source_id = braze_campaign_id | append: customer_id %}
    {% assign cache_id = source_id %}
    {% assign voucherify_campaign_id = "VOUCHERIFY-CAMPAIGN_ID" %}
    {% assign prefix = "SummerTime-" %}
    ```
    
    {% endraw %}
    
2.  次に、Voucherifyにキャンペーンでコードを1つ生成するよう依頼する。URLに作成するクーポンコードの名前を指定する：  
    
    {% raw %}
    
    ```liquid
    {% connected_content
       YOUR-API-ENDPOINT/v1/campaigns/{{voucherify_campaign_id}}/vouchers/{{prefix}}{{phoneNumber}}?cache_id={{cache_id}}
       :method post
       :headers {
            "X-App-Id": "VOUCHERIFY-APP-ID",
            "X-App-Token": "VOUCHERIFY-APP-TOKEN"
       }
       :content_type application/json
       :cache_max_age 
       :save voucher_created
       :retry
    %}  
    ```  
    
    {% endraw %}  

3.  最後に、作成したコードを公開する。コード・スニペットは、キャンペーンからランダムなバウチャーを生成するために使用したものとほとんど同じように見える。しかし、今回は特定のクーポンコードをターゲットにしている。  
    
    {% raw %}  
    
    ```liquid
    {% connected_content
       YOUR-API-ENDPOINT/v1/publications?cache_id={{cache_id}}
       :method post
       :headers {
           "X-App-Id": "VOUCHERIFY-APP-ID",
           "X-App-Token": "VOUCHERIFY-APP-TOKEN"
       }
       :body voucher={{prefix}}{{phoneNumber}}&customer={{customer_id}}&channel=Braze&source_id={{source_id}}
       :content_type application/json
       :cache_max_age 
       :save publication
       :retry
    %}
    ```
    
    {% endraw %}

その結果、顧客は次のようなメールを受け取る：  

![\]({% image_buster /assets/img/voucherify/voucherify_cc_custom_code_email.png %})

以下は、この例で使用したスニペットである：

{% raw %}

```liquid
{% assign braze_campaign_id = {{campaign.${dispatch_id}}} %}
{% assign customer_id = {{${user_id}}} %}
{% assign phoneNumber = {{${phone_number}}} %}
{% assign source_id = braze_campaign_id | append: customer_id %}
{% assign cache_id = source_id %}
{% assign voucherify_campaign_id = "VOUCHERIFY-CAMPAIGN_ID" %}
{% assign prefix = "Your Prefix" %}

{% connected_content
   YOUR-API-ENDPOINT/v1/campaigns/{{voucherify_campaign_id}}/vouchers/{{prefix}}{{phoneNumber}}?cache_id={{cache_id}}
   :method post
   :headers {
        "X-App-Id": "VOUCHERIFY-APP-ID",
        "X-App-Token": "VOUCHERIFY-APP-TOKEN"
   }
   :content_type application/json
   :cache_max_age 
   :save voucher_created
   :retry
%} 

{% connected_content
   YOUR-API-ENDPOINT/v1/publications?cache_id={{cache_id}}
   :method post
   :headers {
       "X-App-Id": "VOUCHERIFY-APP-ID",
       "X-App-Token": "VOUCHERIFY-APP-TOKEN"
   }
   :body voucher={{prefix}}{{phoneNumber}}&customer={{customer_id}}&channel=Braze&source_id={{source_id}}
   :content_type application/json
   :cache_max_age 
   :save publication
   :retry
%}
```

{% endraw %}

## Brazeメッセージに取得したデータを表示する

コネクテッド・コンテンツ・スクリプトを使用したいBrazeキャンペーンまたはキャンバスがすでにあると仮定する。

### ステップ1:コネクテッド・コンテンツ・スクリプトをメッセージテンプレートに追加する

1.  コネクテッド・コンテンツ・スクリプトをコピーし、メッセージHTMLテンプレートの{% raw %}`<body>`{% endraw %} タグの下に貼り付ける。**CAMPAIGN_IDを**VoucherifyキャンペーンダッシュボードのURLアドレスからコピーしたVoucherify{% raw %}`campaign_id`{% endraw %} に置き換える。<br>![\]({% image_buster /assets/img/voucherify/voucherify_cc_campaignId.png %}){: style="margin-top:15px;margin-bottom:15px;"}
    {% raw %}  
    ```
    assign voucherify_campaign_id = "camp_Y7h1meBSyybsNs7UpSVVZZce"
    ```
    {% endraw %}

2. Voucherify APIエンドポイントを指定する。APIエンドポイントがわからない場合は、**プロジェクト設定**＞**一般**＞**APIエンド**ポイントで確認できる。<br>
    {% raw %}
    ```
    YOUR API ENDPOINT/v1/publications?cache_id={{cache_id}}
    ```
    {% endraw %}
    
    | 共有クラスタ   | Braze コネクテッドコンテンツ用エンドポイント          |
    | ---------------- | --------------------------------------------- |
    | ヨーロッパ（デフォルト） | https://api.voucherify.io/v1/publications     |
    | 米国    | https://us1.api.voucherify.io/v1/publications |
    | アジア（シンガポール） | https://as1.api.voucherify.io/v1/publications |
    {: .reset-td-br-1 .reset-td-br-2}
    
3.  認証用のAPIキーを追加する。`Voucherify-App-Id` と`Voucherify-App-Token` は、**プロジェクト設定 > 一般 > アプリケーションキーで**確認できる**。**<br>![\]({% image_buster /assets/img/voucherify/voucherify_cc_app_keys.png %}){: style="margin-top:15px;margin-bottom:15px;"}
    {% raw %}
    ```
    "X-App-Id": "VOUCHERIFY-APP-ID",
    "X-App-Token": "VOUCHERIFY-APP-TOKEN"
    ```
    {% endraw %}
    
これでコネクテッド・コンテンツ・スクリプトの準備は整った。

{% raw %}

```liquid
{% assign braze_campaign_id = {{campaign.${api_id}}} %}
{% assign customer_id = {{${user_id}}} %}
{% assign source_id = braze_campaign_id | append: customer_id %}
{% assign voucherify_campaign_id = "camp_Y7h1meBSyybsNs7UpSVVZZce" %}
{% assign cache_id = source_id %}

{% connected_content
   https://api.voucherify.io/v1/publications?cache_id={{cache_id}}
   :method post
   :headers {
        "X-App-Id": "490a3fb6-a",
        "X-App-Token": "328099d5-a"
   }
   :body campaign={{voucherify_campaign_id}}&customer={{customer_id}}&channel=Braze&source_id={{source_id}}
   :content_type application/json
   :cache_max_age
   :retry
   :save publication
 %}
```

{% endraw %}

### ステップ2:取得したデータを表示するスニペットを作成する

Voucherify APIからのレスポンスは、コネクテッドコンテンツによって{% raw %}`:save`{% endraw %} パラメータの値で保存される。以下に例を示します。

{% raw %}

```liquid
:save member
```
{% endraw %}

これにより、VoucherifyレスポンスのデータをBrazeメッセージで取得し、表示することができる。

Voucherify APIからのJSON形式のレスポンスに含まれる公開コード、ロイヤルティカード残高、有効期限、その他のパラメータを表示するスニペットを作成できる。

例えば、メッセージテンプレートに公開コードを表示するには、voucherオブジェクトから一意のコードをフェッチするスニペットを作成しなければならない。

コネクテッド・コンテンツのスクリプト：

![Connected Content script showing to save a Voucherify response at the end of the Connected Content call]({% image_buster /assets/img/voucherify/voucherify_cc_save_parameter.png %})

Brazeメッセージテンプレートのスニペット：

{% raw %}

```liquid
{{publication.voucher.code}}
```

{% endraw %}

その結果、各顧客のプロファイルに自動的に割り当てられたユニークなコードがメッセージングされる。コードがユーザーによって受信されるたびに、そのコードはVoucherifyのユーザープロファイルに公開される。

Voucherify APIから取得したロイヤルティカードの残高を表示するには、以下のスニペットを作成する必要がある：

{% raw %}

```liquid
{{member.loyalty_card.balance}}
```

{% endraw %}

ここで、メンバーはコネクテッド・コンテンツ・スクリプトの{% raw %}`:save`{% endraw %} パラメータの値である。

{% raw %}

```liquid
:save member
```

{% endraw %}

私たちは、'Preview mode' に全面的に依存せず、何度かテスト・メッセージを送信して、すべてが思い通りに機能することを確認することを強く勧める。

### ステップ3:レート制限の設定

キャンペーンターゲットを設定する際、詳細設定を使用して1分あたりのメッセージ送信数を制限する。

![\]({% image_buster /assets/img/voucherify/voucherify_cc_limiter.png %})

レート制限とフリークエンシーキャップについてはBraze[ドキュメントを]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting)参照のこと。
