---
nav_title: API コールの実行
article_title: 接続されたコンテンツAPI コールの実行
page_order: 0
description: "この記事では、コネクテッドコンテンツ API 呼び出しを行う方法と、役立つサンプル、および高度なコネクテッドコンテンツのユースケースについて説明します。"
search_rank: 2
---

# [![Brazeラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/connected-content){: style="float:right;width:120px;border:0;" class="noimgborder"}API 呼び出し

> コネクテッドコンテンツを使用して、ユーザーに送信するメッセージに API を介して直接アクセス可能な情報を挿入します。Web サーバーから直接、またはパブリックにアクセス可能な API からコンテンツをプルできます。

## コネクテッドコンテンツタグ

{% raw %}

コネクテッドコンテンツ呼び出しを送信するには、`{% connected_content %}` タグを使用します。このタグでは、`:save` を使用して変数を割り当てたり宣言したりできます。これらの変数の内容には、メッセージの後の方で [Liquid][2] を使って参照できます。

たとえば、次のメッセージ本文は、`http://numbersapi.com/random/trivia` という URL にアクセスし、メッセージに楽しいトライビアを含めます。

```
{% connected_content http://numbersapi.com/random/trivia :save result %}
Hi there, here is fun some trivia for you!: {{result.text}}
```

### 変数の追加

また、コネクテッドコンテンツリクエストを作成するときに、URL 文字列に変数としてユーザープロファイル 属性を含めることもできます。 

たとえば、ユーザーのメールの住所とID に基づいてコンテンツを返すウェブサービスがあるとします。アットマーク (@) などの特殊文字を含む属性を渡す場合は、URL で使用できない文字を URL フレンドリなエスケープバージョンで置き換えるために、Liquid フィルター `url_param_escape` を必ず使用してください (次のメールアドレス属性を参照)。

```
Hi, here are some articles that you might find interesting:

{% connected_content http://www.yourwebsite.com/articles?email={{${email_address} | url_param_escape}}&user_id={{${user_id}}} %}
```
{% endraw %}
{% alert note %}
Liquid 構文のバージョン内で適切に動作するには、属性値を `${}` で囲む必要があります。
{% endalert %}

接続コンテンツリクエストは、GET およびPOST リクエストのみをサポートします。

## エラー処理

URL が使用できず、404 ページに達すると、Braze はその場所に空の文字列を表示します。URL がHTTP 500 または502 ページに達すると、URL は再試行ロジックで失敗します。

エンドポイントがJSON を返す場合は、`connected` の値がnull であるかどうかを確認して、[条件付きでメッセージ][1] を中止することで、そのことを検出できます。Braze では、ポート 80 (HTTP) と 443 (HTTPS) を介して通信する URL のみが許可されます。

### 不健全ホストの検出

コネクテッドコンテンツは、不健全ホストの検出メカニズムを採用して、タイムアウト、過剰なリクエスト、または Braze がターゲットエンドポイントと正常に通信することを妨げるその他の結果が発生する原因となる、ターゲットホストの著しい速度低下または過負荷の発生を検出します。これは、ターゲットホストに問題を引き起こす可能性のある不必要な負荷を軽減するための保護手段として機能します。また、Brazeインフラを安定させ、高速メッセージング速度を維持する役割も果たしている。

ターゲットホストが高率に著しい速度低下や過負荷に見舞われた場合、Brazeは一時的にターゲットホストへのリクエストを1分間停止し、代わりに障害を示すレスポンスをシミュレートする。1分後、Brazeは少数のリクエストを使ってホストの健全性を調査し、ホストが健全であることが判明した場合、リクエストをフルスピードで再開する。ホストがまだ不健全である場合、Braze はもう1分待ってから再試行します。

ターゲットホストへのリクエストが不健全ホスト検出器によって停止された場合、Braze はメッセージのレンダリングを続行し、エラー応答コードを受け取ったかのように Liquid ロジックに従います。これらのコネクテッドコンテンツリクエストが不健全なホスト検出器によって停止されたときに再試行されるようにするには、`:retry` オプションを使用します。`:retry` オプションの詳細については、[コネクテッドコンテンツの再試行]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries)を参照してください。

不健全なホスト検出が問題を引き起こしている可能性がある場合は、[Braze サポート]({{site.baseurl}}/support_contact/)にお問い合わせください。

{% alert tip %}
一般的なエラーコードのトラブルシューティング方法については、[Webhookおよびコネクテッドコンテンツリクエストのトラブルシューティングを]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors#unhealthy-host-detection)参照。
{% endalert %}

## パフォーマンス

Braze はメッセージを非常に高速で配信するため、サーバーが数千の同時接続を処理できるようにして、コンテンツをプルダウンするときにサーバーが過負荷状態にならないようにしてください。パブリック API を使用する場合は、API プロバイダーが使用するレート制限に違反しないように使用してください。Braze では、パフォーマンス上の理由からサーバーの応答時間が2 秒未満である必要があります。サーバーの応答時間が2 秒を超えると、その内容は挿入されません。

Braze は、各受信者に複数回、同じコネクテッドコンテンツ API 呼び出しを行うことができます。これは、状況によっては Braze がメッセージペイロードを表示するためにコネクテッドコンテンツ API 呼び出しを行う必要があり、メッセージペイロードは、検証、再試行ロジック、またはその他の内部目的のために、受信者ごとに複数回レンダリングされることがあるためです。システムは、各受信者につき複数回、同じコネクテッドコンテンツ API 呼び出しの処理を行わなければなりません。

## 知っておくべきこと

* Braze は API 呼び出しについて課金せず、指定のデータポイント割り当てにはカウントされません。
* コネクテッドコンテンツ応答には 1 MB の制限があります。
* コネクテッドコンテンツ呼び出しは、メッセージの送信時に行われます。ただし、アプリ内メッセージは、メッセージが表示されたときにこの呼び出しを行います。
* コネクテッドコンテンツ呼び出しはリダイレクトに従いません。

## 認証タイプ

### 基本認証の使用

URL に基本的な認証が必要な場合、Braze は API 呼び出しで使用するための基本的な認証情報を生成できます。既存の基本的な認証情報を管理したり、[**設定**] > [**コネクテッドコンテンツ**] から新しいものを追加したりできます。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation) を使用している場合、**Connected Content** は**設定の管理** にあります。
{% endalert %}

![Braze ダッシュボードの「コネクテッドコンテンツ」の設定。][34]

新しい認証情報を追加するには、**認証情報**を追加します。認証情報に名前を付け、ユーザーの名前とパスワードを入力します。

![名前、ユーザー名、パスワードを入力するオプションがある [新しい認証情報の作成] ウィンドウ。][35]{: style="max-width:30%" }

次に、トークンの名前を参照することで、API 呼び出しでこの基本的な認証情報を使用できます。

{% raw %}
```
Hi there, here is fun some trivia for you!: {% connected_content https://yourwebsite.com/random/trivia :basic_auth credential_name %}
```
{% endraw %}

{% alert note %}
認証情報を削除する場合、これを使用しようとしているコネクテッドコンテンツ呼び出しはすべて中止されることに注意してください。
{% endalert %}

### トークン 認証の使用

Braze コネクテッドコンテンツを使用する場合、特定の API では、ユーザー名とパスワードの代わりにトークンが必要になることがあります。次の呼び出しに含まれているのは、メッセージを参照し、それをメッセージのモデルとして使用するためのコードスニペットです。

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

一部の API 設定では、アクセスする API エンドポイントの認証に使用できるアクセストークンを取得する必要があります。

#### アクセストークンを取得する

次の例は、アクセストークンを取得してローカル変数に保存し、後続の API 呼び出しの認証に使用できるようにする方法を示しています。パラメーター `:cache_max_age` を追加して、アクセストークンの有効期間を照合し、アウトバウンドコネクテッドコンテンツ呼び出しの回数を減らすことができます。詳細については、[構成可能なキャッシュ][36] を参照してください。

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

#### 取得したアクセストークンを使用して API を承認する

これでトークンが保存されたので、これをダイナミックなコネクテッドコンテンツ呼び出しにテンプレート化して、リクエストを承認できます。

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

## コネクテッドコンテンツ IP の許可リスト

コネクテッドコンテンツを使用したメッセージが Braze から送信されると、Braze サーバーは、自動的に顧客またはサードパーティのサーバーにネットワークリクエストを行い、データをプルバックします。IP 許可リストを使用すると、コネクテッドコンテンツリクエストが実際に Braze から送信されていることを確認し、セキュリティレイヤーを追加することができます。

Braze は、次のIP 範囲から接続コンテンツリクエストを送信します。リストされている範囲は自動的に追加され、許可リストにオプトインされているすべての API キーにダイナミックに追加されます。 

Braze には、すべてのサービスに使用される一連の予約済み IP があります。これらの ＩＰ はすべて一度にアクティブになるわけではありません。これは、Braze が別のデータセンターから送信したり、保守を行ったりするために、顧客に影響を与えないように設計されています。Braze は、コネクテッドコンテンツリクエストを作成するときに、以下の IP のいずれか 1 つ、サブセット、またはすべてを使用できます。

| インスタンス `US-01`、`US-02`、`US-03`、`US-04`、`US-05`、`US-06`、`US-07` の場合:  |
|---|
| `23.21.118.191`
| `34.206.23.173`
| `50.16.249.9`
| `52.4.160.214`
| `54.87.8.34`
| `54.156.35.251`
| `52.54.89.238`
| `18.205.178.15`

| インスタンス `EU-01` と `EU-02` の場合:  |
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

| インスタンス `US-08` の場合:  |
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

コネクテッドコンテンツ呼び出しのトラブルシューティングには、[Webhook.site](https://webhook.site/) を使用します。 

1. コネクテッドコンテンツ呼び出しの URL を、サイトで生成された一意の URL に切り替えます。
2. キャンペーンまたはキャンバスステップをプレビューしてテストし、リクエストがこの Web サイトを介して処理されることを確認します。

このツールを使用して、リクエストヘッダー、リクエスト本文、および呼び出しで送信される他の情報に関する問題を診断できます。

[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/
[2]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#liquid-usage-use-cases--overview
[16]: [success@braze.com](mailto:success@braze.com)
[34]: {% image_buster /assets/img_archive/basic_auth_mgmt.png %}
[35]: {% image_buster /assets/img_archive/basic_auth_token.png %}
[36]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/local_connected_content_variables/#configurable-caching
