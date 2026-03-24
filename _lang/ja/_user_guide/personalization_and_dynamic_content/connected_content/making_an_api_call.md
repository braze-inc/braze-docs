---
nav_title: コネクテッドコンテンツ呼び出しを実行する
article_title: コネクテッドコンテンツ API 呼び出しの実行
page_order: 0
description: "このリファレンス記事では、コネクテッドコンテンツ API 呼び出しを行う方法と、役立つサンプル、および高度なコネクテッドコンテンツのユースケースについて説明します。"
search_rank: 2
---

# [![Brazeラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/connected-content){: style="float:right;width:120px;border:0;" class="noimgborder"} コネクテッドコンテンツ API 呼び出しの実行

> コネクテッドコンテンツを使用すると、API でアクセスできるあらゆる情報を、ユーザーに送信するメッセージに直接挿入できます。Web サーバーから直接、またはパブリックにアクセス可能な API からコンテンツをプルできます。<br><br>このページでは、コネクテッドコンテンツ API 呼び出しの方法、高度なコネクテッドコンテンツのユースケース、エラー処理などについて説明します。

## コネクテッドコンテンツの呼び出し量について

{% alert important %}
1回の送信は1回のコネクテッドコンテンツ呼び出しに等しいわけではありません。Braze は、メッセージ送信とコネクテッドコンテンツリクエストの間の1:1の比率を保証しません。システムは、呼び出し回数の最小化よりも、正確なメッセージレンダリングと配信を優先するように設計されています。エンドポイントは、受信者数や送信メッセージ数よりも多くのリクエストを処理できるように構築する必要があります。
{% endalert %}

Braze は、受信者ごとに同じコネクテッドコンテンツ API 呼び出しを複数回実行することがあります。一般的な理由は以下のとおりです。

- **複数パートを持つメール:** 1通のメールで、HTML 本文、プレーンテキスト本文、Accelerated Mobile Pages (AMP) バージョン（存在する場合）のそれぞれに対して個別のレンダリングパスがトリガーされることがあります。各パスでそのパート内のコネクテッドコンテンツがトリガーされるため、1人の受信者が複数の同一または類似の呼び出しを生成する可能性があります。
- **検証と再試行:** メッセージペイロードは、検証、再試行ロジック、またはその他の内部目的のために、受信者ごとに複数回レンダリングされることがあります。
- **チャネルの動作:** コネクテッドコンテンツは、メッセージがレンダリングされるときに実行されます。アプリ内メッセージの場合、メッセージはインプレッション時にレンダリングされます。

ログに送信数や受信者数よりも多くのコネクテッドコンテンツ呼び出しが記録されている場合、それは想定される動作です。負荷の軽減とスケール計画に関するガイダンスについては、[大量エンドポイントのベストプラクティス](#best-practices-for-high-volume-endpoints)を参照してください。

## コネクテッドコンテンツ呼び出しを送信する

{% raw %}

コネクテッドコンテンツ呼び出しを送信するには、`{% connected_content %}` タグを使用します。このタグでは、`:save` を使用して変数を割り当てたり宣言したりできます。これらの変数の内容は、メッセージの後の部分で [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid) を使って参照できます。

たとえば、次のメッセージ本文は、`http://numbersapi.com/random/trivia` という URL にアクセスし、メッセージに楽しいトリビアを含めます。

```
{% connected_content http://numbersapi.com/random/trivia :save result %}
Hi there, here is some fun trivia for you!: {{result.text}}
```

### 変数の追加

コネクテッドコンテンツリクエストを作成するときに、URL 文字列に変数としてユーザープロファイル属性を含めることもできます。

たとえば、ユーザーのメールアドレスと ID に基づいてコンテンツを返す Web サービスがあるとします。アットマーク (@) などの特殊文字を含む属性を渡す場合は、URL で使用できない文字を URL フレンドリなエスケープバージョンに置き換えるために、Liquid フィルター `url_param_escape` を必ず使用してください（次のメールアドレス属性を参照）。

```
Hi, here are some articles that you might find interesting:

{% connected_content http://www.yourwebsite.com/articles?email={{${email_address} | url_param_escape}}&user_id={{${user_id}}} %}
```
{% endraw %}
{% alert note %}
Braze の Liquid 構文内で適切に動作するには、属性値を `${}` で囲む必要があります。
{% endalert %}

コネクテッドコンテンツリクエストは、GET および POST リクエストのみをサポートします。

## エラー処理

URL が使用できず 404 ページに達すると、Braze はその場所に空の文字列をレンダリングします。URL が HTTP 500 または 502 ページに達すると、URL は再試行ロジックで失敗します。

エンドポイントが JSON を返す場合は、`connected` の値が null であるかどうかを確認して、[条件付きでメッセージを中止]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/)することで検出できます。Braze では、ポート 80 (HTTP) と 443 (HTTPS) を介して通信する URL のみが許可されます。

### 不健全ホストの検出

コネクテッドコンテンツは、不健全ホストの検出メカニズムを採用して、ターゲットホストの著しい速度低下または過負荷の発生率が高い場合を検出します。これにより、タイムアウト、過剰なリクエスト、または Braze がターゲットエンドポイントと正常に通信することを妨げるその他の結果が発生します。これは、ターゲットホストに問題を引き起こす可能性のある不必要な負荷を軽減するための保護手段として機能します。また、Braze インフラを安定化し、高速メッセージング速度を維持するのにも役立ちます。

ターゲットホストが高率で著しい速度低下や過負荷に見舞われた場合、Braze はターゲットホストへのリクエストを一時的に1分間停止し、代わりに障害を示すレスポンスをシミュレートします。1分後、Braze は少数のリクエストを使ってホストの健全性を調査し、ホストが健全であることが判明した場合、リクエストをフルスピードで再開します。ホストがまだ不健全である場合、Braze はもう1分待ってから再試行します。

ターゲットホストへのリクエストが不健全ホスト検出器によって停止された場合、Braze はメッセージのレンダリングを続行し、エラー応答コードを受け取ったかのように Liquid ロジックに従います。これらのコネクテッドコンテンツリクエストが不健全ホスト検出器によって停止されたときに再試行されるようにするには、`:retry` オプションを使用します。`:retry` オプションの詳細については、[コネクテッドコンテンツの再試行]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries)を参照してください。

不健全ホスト検出が問題を引き起こしている可能性がある場合は、[Braze サポート]({{site.baseurl}}/support_contact/)にお問い合わせください。

{% alert note %}
コネクテッドコンテンツに使用する特定の URL を許可リストに登録できます。この機能を利用するには、カスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

{% alert tip %}
一般的なエラーコードのトラブルシューティング方法については、[Webhook およびコネクテッドコンテンツリクエストのトラブルシューティング]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors#unhealthy-host-detection)を参照してください。
{% endalert %}

### レート制限 (429) と不健全ホスト検出の違い

以下は異なるメカニズムです。

- **429 Too Many Requests:** エンドポイント（またはアップストリームサービス）がこのレスポンスを返しています。サーバーまたはミドルウェアがトラフィックを拒否していることを意味し、多くの場合、独自のレート制限があるためです。Braze はコネクテッドコンテンツに個別のレート制限を適用しません。コネクテッドコンテンツのリクエスト量は、[メッセージ配信速度のレート制限]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting)に直接比例してスケールします。メッセージは受信者ごとに複数回レンダリングされる可能性があるため（たとえば、メールの HTML、プレーンテキスト、AMP）、コネクテッドコンテンツリクエストの数はそのレート制限を超える可能性があります。設定した1分あたりのメッセージ数以下になるとは想定しないでください。429 が発生する場合は、エンドポイントまたはミドルウェアを予想されるリクエスト量を処理できるようにスケールするか、キャンペーンまたはキャンバスステップのレート制限を下げて、1分あたりに送信されるメッセージ（およびコネクテッドコンテンツ呼び出し）を減らしてください。
- **不健全ホスト検出:** 1分間の時間枠内で高率かつ大量の*障害*が発生した後にトリガーされる Braze 側の保護手段です。障害カウントには、`408`、`429`、`502`、`503`、`504`、`529` のステータスコードが含まれます。トリガーされると、Braze はそのホストへのリクエストを一時的に停止し、障害レスポンスをシミュレートします。これは、お客様独自のレート制限とは独立しています。検出しきい値の詳細については、[Webhook およびコネクテッドコンテンツリクエストのトラブルシューティング]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors/#unhealthy-host-detection)を参照してください。不健全ホスト検出を回避するには、[コネクテッドコンテンツの呼び出し量について](#understanding-connected-content-call-volume)および[大量エンドポイントのベストプラクティス](#best-practices-for-high-volume-endpoints)で説明されている呼び出し量をエンドポイントが処理できるようにしてください。

## 効率的なパフォーマンスを実現する

Braze はメッセージを非常に高速で配信するため、サーバーが数千の同時接続を処理できるようにして、コンテンツをプルダウンするときにサーバーが過負荷状態にならないようにしてください。パブリック API を使用する場合は、API プロバイダーが設定しているレート制限に違反していないことを確認してください。パフォーマンス上の理由から、Braze ではサーバーの応答時間が 2 秒未満であることを必要としています。サーバーの応答に 2 秒以上かかる場合、コンテンツは挿入されません。

エンドポイントのキャパシティ計画と呼び出し量の削減については、[大量エンドポイントのベストプラクティス](#best-practices-for-high-volume-endpoints)を参照してください。

## 知っておくべきこと

* Braze は API 呼び出しに課金せず、データポイント使用量にはカウントされません。
* コネクテッドコンテンツの応答には 1 MB の制限があります。
* コネクテッドコンテンツは、メッセージがレンダリングされるときに実行されます。アプリ内メッセージの場合、メッセージはインプレッション時にレンダリングされます。
* コネクテッドコンテンツ呼び出しはリダイレクトに従いません。

## 大量エンドポイントのベストプラクティス

メッセージでコネクテッドコンテンツを使用し、大量に送信する場合は、受信者数や送信数よりも多くのリクエストを想定して計画してください。

1. **ピーク負荷を見積もる:** エンドポイントまたはミドルウェアのサイジングには、保守的な乗数を使用してください。コネクテッドコンテンツリクエストは、受信者数や送信メッセージ数を超える可能性があります。たとえば、メールの場合、1人の受信者が複数の呼び出し（HTML、プレーンテキスト、AMP）を生成する可能性があるため、受信者数 × 2 または × 3 が保守的な見積もりとしてよく使用されます。
2. **適切な場合はキャッシュを使用する:** GET リクエストはデフォルトでキャッシュされます。POST リクエストの場合、レスポンスが一定期間再利用できるとき（たとえば、リクエストごとに変わらないトークンやコンテンツ）は `:cache_max_age` を追加してください。[レスポンスのキャッシュ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/caching_responses/)および以下の [POST キャッシュに関する FAQ](#what-is-caching-behavior) を参照してください。
3. **配信速度のレート制限を設定する:** キャンペーンまたはキャンバスステップの[配信速度のレート制限]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting)は、コネクテッドコンテンツのリクエスト量を間接的に制限する唯一の手段です。Braze はコネクテッドコンテンツ自体にレート制限を適用しません。これはあくまでプロキシであり、完全なものではありません。コネクテッドコンテンツリクエストはメッセージと1:1ではないためです。エンドポイントが処理できる範囲内にメッセージ（およびコネクテッドコンテンツ）の量を抑えるために使用してください。
4. **冪等性と再試行に対応した設計にする:** Braze は受信者ごとにエンドポイントを複数回呼び出す可能性があります。エンドポイントが重複リクエストを受けても不正な副作用が発生しないようにしてください。

## 認証タイプ

### 基本認証の使用

URL に基本認証が必要な場合、Braze は API 呼び出しで使用する基本認証の認証情報を保存できます。**設定** > **コネクテッドコンテンツ**で、既存の基本認証の認証情報を管理し、新しい認証情報を追加できます。

![Braze ダッシュボードのコネクテッドコンテンツ設定。]({% image_buster /assets/img/connected_content/basic_auth_mgmt.png %})

新しい認証情報を追加するには、**認証情報の追加** > **基本認証**を選択します。

![基本認証またはトークン認証を使用するオプションがある「認証情報の追加」ドロップダウン。]({% image_buster /assets/img/connected_content/add_credential_button.png %}){: style="max-width:60%"}

認証情報に名前を付け、ユーザー名とパスワードを入力します。

![名前、ユーザー名、パスワードを入力するオプションがある「新しい認証情報の作成」ウィンドウ。]({% image_buster /assets/img/connected_content/basic_auth_token.png %}){: style="max-width:60%"}

次に、トークンの名前を参照することで、API 呼び出しでこの基本認証の認証情報を使用できます。

{% raw %}
```
Hi there, here is some fun trivia for you!: {% connected_content https://yourwebsite.com/random/trivia :basic_auth credential_name %}
```
{% endraw %}

{% alert note %}
認証情報を削除する場合、これを使用しようとしているコネクテッドコンテンツ呼び出しはすべて中止されることに注意してください。
{% endalert %}

### トークン認証の使用

Braze コネクテッドコンテンツを使用する場合、特定の API では、ユーザー名とパスワードの代わりにトークンが必要になることがあります。Braze は、トークン認証ヘッダー値を保持する認証情報を保存することもできます。

トークン値を保持する認証情報を追加するには、**認証情報の追加** > **トークン認証**を選択します。次に、API 呼び出しヘッダーと許可ドメインのキーと値のペアを追加します。

![トークン認証の詳細が記載されたトークンの例「token_credential_abc」。]({% image_buster /assets/img/connected_content/token_auth.png %}){: style="max-width:60%"}

そして、認証情報名を参照することで、API 呼び出しでこの認証情報を使用できます。

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

### オープン認証 (OAuth) の使用

一部の API 設定では、アクセスする API エンドポイントの認証に使用できるアクセストークンを取得する必要があります。

#### ステップ 1: アクセストークンを取得する

次の例は、アクセストークンを取得してローカル変数に保存し、後続の API 呼び出しの認証に使用できるようにする方法を示しています。`:cache_max_age` パラメーターを追加して、アクセストークンの有効期間に合わせることで、アウトバウンドコネクテッドコンテンツ呼び出しの回数を減らすことができます。詳細については、[設定可能なキャッシュ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/local_connected_content_variables/#configurable-caching)を参照してください。

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

#### ステップ 2: 取得したアクセストークンを使用して API を認可する

トークンが保存されたら、後続のコネクテッドコンテンツ呼び出しにダイナミックにテンプレート化して、リクエストを認可できます。

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

### 認証情報の編集

認証タイプの認証情報名を編集できます。

- 基本認証では、ユーザー名とパスワードを更新できます。以前に入力したパスワードは表示されないことに注意してください。
- トークン認証では、ヘッダーのキーと値のペアと許可ドメインを更新できます。以前に設定したヘッダー値は表示されないことに注意してください。

![認証情報を編集するオプション。]({% image_buster /assets/img/connected_content/edit_credentials.png %}){: style="max-width:60%"}

## コネクテッドコンテンツ IP の許可リスト

コネクテッドコンテンツを使用したメッセージが Braze から送信されると、Braze サーバーは自動的に顧客またはサードパーティのサーバーにネットワークリクエストを行い、データをプルバックします。IP 許可リストを使用すると、コネクテッドコンテンツのリクエストが実際に Braze から来ていることを確認でき、セキュリティのレイヤーが追加されます。

Braze は、次の IP 範囲からコネクテッドコンテンツリクエストを送信します。リストされている範囲は、許可リストにオプトインされているすべての API キーに自動的かつダイナミックに追加されます。

Braze には、すべてのサービスに使用される一連の予約済み IP があり、すべてが常にアクティブになるわけではありません。これは、Braze が別のデータセンターから送信したり、メンテナンスを行ったりする際に、顧客に影響を与えないように設計されています。Braze は、コネクテッドコンテンツリクエストを行うときに、以下にリストされている IP のいずれか 1 つ、サブセット、またはすべてを使用する可能性があります。

{% multi_lang_include data_centers.md datacenters='ips' %}

### `User-Agent` ヘッダー

Braze は、すべてのコネクテッドコンテンツおよび Webhook リクエストに、以下のような `User-Agent` ヘッダーを含めます。

```text
Braze Sender 75e404755ae1270441f07eb238f0faf25e44dfdc
```

{% alert tip %}
ハッシュ値は定期的に変更されることに注意してください。`User-Agent` でトラフィックをフィルターしている場合は、`Braze Sender` で始まるすべての値を許可してください。
{% endalert %}

## トラブルシューティング

コネクテッドコンテンツ呼び出しのトラブルシューティングには、[Webhook.site](https://webhook.site/) を使用します。

1. コネクテッドコンテンツ呼び出しの URL を、サイトで生成された一意の URL に切り替えます。
2. キャンペーンまたはキャンバスステップをプレビューしてテストし、リクエストがこの Web サイトに届くことを確認します。

このツールを使用して、リクエストヘッダー、リクエスト本文、および呼び出しで送信されるその他の情報に関する問題を診断できます。

## よくある質問

### コネクテッドコンテンツの呼び出しがユーザー数や送信数より多いのはなぜですか？

これは想定される動作です。Braze は、メッセージペイロードが複数回レンダリングされる可能性があるため（たとえば、メールの HTML、プレーンテキスト、AMP、検証や再試行ロジック、その他の内部目的）、受信者ごとに同じコネクテッドコンテンツ API 呼び出しを複数回実行することがあります。送信とコネクテッドコンテンツ呼び出しの間に保証された1:1の比率はありません。詳細と軽減策については、[コネクテッドコンテンツの呼び出し量について](#understanding-connected-content-call-volume)および[大量エンドポイントのベストプラクティス](#best-practices-for-high-volume-endpoints)を参照してください。

### コネクテッドコンテンツでレート制限はどのように機能しますか？

コネクテッドコンテンツには専用のレート制限がありません。その代わり、レート制限はメッセージ送信レートに基づいています。コネクテッドコンテンツ呼び出しの回数が送信されたメッセージよりも多い場合は、メッセージングのレート制限を、意図するコネクテッドコンテンツのレート制限よりも低く設定することをお勧めします。

### キャッシュ動作とは何ですか？

GET リクエストはデフォルトでキャッシュされます（[レスポンスのキャッシュ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/caching_responses/)を参照）。**POST リクエストはデフォルトではキャッシュされません**が、コネクテッドコンテンツ呼び出しに `:cache_max_age` を追加することでキャッシュを有効にできます。これにより、同じ POST（たとえば、トークンやコンテンツリクエスト）がキャッシュウィンドウ内で繰り返し行われる場合に、エンドポイントの負荷を軽減できます。

{% raw %}
```liquid
{% connected_content https://api.example.com/token :method post :body grant_type=client_credentials :cache_max_age 900 :save token %}
```
{% endraw %}

キャッシュは重複するコネクテッドコンテンツ呼び出しの削減に役立ちますが、ユーザーごとに1回の呼び出しになることは保証されません。キャッシュ期間は5分から4時間です。詳細については、[レスポンスのキャッシュ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/caching_responses/)を参照してください。

### コネクテッドコンテンツ HTTP のデフォルト動作とは何ですか？

{% multi_lang_include connected_content.md section='default behavior' %}

{% multi_lang_include connected_content.md section='http post' %}