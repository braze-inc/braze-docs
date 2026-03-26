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

> 이 엔드포인트를 사용하여 제공된 외부 ID를 사용하여 미식별(별칭 전용, 이메일 전용 또는 전화번호 전용) 사용자를 식별할 수 있습니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5f74e0f7-0620-4c7b-b0a2-f5f38fdbff58 {% endapiref %}

## 작동 방식

`/users/identify`를 호출하면 별칭(별칭 전용 프로필), 이메일 주소(이메일 전용 프로필) 또는 전화번호(전화번호 전용 프로필)로 식별되는 고객 프로필을 `external_id`(식별된 프로필)가 있는 고객 프로필과 결합한 다음 별칭 전용 프로필을 제거합니다.

사용자를 식별하려면 다음 오브젝트에 `external_id`가 포함되어야 합니다:

- `aliases_to_identify`
- `emails_to_identify`
- `phone_numbers_to_identify`

해당 `external_id`를 가진 사용자가 없으면, `external_id`가 별칭 사용자의 기록에 추가되고 사용자는 식별된 것으로 간주됩니다. 사용자는 특정 레이블에 대해 하나의 별칭만 가질 수 있습니다. 사용자가 이미 `external_id`와 함께 존재하고 별칭 전용 프로필과 동일한 레이블로 기존 별칭이 있는 경우, 고객 프로필은 결합되지 않습니다.

{% alert tip %}
사용자 식별 시 예기치 않은 데이터 손실을 방지하려면 먼저 [데이터 수집 모범 사례]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/best_practices/#capturing-user-data-when-alias-only-user-info-is-already-present)를 참조하여 별칭 전용 사용자 정보가 이미 존재하는 경우 사용자 데이터를 캡처하는 방법에 대해 알아보는 것이 좋습니다.
{% endalert %}

### 병합 동작

기본적으로, 이 엔드포인트는 익명 사용자에게서 **독점적으로** 발견된 다음 필드 목록을 식별된 사용자로 병합합니다.

{% details 병합되는 필드 목록 %}
- 이름
- 성
- 이메일
- 성별
- 생년월일
- 전화번호
- 시간대
- 거주 도시
- 국가
- 언어
- 세션 수(두 프로필의 세션 합계)
- 첫 세션 날짜(Braze는 두 날짜 중 더 이른 날짜를 선택합니다)
- 마지막 세션 날짜(Braze는 두 날짜 중 더 늦은 날짜를 선택합니다)
- 커스텀 속성
- 커스텀 이벤트 및 구매 이벤트 데이터
- "Y일 동안 X회" 세분화를 위한 커스텀 이벤트 및 구매 이벤트 등록정보(여기서 X<=50 및 Y<=30)
- 세분화 가능한 커스텀 이벤트 요약
  - 이벤트 수(두 프로필의 합계)
  - 이벤트가 처음 발생한 날짜(Braze는 두 날짜 중 더 이른 날짜를 선택합니다)
  - 이벤트가 마지막으로 발생한 날짜(Braze는 두 날짜 중 더 늦은 날짜를 선택합니다)
- 인앱 구매 총액(센트 단위)(두 프로필의 합계)
- 총 구매 횟수(두 프로필의 합계)
- 첫 구매 날짜(Braze는 두 날짜 중 더 이른 날짜를 선택합니다)
- 마지막 구매 날짜(Braze는 두 날짜 중 더 늦은 날짜를 선택합니다)
- 앱 요약
- Last_X_at 필드(Braze는 고아 프로필 필드가 더 최근인 경우 필드를 업데이트합니다)
- 캠페인 요약(Braze는 가장 최근 날짜 필드를 선택합니다)
- 워크플로우 요약(Braze는 가장 최근 날짜 필드를 선택합니다)
- 메시지 및 메시지 참여 내역
- 커스텀 이벤트 및 구매 이벤트 수와 첫 번째 날짜 및 마지막 날짜 타임스탬프
  - 이 병합된 필드는 "Y일 동안 X 이벤트" 필터를 업데이트합니다. 구매 이벤트의 경우 이러한 필터에는 "Y일 내 구매 횟수" 및 "지난 Y일 동안 지출한 금액"이 포함됩니다.
- 앱이 두 고객 프로필에 모두 존재하는 경우 세션 데이터
  - 예를 들어, 타겟 사용자가 "ABCApp"에 대한 앱 요약이 없지만 원래 사용자가 있다면, 병합 후 타겟 사용자는 프로필에 "ABCApp" 앱 요약을 갖게 됩니다.
{% enddetails %}

## 필수 조건

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

요청당 최대 50개의 사용자 별칭을 추가할 수 있습니다. 하나의 `external_id`에 여러 개의 추가 사용자 별칭을 연결할 수 있습니다.

{% alert important %}
요청당 `aliases_to_identify`, `emails_to_identify` 또는 `phone_numbers_to_identify` 중 하나가 필요합니다. 예를 들어, 요청에 `emails_to_identify`를 사용하여 이메일로 사용자를 식별할 수 있습니다.
{% endalert %}

| 매개변수                   | 필수 | 데이터 유형                           | 설명                                                                                                                                                                 |
|-----------------------------|----------|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `aliases_to_identify`       | 필수 | 식별할 별칭 오브젝트 배열 | [식별할 별칭 오브젝트]({{site.baseurl}}/api/objects_filters/aliases_to_identify/) 및 [사용자 별칭 오브젝트]({{site.baseurl}}/api/objects_filters/user_alias_object/)를 참조하세요. |
| `emails_to_identify`        | 필수 | 식별할 별칭 오브젝트 배열 | `email`이 식별자로 지정된 경우 필수입니다. 사용자를 식별하기 위한 이메일 주소입니다. [이메일로 사용자 식별하기](#identifying-users-by-email)를 참조하세요.                                                                                                              |
| `phone_numbers_to_identify` | 필수 | 식별할 별칭 오브젝트 배열 | 사용자를 식별하기 위한 전화번호입니다.                                                                                                                                            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### 이메일 주소 및 전화번호로 사용자 식별

이메일 주소나 전화번호를 식별자로 지정하는 경우 식별자에 `prioritization`도 포함해야 합니다.

`prioritization`은 여러 사용자가 발견된 경우 병합할 사용자를 지정하는 배열이어야 합니다. `prioritization`은 정렬된 배열로, 우선순위에서 하나 이상의 사용자가 일치하는 경우 병합이 발생하지 않습니다.

배열에 허용되는 값은 다음과 같습니다:

- `identified`
- `unidentified`
- `most_recently_updated`(가장 최근에 업데이트된 사용자에게 우선순위를 부여하는 것을 의미함)
- `least_recently_updated`(가장 오래전에 업데이트된 사용자에게 우선순위를 부여하는 것을 의미함)

우선순위 배열에는 한 번에 다음 옵션 중 하나만 존재할 수 있습니다:

- `identified`는 `external_id`를 가진 사용자에게 우선순위를 지정하는 것을 의미합니다
- `unidentified`는 `external_id`가 없는 사용자에게 우선순위를 지정하는 것을 의미합니다

{% alert note %}
이메일 주소나 전화번호가 여러 사용자와 일치하는 경우 병합이 발생하지 않습니다. 여기에는 해당 사용자 중 하나가 요청에 지정된 것과 동일한 `external_id`를 가진 경우도 포함됩니다. 이 경우 엔드포인트는 `"message": "success"`를 반환하지만 고객 프로필은 결합되지 않습니다. 이를 방지하려면 이 엔드포인트를 호출하기 전에 이메일 주소나 전화번호가 미식별 사용자에게만 연결되어 있는지 확인하세요.
{% endalert %}

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

### 대소문자 구분

`alias_name` 필드는 대소문자를 구분합니다. `201` 상태 코드를 반환하는 요청은 요청 구문이 유효했음을 확인할 뿐, 별칭이 일치했음을 확인하는 것은 아닙니다. 요청의 `alias_name` 대소문자가 고객 프로필에 저장된 별칭과 정확히 일치하지 않으면 작업이 자동으로 실패하고 `external_id`가 할당되지 않습니다. 예를 들어, 저장된 별칭이 `JimJones@example.com`인 경우 `jimjones@example.com`으로 요청하면 성공을 반환하지만 결과가 생성되지 않습니다.

{% alert tip %}
`alias_name` 및 `alias_label`에 대한 자세한 내용은 [사용자 별칭]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases) 설명서를 참조하세요.
{% endalert %}

## 응답

```json
{
    "aliases_processed": 1,
    "message": "success"
}
```

{% endapi %}