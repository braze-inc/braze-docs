---
nav_title: "DELETE: 카탈로그 필드 삭제"
article_title: "DELETE: 카탈로그 필드 삭제"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "이 문서에서는 카탈로그 필드 브레이즈 엔드포인트 삭제에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 카탈로그 필드 삭제
{% apimethod delete %}
/catalogs/{catalog_name}/fields/{field_name}
{% endapimethod %}

> 이 엔드포인트를 사용하여 카탈로그 필드를 삭제합니다.
{% alert important %}
이 엔드포인트는 현재 얼리 액세스 중입니다. 이 얼리 액세스에 참여하려면 고객 성공 관리자에게 문의하세요.
{% endalert %}

## 필수 구성 요소

이 엔드포인트를 사용하려면 `catalogs.delete_fields` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog fields' %}

## 경로 매개변수

| 매개변수      | 필수 | 데이터 유형 | 설명                |
| -------------- | -------- | --------- | -------------------------- |
| `catalog_name` | 필수 | 문자열    | 카탈로그의 이름입니다.       |
| `field_name`   | 필수 | 문자열    | 카탈로그 필드의 이름입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 요청 예시

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants/fields/ratings' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
```

## 응답

이 엔드포인트에 대한 상태 코드 응답은 `202` 및 `404` 두 가지입니다.

### 성공 응답의 예

`202` 상태 코드는 다음 응답 본문을 반환할 수 있습니다.

```json
{
  "message": "success"
}
```

### 오류 응답의 예

`404` 상태 코드는 다음과 같은 응답 본문을 반환할 수 있습니다. 발생할 수 있는 오류에 대한 자세한 내용은 [문제 해결을](#troubleshooting) 참조하세요.

```json
{
  "errors": [
    {
      "id": "catalog-not-found",
      "message": "Could not find catalog",
      "parameters": [
        "catalog_name"
      ],
      "parameter_values": [
        "restaurants"
      ]
    }
  ],
  "message": "Invalid Request"
}
```

## 문제 해결

다음 표에는 반환될 수 있는 오류와 관련 문제 해결 단계가 나와 있습니다.

| 오류                           | 문제 해결                                                  |
| ------------------------------- | ---------------------------------------------------------------- |
| `catalog-not-found`             | 카탈로그 이름이 유효한지 확인합니다.                            |
| `field-referenced-by-selection` | 카탈로그 필드가 현재 선택 항목에서 사용 중인지 확인합니다. |
| `field-is-inventory`            | 카탈로그 필드가 인벤토리 필드로 사용되는지 확인합니다.      |
| `invalid-field-name`            | 카탈로그 필드 이름이 유효한지 확인합니다.                      |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
