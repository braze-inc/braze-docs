---
nav_title: スクーバ
article_title: Scuba Analytics
description: "この Scuba と Braze のテクニカルリファレンスでは、Braze Segments を使用して Scuba のリアルタイムデータインサイトをアクティブにする方法を説明します。"
page_type: partner
search_tag: Partner
noindex: true
hidden: true
---

# Scuba Analytics

>[Scuba Analytics](https://scuba.io) は、高速時系列データ向けに設計された、機械学習を採用したフルスタックのデータコラボレーションプラットフォームです。Scuba では、ユーザー (アクターとも呼ばれます) を選択的にエクスポートし、Braze プラットフォームにそれらのユーザーを読み込むことができます。Scuba では、カスタムアクタープロパティを使用して動作トレンドを分析し、さまざまなプラットフォーム間でデータを有効化し、マシンラーニングを使用して予測モデリングを実行します。

_この統合は Scuba Analytics によって管理されます。_

## 前提条件

Braze で Scuba Analytics を使用するには、以下が必要です。

| 必要条件 | 説明 |
|---|---|
|Scuba API トークン | `https://{scuba_hostname}/api/create_token` エンドポイントから取得できる Scuba API トークン。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze RESTエンドポイント  | REST エンドポイントのURL。エンドポイントはインスタンスの [Braze URL](https://scuba.io) に応じて異なります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Braze への Scuba データのアップロード

{% alert important %}
以下の要求はcurl を使用します。API リクエストの管理を改善するには、Postman などの API クライアントを使用することをお勧めします。
{% endalert %}

Braze に Scuba データをアップロードするには、`https://scuba.pliant.io/a/scuba-connectors/prod/braze-activation` に対して `application/json` content-type を使用して POST リクエストを行います。

```bash
curl -X POST "https://scuba.pliant.io/a/scuba-connectors/prod/braze-activation" \
-H "content-type: application/json" \
-d '{"braze_host":"BRAZE_API_ENDPOINT", \
"braze_api_key":"BRAZE_API_KEY", \
"scuba_host":"HOSTNAME", \
"scuba_token":"SCUBA_API_TOKEN", \
"scuba_table_name":"TABLE_NAME", \
"scuba_actor_property_name":"ACTOR_PROPERTY_NAME", \
"scuba_actor_property_value_filter":"ACTOR_PROPERTY_FILTER" \
"scuba_actor_id":"ACTOR_ID", \
"scuba_period_start":"PERIOD_START", \
"scuba_period_end":"PERIOD_END", \
"scuba_record_limit":"RECORD_LIMIT"}'
```

次のように置き換えます。

| placeholder             | 説明                                                                                                                                                                                     |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `BRAZE_API_ENDPOINT`    | 現在の Braze インスタンスの Braze REST エンドポイント URL。詳細については、「[REST API キー]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/#rest-api-keys)」を参照してください。 |
| `BRAZE_API_KEY`         | `users.track` 権限を持つBraze REST API キー。                                                                                                                                      |
| `HOSTNAME`              | 現在のScuba インスタンスのホスト名。                                                                                                                                                    |
| `SCUBA_API_TOKEN`       | Scuba API トークン。                                                                                                                                                                           |
| `TABLE_NAME`            | データセットが属するテーブル。詳細については、[用語集:データセットテーブル](https://docs.scuba.io/glossary/dataset-table)。                                                                                                      |
| `ACTOR_PROPERTY_NAME`   | データセットが属するアクタプロパティ。この名前に一致するデータのみが返されます。詳細については、[用語集:アクタープロパティ ](https://docs.scuba.io/glossary/actor-property)。                                             |
| `ACTOR_PROPERTY_FILTER` | アクタープロパティのオーディエンス検索フィルター。                                                                                                                                             |
| `ACTOR_ID`              | データセットが属するアクタプロパティのID。この ID は、Braze の`external_id` に一致します。詳細については、[用語集:Actor](https://docs.scuba.io/glossary/actor).を参照してください。                                              |
| `PERIOD_START`          | BQL 互換の日付としての期間開始日。詳細については、[BQL構文および使用法](https://docs.scuba.io/guides/bql-syntax-and-usage)を参照してください。                                                                                                 |
| `PERIOD_END`            | BQL 互換の日付としての期間終了日。詳細については、[BQL構文および使用法](https://docs.scuba.io/guides/bql-syntax-and-usage)を参照してください。                                                                                                   |
| `RECORD_LIMIT`          | **オプション**:返されるレコードの最大数。`scuba_record_limit` が省略された場合、Scuba は最大100件のレコードを返します。これを変更するには、負でない数値を `scuba_record_limit` に割り当てます。    |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### デフォルト動作

デフォルトでは、`update_existing_only` は`false` に設定されています。これにより、Braze内の既存のレコードが更新され、存在しないレコードの新規レコードが作成されます。Scuba が新しいレコードを作成しないようにするには、`update_existing_only` を `true` に設定します。

### レート制限

Scuba は、1分あたり50,000件のリクエストのレート制限をこのエンドポイントに適用します。

## Scuba の行動データを使用したセグメントの作成

[データをアップロード](#uploading-your-scuba-data-to-braze)したら、Scuba の行動データを使用して Braze でユーザーセグメントを作成できます。

### ステップ1:新しいSegmentの作成

Braze で、**Audience** > **Segments** に移動し、**Segmentの作成** を選択して、Segmentの名前を入力します。

![Braze での新しいSegmentの作成。]({% image_buster /assets/img/scuba/analytics/segment_name.png %})

### ステップ2:Scuba 属性を探して選択する

**Segment Details** > **Filters**で、**Custom Attributes**を選択します。

![[セグメントの詳細] での「カスタム属性」フィルターの選択。]({% image_buster /assets/img/scuba/analytics/filter_attribute.png %})

**検索カスタム属性s**を選択し、前回のPOSTリクエストで使用したアクタープロパティの名前を選択します。

![アクタープロパティをカスタム属性として選択します。]({% image_buster /assets/img/scuba/analytics/select_property.png %})

### ステップ 3:属性の設定

アクタープロパティ名の横で、演算子と値を選択します (該当する場合)。これらの値は、Scuba で定義したアクタープロパティによって決定されます。完了したら、[**保存**] を選択します。

![選択されているプロパティ名に対する演算子と値の選択。]({% image_buster /assets/img/scuba/analytics/operator_end.png %})


