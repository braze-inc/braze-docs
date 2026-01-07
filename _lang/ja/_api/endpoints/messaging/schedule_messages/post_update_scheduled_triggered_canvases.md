---
nav_title: "POST:スケジュールされたAPIトリガーキャンバスを更新する"
article_title: "POST:スケジュールされたAPIトリガー・キャンバスを更新する"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、「スケジュールされた API トリガーキャンバスを更新」Braze エンドポイントの詳細について説明します。"

---
{% api %}
# スケジュールされたAPIトリガーキャンバスを更新する
{% apimethod postcore_endpoint|https://www.braze.com/docs/core_endpoints %}
/canvas/trigger/schedule/update
{% endapimethod %}

> このエンドポイントを使用して、ダッシュボードで作成されたスケジュール済みAPIトリガーキャンバスを更新する。

これにより、どのアクションがメッセージ送信のトリガーになるかを決めることができる。Brazeがテンプレート化した`trigger_properties` をメッセージ自体に渡すことができる。

このエンドポイントを使用してメッセージを送信するには、[キャンバスを]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier)構築するときに作成されたキャンバスIDが必要であることに注意してほしい。

どのスケジュールも、スケジュール作成リクエストや以前のスケジュール更新リクエストで提供したものを完全に上書きする。
  - 例えば、最初に`"schedule" : {"time" : "2015-02-20T13:14:47", "in_local_time" : true}` を指定し、更新で`"schedule" : {"time" : "2015-02-20T14:14:47"}` を指定した場合、Brazeはユーザーのローカライゼーション時間ではなく、UTCで指定した時間にメッセージを送信する。
  - スケジュールされたトリガーは、送信予定時刻に近いか、送信予定時刻中に更新されるため、Brazeは、ターゲットユーザーのすべて、一部、または全員に、直前の変更を適用する可能性がある。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#8fdf158b-ce20-41d8-80e4-a9300a6706d4 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`canvas.trigger.schedule.update`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## 要求本文:

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) see Canvas identifier,
  "schedule_id": (required, string) the `schedule_id` to update (obtained from the response to create schedule),
  "schedule": {
    // required, see create schedule documentation
  }
}
```

## リクエストパラメーター

| パラメーター | required | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
|`canvas_id`|必須|string| [キャンバス識別子]({{site.baseurl}}/api/identifier_types/)を参照してください。 |
| `schedule_id` | オプション | 文字列 | 更新する`schedule_id` （スケジュール作成のレスポンスから取得）。 |
|`schedule` | 必須 | オブジェクト | [スケジュールオブジェクト]({{site.baseurl}}/api/objects_filters/schedule_object/)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 例のリクエスト
```
curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/schedule/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "schedule_id": "schedule_identifier",
  "schedule": {
    "time": "2017-05-24T21:30:00Z",
    "in_local_time": true
  }
}'
```

{% endapi %}
