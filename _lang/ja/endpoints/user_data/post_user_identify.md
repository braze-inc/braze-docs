---
nav_title: "POST:ユーザーを識別する"
article_title: "POST:ユーザーを識別する"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
alias: /users_identify_merge/
description: "この記事では、「ユーザーの特定」Braze エンドポイントの詳細について説明します。"

---
{% api %}
# ユーザーを識別する
{% apimethod post %}
/users/identify
{% endapimethod %}

> このエンドポイントを使用して、指定された外部 ID を使用して識別されていない (エイリアスのみ、メールのみ、または電話番号のみ) ユーザーを識別します。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5f74e0f7-0620-4c7b-b0a2-f5f38fdbff58 {% endapiref %}

## CDI の仕組み

`/users/identify` を呼び出すと、エイリアス (エイリアスのみのプロファイル)、メールアドレス (メールのみのプロファイル)、または電話番号 (電話番号のみのプロファイル) によって識別されるユーザープロファイルと、`external_id` (識別されたプロファイル) を持つユーザープロファイルが結合され、エイリアスのみのプロファイルが削除されます。 

ユーザーを識別するには、`external_id` を以下のオブジェクトに含める必要があります。

- `aliases_to_identify`
- `emails_to_identify` 
- `phone_numbers_to_identify`

その`external_id` を持つユーザーが存在しない場合、`external_id` がエイリアスされたユーザーの記録に追加され、そのユーザーは識別されたとみなされる。ユーザーは、特定のラベルに対して 1 つのエイリアスしか持つことができません。`external_id` を持つユーザーがすでに存在し、エイリアスのみのプロファイルと同じラベルを持つ既存のエイリアスがある場合、ユーザープロファイルは結合されません。

{% alert tip %}
ユーザーを識別する際にデータの予期しない損失を防ぐために、まず[データ収集のベストプラクティス]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/best_practices/#capturing-user-data-when-alias-only-user-info-is-already-present)を参照して、エイリアスのみのユーザー情報が既に存在する場合のユーザーデータのキャプチャについて学ぶことを強くお勧めします。
{% endalert %}

### マージ動作

デフォルトでは、このエンドポイントは、匿名ユーザーに**のみ存在する以下のフィールドが識別されたユーザーに統合されます。

{% details List of fields that are merged %}
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
- セッション数 （両方のプロファイルのセッションの合計）
- 初回セッションの日付 (Braze は2つの日付のうち早い方を選択します)
- 最終セッションの日付 (Braze は2つの日付のうち遅い方の日付を選択します)
- カスタム属性
- カスタム・イベントと購入イベントのデータ
- &quot のカスタムイベントおよび購入イベントプロパティ;Y 日数とクォートのX 回; セグメンテーション (ここでX<=50) および Y<=30)
- セグメント可能なカスタム・イベントのサマリー
  - イベント数（両プロファイルの合計）
  - イベントが最初に発生した日（Brazeは2つの日付のうち早い方を選ぶ）
  - イベントが最後に発生した日（Brazeは2つの日付のうち遅い方を選ぶ）
- アプリ内購入の合計（セント単位）（両方のプロファイルの合計)
- 購入総数 (両方のプロファイルの合計)
- 初回購入日 (Braze は2つの日付のうち早い方を選択します)
- 最終購入日 (Braze は2つの日付のうち遅い方を選択します)
- アプリの概要
- Last_X_at フィールド s (Braze はフィールドs を更新します。孤立したプロファイル フィールドs がより新しい場合)
- キャンペーンの概要（Brazeは最新の日付フィールドを選択します）
- ワークフローのサマリー（Brazeは最新の日付フィールドを選ぶ）
- メッセージとメッセージのエンゲージメント履歴
- カスタムイベントと購入イベントのカウントと最初の日付と最後の日付のタイムスタンプ 
  - これらの統合されたフィールドは、「Y日以内にXイベント」フィルターを更新する。購入イベントの場合、これらのフィルターには、「Y日間の購入回数」と「過去Y日間の使用金額」が含まれる。
- 両方のユーザープロファイルにアプリが存在する場合のセッションデータ
  - たとえば、ターゲットユーザーには「ABCApp」のアプリ概要がなく、元のユーザーにはある場合、ターゲットユーザーのプロファイルにはマージ後に「ABCApp」のアプリ概要が表示されます。
{% enddetails %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/api_key/)と`users.identify`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='users identify' %}

## 要求本文:

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

リクエストごとに最大50個のユーザーエイリアスを追加できます。複数の追加ユーザーエイリアスを単一の`external_id`に関連付けることができます。

{% alert important %}
リクエストごとに `aliases_to_identify`、`emails_to_identify`、または`phone_numbers_to_identify` のいずれかが必要です。例えば、`emails_to_identify` をリクエストに使うことで、このエンドポイントを使ってメールによってユーザーを識別することができます。
{% endalert %}

| パラメーター                   | required | データ型                           | 説明                                                                                                                                                                 |
|-----------------------------|----------|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `aliases_to_identify`       | 必須 | オブジェクトを識別するためのエイリアスの配列 | [エイリアスを参照してオブジェクトを識別する]({{site.baseurl}}/api/objects_filters/aliases_to_identify/)および[ユーザーエイリアスオブジェクト]({{site.baseurl}}/api/objects_filters/user_alias_object/)を参照してください。 |
| `emails_to_identify`        | 必須 | オブジェクトを識別するためのエイリアスの配列 | 識別子として `email` が指定されている場合は必須。ユーザーを識別するためのメールアドレス。[メールによるユーザーの識別](#identifying-users-by-email)を参照してください。                                                                                                              |
| `phone_numbers_to_identify` | 必須 | オブジェクトを識別するためのエイリアスの配列 | ユーザーを識別するための電話番号。                                                                                                                                            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### メールアドレスと電話番号によるユーザーの識別

メールアドレスや電話番号を識別子として指定する場合は、`prioritization` も識別子に含める必要があります。

`prioritization` は、複数のユーザーが見つかった場合に、どのユーザーをマージするかを指定する配列でなければなりません。`prioritization` は順序付き配列です。つまり、優先順位付けから複数のユーザーがマッチした場合、マージは行われません。

配列に指定できる値は以下の通りです。

- `identified`
- `unidentified`
- `most_recently_updated` (最近更新されたユーザーを優先することを意味します）
- `least_recently_updated` (最も最近更新されていないユーザーを優先することを意味します）

優先配列には、一度に以下のオプションのうち1つしか存在できません。

- `identified` を持つユーザーを優先することである。 `external_id`
- `unidentified` のないユーザーを優先することである。 `external_id`

配列に`identified` を指定した場合、ユーザーはキャンバスに入力するために `external_id` を持っている**必要がある**ことを意味します。メールアドレスを持つユーザーに、識別子の有無にかかわらずメッセージを入力させたい場合は、代わりに`most_recently_updated` または`least_recently_updated` パラメータのみを使用する。

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

{% alert tip %}
詳細については、`alias_name`および`alias_label`、[ユーザーエイリアス]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)ドキュメントをご覧ください。
{% endalert %}

## 応答

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
    "aliases_processed": 1,
    "message": "success"
}
```

{% endapi %}
