--- 
nav_title: SessionM
article_title: SessionM
description: "この参考記事では、カスタマーエンゲージメントとロイヤルティのプラットフォームであるBrazeとSessionMのパートナーシップについて概説している。"
alias: /partners/sessionm/
page_type: partner
search_tag: Partner
--- 

# SessionM ロイヤルティプラットフォーム

> [SessionM](https://www.mastercardservices.com/en/capabilities/sessionm) は、キャンペーン管理機能とロイヤルティ管理ソリューションを提供するカスタマーエンゲージメントとロイヤリティプラットフォームで、マーケターがターゲットを絞ったアウトリーチを推進してエンゲージメントと収益性を向上させるのを支援します。

## 前提条件

| ソース | 必要条件 | 説明 |
| --- | --- | --- |
| Braze | Braze REST API キー | `trigger_send` 権限を持つ Braze REST API キー。これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze | Braze RESTエンドポイント | RESTエンドポイントのURL。エンドポイントは、[インスタンス]({{site.baseurl}}/api/basics/#endpoints)のBraze URLによって異なります。 |
| BrazeとSessionM | 一致する識別子 | 統合を使用するには、SessionMとBrazeの両方が、それぞれのプラットフォームで使用されている識別子の記録を持っていることを確認する。`user_id` への参照は、SessionM でのプロファイル作成時に生成された SessionM のユーザー識別子に対応します。 |
| SessionM | SessionM アカウント | このパートナーシップを利用するには、SessionMのアカウントが必要である。 |
| SessionM | SessionM Core RESTエンドポイント | エンドポイントは、インスタンスのSessionM URLに依存する。これは SessionM ダッシュボードの **Digital Properties** から作成できます。 |
| SessionM | SessionM Core REST API キー | インスタンスとBraze統合に関連付けられたSessionM APIキー。このキーは、タグを含むすべてのコアベースのコールに使用できる。これは SessionM ダッシュボードの**デジタルプロパティ**から作成できます。 |
| SessionM | SessionM Core REST APIのシークレット | インスタンスとBraze統合に関連付けられたSessionM APIシークレット。このキーは、タグを含むすべてのコアベースのコールに使用できる。これは SessionM ダッシュボードの**デジタルプロパティ**から作成できます。 |
| SessionM | SessionM Connect RESTエンドポイント | エンドポイントは、インスタンスのSessionM URLに依存する。SessionMテクニカルアカウントマネージャーまたはデリバリーチームに連絡する。 |
| SessionM | SessionM Connect REST認可文字列 | インスタンスに関連付けられたSessionM Connect Basic Authorization 文字列。この認証文字列は、get_user_offers. を含む、すべての接続ベースの通話に使用できる。この認証文字列を提供 するには、SessionMのテクニカルアカウントマネージャーまたはデリバリーチームに連絡すること。 |
| SessionM | SessionM Connect RESTの小売（店）ID。 | インスタンスに関連付けられている特定の顧客に対する一意の GUID 識別子。SessionMテクニカルアカウントマネージャーまたはデリバリーチームに連絡する。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/)を使用している場合は、**デベロッパコンソール**> **API設定**でAPI キーを作成できます。
{% endalert %} 

## ユースケース

以下のユースケースは、SessionMとBrazeの統合を活用するいくつかの方法を示している。

- ロイヤルティ、顧客データ管理、メッセージングの各プラットフォームのデータを統合したセグメンテーションを作成する。
- 堅牢なセグメンテーションを使用して、オファーやプロモーションで特定のユーザーセットをターゲットにします。
- メッセージを送信するときに、最新のユーザー、オファー、およびロイヤルティの情報を活用します。
- プロモーションやロイヤルティ活動の進捗状況や完了について、顧客に詳細な通知を行います。
- 新しいオファーが付与されたときに顧客に通知し、オファーの詳細を提供します。

## SessionMとBrazeの統合

### ステップ1:Brazeでセグメンテーションを作成する

Brazeで、SessionMのプロモーションやオファーでターゲットとするユーザーのセグメンテーションを作成する。 

![カスタム属性」フィルターを選択したセグメンテーションビルダー。]({% image_buster /assets/img/sessionm/CreateSegment.png %})

### ステップ 2:Braze のセグメントをSessionM にインポートする

#### オプション 1: SessionM Tagエンドポイントにエクスポートする（推奨）。

まず、BrazeでWebhookキャンペーンを作成し、Webhook URLを{% raw %}`{{endpoint_core}}/priv/v1/apps/{{appkey_core}}/users/{{${user_id}}}/tags`{% endraw %} に設定する。Liquid を使って、URL 内で`user_id` を定義します。 

生テキストの**リクエストボディ**を使用して、SessionM のユーザープロファイルに追加する希望のタグと、必要な存続時間を含む、Webhook 本文を作成します。例は次のとおりです。

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
    \- 対応する値`application/json`を持つキー`Content-Type`を作成する
    \- 対応する値`Basic YOUR-ENCODED-STRING-KEY`を持つキー`Authorization`を作成します。エンドポイントのエンコードされた文字列キーについては、SessionM チームに問い合わせること。 

![Webhookの設定。]({% image_buster /assets/img/sessionm/SessionMWebhookSettings.png %}){: style="max-width:85%;"}

配信をスケジュールし、[以前に作成した](#step-1-create-a-segment-in-braze)セグメントをターゲットとするように**ターゲットオーディエンス**を設定してから、キャンペーンを開始します。

{% alert important %}
このプロセスは、Postman などのAPI クライアントを使用して、[SessionM のタグエンドポイント](https://docs.sessionm.com/developer/APIs/Core/Customers/customers_tags.htm#create-or-increment-a-customer-tag)にリクエストを直接送信することでも実行できます。この場合、リクエストには顧客、タグ名、各ユーザーの存続時間 (1回の呼び出しにつき1ユーザー) を指定します。
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

Braze セグメンターを使用してBraze セグメントをエクスポートし、タグ付けする顧客、タグ名、ファイル内の各ユーザーの存続期間を含む CSV ファイルを SessionM に提供します。

## Braze でリアルタイムのオファーウォレットを取得する

SessionM と Braze を統合することで、コネクテッドコンテンツを使用して、メッセージ送信時に SessionM のユーザーデータをリアルタイムで取り込むことができ、顧客に古い、有効期限が切れた、または既に償還されたロイヤルティオファーを送信するリスクを排除できます。 

次の例では、コネクテッドコンテンツを使用してオファーウォレットデータをメッセージにテンプレート化しています。ただし、コネクテッドコンテンツは、SessionM の接続エンドポイントのいずれでも使用できます。 

### ステップ1:SessionM でオファーを発行する

SessionM は、設定可能ないくつかの異なる内部レバーから顧客にオファーを発行します。発行後、オファーはSessionMが「オファーウォレット」と呼ぶ状態に移されます。

お客様は、必要なアクションを実行するか、ターゲティングを満たす必要があり、SessionM 内でオファーが発行されます。

次に SessionM は、発行済みの状態で顧客のウォレットにオファーを追加します。

### ステップ2:SessionM オファーウォレット API を呼び出す

SessionM オファーのあるキャンペーンまたはキャンバスステップで、[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/)を使用して、[SessionM`get_user_offers` エンドポイント](https://domains-connecteast1.ent-sessionm.com/offers/swagger/ui/index#!/InfoV232583210323232323232323232323232This32API32allows32for32the32querying32of32information32about32offers32in32a32read45only32fashion4610323232323232323232323232May32be32initiated32by32the32dashboard32or32the32mobile32app4610323232323232323232323232/InfoV2_GetUserOffers/)に API コールを行います。

コネクテッドコンテンツリクエストで、ユーザーの SessionM `user_id` と `retailer_id` を指定して、顧客のウォレットにあるアクティブなオファーの完全なリストを取得します。このエンドポイントへの各リクエストは、1人のユーザーを含むことができる。コネクテッドコンテンツ呼の基本認証ヘッダー用のエンコードされた文字列キーについては、SessionMチームに問い合わせること。

リクエスト本文では、`culture` のデフォルトは `en-US` ですが、Liquid を使用して、多言語 SessionM オファー用にユーザーの言語をテンプレート化することができます (たとえば、"{% raw %}`"culture":"{{${language}}}"`{% endraw %}"を使用します)。

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

リクエストがエンドポイントに行われた後、SessionM は各オファーの完全な詳細とともに、発行された状態のオファーの完全なリストを返します。これは返されたレスポンシブの例である：

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

Liquid ドット記法を使えば、これをメッセージに入力できます。たとえば、結果として得られる `offer_id` でメッセージをパーソナライズするには、`100` を返す {% raw %}`{{wallet.payload.available_points}`{% endraw %} を使用してリターンペイロードを活用できます。

{% alert note %}
これは個別のAPIである。500ユーザーを超えるバッチを送信する場合は、SessionMアカウントチームに連絡して、統合にバルクデータを組み込む方法について問い合わせること。
{% endalert %}

## トリガーメッセージの設定

SessionMとBrazeの統合により、ユーザープロファイルのデータ、オファーの詳細、ポイント残高がメッセージングにダイナミックな形で入力され、アクションの時点で顧客にリアルタイムで送信される。

### ステップ1:SessionMデリバリーチームがテンプレートを設定する

SessionM デリバリーチームと協力して、トリガーされたメッセージングで使用するテンプレートを開発します。SessionMは、ユーザープロファイルのデータ、オファーの詳細、ポイント残高をメッセージングに挿入し、Brazeでトリガーすることで、リアルタイムでの顧客メッセージングを実現する。

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

- **データを提供する：** `offer_id`、`offer title`、`user offer id`、`description`、`terms and conditions`、`logo`、`pos discount id`、`expiration date`
- **ポイント付与データ：** `point award amount`、`point account name`
- **イベントのトリガーデータ：**トリガー/送信Webhookの結果を利用するトリガーイベント内のすべてのデータ。
- **キャンペーン専用データ：** `campaign runtime`、`campaign_id`、`campaign name`、`campaign custom data`

追加フィールドは、メッセージをパーソナライズするための`trigger_properties` としてBrazeに送信される。 

### ステップ2:Brazeキャンペーンまたはキャンバスを作成する

SessionM によってトリガーされる API トリガーのキャンペーンまたはキャンバスを Braze で作成します。`offer_id` や `offer title` などの追加フィールドが設定されている場合は、Liquid (例えば{% raw %}`{{api_trigger_properties.${offer_id}}}`{% endraw %}) を使用して、パーソナライズされたフィールドをメッセージングに追加します。

![APIトリガーのプロパティ。]({% image_buster /assets/img/sessionm/apiTriggerProperties.png %})

[**配信のスケジュール**] タブで、キャンペーンまたはキャンバス ID をメモします。これは SessionM キャンペーンの**高度な設定**に追加されます。

![APIトリガーキャンペーン。]({% image_buster /assets/img/sessionm/apiTriggerCampaign.png %})

キャンペーンまたはキャンバスの詳細を確定し、「**Launch**」を選択する。 

### ステップ 3:SessionMのプロモーションやメッセージングキャンペーンを行う

次に、SessionMでキャンペーンを作成する。

![SessionMキャンペーン作成。]({% image_buster /assets/img/sessionm/SessionMCampaignCreation.png %})

SessionMキャンペーンの詳細設定を更新して、`braze_campaign_id` または`braze_canvas_id` を含む以下のJSONペイロードを含めること。

{% raw %}
```
{
"braze_campaign_id": "{{CAMPAIGN ID}}",
"braze_canvas_id": "{{CANVAS ID}}",
}
```
{% endraw %}

![SessionMの詳細設定。]({% image_buster /assets/img/sessionm/SessionMAdvancedSettings.png %}){: style="max-width:85%;"}

スケジュールやビヘイビアに関するメッセージトリガーを作成する。次に、**外部メッセージ**メニューの**メッセージングバリアント**として **Braze メッセージングバリアント**を選択し、テンプレートを使用します。

![SessionMの外部メッセージ。]({% image_buster /assets/img/sessionm/SessionMExternalMessage.png %})

このテンプレートは、関連するスタティック属性とダイナミックな属性を引き出し、Brazeエンドポイントにコールアウトする。

![セッションM Brazeテンプレート。]({% image_buster /assets/img/sessionm/SessionMBrazeTemplate.png %}){: style="max-width:85%;"}
