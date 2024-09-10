---
nav_title: API コールの実行
article_title: 接続されたコンテンツAPI コールの実行
page_order: 0
description: "このリファレンス記事では、Connected Content API 呼び出しの方法、役立つサンプル、高度なConnected Content ユースケースについて説明します。"
search_rank: 2
---

# [![Brazeラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/connected-content){: style="float:right;width:120px;border:0;" class="noimgborder"}API 呼び出し

> 接続コンテンツを使用して、ユーザー s に送信するメッセージにAPI を介して直接アクセス可能な情報を挿入します。Web サーバーから直接、またはパブリックにアクセス可能なAPI からコンテンツをプルできます。

## 接続内容タグ

{% raw %}

接続内容呼び出しを送信するには、`{% connected_content %}` タグを使用します。このタグでは、`:save` を使用して変数を割り当てたり宣言したりできます。これらの変数の側面は、メッセージの後で[Liquid][2] で参照できます。

たとえば、次のメッセージ本文は、URL `http://numbersapi.com/random/trivia` にアクセスし、メッセージに面白いトライビアファクトを含めます。

```
{% connected_content http://numbersapi.com/random/trivia :save result %}
Hi there, here is fun some trivia for you!: {{result.text}}
```

### 変数の追加

また、接続コンテンツリクエストを作成するときに、URL 文字列に変数としてユーザープロファイル 属性s を含めることもできます。 

たとえば、ユーザーのメールの住所とID に基づいてコンテンツを返すウェブサービスがあるとします。アットマーク(@) などの特殊文字を含む属性s を渡す場合は、URL で許可されていない文字をURL フレンドリエスケープバージョンで置き換えるために、リキッドフィルター`url_param_escape` を使用するようにしてください(次のメール住所属性を参照)。

```
Hi, here are some articles that you might find interesting:

{% connected_content http://www.yourwebsite.com/articles?email={{${email_address} | url_param_escape}}&user_id={{${user_id}}} %}
```
{% endraw %}
{% alert note %}
Liquid 構文のバージョン内で適切に動作するには、属性値を`${}` で囲む必要があります。
{% endalert %}

接続コンテンツリクエストは、GET およびPOST リクエストのみをサポートします。

## エラー処理

URL が使用できず、404 ページに達すると、Braze はその場所に空の文字列を表示します。URL がHTTP 500 または502 ページに達すると、URL は再試行ロジックで失敗します。

エンドポイントがJSON を返す場合は、`connected` の値がnull であるかどうかを確認して、[条件付きでメッセージ][1] を中止することで、そのことを検出できます。Braze では、ポート80 (HTTP) と443 (HTTPS) を介して通信するURL のみが許可されます。

## パフォーマンス

Braze はメッセージを非常に高速で配信するため、サーバーが数千の同時接続を処理できるようにして、コンテンツをプルダウンするときにサーバーが読み込むを乗り越えないようにしてください。パブリックAPI を使用する場合は、API プロバイダーが使用するレート制限に違反しないように使用してください。Braze では、パフォーマンス上の理由からサーバーの応答時間が2 秒未満である必要があります。サーバーの応答時間が2 秒を超えると、その内容は挿入されません。

Brazeは、1受信者に複数回、同じConnected Content API呼び出しを行うことができます。これは、Braze がメッセージペイ読み込むを表示するために接続コンテンツAPI 呼び出しを行う必要がある場合があるためです。また、メッセージペイ読み込むは、検証、再試行ロジック、または他の内部のために、受信者ごとに複数回レンダリングできます。1受信者に1回以上、同じ接続内容の呼び出しを許容できる必要があります。

## 知っておくべきこと

* Braze はAPI コールの料金を請求せず、指定されたデータポイント割り当てにはカウントされません。
* Connected Content レスポンスには1MB の制限があります。
* 接続されたコンテンツコールは、メッセージが送信されるとh をアプリします。ただし、アプリ内メッセージs は、メッセージが表示されたときにこのコールを発信します。
* 接続されたコンテンツコールはリダイレクトに従いません。

## 認証タイプ

### 基本認証の使用

URL に基本的な認証が必要な場合、Braze はAPI 呼び出しで使用するための基本的な認証 認証情報を生成できます。既存の基本認証 認証情報s を管理し、**Settings**> **Connected Content** から新しいものを追加できます。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation) を使用している場合、**Connected Content** は**設定の管理** にあります。
{% endalert %}

![][34]

新しい認証情報を追加するには、**認証情報**を追加します。認証情報に名前を付け、ユーザーの名前とパスワードを入力します。

![][35]{: style="max-width:30%" }

次に、トークンの名前を参照することで、API 呼び出しでこの基本認証 認証情報を使用できます。

{% raw %}
```
Hi there, here is fun some trivia for you!: {% connected_content https://yourwebsite.com/random/trivia :basic_auth credential_name %}
```
{% endraw %}

{% alert note %}
認証情報を削除する場合、使用しようとしている接続コンテンツコールはすべて中止されることに注意してください。
{% endalert %}

### トークン 認証の使用

Braze 接続コンテンツを使用する場合、特定のAPI では、ユーザーの名前とパスワードの代わりにトークンが必要になることがあります。次の呼び出しに含まれているのは、メッセージをリファレンスし、モデル化するためのコードな抜粋です。

{% raw %}
```
{% assign campaign_name="New Year Sale" %}
{% connected_content
     https://your_API_link_here/
     :method post
     :headers {
       "X-App-Id": "YOUR-APP-ID",
       "X-App-Token": "YOUR-APP-TOKEN"
  }
     :body campaign={{campaign_name}}&customer={{${user_id}}}&channel=Braze
     :content_type application/json
     :save publication
%}
```
{% endraw %}

### オープン認証(OAuth)の使用

一部のAPI 設定では、アクセスするAPI エンドポイントの認証に使用できるアクセストークンを取得する必要があります。

#### 接続トークンを取得する

次の例は、アクセストークンを取得してローカル変数に保存し、後続のAPI 呼び出しの認証に使用できるようにする方法を示しています。`:cache_max_age`パラメータを追加して、アクセストークンが有効な時刻を照合し、発信接続コンテンツコールの回数を減らすことができます。詳細については、\[構成可能なキャッシュ][36]] を参照してください。

{% raw %}
```
{% connected_content
     https://your_API_access_token_endpoint_here/
     :method post
     :headers {
       "Content-Type": "YOUR-CONTENT-TYPE",
       "Authorization": "Bearer YOUR-APP-TOKEN"
  }
     :cache_max_age 900
     :save token_response
%}
```
{% endraw %}

#### 取得したアクセストークンを使用してAPI を許可する

これでトークンが保存されたので、dをダイナミックな接続内容呼び出しにテンプレートして、リクエストを承認できます。

{% raw %}
```
{% connected_content
     https://your_API_endpoint_here/
     :headers {
       "Content-Type": "YOUR-CONTENT-TYPE",
       "Authorization": "{{token_response}}"
  }
     :body key1=value1&key2=value2
     :save response
%}
```
{% endraw %}

## 接続されたコンテンツIP の許可

Brazeサーバーは、Connected Contentを使用したメッセージをBrazeから送信すると、自動的に顧客またはサードパーティのサーバーにネットワークリクエストを行い、データをプルバックします。IP allowlisting を使用すると、Connected Content リクエストが実際にBraze から送信されていることを確認し、セキュリティレイヤーを追加できます。

Braze は、次のIP 範囲から接続コンテンツリクエストを送信します。リストされている範囲は自動的に追加され、allowlisting にオプトインされているすべてのAPI キーにダイナミックな追加されます。 

Braze には、すべてのサービスに使用される予約のIP があります。すべてのIP が一度に有効になるわけではありません。これは、Brazeが別のデータセンタから送信したり、保守を行ったりするために、顧客に影響を与えることなく設計されています。Brazeは、接続コンテンツリクエストを作成するときに、以下のIPの1つ、サブセット、またはすべてを使用できます。

| インスタンス`US-01`、`US-02`、`US-03`、`US-04`、`US-05`、`US-06`、`US-07`: |
|---|
| `23.21.118.191`
| `34.206.23.173`
| `50.16.249.9`
| `52.4.160.214`
| `54.87.8.34`
| `54.156.35.251`
| `52.54.89.238`
| `18.205.178.15`

| インスタンス`EU-01` および`EU-02` の場合: |
|---|
| `52.58.142.242`
| `52.29.193.121`
| `35.158.29.228`
| `18.157.135.97`
| `3.123.166.46`
| `3.64.27.36`
| `3.65.88.25`
| `3.68.144.188`
| `3.70.107.88`

| インスタンス`US-08`の場合: |
|---|
| `52.151.246.51`
| `52.170.163.182`
| `40.76.166.157`
| `40.76.166.170`
| `40.76.166.167`
| `40.76.166.161`
| `40.76.166.156`
| `40.76.166.166`
| `40.76.166.160`
| `40.88.51.74`
| `52.154.67.17`
| `40.76.166.80`
| `40.76.166.84`
| `40.76.166.85`
| `40.76.166.81`
| `40.76.166.71`
| `40.76.166.144`
| `40.76.166.145`

## トラブルシューティング

接続コンテンツコールのトラブルシューティングには、[Webhook.site](https://webhook.site/) を使用します。 

1. Connected Content コールのURL をサイトで生成された一意のURL に切り替えます。
2. キャンペーンまたはキャンバスステップをプレビューしてテストし、リクエストがこのWeb サイトを通過するかどうかを確認します。

このツールを使用して、リクエストヘッダーs、リクエストボディ、およびコールで送信されている他の情報に関する問題を診断できます。

[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/
[2]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#liquid-usage-use-cases--overview
[16]: [success@braze.com](mailto:success@braze.com)
[34]: {% image_buster /assets/img_archive/basic_auth_mgmt.png %}
[35]: {% image_buster /assets/img_archive/basic_auth_token.png %}
[36]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/local_connected_content_variables/#configurable-caching
