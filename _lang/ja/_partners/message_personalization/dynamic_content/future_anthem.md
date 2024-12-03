---
nav_title: 未来の賛歌
article_title: 未来の賛歌
description: "Future AnthemとBrazeの統合方法を学習する。"
alias: /partners/future_anthem/
page_type: partner
search_tag: Partner
---

# 未来の賛歌

> フューチャーアンセムのリアルマネーゲーム業界向けオールインワン製品であるAmplifier AIは、コンテンツのパーソナライゼーション、リアルタイム体験、ダイナミックなオーディエンスを提供する。Amplifier AIは、スポーツ、カジノ、宝くじにシームレスに対応し、カスタマーは、好きなゲーム、好きなチーム、エンゲージメントスコア、次のベットの推奨、予想される次のベットなど、業界固有のプレイヤー属性でBrazeのプレイヤープロファイルを強化することができる。

{% alert important %}
この機能は現在アーリーアクセス中である。まずはFuture Anthemカスタマーサクセスチームまでご連絡を。
{% endalert %}

## 前提条件

| 必要条件              | 説明                                            |
|--------------------------|--------------------------------------------------------|
| 将来のアンセム口座    | フューチャー・アンセムのアカウントだ。 |
| Braze REST API キー       | を持つREST APIキー。 [`users.track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track).これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze RESTエンドポイント      | インスタンスにマッチするBraze[RESTエンドポイント](https://www.braze.com/docs/developer_guide/rest_api/basics/#endpoints)、例えば`rest.iad-01.com` 。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ユースケース

この統合により、次のことが可能になります。

- エンゲージメントスコアが高いユーザーを識別子し、限定プロモーションやVIP報酬など、パーソナライズされたオファーを提供する。
- ユーザーがすでに好きなゲーム群に基づいて、似たようなゲームをユーザーに提案する。

## 統合

フューチャーアンセムカスタマーサクセスチームが統合の設定をサポートする。カスタマーサクセスの担当者にご連絡いただければ、Brazeに送信する最も関連性の高い属性を特定するお手伝いをいたします。

|フューチャーアンセムのアトリビューション属性例|アトリビューションの属性例|
|-----------------------------------|---------------------------|
|![ユーザープロファイルの属性。]({% image_buster /assets/img/future_anthem/future_anthem_example_attributes.png %})|![オブジェクト属性。]({% image_buster /assets/img/future_anthem/braze_example_attributes.png %})|

## カスタム属性のアトリビューション

これらは利用可能なBrazeカスタム属性である。より詳細な情報については、[Future Anthemを参照のこと：Getting Started](https://knowledge.futureanthem.com/getting-started).

{% tabs local %}
{% tab ベットの推奨 %}

| サブカテゴリー | 例（JSON） | データ型 |
| ------- | ----------- |----------- |
| ユーザー設定 | `{"Sport": "Ice Hockey", "League": "NHL", "Market": "Goals", "Team": "Rangers", "Player": "Kreider"}`| オブジェクト |
| シングルベットの推奨 | `{"Sport": "Ice Hockey", "League": "NHL", "Market": "Goals", "Team": "Rangers", "Player": "Kreider"}`| オブジェクト |
| アキュムレーター・ベットの推奨 | `{"Bet_1": "Halland Goal vs. Manchester United", "Bet_2": "Liverpool vs. Everton"}`| オブジェクト |
| アキュムレーター・ベットの推奨 | `{"Bet_1": 1.5, "Bet_2": 2}` | オブジェクト |
| ベットビルダーのベット推奨 | `{"Sport":"American Football", "Competition":"NFL", "Event":"Seahwaks@Giants", "Market":"MoneyLine", "Selection":"Seahawks"}`| オブジェクト |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab ボーナス推薦 %}

| サブカテゴリー | 例 | データ型 |
| ------- | ----------- |----------- |
|NGR - ユーザー生涯のネットゲーミング収入 | 2232| 数値|
| NGR14 - 過去14日間のネットゲーミング収入 | 42 | 数値
| 選手の収益性スコア| 130 | 数値 |
| エンゲージメント・スコア | 0.78 | 数値 |
| 解約リスクスコア | 0.02 | 数値 |
| 次回のベット予定日 | 2024-08-29 | 時刻 |
| ベット＆ゲット - ボーナス価値推奨 | 20 | 数値 |
| 今後、その他のボーナス・バリューを推奨する | 0 | 数値 |
| 将来のCLTV  | 3126 | 数値 |

{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab おすすめゲーム %}

| サブカテゴリー | 例 | データ型 |
| ------- | ----------- |----------- |
| あなたにおすすめ | フラッフィー」、「フィッシン・フレンジー」、「ビッグ・バス・ボナンザ」、「レインボー・ゴールド」、「ワイルド・ウェスト| 配列 |
| お気に入りのゲーム | フィッシン・フレンジー | 配列 |
| おすすめ新作ゲーム | スティッキネス、ディープ・メガウェイズ、ゴールド・パーティー、フリントストーン| 配列 |
| あなたのような選手がプレーしている（協調フィルタリング） |ゴールドブリッツ、ビッグバススプラッシュ、リック・アンド・モーティ、ブック・オブ・デッド、オリンポスの門、ラック・オ・アイリッシュ | 配列 |
| あなたがプレーしたから（ゲームの類似性）|Fluffy Favourites 2, Luck Rish Express, Gold Cash, Aztec Treasure Hunt, Stars Bonanza | 配列 |
| 次ページ（ゲームの順序） | フィッシン・フレンジー ザ・ビッグ・キャッチ」、「ビッグ・バンカー」、「9 Masks Of Fire」、「スーパー・ライオン」、「フィッシン・ビガー・ポット・オブ・ゴールド | 配列 |
| 人気ゲーム | テンプル・オブ・アイリス, フィッシング・フレンジー, リッシング報酬, クレイジー・タイム, フラッフィー・フェイバリット | 配列 |
| トレンドゲーム | ピッグバンカー、ハイパーゴールド、ピラミッドキング、ゴールドキャッシュ | 配列 |

{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}

{% tab 選手クラスタ %}

| サブカテゴリー | 例 | データ型 |
| ------- | ----------- |----------- |
| 選手がどのクラスタにいるかを表示する | 高価値ゲーム 多様性| string |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}

{% tab 選手の持続性 - 選手の潜在的リスク %}

| サブカテゴリー | 例 | データ型 |
| ------- | ----------- |----------- |
| リスクスコア | 0.5| 数値 |
| 危険な選手 | 正しい | ブール値 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}
