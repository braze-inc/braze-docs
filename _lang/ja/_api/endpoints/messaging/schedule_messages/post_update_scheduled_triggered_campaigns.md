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
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}。
/campaigns/trigger/schedule/update
{% endapimethod %}

> このエンドポイントを使用して、ダッシュボードで作成した、API でトリガーされるスケジュール済みキャンペーンを更新します。これにより、メッセージの送信をトリガーするアクションを決めることができます。

Brazeがテンプレート化した`trigger_properties` をメッセージ自体に渡すことができる。

このエンドポイントでメッセージを送信するには、[API-Triggered キャンペーン]({{site.baseurl}}/api/api_campaigns/) をビルドするときに作成されるキャンペーン ID が必要です。

どのスケジュールも、あなたがスケジュール作成リクエストや以前の更新スケジュールリクエストで提供したスケジュールを完全に上書きする。例えば、当初スケジュールを`"schedule" : {"time" : "2015-02-20T13:14:47", "in_local_time" : true}` に設定し、後で`"schedule" : {"time" : "2015-02-20T14:14:47"}` に更新した場合、Brazeはユーザーのローカライゼーション時間ではなく、UTCで指定した時間にメッセージを送信する。

スケジュールされたトリガーが、送信予定時刻に近いか、送信予定時刻中に更新された場合、ベストエフォートで更新されるため、Brazeはターゲットとするユーザー全員、一部、または全員に直前の変更を適用することができる。元のスケジュールがローカル時刻を使用しており、元の時刻がいずれかのタイムゾーンで既に経過している場合、更新は適用されません。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6d2a6e66-9d6f-4ae1-965a-79fa52b86b1d {% endapiref %}

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`campaigns.trigger.schedule.update`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## 要求本文:

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

| パラメーター | required | データ型 | 説明 |
| --------- | ---------| --------- | ----------- |
|`campaign_id`|必須|文字列| [キャンペーン識別子]({{site.baseurl}}/api/identifier_types/)を参照してください|
| `schedule_id` | 必須 | 文字列 | 更新する`schedule_id` (スケジュールを作成するレスポンスから取得)。 |
|`schedule` | 必須 | オブジェクト | [スケジュールオブジェクト]({{site.baseurl}}/api/objects_filters/schedule_object/)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 例のリクエスト
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
