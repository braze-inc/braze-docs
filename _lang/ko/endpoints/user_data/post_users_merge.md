---
nav_title: "POST: 사용자 병합"
article_title: "POST: 사용자 병합"
search_tag: Endpoint
page_order: 6
layout: api_page
page_type: reference
description: "이 문서에서는 사용자 Braze 병합 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 사용자 병합
{% apimethod post %}
/users/merge
{% endapimethod %}

> 이 엔드포인트를 사용하여 한 사용자를 다른 사용자와 병합할 수 있습니다. 

요청당 최대 50개의 병합을 지정할 수 있습니다. 이 엔드포인트는 비동기식입니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d262b86d-cf84-46e2-b9d0-f882bb7078de {% endapiref %}

## Prerequisites

이 엔드포인트를 사용하려면 `users.merge` 권한이 있는 [API 키]({{site.baseurl}}/api/api_key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='users merge' %}

## 요청 본문

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "merge_updates" : (required, array of objects)
}
```

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `merge_updates` | 필수 | 배열 | 객체 배열입니다. 각 객체에는 `identifier_to_merge` 객체와 `identifier_to_keep` 객체가 포함되어야 하며, 각 객체는 `external_id`, `user_alias`, `phone` 또는 `email` 로 사용자를 참조해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### 병합 동작

아래에 설명된 동작은 스노우플레이크가 **지원하지 않는** 모든 Braze 기능에 적용됩니다. 사용자 병합은 **메시징 기록** 탭, 세그먼트 확장, 쿼리 작성기 및 커런츠에 반영되지 않습니다.

{% alert important %}
엔드포인트는 업데이트되는 `merge_updates` 객체의 순서를 보장하지 않습니다.
{% endalert %}

이 엔드포인트는 대상 사용자에서 다음 필드를 찾을 수 없는 경우 병합합니다.

- First name
- Last name
- 이메일 주소( [암호화되지]({{site.baseurl}}/user_guide/data/field_level_encryption/) 않은 경우)
- Gender
- Date of birth
- Phone number
- Time zone
- Home city
- Country
- 언어
- 장치 정보
- 세션 수(두 프로필의 세션 합계)
- 첫 세션 날짜(Braze는 두 날짜 중 빠른 날짜를 선택합니다)
- 마지막 세션 날짜(Braze는 두 날짜 중 늦은 날짜를 선택합니다.)
- 사용자 지정 속성(대상 프로필의 기존 사용자 지정 속성은 유지되며 대상 프로필에 존재하지 않았던 사용자 지정 속성도 포함됨)
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
- 캠페인 상호작용 데이터(Braze는 가장 최근 날짜 필드를 선택합니다)
- 워크플로 요약(Braze가 가장 최근 날짜 필드를 선택합니다)
- 메시지 및 메시지 참여 내역
- 세션 데이터는 앱이 두 사용자 프로필 모두에 있는 경우에만 병합됩니다.

{% alert note %}
사용자를 병합할 때 `/users/merge` 엔드포인트를 사용하는 것은 [`changeUser()` 방법을](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser) 사용하는 것과 동일한 방식으로 작동합니다.
{% endalert %}

#### 사용자 지정 이벤트 날짜 및 구매 이벤트 날짜 동작

이렇게 병합된 필드는 'Y일 동안의 X 이벤트에 대한' 필터를 업데이트합니다. 구매 이벤트의 경우 이러한 필터에는 'Y일 내 구매 횟수' 및 '지난 Y일 동안 지출한 금액'이 포함됩니다.

### 이메일 또는 전화번호로 사용자 병합하기

식별자로 `email` 또는 `phone` 을 지정한 경우, 식별자에 `prioritization` 값을 추가로 입력해야 합니다. `prioritization` 은 여러 사용자가 있는 경우 병합할 사용자를 지정하는 정렬된 배열이어야 합니다. 즉, 우선순위에서 일치하는 사용자가 두 명 이상이면 병합이 이루어지지 않습니다.

배열에 허용되는 값은 다음과 같습니다:

- `identified`
- `unidentified`
- `most_recently_updated` (가장 최근에 업데이트한 사용자에게 우선순위를 부여하는 것을 의미함)
- `least_recently_updated` (가장 최근에 업데이트한 사용자에게 우선순위를 부여하는 것을 의미함)

우선순위 배열에는 한 번에 다음 옵션 중 하나만 존재할 수 있습니다.

- `identified` 를 가진 사용자에게 우선순위를 지정하는 것을 말합니다. `external_id`
- `unidentified` 없는 사용자에게 우선순위를 지정하는 것을 말합니다. `external_id`

## 요청 예시

### 기본 요청

요청의 패턴을 보여주기 위한 기본 요청 본문입니다.

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "external_id": "old-user1"
      },
      "identifier_to_keep": {
        "external_id": "current-user1"
      }
    },
    {
      "identifier_to_merge": {
        "email": "user1@braze.com",
        "prioritization": ["unidentified", "most_recently_updated"]
      },
      "identifier_to_keep":  {
        "email": "user2@braze.com",
        "prioritization": ["identified", "most_recently_updated"]
      }
    },
    {
      "identifier_to_merge": {
        "user_alias": {
          "alias_name": "old-user2@example.com",
          "alias_label": "email"
        }
      },
      "identifier_to_keep": {
        "user_alias": {
          "alias_name": "current-user2@example.com",
          "alias_label": "email"
        }
      }
    }
  ]
}'
```

### 미확인 사용자 병합하기

다음 요청은 이메일 주소 `john.smith@braze.com` 를 가진 가장 최근에 업데이트된 미확인 사용자를 외부 ID `john` 를 가진 사용자로 병합합니다. 이 예제에서 `most_recently_updated` 을 사용하면 확인되지 않은 사용자 한 명으로 쿼리를 필터링합니다. 따라서 이 이메일 주소를 가진 미확인 사용자 두 명이 있는 경우 외부 ID `john` 를 가진 사용자로 한 명만 병합됩니다.

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "email": "john.smith@braze.com",
        "prioritization": ["unidentified", "most_recently_updated"]
      },
      "identifier_to_keep": {
        "external_id": "john"
      }
    }
  ]
}'
```

### 미확인 사용자를 식별된 사용자로 병합하기

다음 예제는 이메일 주소가 `john.smith@braze.com` 인 가장 최근에 업데이트된 미확인 사용자를 이메일 주소가 `john.smith@braze.com` 인 가장 최근에 업데이트된 식별된 사용자로 병합합니다. 

`most_recently_updated` 을 사용하면 쿼리가 한 명의 사용자( `identifier_to_merge` 의 경우 식별되지 않은 사용자 1명, `identifier_to_keep` 의 경우 식별된 사용자 1명)로만 필터링됩니다.

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "email": "john.smith@braze.com",
        "prioritization": ["unidentified", "most_recently_updated"]
      },
      "identifier_to_keep": {
        "email": "john.smith@braze.com",
        "prioritization": ["identified", "most_recently_updated"]
      }
    }
  ]
}'
```

### most_recently_updated 우선순위를 포함하지 않고 미확인 사용자 병합하기

이메일 주소가 `john.smith@braze.com` 인 미확인 사용자 두 명이 있는 경우 이 예제 요청은 해당 이메일 주소를 가진 미확인 사용자 두 명이 있으므로 사용자를 병합하지 않습니다. 이 요청은 이메일 주소가 `john.smith@braze.com` 인 미확인 사용자가 한 명만 있는 경우에만 작동합니다.

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "email": "john.smith@braze.com",
        "prioritization": ["unidentified"]
      },
      "identifier_to_keep": {
        "external_id": "john"
      }
    }
  ]
}'
```

## Response

이 엔드포인트에 대한 상태 코드 응답은 `202` 와 `400` 두 가지입니다.

### 성공 응답의 예

`202` 상태 코드는 다음과 같은 응답 본문을 반환할 수 있습니다.

```json
{
  "message": "success"
}
```

### 오류 응답의 예

`400` 상태 코드는 다음과 같은 응답 본문을 반환할 수 있습니다. 발생할 수 있는 오류에 대한 자세한 내용은 [문제 해결을](#troubleshooting) 참조하세요.

```json
{
  "message": "'merge_updates' must be an array of objects"
}
```

## 문제 해결

다음 표에는 발생할 수 있는 오류 메시지가 나열되어 있습니다.

| 오류 | 문제 해결 |
| --- |
| `'merge_updates' must be an array of objects` | `merge_updates` 이 객체 배열인지 확인합니다. |
| `a single request may not contain more than 50 merge updates` | 한 요청에 병합 업데이트는 최대 50개까지만 지정할 수 있습니다. |
| `identifiers must be objects with an 'external_id' property that is a string, 'user_alias' property that is an object, 'email' property that is a string, or 'phone' property that is a string` | 요청에 포함된 식별자를 확인하세요. |
| `'merge_updates' must only have 'identifier_to_merge' and 'identifier_to_keep'` | `merge_updates` 에 `identifier_to_merge` 과 `identifier_to_keep` 두 개의 객체만 포함되어 있는지 확인합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
