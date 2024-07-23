---
nav_title: "POST: 식별자로 사용자 프로필 내보내기"
article_title: "POST: 식별자로 사용자 프로필 내보내기"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 식별자 Braze 엔드포인트로 사용자 내보내기에 대한 세부 정보를 간략하게 설명합니다."

---
{% api %}
# 식별자로 사용자 프로필 내보내기
{% apimethod post %}
/users/export/ids
{% endapimethod %}

> 이 엔드포인트를 사용하여 사용자 식별자를 지정하여 모든 고객 프로필에서 데이터를 내보낼 수 있습니다. 

최대 50 `external_ids` 개 또는 `user_aliases` 단일 요청에 포함될 수 있습니다. `device_id`, `email_address` 또는 `phone`를 지정하려는 경우 요청당 식별자 중 하나만 포함할 수 있습니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#b9750447-9d94-4263-967f-f816f0c76577 {% endapiref %}

## 필수 구성 요소

이 엔드포인트를 사용하려면 권한이 있는 `users.export.ids` [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='users export ids' %}

## 요청 본문

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_ids": (optional, array of strings) External identifiers for users you wish to export,
  "user_aliases": (optional, array of user alias objects) user aliases for users to export,
  "device_id": (optional, string) Device identifier as returned by various SDK methods such as `getDeviceId`,
  "braze_id": (optional, string) Braze identifier for a particular user,
  "email_address": (optional, string) Email address of user,
  "phone": (optional, string) Phone number of user,
  "fields_to_export": (optional, array of strings) Name of user data fields to export. Defaults to all if not provided
}
```

## 요청 매개 변수

| 매개 변수 | 필수 | 데이터형 | 설명 |
|-----|-----|-----|-----|
|`external_ids` | 선택 사항 | 문자열 배열 | 내보내려는 사용자의 외부 식별자입니다. |
|`user_aliases` | 선택 사항 | 사용자 별칭 객체의 배열 | 내보낼 사용자의 [사용자 별칭]({{site.baseurl}}/api/objects_filters/user_alias_object/)입니다. |
|`device_id` | 선택 사항 | 문자열 | `getDeviceId`와 같이 다양한 SDK 메서드에서 반환되는 기기 식별자입니다. |
|`braze_id` | 선택 사항 | 문자열 | 특정 사용자에 대한 Braze 식별자입니다. |
|`email_address` | 선택 사항 | 문자열 | 사용자의 이메일 주소입니다. |
|`phone` | 선택 사항 | [E.164](https://en.wikipedia.org/wiki/E.164) 형식의 문자열 | 사용자의 전화 번호입니다. |
|`fields_to_export` | 선택 사항 | 문자열 배열 | 내보낼 사용자 데이터 필드의 이름입니다. 제공되지 않은 경우 기본값은 all입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## 요청 예시
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/export/ids' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "external_ids": ["user_identifier1", "user_identifier2"],
  "user_aliases": [
    {
      "alias_name": "example_alias",
      "alias_label": "example_label"
    }
  ],
  "device_id": "1234567",
  "braze_id": "braze_identifier",
  "email_address": "example@braze.com",
  "phone": "11112223333",
  "fields_to_export": ["first_name", "email", "purchases"]
}'
```

## 내보낼 필드

다음은 유효한 `fields_to_export`의 목록입니다. `fields_to_export`를 사용하여 반환되는 데이터를 최소화하면 이 API 엔드포인트의 응답 시간을 개선할 수 있습니다.

| 내보낼 필드 | 데이터형 | 설명 |
|---|---|---|
| `apps` | 배열 | 이 사용자가 세션을 기록한 앱에는 다음 필드가 포함됩니다.<br><br>- `name`: 앱 이름<br>- `platform`: iOS, Android 또는 웹과 같은 앱 플랫폼<br>- `version`: 앱 버전 번호 또는 이름 <br>- `sessions`: 이 앱의 총 세션 수<br>- `first_used`: 첫 번째 세션 날짜<br>- `last_used`: 마지막 세션 날짜<br><br>모든 필드는 문자열입니다. |
| `attributed_campaign` | 문자열 | [어트리뷰션 통합]({{site.baseurl}}/partners/message_orchestration/attribution)의 데이터(설정된 경우). 특정 광고 캠페인의 식별자입니다. |
| `attributed_source` | 문자열 | [어트리뷰션 통합]({{site.baseurl}}/partners/message_orchestration/attribution)의 데이터(설정된 경우). 광고가 게재된 플랫폼의 식별자입니다. |
| `attributed_adgroup` | 문자열 | [어트리뷰션 통합]({{site.baseurl}}/partners/message_orchestration/attribution)의 데이터(설정된 경우). 아래 캠페인의 선택적 하위 그룹화에 대한 식별자입니다. |
| `attributed_ad` | 문자열 | [어트리뷰션 통합]({{site.baseurl}}/partners/message_orchestration/attribution)의 데이터(설정된 경우). 캠페인 및 광고그룹 아래에 있는 선택적 하위 그룹의 식별자입니다. |
| `braze_id` | 문자열 | 이 사용자에 대해 Braze가 설정한 장치별 고유 사용자 식별자입니다. |
| `country` | 문자열 | [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) 표준을 사용하는 사용자 국가입니다. |
| `created_at` | 문자열 | 고객 프로필을 만든 날짜 및 시간(ISO 8601 형식)입니다. |
| `custom_attributes` | 객체 | 이 사용자에 대한 커스텀 속성 키-값 페어입니다. |
| `custom_events` | 배열 | 지난 90일 동안 이 사용자에게 발생한 커스텀 이벤트입니다. |
| `devices` | 배열 | 사용자 장치에 대한 정보로, 플랫폼에 따라 다음이 포함될 수 있습니다.<br><br>- `model`: 기기의 모델 이름<br>- `os`: 기기의 운영 체제<br>- `carrier`: 기기의 서비스 제공업체(사용 가능한 경우)<br>- `idfv`: (iOS) Braze 기기 식별자, 공급업체의 Apple 식별자(있는 경우)<br>- `idfa`: (iOS) 광고용 식별자(있는 경우)<br>- `device_id`: (Android) Braze 기기 식별자<br>- `google_ad_id`: (Android) Google Play 광고 식별자(있는 경우)<br>- `roku_ad_id`: (Roku) Roku 광고 식별자<br>- `ad_tracking_enabled`: 기기에서 광고 추적이 활성화된 경우 true 또는 false일 수 있습니다.
| `dob` | 문자열 | 사용자의 생년월 `YYYY-MM-DD`일(. |
| `email` | 문자열 | 사용자의 이메일 주소입니다. |
| `external_id` | 문자열 | 식별된 사용자의 고유 사용자 식별자입니다. |
| `first_name` | 문자열 | 사용자의 이름입니다. |
| `gender` | 문자열 | 사용자의 성별입니다. 가능한 값은 다음과 같습니다.<br><br>- `M`: 남성<br>- `F`: 여성<br>- `O`: 기타<br>- `N`: 해당 없음<br>- `P`: 말하지 않는 것을 선호합니다.<br>- `nil`: unknown |
| `home_city` | 문자열 | 사용자의 거주 도시입니다. |
| `language` | 문자열 | ISO-639-1 표준의 사용자 언어. |
| `last_coordinates` | float 배열 | 사용자의 가장 최근 기기 위치( `[longitude, latitude]` 양식). |
| `last_name` | 문자열 | 사용자의 성입니다. |
| `phone` | 문자열 | E.164 형식의 사용자 전화 번호입니다. |
| `purchases` | 배열 | 이 사용자가 지난 90일 동안 구매한 항목입니다. |
| `push_tokens` | 배열 | 앱의 알림을 보낼 위치를 지정하는 고유한 익명 식별자입니다. |
| `random_bucket` | 정수 | 무작위 사용자의 균일하게 분산된 세그먼트를 생성하는 데 사용되는 사용자의 [무작위 버킷 번호]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events#random-bucket-number-event)입니다. |
| `time_zone` | 문자열 | IANA 시간대 데이터베이스와 동일한 형식의 사용자 시간대입니다. |
| `total_revenue` | 플로트 | 이 사용자에게 귀속된 총 수익입니다. 총 매출은 사용자가 전환 기간 동안 수신한 캠페인과 캔버스에 대한 구매를 기반으로 계산됩니다. |
| `uninstalled_at` | 타임스탬프 | 사용자가 앱을 제거한 날짜 및 시간입니다. 앱이 제거되지 않은 경우 생략됩니다. |
| `user_aliases` | 객체 | [사용자 별칭 객체]({{site.baseurl}}/api/objects_filters/user_alias_object#user-alias-object-specification)는 `alias_name` 및 `alias_label`를 포함합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

`/users/export/ids` 엔드포인트는 수신된 모든 캠페인 및 캔버스, 수행된 모든 커스텀 이벤트, 수행된 모든 구매 및 모든 커스텀 속성과 같은 데이터를 포함하여 이 사용자에 대한 전체 고객 프로필을 함께 가져옵니다. 따라서 이 엔드포인트는 다른 REST API 엔드포인트보다 느립니다.

요청된 데이터에 따라 이 API 엔드포인트는 분당 2,500개 요청 사용량 제한으로 인해 요구 사항을 충족하기에 충분하지 않을 수 있습니다. 이 엔드포인트를 정기적으로 사용하여 사용자를 내보낼 것으로 예상되는 경우 비동기식이고 더 큰 데이터 풀에 더 최적화된 세그먼트별로 사용자를 내보내는 것이 좋습니다.

## 응답

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "users" : (array of object) the data for each of the exported users, may be empty if no users are found,
    "invalid_user_ids" : (optional, array of string) each of the identifiers provided in the request that did not correspond to a known user
}
```

이 엔드포인트를 통해 액세스할 수 있는 데이터의 예는 다음 예제를 참조하세요.

### 샘플 사용자 내보내기 파일 출력

사용자 내보내기 개체(가능한 한 최소한의 데이터를 포함합니다. 개체에서 필드가 누락된 경우 null, false 또는 비어 있는 것으로 가정해야 함):

{% tabs %}
{% tab All fields %}

```json
{
    "created_at": (string),
    "external_id" : (string),
    "user_aliases" : [
      {
        "alias_name" : (string),
        "alias_label" : (string)
      }
    ],
    "braze_id": (string),
    "first_name" : (string),
    "last_name" : (string),
    "email" : (string),
    "dob" : (string) date for the user's date of birth,
    "home_city" : (string),
    "country" : (string) ISO-3166-1 alpha-2 standard,
    "phone" : (string),
    "language" : (string) ISO-639-1 standard,
    "time_zone" : (string),
    "last_coordinates" : (array of float) [lon, lat],
    "gender" : (string) "M" | "F",
    "total_revenue" : (float),
    "attributed_campaign" : (string),
    "attributed_source" : (string),
    "attributed_adgroup" : (string),
    "attributed_ad" : (string),
    "push_subscribe" : (string) "opted_in" | "subscribed" | "unsubscribed",
    "email_subscribe" : (string) "opted_in" | "subscribed" | "unsubscribed",
    "custom_attributes" : (object) custom attribute key-value pairs,
    "custom_events" : [
      {
        "name" : (string),
        "first" : (string) date,
        "last" : (string) date,
        "count" : (int)
      },
      ...
    ],
    "purchases" : [
      {
        "name" : (string),
        "first" : (string) date,
        "last" : (string) date,
        "count" : (int)
      },
      ...
    ],
    "devices" : [
      {
        "model" : (string),
        "os" : (string),
        "carrier" : (string),
        "idfv" : (string) only included for iOS devices when IDFV collection is enabled,
        "idfa" : (string) only included for iOS devices when IDFA collection is enabled,
        "google_ad_id" : (string) only included for Android devices when Google Play Advertising Identifier collection is enabled,
        "roku_ad_id" : (string) only included for Roku devices,
        "ad_tracking_enabled" : (bool)
      },
      ...
    ],
    "push_tokens" : [
      {
        "app" : (string) app name,
        "platform" : (string),
        "token" : (string)
      },
      ...
    ],
    "apps" : [
      {
        "name" : (string),
        "platform" : (string),
        "version" : (string),
        "sessions" : (integer),
        "first_used" : (string) date,
        "last_used" : (string) date
      },
      ...
    ],
    "campaigns_received" : [
      {
        "name" : (string),
        "last_received" : (string) date,
        "engaged" : 
         {
           "opened_email" : (bool),
           "opened_push" : (bool),
           "clicked_email" : (bool),
           "clicked_triggered_in_app_message" : (bool)
          },
          "converted" : (bool),
          "api_campaign_id" : (string),
          "variation_name" : (optional, string) exists only if it is a multivariate campaign,
          "variation_api_id" : (optional, string) exists only if it is a multivariate campaign,
          "in_control" : (optional, bool) exists only if it is a multivariate campaign
        },
      ...
    ],
    "canvases_received": [
      {
        "name": (string),
        "api_canvas_id": (string),
        "last_received_message": (string) date,
        "last_entered": (string) date,
        "variation_name": (string),
        "in_control": (bool),
        "last_exited": (string) date,
        "steps_received": [
          {
            "name": (string),
            "api_canvas_step_id": (string),
            "last_received": (string) date
          },
          {
            "name": (string),
            "api_canvas_step_id": (string),
            "last_received": (string) date
          },
          {
            "name": (string),
            "api_canvas_step_id": (string),
            "last_received": (string) date
          }
        ]
      },
      ...
    ],
    "cards_clicked" : [
      {
        "name" : (string)
      },
      ...
    ]
}
```

{% endtab %}
{% tab Sample output %}

```json
{
    "created_at" : "2020-07-10 15:00:00.000 UTC",
    "external_id" : "A8i3mkd99",
    "user_aliases" : [
      {
        "alias_name" : "user_123",
        "alias_label" : "amplitude_id"
      }
    ],
    "braze_id": "5fbd99bac125ca40511f2cb1",
    "random_bucket" : 2365,
    "first_name" : "Jane",
    "last_name" : "Doe",
    "email" : "example@braze.com",
    "dob" : "1980-12-21",
    "home_city" : "Chicago",
    "country" : "US",
    "phone" : "+442071838750",
    "language" : "en",
    "time_zone" : "Eastern Time (US & Canada)",
    "last_coordinates" : [41.84157636433568, -87.83520818508256],
    "gender" : "F",
    "total_revenue" : 65,
    "attributed_campaign" : "braze_test_campaign_072219",
    "attributed_source" : "braze_test_source_072219",
    "attributed_adgroup" : "braze_test_adgroup_072219",
    "attributed_ad" : "braze_test_ad_072219",
    "push_subscribe" : "opted_in", 
    "push_opted_in_at": "2020-01-26T22:45:53.953Z",
    "email_subscribe" : "subscribed",
    "custom_attributes": 
    {
      "loyaltyId": "37c98b9d-9a7f-4b2f-a125-d873c5152856",
      "loyaltyPoints": "321",
       "loyaltyPointsNumber": 107
    },
    "custom_events": [
      {
        "name": "Loyalty Acknowledgement",
        "first": "2021-06-28T17:02:43.032Z",
        "last": "2021-06-28T17:02:43.032Z",
        "count": 1
      },
      ...
    ],
    "purchases": [
      {
        "name": "item_40834",
        "first": "2021-09-05T03:45:50.540Z",
        "last": "2022-06-03T17:30:41.201Z",
        "count": 10
      },
      ...
    ],
    "devices": [
      {
        "model": "Pixel XL",
        "os": "Android (Q)",
        "carrier": null,
        "device_id": "312ef2c1-83db-4789-967-554545a1bf7a",
        "ad_tracking_enabled": true
      },
      ...
    ],
    "push_tokens": [
      {
        "app": "MovieCanon",
        "platform": "Android",
        "token": "12345abcd",
        "device_id": "312ef2c1-83db-4789-967-554545a1bf7a",
        "notifications_enabled": true
      },
      ...
    ],
    "apps": [
      {
        "name": "MovieCannon",
        "platform": "Android",
        "version": "3.29.0",
        "sessions": 1129,
        "first_used": "2020-02-02T19:56:19.142Z",
        "last_used": "2021-11-11T00:25:19.201Z"
      },
      ...
    ],
    "campaigns_received": [
      {
        "name": "Email Unsubscribe",
        "api_campaign_id": "d72fdc84-ddda-44f1-a0d5-0e79f47ef942",
        "last_received": "2022-06-02T03:07:38.105Z",
        "engaged": 
        {
           "opened_email": true
        },
        "converted": true,
        "multiple_converted": 
        {
          "Primary Conversion Event - A": true
        },
        "in_control": false,
        "variation_name": "Variant 1",
        "variation_api_id": "1bddc73a-a134-4784-9134-5b5574a9e0b8"
      },
      ...
    ],
    "canvases_received": [
      {
        "name": "Non Global  Holdout Group 4/21/21",
        "api_canvas_id": "46972a9d-dc81-473f-aa03-e3473b4ed781",
        "last_received_message": "2021-07-07T20:46:24.136Z",
        "last_entered": "2021-07-07T20:45:24.000+00:00",
        "variation_name": "Variant 1",
        "in_control": false,
        "last_entered_control_at": null,
        "last_exited": "2021-07-07T20:46:24.136Z",
        "steps_received": [
          {
            "name": "Step",
            "api_canvas_step_id": "43d1a349-c3c8-4be1-9fbe-ce708e4d1c39",
            "last_received": "2021-07-07T20:46:24.136Z"
          },
          ...
        ]
      }
      ...
    ],    
    "cards_clicked" : [
      {
        "name" : "Loyalty Promo"
      },
      ...
    ]
}
```

{% endtab %}
{% endtabs %}

{% alert tip %}
CSV 및 API 내보내기에 대한 도움말은 [내보내기 문제 해결]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/)을 참조하세요.
{% endalert %}

{% endapi %}
