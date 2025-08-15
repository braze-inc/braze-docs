---
nav_title: Hightouch Personalization API
article_title: Hightouch Personalization API
description: "このリファレンス記事では、Braze と Hightouch の Personalization API の統合について説明します。この API は、クラウドデータウェアハウス内のデータセットに基づいて低レイテンシーのデータ API をホストするためのマネージドサービスです。このリファレンス記事では、Hightouch Personalization APIが解決するユースケース、使用するデータ、設定方法、Brazeとの統合方法について説明する。"
page_type: partner
search_tag: Partner
---

# Hightouch Personalization API

> Hightouch の [Personalization API](https://hightouch.com/docs/destinations/personalization-api) は、クラウドデータウェアハウスのデータセットに基づいて低レイテンシーのデータAPI をホストできるようにするマネージドサービスです。

![]({% image_buster /assets/img/hightouch/cohort7.png %})

Braze と Hightouch の統合により、[Braze コネクテッドコンテンツ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/)とこの API を使用して、送信時に最新の顧客またはオブジェクトのデータをキャンペーンまたはキャンバスに取り込むことができます。

Hightouch の Personalization API は、Braze の設定で使用する REST エンドポイントを提供します。具体的には、Braze のコネクテッドコンテンツを使用して Personalization API に対する GET リクエストを実行し、特定の識別子に関連するすべての情報を取得できます。この API によって公開されるデータは、顧客、製品、またはその他のオブジェクトデータを表す場合があります。 

![]({% image_buster /assets/img/hightouch/cohort6.png %})

## 前提条件

| 必要条件| 説明|
| ---| ---| 
| パーソナライゼーションAPIを有効にした[Hightouchアカウント](https://app.hightouch.com/login) | このパートナーシップを活用するには、[Business Tier アカウント](https://hightouch.com/pricing)が必要です。|
| 定義されたユースケース | API を設定する前に、この統合のユースケースを決定しておく必要があります。一般的な使用例については、以下のリストを参照のこと。 |
| クラウドデータウェアハウスなどのソースに保存されているデータ | Hightouch は、[25以上のデータソース](https://hightouch.com/integrations)と統合しています。 |
| ハイタッチAPIキー | これは、**[Hightouch] > [Settings] > [API keys] > [Add API key]** 内で作成できます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% tabs %}
{% tab 使用例 %}

### ユースケース

始める前に、パーソナライゼーションAPIをどのように使いたいかを正確に計画しておくと便利だ。

一般的な使用例には以下のようなものがある：
- メールテンプレート、キャンペーン、アプリ内エクスペリエンスへのパーソナライズされた製品レコメンデーションの埋め込むみを効率化する**製品レコメンデーション**
- ダイナミックな製品レコメンデーションでマーケティングタッチポイントを充実させることで**パーソナライズされたマーケティングキャンペーンを強化する**
- 例えば、カスタマイズされた検索結果、コホートベースの価格設定、メッセージング、おすすめ記事、最寄りの店舗など、**アプリ内またはウェブでパーソナライゼーションを提供する**。
- **財務データまたは医療データに基づくレコメンデーション** \- 財務データに厳しい要件があり、Hightouch はその[厳格なデータセキュリティポリシー](https://hightouch.com/docs/security/overview#compliance)によってこれらの要件を満たします。Hightouch を使用すると、セグメンテーション基準で使用される基本的な属性を公開せずに、財務データまたは医療データに基づいて顧客セグメントを作成できます。

{% endtab %}
{% tab データセット %}

### データセット

パーソナライゼーションAPIは、ウェアハウス内の選択されたデータのキャッシュとして機能するため、レコメンデーションデータはすでにそこに保存されているはずだ。必要に応じて、Hightouch を使用してテンプレートに従って変換できます。この種のデータには以下が含まれる：
- 地理的地域、年齢、その他の人口統計学的情報などのユーザー・メタデータ
- 過去の購入、ページビュー、クリックなどのユーザーアクションやイベント。

{% endtab %}
{% endtabs %}

## 統合

### ステップ1:データソースを Hightouch に接続する

[ハイタッチ・ソースは](https://hightouch.com/docs/getting-started/concepts#sources)、組織のビジネス・データが存在する場所である。この場合、ユーザーデータが保存されている場所はどこでもかまいません。
1. ハイタッチで、「**ソースの概要」＞「ソースの追加**」と進む。ソースとしてデータウェアハウスを選択します。<br><br>
2. 関連する認証情報を入力する。これらはソースによって異なる。 

詳細については、関連するソースの[ドキュメント](https://hightouch.com/docs)を参照してください。

### ステップ2:モデルデータ

ハイタッチ・モデルは、ソースからどのようなデータを引き出すかを定義する。新しいモデルをセットアップするには、以下の手順に従う：

1. Hightouch で [[**Models overview**](https://app.hightouch.com/models)] > [**Add model**] に移動し、接続したソースを選択します。<br><br>
2. 次に[モデリング方法](https://hightouch.com/docs/models/creating-models)を選択します。すべての情報を1つのテーブルにまとめる必要があるので、ビジュアル・テーブル・セレクタを使って定義することができる。あるいは、必要なカラムだけを含むSQLを書いたり、既存のdbtモデル、ルッカー・ルック、シグマ・ワークブックに頼ることもできる。<br><br>
3. 続行する前に、モデルをプレビューして、興味のあるデータを照会していることを確認する。デフォルトでは、Brazeはプレビューを最初の100レコードに制限している。データを検証したら、[**Continue**] をクリックします。<br><br>
4. 例えば、"User recommendations "のように、モデルに名前をつける。<br><br>
5. 最後に主キーを選択し、[**Finish**] をクリックします。主キーは、一意の識別子を持つ列である必要があります。これは、特定のユーザーのレコメンデーションを取得するために Personalization API を呼び出すときに使用するフィールドでもあります。

### ステップ3:パーソナライゼーションAPIを設定する

API でリクエストを受信するための準備は、次の2つのステップからなります。
- お客様のインフラに最も近い地域でパーソナライゼーションAPIを有効にする
- Hightouchが管理するキャッシュで実体化されるべきモデルを定義するためにシンクを作成する。

以下の指示に従って、両方を完了させる：

1. ハイタッチでは [**目的地**](https://app.hightouch.com/destinations)を選択し、あなたのために作成されたHightouchパーソナライゼーションAPIを選択する。この宛先が有効になっていない場合は、[ハイタッチ・サポートに](mailto:friends@hightouch.com)連絡すること。<br><br>
2. 次に、適切な地域を選択する。インフラに最も近い地域を選択することで、応答時間を短縮することができる。インフラストラクチャに近いリージョンが表示されない場合は、[Hightouch サポート](mailto:friends@hightouch.com)にお問い合わせください。<br><br>
3. [[**Syncs**] 概要ページ](https://app.hightouch.com/syncs)に進み、[**Add sync**] ボタンをクリックします。次に、該当するモデルと、以前に設定した宛先を選択します。<br><br> 
4. 英数字のコレクション名を入力します。コレクションは概念的にはデータベースのテーブルに似ている。各コレクションは特定のデータタイプ (顧客や請求書など) を表します。コレクション名には英数字のみを使用する必要があります。コレクション名は、Personalization API エンドポイントの一部になります。<br><br>
5. 次に、モデルのどの列をレコード検索の一次インデックスとして使用するかを指定します。このフィールドは、コレクション内の各レコードを一意に識別する必要があり、多くの場合、モデルの主キーと同じである。パーソナライゼーションAPIは、複数のインデックスの検索をサポートする。たとえば、`user_id`、`anonymous_id`、または `email_address` を使用して顧客プロファイルを取得できます。複数のインデックスを有効にする場合は、[Hightouch サポート](mailto:friends@hightouch.com)にご連絡ください。<br><br>
6. フィールドマッパーを使用して、APIレスポンスペイロードに含まれるべきモデルのカラムを指定する。これらのフィールドの名前を変更し、リキッドテンプレート言語を使用して変換を適用するために高度なマッパーを使用することができる。<br><br>
7. ユースケースに適した[削除動作](https://www.hightouch.com/docs/destinations/personalization-api#delete-behavior)を選択します。<br><br>
8. 最後に [**Continue**] をクリックし、[同期スケジュール](https://hightouch.com/docs/syncs/schedule-sync-ui)を選択します。

Hightouch は、ウェアハウス内のデータをマネージドデータベースに同期し、Personalization API を介して公開します。

### ステップ4:Braze Connected Contentを通じてパーソナライゼーションAPIを呼び出す

パーソナライゼーションAPIインスタンスを設定したら、それをBraze Connected Contentのエンドポイントとして使用できる。 

API は、`https://personalization.{region}.hightouch.com` でアクセスできます (例: `https://personalization.us-west-2.hightouch.com`)。 

情報はエンドポイント `/v1/collections/:collection_name/records/:index_key/:index_value` を使用して取得できます。

例えば、キャンペーンやキャンバスにこのスニペットを入れることができる：

{% raw %}

```liquid
{% connected_content
     https://personalization.us-west-2.hightouch.com/v1/collections/customer/records/id/12345
     :method get
     :headers {
       "Authorization": "Bearer {{YOUR-API-KEY}}"
  }
     :content_type application/json
     :save customer
%}
```
{% endraw %}

リキッドテンプレートを使って、JSONペイロードで返されたプロパティを参照し、メッセージングで使うことができる。

以下のペイロードの例の場合：

```json
{
    "user_id": 12345,
    "full_name": "Jane Doe",
    "lifetime_value": 1492.18,
    "churn_risk": 0.04,
    "90_day_summary": {
        "num_songs_listened": 813,
        "top_genres": [
            "house",
            "techno",
            "ambient"
        ],
        "top_artists": [
            "deadmau5",
            "Marsh",
            "Enamour"
        ],
    },
    "recommendations": {
        "concerts": [
            {
                "artist": "Aphex Twin",
                "location": "San Francisco, CA",
                "event_date": "2023-01-31"
            },
            {
                "artist": "Sultan + Shepard",
                "location": "San Francisco, CA",
                "event_date": "2023-02-25"
            }
        ],
        "upcoming_album_release": {
            "title": "Universal Language",
            "artist": "Simon Doty",
            "label": "Anjunadeep",
            "release_date": "2023-04-28"
        }
    },
}
```

以下の Liquid リファレンスは、この例のデータを戻します。

| 液体テンプレート | 戻されるデータの例 |
| --- | --- |
| {% raw %}`{{artists.recommendations.concerts[0].artist}}`{% endraw %}| Aphex Twin |
| {% raw %}`{{artists.recommendations.concerts[0].location}}`{% endraw %}| カリフォルニア州サンフランシスコ |
| {% raw %}`{{artists.recommendations.upcoming_album_release.title}}`{% endraw %}| Universal Language |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## トラブルシューティング

ご質問がある場合は、[Hightouch サポート](mailto:friends@hightouch.com)までお問い合わせください。

