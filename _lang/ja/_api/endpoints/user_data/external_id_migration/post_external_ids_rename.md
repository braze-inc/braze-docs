---
nav_title: "ポスト:外部 ID の名前を変更"
article_title: "ポスト:外部 ID の名前を変更"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "この記事では、外部 ID の名前変更エンドポイントの詳細について説明します。"

---
{% api %}
# 外部 ID の名前を変更
{% apimethod post %}
/users/external_ids/rename
{% endapimethod %}

> このエンドポイントを使用して、ユーザーの外部 ID の名前を変更します。 

1 回のリクエストで最大 50 個の名前変更オブジェクトを送信できます。 

このエンドポイントは、ユーザーに新しい（プライマリ）`external_id`を設定し、既存のエンドポイントを廃止します。`external_id`つまり、`external_id`非推奨のものが削除されるまで、ユーザーはどちらでも識別できます。複数の外部 ID があると、移行期間を設けることができるため、以前の外部 ID 命名スキーマを使用する古いバージョンのアプリが壊れることはありません。 

[古い命名スキーマが使用されなくなったら、エンドポイントを使用して非推奨の外部 ID を削除することを強くお勧めします。`/users/external_ids/remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove)

{% alert warning %}
廃止された外部 ID は、`/users/external_ids/remove`代わりにエンドポイントで必ず削除してください。`/users/delete`廃止された外部 ID `/users/delete` を使用してにリクエストを送信すると、ユーザープロファイルが完全に削除され、元に戻すことはできません。
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#17682d2b-1546-4a3c-9703-aa5a12861d7c {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`users.external_ids.rename`権限のある [API キーが必要です]({{site.baseurl}}/api/api_key/)。

## レート制限

{% multi_lang_include rate_limits.md endpoint='external id migration' %}

## リクエスト本文

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

| パラメーター | 必須 | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
| `external_id_renames` | 必須 | 外部識別子名前変更オブジェクトの配列 | ビューリクエストの例と、外部識別子名前変更オブジェクトの構造に関する次の制限事項。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

- はユーザーのプライマリ ID である必要があり、非推奨の ID `current_external_id` であってはなりません
- は、プライマリ ID または非推奨 ID `new_external_id` としてまだ使用されていない必要があります。
- `current_external_id``new_external_id`とを同じにすることはできません

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
この応答では、すべての名前の変更が成功し、名前の変更が失敗し、関連するエラーが発生したかどうかが確認されます。`rename_errors`フィールド内のエラーメッセージは、元のリクエストの配列内のオブジェクトのインデックスを参照します。

```
{
  "message" : (string) status message,
  "external_ids" : (array of strings) successful rename operations,
  "rename_errors": (array of arrays) <minor error message>
}
```

有効なリクエストがあると、`message``success`このフィールドが返されます。`rename_errors`より詳細なエラーがアレイにキャプチャされます。次の場合、`message`このフィールドはエラーを返します。
-API キーが無効です
\- 空の`external_id_renames` 配列
-50 `external_id_renames` 個を超えるオブジェクトを含む配列
-レート制限に達しました（1 分あたり 1,000 リクエスト以上）

## よくある質問

**これはMAUに影響しますか？**<br>
いいえ、ユーザー数は同じなので、新しいユーザー数が増えるだけです`external_id`。

**ユーザーの行動は歴史的に変わりますか？**<br>
いいえ。ユーザーはそのままで、過去の行動はすべてそのユーザーに関連しているからです。

**開発/ステージングワークスペースで実行できますか？**<br>
はい。実際、ステージングまたは開発ワークスペースでテスト移行を実行し、本番データで実行する前にすべてがスムーズに進んでいることを確認することを強くお勧めします。

**これはデータポイントを消費しますか？**<br>
この機能にはデータポイントはかかりません。

**推奨非推奨期間はどのくらいですか?**<br>
非推奨の外部IDを保持できる期間に厳しい制限はありませんが、非推奨のIDでユーザーを参照する必要がなくなったら削除することを強くお勧めします。

{% endapi %}
