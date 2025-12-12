---
nav_title: "GET: 사용자 지정 속성 내보내기"
article_title: "GET: 사용자 지정 속성 내보내기"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 사용자 지정 속성 내보내기 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 사용자 지정 속성 내보내기
{% apimethod get %}
/custom_attributes
{% endapimethod %}

> 이 엔드포인트를 사용하여 앱에 대해 기록된 사용자 지정 속성 목록을 내보낼 수 있습니다. 속성은 알파벳순으로 정렬된 50개 그룹으로 반환됩니다.

## 필수 구성 요소

이 엔드포인트를 사용하려면 `custom_attributes.get` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='custom_attributes' %}

## 쿼리 매개변수

이 엔드포인트를 호출할 때마다 50개의 어트리뷰트가 반환된다는 점에 유의하세요. 속성이 50개 이상인 경우 다음 예제 응답에 표시된 것처럼 `Link` 헤더를 사용하여 다음 페이지에서 데이터를 검색합니다.

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `cursor` | Optional | 문자열 | 사용자 정의 속성의 페이지 매김을 결정합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 요청 예시

### 커서 없음

```
curl --location --request GET 'https://rest.iad-01.braze.com/custom_attributes' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

### 커서 포함

```
curl --location --request GET 'https://rest.iad-03.braze.com/custom_attributes?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 응답

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "attributes" : [
        {
            "array_length": 100, (number) the maximum array length, or null if not applicable,
            "data_type": "Number", (string) the data type,
            "description": "The attribute description", (string) the attribute description,
            "name": "The attribute name", (string) the attribute name,
            "status": "Active", (string) the attribute status,
            "tag_names": ["Tag One", "Tag Two"] (array) the tag names associated with the attribute formatted as strings,
        },
        ...
    ]
}
```

### 치명적인 오류 응답 코드 {#fatal-export}

요청에 치명적인 오류가 발생할 경우 반환되는 상태 코드 및 관련 오류 메시지는 [치명적인 오류를]({{site.baseurl}}/api/errors/#fatal-errors) 참조하세요.

{% alert tip %}
CSV 및 API 내보내기 문제 해결에 대한 도움은 [내보내기 문제 해결]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/)를 방문하세요.
{% endalert %}

{% endapi %}
