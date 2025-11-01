---
nav_title: "사용자 속성 개체"
article_title: API 사용자 속성 개체
page_order: 11
page_type: reference
description: "이 참조 문서에서는 사용자 속성 개체의 다양한 구성 요소에 대해 설명합니다."

---

# 사용자 속성 개체

> 속성 객체에 필드가 있는 API 요청은 지정된 사용자 프로필에 지정된 값으로 해당 이름의 속성을 만들거나 업데이트합니다. 

대시보드의 사용자 프로필에서 이러한 특수 값을 업데이트하거나 사용자에 대한 사용자 지정 속성 데이터를 추가하려면 Braze 사용자 프로필 필드 이름(아래와 같이 나열되거나 [Braze 사용자 프로필 필드](#braze-user-profile-fields) 섹션에 나열된 것)을 사용하세요.

## 개체 본문

```json
{
  // One of "external_id" or "user_alias" or "braze_id" or "email" or "phone" is required
  "external_id" : (optional, string) see external user ID,
  "user_alias" : (optional, User alias object),
  "braze_id" : (optional, string) Braze user identifier,
  "email": (optional, string) User email address,
  "phone": (optional, string) User phone number,
  // Setting this flag to true will put the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" defaults to true.
  "_update_existing_only" : (optional, boolean),
  // See note regarding anonymous push token imports
  "push_token_import" : (optional, boolean),
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

- [외부 사용자 ID]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields)
- [사용자 별칭]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)

프로필 속성을 제거하려면 `null` 로 설정합니다. `external_id` 및 `user_alias` 같은 일부 필드는 사용자 프로필에 추가한 후에는 제거할 수 없습니다.

#### 기존 프로필만 업데이트

Braze에서 기존 사용자 프로필만 업데이트하려면 요청 본문에 `true` 값과 함께 `_update_existing_only` 키를 전달해야 합니다. 이 값을 생략하면 `external_id` 주소가 없는 경우 Braze에서 새 사용자 프로필을 생성합니다.

{% alert note %}
`/users/track` 엔드포인트를 통해 별칭 전용 사용자 프로필을 만드는 경우 `_update_existing_only` 을 `false` 으로 설정해야 합니다. 이 값을 생략하면 별칭 전용 프로필이 생성되지 않습니다.
{% endalert %}

#### 푸시 토큰 가져오기

Braze로 푸시 토큰을 가져오기 전에 필요한지 다시 확인하세요. Braze SDK를 설치하면 API를 통해 푸시 토큰을 업로드할 필요 없이 자동으로 푸시 토큰을 처리합니다.

API를 통해 업로드해야 하는 경우, 식별된 사용자 또는 익명 사용자를 위해 업로드할 수 있습니다. 즉, `external_id`가 존재하거나 익명 사용자의 `push_token_import` 플래그가 `true`로 설정되어 있어야 합니다. 

{% alert note %}
다른 시스템에서 푸시 토큰을 가져올 때 `external_id`를 항상 사용할 수 있는 것은 아닙니다. Braze로 전환하는 동안 이러한 사용자와의 커뮤니케이션을 유지하려면 `push_token_import` 을 `true` 로 지정하여 `external_id` 을 제공하지 않고 익명 사용자의 레거시 토큰을 가져올 수 있습니다.
{% endalert %}

`push_token_import` 를 `true` 로 지정하는 경우:

* `external_id` 및 `braze_id` 을 지정해서는 **안됩니다**.
* 속성 객체에는 푸시 토큰이 **포함되어야 합니다.** 
* 토큰이 이미 Braze에 존재하는 경우 요청은 무시되며, 그렇지 않으면 각 토큰에 대해 임시 익명 사용자 프로필을 생성하여 해당 개인에게 계속 메시지를 보낼 수 있도록 합니다.

가져온 후, 각 사용자가 Braze 지원 버전의 앱을 실행하면 Braze는 가져온 푸시 토큰을 자동으로 Braze 사용자 프로필로 이동하고 임시 프로필을 정리합니다.

Braze는 한 달에 한 번씩 푸시 토큰이 없으며 `push_token_import` 플래그가 있는 익명 프로필을 확인합니다. 익명 프로필에 더 이상 푸시 토큰이 없는 경우 해당 프로필을 삭제합니다. 그러나 익명 프로필에 푸시 토큰이 남아 있어 실제 사용자가 아직 해당 푸시 토큰으로 디바이스에 로그인하지 않았다는 것을 암시하는 경우에는 아무 조치도 취하지 않습니다.

자세한 내용은 [푸시 토큰 마이그레이션하기를](#migrating-push-tokens) 참조하세요.

#### 사용자 지정 속성 데이터 유형

사용자 지정 속성으로 저장할 수 있는 데이터 유형은 다음과 같습니다:

| 데이터 유형 | 참고 |
| --- | --- |
| 배열 | 사용자 지정 속성 배열이 지원됩니다. 사용자 지정 속성 배열에 요소를 추가하면 해당 요소가 이미 존재하지 않는 한 배열의 끝에 추가되며, 이 경우 현재 위치에서 배열의 끝으로 이동합니다.<br><br>예를 들어 `['hotdog','hotdog','hotdog','pizza']` 배열을 가져온 경우 고유 값만 지원되므로 배열 속성에 `['hotdog', 'pizza']`로 표시됩니다.<br><br>`"my_array_custom_attribute":[ "Value1", "Value2" ]` 와 같이 배열의 값을 설정하는 것 외에도 `"my_array_custom_attribute" : { "add" : ["Value3"] },` 와 같이 기존 배열에 추가하거나 다음과 같이 배열에서 값을 제거할 수 있습니다. `"my_array_custom_attribute" : { "remove" : [ "Value1" ]}`<br><br>커스텀 속성 배열의 최대 요소 개수는 기본값이 25개이지만 개별 배열의 경우 최대 100개까지 늘릴 수 있습니다. 자세한 내용은 [배열을]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays) 참조하세요. |
| 객체 배열 | 객체 배열을 사용하면 각 객체에 속성 집합이 포함된 객체 목록을 정의할 수 있습니다. 호텔 숙박, 구매 내역, 환경 설정 등 사용자에 대한 여러 관련 데이터 집합을 저장해야 하는 경우 유용합니다. <br><br> 예를 들어 `hotel_stays` 라는 사용자 프로필에 사용자 지정 속성을 정의할 수 있습니다. 이 사용자 지정 속성은 `hotel_name`, `check_in_date`, `nights_stayed` 과 같은 속성을 사용하여 각 개체가 별도의 숙박을 나타내는 배열로 정의할 수 있습니다. 자세한 내용은 [이 예시를](#array-of-objects-example) 참조하세요. |
| 부울 | `true` 또는 `false` |
| 날짜 | [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) 형식 또는 다음 형식 중 하나로 저장해야 합니다: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` <br><br>'T'는 자리 표시자가 아닌 시간 지정자이므로 변경하거나 제거해서는 안 됩니다. <br><br>표준 시간대가 없는 시간 속성은 기본값이 자정(UTC)으로 설정됩니다(대시보드에서 회사 표준 시간대의 자정에 해당하는 시간으로 형식이 지정됨). <br><br> 향후 타임스탬프가 있는 이벤트는 기본적으로 현재 시간으로 설정됩니다. <br><br> 일반 사용자 지정 속성의 경우, 연도가 0보다 작거나 3000보다 크면 Braze는 이 값을 사용자에게 문자열로 저장합니다. |
| 플로트 | 플로트 사용자 지정 속성은 소수점이 있는 양수 또는 음수입니다. 예를 들어 플로트를 사용하여 제품이나 서비스에 대한 계정 잔액이나 사용자 평점을 저장할 수 있습니다. |
| 정수 | 정수 사용자 지정 속성은 'inc' 필드와 증가시킬 값을 가진 객체를 할당하여 양수 또는 음수 정수로 증가시킬 수 있습니다. <br><br>예시: `"my_custom_attribute_2" : {"inc" : int_value},`|
| Nested custom attributes | 중첩된 사용자 지정 속성은 속성 집합을 다른 속성의 속성으로 정의합니다. 사용자 지정 속성 개체를 정의할 때 해당 개체에 대한 추가 속성 집합을 정의합니다. 자세한 내용은 [중첩 커스텀 속성]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/)을 참조하세요. |
| 문자열 | 문자열 사용자 지정 속성은 텍스트 데이터를 저장하는 데 사용되는 문자 시퀀스입니다. 예를 들어 문자열을 사용하여 이름과 성, 이메일 주소 또는 환경설정을 저장할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
사용자 지정 이벤트와 사용자 지정 속성을 언제 사용해야 하는지에 대한 자세한 내용은 [사용자 지정 이벤트]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) 및 [사용자 지정 속성에]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) 대한 각 문서를 참조하세요.
{% endalert %}

##### 객체 배열 예시 

이 개체 배열을 사용하면 숙박 내 특정 기준에 따라 세그먼트를 생성하고 Liquid 템플릿으로 각 숙박의 데이터를 사용하여 메시지를 개인화할 수 있습니다.

```json
"hotel_stays": [
  { "hotel_name": "Ocean View Resort", "check_in_date": "2023-06-15", "nights_stayed": 5 },
  { "hotel_name": "Mountain Lodge", "check_in_date": "2023-09-10", "nights_stayed": 3 }
  ]
```

#### 브레이즈 사용자 프로필 필드 {#braze-user-profile-fields}

{% alert important %}
다음 사용자 프로필 필드는 대소문자를 구분하므로 소문자로 참조하세요.
{% endalert %}

| 사용자 프로필 필드 | 데이터 유형 사양 |
| ---| --- |
| alias_name | (문자열) |
| alias_label | (문자열) |
| braze_id | (문자열, 선택 사항) SDK에서 사용자 프로필을 인식하면 연결된 `braze_id` 으로 익명 사용자 프로필이 생성됩니다. `braze_id` 주소는 Braze에서 자동으로 할당되며, 편집할 수 없고 기기별로 다릅니다. | 
| 국가 | (문자열) [ISO-3166-1 알파-2 표준에](http://en.wikipedia.org/wiki/ISO_3166-1) 따라 국가 코드를 Braze에 전달해야 합니다. 저희 API는 다양한 형식으로 수신된 국가를 매핑하기 위해 최선을 다할 것입니다. 예를 들어 '오스트레일리아'는 'AU'로 매핑될 수 있습니다. 그러나 입력값이 지정된 [ISO-3166-1 alpha-2 표준](http://en.wikipedia.org/wiki/ISO_3166-1)과 일치하지 않으면 국가 값이 `NULL`로 설정됩니다. <br><br>CSV 가져오기 또는 API를 통해 사용자에 대해 `country` 을 설정하면 Braze가 SDK를 통해 이 정보를 자동으로 캡처하지 못합니다. |
| current_location | (객체) 형식 {"longitude": -73.991443, "latitude": 40.753824} |
| date_of_first_session | (사용자가 앱을 처음 사용한 날짜) ISO 8601 형식 또는 다음 형식 중 하나의 문자열입니다: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` |
| date_of_last_session | (사용자가 마지막으로 앱을 사용한 날짜) ISO 8601 형식 또는 다음 형식 중 하나의 문자열입니다: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY`  |
| dob | (생년월일) 1980-12-21과 같이 "YYYY-MM-DD" 형식의 문자열입니다(예: 1980-12-21). |
| 이메일 | (문자열) |
| email_subscribe | (문자열) 사용 가능한 값은 "opted_in"(명시적으로 이메일 메시지를 수신하도록 등록), "unsubscribed"(명시적으로 이메일 메시지를 구독 취소), 및 "subscribed"(구독 취소도 옵트인하지도 않음)입니다.  |
| email_open_tracking_disabled |(부울) `true` 또는 `false` 허용됨. 이 사용자에게 향후 전송되는 모든 이메일에 열린 추적 픽셀이 추가되지 않도록 하려면 `true` 으로 설정합니다. SparkPost 및 SendGrid에서만 사용할 수 있습니다.|
| email_click_tracking_disabled |(부울) `true` 또는 `false` 허용됨. 이 사용자에게 전송되는 향후 이메일 내의 모든 링크에 대한 클릭 추적을 사용하지 않으려면 `true` 으로 설정합니다. SparkPost 및 SendGrid에서만 사용할 수 있습니다.|
| external_id | (문자열) 사용자 프로필의 고유 식별자입니다. `external_id`를 할당하면 고객 프로필이 사용자의 모든 기기에서 식별됩니다. 알 수 없는 사용자 프로필에 external_id를 처음 할당하는 경우 기존의 모든 사용자 프로필 데이터가 새 사용자 프로필로 마이그레이션됩니다. |
| Facebook | `id`(문자열), `likes`(문자열 배열), `num_friends`(정수) 중 하나를 포함하는 해시입니다. |
| first_name | (문자열) |
| 성별 | (문자열) "M", "F", "O"(기타), "N"(해당 없음), "P"(말하지 않음) 또는 nil(알 수 없음)입니다. |
| home_city | (문자열) |
| language | (문자열)의 경우 [ISO-639-1 표준에](http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) 따라 해당 언어가 Braze에 전달되어야 합니다. 지원되는 언어에 대해서는 [허용되는 언어 목록을]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/language_codes/) 참조하세요.<br><br>CSV 가져오기 또는 API를 통해 사용자에 대해 `language` 을 설정하면 Braze가 SDK를 통해 이 정보를 자동으로 캡처하지 못합니다. |
| last_name | (문자열) |
| marked_email_as_spam_at | (문자열) 사용자의 이메일이 스팸으로 표시된 날짜입니다. ISO 8601 형식 또는 다음 형식 중 하나로 표시됩니다: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` |
| 전화 | (문자열) 전화 번호를 [E.164](https://en.wikipedia.org/wiki/E.164) 형식으로 제공하는 것이 좋습니다. 자세한 내용은 [사용자 전화번호를]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#formatting) 참조하세요.|
| push_subscribe | (문자열) 사용 가능한 값은 "opted_in"(푸시 메시지를 수신하도록 명시적으로 등록됨), "unsubscribed"(푸시 메시지를 명시적으로 구독 취소함), 및 "subscribed"(구독 취소도 수신 동의도 아님)입니다.  |
| push_tokens | `app_id` 및 `token` 문자열이 포함된 객체 배열입니다. 선택적으로 이 토큰이 연결된 기기에 `device_id`를 제공할 수 있습니다(예: `[{"app_id": App Identifier, "token": "abcd", "device_id": "optional_field_value"}]`). `device_id`를 제공하지 않으면 무작위로 생성됩니다. |
| subscription_groups| `subscription_group_id` 및 `subscription_state` 문자열이 포함된 객체 배열(예: `[{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed"}]`) . `subscription_state` 에 사용할 수 있는 값은 "구독" 및 "구독 취소"입니다.|
| time_zone | (문자열) [IANA 표준 시간대 데이터베이스](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)의 표준 시간대 이름(예: "America/New_York" 또는 "동부 표준시(미국 & 캐나다)"). 유효한 표준 시간대 값만 설정됩니다. |
| 트위터 | `id`(정수), `screen_name`(문자열, X(옛 트위터) 핸들), `followers_count`(정수), `friends_count`(정수), `statuses_count`(정수) 중 하나를 포함하는 해시입니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

이 API를 통해 명시적으로 설정된 언어 값은 Braze가 기기에서 자동으로 수신하는 로캘 정보보다 우선합니다.

####  사용자 속성 예제 요청

이 예시에는 API 호출당 허용되는 총 75개의 속성 개체 중 4개의 사용자 속성 개체가 포함되어 있습니다.

```json
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "attributes" : [
    {
      "external_id" : "user1",
      "first_name" : "Jon",
      "has_profile_picture" : true,
      "dob": "1988-02-14",
      "music_videos_favorited" : { "add" : [ "calvinharris-summer" ], "remove" : ["nickiminaj-anaconda"] }
    },
    {
      "external_id" : "user2",
      "first_name" : "Jill",
      "has_profile_picture" : false,
      "push_tokens": [{"app_id": "Your App Identifier", "token": "abcd", "device_id": "optional_field_value"}]

    },
    {
      "user_alias" : { "alias_name" : "device123", "alias_label" : "my_device_identifier"},
      "first_name" : "Alice",
      "has_profile_picture" : false
    },
    {
      "external_id": "user3",
      "subscription_groups" : [{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed"}]
    }
  ]
}
```

## 푸시 토큰 마이그레이션

Braze를 통합하기 전에 자체적으로 또는 다른 제공업체를 통해 푸시 알림을 보내고 있었다면, 푸시 토큰 마이그레이션을 통해 등록된 푸시 토큰으로 사용자에게 푸시 알림을 계속 보낼 수 있습니다.

### SDK를 통한 자동 마이그레이션

[Braze SDK를 통합한]({{site.baseurl}}/developer_guide/sdk_integration/) 후에는 옵트인한 사용자의 푸시 토큰이 다음에 앱을 열 때 자동으로 마이그레이션됩니다. 그때까지는 해당 사용자에게 Braze를 통해 푸시 알림을 보낼 수 없습니다.

또는 [푸시 토큰을 수동으로 마이그레이션하여](#manual-migration-via-api) 사용자의 재참여를 더욱 신속하게 유도할 수 있습니다.

#### 웹 토큰 고려 사항

웹 푸시 토큰의 특성상 웹용 푸시를 구현할 때 다음 사항을 고려해야 합니다:

|Consideration|세부 정보|
|----------------------|------------|
| **서비스 작업자**  | `manageServiceWorkerExternally` 또는 `serviceWorkerLocation` 와 같은 다른 옵션을 지정하지 않는 한 기본적으로 웹 SDK는 `./service-worker` 에서 서비스 워커를 찾습니다 . 서비스 워커가 제대로 설정되어 있지 않으면 사용자의 푸시 토큰이 만료될 수 있습니다. |
| **만료된 토큰**   | 사용자가 60일 이내에 웹 세션을 시작하지 않으면 푸시 토큰이 만료됩니다. Braze는 만료된 푸시 토큰을 마이그레이션할 수 없으므로, 다시 참여하려면 [푸시 프라이머를]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages) 보내야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### API를 통한 수동 마이그레이션

수동 푸시 토큰 마이그레이션은 API를 통해 이전에 생성한 키를 Braze 플랫폼으로 가져오는 프로세스입니다.

[`users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)를 사용하여 프로그래밍 방식으로 iOS(APN) 및 Android(FCM) 토큰을 플랫폼으로 마이그레이션합니다. 식별된 사용자(연결된 외부 ID가 있는 사용자)와 익명 사용자(외부 ID가 없는 사용자)를 모두 마이그레이션할 수 있습니다.

푸시 토큰 마이그레이션 중에 앱의 `app_id`를 지정하여 적절한 푸시 토큰을 적절한 앱에 연결합니다. 각 앱(iOS, Android 등)에는 [API 키]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) 페이지의 **식별** 섹션에서 찾을 수 있는 고유한 `app_id` 이 있습니다. 올바른 플랫폼의 `app_id` 을 사용해야 합니다.

{% alert important %}
API를 통해 웹 푸시 토큰을 마이그레이션하는 것은 불가능합니다. 이는 웹 푸시 토큰이 다른 플랫폼과 동일한 스키마를 따르지 않기 때문입니다. 

<br>프로그래밍 방식으로 웹 푸시 토큰을 마이그레이션하려는 경우 `Received '400: Invalid subscription auth' sending to 'https://fcm.googleapis.com/fcm/send` 오류가 표시될 수 있습니다.

<br>
API 마이그레이션의 대안으로 SDK를 통합하여 토큰 기반이 자연스럽게 다시 채워질 수 있도록 하는 것이 좋습니다.
{% endalert %}

{% tabs local %}
{% tab External ID present %}
식별된 사용자의 경우 `push_token_import` 플래그를 `false`로 설정(또는 매개변수 생략)하고 사용자 `attributes` 오브젝트에 `external_id`, `app_id`, `token` 값을 지정합니다. 

For example:

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "attributes" : [
    {
      "push_token_import" : false,
      "external_id": "example_external_id",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING"}
      ]
    }
  ]
}'
```
{% endtab %}

{% tab External ID missing %}
다른 시스템에서 푸시 토큰을 가져올 때 `external_id`를 항상 사용할 수 있는 것은 아닙니다. 이 경우 `push_token_import` 플래그를 `true`로 설정하고 `app_id` 및 `token` 값을 지정합니다. Braze는 각 토큰에 대해 임시 익명 고객 프로필을 생성하여 이러한 개인에게 계속 메시지를 보낼 수 있도록 합니다. 토큰이 이미 Braze에 존재하는 경우 요청은 무시됩니다.

For example:

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "attributes": [ 
    {
      "push_token_import" : true,
      "email": "braze.test1@testbraze.com",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING", "device_id": "DEVICE_ID"}
      ]
    },
      
    {
      "push_token_import" : true,
      "email": "braze.test2@testbraze.com",
      "country": "US",
      "language": "en",
      "YOUR_CUSTOM_ATTRIBUTE_1": "YOUR_VALUE",
      "YOUR_CUSTOM_ATTRIBUTE_2": "YOUR_VALUE",
      "push_tokens": [
        {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING", "device_id": "DEVICE_ID"}  
      ]
    }
  ]
}'
```

가져온 후 익명 사용자가 Braze 지원 버전의 앱을 실행하면, Braze는 가져온 푸시 토큰을 자동으로 Braze 고객 프로필로 이동하고 임시 프로필을 정리합니다.

Braze는 한 달에 한 번씩 푸시 토큰이 없으며 `push_token_import` 플래그가 있는 익명 프로필을 확인합니다. 익명 프로필에 더 이상 푸시 토큰이 없는 경우 해당 프로필을 삭제합니다. 그러나 익명 프로필에 푸시 토큰이 남아 있어 실제 사용자가 아직 해당 푸시 토큰으로 기기에 로그인하지 않았다는 것을 암시하는 경에는 아무 조치도 취하지 않습니다.
{% endtab %}
{% endtabs %}

### Android 푸시 토큰 가져오기

{% alert important %}
다음 고려 사항은 Android 앱에만 적용됩니다. iOS 앱에는 푸시 표시를 위한 프레임워크가 하나만 있으며, Braze에 필요한 푸시 토큰과 인증서가 있는 한 푸시 알림이 즉시 렌더링되므로 이러한 단계가 필요하지 않습니다.
{% endalert %}

Braze SDK 통합이 완료되기 전에 사용자에게 Android 푸시 알림을 보내야 하는 경우 키-값 페어를 사용하여 푸시 알림의 유효성을 검사하세요. 

푸시 페이로드를 처리하고 표시하려면 수신기가 있어야 합니다. 수신자에게 푸시 페이로드를 알리려면 푸시 캠페인에 필요한 키-값 쌍을 추가합니다. 이 쌍의 값은 Braze 이전에 사용한 특정 푸시 파트너에 따라 달라집니다.

{% alert note %}
일부 푸시 알림 제공업체의 경우, Braze가 키-값 페어를 올바르게 해석할 수 있도록 평평하게 만들어야 합니다. 특정 Android 앱의 키-값 쌍을 평평하게 하려면 고객 성공 관리자에게 문의하세요.
{% endalert %}