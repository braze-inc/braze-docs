---
nav_title: "POST:スケジュールされた API トリガーキャンペーンの更新"
article_title: "POST:スケジュールされた API トリガーキャンペーンの更新"
search_tag: Endpoint
page_order: 4
layout: api_page
description: "この記事では、「スケジュールされた API トリガーキャンペーンの更新」Braze エンドポイントの詳細について説明します。"

---
{% api %}
# スケジュールされた API トリガーキャンペーンの更新
{% apimethod post core_endpoint|{1} %}
/campaigns/trigger/schedule/update
{% endapimethod %}

> このエンドポイントを使用して、ダッシュボードで作成した、API でトリガーされるスケジュール済みキャンペーンを更新します。これにより、メッセージの送信をトリガーするアクションを決めることができます。

メッセージ自体にテンプレート化される `trigger_properties` を渡すことができます。

このエンドポイントでメッセージを送信するには、[API-Triggered キャンペーン]({{site.baseurl}}/api/api_campaigns/) をビルドするときに作成されるキャンペーン ID が必要です。

スケジュールは、スケジュール作成リクエストまたは以前のスケジュール更新リクエストで指定したものを完全に上書きします。たとえば、最初に`"schedule" : {"time" : "2015-02-20T13:14:47", "in_local_time" : true}` を指定し、次に更新で`"schedule" : {"time" : "2015-02-20T14:14:47"}` を指定した場合、メッセージはユーザーのローカル時刻ではなくUTC で指定された時刻に送信されます。送信予定時刻に非常に近いか、送信予定時刻に更新されたスケジュールされたトリガーは、ベストエフォートで更新されます。このため、直前の変更は、ターゲットユーザーの全員または一部に適用されるか、あるいはまったく適用されない可能性があります。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6d2a6e66-9d6f-4ae1-965a-79fa52b86b1d {% endapiref %}

## 前提条件

このエンドポイントを使用するには、`campaigns.trigger.schedule.update` 権限を持つ[API キー]({{site.baseurl}}/api/basics#rest-api-key/) が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## Request body

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

## リクエストパラメーター

| パラメータ | required | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
|`campaign_id`|必須|string| [キャンペーン 識別子]({{site.baseurl}}/api/identifier_types/)を参照|
| `schedule_id` | 必須 | string | 更新する`schedule_id` (スケジュールを作成するレスポンスから取得)。 |
|`schedule` | required | オブジェクト | [スケジュールオブジェクト]({{site.baseurl}}/api/objects_filters/schedule_object/)を参照してください。 |
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
