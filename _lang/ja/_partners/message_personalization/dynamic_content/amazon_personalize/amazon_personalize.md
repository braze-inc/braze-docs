---
nav_title: Amazon Personalize
article_title:Amazon Personalize
alias: /partners/amazon_personalize/
description:この記事では、BrazeとAmazon Personalizeの統合およびリファレンスアーキテクチャについて概説します。この記事は、Amazon Personalizeが提供するユースケース、そのデータの取り扱い方法、サービスの設定方法、およびBrazeとの統合方法を理解するのに役立ちます。
page_type: partner
search_tag:Partner
---

# Amazon Personalize
<!--
{% multi_lang_include video.html id="xFZ3HMleYYE" align="right" %}
-->
> Amazon Personalizeは、まるで自分専用の終日Amazon機械学習レコメンデーションシステムを持っているかのようです。20年以上の推薦経験に基づき、Amazon Personalizeはリアルタイムのパーソナライズされた製品およびコンテンツの推薦とターゲットを絞ったマーケティングプロモーションを提供することで、顧客エンゲージメントを向上させることができます。

機械学習とあなたが定義するアルゴリズムを使用して、Amazon Personalizeはあなたのウェブサイトやアプリケーションに高品質の推薦を出力するモデルをトレーニングするのに役立ちます。これらのモデルにより、ユーザー' past behaviors, sort items by relevancy, and recommend other items based on similarity. Lists obtained from the Amazon Personalize API can then be used in Braze Connected Content to run personalized Braze recommendation campaigns. By integrating with Amazon Personalize, customers are given the freedom to control the parameters used to train the models and define optional business objectives that optimize the algorithm'の出力に基づいて推奨リストを作成できます。 

この記事は、Amazon Personalizeが提供するユースケース、そのデータの取り扱い方法、サービスの設定方法、およびBrazeとの統合方法について理解するのに役立ちます。

## 前提条件

| 要件| 説明|
| ---| ---| 
| Amazon Web Service アカウント | このパートナーシップを利用するには、AWSアカウントが必要です。AWSアカウントを取得した後、Amazon Personalizeコンソール、AWSコマンドラインインターフェイス（AWS CLI）、またはAWS SDKを通じてAmazon Personalizeにアクセスできます。 |
| 定義された使用例 | モデルを作成する前に、この統合の使用例を決定する必要があります。次のリストを参照して、一般的な使用例を確認してください。 |
| データセット | Amazon Personalize のレコメンデーションモデルには、インタラクション、ユーザー、アイテムの3種類のデータセットが必要です。次のデータセットの要件を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% tabs %}
{% tab Use Cases %}

**ユースケース**

モデルを作成する前に、この統合の使用例を決定する必要があります。いくつかの一般的な使用例には以下が含まれます：
- ユーザーの以前のやり取りに基づいてアイテムを推薦し、ユーザーにとって本当にパーソナライズされた体験を作り出します。
- 各ユーザーに合わせたアイテムや検索結果のリストを提供し、ユーザーに関連性の高いアイテムを表示することでエンゲージメントを高めます。
- 類似のアイテムのおすすめを見つけ、ユーザーが新しいものを発見できるようにします。

次のガイドでは、ユーザーの個別化された推奨事項のレシピに焦点を当てます。

{% endtab %}
{% tab Datasets %}

**データセット**

Amazon Personalizeのレコメンデーションモデルを開始するには、3種類のデータセットが必要です:

- インタラクション
  - ユーザーとアイテム間の履歴のやり取りを保存します
  - 必要な`USER_ID`、`ITEM_ID`、`EVENT_TYPE`、`TIMESTAMP`の値と、オプションでイベントに関するメタデータを受け入れます
- ユーザー
  - ユーザーに関するメタデータを保存します
  - `USER_ID` の値と、性別、年齢、ロイヤルティメンバーシップなどのメタデータフィールド（文字列または数値）が少なくとも1つ必要です。
- アイテム
  - アイテムに関するメタデータを保存します
  - `ITEM_ID`と、アイテムを説明する少なくとも1つのメタデータフィールド（テキスト、カテゴリカル、または数値）が必要です。

ユーザー推薦レシピの場合、少なくとも25人のユニークユーザーからそれぞれ少なくとも2回のインタラクションを含む、少なくとも1000ポイントのインタラクションデータを含むインタラクションデータセットを提供する必要があります。これらのデータセットは、S3に保存されたCSVファイルを使用して一括でアップロードするか、APIを通じて段階的にアップロードできます。

{% endtab %}
{% endtabs %}

## モデルの作成

### ステップ1:トレーニング

データセットがインポートされると、ソリューションを作成できます。ソリューションは、モデルをトレーニングするためにAmazon Personalizeの[レシピ](https://docs.aws.amazon.com/personalize/latest/dg/working-with-predefined-recipes.html)（アルゴリズム）の1つを使用します。私たちの場合、`USER_PERSONALIZATION`レシピを使用します。ソリューションのトレーニングは、ソリューションバージョン（訓練されたモデル）を作成し、モデルのパフォーマンス指標に基づいて評価することができます。

Amazon Personalizeを使用すると、モデルがトレーニングに使用するハイパーパラメータを調整できます。以下に例を示します。
- Amazon Personalize コンソールにある「ユーザー履歴の長さのパーセンタイル」パラメータは、トレーニングに含めるユーザー履歴のパーセンタイルを調整できます。<br><br>![最小最大ユーザープロファイル設定][3]
  - `min_user_history_length_percentile`: 非常に短い履歴のユーザーの割合を除外することで、人気のあるアイテムを排除し、より深い基礎的なパターンに基づいて推奨を構築するのに役立ちます。
  - `max_user_history_length_percentile`: 非常に長い履歴の長さでトレーニングする際に考慮するユーザーの割合を調整します。

隠れ次元の数は、複雑なデータセットのより複雑なパターンを検出するのに役立ちます。一方、時間を通じた逆伝播技術（BPTT）は、一連のイベントが発生した後に高価値のアクションをもたらした初期のイベントに対する報酬を調整します。

さらに、Amazon Personalizeは、異なる値を持つ複数のバージョンのソリューションを同時に実行することによって、自動ハイパーパラメータチューニングを提供します。ソリューションを作成する際に**HPOを実行**をオンにしてチューニングを使用します。

### ステップ2:評価と比較

ソリューションのトレーニングが完了すると、評価して異なるバージョンを比較する準備が整います。各ソリューションバージョンは計算されたメトリクスを表示します。利用可能なメトリクスのいくつかには次のものが含まれます:

- `Normalize discounted cumulative gain`: 推奨されるアイテムの順序を実際のアイテムリストと比較し、リスト内の位置に対応する重みを各アイテムに与えます
- `Precision @k`: 適切に推奨されたアイテムの数をすべての推奨アイテムの数で割った値で、`k` はアイテムの数です
- `Mean reciprocal rank`: 最初の、最も高くランク付けされた推奨事項に焦点を当て、最初の一致した推奨事項が表示されるまでに表示される推奨項目の数を計算します
- `Coverage`: データセット内の一意のアイテムの総数に対する一意の推奨アイテムの割合

## おすすめを取得する

ソリューションバージョンが満足のいくものになったら、推奨事項を活用する時です。推奨事項にアクセスする方法は2つあります:

1. リアルタイムキャンペーン<br>キャンペーンは、定義された最小トランザクションスループットを持つデプロイされたソリューションバージョンです。トランザクションは推奨出力を取得するための単一のAPI呼び出しであり、TPS（1秒あたりのトランザクション数）として定義され、最小値は1です。キャンペーンは負荷が増加した場合にリソースをスケールしますが、最低値を下回ることはありません。コンソール、AWS CLI、またはコード内のAWS SDKを通じて推奨事項を照会できます。<br><br>
2. バッチジョブ<br>バッチジョブは推奨事項をS3バケットにエクスポートします。この仕事は、推奨事項をエクスポートしたいユーザーIDのリストを含むJSONファイルを入力として受け取ります。次に、正しい権限と出力先を指定したら、ジョブを実行する準備が整います。実行時間は、データセットのサイズと推奨リストの長さに依存します。

### フィルター

フィルターを使用すると、アイテムのID、イベントタイプ、またはメタデータに基づいてアイテムを除外することで、推奨出力を調整できます。また、年齢やロイヤルティメンバーシップのステータスなどのメタデータに基づいてユーザーをフィルタリングすることもできます。フィルターは、ユーザーがすでに操作したアイテムを推奨するのを防ぐのに役立ちます。

## Brazeとの結果の統合

作成されたモデルと推奨キャンペーンを使用して、コンテンツカードと接続されたコンテンツを使用してユーザー向けにBrazeキャンペーンを実行する準備が整いました。
Brazeキャンペーンを実行する前に、これらの推奨事項をAPIを通じて提供できるサービスを作成する必要があります。AWSサービスを使用してサービスをデプロイするには、ワークショップ記事の[ステップ3][1]に従うことができます。独自のバックエンドサービスを展開して、推奨事項を提供することもできます。

### コンテンツカードキャンペーンのユースケース

リストの最初の推奨アイテムを使用してコンテンツカードキャンペーンを実行しましょう。<br><br>
次の例では、クエリを実行します
`GET http://<service-endpoint.com>/recommendations?user_id=user123` エンドポイントに`user_id` パラメータを指定すると、推奨アイテムのリストが返されます:

```json
[
  {
    "id": "abc123",
    "url": "http://productpage.com/product/abc123",
    "name": "First Item",
    "price": 39.99,
    "image": "http://pp.cdn.com/abvh3321pjb1j"
  },
  {
    "id": "xyz987",
    "url": "http://productpage.com/product/xyz987",
    "name": "Great Item",
    "price": 19.99,
    "image": "http://pp.cdn.com/234bjl1gioj1b2b"
  },
  ...
]
```

Brazeダッシュボードで、新しい[コンテンツカードキャンペーン]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/)を作成します。メッセージテキストフィールドで、APIをクエリして応答を`recommendations`変数に保存するためのConnected Content Liquidブロックを作成します。

{% raw %}

```liquid
{% connected_content https:/<service-endpoint.com>/recommendations?user_id={{${user_id}}} :save recommendations %}
```

次に、結果の配列の最初の項目を参照して、ユーザーにコンテンツを表示できます。

```liquid
This seems like a great fit for you:
{% recommendations[0].name %}
{% recommendations[0].price %}
```

{% endraw %}

タイトル、画像、URLのリンクを含めて、これが完全なコンテンツカードの外観です:

![メッセージ本文と「画像を追加」フィールドに接続されたコンテンツが追加されたキャンペーンの画像。この画像は、「Web URLにリダイレクト」フィールドに追加された接続コンテンツロジックを示しており、ユーザーを推奨URLにリンクしています。][2]

[1]: {{site.baseurl}}/partners/message_personalization/dynamic_content/amazon_personalize/workshop/#step-3-send-personalized-emails-from-braze
[2]: {% image_buster /assets/img/amazon_personalize/content-card-campaign.png %}
[3]: {% image_buster /assets/img/amazon_personalize/min_and_max_user_percentile.png %}