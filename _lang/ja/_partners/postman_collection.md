---
nav_title: 郵便配達員とサンプルのリクエスト
article_title: 郵便配達員とサンプルのリクエスト
page_order: 3
description: "このリファレンス記事では、Braze Postman コレクションの概要、コレクションの設定方法と使用方法、リクエストの編集方法と送信方法について説明します。"
page_type: reference

---

# 郵便配達員とサンプルのリクエスト

> Braze を使用すると、Postman コレクションを通じてすべてのエンドポイントのサンプル API リクエストを生成できます。このリファレンス記事では、Braze Postman コレクションの概要、コレクションの設定方法と使用方法、リクエストの編集方法と送信方法について説明します。

## Postmanとは何ですか?

Postman は、API リクエストを構築およびテストするための無料で使用できるビジュアル編集ツールです。API を操作する他の方法 (cURL の使用など) とは異なり、Postman を使用すると、API リクエストの編集、ヘッダー情報の表示などを簡単に行うことができます。Postman には、事前に作成されたサンプル API リクエストのコレクションまたはライブラリを保存する機能があります。お客様が REST API を簡単に使い始められるように、すべての API エンドポイントのサンプルをあらかじめ用意したコレクションを作成しました。

開始するには、[Postman ドキュメント](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#intro) の **「Postman で実行」を** クリックして、Postman コレクションを表示またはダウンロードしてください。

## Braze Postmanコレクションの使用

Postman アカウントをお持ちの場合 ([Postman の Web サイト][1]から macOS、Windows、Linux バージョンをダウンロードできます)、オレンジ色 **の \[Postman で実行]** ボタンをクリックして、独自の Postman アプリで Postman ドキュメントを開くことができます。その後、 [環境を作成する](#setting-up-your-postman-environment)か、Braze REST API環境をテンプレートとして使用し、利用可能な `POST` そして `GET` ご自身のニーズに合わせてリクエストしてください。

### Postman環境の設定

{% raw %}
Braze Postmanコレクションはテンプレート変数を使用します。 `{{instance_url}}`、BrazeインスタンスのREST API URLを事前構築されたリクエストに置き換え、 `{{api_key}}`API キーの変数。コレクション内のすべてのリクエストを手動で編集するのではなく、Postman 環境でこの変数を設定できます。ドロップダウンからテンプレート環境 (Braze REST API 環境テンプレート) を選択し、変数値を独自のものに置き換えるか、独自の環境を設定することができます。
{% endraw %}

独自の環境を設定するには、次の手順を実行します。

1. **\[ワークスペース** ] タブから **\[環境]**を選択します。
2. 新しい環境を作成するには、**「+」** プラスボタンをクリックします。
3. この環境に名前を付け（たとえば、「Braze APIリクエスト」）、キーを追加します。 `instance_url` そして `api_key` \[Brazeインスタンスに対応する値][7] および\[Braze REST APIキー][8]。
4. \[**保存**] をクリックします。

{% alert note %}
で `POST` リクエストボディ、 `api_key` 引用符で囲む必要があります: `"MY-API-KEY-EXAMPLE"`。で `GET` URL はそうすべきではありません。このドキュメントでは、すでにこのフォーマットを提供しています。 `POST` リクエストボディ、 `GET`URL、環境テンプレート `YOUR-API-KEY-HERE`。
{% endalert %}

![Postman の Braze REST API 環境に API キーとインスタンス URL の変数を追加します。][3]

### コレクションから事前に構築されたリクエストを使用する

環境を構成したら、コレクション内の事前構築されたリクエストのいずれかを、新しい API リクエストを構築するためのテンプレートとして使用できます。事前に構築されたリクエストのいずれかの使用を開始するには、Postman の **コレクション** メニュー内でそのリクエストをクリックします。これにより、リクエストが Postman アプリのメイン ウィンドウに新しいタブとして開きます。

一般的に、Braze APIエンドポイントが受け入れるリクエストには2つの種類があります。 `GET` そして `POST`。どちらによって `HTTP` エンドポイントが使用するメソッドを変更する場合は、事前に構築されたリクエストを別の方法で編集する必要があります。

#### POSTリクエストを編集する

編集する場合 `POST` リクエストを開くには、リクエスト エディターの **[本文] セクション** に移動します。読みやすくするために、**raw** ラジオボタンを選択してフォーマットします。 `JSON` リクエスト本体。

![Postman で POST User Track リクエストを編集するときの Body タブ][4]

#### GETリクエストを編集する

編集する場合 `GET` リクエストでは、リクエスト URL で渡されるパラメータを編集します。これを行うには、**「Params」** タブを選択し、表示されるフィールドでキーと値のペアを編集します。

![Postman で登録解除された電子メール アドレスの GET クエリ リスト要求を編集するときの Params タブ。][5]

### リクエストを送信

API リクエストの準備ができたら、**「送信」を**クリックします。リクエストが送信され、応答データがリクエスト エディターの下のセクションに入力されます。ここから、Braze API から返された生データを表示したり、HTTP 応答コードを確認したり、リクエストの処理にかかった時間を確認したり、ヘッダー情報を表示したりできます。

![ステータスが 201 Created、応答時間が 269 ミリ秒の POST 要求からの本文応答データの例。][6]

[1]: https://www.getpostman.com
[3]: {% image_buster /assets/img_archive/postman_variable.png %}
[4]: {% image_buster /assets/img_archive/postman_post.png %}
[5]: {% image_buster /assets/img_archive/postman_get.png %}
[6]: {% image_buster /assets/img_archive/postman_response.png %}
[7]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[8]: {{site.baseurl}}/api/api_key/
