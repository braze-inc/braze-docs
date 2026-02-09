---
nav_title: Future Anthem
article_title: Future Anthem
description: "Future AnthemとBrazeの統合方法を学習する。"
alias: /partners/future_anthem/
page_type: partner
search_tag: Partner
---

# Future Anthem

> [フューチャーアンセムの](https://www.futureanthem.com/)リアルマネーゲーム業界向けオールインワン製品であるAmplifier AIは、コンテンツのパーソナライゼーション、リアルタイム体験、ダイナミックなオーディエンスを提供する。Amplifier AIはスポーツ、カジノ、宝くじにシームレスに対応し、カスタマーはBrazeのプレイヤープロファイルを、好きなゲーム、好きなチーム、エンゲージメントスコア、次のベットの推奨度、予想される次のベットなど、業界特有のプレイヤー属性で強化することができる。

{% alert important %}
この機能は現在早期アクセス段階です。まずはFuture Anthemカスタマーサクセスチームにご連絡を。
{% endalert %}

## 前提条件

| 必要条件              | 説明                                            |
|--------------------------|--------------------------------------------------------|
| Future Anthem アカウント    | Future Anthem アカウントです。 |
| Braze REST API キー       | [`users.track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) を持つ Braze REST API キー。これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze RESTエンドポイント      | インスタンスにマッチするBraze[RESTエンドポイント]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)、例えば`rest.iad-01.com` 。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ユースケース

この統合により、次のことが可能になります。

- エンゲージメントスコアが高いユーザーを特定し、限定プロモーションや VIP 特典などのパーソナライズされたオファーでそれらのユーザーをターゲットにします。
- ユーザーがすでに好きなゲーム群に基づいて、似たようなゲームをユーザーに提案する。

## 統合

Future Anthem カスタマーサクセスチームが統合の設定をサポートします。カスタマーサクセスの担当者にご連絡いただければ、Brazeに送信する最も関連性の高い属性を特定するお手伝いをいたします。

|Future Anthem の属性例|Braze の属性例|
|-----------------------------------|---------------------------|
|![ユーザープロファイルの属性。]({% image_buster /assets/img/future_anthem/future_anthem_example_attributes.png %})|![オブジェクト属性。]({% image_buster /assets/img/future_anthem/braze_example_attributes.png %})|

## Braze のカスタム属性

これらは利用可能なBrazeカスタム属性である。より詳細な情報については、[Future Anthem を参照してください。はじめに](https://knowledge.futureanthem.com/getting-started).

{% tabs local %}
{% tab Bet Recommendations %}

| サブカテゴリー | 例（JSON） | データ型 |
| ------- | ----------- |----------- |
| ユーザー設定 | `{"Sport": "Ice Hockey", "League": "NHL", "Market": "Goals", "Team": "Rangers", "Player": "Kreider"}`| オブジェクト |
| シングルベットの推奨 | `{"Sport": "Ice Hockey", "League": "NHL", "Market": "Goals", "Team": "Rangers", "Player": "Kreider"}`| オブジェクト |
| アキュムレーター・ベットの推奨 | `{"Bet_1": "Halland Goal vs. Manchester United", "Bet_2": "Liverpool vs. Everton"}`| オブジェクト |
| アキュムレーター・ベットの推奨 | `{"Bet_1": 1.5, "Bet_2": 2}` | オブジェクト |
| ベットビルダーのベット推奨 | `{"Sport":"American Football", "Competition":"NFL", "Event":"Seahwaks@Giants", "Market":"MoneyLine", "Selection":"Seahawks"}`| オブジェクト |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Bonus Recommendations %}

| サブカテゴリー | 例 | データ型 |
| ------- | ----------- |----------- |
|NGR – ユーザーの存続期間における純ゲーム収益 | 2232| 数値|
| NGR –過去14日間のアクティビティの純ゲーム収益 | 42 | 数値
| 選手の収益性スコア| 130 | 数値 |
| エンゲージメント・スコア | 0.78 | 数値 |
| 解約リスクスコア | 0.02 | 数値 |
| 次回のベット予定日 | 2024年8月29日 | 時刻 |
| ベット＆ゲット - ボーナス価値推奨 | 20 | 数値 |
| 将来の他のボーナス値のおすすめ | 0 | 数値 |
| 将来のCLTV  | 3126 | 数値 |

{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Game Recommendations %}

| サブカテゴリー | 例 | データ型 |
| ------- | ----------- |----------- |
| あなたにおすすめ | フラッフィー・フェイバリッツ、フィッシン・フレンジー、ビッグ・バス・ボナンザ、レインボー・ゴールド、ワイルド・ウエスト| 配列 |
| お気に入りのゲーム | フィッシンフレンジー | 配列 |
| おすすめ新作ゲーム | スティッキー・ビーズ、ビウェア・ザ・ディープ・メガウェイズ、ゴールド・パーティ、ザ・フリントストーンズ| 配列 |
| あなたのようなプレイヤーがプレイしています (協調フィルタリング) |ゴールド・ブリッツ、ビッグ・バス・スプラッシュ、リック・アンド・モーティ、ブック・オブ・デッ」、ゲイツ・オブ・オリンプス、ラック・オブ・ジ・アイリッシュ | 配列 |
| あなたがプレイしたから (ゲームの類似性)|フラッフィー・フェイバリッツ2、ラック・リッシュ・エクスプレス、ゴールド・キャッシュ、アステカ・トレジャー・ハント、スターズ・ボナンザ | 配列 |
| 次へ (ゲームの順序) | フィッシン・フレンジー・ザ・ビッグ・キャッチ、ビッグ・バンカー、ナイン・マスクス・オブ・ファイア、スーパー・ライオン、フィッシン・ビガー・ポッツ・オブ・ゴールド | 配列 |
| 人気ゲーム | テンプル・オブ・アイリス、フィッシン・フレンジー、リッシング・リワード、クレイジー・タイム、フラッフィー・フェイバリッツ | 配列 |
| トレンドゲーム | ピッグ・バンカー、ハイパー・ゴールド、ピラミッド・キング、ゴールド・キャッシュ | 配列 |

{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}

{% tab Player Cluster %}

| サブカテゴリー | 例 | データ型 |
| ------- | ----------- |----------- |
| プレイヤーがどのクラスターにいるかを表示する | 高価値ゲームの多様性| string |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}

{% tab Player Sustain - Player potential risk %}

| サブカテゴリー | 例 | データ型 |
| ------- | ----------- |----------- |
| リスクスコア | 0.5| 数値 |
| 危険なプレイヤー | 正しい | ブール値 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}
