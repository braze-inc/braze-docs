---
nav_title: "POST:ユーザーを識別する"
article_title: "POST:ユーザーを識別する"
search_tag: エンドポイント
page_order: 3
layout: api_page
page_type: reference
alias: /users_identify_merge/
description: "この記事では、「ユーザーの識別」Braze エンドポイントの詳細について説明します。"

---
{% api %}
# ユーザーを識別する
{% apimethod post %}
/users/identify
{% endapimethod %}

> このエンドポイントを使用して、指定された external ID を使用して未識別（エイリアスのみ、メールのみ、または電話番号のみ）のユーザーを識別します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5f74e0f7-0620-4c7b-b0a2-f5f38fdbff58 {% endapiref %}

## 仕組み

`/users/identify` を呼び出すと、エイリアス（エイリアスのみのプロファイル）、メールアドレス（メールのみのプロファイル）、または電話番号（電話番号のみのプロファイル）で識別されるユーザープロファイルと、`external_id` を持つユーザープロファイル（識別済みプロファイル）が結合され、エイリアスのみのプロファイルが削除されます。

ユーザーを識別するには、以下のオブジェクトに `external_id` を含める必要があります。

- `aliases_to_identify`
- `emails_to_identify`
- `phone_numbers_to_identify`

その `external_id` を持つユーザーが存在しない場合、`external_id` はエイリアスユーザーのレコードに追加され、ユーザーは識別済みとみなされます。ユーザーは特定のラベルに対して1つのエイリアスしか持つことができません。`external_id` を持つユーザーが既に存在し、かつエイリアスのみのプロファイルと同じラベルを持つ既存のエイリアスがある場合、ユーザープロファイルは結合されません。

{% alert tip %}
ユーザーを識別する際にデータの予期しない損失を防ぐために、まず[データ収集のベストプラクティス]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/best_practices/#capturing-user-data-when-alias-only-user-info-is-already-present)を参照して、エイリアスのみのユーザー情報が既に存在する場合のユーザーデータのキャプチャについて学ぶことを強くお勧めします。
{% endalert %}

### マージ動作

デフォルトでは、このエンドポイントは匿名ユーザーに**のみ**存在する以下のフィールドリストを、識別済みユーザーにマージします。

{% details マージされるフィールドのリスト %}
- 名
- 姓
- メール
- 性別
- 生年月日
- 電話番号
- タイムゾーン
- 市区町村
- 国
- 言語
- セッション数（両方のプロファイルのセッションの合計）
- 初回セッションの日付（Braze は2つの日付のうち早い方を選択します）
- 最終セッションの日付（Braze は2つの日付のうち遅い方を選択します）
- カスタム属性
- カスタムイベントと購入イベントのデータ
- 「Y日間でX回」セグメンテーション用のカスタムイベントおよび購入イベントのプロパティ（X<=50 および Y<=30）
- セグメント可能なカスタムイベントのサマリー
  - イベント数（両方のプロファイルの合計）
  - イベントが最初に発生した日時（Braze は2つの日付のうち早い方を選択します）
  - イベントが最後に発生した日時（Braze は2つの日付のうち遅い方を選択します）
- アプリ内購入の合計（セント単位）（両方のプロファイルの合計）
- 購入総数（両方のプロファイルの合計）
- 初回購入日（Braze は2つの日付のうち早い方を選択します）
- 最終購入日（Braze は2つの日付のうち遅い方を選択します）
- アプリの概要
- Last_X_at フィールド（孤立したプロファイルのフィールドがより新しい場合、Braze はフィールドを更新します）
- キャンペーンの概要（Braze は最も新しい日付フィールドを選択します）
- ワークフローの概要（Braze は最も新しい日付フィールドを選択します）
- メッセージとメッセージのエンゲージメント履歴
- カスタムイベントと購入イベントのカウント、および最初の日付と最後の日付のタイムスタンプ
  - これらのマージされたフィールドは「Y日間でXイベント」フィルターを更新します。購入イベントの場合、これらのフィルターには「Y日間の購入回数」と「過去Y日間の使用金額」が含まれます。
- 両方のユーザープロファイルにアプリが存在する場合のセッションデータ
  - 例えば、ターゲットユーザーが「ABCApp」のアプリ概要を持っていないが、元のユーザーが持っている場合、マージ後にターゲットユーザーのプロファイルには「ABCApp」のアプリ概要が表示されます。
{% enddetails %}

## 前提条件

このエンドポイントを使用するには、`users.identify` 権限を持つ [API キー]({{site.baseurl}}/api/api_key/)が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='users identify' %}

## リクエスト本文

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
   "aliases_to_identify" : (required, array of alias to identify objects),
   "emails_to_identify": (optional, array of alias to identify objects) User emails to identify,
   "phone_numbers_to_identify": (optional, array of alias to identify objects) User phone numbers to identify,
},
```

### リクエストパラメーター

リクエストごとに最大50個のユーザーエイリアスを追加できます。複数の追加ユーザーエイリアスを単一の `external_id` に関連付けることができます。

{% alert important %}
リクエストごとに `aliases_to_identify`、`emails_to_identify`、または `phone_numbers_to_identify` のいずれかが必要です。例えば、リクエストで `emails_to_identify` を使用することで、このエンドポイントを使ってメールによるユーザーの識別ができます。
{% endalert %}

| パラメーター                   | 必須 | データタイプ                           | 説明                                                                                                                                                                 |
|-----------------------------|----------|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `aliases_to_identify`       | 必須 | 識別するエイリアスオブジェクトの配列 | [識別するエイリアスオブジェクト]({{site.baseurl}}/api/objects_filters/aliases_to_identify/)および[ユーザーエイリアスオブジェクト]({{site.baseurl}}/api/objects_filters/user_alias_object/)を参照してください。 |
| `emails_to_identify`        | 必須 | 識別するエイリアスオブジェクトの配列 | 識別子として `email` が指定されている場合は必須です。ユーザーを識別するためのメールアドレス。[メールによるユーザーの識別](#identifying-users-by-email)を参照してください。                                                                                                              |
| `phone_numbers_to_identify` | 必須 | 識別するエイリアスオブジェクトの配列 | ユーザーを識別するための電話番号。                                                                                                                                            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### メールアドレスと電話番号によるユーザーの識別

メールアドレスや電話番号を識別子として指定する場合は、識別子に `prioritization` も含める必要があります。

`prioritization` は、複数のユーザーが見つかった場合にマージするユーザーを指定する配列でなければなりません。`prioritization` は順序付き配列であり、優先順位付けから複数のユーザーが一致した場合、マージは行われません。

配列に指定できる値は次のとおりです。

- `identified`
- `unidentified`
- `most_recently_updated`（最近更新されたユーザーを優先することを意味します）
- `least_recently_updated`（最も更新が古いユーザーを優先することを意味します）

優先順位配列には、一度に以下のオプションのうち1つしか存在できません。

- `identified` は `external_id` を持つユーザーを優先することを意味します
- `unidentified` は `external_id` を持たないユーザーを優先することを意味します

{% alert note %}
メールアドレスまたは電話番号が複数のユーザーに一致する場合、マージは行われません。これには、一致したユーザーの1人がリクエストで指定された `external_id` と同じ `external_id` を持つケースも含まれます。この場合、エンドポイントは `"message": "success"` を返しますが、ユーザープロファイルは結合されません。これを回避するには、このエンドポイントを呼び出す前に、メールアドレスまたは電話番号が未識別のユーザーにのみ関連付けられていることを確認してください。
{% endalert %}

## リクエスト例

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/identify' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "aliases_to_identify": [
    {
      "external_id": "external_identifier",
      "user_alias": {
          "alias_name": "example_alias",
          "alias_label": "example_label"
      }
    }
  ],
  "emails_to_identify": [
    {
      "external_id": "external_identifier_2",
      "email": "john.smith@braze.com",
      "prioritization": ["unidentified", "most_recently_updated"]
    }
  ]
}'
```

### 大文字と小文字の区別

`alias_name` フィールドは大文字と小文字を区別します。`201` ステータスコードを返すリクエストは、リクエストの構文が有効であることのみを確認するものであり、エイリアスが一致したことを確認するものではありません。リクエスト内の `alias_name` の大文字と小文字がユーザープロファイルに保存されているエイリアスと正確に一致しない場合、操作はサイレントに失敗し、`external_id` は割り当てられません。例えば、保存されているエイリアスが `JimJones@example.com` の場合、`jimjones@example.com` でリクエストすると成功を返しますが、結果は生成されません。

{% alert tip %}
`alias_name` および `alias_label` の詳細については、[ユーザーエイリアス]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)のドキュメントをご覧ください。
{% endalert %}

## 応答

```json
{
    "aliases_processed": 1,
    "message": "success"
}
```

{% endapi %}