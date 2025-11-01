---
nav_title: "POST: 사용자 식별"
article_title: "POST: 사용자 식별"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
alias: /users_identify_merge/
description: "이 문서에서는 사용자 식별 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 사용자 식별
{% apimethod post %}
/users/identify
{% endapimethod %}

> 이 엔드포인트를 사용하여 제공된 외부 ID를 사용하여 미확인(별칭 전용, 이메일 전용 또는 전화번호 전용) 사용자를 식별할 수 있습니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5f74e0f7-0620-4c7b-b0a2-f5f38fdbff58 {% endapiref %}

## 작동 방식

`/users/identify` 을 호출하면 별칭(별칭 전용 프로필), 이메일 주소(이메일 전용 프로필) 또는 전화번호(전화번호 전용 프로필)로 식별되는 사용자 프로필을 `external_id` (식별된 프로필)이 있는 사용자 프로필과 결합한 다음 별칭 전용 프로필을 제거합니다. 

사용자를 식별하려면 다음 객체에 `external_id` 이 포함되어야 합니다:

- `aliases_to_identify`
- `emails_to_identify` 
- `phone_numbers_to_identify`

`external_id` 을 가진 사용자가 없는 경우 `external_id` 이 별칭 사용자의 레코드에 추가되며 해당 사용자는 식별된 것으로 간주됩니다. 사용자는 특정 레이블에 대해 하나의 별칭만 가질 수 있습니다. 사용자가 이미 `external_id` 계정을 가지고 있고 별칭 전용 프로필과 동일한 레이블을 가진 기존 별칭을 가지고 있는 경우에는 사용자 프로필이 결합되지 않습니다.

{% alert tip %}
사용자 식별 시 예기치 않은 데이터 손실을 방지하려면 먼저 [데이터 수집 모범 사례를]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/best_practices/#capturing-user-data-when-alias-only-user-info-is-already-present) 참조하여 별칭 전용 사용자 정보가 이미 존재하는 경우 사용자 데이터를 캡처하는 방법에 대해 알아보는 것이 좋습니다.
{% endalert %}

### 병합 동작

기본적으로 이 엔드포인트는 익명 **사용자에게만** 있는 다음 필드 목록을 식별된 사용자에게 병합합니다.

{% details List of fields that are merged %}
- First name
- Last name
- Email
- Gender
- Date of birth
- Phone number
- Time zone
- Home city
- Country
- 언어
- 세션 수(두 프로필의 세션 합계)
- 첫 세션 날짜(Braze는 두 날짜 중 빠른 날짜를 선택합니다)
- 마지막 세션 날짜(Braze는 두 날짜 중 늦은 날짜를 선택합니다.)
- 사용자 지정 속성
- 사용자 지정 이벤트 및 구매 이벤트 데이터
- "Y일 동안 X회" 세그먼트에 대한 커스텀 이벤트 및 구매 이벤트 속성정보(여기서 X<=50 와 Y<=30)
- 세분화 가능한 사용자 지정 이벤트 요약
  - 이벤트 수(두 프로필의 합계)
  - 이벤트가 처음 발생한 날짜(Braze는 두 날짜 중 빠른 날짜를 선택합니다.)
  - 이벤트가 마지막으로 발생한 날짜(Braze는 두 날짜 중 나중에 발생한 날짜를 선택합니다.)
- 인앱 구매 총액(센트 단위)(두 프로필의 합계)
- 총 구매 횟수(두 프로필의 합산)
- 최초 구매 날짜(Braze는 두 날짜 중 빠른 날짜를 선택합니다.)
- 마지막 구매 날짜(Braze는 두 날짜 중 늦은 날짜를 선택합니다.)
- 앱 요약
- Last_X_at 필드(고아가 된 프로필 필드가 더 최신인 경우 Braze가 필드를 업데이트합니다)
- 캠페인 요약(Braze는 가장 최근 날짜 필드를 선택합니다)
- 워크플로 요약(Braze가 가장 최근 날짜 필드를 선택합니다)
- 메시지 및 메시지 참여 내역
- 사용자 지정 이벤트 및 구매 이벤트 수와 첫 번째 날짜 및 마지막 날짜 타임스탬프 
  - 이렇게 병합된 필드는 'Y일 동안의 X 이벤트에 대한' 필터를 업데이트합니다. 구매 이벤트의 경우 이러한 필터에는 'Y일 내 구매 횟수' 및 '지난 Y일 동안 지출한 금액'이 포함됩니다.
- 앱이 두 사용자 프로필에 모두 존재하는 경우 세션 데이터
  - 예를 들어, 대상 사용자에게는 "ABCApp"에 대한 앱 요약이 없지만 원래 사용자에게는 있는 경우, 병합 후 대상 사용자의 프로필에 "ABCApp" 앱 요약이 표시됩니다.
{% enddetails %}

## Prerequisites

이 엔드포인트를 사용하려면 `users.identify` 권한이 있는 [API 키]({{site.baseurl}}/api/api_key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='users identify' %}

## 요청 본문

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
   "aliases_to_identify" : (required, array of alias to identify objects),
   "emails_to_identify": (optional, array of alias to identify objects) User emails to identify,
   "phone_numbers_to_identify": (optional, array of alias to identify objects) User phone numbers to identify,
},
```

### 요청 매개변수

요청당 최대 50개의 사용자 별칭을 추가할 수 있습니다. 하나의 `external_id` 에 여러 개의 추가 사용자 별칭을 연결할 수 있습니다.

{% alert important %}
다음 중 하나가 필요합니다: `aliases_to_identify`, `emails_to_identify`, 또는 요청당 `phone_numbers_to_identify`. 예를 들어, 이 엔드포인트를 사용하여 요청에 `emails_to_identify` 을 사용하여 이메일로 사용자를 식별할 수 있습니다.
{% endalert %}

| 매개변수                   | 필수 | 데이터 유형                           | 설명                                                                                                                                                                 |
|-----------------------------|----------|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `aliases_to_identify`       | 필수 | 객체를 식별하기 위한 별칭 배열 | [객체]({{site.baseurl}}/api/objects_filters/aliases_to_identify/) 및 [사용자 별칭 객체를]({{site.baseurl}}/api/objects_filters/user_alias_object/) [식별하려면 별칭을]({{site.baseurl}}/api/objects_filters/aliases_to_identify/) 참조하세요. |
| `emails_to_identify`        | 필수 | 객체를 식별하기 위한 별칭 배열 | `email` 식별자로 지정된 경우 필수입니다. 사용자를 식별하기 위한 이메일 주소. [이메일로 사용자 식별하기를](#identifying-users-by-email) 참조하세요.                                                                                                              |
| `phone_numbers_to_identify` | 필수 | 객체를 식별하기 위한 별칭 배열 | 사용자를 식별하기 위한 전화번호.                                                                                                                                            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### 이메일 주소 및 전화번호로 사용자 식별

이메일 주소나 전화번호를 식별자로 지정하는 경우 식별자에 `prioritization` 도 포함해야 합니다.

`prioritization` 은 여러 사용자가 있는 경우 병합할 사용자를 지정하는 배열이어야 합니다. `prioritization` 은 정렬된 배열이므로 우선순위에서 일치하는 사용자가 두 명 이상이면 병합이 수행되지 않습니다.

배열에 허용되는 값은 다음과 같습니다:

- `identified`
- `unidentified`
- `most_recently_updated` (가장 최근에 업데이트한 사용자에게 우선순위를 부여하는 것을 의미함)
- `least_recently_updated` (가장 최근에 업데이트한 사용자에게 우선순위를 부여하는 것을 의미함)

우선순위 배열에는 한 번에 다음 옵션 중 하나만 존재할 수 있습니다.

- `identified` 를 가진 사용자에게 우선순위를 지정하는 것을 말합니다. `external_id`
- `unidentified` 없는 사용자에게 우선순위를 지정하는 것을 말합니다. `external_id`

배열에 `identified` 을 지정하는 경우, 이는 사용자에게 `external_id` 이 **있어야** 캔버스에 입력할 수 있다는 의미입니다. 이메일 주소가 있는 사용자가 본인 확인 여부와 관계없이 메시지를 입력하도록 하려면 `most_recently_updated` 또는 `least_recently_updated` 매개변수만 사용하세요.

## 요청 예시

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/identify' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "aliases_to_identify": [
    {
      "external_id": "external_identifier",
      "user_alias": {
          "alias_name": "example_alias",
          "alias_label": "example_label"
      }
    }
  ],
  "emails_to_identify": [
    {
      "external_id": "external_identifier_2",
      "email": "john.smith@braze.com",
      "prioritization": ["unidentified", "most_recently_updated"]
    }
  ]
}'
```

{% alert tip %}
자세한 내용은 `alias_name` 및 `alias_label` 에서 [사용자 별칭]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases) 문서를 참조하세요.
{% endalert %}

## 응답

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
    "aliases_processed": 1,
    "message": "success"
}
```

{% endapi %}
