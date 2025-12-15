---
nav_title: "POST:外部IDの名前を変更する"
article_title: "POST:外部IDの名前を変更する"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "この記事では、「外部 ID の名前を変更」エンドポイントの詳細について説明します。"

---
{% api %}
# 外部IDの名前を変更する
{% apimethod post %}
/users/external_ids/rename
{% endapimethod %}

> このエンドポイントを使用して、ユーザーの外部IDの名前を変更する。

1 回のリクエストで最大 50 個の名前変更オブジェクトを送信できます。

このエンドポイントは、ユーザーに新しい（プライマリ）`external_id` を設定し、既存の`external_id` を廃止する。つまり、非推奨の方が削除されるまで、どちらの `external_id` でもユーザーを識別できるということです。複数の外部IDを持つことで、以前の外部ID命名スキーマを使用しているレガシーバージョンのアプリが壊れないように、移行期間を設けることができる。

古い命名スキーマが使用されなくなった後は、[`/users/external_ids/remove` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove)を使用して非推奨の外部 ID を削除することを強く推奨します。

{% alert warning %}
非推奨の外部 ID は、`/users/delete` ではなく `/users/external_ids/remove` エンドポイントを使用して削除してください。非推奨外部 ID を使用して `/users/delete` にリクエストを送信すると、ユーザープロファイルは完全に削除され、元に戻すことはできません。
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#17682d2b-1546-4a3c-9703-aa5a12861d7c {% endapiref %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/api_key/)と`users.external_ids.rename`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='external id migration' %}

## 要求本文:

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_id_renames" : (required, array of external ID rename objects)
}
```

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
| `external_id_renames` | 必須 | 外部識別子リネームオブジェクトの配列 | 外部識別子の名前変更オブジェクトの構造に対するリクエスト例と次の制限事項を表示します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

次のことに注意してください。

- `current_external_id` はユーザーのプライマリ ID である必要があり、非推奨 ID にすることはできません
- `new_external_id` は、プライマリ ID または非推奨 IDとしてすでに使用されているものであってはなりません。
- `current_external_id` と`new_external_id` が同じであるはずがない。

## リクエスト例
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/external_ids/rename' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "external_id_renames" :[
    {
      "current_external_id": "existing_external_id",
      "new_external_id" : "new_external_id"
    }
  ]
}'
```

## 応答

この応答は、成功したすべての名前変更と、関連するエラーを伴う失敗した名前変更を確認します。`rename_errors` フィールドのエラーメッセージは、オリジナルリクエストの配列のオブジェクトのインデックスを参照する。

```
{
  "message" : (string) status message,
  "external_ids" : (array of strings) successful rename operations,
  "rename_errors": (array of arrays) <minor error message>
}
```

`message` フィールドは、有効なリクエストに対しては`success` を返す。より具体的なエラーは、`rename_errors` の配列に収められている。`message` フィールドは、以下の場合にエラーを返す：

- 無効なAPIキー
- 空の`external_id_renames` 配列
- 50 を超えるオブジェクトを持つ `external_id_renames` 配列
- レート制限に達しました (1分あたり1,000件以上のリクエスト)

## よくある質問

### これは MAU に影響しますか?
いや、ユーザー数は変わらないから、新しい`external_id` 。

### ユーザーの行動は長期的に変化していますか?
いや、ユーザーは変わらないし、過去の行動もすべてユーザーとつながっているからだ。

### 開発ワークスペースまたはステージングワークスペースで実行できますか?
はい。実際、ステージングまたは開発ワークスペースでテスト移行を実行し、本番データで実行する前にすべてがスムーズに進んでいることを確認するよう、強く推奨します。

### これはデータポイントを記録するのか？
この機能はデータポイントを記録しない。

### 推奨される償却期間は？
非推奨の外部IDをいつまで残しておけるかについての厳しい制限はないが、非推奨のIDでユーザーを参照する必要がなくなったら、削除することを強く推奨する。

{% endapi %}
