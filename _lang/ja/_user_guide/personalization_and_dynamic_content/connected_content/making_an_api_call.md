---
nav_title: コネクテッドコンテンツ呼び出しを実行する
article_title: 接続されたコンテンツAPI コールの実行
page_order: 0
description: "この記事では、コネクテッドコンテンツ API 呼び出しを行う方法と、役立つサンプル、および高度なコネクテッドコンテンツのユースケースについて説明します。"
search_rank: 2
---

# [![Brazeラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/connected-content){: style="float:right;width:120px;border:0;" class="noimgborder"} コネクテッドコンテンツAPIコールの作成

> コネクテッド・コンテンツを使えば、ユーザーに送るメッセージに、APIでアクセスできるあらゆる情報を直接挿入することができる。Web サーバーから直接、またはパブリックにアクセス可能な API からコンテンツをプルできます。<br><br>このページではコネクテッドコンテンツ API 呼び出しの方法、高度なコネクテッドコンテンツユースケース、エラー処理などについて説明します。

## コネクテッドコンテンツ呼び出しを送信する

{% raw %}

コネクテッドコンテンツ呼び出しを送信するには、`{% connected_content %}` タグを使用します。このタグでは、`:save` を使用して変数を割り当てたり宣言したりできます。これらの変数の内容には、メッセージの後の方で [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid) を使って参照できます。

たとえば、次のメッセージ本文は、`http://numbersapi.com/random/trivia` という URL にアクセスし、メッセージに楽しいトライビアを含めます。

```
{% connected_content http://numbersapi.com/random/trivia :save result %}
Hi there, here is some fun trivia for you!: {{result.text}}
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

エンドポイントがJSON を返す場合は、`connected` の値がnull であるかどうかを確認して、[条件付きでメッセージ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/) を中止することで、そのことを検出できます。Braze では、ポート 80 (HTTP) と 443 (HTTPS) を介して通信する URL のみが許可されます。

### 不健全ホストの検出

コネクテッドコンテンツは、不健全ホストの検出メカニズムを採用して、タイムアウト、過剰なリクエスト、または Braze がターゲットエンドポイントと正常に通信することを妨げるその他の結果が発生する原因となる、ターゲットホストの著しい速度低下または過負荷の発生を検出します。これは、ターゲットホストに問題を引き起こす可能性のある不必要な負荷を軽減するための保護手段として機能します。また、Brazeインフラストラクチャを安定化し、高速メッセージング速度を維持するのにも役立ちます。

ターゲットホストが高率に著しい速度低下や過負荷に見舞われた場合、Brazeはターゲットホストへのリクエストを一時的に1分間停止し、代わりに障害を示すレスポンスをシミュレートする。1分後、Brazeは少数のリクエストを使ってホストの健全性を調査し、ホストが健全であることが判明した場合、リクエストをフルスピードで再開する。ホストがまだ不健全である場合、Braze はもう1分待ってから再試行します。

ターゲットホストへのリクエストが不健全ホスト検出器によって停止された場合、Braze はメッセージのレンダリングを続行し、エラー応答コードを受け取ったかのように Liquid ロジックに従います。これらのコネクテッドコンテンツリクエストが不健全なホスト検出器によって停止されたときに再試行されるようにするには、`:retry` オプションを使用します。`:retry` オプションの詳細については、[コネクテッドコンテンツの再試行]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries)を参照してください。

不健全なホスト検出が問題を引き起こしている可能性がある場合は、[Braze サポート]({{site.baseurl}}/support_contact/)にお問い合わせください。

{% alert note %}
コネクテッドコンテンツに使用する特定のURLを許可することができる。この機能を利用するには、カスタマー・サクセス・マネージャーに連絡すること。
{% endalert %}

{% alert tip %}
一般的なエラーコードのトラブルシューティング方法については、[Webhookおよびコネクテッドコンテンツリクエストのトラブルシューティングを]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors#unhealthy-host-detection)参照。
{% endalert %}

## 効率的なパフォーマンスを可能にする

Braze はメッセージを非常に高速で配信するため、サーバーが数千の同時接続を処理できるようにして、コンテンツをプルダウンするときにサーバーが過負荷状態にならないようにしてください。パブリック API を使用する場合は、API プロバイダーが使用するレート制限に違反していないことを確認してください。パフォーマンス上の理由から、Braze ではサーバーの応答時間が 2 秒未満であることを必要としています。サーバーの応答に 2 秒以上かかる場合、コンテンツは挿入されません。

Braze は、各受信者に複数回、同じコネクテッドコンテンツ API 呼び出しを行うことができます。これは、状況によっては Braze がメッセージペイロードを表示するためにコネクテッドコンテンツ API 呼び出しを行う必要があり、メッセージペイロードは、検証、再試行ロジック、またはその他の内部目的のために、受信者ごとに複数回レンダリングされることがあるためです。システムは、各受信者につき複数回、同じコネクテッドコンテンツ API 呼び出しの処理を行わなければなりません。

## 知っておくべきこと

* BrazeはAPIコールには課金せず、データポイント使用量にはカウントしない。
* コネクテッドコンテンツ応答には1 MB の制限があります。
* コネクテッドコンテンツ呼び出しは、メッセージの送信時に行われます。ただし、アプリ内メッセージは、メッセージが表示されたときにこの呼び出しを行います。
* コネクテッドコンテンツ呼び出しはリダイレクトに従いません。

## 認証タイプ

### 基本認証の使用

URLにBasic認証が必要な場合、BrazeはAPIコールで使用するBasic認証情報を保存することができる。**設定**＞**コネクテッドコンテンツで**、既存のベーシック認証情報を管理し、新しい認証情報を追加できる。

![ダッシュボードのコネクテッドコンテンツ設定。]({% image_buster /assets/img/connected_content/basic_auth_mgmt.png %})

新しい認証情報を追加するには、「**Add credential（認証情報の追加**）」 > 「**Basic authentication（基本認証**）」を選択する。 

!["認証情報の追加 "ドロップダウンには、ベーシック認証またはトークン認証を使用するオプションがある。]({% image_buster /assets/img/connected_content/add_credential_button.png %}){: style="max-width:60%"}

認証情報に名前を付け、ユーザーの名前とパスワードを入力します。

![名前、ユーザ名、パスワードを入力するオプションのある "Create New Credential "ウィンドウが表示される。]({% image_buster /assets/img/connected_content/basic_auth_token.png %}){: style="max-width:60%"}

次に、トークンの名前を参照することで、API 呼び出しでこの基本的な認証情報を使用できます。

{% raw %}
```
Hi there, here is some fun trivia for you!: {% connected_content https://yourwebsite.com/random/trivia :basic_auth credential_name %}
```
{% endraw %}

{% alert note %}
認証情報を削除する場合、これを使用しようとしているコネクテッドコンテンツ呼び出しはすべて中止されることに注意してください。
{% endalert %}

### トークン 認証の使用

Braze コネクテッドコンテンツを使用する場合、特定の API では、ユーザー名とパスワードの代わりにトークンが必要になることがあります。Brazeは、トークン認証ヘッダー値を保持する認証情報を保存することもできる。

トークン値を保持する認証情報を追加するには、「**Add credential（認証情報の追加**）」 > 「**Token authentication（トークン認証**）」を選択する。次に、APIコールヘッダーと許可ドメインのキーと値のペアを追加する。

![トークン認証の詳細が記載されたトークンの例"token_credential_abc" 。]({% image_buster /assets/img/connected_content/token_auth.png %}){: style="max-width:60%"}

そして、認証情報名を参照することで、APIコールでこの認証情報を使用することができる：

{% raw %}
```
{% assign campaign_name="New Year Sale" %}
{% connected_content
     https://api.endpoint.com/your_path
     :method post
     :auth_credentials token_credential_abc
     :body campaign={{campaign_name}}&customer={{${user_id}}}&channel=Braze
     :content_type application/json
     :save publication
%}
```
{% endraw %}

### オープン認証(OAuth)の使用

一部の API 設定では、アクセスする API エンドポイントの認証に使用できるアクセストークンを取得する必要があります。

#### ステップ1:アクセストークンを取得する

次の例は、アクセストークンを取得してローカル変数に保存し、後続の API 呼び出しの認証に使用できるようにする方法を示しています。パラメーター `:cache_max_age` を追加して、アクセストークンの有効期間を照合し、アウトバウンドコネクテッドコンテンツ呼び出しの回数を減らすことができます。詳細については、[設定可能なキャッシュ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/local_connected_content_variables/#configurable-caching)を参照してください。

{% raw %}
```
{% connected_content
     https://your_API_access_token_endpoint_here/
     :method post
     :auth_credentials access_token_credential_abc
     :headers {
       "Content-Type": "YOUR-CONTENT-TYPE"
     }
     :cache_max_age 900
     :save token_response
%}
```
{% endraw %}

#### ステップ2:取得したアクセストークンを使用して API を承認する

トークンが保存されたので、これをダイナミックなコネクテッドコンテンツ呼び出しにテンプレート化して、リクエストを承認できます。

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

### 認証情報を編集する

認証タイプの認証情報を編集することができる。

- ベーシック認証では、ユーザー名とパスワードを更新することができる。以前に入力したパスワードは表示されないことに注意。
- トークン認証では、ヘッダーのキーと値のペアと許可ドメインを更新することができる。以前に設定したヘッダー値は表示されないことに注意。

![認証情報を編集するオプション。]({% image_buster /assets/img/connected_content/edit_credentials.png %}){: style="max-width:60%"}

## コネクテッドコンテンツ IP の許可リスト

コネクテッドコンテンツを使用したメッセージが Braze から送信されると、Braze サーバーは、自動的に顧客またはサードパーティのサーバーにネットワークリクエストを行い、データをプルバックします。IP allowlistingを使えば、コネクテッドコンテンツのリクエストが実際にBrazeから来ていることを確認でき、セキュリティのレイヤーが増える。

Braze は、次のIP 範囲から接続コンテンツリクエストを送信します。リストされている範囲は自動的に追加され、許可リストにオプトインされているすべての API キーにダイナミックに追加されます。 

Braze には、すべてのサービスに使用される一連の予約済み IP があります。これらの ＩＰ はすべて一度にアクティブになるわけではありません。これは、Braze が別のデータセンターから送信したり、保守を行ったりするために、顧客に影響を与えないように設計されています。Braze は、コネクテッドコンテンツリクエストを作成するときに、以下の IP のいずれか 1 つ、サブセット、またはすべてを使用できます。

{% multi_lang_include data_centers.md datacenters='ips' %}

### `User-Agent` ヘッダー

Brazeは、すべてのコネクテッドコンテンツとWebhookリクエストに、以下のような`User-Agent` ヘッダーを含む：

```text
Braze Sender 75e404755ae1270441f07eb238f0faf25e44dfdc
```

{% alert tip %}
ハッシュ値は定期的に変更されることを覚えておいてほしい。`User-Agent` でトラフィックをフィルターしている場合、`Braze Sender` で始まるすべての値を許可する。
{% endalert %}

## トラブルシューティング

コネクテッドコンテンツ呼び出しのトラブルシューティングには、[Webhook.site](https://webhook.site/) を使用します。 

1. コネクテッドコンテンツ呼び出しの URL を、サイトで生成された一意の URL に切り替えます。
2. キャンペーンまたはキャンバスステップをプレビューしてテストし、リクエストがこの Web サイトを介して処理されることを確認します。

このツールを使用して、リクエストヘッダー、リクエスト本文、および呼び出しで送信される他の情報に関する問題を診断できます。

## よくある質問

### コネクテッド・コンテンツのコールがユーザーや送信数より多いのはなぜか？ 

メッセージペイロードをレンダリングするためにコネクテッドコンテンツ API 呼び出しを実行する必要があるため、Braze は受信者ごとに同じコネクテッドコンテンツ API 呼び出しを複数回実行することがあります。検証、再試行ロジック、その他の内部目的で、受信者ごとにメッセージペイロードを複数回レンダリングできます。

コネクテッドコンテンツ API 呼び出しは、再試行ロジックがその呼び出しで使用されていない場合でも、受信者ごとに複数回行われることが予想されます。コネクテッドコンテンツを含むメッセージのレート制限を設定するか、予想される量を処理できるようにサーバーを設定することをお勧めします。

### コネクテッドコンテンツでレート制限はどのように機能するのか？

コネクテッドコンテンツには専用のレート制限がありません。その代わり、レート制限はメッセージ送信レートに基づいている。コネクテッドコンテンツ呼び出しの回数が送信されたメッセージよりも多い場合は、メッセージングのレート制限をコネクテッドコンテンツのレート制限よりも低く設定することをお勧めします。  

### キャッシュ動作とは何か？

デフォルトでは、POSTリクエストはキャッシュしない。ただし `:cache_max_age` パラメータを追加することで、POST 呼び出しを強制的にキャッシュさせることができます。

キャッシュは、コネクテッドコンテンツの重複コールを削減するのに役立ちます。しかし、ユーザーごとにコネクテッド・コンテンツの呼び出しが1回になるとは限らない。

### コネクテッドコンテンツHTTPのデフォルト動作とは？ 

{% multi_lang_include connected_content.md section='default behavior' %}

{% multi_lang_include connected_content.md section='http post' %}
