---
nav_title: "POST:スケジュールされたAPIトリガー・キャンバスを更新する"
article_title: "POST:スケジュールされたAPIトリガー・キャンバスを更新する"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、「スケジュールされた API トリガーキャンバスを更新」Braze エンドポイントの詳細について説明します。"

---
{% api %}
# スケジュールされたAPIトリガーキャンバスを更新する
{% apimethod post core_endpoint|{1} %}
/canvas/trigger/schedule/update
{% endapimethod %}

> このエンドポイントを使用して、ダッシュボードで作成されたスケジュール済みAPIトリガーキャンバスを更新する。 

これにより、メッセージ送信をトリガーするアクションを決定できます。メッセージ自体にテンプレート化される `trigger_properties` を渡すことができます。

このエンドポイントを使用してメッセージを送信するには、[キャンバスを]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier)構築するときに作成されたキャンバスIDが必要であることに注意してほしい。

どのスケジュールも、スケジュール作成リクエストや以前のスケジュール更新リクエストで提供したものを完全に上書きする。 
  - 例えば、最初に`"schedule" : {"time" : "2015-02-20T13:14:47", "in_local_time" : true}` を指定し、更新時に`"schedule" : {"time" : "2015-02-20T14:14:47"}` を指定した場合、メッセージはユーザーのローカル時間ではなく、UTCで指定された時間に送信されるようになる。 
  - 送信予定時刻に非常に近いか、送信予定時刻に更新されたスケジュールされたトリガーは、ベストエフォートで更新されます。このため、直前の変更は、ターゲットユーザーの全員または一部に適用されるか、あるいはまったく適用されない可能性があります。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#8fdf158b-ce20-41d8-80e4-a9300a6706d4 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`canvas.trigger.schedule.update`権限を持つ [API キー]({{site.baseurl}}/api/basics#rest-api-key/) が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## Request body

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
| `schedule_id` | オプション | string | 更新する`schedule_id` （スケジュール作成のレスポンスから取得）。 |
|`schedule` | required | オブジェクト | [スケジュールオブジェクト]({{site.baseurl}}/api/objects_filters/schedule_object/)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例
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
