---
nav_title: "POST: 라이브 활동 시작"
article_title: "POST: 라이브 활동 시작"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "이 문서에서는 라이브 활동 시작 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 라이브 활동 시작
{% apimethod post %}
/messages/live_activity/start
{% endapimethod %}

> 이 엔드포인트를 사용하여 iOS 앱에 표시되는 [실시간 활동을]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?sdktab=swift) 원격으로 시작할 수 있습니다. 이 엔드포인트에는 추가 설정이 필요합니다.

라이브 활동을 만든 후에는 특정 세그먼트에 대해 원격으로 활동을 시작하도록 POST 요청을 할 수 있습니다. Apple의 실시간 활동에 대한 자세한 내용은 [ActivityKit 푸시 알림으로 실시간 활동 시작 및 업데이트](https://developer.apple.com/documentation/activitykit/starting-and-updating-live-activities-with-activitykit-push-notifications)를 참조하세요.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#2300226e-f26a-4154-9bcc-5883f1f294cd {% endapiref %}

## 필수 구성 요소

이 엔드포인트를 사용하려면 다음을 완료해야 합니다:

- `messages.live_activity.start` 권한을 사용하여 API 키를 생성합니다.
- 브레이즈 스위프트 SDK를 사용하여 [라이브 활동을 생성합니다]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?tab=local&sdktab=swift#swift_create-an-activity).

{% multi_lang_include api/payload_size_alert.md %}

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 본문

```json
{
  "app_id": "(required, string) App API identifier retrieved from the Developer Console.",
  "activity_id": "(required, string) Define a custom string as your `activity_id`. You will use this ID when you wish to send update or end events to your Live Activity.",
  "activity_attributes_type": "(required, string) The activity attributes type you define within `liveActivities.registerPushToStart` in your app",
  "activity_attributes": "(required, object) The static attribute values for the activity type (such as the sports team names, which don't change)",
  "content_state": "(required, object) You define the ContentState parameters when you create your Live Activity. Pass the updated values for your ContentState using this object. The format of this request must match the shape you initially defined.",
  "dismissal_date": "(optional, datetime in ISO-8601 format) The time to remove the Live Activity from the user’s UI. If this time is in the past, the Live Activity will be removed immediately.",
  "stale_date": "(optional, datetime in ISO-8601 format) The time the Live Activity content is marked as outdated in the user’s UI.",
  "notification": "(required, object) Include an `apple_push` object to define a push notification that creates an alert for the user, displayed on paired watchOS devices. Should include `notification.alert.title` and `notification.alert.body`",
  // One of the following:
  "external_user_ids": "(optional, array of strings) see external user identifier",
  "custom_audience": "(optional, connected audience object) see connected audience",
  "segment_id": "(optional, string) see segment identifier"
}
```

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형| 설명  |
|-----------|----------|----------|--------------|
| `app_id` | 필수 | 문자열 | [API 키]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) 페이지에서 검색한 앱 [API 식별자입니다]({{site.baseurl}}/api/identifier_types/#the-app-identifier).  |
| `activity_id` | 필수 | 문자열  | 사용자 지정 문자열을 `activity_id` 로 정의합니다. 라이브 활동에 업데이트 또는 종료 이벤트를 보내려는 경우 이 ID를 사용합니다.  |
| `activity_attributes_type`  | 필수 | 문자열 | 앱의 `liveActivities.registerPushToStart` 내에서 정의하는 활동 속성 유형입니다.  |
| `activity_attributes` | 필수 | 객체  | 활동 유형에 대한 정적 속성 값(예: 변경되지 않는 스포츠 팀 이름)입니다. |
| `content_state` | 필수 | 객체  | 라이브 활동을 만들 때 `ContentState` 매개변수를 정의합니다. 이 개체를 사용하여 `ContentState`에 대해 업데이트된 값을 전달합니다.<br><br>이 요청의 형식은 처음에 정의한 모양과 일치해야 합니다. |
| `dismissal_date` | 선택 사항 | 날짜 시간 <br>[(ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 문자열[)](https://en.wikipedia.org/wiki/ISO_8601)  | 이 매개변수는 사용자 UI에서 라이브 활동을 제거할 시간을 정의합니다. |
| `stale_date` | 선택 사항 | 날짜 시간 <br>[(ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 문자열[)](https://en.wikipedia.org/wiki/ISO_8601)  | 이 매개변수는 라이브 활동 콘텐츠가 사용자 UI에서 오래된 것으로 표시되는 시점을 시스템에 알려줍니다. |
| `notification` | 필수 | 객체 | 객체를 포함하여 [`apple_push`]({{site.baseurl}}/api/objects_filters/messaging/apple_object/) 객체를 포함하여 푸시 알림을 정의합니다. 이 푸시 알림의 동작은 사용자가 활성 상태인지 또는 사용자가 프록시 기기를 사용하고 있는지에 따라 달라집니다. {::nomarkdown}<ul><li>다음과 같은 경우 <code>notification</code> 가 포함되어 있고 업데이트가 전달될 때 사용자가 iPhone에서 활성화되어 있으면 업데이트된 실시간 활동 UI가 아래로 슬라이드되어 푸시 알림처럼 표시됩니다.</li><li>다음과 같은 경우 <code>notification</code> 가 포함되어 있고 사용자가 iPhone에서 활성화되어 있지 않으면 잠금 화면에 업데이트된 라이브 활동 UI가 표시되도록 화면이 켜집니다.</li><li>그리고 <code>notification alert</code> 는 표준 푸시 알림으로 표시되지 않습니다. 또한 사용자에게 Apple Watch와 같은 프록시 디바이스가 있는 경우에는 <code>alert</code> 가 표시됩니다.</li></ul>{:/} |
| `external_user_ids` | `segment_id` 또는 `audience` 제공 시 선택 사항 | 문자열 배열 | [외부 사용자 ID를]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields) 참조하세요.  |
| `segment_id `  | `external_user_ids` 또는 `audience` 제공 시 선택 사항 | 문자열    | [세그먼트 식별자를]({{site.baseurl}}/api/identifier_types/) 참조하세요. |
| `custom_audience` | `external_user_ids` 또는 `segment_id` 제공 시 선택 사항 | 연결된 대상 개체  | [연결된 오디언스]({{site.baseurl}}/api/objects_filters/connected_audience/)을 참조하십시오. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 요청 예시

```json
curl --location --request POST 'https://rest.iad-01.braze.com/messages/live_activity/start' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {YOUR-REST-API-KEY}' \
--data-raw '{
    "app_id": "{YOUR-APP-API-IDENTIFIER}",
    "activity_id": "football-chiefs-bills-2024-01-21",
    "content_state": {
        "teamOneScore": 0,
        "teamTwoScore": 0
    },
    "activity_attributes_type": "FootballActivity",
    "activity_attributes": {
        "team1Name": "Chiefs",
        "team2Name": "Bills"
    },
    "dismissal_date": "2024-01-22T00:00:00+0000",
    "stale_date": "2024-01-22T16:55:49+0000",
    "notification": {
        "alert": {
            "body": "The game is starting! Tune in soon!",
            "title": "Chiefs v. Bills"
        }
    },
    // One of the following required:
    "segment_id": "{YOUR-SEGMENT-API-IDENTIFIER}", // Optional
    "custom_audience": {...}, // Optional
    "external_user_ids": ["user-id1", "user-id2"], // Optional
}'
```

## 응답

이 엔드포인트에 대한 상태 코드 응답은 `201` 와 `4XX` 두 가지입니다.

### 성공 응답의 예

요청 형식이 올바르게 지정되어 요청을 수신한 경우 `201` 상태 코드가 반환됩니다. `201` 상태 코드는 다음과 같은 응답 본문을 반환할 수 있습니다.

```json
{
  "message": "success"
}
```

### 오류 응답의 예

`4XX` 상태 코드 클래스는 클라이언트 오류를 나타냅니다. 발생할 수 있는 오류에 대한 자세한 내용은 [API 오류 및 응답 문서를]({{site.baseurl}}/api/errors/) 참조하세요.

`400` 상태 코드는 다음과 같은 응답 본문을 반환할 수 있습니다. 

```json
{
    "error": "\nProblem:\n  message body does not match declared format\nResolution:\n  when specifying application/json as content-type, you must pass valid application/json in the request's 'body' "
}
```

{% endapi %}
