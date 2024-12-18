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

> このエンドポイントを使用して、未確認の（エイリアスのみの）ユーザーを識別します。 

{% alert important %}
2023年8月7日から、このエンドポイントはすべての呼び出しのデータをマージします。これは、[`merge_behavior`](#merge)がすべての呼び出しに対して`merge`に設定されることを意味します。
{% endalert %}

`/users/identify` を呼び出すと、エイリアスのみのプロファイルと識別されたプロファイルが結合され、エイリアスのみのプロファイルが削除されます。

ユーザーを識別するには、`external_id`を`aliases_to_identify`オブジェクトに含める必要があります。その`external_id`を持つユーザーがいない場合、`external_id`はエイリアスされたユーザーの記録に追加され、ユーザーは識別されたと見なされます。リクエストごとに最大50個のユーザーエイリアスを追加できます。

その後、複数の追加ユーザーエイリアスを単一の`external_id`に関連付けることができます。 
- これらの後続の関連付けが`merge_behavior`フィールドを`none`に設定して行われると、ユーザーエイリアスに関連付けられたプッシュトークンとメッセージ履歴のみが保持されます。属性、イベント、または購入は「孤立」し、識別されたユーザーには利用できません。1つの回避策は、識別前にエイリアスされたユーザーのデータを[`/users/export/ids`エンドポイント]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)を使用してエクスポートし、識別されたユーザーに属性、イベント、および購入を再関連付けることです。
- `merge_behavior` フィールドを `merge` に設定して関連付けを行うと、このエンドポイントは匿名ユーザーで見つかった[特定のフィールド](#merge)を識別されたユーザーにマージします。

{% alert tip %}
ユーザーを識別する際にデータの予期しない損失を防ぐために、まず[データ収集のベストプラクティス]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/best_practices/#capturing-user-data-when-alias-only-user-info-is-already-present)を参照して、エイリアスのみのユーザー情報が既に存在する場合のユーザーデータのキャプチャについて学ぶことを強くお勧めします。
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5f74e0f7-0620-4c7b-b0a2-f5f38fdbff58 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/api_key/)と`users.identify`の権限が必要です。

## レート制限 
2021年9月16日以降に Braze にオンボーディングしたお客様については、このエンドポイントに対して行う要求にレート制限が適用されます。詳細については、[APIの制限]({{site.baseurl}}/api/basics/#api-limits)を参照してください。

## 要求本文:

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
   "aliases_to_identify" : (required, array of alias to identify objects), 
   "merge_behavior": (optional, string) one of 'none' or 'merge' is expected
}
```

### リクエストパラメーター

| パラメータ             | 必須 | データ型                           | 説明                                                                                                                                                                 |
| --------------------- | -------- | ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `aliases_to_identify` | 必須 | オブジェクトを識別するためのエイリアスの配列 | [エイリアスを参照してオブジェクトを識別する]({{site.baseurl}}/api/objects_filters/aliases_to_identify/)および[ユーザーエイリアスオブジェクト]({{site.baseurl}}/api/objects_filters/user_alias_object/)を参照してください。 |
| `merge_behavior`      | オプション | 文字列                              | `merge` か のどちらかが予想される。                                                                                                                                       |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

#### Merge_behavior フィールド {#merge}

`merge_behavior`フィールドを`merge`に設定すると、エンドポイントは匿名ユーザーに見つかった以下のフィールドのいずれかを特定のユーザーに**排他的に**マージするように設定されます。 
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
- Y日間にX回」のセグメンテーション（X<=50、Y<=30）のためのカスタムイベントと購入イベントのプロパティ。
- セグメント可能なカスタム・イベントのサマリー
  - イベント数（両プロファイルの合計）
  - イベントが最初に発生した日（Brazeは2つの日付のうち早い方を選ぶ）
  - イベントが最後に発生した日（Brazeは2つの日付のうち遅い方を選ぶ）
- アプリ内購入の合計（セント単位）（両方のプロファイルの合計)
- 購入総数 (両方のプロファイルの合計)
- 初回購入日 (Braze は2つの日付のうち早い方を選択します)
- 最終購入日 (Braze は2つの日付のうち遅い方を選択します)
- アプリの概要
- Last_X_atフィールド（Brazeは、孤児となったプロファイルフィールドがより新しいものであれば、フィールドを更新する）
- キャンペーンの概要（Brazeは最新の日付フィールドを選択します）
- ワークフローのサマリー（Brazeは最新の日付フィールドを選ぶ）
- メッセージとメッセージのエンゲージメント履歴

匿名ユーザーから識別されたユーザーに対して検出された次のいずれかのフィールド。
- カスタムイベントと購入イベントのカウントと最初の日付と最後の日付のタイムスタンプ 
  - これらの統合されたフィールドは、「Y日以内にXイベント」フィルターを更新する。購入イベントの場合、これらのフィルターには、「Y日間の購入回数」と「過去Y日間の使用金額」が含まれる。

セッションデータは、両方のユーザープロファイルにアプリが存在する場合にのみマージされる。たとえば、ターゲットユーザーには「ABCApp」のアプリ概要がなく、元のユーザーにはある場合、ターゲットユーザーのプロファイルにはマージ後に「ABCApp」のアプリ概要が表示されます。 

フィールドを`none`に設定しても、ユーザーデータは識別されたユーザープロファイルにマージされません。

### メールによるユーザーの識別
識別子として`email` が指定された場合、識別子にはさらに`prioritization` の値が必要となる。`prioritization` は、複数のユーザーが見つかった場合に、どのユーザーをマージするかを指定する配列でなければならない。`prioritization` は順序付き配列である。つまり、優先順位付けから複数のユーザーがマッチした場合、マージは行われない。

配列に使用できる値は、`identified`、`unidentified`、`most_recently_updated` です。`most_recently_updated` は、最も最近更新されたユーザーを優先することを意味します。

優先配列には、一度に以下のオプションのうち1つしか存在できません。
- `identified` を持つユーザーを優先することである。 `external_id`
- `unidentified` のないユーザーを優先することである。 `external_id`

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
  "merge_behavior": "merge"
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
