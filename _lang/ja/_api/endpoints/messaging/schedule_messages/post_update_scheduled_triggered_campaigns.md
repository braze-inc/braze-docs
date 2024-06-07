---
nav_title: "ポスト:スケジュールされた API トリガー キャンペーンの更新"
article_title: "ポスト:スケジュールされた API トリガー キャンペーンの更新"
search_tag: Endpoint
page_order: 4
layout: api_page
description: "この記事では、スケジュールされた API トリガー キャンペーンの更新の Braze エンドポイントについて詳しく説明します。"

---
{% api %}
# スケジュールされた API トリガー キャンペーンを更新する
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/campaigns/trigger/schedule/update
{% endapimethod %}

> このエンドポイントを使用して、ダッシュボードで作成されたスケジュールされた API トリガー キャンペーンを更新し、メッセージを送信するトリガーとなるアクションを決定できるようにします。

通行できます `trigger_properties` メッセージ自体にテンプレート化されます。

このエンドポイントを使用してメッセージを送信するには、[API トリガー キャンペーン]({{site.baseurl}}/api/api_campaigns/)の作成時に作成されたキャンペーン ID が必要であることに注意してください。

任意のスケジュールは、スケジュール作成リクエストまたは以前のスケジュール更新リクエストで指定したスケジュールを完全に上書きします。例えば、最初に `"schedule" : {"time" : "2015-02-20T13:14:47", "in_local_time" : true}` そしてアップデートでは `"schedule" : {"time" : "2015-02-20T14:14:47"}`、メッセージはユーザーの現地時間ではなく、UTC で指定された時間に送信されるようになります。送信されるはずの時間に非常に近い時間またはその間に更新されるスケジュールされたトリガーは、最大限の努力で更新されるため、土壇場での変更が対象ユーザーのすべて、一部、またはまったく適用されない可能性があります。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6d2a6e66-9d6f-4ae1-965a-79fa52b86b1d {% endapiref %}

## 前提条件

このエンドポイント [を]({{site.baseurl}}/api/basics#rest-api-key/) 使用するには、 `campaigns.trigger.schedule.update` 許可。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## リクエスト本文

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) see campaign identifier,
  "schedule_id": (required, string) the `schedule_id` to update (obtained from the response to create schedule),
  "schedule": {
    // required, see create schedule documentation
  }
}
```

## リクエストパラメータ

| パラメータ | 必須 | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
|`campaign_id`|必須|文字列| [キャンペーン識別子を]({{site.baseurl}}/api/identifier_types/)参照 |
| `schedule_id`| 必須 | 文字列 | `schedule_id` 更新する（スケジュールを作成するための応答から取得）。 |
|`schedule`| 必須 | オブジェクト | [スケジュール オブジェクト]({{site.baseurl}}/api/objects_filters/schedule_object/)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## リクエスト例
```
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/schedule/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "schedule_id": "schedule_identifier",
  "schedule": {
    "time": "2017-05-24T21:30:00Z",
    "in_local_time": true
  }
}'
```

{% endapi %}
