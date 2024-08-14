---
nav_title: "POST: 실시간 활동 업데이트"
article_title: "POST: 실시간 활동 업데이트"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "이 문서에서는 실시간 활동 업데이트 엔드포인트에 대한 세부 정보를 간략하게 설명합니다."

---
{% api %}
# 실시간 활동 업데이트
{% apimethod post %}
/messages/live_activity/update
{% endapimethod %}

> 이 엔드포인트를 사용하여 iOS 앱에 표시되는[라이브 활동을]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/live_activities/)업데이트하고 종료하세요. 이 끝점에는 추가 설정이 필요합니다.

실시간 활동을 등록한 후 JSON 페이로드를 전달하여 APN(Apple 푸시 알림 서비스)을 업데이트할 수 있습니다. 자세한 내용은[푸시 알림 페이로드로 실시간 활동 업데이트](https://developer.apple.com/documentation/activitykit/updating-and-ending-your-live-activity-with-activitykit-push-notifications)에 대한 Apple 설명서를 참조하세요.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#2300226e-f26a-4154-9bcc-5883f1f294cd {% endapiref %}

## 전제 조건

이 엔드포인트를 사용하려면 다음을 완료해야 합니다.

- `messages.live_activity.update` 권한을 사용하여 API 키를 생성합니다.
- Braze Swift SDK를 사용하여[원격]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/live_activities/?tab=remote#step-2-start-the-activity) 또는 [로컬]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/live_activities/?tab=local#step-2-start-the-activity)로 라이브 활동을 등록하세요.

## 비율 제한

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 본문

```json
{
   "app_id": "(required, string) App API identifier retrieved from the Developer Console.",
   "activity_id": "(required, string) When you register your Live Activity using launchActivity, you use the pushTokenTag parameter to name the Activity’s push token to a custom string. Set activity_id to this custom string to define which Live Activity you want to update.",
   "content_state": "(required, object) You define the ContentState parameters when you create your Live Activity. Pass the updated values for your ContentState using this object. The format of this request must match the shape you initially defined.",
   "end_activity": "(optional, boolean) If true, this request ends the Live Activity.",
   "dismissal_date": "(optional, datetime in ISO-8601 format) The time to remove the Live Activity from the user’s UI. If this time is in the past, the Live Activity will be removed immediately.",
   "stale_date": "(optional, datetime in ISO-8601 format) The time the Live Activity content is marked as outdated in the user’s UI.",
   "notification": "(optional, object ) Include an `apple_push` object to define a push notification that creates an alert for the user."
 }
 ```

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `app_id` | 필수 | 문자열 |[API 키]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) 페이지에서 검색된 앱 [API 식별자]({{site.baseurl}}/api/identifier_types/#the-app-identifier)입니다. |
| `activity_id` | 필수 | 문자열 | [`launchActivity`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class)를 사용하여 실시간 활동을 등록하면 `pushTokenTag` 매개변수를 사용하여 활동의 푸시 토큰 이름을 커스텀 문자열로 지정합니다.<br><br>업데이트할 라이브 활동을 정의하려면 `activity_id`를 이 커스텀 문자열에 추가하세요. |
| `content_state` | 필수 | 객체 | 라이브 활동을 생성할 때 `ContentState` 매개변수를 사용합니다. 이 개체를 사용하여 `ContentState`에 대해 업데이트된 값을 전달합니다.<br><br>이 요청의 형식은 처음에 정의한 형태와 일치해야 합니다. |
| `end_activity` | 선택사항 | 부울 | 만약에 `true`인 경우 이 요청으로 라이브 활동이 종료됩니다. |
| `dismissal_date`| 선택사항 | 날짜 시간 <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 문자열) | 이 매개변수는 사용자 UI에서 라이브 활동을 제거하는 시간을 정의합니다. 이 시간이 과거이고 `end_activity`가 `true`인 경우, 라이브 활동이 즉시 삭제됩니다.<br><br> 만약에 `end_activity`가 `false` 또는 생략되면 이 매개변수는 라이브 활동만 업데이트합니다.|
| `stale_date`| 선택사항 | 날짜 시간 <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 문자열) | 이 매개변수는 라이브 활동 콘텐츠가 사용자 UI에서 오래된 것으로 표시되는 시기를 시스템에 알려줍니다. |
| `notification` | 선택사항 | 객체 | 푸시 알림을 정의하는 [`apple_push`]({{site.baseurl}}/api/objects_filters/messaging/apple_object/) 개체입니다. 이 푸시 알림의 동작은 사용자가 활성 상태인지 또는 사용자가 프록시 기기를 사용하고 있는지에 따라 달라집니다. {::nomarkdown}<ul><li><code>알림</code>이 포함되어 있고 업데이트가 전달될 때 사용자가 iPhone에서 활성 상태인 경우 업데이트된 라이브 활동 UI가 아래로 미끄러져 푸시 알림처럼 표시됩니다.</li><li><code>알림</code>이 포함되어 있고 사용자가 iPhone에서 활성 상태가 아닌 경우 화면이 켜지고 잠금 화면에 업데이트된 라이브 활동 UI가 표시됩니다.</li><li><code>알림 경고는</code>표준 푸시 알림으로 표시되지 않습니다. 또한 사용자가 Apple Watch와 같은 프록시 장치를 사용하는 경우 해당 기기에 <code>경고</code>가 표시됩니다.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## 예시 요청

```json
curl --location --request POST 'https://rest.iad-01.braze.com/messages/live_activity/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {YOUR-REST-API-KEY}' \
--data-raw '{
    "app_id": "{YOUR-APP-API-IDENTIFIER}",
    "activity_id": "live-activity-1",
    "content_state": {
        "teamOneScore": 2,
        "teamTwoScore": 4
    },
    "end_activity": false,
    "dismissal_date": "2023-02-28T00:00:00+0000",
    "stale_date": "2023-02-27T16:55:49+0000",
    "notification": {
        "alert": {
            "body": "It's halftime! Let's look at the scores",
            "title": "Halftime"
        }
    }
}'
```

## 응답

이 엔드포인트에는 `201` 및 `4XX` 상태 코드 응답이 있습니다.

### 성공 응답 예시

요청의 형식이 올바르고 요청을 받은 경우 `201` 상태 코드가 반환됩니다. 상태 코드 `201`은 다음 응답 본문을 반환할 수 있습니다.

```json
{
  "message": "success"
}
```

### 오류 응답 예시

`4XX` 상태 코드 클래스는 클라이언트 오류를 ​​나타냅니다. 발생할 수 있는 오류에 대한 자세한 내용은 [API 오류 및 응답 문서]({{site.baseurl}}/api/errors/)를 참조하세요.

`400` 상태 코드는 다음 응답 본문을 반환할 수 있습니다. 

```json
{
    "error": "\nProblem:\n  message body does not match declared format\nResolution:\n  when specifying application/json as content-type, you must pass valid application/json in the request's 'body' "
}
```

{% endapi %}
