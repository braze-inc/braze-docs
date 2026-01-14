---
nav_title: コネクテッドコンテンツを使用したデータの取得
article_title: コネクテッドコンテンツと Voucherify を使用したデータの取得
page_order: 2
alias: /partners/voucherify/connected_content/
description: "このリファレンス記事では、Braze コネクテッドコンテンツを使用して Voucherify API からデータを取得し、特定の Braze セグメントにメッセージを送信する方法について説明します。"
page_type: partner
search_tag: Partner
---

# コネクテッドコンテンツを使用したデータの取得

> Braze コネクテッドコンテンツを使用して、Voucherify API からデータを取得し、特定の Braze セグメントにメッセージを送信できます。このリファレンス記事では、Voucherify クーポンの発行、新しい紹介者の招待、ロイヤルティカードの残高の取得などのために、コネクテッドコンテンツスクリプトを設定する方法などを紹介します。

_この統合は Voucherify によって管理されます。_

## 統合について

スクリプトの基本スキーマは次のようになります:
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

Voucherify の [GitHub リポジトリ](https://github.com/voucherifyio/braze-connected-content)にアクセスして、コネクテッドコンテンツスクリプトの例を参照してください。

## セキュリティ設定

以下の設定が行われてない場合、コネクテッドコンテンツメッセージがトリガーされるたびに、Voucherify API が2回以上呼び出されます。これらの設定により、Brazeに請求されるAPIコールの数が減り、メッセージ配信を妨げる可能性のあるハードブロッキングAPI制限に達するリスクが軽減されます。

{% tabs %}
{% tab Rate Limiter %}

**レート制限**

Braze によって送信されるメッセージの数を1分あたり[制限する]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting)ようにしてください。これにより、キャンペーンからの過剰なトラフィックに対して、BrazeおよびVoucherifyのAPIの両方が保護されます。キャンペーンの設定中にユーザーをターゲットにする場合、送信率を1分あたり500メッセージに制限してください。

![]({% image_buster /assets/img/voucherify/voucherify_cc_limiter.png %})

{% endtab %}
{% tab Caching %}

**POST 呼び出しでのキャッシュ**

HTTP POST を使用して実行されるコネクテッドコンテンツ呼び出しは、デフォルトではキャッシュを行わず、発行済みのコードごとに2つの API リクエストを行います。この動作はAPIの制限に負担をかける可能性があります。このキャッシュメカニズムでは、バウチャー発行ごとに1回の API 呼び出しに制限できます。 

{% alert important %}
このチュートリアルにおけるコネクテッドコンテンツのすべての例には、BrazeによってトリガーされるAPIコールの数を減らすためにデフォルトのキャッシングが含まれています。
{% endalert %}

POST呼び出しにキャッシュを追加するには:

1. {% raw %}`:cache_max_age`{% endraw %}属性を追加します。デフォルトでは、キャッシュ期間は5分です。秒単位で期間をカスタマイズできます。5分から4時間の間で設定できます。例: {% raw %}`:cache_max_age 3600`{% endraw %} の場合キャッシュ期間は1時間です。
2. 宛先エンドポイントクエリパラメーターにキャッシュキー {% raw %}`cache_id={{cache_id}}`{% endraw %} を指定します。これにより、Braze が一意のコード発行を識別できるようになります。最初に変数を定義してから、エンドポイントに一意のクエリ文字列を付加します。これにより、各コード発行が {% raw %}`source_id`{% endraw %} によって区別されます。

![]({% image_buster /assets/img/voucherify/voucherify_cc_cache.png %})

_結果に注意してください。_BrazeはURLに基づいてAPIコールをキャッシュします。クエリパラメーターとして使用される一意の文字列は Voucherify では無視されますが、この文字列により Braze の異なる API リクエストが区別され、一意の試行を個別にキャッシュすることができるようになります。そのクエリパラメータがないと、すべての顧客はキャッシュ期間中に同じクーポンコードを受け取ります。

{% endtab %}
{% tab Retry attribute %}

**retry 属性**

コネクテッドコンテンツは Voucherify 応答を検証しないため、コネクテッドコンテンツスクリプトに [retry]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries) 属性を追加することを推奨します。コネクテッドコンテンツのロジックは、メッセージを中断する前に5回再試行します (これはレート制限に準拠します)。この方法は、Voucherifyからデータを取得するのに少し時間がかかる場合に、コードの公開が失敗するケースを防ぐのに役立ちます。

{% raw %}`:retry`{% endraw %}を使用しない場合、Voucherifyから返される応答に関係なく、Brazeは配信を送信しようとします。これにより、公開されたコードなしでメールが生成される可能性があります。

![]({% image_buster /assets/img/voucherify/voucherify_cc_retry.png %})

{% endtab %}
{% tab Unique publications %}

**顧客ごとの一意のコード発行**

スクリプト本文の{% raw %}`source_id`{% endraw %}パラメータは、各顧客が単一のBrazeキャンペーンで一意のコードを1つだけ受け取ることができるようにします。その結果、たとえBrazeが意図せずリクエストを複数回行ったとしても、各ユーザーは最初のメッセージで彼/彼女に公開されたのと同じ一意のコードを受け取ります。

![]({% image_buster /assets/img/voucherify/voucherify_cc_sourceId_unique_publication.png %})

次の構成を使用して、{% raw %}`{{source_id}}`{% endraw %}およびその出版物への影響を変更できます:

| 構成 | 効果 |
| ------------- | ------ |
| {% raw %}`{{campaign.${dispatch_id}}}`{% endraw %} | 1回の送信内の顧客は同じコード発行を使用します。 |
| {% raw %}`{{campaign.${api_id}}}`{% endraw %} | 1つのキャンペーン内のすべての顧客は同じコード発行を使用します。 |
| {% raw %}`{{${user_id}}}`{% endraw %} または {% raw %}`{{${braze_id}}}`{% endraw %} | どのキャンペーンが送信されてもすべての顧客が同じコード発行を使用することを確認します ({% raw %}`external_id`{% endraw %}である {% raw %}`${user_id}`{% endraw %}と、内部 ID である {% raw %}`${braze_id}`{% endraw %} を使用できます)。 |
| {% raw %}`{{campaign.${dispatch_id}}}`{% endraw %} と {% raw %}`{{campaign.${user_id}}}`{% endraw %} | 1つの送信内の各顧客は、同じ一意のコード発行を使用します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Join-once %}

**1回のみの参加**

Voucherifyキャンペーンに制限がある場合_顧客は一度しか参加できません_、スクリプト本文から公開ソースIDを削除してください。Voucherifyは、同じ顧客に送信される各Brazeメッセージが最初に公開されたのと同じコードを配信することを確認します。

![]({% image_buster /assets/img/voucherify/voucherify_cc_join_once.png %}){: style="max-width:50%;"}

あなたのコネクテッドコンテンツスクリプトは次のようになります:

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

以下のすべてのユースケースでは、Voucherify の発行ソース ID と Braze のキャッシュおよび再試行パラメーターを使用して、Braze キャンペーンによって呼び出される API 呼び出しを制限していることに留意してください。次に示す影響に注意する必要があります。

- 同じ顧客に異なるコードを単一のBrazeキャンペーンで公開および送信することはできません。
- Voucherifyキャンペーンで_一度だけ参加機能_を使用する場合は、上記の一度だけ参加タブに記載されているように、コネクテッドコンテンツ本文から`source_id`を削除する必要があります。

Voucherify の [GitHub リポジトリ](https://github.com/voucherifyio/braze-connected-content)にアクセスして、コネクテッドコンテンツスクリプトの例を参照してください。

### 公開してユニークなクーポンコードを送信する

このユースケースでは、コネクテッドコンテンツスクリプトがVoucherify APIを呼び出して一意のクーポンコードを発行し、それをBrazeメッセージで送信します。各Brazeユーザーは一意のコードを1つだけ受け取ります。

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

顧客に紹介プログラムに参加してもらうには、その人に紹介コードを割り当てる必要があります。コネクテッドコンテンツは前の例と同じです。このコネクテッドコンテンツスクリプトを使用すると、選択したBrazeユーザーにユニークな紹介コードを公開して送信できます。各ユーザーは、他のユーザーと共有して新しい紹介者を獲得するための紹介コードを1つだけ受け取ります。 

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

### ロイヤルティカード残高を取得する

ここに、カスタム属性として事前にBrazeに送信されたロイヤルティカードコードに基づいて現在のロイヤルティ残高を取得するコネクテッドコンテンツスクリプトのユースケースがあります。このスクリプトを使用する前に、ロイヤルティカードコードをBrazeユーザープロファイルにカスタム属性として保存する必要があることに注意してください。

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

コネクテッドコンテンツは、クリエイティブなシナリオの導入を可能にする強力なツールです。顧客のプロファイル情報に基づいてカスタムクーポンコードを作成できます。

ここに、顧客の電話番号を考慮して一意のコードを生成するコードスニペットがあります。このユースケースでは、コネクテッドコンテンツスクリプトがVoucherify APIを呼び出してカスタムクーポンコードを発行します。

1.  まず、必要なすべての変数を定義します。次に、クーポン{コード}を「SummerTime-」というプレフィックスで始め、残りの{コード}は{顧客}の電話番号にします。クーポンコードの基準とするカスタム属性を決定できます。  
    
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
    
2.  次に、Voucherifyに依頼してキャンペーンで単一のコードを生成します。URLで作成するクーポンコードの名前を提供します:  
    
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

3.  最後に、作成したコードを公開します。コードスニペットは、キャンペーンからランダムなバウチャーを生成するために使用したものとほとんど同じように見えます。しかし、今回は特定のバウチャーコードを対象としています。  
    
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

その結果、顧客に次のメールが送信されます。  

![]({% image_buster /assets/img/voucherify/voucherify_cc_custom_code_email.png %})

こちらがこの例で使用されている完全なスニペットです:

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

私たちは、すでにコネクテッドコンテンツスクリプトを使用したいBrazeキャンペーンまたはキャンバスを持っていると仮定しています。

### ステップ1:メッセージテンプレートにコネクテッドコンテンツスクリプトを追加

1.  メッセージHTMLテンプレートの{% raw %}`<body>`{% endraw %}タグの下にコネクテッドコンテンツスクリプトをコピーして貼り付けます。置き換える **CAMPAIGN_ID**をVoucherifyキャンペーンダッシュボードのURLアドレスからコピーしたVoucherify{% raw %}`campaign_id`{% endraw %} に置き換える。<br>![]({% image_buster /assets/img/voucherify/voucherify_cc_campaignId.png %}){: style="margin-top:15px;margin-bottom:15px;"}
    {% raw %}  
    ```
    assign voucherify_campaign_id = "camp_Y7h1meBSyybsNs7UpSVVZZce"
    ```
    {% endraw %}

2. Voucherify APIエンドポイントを提供してください。APIエンドポイントがわからない場合は、**プロジェクト設定** > **一般** > **APIエンドポイント**で確認できます。<br>
    {% raw %}
    ```
    YOUR API ENDPOINT/v1/publications?cache_id={{cache_id}}
    ```
    {% endraw %}
    
    | 共有クラスタ   | Braze コネクテッドコンテンツのエンドポイント          |
    | ---------------- | --------------------------------------------- |
    | ヨーロッパ（デフォルト） | https://api.voucherify.io/v1/publications     |
    | アメリカ合衆国    | https://us1.api.voucherify.io/v1/publications |
    | アジア（シンガポール） | https://as1.api.voucherify.io/v1/publications |
    {: .reset-td-br-1 .reset-td-br-2 role="presentation" }
    
3.  認証のためにAPIキーを追加してください。`Voucherify-App-Id`と`Voucherify-App-Token`は**プロジェクト設定 > 一般 > アプリケーションキー.**で見つけることができます。<br>![]({% image_buster /assets/img/voucherify/voucherify_cc_app_keys.png %}){: style="margin-top:15px;margin-bottom:15px;"}
    {% raw %}
    ```
    "X-App-Id": "VOUCHERIFY-APP-ID",
    "X-App-Token": "VOUCHERIFY-APP-TOKEN"
    ```
    {% endraw %}
    
これで、コネクテッドコンテンツスクリプトの準備が整いました。

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

Voucherify API からの応答は、{% raw %}`:save`{% endraw %} パラメーターの値の下にコネクテッドコンテンツによって保存されます。以下に例を示します。

{% raw %}

```liquid
:save member
```
{% endraw %}

これにより、Voucherify 応答からデータを取得して Braze メッセージに表示できます。

スニペットを作成して、公開されたコード、ロイヤルティカードの残高、有効期限、およびVoucherify APIからのJSON形式のレスポンスに含まれるその他のパラメーターを表示できます。

例えば、メッセージテンプレートに公開されたコードを表示するには、バウチャーオブジェクトからユニークなコードを取得するスニペットを作成する必要があります。

コネクテッドコンテンツスクリプト:

![コネクテッドコンテンツのスクリプトで、コネクテッドコンテンツ呼び出しの最後にVoucherifyのレスポンスを保存することを示す]({% image_buster /assets/img/voucherify/voucherify_cc_save_parameter.png %})

Brazeメッセージテンプレートのスニペット:

{% raw %}

```liquid
{{publication.voucher.code}}
```

{% endraw %}

その結果、それぞれの顧客は各自のプロファイルに自動的に割り当てられた一意のコードを含むメッセージを受け取ります。ユーザーがコードを受け取るたびに、そのコードは Voucherify のプロファイルに発行されます。

ロイヤルティカードの残高を Voucherify API から取得して表示するには、次のスニペットを作成する必要があります。

{% raw %}

```liquid
{{member.loyalty_card.balance}}
```

{% endraw %}

ここで member は、コネクテッドコンテンツスクリプトの {% raw %}`:save`{% endraw %}パラメーターの値です。

{% raw %}

```liquid
:save member
```

{% endraw %}

「プレビューモード」に完全に依存せず、いくつかのテストメッセージを送信して、すべてが正常に動作していることを確認することを強くお勧めします。

### ステップ3:レート制限を設定する

キャンペーンターゲットを設定する際は、高度な設定を使用して、1分あたりに送信されるメッセージの数を制限します。

![]({% image_buster /assets/img/voucherify/voucherify_cc_limiter.png %})

レート制限とフリークエンシーキャップについて詳しくは、Braze の[ドキュメント]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting)でご確認ください。

