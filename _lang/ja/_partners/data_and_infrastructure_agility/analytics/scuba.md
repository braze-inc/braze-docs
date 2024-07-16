---
nav_title: Scuba
article_title:Scuba Analytics
description:"このScubaとBrazeのテクニカルリファレンスでは、Brazeセグメンテーションを使用してScubaのリアルタイムデータのインサイトを有効にする方法を説明している。"
alias: /partners/scuba/
page_type: partner
search_tag:Partner
---

# Scuba Analytics

>[Scuba Analyticsは][1]、高速時系列データ用に設計された、フルスタックの機械学習機能付きデータ連携プラットフォームである。Scubaでは、ユーザー（アクターとも呼ばれる）を選択的にエクスポートし、Brazeプラットフォームに読み込むことができる。Scubaでは、カスタムアクタープロパティを使用して行動傾向を分析し、さまざまなプラットフォームで顧客データを活性化し、機械学習を使用して予測モデリングを行う。

## 前提条件

BrazeでScuba Analyticsを使うには、以下のものが必要だ：

- `users.track` 権限を持つ[Braze REST API キー]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/#rest-api-keys)。
- `https://{scuba_hostname}/api/create_token` エンドポイントから取得できる Scuba API トークン。

## スキューバデータをBrazeにアップロードする

{% alert important %}
以下のリクエストはcurlを使用している。より良いAPIリクエスト管理のためには、PostmanのようなAPIクライアントの使用を推奨する。
{% endalert %}

ScubaデータをBrazeにアップロードするには、`application/json` content-typeを使用して`https://scuba.pliant.io/a/scuba-connectors/prod/braze-activation` ：

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
| `BRAZE_API_ENDPOINT`    | 現在のBrazeインスタンスのBraze RESTエンドポイントURL。詳細については、[REST APIキーを]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/#rest-api-keys)参照のこと。 |
| `BRAZE_API_KEY`         | `users.track` 権限を持つ Braze REST API キー。                                                                                                                                      |
| `HOSTNAME`              | 現在のScubaインスタンスのホスト名。                                                                                                                                                    |
| `SCUBA_API_TOKEN`       | あなたのScuba APIトークン。                                                                                                                                                                           |
| `TABLE_NAME`            | データセットが属するテーブル。詳しくは、[Glossary: データセットの][3]表を参照のこと。                                                                                                      |
| `ACTOR_PROPERTY_NAME`   | データセットが属するアクター・プロパティ。この名前に一致するデータのみが返される。詳しくは、[Glossary: Actorプロパティを][4]参照のこと。                                             |
| `ACTOR_PROPERTY_FILTER` | 俳優プロパティのオーディエンス検索フィルター。                                                                                                                                             |
| `ACTOR_ID`              | データセットが属するアクタープロパティのID。このIDはBrazeのあなたの`external_id` 。詳しくは、[Glossary: Actorを][5]参照のこと。                                              |
| `PERIOD_START`          | BQL互換の日付としての開始期間。詳細については、[BQLの構文と使用][6]法を参照のこと。                                                                                                 |
| `PERIOD_END`            | BQLと互換性のある日付でのエンドピリオド。詳細については、[BQLの構文と使用][6]法を参照のこと。                                                                                                   |
| `RECORD_LIMIT`          | **オプション**だ：返すレコードの最大数。`scuba_record_limit` が省略された場合、スキューバは最大100レコードを返す。これを変更するには、`scuba_record_limit` に任意の非負数を代入する。    |
{: .reset-td-br-1 .reset-td-br-2}

### デフォルト

デフォルトでは、`update_existing_only` が`false` に設定されており、Brazeの既存のレコードを更新するだけでなく、存在しないレコードの新規レコードも作成する。スキューバが新しいレコードを作成しないようにするには、`update_existing_only` を`true` に設定する。

### レート制限

Scubaはこのエンドポイントに対して、毎分50,000リクエストのレート制限を適用する。

## スクーバの行動データを使ってセグメンテーションを作成する

[データをアップロード](#uploading-your-scuba-data-to-braze)したら、BrazeでScubaの行動データを使ってユーザーセグメンテーションを作成できる。

### ステップ1:新しいセグメンテーションを作成する

Brazeで、「**オーディエンス**」>「**セグメンテーション**」と進み、「**セグメンテーションを作成**」を選択し、セグメンテーションの名前を入力する。

![Brazeで新しいセグメンテーションを作成する。][501]

### ステップ2:スキューバ属性を見つけて選択する。

**セグメンテーションの詳細**＞**フィルターで**、**カスタム属性を**選択する。

!['Segment Details' で'Custom Attribute' フィルターを選択する。][502]

**カスタム属性を検索**]を選択し、前回の POST リクエストで使用したアクター・プロパティ名を選択する。

![カスタム属性としてアクタープロパティを選択する。][503]

### ステップ3:属性を設定する

アクター・プロパティ名の横に、演算子と値（該当する場合）を選択する。これらの値は、've defined in Scuba. When you'終了したら、**Save** を選択するアクター・プロパティによって決定される。

![選択された操作と値を選択する ][504]

[1]: https://scuba.io
[3]: https://docs.scuba.io/glossary/dataset-table
[4]: https://docs.scuba.io/glossary/actor-property
[5]: https://docs.scuba.io/glossary/actor
[6]: https://docs.scuba.io/guides/bql-syntax-and-usage
[501]: {% image_buster /assets/img/scuba/analytics/segment_name.png %}
[502]: {% image_buster /assets/img/scuba/analytics/filter_attribute.png %}
[503]: {% image_buster /assets/img/scuba/analytics/select_property.png %}
[504]: {% image_buster /assets/img/scuba/analytics/operator_end.png %}
