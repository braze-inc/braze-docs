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

## 전제 조건

이 엔드포인트를 사용하려면 `users.merge` 권한이 있는 [API 키]({{site.baseurl}}/api/api_key/)가 필요합니다.

## 요금 제한

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
| `merge_updates` | 필수 | 배열 | 객체 배열입니다. 각 객체에는 `identifier_to_merge` 객체와 `identifier_to_keep` 객체가 포함되어야 하며, 각 객체는 `external_id`, `user_alias` 또는 `email`로 사용자를 참조해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

### 병합 동작

아래에 설명된 동작은 스노우플레이크가 *지원하지 않는* 모든 Braze 기능에 적용됩니다. 사용자 병합은 **메시징 기록** 탭, 세그먼트 확장, 쿼리 작성기 및 커런츠에 반영되지 않습니다.

{% alert important %}
엔드포인트는 업데이트되는 `merge_updates` 객체의 순서를 보장하지 않습니다.
{% endalert %}

이 엔드포인트는 타겟 사용자에서 다음 필드를 찾을 수 없는 경우 해당 필드를 병합합니다.

- 이름
- 성
- 이메일
- 성별
- 생년월일
- 전화번호
- 시간대
- 거주 구/군/시
- 국가
- 언어
- 세션 수(두 프로필의 세션 합계)
- 첫 세션 날짜(Braze는 두 날짜 중 빠른 날짜를 선택합니다)
- 마지막 세션 날짜(Braze는 두 날짜 중 늦은 날짜를 선택합니다.)
- 사용자 지정 속성(대상 프로필의 기존 사용자 지정 속성은 유지되며 대상 프로필에 존재하지 않았던 사용자 지정 속성도 포함됨)
- 사용자 지정 이벤트 및 구매 이벤트 데이터
- "Y일 동안 X회" 세분화에 대한 사용자 지정 이벤트 및 구매 이벤트 속성(여기서 X<=50, Y<=30)
- 세분화 가능한 사용자 지정 이벤트 요약
  - 이벤트 수(두 프로필의 합계)
  - 이벤트가 처음 발생한 날짜(Braze는 두 날짜 중 빠른 날짜를 선택합니다.)
  - 이벤트가 마지막으로 발생한 날짜(Braze는 두 날짜 중 나중에 발생한 날짜를 선택합니다.)
- 인앱 구매 총액(센트 단위)(두 프로필의 합계)
- 총 구매 횟수(두 프로필의 합계)
- 최초 구매 날짜(Braze는 두 날짜 중 빠른 날짜를 선택합니다.)
- 마지막 구매 날짜(Braze는 두 날짜 중 늦은 날짜를 선택합니다.)
- 앱 요약
- Last\_X\_at 필드(고아가 된 프로필 필드가 더 최신인 경우 Braze가 필드를 업데이트합니다.)
- 캠페인 상호작용 데이터(Braze는 가장 최근 날짜 필드를 선택합니다)
- 워크플로 요약(Braze가 가장 최근 날짜 필드를 선택합니다)
- 메시지 및 메시지 참여 내역

세션 데이터는 앱이 두 고객 프로필에 모두 존재하는 경우에만 병합됩니다.

#### 사용자 지정 이벤트 날짜 및 구매 이벤트 날짜 동작
이렇게 병합된 필드는 'Y일 동안의 X 이벤트에 대해' 필터를 업데이트합니다. 구매 이벤트의 경우 이러한 필터에는 'Y일 동안의 구매 횟수' 및 '지난 Y일 동안 지출한 금액'이 포함됩니다.

### 이메일로 사용자 병합하기

식별자로 `email`을 지정한 경우 식별자에 `prioritization` 값을 추가로 입력해야 합니다. `prioritization`은 여러 사용자가 있는 경우 병합할 사용자를 지정하는 배열이어야 합니다. `prioritization`은 정렬된 배열이므로 우선순위에서 일치하는 사용자가 두 명 이상이면 병합이 발생하지 않습니다.

배열에 허용되는 값은 `identified`, `unidentified`, `most_recently_updated`. `most_recently_updated`이며 이는 가장 최근에 업데이트된 사용자에게 우선순위를 지정하는 것을 의미합니다.

우선순위 배열에는 한 번에 다음 옵션 중 하나만 존재할 수 있습니다.
- `identified`은 `external_id`로 사용자에게 우선 순위를 지정하는 것을 의미합니다
- `unidentified`는 `external_id` 없이 사용자에게 우선 순위를 지정하는 것을 의미합니다

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

다음 요청은 이메일 주소가 "john.smith@braze.com"인 가장 최근에 업데이트된 미확인 사용자를 `external_id` "john"인 사용자로 병합합니다. `most_recently_updated`를 사용하면 확인되지 않은 사용자 한 명으로만 쿼리가 필터링됩니다. 따라서 이 이메일 주소를 가진 미확인 사용자가 두 명인 경우 `external_id` "john"을 가진 사용자로 한 명만 병합됩니다.

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

다음 예는 이메일 주소가 "john.smith@braze.com"인 가장 최근에 업데이트된 미확인 사용자를 이메일 주소가 "john.smith@braze.com"인 가장 최근에 업데이트된 식별된 사용자로 병합합니다. `most_recently_updated`를 사용하면 쿼리가 한 명의 사용자(`identifier_to_merge`의 경우 식별되지 않은 사용자 1명, `identifier_to_keep`의 경우 식별된 사용자 1명)로만 필터링됩니다.

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

### most\_recently\_updated 우선순위를 포함하지 않고 미확인 사용자 병합하기

이메일 주소가 "john.smith@braze.com"인 미확인 사용자가 두 명 있는 경우, 이 예제 요청은 해당 이메일 주소를 가진 미확인 사용자가 두 명 있으므로 사용자를 병합하지 않습니다. 이 요청은 이메일 주소가 "john.smith@braze.com"인 미확인 사용자가 한 명만 있는 경우에만 작동합니다.

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

## 응답

이 엔드포인트에 대한 상태 코드 응답은 `202` 및`400` 두 가지입니다.

### 성공 응답 예시

상태 코드 `202`는 다음과 같은 응답 본문을 반환할 수 있습니다.

```json
{
  "message": "success"
}
```

### 오류 응답 예시

상태 코드 `400`은 다음과 같은 응답 본문을 반환할 수 있습니다. 발생할 수 있는 오류에 대한 자세한 내용은 [문제 해결을](#troubleshooting) 참조하세요.

```json
{
  "message": "'merge_updates' must be an array of objects"
}
```

## 문제 해결

다음 표에는 발생할 수 있는 오류 메시지가 나열되어 있습니다.

| 오류 | 문제 해결 |
| --- |
| `'merge_updates' must be an array of objects` | `merge_updates`는 객체 배열인지 확인합니다. |
| `a single request may not contain more than 50 merge updates` | 한 요청에 병합 업데이트는 최대 50개까지만 지정할 수 있습니다. |
| `identifiers must be objects with an 'external_id' property that is a string, 'user_alias' property that is an object, or 'email' property that is a string` | 요청의 식별자를 확인하세요. |
| `'merge_updates' must only have 'identifier_to_merge' and 'identifier_to_keep'` | `merge_updates`는 `identifier_to_merge` 및 `identifier_to_keep` 두 개의 객체만 포함되어 있는지 확인합니다. |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}
