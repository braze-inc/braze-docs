--- 
nav_title: セッションM
article_title: セッションM
description: "この参考記事では、カスタマーエンゲージメントとロイヤルティのプラットフォームであるBrazeとSessionMのパートナーシップについて概説している。"
alias: /partners/sessionm/
page_type: partner
search_tag: Partner
--- 

# SessionMロイヤルティプラットフォーム

> [SessionMは](https://www.mastercardservices.com/en/capabilities/sessionm)カスタマーエンゲージメントとロイヤルティのプラットフォームで、キャンペーン管理機能とロイヤルティ管理ソリューションを提供し、マーケターがターゲットを絞ったアウトリーチを推進してエンゲージメントと収益性を向上させるのを支援する。

## 前提条件

| ソース | 必要条件 | 説明 |
| --- | --- | --- |
| Braze | Braze REST API キー | `trigger_send` 権限を持つ Braze REST API キー。これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze | Braze RESTエンドポイント | RESTエンドポイントのURL。エンドポイントは、[インスタンス]({{site.baseurl}}/api/basics/#endpoints)のBraze URLによって異なります。 |
| BrazeとSessionM | 一致する識別子 | 統合を使用するには、SessionMとBrazeの両方が、それぞれのプラットフォームで使用されている識別子の記録を持っていることを確認する。`user_id` への参照は、SessionMでのプロファイル生成時に生成されたSessionMのユーザー識別子に対応する。 |
| セッションM | セッションMアカウント | このパートナーシップを利用するには、SessionMのアカウントが必要である。 |
| セッションM | SessionM Core RESTエンドポイント | エンドポイントは、インスタンスのSessionM URLに依存する。これは、**デジタルプロパティから**SessionMダッシュボードで作成できる。 |
| セッションM | SessionM Core REST API キー | インスタンスとBraze統合に関連付けられたSessionM APIキー。このキーは、タグを含むすべてのコアベースのコールに使用できる。これは、**デジタルプロパティから**SessionMダッシュボードで作成できる。 |
| セッションM | SessionM Core REST APIのシークレット | インスタンスとBraze統合に関連付けられたSessionM APIシークレット。このキーは、タグを含むすべてのコアベースのコールに使用できる。これは、**デジタルプロパティから**SessionMダッシュボードで作成できる。 |
| セッションM | SessionM Connect RESTエンドポイント | エンドポイントは、インスタンスのSessionM URLに依存する。SessionMテクニカルアカウントマネージャーまたはデリバリーチームまでご連絡ください。 |
| セッションM | SessionM Connect REST認可文字列 | インスタンスに関連付けられたSessionM Connect Basic Authorization文字列。この認証文字列は、get_user_offersを含む、すべてのconnectベースのコールで使用できる。SessionMテクニカルアカウントマネージャーまたはデリバリーチームまでご連絡ください。 |
| セッションM | SessionM Connect RESTの小売（店）ID。 | インスタンスに関連付けられた特定の顧客に対する一意のguid識別。SessionMテクニカルアカウントマネージャーまたはデリバリーチームに連絡する。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合は、**デベロッパコンソール**> **API設定**でAPI キーを作成できます。
{% endalert %} 

## ユースケース

以下のユースケースは、SessionMとBrazeの統合を活用するいくつかの方法を示している。

- ロイヤルティ、顧客データ管理、メッセージングの各プラットフォームのデータを統合したセグメンテーションを作成する。
- 強力なセグメンテーションを使用して、オファーやプロモーションで特定のユーザーをターゲットにする。
- メッセージングの際には、最新のユーザー、オファー、ロイヤルティ情報を活用しよう。
- プロモーションやロイヤルティ活動の進捗や完了について、顧客に詳細な通知を行う。
- 新しいオファーが獲得されたら顧客に通知し、オファーの詳細を提供する。

## SessionMとBrazeの統合

### ステップ 1: Brazeでセグメンテーションを作成する

Brazeで、SessionMのプロモーションやオファーでターゲットとするユーザーのセグメンテーションを作成する。 

![カスタム属性」フィルターを選択したセグメンテーションビルダー]({% image_buster /assets/img/sessionm/CreateSegment.png %})

### ステップ 2: BrazeのセグメンテーションをSessionMにインポートする。

#### オプション 1: SessionM Tagエンドポイントにエクスポートする（推奨）。

まず、BrazeでWebhookキャンペーンを作成し、Webhook URLを{% raw %}`{{endpoint_core}}/priv/v1/apps/{{appkey_core}}/users/{{${user_id}}}/tags`{% endraw %} に設定する。Liquidを使って、URL内部で`user_id` 。 

生テキストの**リクエストボディを**使用して、SessionMのユーザープロファイルに追加される希望 のタグと、希望するライブ時間を含むように、Webhookボディを構成する。例は次のとおりです。

 ```
 {
   "tags":[
    "braze_test"
   ],
   "ttl":2592000
}
 ```

![]({% image_buster /assets/img/sessionm/SessionMWebhookComposer.png %}){: style="max-width:85%;"}

**設定]**タブで、各リクエストヘッダーフィールドのキーと値のペアを追加する：
    \- 対応する値を持つキー`Content-Type` を作成する。 `application/json`
    \- 対応する値`Basic YOUR-ENCODED-STRING-KEY` を持つキー`Authorization` を作成する。エンドポイントのエンコードされた文字列キーについては、SessionM チームに問い合わせること。 

![Webhook 設定。]({% image_buster /assets/img/sessionm/SessionMWebhookSettings.png %}){: style="max-width:85%;"}

配信スケジュールを立て、**ターゲットオーディエンスを** [前回作成した](#step-1-create-a-segment-in-braze)セグメンテーションに設定し、キャンペーンを開始する。

{% alert important %}
このプロセスは、PostmanなどのAPIクライアントを介して、顧客、タグ名、コール内の各ユーザーの生存時間（コールごとに1ユーザー）を指定して、[SessionMタグエンドポイントに](https://docs.sessionm.com/developer/APIs/Core/Customers/customers_tags.htm#create-or-increment-a-customer-tag)直接リクエストを行うことでも実行できる。
<br><br>
以下のリクエスト例はcURLを使用している。 

{% raw %}
```bash
curl --location -g --request POST '{{endpoint_core}}/priv/v1/apps/{{apikey_core}}/users/{{user_id}}/tags' \
--header 'Content-Type: application/json' \
--header 'Authorization: Basic {{base64_encoded_string}}' \
--data-raw '{
"tags":[
"tagname1",
"tagname2"
],
"ttl":20000
}'
```
{% endraw %}
{% endalert %}

#### オプション 2: CSV インポート

Braze segmenterを使用してBrazeセグメントをエクスポートし、タグ付けする顧客、タグ名、ファイル内の各ユーザーの生存期間を含むCSVファイルをSessionMに提供する。

## Brazeでリアルタイムのオファーウォレットを検索する

SessionMとBrazeを統合することで、コネクテッドコンテンツを使用して、メッセージ送信時にSessionMのユーザーデータをリアルタイムで取り込むことができ、顧客に古い、有効期限が切れた、または既に償還されたロイヤルティオファーを伝えるリスクを排除することができる。 

次の例では、コネクテッドコンテンツを使用して、オファーウォレットのデータをメッセージにテンプレート化している。しかし、コネクテッドコンテンツは、SessionMのコネクトエンドポイントのどれでも使用できる。 

### ステップ1:セッションMでオファーを出す

セッションMは、設定可能ないくつかの異なる内部レバーから顧客にオファーを発行する。発行後、オファーはSessionMが「オファーウォレット」と呼ぶ状態に移される。

顧客は必要なアクションを完了するか、ターゲティングを満たす必要があり、SessionM内でオファーが発行される。

次にSessionMは、発行された状態の顧客のウォレットにオファーを追加する。

### ステップ2:SessionMオファーウォレットAPIを呼び出す

SessionMオファーのあるキャンペーンまたはキャンバスステップで、[コネクテッドコンテンツを]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/)使用して、[SessionM`get_user_offers` エンドポイントに](https://domains-connecteast1.ent-sessionm.com/offers/swagger/ui/index#!/InfoV232583210323232323232323232323232This32API32allows32for32the32querying32of32information32about32offers32in32a32read45only32fashion4610323232323232323232323232May32be32initiated32by32the32dashboard32or32the32mobile32app4610323232323232323232323232/InfoV2_GetUserOffers/)APIコールを行う。

コネクテッドコンテンツリクエストで、ユーザーのSessionM`user_id` と、顧客がウォレットに持っているアクティブオファーの全リストを取得するためのあなたの`retailer_id` を指定する。このエンドポイントへの各リクエストは、1人のユーザーを含むことができる。コネクテッドコンテンツ呼の基本認証ヘッダー用のエンコードされた文字列キーについては、SessionMチームに問い合わせること。

リクエストボディの中で、`culture` はデフォルトで`en-US` 。しかし、多言語のSessionMオファーのために、ユーザーの言語をテンプレート化するために、Liquidを使うことができる(例えば、{% raw %}`"culture":"{{${language}}}"`{% endraw %})。

{% raw %}
```
{% capture postbody %}
{"retailer_id":"YOUR-RETAIL-ID","user_id":"{{${user_id}}}","skip":0,"take":1000,"include_pending_extended_data":false,"culture":"en-US"}
{% endcapture %}

{% connected_content
     {{endpoint_connect}}/offers/api/2.0/offers/get_user_offers
:method post     
:headers {
       "Content-Type": "application/json",
       "Authorization": "Basic YOUR-BASE64-ENCODED-KEY"
  }
     :body {{postbody}}
     :save wallet
%}
```
{% endraw %}

### ステップ 3:Brazeメッセージングにオファーウォレットを入力する

リクエストがエンドポイントに行われた後、SessionMは各オファーの完全な詳細とともに、発行された状態のオファーの完全なリストを返す。これは返されたレスポンシブの例である：

{% raw %}
```
{
    "status": "ok",
    "payload": {
      "user": {
        "opted_in": false,
        "activated": false,
        ...
      },
      "user_id": "00000000-0000-0000-0000-000000000000",
      "user_offers": [
        {
          "offer_id": "1a2b3324-1da6-4e49-b921-afc386dabb60",
          "offer_group_id": "00000000-0000-0000-0000-000000000000",
          "offer_type": "manual_fulfillment",
          ...
        }
      ],
      "total_records": 1,
      "offer_groups": [
        {
          "id": "00000000-0000-0000-0000-000000000000",
          "name": "All Offers",
          "sort_order": 0
        }
      ],
      "offer_categories": [
        {
          "id": "9a82f973-aae6-4e10-839b-7117a852cf9e",
          "name": "All Offers",
          "sort_order": 0
        }
      ],
      "total_points": 1000,
      "available_points": 100
    }
}
```
{% endraw %}

Liquidドット記法を使えば、これをメッセージに入力することができる。例えば、`offer_id` の結果でメッセージをパーソナライズさせるために、{% raw %}`{{wallet.payload.available_points}`{% endraw %} を使って、`100` を返すペイロードを活用することができる。

{% alert note %}
これは個別のAPIである。500ユーザー以上のバッチを送信する場合は、SessionMアカウントチームに連絡して、統合にバルクデータを組み込む方法について問い合わせること。
{% endalert %}

## トリガーメッセージの設定

SessionMとBrazeの統合により、ユーザープロファイルのデータ、オファーの詳細、ポイント残高がメッセージングにダイナミックな形で入力され、アクションの時点で顧客にリアルタイムで送信される。

### ステップ1:SessionMデリバリーチームがテンプレートを設定する

SessionMデリバリーチームと協力して、トリガーメッセージで使用するテンプレートを開発する。SessionMは、ユーザープロファイルのデータ、オファーの詳細、ポイント残高をメッセージングに挿入し、Brazeでトリガーすることで、リアルタイムでの顧客メッセージングを実現する。

SessionMのすべてのテンプレートにある標準フィールドには、以下が含まれる：
- `canvas_id`
- `campaign_id`
- `broadcast flag`
- `customer identifier`
- `email address`

{% alert note %}
`broadcast flag` を`true` に設定すると、Brazeのキャンペーンまたはキャンバスがターゲットとするセグメンテーション全体にメッセージが送信される。
{% endalert %}

特定のニーズに応じてフィールドを追加設定することもできる：

- **データを提供する：** `offer_id` `offer title`, , , , , 、`user offer id` `description` `terms and conditions` `logo` `pos discount id` `expiration date`
- **ポイント賞データ：** `point award amount`, `point account name`
- **イベントのトリガーデータ：**トリガー/送信Webhookの結果を利用するトリガーイベント内のすべてのデータ。
- **キャンペーン専用データ：** `campaign runtime` `campaign_id` `campaign name` 、 `campaign custom data`

追加フィールドは、メッセージをパーソナライズするための`trigger_properties` としてBrazeに送信される。 

### ステップ2:Brazeキャンペーンまたはキャンバスを作成する

SessionMをトリガーとするAPIトリガーキャンペーンまたはキャンバスをBrazeで作成する。`offer_id` や`offer title` などの追加フィールドが設定されている場合、パーソナライズされたフィールドをメッセージングに追加するには、Liquid ({% raw %}`{{api_trigger_properties.${offer_id}}}`{% endraw %} など) を使用する。

![API トリガーのプロパティ]({% image_buster /assets/img/sessionm/apiTriggerProperties.png %})

**スケジュール配信**タブで、キャンペーンまたはキャンバスIDをメモする。

![APIトリガーキャンペーン]({% image_buster /assets/img/sessionm/apiTriggerCampaign.png %})

キャンペーンまたはキャンバスの詳細を確定し、「**Launch**」を選択する。 

### ステップ 3:SessionMのプロモーションやメッセージングキャンペーンを行う

次に、SessionMでキャンペーンを作成する。

![SessionM キャンペーン作成。]({% image_buster /assets/img/sessionm/SessionMCampaignCreation.png %})

SessionMキャンペーンの詳細設定を更新して、`braze_campaign_id` または`braze_canvas_id` を含む以下のJSONペイロードを含めること。

{% raw %}
```
{
"braze_campaign_id": "{{CAMPAIGN ID}}",
"braze_canvas_id": "{{CANVAS ID}}",
}
```
{% endraw %}

![] （{% image_buster /assets/img/sessionm/SessionMAdvancedSettings.png %} ）。{: style="max-width:85%;"}

スケジュールやビヘイビアに関するメッセージトリガーを作成する。次に、**外部メッセージ**メニューの**メッセージングバリアントとして** **Braze Messaging Variantを**選択し、テンプレートを使用する。

![SessionM 外部メッセージ]({% image_buster /assets/img/sessionm/SessionMExternalMessage.png %})

このテンプレートは、関連するスタティック属性とダイナミックな属性を引き出し、Brazeエンドポイントにコールアウトする。

![SessionM Braze テンプレート。]({% image_buster /assets/img/sessionm/SessionMBrazeTemplate.png %}){: style="max-width:85%;"}
