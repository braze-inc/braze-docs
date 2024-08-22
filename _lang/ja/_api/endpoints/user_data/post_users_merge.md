---
nav_title: "POST:ユーザーをマージする"
article_title: "POST:ユーザーをマージする"
search_tag: Endpoint
page_order: 6
layout: api_page
page_type: reference
description: "この記事では、「ユーザーのマージ」Braze エンドポイントの詳細について説明します。"

---
{% api %}
# ユーザーをマージする
{% apimethod post %}
/users/merge
{% endapimethod %}

> このエンドポイントを使用して、あるユーザーを別のユーザーにマージする。 

マージはリクエストごとに50個まで指定できます。このエンドポイントは非同期である。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d262b86d-cf84-46e2-b9d0-f882bb7078de {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`users.merge` 権限を持つ [API キー]({{site.baseurl}}/api/api_key/)が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='users merge' %}

## Request body

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "merge_updates" : (required, array of objects)
}
```

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
|---|---|---|---|
| `merge_updates` | required | 配列 | オブジェクトの配列。各オブジェクトには `identifier_to_merge` オブジェクトと `identifier_to_keep` オブジェクトが含まれている必要があり、それぞれが `external_id`、`user_alias`、`phone_number`、または `email` のいずれかでユーザーを参照する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

### マージ動作

以下に説明する動作は、Snowflakeを使用して*いない*Brazeの全機能に当てはまる。**メッセージング履歴]**タブ、\[セグメント拡張]、\[クエリビルダー]、および\[カレント]では、ユーザーのマージが反映されない。

{% alert important %}
エンドポイントは、`merge_updates` オブジェクトが更新される順序を保証しない。
{% endalert %}

このエンドポイントは、以下のフィールドがターゲット・ユーザーに見つからない場合、それらをマージする：

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
- デバイス情報
- セッション数 （両方のプロファイルのセッションの合計）
- 初回セッションの日付 (Braze は2つの日付のうち早い方を選択します)
- 最終セッションの日付 (Braze は2つの日付のうち遅い方の日付を選択します)
- カスタム属性（ターゲットプロファイル上の既存のカスタム属性は保持され、ターゲットプロファイル上に存在しなかったカスタム属性も含まれる）
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
- キャンペーンのインタラクションデータ（Brazeは最新の日付フィールドを選ぶ）
- ワークフローのサマリー（Brazeは最新の日付フィールドを選ぶ）
- メッセージとメッセージのエンゲージメント履歴

セッションデータは、両方のユーザープロファイルにアプリが存在する場合にのみマージされる。

{% alert note %}
ユーザーをマージする場合、`/users/merge` エンドポイントを使用すると、[`changeUser()` メソッドを](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser)使用した場合と同じように機能します。
{% endalert %}

#### カスタムイベント日と購入イベント日の動作

これらの統合されたフィールドは、「Y日以内にXイベント」フィルターを更新する。購入イベントの場合、これらのフィルターには、「Y日間の購入回数」と「過去Y日間の使用金額」が含まれる。

### 電子メールまたは電話番号でユーザーをマージする

識別子として `email` または `phone_number` が指定された場合、識別子にはさらに `prioritization` の値が必要になります。`prioritization` は、複数のユーザーが見つかった場合に、どのユーザーをマージするかを指定する配列でなければならない。`prioritization` は順序付き配列である。つまり、優先順位付けから複数のユーザーがマッチした場合、マージは行われない。

配列に使用できる値は、`identified`、`unidentified`、`most_recently_updated` です。`most_recently_updated` は、最も最近更新されたユーザーを優先することを意味します。

優先配列には、一度に以下のオプションのうち1つしか存在できません。
- `identified` を持つユーザーを優先することである。 `external_id`
- `unidentified` のないユーザーを優先することである。 `external_id`

## リクエスト例

### 基本リクエスト

これはリクエストのパターンを示す基本的なリクエストボディである。

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "external_id": "old-user1"
      },
      "identifier_to_keep": {
        "external_id": "current-user1"
      }
    },
    {
      "identifier_to_merge": {
        "email": "user1@braze.com",
        "prioritization": ["unidentified", "most_recently_updated"]
      },
      "identifier_to_keep":  {
        "email": "user2@braze.com",
        "prioritization": ["identified", "most_recently_updated"]
      }
    },
    {
      "identifier_to_merge": {
        "user_alias": {
          "alias_name": "old-user2@example.com",
          "alias_label": "email"
        }
      },
      "identifier_to_keep": {
        "user_alias": {
          "alias_name": "current-user2@example.com",
          "alias_label": "email"
        }
      }
    }
  ]
}'
```

### 未確認ユーザーをマージする

以下のリクエストは、電子メールアドレス "john.smith@braze.com" を持つ、直近に更新された未確認ユーザーを、`external_id` "john "を持つユーザーにマージします。`most_recently_updated` を使用して、クエリを1人のみの未確認ユーザーに絞り込みます。そのため、このメールアドレスを持つ未確認のユーザーが2人いた場合、`external_id` "john "のユーザーにマージされるのは1人だけである。

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "email": "john.smith@braze.com",
        "prioritization": ["unidentified", "most_recently_updated"]
      },
      "identifier_to_keep": {
        "external_id": "john"
      }
    }
  ]
}'
```

### 未確認ユーザーを識別されたユーザーにマージする

この次の例は、電子メールアドレス "john.smith@braze.com" を持つ、最も最近更新された未確認ユーザーを、電子メールアドレス "john.smith@braze.com" を持つ、最も最近更新された識別されたユーザーにマージします。`most_recently_updated` を使用して、クエリを1人のみのユーザーに絞り込みます (`identifier_to_merge` の場合は未確認ユーザー1人、`identifier_to_keep` の場合は識別されたユーザー1人）。

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "email": "john.smith@braze.com",
        "prioritization": ["unidentified", "most_recently_updated"]
      },
      "identifier_to_keep": {
        "email": "john.smith@braze.com",
        "prioritization": ["identified", "most_recently_updated"]
      }
    }
  ]
}'
```

### most_recently_updated の優先順位付けを含めずに、未確認ユーザーをマージする

メールアドレス"john.smith@braze.com"を持つ正体不明のユーザーが2人いる場合、このリクエスト例では、そのメールアドレスを持つ正体不明のユーザーが2人いるため、どのユーザーもマージしない。このリクエストは、メールアドレス"john.smith@braze.com"を持つ未確認ユーザーが1人しかいない場合にのみ機能する。

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "email": "john.smith@braze.com",
        "prioritization": ["unidentified"]
      },
      "identifier_to_keep": {
        "external_id": "john"
      }
    }
  ]
}'
```

## 応答

このエンドポイントには、`202` と `400` の2つのステータスコード応答があります。

### 成功応答の例

ステータスコード `202` は、次の応答本文を返す可能性があります。

```json
{
  "message": "success"
}
```

### エラー応答例

ステータスコード `400` は、次の応答本文を返す可能性があります。遭遇する可能性のあるエラーの詳細については、「[トラブルシューティング](#troubleshooting)」を参照のこと。

```json
{
  "message": "'merge_updates' must be an array of objects"
}
```

## トラブルシューティング

以下の表は、起こりうるエラーメッセージの一覧である。

| エラー | トラブルシューティング |
| --- |
| `'merge_updates' must be an array of objects` | `merge_updates` がオブジェクトの配列であることを確認する。 |
| `a single request may not contain more than 50 merge updates` | 1回のリクエストで指定できるマージ更新は50件までです。 |
| `identifiers must be objects with an 'external_id' property that is a string, 'user_alias' property that is an object, or 'email' property that is a string` | リクエストの識別子をチェックする。 |
| `'merge_updates' must only have 'identifier_to_merge' and 'identifier_to_keep'` | `merge_updates` に `identifier_to_merge` と `identifier_to_keep` という2つのオブジェクトしか含まれていないことを確認します。 |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}
