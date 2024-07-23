---
nav_title: "사용자 속성 개체"
article_title: API 사용자 속성 개체
page_order: 11
page_type: reference
description: "이 참조 문서에서는 사용자 속성 개체의 다양한 구성 요소에 대해 설명합니다."

---

# 사용자 속성 개체

> 속성 객체에 필드가 있는 API 요청은 지정된 고객 프로필에 지정된 값으로 해당 이름의 속성을 만들거나 업데이트합니다. 

대시보드의 사용자 프로필에서 이러한 특수 값을 업데이트하거나 사용자에 대한 사용자 지정 속성 데이터를 추가하려면 Braze 사용자 프로필 필드 이름(아래와 같이 나열되거나 [Braze 사용자 프로필 필드][27] 섹션에 나열된 것)을 사용하세요.

## 개체 본문

```json
{
  // One of "external_id" or "user_alias" or "braze_id" or "email" is required
  "external_id" : (optional, string) see external user ID,
  "user_alias" : (optional, User alias object),
  "braze_id" : (optional, string) Braze user identifier,
  "email": (optional, string) User email address,
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

프로필 속성을 제거하려면 `null` 로 설정합니다. `external_id` 및 `user_alias` 같은 일부 필드는 고객 프로필에 추가한 후에는 제거할 수 없습니다.

#### 기존 프로필만 업데이트

Braze에서 기존 고객 프로필만 업데이트하려면 요청 본문에 `true` 값과 함께 `_update_existing_only` 키를 전달해야 합니다. 이 값을 생략하면 `external_id` 주소가 없는 경우 Braze에서 새 고객 프로필을 생성합니다.

{% alert note %}
`/users/track` 엔드포인트를 통해 별칭 전용 고객 프로필을 만드는 경우 `_update_existing_only`를 `false`로 설정해야 합니다. 이 값을 생략하면 별칭 전용 프로필이 생성되지 않습니다.
{% endalert %}

#### 푸시 토큰 가져오기

Braze로 푸시 토큰을 가져오기 전에 필요한지 다시 확인하세요. Braze SDK를 설치하면 API를 통해 푸시 토큰을 업로드할 필요 없이 자동으로 푸시 토큰을 처리합니다.

API를 통해 업로드해야 하는 경우, 식별된 사용자 또는 익명 사용자를 위해 업로드할 수 있습니다. 즉, `external_id`가 존재하거나 익명 사용자의 `push_token_import` 플래그가 `true`로 설정되어 있어야 합니다. 

{% alert note %}
다른 시스템에서 푸시 토큰을 가져올 때 `external_id`를 항상 사용할 수 있는 것은 아닙니다. Braze로 전환하는 동안 이러한 사용자와의 커뮤니케이션을 유지하려면 `push_token_import`를 `true`로 지정하여 `external_id`를 제공하지 않고 익명 사용자의 레거시 토큰을 가져올 수 있습니다.
{% endalert %}

`push_token_import` 를 `true` 로 지정하는 경우:

* `external_id` 및 `braze_id`를 지정해서는 **안됩니다**
* 속성 객체에는 푸시 토큰이 **포함되어야** 합니다.
* 토큰이 이미 Braze에 존재하는 경우 요청은 무시되며, 그렇지 않으면 Braze는 각 토큰에 대해 임시 익명 고객 프로필을 생성하여 해당 개인에게 계속 메시지를 보낼 수 있도록 합니다

가져온 후, 각 사용자가 Braze 지원 버전의 앱을 실행하면 Braze는 가져온 푸시 토큰을 자동으로 Braze 고객 프로필로 이동하고 임시 프로필을 정리합니다.

Braze는 한 달에 한 번씩 푸시 토큰이 없으며 `push_token_import` 플래그가 있는 익명 프로필을 확인합니다. 익명 프로필에 더 이상 푸시 토큰이 없는 경우 해당 프로필을 삭제합니다. 그러나 익명 프로필에 푸시 토큰이 남아 있어 실제 사용자가 아직 해당 푸시 토큰으로 기기에 로그인하지 않았다는 것을 암시하는 경에는 아무 조치도 취하지 않습니다.

자세한 내용은 [푸시 토큰 마이그레이션][3]을 참조하세요.

#### 사용자 지정 속성 데이터 유형

사용자 지정 속성으로 저장할 수 있는 데이터 유형은 다음과 같습니다:

| 데이터 유형 | 참고 사항
| --- | --- |
| 배열 > 사용자 지정 속성 배열은 1차원 집합이며, 다차원 배열은 지원되지 않습니다. 사용자 지정 속성 배열에 요소를 추가하면 해당 요소가 이미 존재하지 않는 한 배열의 끝에 추가되며, 이 경우 현재 위치에서 배열의 끝으로 이동합니다.<br><br>예를 들어 `['hotdog','hotdog','hotdog','pizza']` 배열을 가져온 경우 고유 값만 지원되므로 배열 속성에 `['hotdog', 'pizza']`로 표시됩니다.<br><br>`"my_array_custom_attribute":[ "Value1", "Value2" ]`와 같이 배열의 값을 설정하는 것 외에도 `"my_array_custom_attribute" : { "add" : ["Value3"] },` 과 같이 기존 배열에 추가하거나 `"my_array_custom_attribute" : { "remove" : [ "Value1" ]}`과 같이 배열에서 값을 제거할 수 있습니다<br><br>커스텀 속성 배열의 최대 요소 개수는 기본값이 25개이지만 개별 배열의 경우 최대 100개까지 늘릴 수 있습니다. 자세한 내용은 [배열][6]을 참조하세요. |
| 부울 | `true` 또는 `false` |
| 날짜 | [ISO 8601][19] 형식 또는 다음 형식 중 하나로 저장해야 합니다: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` <br><br>'T'는 자리 표시자가 아닌 시간 지정자이므로 변경하거나 제거해서는 안 됩니다. <br><br>표준 시간대가 없는 시간 속성은 기본값이 자정(UTC)으로 설정됩니다(대시보드에서 회사 표준 시간대의 자정에 해당하는 시간으로 형식이 지정됨). <br><br> 향후 타임스탬프가 있는 이벤트는 기본적으로 현재 시간으로 설정됩니다. <br><br> 일반 커스텀 속성의 경우, 연도가 0보다 작거나 3000보다 크면 Braze는 이 값을 사용자에게 문자열로 저장합니다. |
| 플로트 | |
| 정수 > 정수 > 정수 사용자 지정 속성은 "inc" 필드와 증가시킬 값을 가진 개체를 할당하여 양수 또는 음수 정수로 증가시킬 수 있습니다. <br><br>예시: `"my_custom_attribute_2" : {"inc" : int_value},`|
| Strings |  |
{: .reset-td-br-1 .reset-td-br-2}

사용자 지정 이벤트와 사용자 지정 속성을 언제 사용해야 하는지에 대한 자세한 내용은 사용자 지정 [이벤트]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) 및 [사용자]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/) 지정 속성에 대한 각 문서를 참조하세요.

#### Braze 고객 프로필 필드 {#braze-user-profile-fields}

{% alert important %}
다음 고객 프로필 필드는 대소문자를 구분하므로 소문자로 참조하세요.
{% endalert %}

| 사용자 프로필 필드 > 데이터 유형 사양 >
| ---| --- |
| alias\_name | (문자열) |
| alias\_label | (문자열) |
| braze\_id | (문자열, 선택 사항) SDK를 통해 고객 프로필이 인식되면 연결된 `braze_id`와 연결된 익명 고객 프로필이 생성됩니다. `braze_id` 주소는 Braze에서 자동으로 할당되며, 편집할 수 없고 기기별로 다릅니다. |
| 국가 | (문자열) [ISO-3166-1 알파-2 표준에][17] 따라 국가 코드를 Braze에 전달해야 합니다. 저희 API는 다양한 형식으로 수신된 국가를 매핑하기 위해 최선을 다할 것입니다. 예를 들어 '오스트레일리아'는 'AU'로 매핑될 수 있습니다. 그러나 입력값이 지정된 [ISO-3166-1 alpha-2 표준][17]과 일치하지 않으면 국가 값이 `NULL`로 설정됩니다. <br><br>CSV 가져오기 또는 API를 통해 사용자에 대해 `country`를 설정하면 Braze가 SDK를 통해 이 정보를 자동으로 캡처하지 못합니다. |
| current\_location | {"longitude": -73.991443, "latitude": 40.753824} 형태의 (객체) |
| date\_of\_first\_session | (사용자가 앱을 처음 사용한 날짜) ISO 8601 형식 또는 다음 형식 중 하나의 문자열입니다. <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` |
| date\_of\_last\_session | (사용자가 마지막으로 앱을 사용한 날짜) ISO 8601 형식 또는 다음 형식 중 하나의 문자열입니다. <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` |
| dob | (생년월일) 형식의 문자열(예: 1980-12-21). |
| 이메일 | (문자열) |
| email\_subscribe | (문자열) 사용 가능한 값은 "opted\_in"(명시적으로 이메일 메시지를 수신하도록 등록), "unsubscribed"(명시적으로 이메일 메시지를 구독 취소) 및 "subscribed"(구독 취소도 옵트인하지도 않음)입니다.  |
| email\_open\_tracking\_disabled |(boolean) `true` 또는 `false` 허용됨. 이 사용자에게 향후 전송되는 모든 이메일에 열린 추적 픽셀이 추가되지 않도록 하려면 `true`로 설정합니다.|
| email\_open\_tracking\_disabled |(boolean) `true` 또는 `false` 허용됨. 이 사용자에게 전송되는 향후 이메일 내의 모든 링크에 대한 클릭 추적을 사용하지 않으려면 `true` 으로 설정합니다.
| external\_id | (문자열) 고객 프로필의 고유 식별자입니다. `external_id`를 할당하면 고객 프로필이 사용자의 모든 기기에서 식별됩니다. 알 수 없는 사용자 프로필에 external\_id를 처음 할당하는 경우 모든 기존 사용자 프로필 데이터가 새 사용자 프로필로 마이그레이션됩니다. |
| facebook | `id`(문자열), `likes`(문자열의 배열), `num_friends`(정수) 중 하나를 포함하는 해시입니다. |
| first\_name | (string) |
| 성별 | (문자열) "M", "F", "O"(기타), "N"(해당 없음), "P"(말하지 않음) 또는 nil(알 수 없음). |
| home\_city | (string) |
| 언어 | (문자열) [ISO-639-1 표준][24]의 언어를 Braze에 전달해야 합니다. 지원되는 언어에 대해서는 [허용되는 언어 목록을][2] 참조하세요.<br><br>CSV 가져오기 또는 API를 통해 사용자에 대해 `language`를 설정하면 Braze가 SDK를 통해 이 정보를 자동으로 캡처하지 못합니다. |
| last\_name | (string) |
| marked\_email\_as\_spam\_at | (문자열) 사용자의 이메일이 스팸으로 표시된 날짜입니다. ISO 8601 형식 또는 다음 형식 중 하나로 표시됩니다: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` |
| 전화 | (문자열) | 
| push\_subscribe | (문자열) 사용 가능한 값은 "opted\_in"(푸시 메시지를 수신하도록 명시적으로 등록됨), "unsubscribed"(푸시 메시지를 명시적으로 구독 취소함), "subscribed"(구독 취소도 수신 동의도 아님) 등입니다.  |
| push\_tokens | `app_id` 및 `token` 문자열이 포함된 객체 배열입니다. 선택적으로 이 토큰이 연결된 기기에 `device_id`를 제공할 수 있습니다(예: `[{"app_id": App Identifier, "token": "abcd", "device_id": "optional_field_value"}]`). `device_id`를 제공하지 않으면 무작위로 생성됩니다. |
| subscription\_groups| `subscription_group_id` 및 `subscription_state` 문자열이 포함된 개체 배열(예: `[{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed"}]`) . `subscription_state`에 사용할 수 있는 값은 "구독" 및 "구독 취소"입니다.|
| time\_zone | (문자열) [IANA 표준 시간대 데이터베이스][26]의 표준 시간대 이름(예: "미국/뉴욕" 또는 "동부 표준시(미국 및 캐나다)"). 유효한 표준 시간대 값만 설정됩니다. |
| twitter | `id`(정수), `screen_name`(문자열, X(옛 트위터) 핸들), `followers_count`(정수), `friends_count`(정수), `statuses_count`(정수) 중 하나를 포함하는 해시입니다. |
{: .reset-td-br-1 .reset-td-br-2}

이 API를 통해 명시적으로 설정된 언어 값은 Braze가 기기에서 자동으로 수신하는 로캘 정보보다 우선합니다.

####  사용자 속성 예제 요청

이 예제에는 API 호출당 75개의 요청이 허용되는 두 개의 사용자 속성 객체가 포함되어 있습니다.

\`\`\`json
POST https://YOUR_REST_API_URL/users/track
콘텐츠-유형: application/json
권한 부여: 무기명 YOUR-REST-API-KEY
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
\`\`\`

[2]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/language_codes/
[3]: {{site.baseurl}}/help/help_articles/push/push_token_migration/
[6]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#arrays
[15]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/
[17]: http://en.wikipedia.org/wiki/ISO_3166-1 "ISO-3166-1 코드"
[19]: http://en.wikipedia.org/wiki/ISO_8601 "ISO 8601 타임코드 위키"
[24]: http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes "ISO-639-1 코드"
[26]: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
[27]: #braze-user-profile-fields
