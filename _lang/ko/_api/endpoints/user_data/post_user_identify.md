---
nav_title: "POST: 사용자 식별"
article_title: "POST: 사용자 식별"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
alias: /users_identify_merge/
description: "이 문서에서는 사용자 식별 Braze 엔드포인트에 대한 세부 정보를 간략하게 설명합니다."

---
{% api %}
# 사용자 식별
{% apimethod post %}
/users/identify
{% endapimethod %}

> 이 엔드포인트를 사용하여 식별되지 않은(별칭 전용) 사용자를 식별합니다. 

{% alert important %}
2023년 8월 7일부터 이 엔드포인트는 모든 호출에 대한 데이터를 병합합니다. 이 수단 [`merge_behavior`](#merge)은 모든 호출에 대해 `merge`로 설정됩니다.
{% endalert %}

`/users/identify` 호출은 별칭 전용 프로필을 식별된 프로필과 결합하고 별칭 전용 프로필을 제거합니다.

사용자를 식별하려면 `aliases_to_identify` 객체에 `external_id`가 포함되어야 합니다. 해당 `external_id`를 가진 사용자가 없는 경우 별칭이 지정된 사용자의 레코드에 `external_id`가 추가되고 사용자가 식별된 것으로 간주됩니다. 요청당 최대 50개의 사용자 별칭을 추가할 수 있습니다.

그런 다음 여러 개의 추가 사용자 별칭을 단일 `external_id`에 연결할 수 있습니다.
\- 이러한 후속 연결이 `none` 필드가 `merge_behavior`으로 설정된 상태에서 이루어지면 사용자 별칭과 연결된 푸시 토큰 및 메시지 기록만 유지됩니다. 모든 속성, 이벤트 또는 구매는 "분리"되며 식별된 사용자가 사용할 수 없습니다. 한 가지 해결 방법은 [`/users/export/ids`엔드포인트]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)를 사용하여 식별하기 전에 별칭이 지정된 사용자의 데이터를 내보낸 다음 속성, 이벤트 및 구매를 식별된 사용자와 다시 연결하는 것입니다.
- `merge`로 설정된 `merge_behavior` 필드와 연결되면 이 엔드포인트는 익명 사용자에 있는 [특정 필드](#merge)를 식별된 사용자에게 병합합니다.

{% alert tip %}
사용자를 식별할 때 예기치 않은 데이터 손실을 방지하려면 먼저 [데이터 수집 권장사항을]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/best_practices/#capturing-user-data-when-alias-only-user-info-is-already-present) 참조하여 별칭 전용 사용자 정보가 이미 있는 경우 사용자 데이터를 캡처하는 방법을 알아보는 것이 좋습니다.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5f74e0f7-0620-4c7b-b0a2-f5f38fdbff58 {% endapiref %}

## 필수 구성 요소

이 엔드포인트를 사용하려면 `users.identify` 권한이 있는 [API 키]({{site.baseurl}}/api/api_key/)가 필요합니다.

## 사용량 제한 
2021년 9월 16일 또는 그 이후에 Braze에 온보딩한 고객의 경우 이 엔드포인트에 대한 요청에 사용량 제한이 적용됩니다. 자세한 내용은 [API 제한]({{site.baseurl}}/api/basics/#api-limits)을 참조하세요.

## 요청 본문

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
   "aliases_to_identify" : (required, array of alias to identify objects), 
   "merge_behavior": (optional, string) one of 'none' or 'merge' is expected
}
```

### 요청 매개 변수

| 매개 변수 | 필수 | 데이터형 | 설명 |
| -----------|----------| --------|------- |
| `aliases_to_identify` | 필수 | 객체를 식별하기 위한 별칭 배열 | 객체 및 [사용자 별칭 객체]({{site.baseurl}}/api/objects_filters/user_alias_object/)를 [식별하려면 별칭]({{site.baseurl}}/api/objects_filters/aliases_to_identify/)을 참조하세요. |
| `merge_behavior` | 선택 사항 | 문자열 | `none` 또는 `merge` 중 하나가 필요합니다.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

#### Merge\_behavior 필드 {#merge}

`merge_behavior` 필드를 `merge`로 설정하면 익명 사용자에게**만** 있는 다음 필드 중 하나를 식별된 사용자에게 병합하도록 엔드포인트가 설정됩니다.
-이름
-성
-이메일
-성별
-생년월일
-전화번호
-시간대
\- 거주 도시
\- 나라
-언어
\- 세션 수(두 프로필의 세션 합계)
\- 첫 번째 세션 날짜 (Braze는 두 날짜 중 더 빠른 날짜를 선택합니다)
\- 마지막 세션 날짜 (Braze는 두 날짜 중 더 늦은 날짜를 선택합니다)
\- 사용자 지정 속성
\- 사용자 지정 이벤트 및 구매 이벤트 데이터
\- "Y일 중 X회" 세그멘테이션을 위한 사용자 지정 이벤트 및 구매 이벤트 속성(여기서 X<=50 및 Y<=30)
\- 세그먼트 가능한 사용자 지정 이벤트 요약
  \- 이벤트 수(두 프로필의 합계)
  \- 이벤트가 처음 발생했습니다 (Braze는 두 날짜 중 더 빠른 날짜를 선택합니다)
  \- 마지막으로 발생한 이벤트(Braze는 두 날짜 중 더 늦은 날짜를 선택함)
\- 인앱 구매 총액(센트)(두 프로필의 합계)
\- 총 구매 횟수(두 프로필의 합계)
\- 첫 구매 날짜 (Braze는 두 날짜 중 더 빠른 날짜를 선택합니다)
\- 마지막 구매 날짜 (Braze는 두 날짜 중 더 늦은 날짜를 선택합니다)
\- 앱 요약
\- Last\_X\_at 필드 (Braze는 고아 프로필 필드가 최신인 경우 필드를 업데이트합니다)
\- 캠페인 요약 (Braze는 가장 최근 날짜 필드를 선택합니다)
\- 워크플로우 요약(Braze는 가장 최근 날짜 필드를 선택함)
\- 메시지 및 메시지 참여 기록

익명 사용자에서 찾은 사용자에 대한 다음 필드 중 하나를 선택합니다.
\- 사용자 지정 이벤트 및 구매 이벤트 수, 첫 번째 날짜 및 마지막 날짜 타임스탬프
  \- 이러한 병합된 필드는 "Y일 내 X 이벤트" 필터를 업데이트합니다. 구매 이벤트의 경우 이러한 필터에는 'Y일 내 구매 횟수' 및 '지난 Y일 동안 지출한 금액'이 포함됩니다.

세션 데이터는 앱이 두 사용자 프로필 모두에 있는 경우에만 병합됩니다. 예를 들어 대상 사용자에게 "ABCApp"에 대한 앱 요약이 없지만 원래 사용자가 있는 경우 대상 사용자는 병합 후 프로필에 "ABCApp" 앱 요약이 표시됩니다. 

필드를 `none`으로 설정하면 사용자 데이터가 식별된 고객 프로필에 병합되지 않습니다.

## 요청 예시
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/identify' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "aliases_to_identify" : 
  [
    {
      "external_id": "external_identifier",
      "user_alias" : {
          "alias_name" : "example_alias",
          "alias_label" : "example_label"
      }
    }
  ],
  "merge_behavior": "merge"
}'
```

{% alert tip %}
`alias_name` 및 `alias_label`에 대한 자세한 내용은 [사용자 별칭]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases) 설명서를 확인하세요.
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
