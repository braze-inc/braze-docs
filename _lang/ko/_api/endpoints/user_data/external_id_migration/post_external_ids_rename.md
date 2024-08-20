---
nav_title: "POST: 외부 ID 이름 변경"
article_title: "POST: 외부 ID 이름 변경"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "이 문서에서는 외부 ID 이름 바꾸기 엔드포인트에 대한 세부 정보를 간략하게 설명합니다."

---
{% api %}
# 외부 ID 이름 변경
{% apimethod post %}
/users/external_ids/rename
{% endapimethod %}

> 이 엔드포인트를 사용하여 사용자의 외부 ID의 이름을 변경합니다. 

요청당 최대 50개의 이름 변경 객체를 전송할 수 있습니다. 

이 엔드포인트는 사용자에 대한 새(기본) `external_id`를 설정하고 기존 `external_id`는 더 이상 사용되지 않습니다. 즉, 더 이상 사용되지 않는 `external_id`를 제거할 때까지 둘 중 하나로 사용자를 식별할 수 있습니다. 외부 ID가 여러 개 있으면 이전 외부 ID 명명 스키마를 사용하는 이전 버전의 앱이 중단되지 않도록 마이그레이션 기간이 허용됩니다. 

이전 이름 지정 스키마를 더 이상 사용하지 않는 경우 [`/users/external_ids/remove` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove)를 사용하여 더 이상 사용되지 않는 외부 ID를 제거하는 것이 좋습니다.

{% alert warning %}
더 이상 사용되지 않는 외부 ID를 제거하고 `/users/external_ids/remove` 엔드포인트를 `/users/delete` 대신 사용해야 합니다. 지원이 중단된 외부 ID로 `/users/delete`에 요청을 보내면 고객 프로필이 완전히 삭제되며 취소할 수 없습니다.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#17682d2b-1546-4a3c-9703-aa5a12861d7c {% endapiref %}

## 사전 요구 사항

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

## 요청 파라미터

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | ---------| --------- | ----------- |
| `external_id_renames` | 필수 | 외부 식별자 이름 바꾸기 개체 배열 | 요청 예와 외부 식별자 이름 바꾸기 개체의 구조에 대한 다음 제한 사항 보기| |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

- `current_external_id`는 사용자의 기본 ID여야 하며 더 이상 사용되지 않는 ID일 수 없습니다
- `new_external_id`는 이미 기본 ID 또는 더 이상 사용되지 않는 ID로 사용되고 있지 않아야 합니다
- `current_external_id`및 `new_external_id`는 같을 수 없습니다

## 요청 예제
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
응답은 모든 성공적인 이름 변경과 관련 오류가 있는 실패한 이름 변경을 확인합니다. `rename_errors` 필드의 오류 메시지는 원래 요청의 배열에 있는 객체의 인덱스를 참조합니다.

```
{
  "message" : (string) status message,
  "external_ids" : (array of strings) successful rename operations,
  "rename_errors": (array of arrays) <minor error message>
}
```

유효한 요청이 있으면 `message` 필드가 `success`를 반환됩니다. 보다 구체적인 오류가 `rename_errors` 어레이에 캡처됩니다. 이 `message` 필드는 다음과 같은 경우 오류를 반환합니다.
\- 잘못된 API 키
\- 빈 `external_id_renames` 배열
\- 50개 이상의 객체가 있는 `external_id_renames` 배열
\- 속도 제한 적중 (분당 1,000회 이상의 요청)

## 자주 묻는 질문

**이것이 MAU에 영향을 미치나요?**<br>
아니요, 사용자 수는 그대로 유지되므로 새 `external_id`만 사용할 수 있습니다.

**사용자 행동이 역사적으로 변했나요?**<br>
아니요, 사용자는 여전히 동일하고 모든 과거 행동이 여전히 사용자와 연결되어 있기 때문입니다.

**개발/스테이징 작업 공간에서 실행할 수 있습니까?**<br>
네. 실제로 스테이징 또는 개발 워크스페이스에서 테스트 마이그레이션을 실행하고 프로덕션 데이터를 실행하기 전에 모든 것이 원활하게 진행되었는지 확인하는 것이 좋습니다.

**이렇게 하면 데이터 포인트가 소모되나요?**<br>
이 기능에는 데이터 포인트가 필요하지 않습니다.

**권장 지원 중단 기간은 어떻게 되나요?**<br>
지원 중단된 외부 ID를 보관할 수 있는 기간에는 엄격한 제한이 없지만, 더 이상 지원 중단된 ID로 사용자를 참조할 필요가 없어지면 삭제하는 것이 좋습니다.

{% endapi %}
