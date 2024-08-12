---
nav_title: "ポスト:ユーザーを識別"
article_title: "ポスト:ユーザーを識別"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
alias: /users_identify_merge/
description: "この記事では、ユーザー識別 Braze エンドポイントの詳細について説明します。"

---
{% api %}
# ユーザーを特定する
{% apimethod post %}
/users/identify
{% endapimethod %}

> このエンドポイントを使用して、身元不明の (エイリアスのみ) ユーザーを識別します。 

{% alert important %}
2023 年 8 月 7 日以降、このエンドポイントはすべての通話のデータを統合します。つまり[`merge_behavior`](#merge)、`merge`すべてのコールでに設定されます。
{% endalert %}

コールすると、`/users/identify`エイリアスのみのプロファイルが識別されたプロファイルに組み合わされ、エイリアスのみのプロファイルが削除されます。

`external_id`ユーザーを識別するには、`aliases_to_identify`オブジェクトにを含める必要があります。それを持つユーザーがいない場合は`external_id`、`external_id`エイリアスされたユーザーのレコードに単に追加され、そのユーザーは識別されたものとみなされます。1 つのリクエストで最大 50 のユーザーエイリアスを追加できます。 

その後、`external_id`複数の追加ユーザーエイリアスを単一のユーザーエイリアスに関連付けることができます。
-`merge_behavior` フィールドをに設定して以降の関連付けを行うと`none`、ユーザーエイリアスに関連付けられているプッシュトークンとメッセージ履歴のみが保持されます。属性、イベント、購入はすべて「孤立」し、特定されたユーザーには使用できなくなります。回避策の 1 つは、[`/users/export/ids`エンドポイントを使用して識別する前に]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)、エイリアスされたユーザーのデータをエクスポートし、属性、イベント、購入を特定されたユーザーに再度関連付けることです。
-`merge_behavior` フィールドをに設定して関連付けを行うと`merge`、[このエンドポイントは匿名ユーザーで見つかった特定のフィールドを識別されたユーザーにマージします](#merge)。

{% alert tip %}
ユーザーを特定する際にデータが予期せず失われるのを防ぐために、[まずデータ収集のベストプラクティスを参照して]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/best_practices/#capturing-user-data-when-alias-only-user-info-is-already-present)、エイリアスのみのユーザー情報がすでに存在する場合のユーザーデータのキャプチャについて学ぶことを強くお勧めします。
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5f74e0f7-0620-4c7b-b0a2-f5f38fdbff58 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`users.identify`権限のある [API キーが必要です]({{site.baseurl}}/api/api_key/)。

## レート制限 
2021 年 9 月 16 日以降に Braze にオンボーディングしたお客様のこのエンドポイントへのリクエストには、レート制限が適用されます。詳細については、「[API の制限]({{site.baseurl}}/api/basics/#api-limits)」を参照してください。

## リクエスト本文

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

| パラメーター | 必須 | データ型 | 説明 |
| -----------|----------| --------|------- |
| `aliases_to_identify` | 必須 | オブジェクトを識別するためのエイリアスの配列 | [オブジェクトとユーザーエイリアスオブジェクトを識別するには]({{site.baseurl}}/api/objects_filters/aliases_to_identify/)[、エイリアスを参照してください]({{site.baseurl}}/api/objects_filters/user_alias_object/)。|
| `merge_behavior` | オプション | 文字列 | `none` `merge` またはのいずれかが必要です。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

#### マージ・ビヘイビア・フィールド {#merge}

`merge_behavior`フィールドを設定すると、`merge`**匿名ユーザーのみにある以下のフィールドのいずれかを**、識別されたユーザーにマージするようにエンドポイントが設定されます。
<b>名</b>
姓
メール
<b>性別</b>
生年月日
電話番号
タイムゾーン: 
自宅の都市
国
言語
-セッション数 (両方のプロファイルからのセッションの合計)
-最初のセッションの日付（Brazeは2つの日付のうち早い日付を選択します）
-最後のセッションの日付（Brazeは2つの日付のうち遅い日付を選択します）
カスタム属性
-カスタムイベントと購入イベントデータ
-「Y日でX回」セグメンテーション用のカスタムイベントおよび購入イベントプロパティ（X<=50、Y<=30）
-セグメント化可能なカスタムイベントの概要
  -イベント数 (両方のプロファイルの合計)
  -イベントが最初に発生しました（Brazeは2つの日付のうち早い日付を選択します）
  -イベントの最終発生（Brazeは2つの日付のうち遅い日付を選択します）
-アプリ内購入合計（セント）（両方のプロファイルからの合計）
-購入総数 (両方のプロファイルの合計)
-初回購入日（Brazeは2つの日付のうち早い方の日付を選択します）
-最終購入日（Brazeは2つの日付のうち遅い方の日付を選択します）
-アプリ概要
-last\_x\_at フィールド（孤立したプロファイルフィールドが最新の場合、Braze はフィールドを更新します）
-キャンペーンの概要（Brazeが最新の日付フィールドを選択します）
-ワークフローの概要（Braze が最新の日付フィールドを選択します）
-メッセージとメッセージのエンゲージメント履歴

匿名ユーザーから特定ユーザーまでの以下のフィールドのいずれか
-カスタムイベントと購入イベント数、初日と最終日のタイムスタンプ
  -これらの統合フィールドにより、「Y日以内にX件のイベントが発生する」フィルターが更新されます。購入イベントの場合、これらのフィルターには「Y 日間の購入数」と「過去 Y 日間の購入金額」が含まれます。

セッションデータは、アプリが両方のユーザープロファイルに存在する場合にのみマージされます。たとえば、ターゲットユーザーには「ABCapp」のアプリ概要がなく、元のユーザーにはある場合、ターゲットユーザーのプロファイルには、統合後に「ABCapp」のアプリ概要が表示されます。 

フィールドをに設定しても`none`、ユーザーデータは指定されたユーザープロファイルに統合されません。

## リクエスト例
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/identify' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "aliases_to_identify" : 
  [
    {
      "external_id": "external_identifier",
      "user_alias" : {
          "alias_name" : "example_alias",
          "alias_label" : "example_label"
      }
    }
  ],
  "merge_behavior": "merge"
}'
```

{% alert tip %}
`alias_name`およびの詳細については`alias_label`、[ユーザーエイリアスのドキュメントをご覧ください]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)。
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
