---
nav_title: Hightouch Personalization API
article_title:ハイトタッチパーソナライゼーションAPI
description:この記事では、BrazeとHightouchのパーソナライゼーションAPIの統合について説明します。HightouchのパーソナライゼーションAPIは、クラウドデータウェアハウス内の任意のデータセットに基づいた低遅延データAPIをホスティングするためのマネージドサービスです。この記事では、Hightouch Personalization APIが解決するユースケース、そのデータの取り扱い方法、設定方法、およびBrazeとの統合方法について説明します。
page_type: partner
search_tag:Partner
---

# ハイトタッチパーソナライゼーションAPI

> Hightouchの[パーソナライゼーションAPI](https://hightouch.com/docs/destinations/personalization-api)は、クラウドデータウェアハウス内の任意のデータセットに基づいて低遅延データAPIをホストできるマネージドサービスです。

![][3]

BrazeとHightouchの統合により、[Braze Connected Content](https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/)を使用して、送信時に最新の顧客データやオブジェクトデータをキャンペーンやCanvasに取り込むことができます。

Hightouch's Personalization API provides a REST endpoint to use within your Braze configuration. Specifically, you can use Braze's Connected Contentの提供により、特定の識別子に関連するすべての情報を取得するためにPersonalization APIにGETリクエストを送信します。このAPIによって公開されるデータは、顧客、製品、またはその他のオブジェクトデータを表す可能性があります。 

![][2]

## 前提条件

| 要件| 説明|
| ---| ---| 
| [Hightouchアカウント](https://app.hightouch.com/login)にパーソナライゼーションAPIが有効になっています | Hightouch [ビジネスティアアカウント](https://hightouch.com/pricing)がこのパートナーシップを利用するために必要です。|
| 定義されたユースケース | APIを設定する前に、この統合の使用例を決定する必要があります。次のリストを参照して、一般的な使用例を確認してください。 |
| クラウドデータウェアハウスまたは他のソースに保存されたデータ | Hightouchは[25以上のデータソース](https://hightouch.com/integrations)と統合します |
| Hightouch APIキー | これは**Hightouch > 設定 > APIキー > APIキーの追加**内で作成できます。 |
{: .reset-td-br-1 .reset-td-br-2}

{% tabs %}
{% tab Use Cases %}

### ユースケース

始める前に、パーソナライゼーションAPIをどのように使用したいかを正確に計画することが役立ちます。

一般的な使用例には次のものがあります:
- **製品の推奨事項** メールテンプレート、キャンペーン、またはアプリ内エクスペリエンスにパーソナライズされた製品の推奨事項を埋め込むことを簡素化するため
- **パーソナライズされたマーケティングキャンペーンを強化する**ために、動的な製品推奨を使用してマーケティング接点を充実させる
- **アプリ内またはウェブのパーソナライゼーションを提供する**、例えば、カスタマイズされた検索結果、コホートベースの価格設定とメッセージング、記事の推薦、または最寄りの店舗の場所
- **財務データまたは医療データに基づく推奨事項**—財務データには厳格な要件があり、Hightouchはその[厳格なデータセキュリティポリシー](https://hightouch.com/docs/security/overview#compliance)を通じてこれらの要件を満たしています。Hightouchを使用すると、セグメンテーション基準に使用される基礎的な属性を公開することなく、財務データや医療データに基づいて顧客セグメントを作成できます。

{% endtab %}
{% tab Datasets %}

### データセット

パーソナライゼーションAPIは、倉庫内の選択されたデータのキャッシュとして機能するため、すでにそこに推奨データが保存されている必要があります。必要に応じてテンプレートに従って変換するためにHightouchを使用できます。この種類のデータには以下が含まれます：
- 地理的地域、年齢、その他の人口統計情報などのユーザーメタデータ
- ユーザーの行動やイベント、過去の購入、ページビュー、クリックなど。

{% endtab %}
{% endtabs %}

## 統合

### ステップ1:データソースをHightouchに接続する

Hightouch [sources](https://hightouch.com/docs/getting-started/concepts#sources) は、組織's business data lives. In this case, it's がユーザーデータを保存している場所です。
1. Hightouchで、**ソースの概要 > ソースの追加**に移動します。ソースとしてデータウェアハウスを選択します。<br><br>
2. 関連する資格情報を入力します。これらはソースによって異なります。 

詳細については、関連するソース[ドキュメント](https://hightouch.com/docs)を参照してください。

### ステップ2:モデルデータ

Hightouchのモデルは、ソースからどのデータを取得するかを定義します。新しいモデルを設定するには、次の手順に従ってください:

1. Hightouch で、[**モデルの概要**](https://app.hightouch.com/models) > **モデルの追加** に移動し、接続したばかりのソースを選択します。<br><br>
2. 次に、[モデリング方法](https://hightouch.com/docs/models/creating-models)を選択します。すべての情報を1つのテーブルに結合する必要があるため、ビジュアルテーブルセレクターを使用して定義できます。あるいは、必要な列だけを含めるようにSQLを書いたり、既存のdbtモデル、Lookerのルック、またはSigmaのワークブックに依存することもできます。<br><br>
3. 続行する前に、モデルをプレビューして、興味のあるものかどうかを確認してください's querying the data you'。デフォルトでは、Brazeはプレビューを最初の100レコードに制限します。データを検証した後、**続行**をクリックします。<br><br>
4. モデルに名前を付けます。例えば、「ユーザーの推薦」です。<br><br>
5. 最後に、主キーを選択して**完了**をクリックします。主キーは一意の識別子を持つ列であるべきです。これはまた、あなたの'll use to call the personalization API to retrieve a particular user'sの推奨事項です。

### ステップ3:パーソナライズAPIを構成する

リクエストを受信するためのAPIの準備には2つのステップがあります:
- インフラストラクチャに最も近い地域でパーソナライズAPIを有効にする
- Hightouch管理のキャッシュでマテリアライズされるモデルを定義するための同期の作成

これらの指示に従って両方を完了してください:

1. Hightouchで、[**宛先**](https://app.hightouch.com/destinations)に移動し、あなたのために作成されたHightouchパーソナライゼーションAPIを選択します。この宛先が有効になっていない場合は、[Hightouchサポート](mailto:friends@hightouch.com)に連絡してください。<br><br>
2. 次に、適切な地域を選択します。インフラストラクチャに最も近い地域を選択すると、応答時間が短縮されます。インフラストラクチャに近い地域が見つからない場合は、[Hightouchサポート](mailto:friends@hightouch.com)に連絡してください。<br><br>
3. [**同期**概要ページ](https://app.hightouch.com/syncs)に移動し、**同期を追加**ボタンをクリックします。次に、関連するモデルと以前に設定した宛先を選択します。<br><br> 
4. 英数字のコレクション名を入力してください。コレクションは概念的にはデータベースのテーブルに似ています。それぞれは、顧客や請求書などの特定のデータ型を表す必要があります。コレクション名は英数字でなければならず、パーソナライゼーションAPIエンドポイントの一部になります。<br><br>
5. 次に、モデルのどの列をレコード検索のプライマリインデックスとして使用するかを指定します。このフィールドはコレクション内の各レコードを一意に識別する必要があり、しばしばモデルの主キーと同じです。パーソナライゼーションAPIは、複数のインデックスでのルックアップをサポートしています。例えば、`user_id`、`anonymous_id`、または`email_address`を使用して顧客プロファイルを取得することができます。複数のインデックスを有効にするには、[Hightouchサポート](mailto:friends@hightouch.com)に連絡してください。<br><br>
6. フィールドマッパーを使用して、モデルからAPI応答ペイロードに含める列を指定します。これらのフィールドの名前を変更し、Liquidテンプレート言語を使用して変換を適用するために高度なマッパーを使用できます。<br><br>
7. ご利用のケースに適した[削除動作](https://www.hightouch.com/docs/destinations/personalization-api#delete-behavior)を選択してください。<br><br>
8. 最後に、**続行**をクリックして、[同期スケジュール](https://hightouch.com/docs/syncs/schedule-sync-ui)を選択します。

Hightouchは、データウェアハウス内のデータを管理されたデータベースに同期し、パーソナライゼーションAPIを介して公開します。

### ステップ 4:Braze Connected Contentを通じてパーソナライゼーションAPIを呼び出す

パーソナライズAPIインスタンスを設定したら、それをBraze Connected Contentエンドポイントとして使用できます。 

APIは`https://personalization.{region}.hightouch.com`でアクセス可能です。例えば、`https://personalization.us-west-2.hightouch.com`。 

このエンドポイント`/v1/collections/:collection_name/records/:index_key/:index_value`を使用して情報を利用できます。

例えば、このスニペットをキャンペーンやキャンバスに含めることができます:

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

JSON ペイロードで返されるプロパティを参照し、それらをメッセージングで使用するために Liquid テンプレートを使用できます。

以下の例のペイロードの場合:

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

次のLiquidリファレンスはこの例のデータを返します:

| 液体テンプレート | 返された例 |
| --- | --- |
| {% raw %}`{{artists.recommendations.concerts[0].artist}}`{% endraw %}| エイフェックス・ツイン |
| {% raw %}`{{artists.recommendations.concerts[0].location}}`{% endraw %}| サンフランシスコ、カリフォルニア州 |
| {% raw %}`{{artists.recommendations.upcoming_album_release.title}}`{% endraw %}| ユニバーサル言語 |
{: .reset-td-br-1 .reset-td-br-2}

## トラブルシューティング

ご質問がある場合は、[Hightouchサポート](mailto:friends@hightouch.com)にお問い合わせください。

[1]: {% image_buster /assets/img/hightouch/cohort5.png %}
[2]: {% image_buster /assets/img/hightouch/cohort6.png %}  
[3]: {% image_buster /assets/img/hightouch/cohort7.png %}  
