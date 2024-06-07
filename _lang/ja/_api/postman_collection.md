---
nav_title: Postmanとサンプルリクエスト
article_title: Postmanとサンプルリクエスト
page_order: 3
description: "このリファレンス記事では、Braze Postman Collection、それが何であるか、コレクションのセットアップと使用方法、およびリクエストの編集と送信方法について説明します。"
page_type: reference

---

# Postmanおよびサンプル要求

> Braze を使用すると、Postman コレクションを介してすべてのエンドポイントのサンプルAPI リクエストを生成できます。このリファレンス記事では、Braze Postman Collection、それが何であるか、コレクションのセットアップと使用方法、およびリクエストの編集と送信方法について説明します。

## ポストマンとは。

Postman は、API リクエストを構築およびテストするための、無料で使用できるビジュアル編集ツールです。API とやり取りする他の方法(cURL を使用するなど) とは異なり、Postman ではAPI リクエストの編集、ヘッダー情報の表示などを簡単に行うことができます。Postman には、事前に作成されたサンプルAPI リクエストのコレクションまたはライブラリを保存する機能があります。REST API を使用してお客様が簡単に立ち上がり、実行できるようにするために、すべてのAPI エンドポイントについて事前に作成された例を含むコレクションを作成しました。

[Postman docs](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#intro)の**Postman**で実行をクリックして、Postman コレクションを表示またはダウンロードして開始します。

## ろう付けポストマンコレクションの使用

Postmanアカウントをお持ちの場合([Postmanウェブサイト][1]からmacOS、Windows、およびLinuxバージョンをダウンロードできます)、オレンジの**Postman**ボタンをクリックして、独自のPostmanアプリで私たちのPostmanドキュメントを開くことができます。次に、[ environment](#setting-up-your-postman-environment) を作成するか、Braze REST API 環境をテンプレートとして使用し、使用可能な`POST` および`GET` リクエストを編集して、ユーザーのニーズに合わせることができます。

### Postman 環境のセットアップ

{% raw %}
Braze Postman Collection では、テンプレート変数`{{instance_url}}` を使用して、Braze インスタンスのREST API URL を組み込み済みのリクエストに置き換え、`{{api_key}}` 変数をAPI キーに置き換えます。Collection 内のすべてのリクエストを手動で編集するのではなく、Postman 環境でこの変数を設定できます。ドロップダウンからテンプレート環境(Braze REST API Environment Template) を選択し、変数値を独自のものに置き換えるか、独自の環境を設定できます。
{% endraw %}

独自の環境をセットアップするには、次の手順を実行します。

1. **Workspaces**タブから、**Environments**を選択します。
2. **+** プラスボタンをクリックして新しい環境を作成します。
3. この環境に名前("Braze API Requests" など) を付け、`instance_url` および`api_key` のキーを[Braze instance][7] および[Braze REST API Key][8] に対応する値で追加します。
4. **Save**をクリックします。

{% alert note %}
`POST` リクエストボディでは、`api_key` は引用符で囲む必要があります: `"MY-API-KEY-EXAMPLE"`。`GET` URL では、そうではありません。このドキュメントの`POST` リクエストボディ、`GET` URL、および`YOUR-API-KEY-HERE` の環境テンプレートでは、この書式設定をすでに提供しています。
{% endalert %}

![Postman でのBraze REST API 環境へのAPI キーおよびインスタンスURL の変数の追加][3]

### コレクションからのあらかじめ作成されたリクエストの使用

環境を設定したら、コレクションに組み込まれている任意のリクエストを、新しいAPI リクエストを構築するためのテンプレートとして使用できます。構築済みのリクエストのいずれかを使用し始めるには、Postman の**Collections** メニュー内でそれをクリックします。これにより、Postman アプリのメインウィンドウに新しいタブとしてリクエストが開きます。

一般に、Braze API エンドポイントが受け入れるリクエストには、`GET` と`POST` の2 種類があります。エンドポイントが使用する`HTTP` メソッドに応じて、事前構築されたリクエストを別の方法で編集する必要があります。

#### POST リクエストの編集

`POST` リクエストを編集する場合は、リクエストを開き、リクエストエディタの**Body** セクションに移動します。読みやすくするには、**raw**ラジオボタンを選択して、`JSON`リクエストボディをフォーマットします。

![Postman でPOST ユーザートラックリクエストを編集するときの本文タブ][4]

#### GET 要求の編集

`GET` リクエストを編集する場合は、リクエストURL で渡されたパラメータを編集します。そのためには、**Params**タブを選択し、表示されるフィールドでキーと値のペアを編集します。

![購読されていないメールアドレスのGET クエリリストをPostman で編集するときのParams タブ][5]

### リクエストを送信する

API リクエストの準備ができたら、**Send** をクリックします。リクエストが送信され、レスポンスデータがリクエストエディタの下のセクションに入力されます。ここから、Braze API から返された生データを表示したり、HTTP レスポンスコードを参照したり、リクエストの処理にかかった時間を確認したり、ヘッダー情報を表示したりできます。

![ステータスが 201 で、応答時間が 269 ミリ秒の POST リクエストからのレスポンスデータの例][6]

[1]: https://www.getpostman.com
[3]: {% image_buster /assets/img_archive/postman_variable.png %}
[4]: {% image_buster /assets/img_archive/postman_post.png %}
[5]: {% image_buster /assets/img_archive/postman_get.png %}
[6]: {% image_buster /assets/img_archive/postman_response.png %}
[7]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[8]: {{site.baseurl}}/api/api_key/
