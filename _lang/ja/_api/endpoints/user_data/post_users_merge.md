---
nav_title: "POST:ユーザーをマージする"
article_title: "POST:ユーザーをマージする"
search_tag: エンドポイント
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

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/api_key/)と`users.merge`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='users merge' %}

## 要求本文:

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

| パラメーター | 必須かどうか | データ型 | 説明 |
|---|---|---|---|
| `merge_updates` | 必須かどうか | 配列 | オブジェクトの配列。各オブジェクトには `identifier_to_merge` オブジェクトと `identifier_to_keep` オブジェクトが含まれている必要があり、それぞれが `external_id`、`user_alias`、`phone`、または `email` のいずれかでユーザーを参照する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### マージ動作

以下に説明する動作は、Snowflakeを使用して**いない**Brazeの全機能に当てはまる。**メッセージング履歴]**タブ、[セグメント拡張]、[クエリビルダー]、および[カレント]では、ユーザーのマージが反映されない。

{% alert important %}
エンドポイントは、`merge_updates` オブジェクトが更新される順序を保証しない。
{% endalert %}

このエンドポイントは、対象ユーザーに以下のフィールドが存在しない場合、それらをマージする。

- 名
- 姓
- メール（[暗号化]({{site.baseurl}}/user_guide/data/field_level_encryption/)されていない場合）
- 性別
- 生年月日
- 電話番号
- タイムゾーン
- 市区町村
- 国
- 言語
- デバイス情報
- セッション数 （両方のプロファイルのセッションの合計）
- 初回セッションの日付（Brazeは二つの日付のうち早い方を選ぶ）
- 最終セッションの日付（Brazeは2つの日付のうち遅い方を選択する）
- カスタム属性（Brazeはターゲットプロファイル上の既存のカスタム属性を保持し、ターゲットプロファイルに存在しなかったカスタム属性も追加する）
- カスタム・イベントと購入イベントのデータ
- 「X回をY日間で」セグメンテーション用のカスタムイベントおよび購入イベントのプロパティ（ここでX<=50  および Y<=30)
- セグメント可能なカスタム・イベントのサマリー
  - イベント数（両プロファイルの合計）
  - イベントが最初に発生した日時（Brazeは二つの日付のうち早い方を選択する）
  - イベントが最後に発生した日時（Brazeは二つの日付のうち遅い方を選択する）
- アプリ内購入の合計（セント単位）（両方のプロファイルの合計)
- 購入総数 (両方のプロファイルの合計)
- 初回購入日（Brazeは二つの日付のうち早い方を選択する）
- 最終購入日（Brazeは二つの日付のうち遅い方を選択する）
- アプリの概要
- Last_X_at フィールド（孤立したプロファイルのフィールドがより新しい場合、Brazeはフィールドを更新する）
- キャンペーンのインタラクションデータ（Brazeは最も新しい日付フィールドを選択する）
- ワークフローの概要（Brazeは最新の日付フィールドを選択する）
- メッセージとメッセージのエンゲージメント履歴
- Brazeは、アプリが両方のユーザープロファイルに存在する場合にのみセッションデータを統合する。

{% alert note %}
ユーザーをマージする場合、`/users/merge` エンドポイントを使用すると、[`changeUser()` メソッドを](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser)使用した場合と同じように機能します。
{% endalert %}

#### カスタムイベント日と購入イベント日の動作

これらの結合フィールドは「X件のイベントがY日間で発生」というフィルターを更新する。購入イベントの場合、これらのフィルターには、「Y日間の購入回数」と「過去Y日間の使用金額」が含まれる。

### 電子メールまたは電話番号でユーザーをマージする

識別子として  または`phone`  `email`が指定された場合、識別子に追加の`prioritization`  値を含めなければならない。複数のユーザーが見つかった場合に、どのユーザーをマージするかを指定する順序付き配列`prioritization`であるべきだ。つまり、優先順位付けから複数のユーザーが一致した場合、マージは行われない。

配列に指定できる値は次のとおりです。

- `identified`
- `unidentified`
- `most_recently_updated` (最近更新されたユーザーを優先することを意味します）
- `least_recently_updated` (最も最近更新されていないユーザーを優先することを意味します）

優先配列には、一度に以下のオプションのうち1つしか存在できません。

- `identified` を持つユーザーを優先することである。 `external_id`
- `unidentified` のないユーザーを優先することである。 `external_id`

## 例のリクエスト

### 基本リクエスト

これはリクエストのパターンを示す基本的なリクエストボディである。

```bash
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

以下のリクエストは、メールアドレスを持つ最新の更新された未識別ユーザーを、`john.smith@braze.com`external IDを持つ`john`ユーザーに統合する。この例では、フィルター`most_recently_updated`を使用することでクエリを未識別ユーザー1件に絞り込む。つまり、このメールアドレスを持つ未識別ユーザーが二人いた場合、external IDを持つユーザーにマージ`john`されるのは一人だけだ。

```bash
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

次の例では、メールアドレスを持つ最新の未識別ユーザーを、メールアドレス`john.smith@braze.com`を持つ最新の識別済み`john.smith@braze.com`ユーザーに統合する。

フィルター`most_recently_updated`を使用して、クエリを1人のユーザーに絞り込む（1人は未特定ユーザー、`identifier_to_merge`もう1人は識別子を持つユーザーである`identifier_to_keep`）。

```bash
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

### 優先most_recently_updated順位付けを含めずに、未識別ユーザーをマージする

メールアドレスが同じ未識別ユーザーが`john.smith@braze.com`2人いる場合、このリクエスト例ではユーザーをマージしない。なぜなら、そのメールアドレスを持つ未識別ユーザーが2人存在するからだ。このリクエストは、メールアドレスが未識別ユーザーが1人だけ`john.smith@braze.com`の場合にのみ機能する。

```bash
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

このエンドポイントには2つのステータスコード応答があります: `202` と `400`。

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
| `identifiers must be objects with an 'external_id' property that is a string, 'user_alias' property that is an object, 'email' property that is a string, or 'phone' property that is a string` | リクエストの識別子をチェックする。 |
| `'merge_updates' must only have 'identifier_to_merge' and 'identifier_to_keep'` | `merge_updates` に `identifier_to_merge` と `identifier_to_keep` という2つのオブジェクトしか含まれていないことを確認します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
