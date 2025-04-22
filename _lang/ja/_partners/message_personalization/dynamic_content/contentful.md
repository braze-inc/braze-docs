---
nav_title: Contentful
article_title: Contentful
description: "この参考記事では、Braze と Contentful の連携について説明します。Contentful は、コネクテッドコンテンツを動的に使用して Contentful から Braze キャンペーンにコンテンツをプルできるコンテンツ管理システムです。"
alias: /partners/contentful/
page_type: partner
search_tag: Partner
---

# Contentful

>[Contentful](https://www.contentful.com/) は、コンテンツの作成、管理、およびあらゆるプラットフォームへの配信を可能にするヘッドレスのコンテンツ管理システムです。コンテンツ管理システム (CMS) とは異なり、Contentful ではコンテンツモデルを作成できるため、どのコンテンツを管理するかを決めることができます。<br><br>このページでは、Contentful のコンテンツ配信 API からデータをフェッチするように Braze コネクテッドコンテンツを構成する手順について説明します。 

統合後は、Contentful の RESTful API を使用して、Web サイト、モバイルアプリ (iOS、Android、および Windows)、その他の多くのプラットフォームなど、複数のチャネルにわたってコンテンツを配信できます。また、コンテンツを Contentful からダイナミックにプルして、Braze キャンペーンで使用することもできます。

## 前提条件

開始する前に、次のものが必要になります。

| 前提条件          | 説明                        |
|-----------------------|------------------------------------|
| Contentful アカウント | Content Delivery API にアクセスできる Contentful アカウントが必要です。 |
| Braze アカウント | コネクテッドコンテンツ機能にアクセスできる Braze アカウントが必要です。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

### ステップ1: Contentful API 認証情報を取得する

1. 認証情報を使って[Contentfulにログインする](https://app.contentful.com/login)。
2. Contentful ダッシュボードの [**設定**] > [**API キー**] で API アクセストークンを作成または取得します。APIキーをまだ持っていない場合は、新規に作成する：<br>2.1 [**API キーの追加**] を選択します。<br>2.2 必要な詳細を入力し、適切な環境を選択します。<br>2.3 [**保存**] を選択し、**スペース ID** と**Content Delivery API - アクセストークン**をメモします。
3. Contentful API を使用してアクセスするコンテンツモデルを特定します。

### ステップ2:Braze コネクテッドコンテンツを構成する

1. 認証情報を使って[Brazeにログインする](https://dashboard.braze.com/sign_in)。
2. Braze ダッシュボードで、 [**テンプレート**] > [**コンテンツブロック**] > [**コンテンツブロックを作成**] > **[HTML コンテンツブロック**] の順に移動します。
3. Contentful の[Contentful Content Delivery API URL](https://www.contentful.com/developers/docs/references/content-delivery-api/#/reference/links) に対してコネクテッドコンテンツリクエストを作成します。Contentful Content Delivery API URL の例は```https://cdn.contentful.com/spaces/{space_id}/environments/{environment_id}/entries``` です。<br><br> 異なるアセットを取得するには、特定の変数を含める必要があります。コネクテッドコンテンツ URL リクエストの例は、Contentful の[エントリ](https://www.contentful.com/developers/docs/references/content-delivery-api/#/reference/entries/entry/get-a-single-entry/console)エンドポイントをターゲットにしています。このエンドポイントは `{space_id}` および `{environment_id}`、あるいは `{entry_id}` および `{access_token}` のような変数を必要とします。これらは Contentful インスタンスから取得できます。このコンテンツブロックの例では、変数を Contentful Space ID と Environment ID に置き換える必要があります。<br><br>Content Delivery API URL の例では、Contentful の利用可能なエンドポイントの1つだけを使用しています。異なるユースケースは、異なるURLを活用することで達成できるかもしれない。例えば、[画像 API](https://www.contentful.com/developers/docs/references/images-api/) を使えば、Contentful に保存されている画像を取り込むことができます。詳しくは、[Content Delivery API](https://www.contentful.com/developers/docs/references/content-delivery-api/) を参照してください。

{% alert note %}
エンドポイントによっては、新しい変数が必要になる場合があります。たとえば、画像 API には`{asset_id}`、`{unique_id},`、`{name}` が必要です。さらなるガイダンスについては、Contentfulに問い合わせること。
{% endalert %}

{% raw %}
```json
        {% assign space_id = "YOUR-CONTENTFUL-SPACE-ID"}
        {% assign environment_id = "YOUR-CONTENTFUL-ENVIRONMENT-ID"}
        {% assign entry_id = "YOUR-CONTENTFUL-ENTRY-ID"}
        {% assign access_token = "YOUR-CONTENTFUL-ACCESS-TOKEN"}
         {% connected_content https://cdn.contentful.com/spaces/{space_id}/environments/{environment_id}/entries/{entry_id}?access_token={access_token}
         :method get
         :headers {
             "Authorization": "YOUR_CONTENTFUL_ACCESS_TOKEN"
                 }
               :content_type application/json
               :save response %}
```
{% endraw %}

{: start="4"}
4\.「テストエンドポイント」を使用して、Braze がコネクテッドコンテンツ API に正常に接続し、目的のデータを取得できることをテストします。
5\.[**完了**] を選択してコンテンツブロックを保存します。
6. コンテンツブロックに「Contentful API」などのわかりやすい名前をつけ、「**コンテンツブロックを起動**」を選択する。

### ステップ 3: キャンペーンやキャンバスでコネクテッドコンテンツを使用する

1. Brazeで、新しいキャンペーンを作成するか、既存のキャンペーンを編集する。
2. コネクテッドコンテンツブロックを使って、Contentful から取得したデータを挿入します。設定時に定義したデータパスを使用して、キャンペーンコンテンツをダイナミックに入力します。<br><br>
- **応答パス**コンテンツブロックをBrazeキャンペーンまたはキャンバスに含めた後、変数`{response}` をメッセージに挿入すると、レスポンスが利用可能になる。<br><br>JSON ドット表記法では、Contentful からの応答本文のどの部分をメッセージに含めるかを指定できます。これはユースケースによって異なります。例えば、Contentful のエントリエンドポイントからタイトル値 ({% raw %}```liquid{{response.items[0].fields.title}}```{% endraw %}) を使用し、次のような応答を受け取ることができます。

{% raw %}
```json
   {
  "fields": {
    "title": {
      "en-US": "Hello!"
    },
    "body": {
      "en-US": "This is a sample message!"
    }
  },
  "metadata": {
    "tags": [
      {
        "sys": {
          "type": "Link",
          "linkType": "Tag",
          "id": "nyCampaign"
        }
      }
    ]
  },
  "sys": {
    "id": "5KsDBWseXY6QegucYAoacS",
    "type": "Entry",
    "version": 1,
    "space": {
      "sys": {
        "type": "Link",
        "linkType": "Space",
        "id": "yadj1kx9rmg0"
      }
    },
    "contentType": {
      "sys": {
        "type": "Link",
        "linkType": "ContentType",
        "id": "hfM9RCJIk0wIm06WkEOQY"
      }
    },
    "createdAt": "2016-12-20T10:43:35.772Z",
    "updatedAt": "2016-12-20T10:43:35.772Z",
    "revision": 1
  }
}
```
{% endraw %}

{: start="3" }
3\.キャンペーンをプレビューしてテストし、コネクテッドコンテンツデータが正しく表示されることを確認する。
4\.設定に満足したら、キャンペーンを開始する。

## トラブルシューティング

### APIレスポンス

Contentful API認証情報とエンドポイントURLが正しいことを確認する。APIコールに問題があることを示すエラーメッセージがBrazeにないか確認する。

### データマッピング

レスポンスパスのマッピングが正しく設定され、APIレスポンス構造が期待するものと一致していることを確認する。

## その他のリソース

- [Contentful コンテンツ配信 API ドキュメント](https://www.contentful.com/developers/docs/references/content-delivery-api/)
- [Braze コネクテッドコンテンツ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/)
- [Braze コンテンツブロック]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/)
