---
nav_title: "ポスト:ユーザーを結合"
article_title: "ポスト:ユーザーを結合"
search_tag: Endpoint
page_order: 6
layout: api_page
page_type: reference
description: "この記事では、Merge ユーザーの Braze エンドポイントについて詳しく説明します。"

---
{% api %}
# ユーザーを結合
{% apimethod post %}
/users/merge
{% endapimethod %}

> このエンドポイントを使用して、あるユーザーを別のユーザーに統合します。 

1 つのリクエストで最大 50 のマージを指定できます。このエンドポイントは非同期です。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d262b86d-cf84-46e2-b9d0-f882bb7078de {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`users.merge`権限のある [API キーが必要です]({{site.baseurl}}/api/api_key/)。

## レート制限

{% multi_lang_include rate_limits.md endpoint='users merge' %}

## リクエスト本文

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

| パラメーター | 必須 | データ型 | 説明 |
|---|---|---|---|
| `merge_updates` | 必須 | 配列 | オブジェクト配列。各オブジェクトには、`identifier_to_merge``identifier_to_keep`オブジェクトとオブジェクトが含まれている必要があります。オブジェクトはそれぞれ`external_id`、`user_alias`またはでユーザーを参照する必要があります`email`。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

### マージ動作

以下に記載されている動作は、*Snowflakeを搭載していないすべてのBraze機能に当てはまります*。ユーザーマージは、[**メッセージング履歴**] タブ、[セグメント拡張]、[クエリビルダー]、および [カレント] には反映されません。

{% alert important %}
エンドポイントは、`merge_updates`更新されるオブジェクトの順序を保証しません。
{% endalert %}

このエンドポイントは、ターゲットユーザーで次のフィールドが見つからない場合、それらのいずれかをマージします。

- 名
- 姓
- メール
- 性別
- 生年月日
- 電話番号
- タイムゾーン
- 自宅の都市
- 国
- 言語
- セッション数 (両方のプロファイルからのセッションの合計)
- 最初のセッションの日付（Brazeは2つの日付のうち早い日付を選択します）
- 最後のセッションの日付（Brazeは2つの日付のうち遅い日付を選択します）
- カスタム属性 (ターゲットプロファイルの既存のカスタム属性は保持され、ターゲットプロファイルに存在しなかったカスタム属性も含まれます)
- カスタムイベントと購入イベントデータ
- 「Y日でX回」セグメンテーション用のカスタムイベントおよび購入イベントプロパティ（X<=50、Y<=30）
- セグメント化可能なカスタムイベントの概要
  - イベント数 (両方のプロファイルの合計)
  - イベントが最初に発生しました（Brazeは2つの日付のうち早い日付を選択します）
  - 最後に発生したイベント（Brazeは2つの日付のうち遅い日付を選択します）
- アプリ内購入合計 (セント) (両方のプロファイルの合計)
- 購入総数 (両方のプロファイルの合計)
- 初回購入日（Brazeは2つの日付のうち早い方の日付を選択します）
- 最終購入日（Brazeは2つの日付のうち遅い日付を選択します）
- アプリ概要
- last\_x\_at フィールド（孤立したプロファイルフィールドが最新の場合、Braze はフィールドを更新します）
- キャンペーンのインタラクションデータ (Braze が最新の日付フィールドを選択します)
- ワークフローの概要 (Braze が最新の日付フィールドを選択します)
- メッセージとメッセージエンゲージメント履歴

セッションデータは、アプリが両方のユーザープロファイルに存在する場合にのみマージされます。このエンドポイントはサブスクリプショングループまたはサブスクリプションをマージしないことに注意してください。

#### カスタムイベント日付と購入イベント日の動作
これらの統合フィールドにより、「Y日以内にX件のイベントが発生する」フィルターが更新されることに注意してください。購入イベントの場合、これらのフィルターには「Y 日間の購入数」と「過去 Y 日間の購入金額」が含まれます。

### メールによるユーザーの結合

識別子として an を指定する場合、`email``prioritization`識別子には追加の値が必要です。は、`prioritization`複数のユーザーが見つかった場合にどのユーザーをマージするかを指定する配列でなければなりません。`prioritization`は順序付けされた配列です。つまり、優先順位付けで複数のユーザーが一致した場合、マージは行われません。

配列に指定できる値は`identified`、`unidentified`、`most_recently_updated`です。`most_recently_updated`最後に更新されたユーザーを優先することを指します。

優先順位付け配列には、一度に次のオプションのうち 1 つしか存在できません。
-`identified` ユーザーに優先順位を付けることを指します `external_id`
-`unidentified` 何もないユーザーを優先することを指します `external_id`

## リクエスト例

### 基本要求
これはリクエストのパターンを示すための基本的なリクエストボディです。

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
        "email": "user1@braze.com"
      },
      "identifier_to_keep": {
        "email": "user2@braze.com"
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

### 身元不明ユーザーの結合

次のリクエストは、メールアドレスが「john.smith@braze.com」で最後に更新された正体不明のユーザーを `external_id`「john」のユーザーに統合します。を使用すると、クエリーが 1 `most_recently_updated` 人の身元不明ユーザーのみにフィルタリングされます。したがって、このメールアドレスを持つ正体不明のユーザーが2人いる場合、`external_id`「john」のユーザーに統合されるのは1人だけです。

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

### 未確認ユーザーを識別済みユーザーへの統合

次の例では、電子メールアドレスが「john.smith@braze.com」で最後に更新された正体不明ユーザーを、電子メールアドレス「john.smith@braze.com」を持つ最後に更新された識別済みユーザーに統合します。を使用すると、クエリーが 1 人のユーザ（1 人の身元不明のユーザとの `identifier_to_merge` 1 人の識別されたユーザ`identifier_to_keep`）`most_recently_updated`だけにフィルタされます。

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

### 「最新」の優先順位付けを含めずに身元不明のユーザーを統合する

メールアドレスが「john.smith@braze.com」の正体不明のユーザーが2人いる場合、この例のリクエストでは、そのメールアドレスを持つ身元不明のユーザーが2人いるため、ユーザーは統合されません。このリクエストは、メールアドレスが「john.smith@braze.com」の身元不明のユーザーが1人しかいない場合にのみ機能します。

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

このエンドポイントには、`202`との 2 つのステータスコード応答があります`400`。

### 成功レスポンスの例

`202`ステータスコードは次のレスポンスボディを返す可能性があります。

```json
{
  "message": "success"
}
```

### エラーレスポンスの例

`400`ステータスコードは次のレスポンスボディを返す可能性があります。発生する可能性のあるエラーの詳細については、「[トラブルシューティング](#troubleshooting)」を参照してください。

```json
{
  "message": "'merge_updates' must be an array of objects"
}
```

## トラブルシューティング

次の表は、発生する可能性のあるエラーメッセージの一覧です。

| エラー | トラブルシューティング |
| --- |
| `'merge_updates' must be an array of objects` | `merge_updates` それがオブジェクトの配列であることを確認してください。|
| `a single request may not contain more than 50 merge updates` | 1 回のリクエストで指定できるマージ更新は 50 件までです。|
| `identifiers must be objects with an 'external_id' property that is a string, or 'user_alias' property that is an object` | リクエスト内の識別子を確認してください。|
| `identifiers must be objects of the same type` | 識別子のオブジェクトタイプが一致していることを確認する。|
| `'merge_updates' must only have 'identifier_to_merge' and 'identifier_to_keep'` | 2 `merge_updates` `identifier_to_merge` つのオブジェクトのみが含まれていることを確認し、`identifier_to_keep`.|
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}
