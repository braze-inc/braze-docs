---
nav_title: "POST: 외부 ID 이름 바꾸기"
article_title: "POST: 외부 ID 이름 바꾸기"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "이 문서에서는 외부 ID 이름 바꾸기 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 외부 ID 이름 바꾸기
{% apimethod post %}
/users/external_ids/rename
{% endapimethod %}

> 이 엔드포인트를 사용하여 사용자의 외부 ID 이름을 변경할 수 있습니다. 

요청당 최대 50개의 개체 이름 바꾸기를 보낼 수 있습니다. 

이 엔드포인트는 사용자에 대해 새(기본) `external_id` 을 설정하고 기존 `external_id` 을 더 이상 사용하지 않도록 설정합니다. 즉, 더 이상 사용되지 않는 사용자 아이디가 제거될 때까지 `external_id` 로 사용자를 식별할 수 있습니다. 여러 개의 외부 ID를 사용하면 이전 외부 ID 명명 스키마를 사용하는 이전 버전의 앱이 중단되지 않도록 마이그레이션 기간을 가질 수 있습니다. 

이전 명명 스키마를 더 이상 사용하지 않는 경우 [`/users/external_ids/remove` 엔드포인트를]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove) 사용하여 더 이상 사용되지 않는 외부 ID를 제거하는 것이 좋습니다.

{% alert warning %}
`/users/delete` 대신 `/users/external_ids/remove` 엔드포인트를 사용하여 더 이상 사용되지 않는 외부 ID를 제거해야 합니다. 더 이상 사용되지 않는 외부 ID로 `/users/delete` 으로 요청을 보내면 사용자 프로필이 완전히 삭제되며 되돌릴 수 없습니다.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#17682d2b-1546-4a3c-9703-aa5a12861d7c {% endapiref %}

## Prerequisites

이 엔드포인트를 사용하려면 `users.external_ids.rename` 권한이 있는 [API 키]({{site.baseurl}}/api/api_key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='external id migration' %}

## 요청 본문

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_id_renames" : (required, array of external ID rename objects)
}
```

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | ---------| --------- | ----------- |
| `external_id_renames` | 필수 | 외부 식별자 이름 변경 개체 배열 | 외부 식별자 이름 바꾸기 객체의 구조에 대한 요청 예시와 다음 제한 사항을 확인하세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

다음 사항에 유의하세요:

- `current_external_id` 은 사용자의 기본 ID여야 하며 더 이상 사용되지 않는 ID일 수 없습니다.
- `new_external_id` 은 이미 기본 아이디 또는 사용되지 않는 아이디로 사용 중이 아니어야 합니다.
- `current_external_id` 과 `new_external_id` 은 동일할 수 없습니다.

## 요청 예시
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/external_ids/rename' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "external_id_renames" :[
    {
      "current_external_id": "existing_external_id",
      "new_external_id" : "new_external_id"
    }
  ]
}'
```

## 응답

응답은 모든 성공적인 이름 변경과 실패한 이름 변경 및 관련 오류를 확인합니다. `rename_errors` 필드의 오류 메시지는 원래 요청의 배열에 있는 객체의 인덱스를 참조합니다.

```
{
  "message" : (string) status message,
  "external_ids" : (array of strings) successful rename operations,
  "rename_errors": (array of arrays) <minor error message>
}
```

`message` 필드에 유효한 요청이 있으면 `success`를 반환합니다. 보다 구체적인 오류는 `rename_errors` 배열에 캡처됩니다. `message` 필드는 다음과 같은 경우 오류를 반환합니다.

- 잘못된 API 키
- 빈 `external_id_renames` 배열
- `external_id_renames` 50개 이상의 객체가 있는 배열
- 속도 제한에 도달(분당 1,000건 이상의 요청)

## Frequently asked questions

### 이것이 MAU에 영향을 미치나요?
아니요, 사용자 수는 동일하게 유지되므로 새로운 `external_id` 을 갖게 됩니다.

### 사용자 행동이 기록적으로 변하나요?
아니요, 사용자는 여전히 동일하며 모든 과거 행동이 여전히 사용자와 연결되어 있기 때문입니다.

### 개발 또는 스테이징 워크스페이스에서 실행할 수 있나요?
예. 실제로 스테이징 또는 개발 작업 공간에서 테스트 마이그레이션을 실행하고 프로덕션 데이터에서 실행하기 전에 모든 것이 원활하게 진행되었는지 확인하는 것이 좋습니다.

### 이 로그는 데이터 포인트를 기록합니까?
이 기능은 데이터 포인트를 기록하지 않습니다.

### 권장 사용 중단 기간은 어떻게 되나요?
사용되지 않는 외부 ID를 얼마나 오래 보관할 수 있는지에 대한 엄격한 제한은 없지만, 더 이상 사용되지 않는 ID로 사용자를 참조할 필요가 없어진 후에는 삭제하는 것이 좋습니다.

{% endapi %}
