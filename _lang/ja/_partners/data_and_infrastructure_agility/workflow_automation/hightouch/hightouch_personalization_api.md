---
nav_title: ハイタッチ・パーソナライゼーションAPI
article_title: ハイタッチ・パーソナライゼーションAPI
description: "この参考記事では、BrazeとHightouchのPersonalization APIとの統合について概説している。Personalization APIは、クラウドデータウェアハウス内の任意のデータセットに基づく低遅延データAPIをホスティングするマネージドサービスである。このリファレンス記事では、Hightouch Personalization APIが解決するユースケース、使用するデータ、設定方法、Brazeとの統合方法について説明する。"
page_type: partner
search_tag: Partner
---

# ハイタッチ・パーソナライゼーションAPI

> Hightouchの[パーソナライゼーションAPIは](https://hightouch.com/docs/destinations/personalization-api)、クラウドデータウェアハウス内の任意のデータセットに基づく低遅延データAPIをホストできるマネージドサービスである。

![][3]

BrazeとHightouchの統合により、[Braze Connected Contentで](https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/)APIを使用し、送信時にキャンペーンやCanvasに最新の顧客データやオブジェクトデータを取り込むことができる。

HightouchのPersonalization APIは、Braze設定内で使用するRESTエンドポイントを提供する。具体的には、BrazeのConnected Contentオファリングを使用して、Personalization APIにGETリクエストを行い、特定の識別子に関連するすべての情報を取得することができる。このAPIによって公開されるデータは、顧客、製品、またはその他のオブジェクトデータを表すことができる。 

![][2]

## 前提条件

| 必要条件| 説明|
| ---| ---| 
| パーソナライゼーションAPIを有効にした[Hightouchアカウント](https://app.hightouch.com/login) | このパートナーシップを利用するには、[ハイタッチ・ビジネス・ティア・アカウントが](https://hightouch.com/pricing)必要である。|
| 定義されたユースケース | APIをセットアップする前に、この統合のユースケースを決定しなければならない。一般的な使用例については、以下のリストを参照のこと。 |
| クラウドデータウェアハウスまたはその他のソースに保存されているデータ | ハイタッチは[25以上のデータソースと](https://hightouch.com/integrations)統合する |
| ハイタッチAPIキー | これは、**ハイタッチ＞設定＞APIキー＞APIキーの追加で**作成できる。 |
{: .reset-td-br-1 .reset-td-br-2}

{% tabs %}
{% tab 使用例 %}

### ユースケース

始める前に、パーソナライゼーションAPIをどのように使いたいかを正確に計画しておくと便利だ。

一般的な使用例には以下のようなものがある：
- メールテンプレート、キャンペーン、アプリ内エクスペリエンスにパーソナライズされたおすすめ**商品を**埋め込むことを効率化する。
- マーケティング・タッチポイントをダイナミックな商品レコメンデーションで充実さ**せる**ことで、**パーソナライズされたマーケティング・キャンペーンを強力に推進する**。
- 例えば、カスタマイズされた検索結果、コホートベースの価格設定、メッセージング、おすすめ記事、最寄りの店舗など、**アプリ内またはウェブでパーソナライゼーションを提供する**。
- **財務データや医療データに基づく推薦-財務**データには厳しい要件があり、ハイタッチは[厳格なデータ・セキュリティ・ポリシーによって](https://hightouch.com/docs/security/overview#compliance)これを満たしている。Hightouchを使用すると、セグメンテーション基準で使用される基本的な属性を公開することなく、財務データや医療データに基づいて顧客セグメントを作成することができる。

{% endtab %}
{% tab データセット %}

### データセット

パーソナライゼーションAPIは、ウェアハウス内の選択されたデータのキャッシュとして機能するため、レコメンデーションデータはすでにそこに保存されているはずだ。必要であれば、ハイタッチを使ってテンプレートに従って変形させることができる。この種のデータには以下が含まれる：
- 地理的地域、年齢、その他の人口統計学的情報などのユーザー・メタデータ
- 過去の購入、ページビュー、クリックなどのユーザーアクションやイベント。

{% endtab %}
{% endtabs %}

## 統合

### ステップ1:データソースをハイタッチに接続する

[ハイタッチ・ソースは](https://hightouch.com/docs/getting-started/concepts#sources)、組織のビジネス・データが存在する場所である。この場合、ユーザーデータが保存されている場所であればどこでもいい。
1. ハイタッチで、「**ソースの概要」＞「ソースの追加**」と進む。ソースとしてデータウェアハウスを選択する。<br><br>
2. 関連する認証情報を入力する。これらはソースによって異なる。 

詳細については、関連するソース・[ドキュメントを](https://hightouch.com/docs)参照のこと。

### ステップ2:モデルデータ

ハイタッチ・モデルは、ソースからどのようなデータを引き出すかを定義する。新しいモデルをセットアップするには、以下の手順に従う：

1. ハイタッチでは [**モデルの概要**](https://app.hightouch.com/models)**> モデルを追加**]を選択し、先ほど接続したソースを選択する。<br><br>
2. 次に、[モデリング方法を](https://hightouch.com/docs/models/creating-models)選択する。すべての情報を1つのテーブルにまとめる必要があるので、ビジュアル・テーブル・セレクタを使って定義することができる。あるいは、必要なカラムだけを含むSQLを書いたり、既存のdbtモデル、ルッカー・ルック、シグマ・ワークブックに頼ることもできる。<br><br>
3. 続行する前に、モデルをプレビューして、興味のあるデータを照会していることを確認する。デフォルトでは、Brazeはプレビューを最初の100レコードに制限している。データを確認したら、**Continueを**クリックする。<br><br>
4. 例えば、"User recommendations "のように、モデルに名前をつける。<br><br>
5. 最後に、主キーを選択し、**Finishを**クリックする。主キーは一意な識別子を持つカラムでなければならない。これは、パーソナライゼーションAPIを呼び出して特定のユーザーのおすすめを取得するために使用するフィールドでもある。

### ステップ3:パーソナライゼーションAPIを設定する

リクエストを受け取るためにAPIを準備するには、2つのステップがある：
- お客様のインフラに最も近い地域でパーソナライゼーションAPIを有効にする
- Hightouchが管理するキャッシュで実体化されるべきモデルを定義するためにシンクを作成する。

以下の指示に従って、両方を完了させる：

1. ハイタッチでは [**目的地**](https://app.hightouch.com/destinations)を選択し、あなたのために作成されたHightouchパーソナライゼーションAPIを選択する。この宛先が有効になっていない場合は、[ハイタッチ・サポートに](mailto:friends@hightouch.com)連絡すること。<br><br>
2. 次に、適切な地域を選択する。インフラに最も近い地域を選択することで、応答時間を短縮することができる。お住まいのインフラに近い地域が表示されない場合は、[ハイタッチ・サポートまで](mailto:friends@hightouch.com)ご連絡を。<br><br>
3. [**シンクの**概要ページに](https://app.hightouch.com/syncs)移動し、**シンクを追加**ボタンをクリックする。次に、該当するモデルと、以前に設定した保存先を選択する。<br><br> 
4. 英数字のコレクション名を入力する。コレクションは概念的にはデータベースのテーブルに似ている。それぞれ、顧客や請求書など、特定のデータ型を表す必要がある。コレクション名は英数字でなければならず、Personalization APIエンドポイントの一部となる。<br><br>
5. 次に、モデルのどのカラムをレコード検索のプライマリー・インデックスとして使用するかを指定する。このフィールドは、コレクション内の各レコードを一意に識別する必要があり、多くの場合、モデルの主キーと同じである。パーソナライゼーションAPIは、複数のインデックスの検索をサポートする。例えば、`user_id` 、`anonymous_id` 、`email_address` を使って顧客プロファイルを検索したい。複数のインデックスを有効にするには、[ハイタッチ・サポートに](mailto:friends@hightouch.com)連絡すること。<br><br>
6. フィールドマッパーを使用して、APIレスポンスペイロードに含まれるべきモデルのカラムを指定する。これらのフィールドの名前を変更し、リキッドテンプレート言語を使用して変換を適用するために高度なマッパーを使用することができる。<br><br>
7. ユースケースに適した[削除動作を](https://www.hightouch.com/docs/destinations/personalization-api#delete-behavior)選択する。<br><br>
8. 最後に、「**続ける**」をクリックし、[同期スケジュールを](https://hightouch.com/docs/syncs/schedule-sync-ui)選択する。

Hightouchは、ウェアハウスのデータを管理データベースに同期し、パーソナライゼーションAPIを介して公開する。

### ステップ4:Braze Connected Contentを通じてパーソナライゼーションAPIを呼び出す

パーソナライゼーションAPIインスタンスを設定したら、それをBraze Connected Contentのエンドポイントとして使用できる。 

APIは`https://personalization.{region}.hightouch.com` 、例えば`https://personalization.us-west-2.hightouch.com` からアクセスできる。 

情報はこのエンドポイント`/v1/collections/:collection_name/records/:index_key/:index_value` を使って入手できる。

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

次のリキッド参照は、この例のデータを返すだろう：

| 液体テンプレート | 返却例 |
| --- | --- |
| {% raw %}`{{artists.recommendations.concerts[0].artist}}`{% endraw %}| エイフェックス・ツイン |
| {% raw %}`{{artists.recommendations.concerts[0].location}}`{% endraw %}| カリフォルニア州サンフランシスコ |
| {% raw %}`{{artists.recommendations.upcoming_album_release.title}}`{% endraw %}| ユニバーサル・ランゲージ |
{: .reset-td-br-1 .reset-td-br-2}

## トラブルシューティング

質問がある場合は、[ハイタッチ・サポートに](mailto:friends@hightouch.com)問い合わせること。

[1]: {% image_buster /assets/img/hightouch/cohort5.png %}
[2]: {% image_buster /assets/img/hightouch/cohort6.png %}  
[3]: {% image_buster /assets/img/hightouch/cohort7.png %}  
