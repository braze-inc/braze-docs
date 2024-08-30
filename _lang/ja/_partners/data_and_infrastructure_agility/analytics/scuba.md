---
nav_title: スクーバ
article_title: Scuba Analytics
description: "このスキューバおよびBrazeテクニカルリファレンスでは、Brazeセグメントを使用してスキューバのリアルタイムデータインサイトを有効にする方法について説明します。"
alias: /partners/scuba/
page_type: partner
search_tag: Partner
---

# Scuba Analytics

>[Scuba Analytics][1] は、高速時系列データ用に設計された、機械学習能力のあるフルスタックのデータ連携プラットフォームです。スクーバでは、ユーザーs(アクターとも呼ばれます)を選択的にエクスポートし、Braze プラットフォームに読み込むできます。Scuba では、カスタムアクタープロパティを使用して動作トレンドを分析し、さまざまなプラットフォーム間でデータを有効化し、マシンラーニングを使用して予測モデリングを実行します。

## 前提条件

Braze でScuba Analytics を使用するには、以下が必要です。

- `users.track` 権限を持つ[Braze REST API キー]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/#rest-api-keys)。
- `https://{scuba_hostname}/api/create_token` エンドポイントから取得できるScuba API トークン。

## Brazeへのスキューバデータの読み込むアップ

{% alert important %}
以下の要求はcurl を使用します。API リクエストの管理を向上させるには、Postman などのAPI クライアントを使用することをお勧めします。
{% endalert %}

Braze にScuba データをアップロードするには、`https://scuba.pliant.io/a/scuba-connectors/prod/braze-activation` に対して`application/json` content-type を使用してPOST リクエストを行います。

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
| `BRAZE_API_ENDPOINT`    | カレントBrazeインスタンスのBraze REST エンドポイント URL。詳細については、[休止API キーs]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/#rest-api-keys)を参照してください。 |
| `BRAZE_API_KEY`         | `users.track` 権限を持つBraze REST API キー。                                                                                                                                      |
| `HOSTNAME`              | 現在のScuba インスタンスのホスト名。                                                                                                                                                    |
| `SCUBA_API_TOKEN`       | スキューバAPI トークン。                                                                                                                                                                           |
| `TABLE_NAME`            | データセットが属するテーブル。詳細については、[用語集を参照してください。データセットテーブル][3]。                                                                                                      |
| `ACTOR_PROPERTY_NAME`   | データセットが属するアクタプロパティ。この名前に一致するデータのみが返されます。詳細については、[用語集を参照してください。アクタプロパティ][4]。                                             |
| `ACTOR_PROPERTY_FILTER` | アクタープロパティのオーディエンス検索フィルター。                                                                                                                                             |
| `ACTOR_ID`              | データセットが属するアクタプロパティのID。このID は、Braze の`external_id` に一致します。詳細については、[用語集を参照してください。アクタ][5]。                                              |
| `PERIOD_START`          | BQL 互換の日付としての開始期間。詳細については、[BQL構文および使用法][6]を参照してください。                                                                                                 |
| `PERIOD_END`            | BQL 互換の日付としての終了期間。詳細については、[BQL構文および使用法][6]を参照してください。                                                                                                   |
| `RECORD_LIMIT`          | **オプション**:返されるレコードの最大数。`scuba_record_limit` が省略された場合、Scuba は最大100 レコードを返します。これを変更するには、負でない数値を`scuba_record_limit` に割り当てます。    |
{: .reset-td-br-1 .reset-td-br-2}

### デフォルト動作

デフォルトでは、`update_existing_only` は`false` に設定されています。これにより、Braze内の既存のレコードが更新され、存在しないレコードの新規レコードが作成されます。Scuba が新しいレコードを作成しないようにするには、`update_existing_only` を`true` に設定します。

### レートリミット

スキューバアプリは、このエンドポイントに対して1分間にレート制限50,000件のリクエストが存在します。

## スキューバのビヘイビアーデータを使用したSegmentの作成

[ データ](#uploading-your-scuba-data-to-braze) をアップロードすると、Scuba のビヘイビアーデータを使用してBraze でユーザー Segmentを作成できます。

### ステップ1:新しいSegmentの作成

Braze で、**Audience** > **Segments** に移動し、**Segmentの作成** を選択して、Segmentの名前を入力します。

![Braze での新しいSegmentの作成。][501]

### ステップ2:スクーバ属性を探して選択する

**Segment Details** > **Filters**で、**Custom Attributes**を選択します。

![「セグメント詳細」で「カスタム属性」フィルターを選択します。][502]

**検索カスタム属性s**を選択し、前回のPOSTリクエストで使用したアクタープロパティの名前を選択します。

![アクタープロパティをカスタム属性として選択します。][503]

### ステップ3:属性の設定

アクタープロパティの名前の隣に、演算子と数値(アプリであればライセンス可能)を選択します。これらの値は、Scuba で定義したアクタープロパティによって決定されます。完了したら、\[**保存**] を選択します。

![選択した操作と値の選択 ][504]

[1]: https://scuba.io
[3]: https://docs.scuba.io/glossary/dataset-table
[4]: https://docs.scuba.io/glossary/actor-property
[5]: https://docs.scuba.io/glossary/actor
[6]: https://docs.scuba.io/guides/bql-syntax-and-usage
[501]: {% image_buster /assets/img/scuba/analytics/segment_name.png %}
[502]: {% image_buster /assets/img/scuba/analytics/filter_attribute.png %}
[503]: {% image_buster /assets/img/scuba/analytics/select_property.png %}
[504]: {% image_buster /assets/img/scuba/analytics/operator_end.png %}
