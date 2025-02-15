---
title: API 또는 코드 용어집
navlink: apitest
layout: api_page
page_order: 2

#Required
description: "Google 검색 설명입니다. 160자를 초과하는 문자는 잘리므로 간결하게 작성하세요."
page_type: glossary
#Use if applicable

tool:
  - Dashboard
  - Docs
  - Canvas
  - Campaigns
  - Segments
  - Templates
  - Media
  - Location
  - Currents
  - Reports

platform:
  - iOS
  - Android
  - Web
  - API

channel:
  - Content Cards
  - Email
  - News Feed
  - In-App Messages
  - Push
  - SMS
  - Webhooks

noindex: true
#ATTENTION: remove noindex and this alert from template

excerpt_separator: ""
---
{% api %}
## 1 이메일 템플릿 만들기
{% apimethod post %}
/templates/email/create
{% endapimethod %}
{% apitags %}
포스트, 이메일, 생성, 템플릿, REST, API
{% endapitags %}

이메일 템플릿 REST API를 사용하여 Braze 대시보드의 템플릿 및 미디어 페이지에서 저장한 이메일 템플릿을 프로그래밍 방식으로 관리할 수 있습니다. Braze는 이메일 템플릿을 만들고 업데이트할 수 있는 두 가지 엔드포인트를 제공합니다.

이 엔드포인트의 응답에는 후속 API 호출에서 템플릿을 업데이트하는 데 사용할 수 있는 필드에 대한 `email_template_id` 필드가 포함됩니다.

{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### 요청 본문
```
{
  "template_name": "email_template_name",
  "subject": "Welcome to my email template!",
  "body": "This is the text within my email body and https://www.braze.com/ here is a link to Braze.com.",
  "plaintext_body": "This is the text within my email body and here is a link to https://www.braze.com/.",
  "preheader": "My preheader is pretty cool."
}

```

#### 응답 예시
```
{
  "template_name": "email_template_name",
  "subject": "Welcome to my email template!",
  "body": "This is the text within my email body and https://www.braze.com/ here is a link to Braze.com.",
  "plaintext_body": "This is the text within my email body and here is a link to https://www.braze.com/.",
  "preheader": "My preheader is pretty cool."
}
```


#### 매개변수 세부 정보

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `modified_after`  | 아니요 | ISO 8601의 문자열 | 지정된 시간 또는 그 이후에 업데이트된 템플릿만 검색합니다. |
| `modified_before`  |  아니요 | ISO 8601의 문자열 | 지정된 시간 또는 그 이전에 업데이트된 템플릿만 검색합니다. |
| `limit` | 아니요 | 양수 | 검색할 템플릿의 최대 개수, 제공하지 않으면 기본값은 100이며 허용되는 최대 값은 1000입니다. |
| `offset`  |  아니요 | 양수 | 검색 기준에 맞는 나머지 템플릿을 반환하기 전에 건너뛸 템플릿의 수입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }


{% endapi %}
{% api %}
## 2 사용 가능한 이메일 템플릿 목록
{% apimethod get %}
/templates/email/list
{% endapimethod %}
{% apitags %}
가져오기, 이메일, 템플릿, 목록, REST
{% endapitags %}

다음 엔드포인트를 사용하여 사용 가능한 템플릿 목록을 가져옵니다.

{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### 요청 본문
```
GET https://YOUR_REST_API_URL/templates/email/list

{
  "count": number of templates returned
  "templates": [template with the following properties]:
    "email_template_id": (string) your email template's API Identifier,
    "template_name": (string) the name of your email template,
    "created_at": (string, in ISO 8601),
    "updated_at": (string, in ISO 8601)
}

```

#### 응답 예시
```
GET https://YOUR_REST_API_URL/templates/email/list

{
  "count": number of templates returned
  "templates": [template with the following properties]:
    "email_template_id": (string) your email template's API Identifier,
    "template_name": (string) the name of your email template,
    "created_at": (string, in ISO 8601),
    "updated_at": (string, in ISO 8601)
}
```


#### 매개변수 세부 정보

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `email_template_id`  | 예 | 문자열 | 이메일 템플릿의 API 식별자입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endapi %}


{% api %}
## 3 캠페인 트리거 전송
{% apimethod post %}campaigns/trigger/send{% endapimethod %}
{% apitags %}게시물, 캠페인, 트리거, 보내기{% endapitags %}

API 트리거 배달을 사용하면 메시지 콘텐츠를 Braze 대시보드 내에 보관하면서 API를 통해 메시지 전송 시기와 수신자를 지정할 수 있습니다. 

{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### 요청 본문
```
POST https://YOUR_REST_API_URL/campaigns/trigger/send
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "campaign_id": (required, string) see Campaign Identifier,
  "send_id": (optional, string) see Send Identifier,
  "trigger_properties": (optional, object) personalization key-value pairs that will apply to all users in this request,
  "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" is omitted,
  "audience": (optional, Connected Audience Object) see Connected Audience,
  // Including 'audience' will only send to users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to 'false', message will send to entire segment targeted by the campaign) [
    {
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, User Alias Object) User Alias of user to receive message,
      "external_user_id": (optional, string) External ID of user to receive message,
      "trigger_properties": (optional, object) personalization key-value pairs that will apply to this user (these key-value pairs will override any keys that conflict with the parent trigger_properties)
    },
    ...
  ]
}

```

#### 응답 예시
```
POST https://YOUR_REST_API_URL/canvas/trigger/send
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "canvas_id": (required, string) see Canvas Identifier,
  "canvas_entry_properties": (optional, object) personalization key-value pairs that will apply to all users in this request,
  "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" is omitted,
  "audience": (optional, Connected Audience Object) see Connected Audience,
  // Including 'audience' will only send to users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to 'false', message will send to the entire segment targeted by the Canvas) [
    {
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, User Alias Object) User Alias of user to receive message,
      "external_user_id": (optional, string) External ID of user to receive message,
      "canvas_entry_properties": (optional, object) personalization key-value pairs that will apply to this user (these key-value pairs will override any keys that conflict with the parent canvas_entry_properties)
    },
    ...
  ]
}
```


#### 매개변수 세부 정보

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `email_template_id`  | 예 | 문자열 | 이메일 템플릿의 API 식별자입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endapi %}


{% api %}
## 4 캠페인 트리거 전송
{% apimethod put %}사용자/트랙{% endapimethod %}
{% apitags %}PUT, 캠페인, 트리거, 전송{% endapitags %}

이 엔드포인트는 커스텀 이벤트, 사용자 속성 및 사용자 구매를 기록하는 데 사용할 수 있습니다. 요청당 최대 75개의 속성, 이벤트 및 구매 개체를 포함할 수 있습니다. 즉, 한 번에 최대 75명의 사용자에 대한 속성만 게시할 수 있지만 동일한 API 호출에서 최대 75개의 이벤트와 최대 75개의 구매도 제공할 수 있습니다.

{% apiref postman %}https://www.getpostman.com/ {% endapiref %}

#### 요청 본문
```
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
   "attributes" : (optional, array of Attributes Object),
   "events" : (optional, array of Event Object),
   "purchases" : (optional, array of Purchase Object)
}

```

#### 응답 예시
```
{
  // One of "external_id" or "user_alias" or "braze_id" is required
  "external_id" : (optional, string) see External User ID,
  "user_alias" : (optional, User Alias Object),
  "braze_id" : (optional, string) Braze User Identifier,
  // Setting this flag to true will put the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" mode is always true.
  "_update_existing_only" : (optional, boolean),
  // See note regarding anonymous push token imports
  "push_token_import" : (optional, boolean).
  // Braze User Profile Fields
  "first_name" : "Jon",
  "email" : "bob@example.com",
  // Custom Attributes
  "my_custom_attribute" : value,
  "my_custom_attribute_2" : {"inc" : int_value},
  "my_array_custom_attribute":[ "Value1", "Value2" ],
  // Adding a new value to an array custom attribute
  "my_array_custom_attribute" : { "add" : ["Value3"] },
  // Removing a value from an array custom attribute
  "my_array_custom_attribute" : { "remove" : [ "Value1" ]},
}
```

#### 매개변수 세부 정보

| 사용자 프로필 필드 | 데이터 유형 사양 |
| ---| --- |
| 국가 | (문자열) [ISO-3166-1 알파-2 표준][17]에 따라 국가 코드를 Braze에 전달해야 합니다. |
| current_location | (객체) {"longitude": -73.991443, "latitude": 40.753824} 형식 |
| date_of_first_session | (사용자가 앱을 처음 사용한 날짜) ISO 8601 형식 또는 `yyyy-MM-dd'T'HH:mm:ss:SSSZ` 형식의 문자열입니다. |
| date_of_last_session | (사용자가 마지막으로 앱을 사용한 날짜) ISO 8601 형식 또는 `yyyy-MM-dd'T'HH:mm:ss:SSSZ` 형식의 문자열입니다. |
| dob | (생년월일) 1980-12-21과 같이 "YYYY-MM-DD" 형식의 문자열입니다(예: 1980-12-21). |
| 이메일 | (문자열) |
| email_subscribe | (문자열) 사용 가능한 값은 "opted_in"(명시적으로 이메일 메시지를 수신하도록 등록), "unsubscribed"(명시적으로 이메일 메시지를 구독 취소) 및 "subscribed"(구독 취소도 옵트인하지도 않음)입니다.  |
| external_id | (문자열) 고유 사용자 식별자입니다. |
| Facebook | `id`(문자열), `likes`(문자열 배열), `num_friends`(정수) 중 하나를 포함하는 해시입니다. |
| first_name | (문자열) |
| 성별 | (문자열) "M", "F", "O"(기타), "N"(해당 없음), "P"(말하지 않음) 또는 nil(알 수 없음)입니다. |
| home_city | (문자열) |
| image_url | (문자열) 사용자 프로필과 연결할 이미지의 URL입니다. |
| 언어 | (문자열) [ISO-639-1 표준][24]의 언어를 Braze에 전달해야 합니다. <br>[허용되는 언어 목록][1]|
| last_name | (문자열) |
|marked_email_as_spam_at| (문자열) 사용자의 이메일이 스팸으로 표시된 날짜입니다. ISO 8601 형식 또는 yyyy-MM-dd'T'HH:mm:ss:SSSZ 형식으로 표시됩니다.|
| 전화 | (문자열) |
| push_subscribe | (문자열) 사용 가능한 값은 "opted_in"(푸시 메시지를 수신하도록 명시적으로 등록됨), "unsubscribed"(푸시 메시지를 명시적으로 구독 취소함), "subscribed"(구독 취소도 수신 동의도 아님) 등입니다.  |
| push_tokens | `app_id` 및 `token` 문자열이 포함된 객체 배열입니다. 선택적으로 이 토큰이 연결된 기기에 `device_id`를 제공할 수 있습니다(예: `[{"app_id": App Identifier, "token": "abcd", "device_id": "optional_field_value"}]`). `device_id`를 제공하지 않으면 무작위로 생성됩니다. |
| time_zone | (문자열) IANA 표준 시간대 데이터베이스][26]의 표준 시간대 이름(예: "미국/뉴욕" 또는 "동부 표준시(미국 및 캐나다)"). 유효한 표준 시간대 값만 설정됩니다. |
| 트위터 | `id`(정수), `screen_name`(문자열, X(옛 트위터) 핸들), `followers_count`(정수), `friends_count`(정수), `statuses_count`(정수) 중 하나를 포함하는 해시입니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}

[1]: /docs/user_guide/data_and_analytics/user_data_collection/language_codes/
