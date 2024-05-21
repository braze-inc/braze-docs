---
nav_title: "ポスト:スケジュールされた API トリガーキャンバスを更新"
article_title: "ポスト:スケジュールされた API トリガーキャンバスを更新"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、アップデートスケジュールされた API トリガーの Canvases Braze エンドポイントの詳細について説明します。"

---
{% api %}
# スケジュールされた API トリガーキャンバスを更新
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/canvas/trigger/schedule/update
{% endapimethod %}

> このエンドポイントを使用して、ダッシュボードで作成されたスケジュールされた API トリガーキャンバスを更新します。 

これにより、メッセージの送信をトリガーするアクションを決定できます。これをメッセージ自体にテンプレートとして渡すことができます。`trigger_properties`

[このエンドポイントでメッセージを送信するには、キャンバスの作成時に作成された Canvas ID が必要であることに注意してください。]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier)

どのスケジュールでも、スケジュールの作成リクエストまたは以前のスケジュールの更新リクエストで指定したスケジュールが完全に上書きされます。
  -たとえば、`"schedule" : {"time" : "2015-02-20T13:14:47", "in_local_time" : true}`最初に提供した後で更新を行った場合`"schedule" : {"time" : "2015-02-20T14:14:47"}`、メッセージはユーザーの現地時間ではなく、UTC で指定された時刻に送信されるようになりました。
  -スケジュールされたトリガーが、送信予定時刻のすぐ近く、または送信予定時刻の間に更新された場合、最善を尽くして更新されるため、最後の瞬間の変更がターゲットユーザーのすべてまたは一部に適用されたり、まったく適用されなかったりする可能性があります。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#8fdf158b-ce20-41d8-80e4-a9300a6706d4 {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`canvas.trigger.schedule.update`権限のある [API キーが必要です]({{site.baseurl}}/api/basics#rest-api-key/)。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエスト本文

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

| パラメーター | 必須 | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
[| `canvas_id` |必須|文字列| キャンバス識別子を参照してください。]({{site.baseurl}}/api/identifier_types/)|
| `schedule_id` | オプション | 文字列 | 更新する (スケジュールを作成するための応答から取得) `schedule_id`.|
| `schedule` | 必須 | オブジェクト | [スケジュールオブジェクトを参照してください]({{site.baseurl}}/api/objects_filters/schedule_object/)。|
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
