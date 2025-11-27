---
nav_title: Postmanとサンプル請求
article_title: Postman とサンプルリクエスト
page_order: 3
description: "このリファレンス記事では、Braze Postmanコレクションについて、コレクションとは何か、コレクションのセットアップと使用方法、リクエストの編集と送信方法について説明する。"
page_type: reference

---

# Postmanとサンプル請求

> Braze では、Postman Collection を通じて、すべてのエンドポイントに対してサンプル API リクエストを生成することができます。このリファレンス記事では、Braze Postmanコレクションについて、コレクションとは何か、コレクションのセットアップと使用方法、リクエストの編集と送信方法について説明する。

## Postman とは？

Postmanは、APIリクエストのビルドとテストのための無料のビジュアル編集ツールである。他の方法（例えばcURLを使う）と比べて、PostmanではAPIリクエストを編集したり、ヘッダー情報を見たりすることができる。コレクション（事前に作成されたAPIリクエストのサンプルのライブラリー）を保存することができる。REST APIのセットアップを高速化するために、すべてのエンドポイントについて、あらかじめ作成されたサンプル集を提供している。

開始するには、[Postman ドキュメント](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#intro)の [**Postman で実行**] をクリックして、Postman コレクションを表示またはダウンロードします。

## Braze Postman コレクションを使用する

Postmanアカウント（macOS版、Windows版、Linux版を[Postmanウェブサイトから](https://www.getpostman.com)ダウンロードできる）を持っていれば、オレンジ色の「**Postmanで実行**」ボタンをクリックすることで、自分のPostmanアプリでPostmanドキュメントを開くことができる。その後、[環境を作成](#setting-up-your-postman-environment)するか、Braze REST API環境をテンプレートとして使用し、利用可能な`POST` 、`GET` リクエストを独自のニーズに合わせて編集することができる。

### Postmanの環境をセットアップする

{% raw %}
Braze Postman Collection は、テンプレート変数 `{{instance_url}}` を使用して、Braze インスタンスの REST API URL を事前に作成されたリクエストに置き換え、`{{api_key}}` 変数を API キーに置き換えます。コレクション内のすべてのリクエストを手動で編集するのではなく、Postman の環境でこの変数を設定できます。ドロップダウンから当社のテンプレート環境（Braze REST API Environment Template）を選択し、変数値を独自のものに置き換えることも、独自の環境を設定することもできる。
{% endraw %}

自分の環境をセットアップするには、以下の手順を実行する：

1. [**ワークスペース**] タブで ［**環境**］ を選択します。
2. 新しい環境を作成するには**＋**プラスボタンをクリックする。
3. この環境に名前を付け (たとえば、「Braze API リクエスト」)、`instance_url` と　`api_key` のキーを追加し、[Braze インスタンス ]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) と [Braze REST API キー]({{site.baseurl}}/api/api_key/)に対応する値を指定します。
4. [**保存**] をクリックします。

{% alert note %}
`POST` リクエストの本文では、`api_key` は引用符で囲む必要があります: `"MY-API-KEY-EXAMPLE"`。`GET` URLでは、このようにしないでください。この書式は、このドキュメントの `POST` リクエストボディ、`GET` URL、および `YOUR-API-KEY-HERE` の環境テンプレートですでに提供しています。
{% endalert %}

![Postman の Braze REST API 環境に API キーとインスタンス URL の変数を追加する。]({% image_buster /assets/img_archive/postman_variable.png %})

### コレクションからビルド済みのリクエストを使う

環境を構成した後、コレクション内の事前に構築されたリクエストのいずれかを、新しい API リクエストを構築するためのテンプレートとして使用できます。事前構築済みのリクエストのいずれかの使用を開始するには、Postman の [**コレクション**] メニュー内でそのリクエストをクリックしてください。これで Postman アプリのメインウィンドウで新しいタブとしてリクエストが開きます。

一般に、Braze API エンドポイントが受け付けるリクエストには、`GET` と `POST` の2種類があります。エンドポイントが使用する `HTTP` メソッドに応じて、事前に構築されたリクエストを異なる方法で編集する必要があります。

#### POSTリクエストを編集する

`POST` リクエストを編集する場合、リクエストを開き、リクエストエディターの**Body**セクションに移動する。読みやすくするために、`JSON` リクエストボディをフォーマットする**raw**ラジオボタンを選択する。

![Postman で POST User Track リクエストを編集する際の本文タブ]({% image_buster /assets/img_archive/postman_post.png %})

#### GETリクエストを編集する

`GET` リクエストを編集する場合は、リクエスト URL で渡されるパラメーターを編集します。そのためには、**Params**タブを選択し、表示されるフィールドのキーと値のペアを編集する。

![Postman で GET Query List of Unsubscribed Email Addresses (配信停止済みメールアドレスのクエリリストの取得) リクエストを編集するときの「パラメータ」タブ。]({% image_buster /assets/img_archive/postman_get.png %})

### リクエストを送信する

API リクエストの準備ができたら、[**送信**] をクリックします。リクエストは送信され、レスポンスデータはリクエストエディタの下のセクションに入力される。ここから、Braze APIから返された生データを見たり、HTTPレスポンスコードを見たり、リクエストの処理にかかった時間を見たり、ヘッダー情報を見たりすることができる。

![ステータスが「201 Created」、応答時間が「269ミリ秒」の POST リクエストからの本文応答データの例。]({% image_buster /assets/img_archive/postman_response.png %})

