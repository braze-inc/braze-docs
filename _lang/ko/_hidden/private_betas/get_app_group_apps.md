---
nav_title: "GET: 워크스페이스 앱 목록"
layout: api_page
page_type: reference
hidden: true
permalink: /get_app_group_apps/

platform: API
description: "이 문서에서는 목록 작업 영역 앱 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."
---
{% api %}
# 워크스페이스 앱 목록
{% apimethod get %}
/app_group/apps
{% endapimethod %}

> 이 엔드포인트를 사용하여 워크스페이스에 있는 앱의 이름과 고유 식별자(`api_key`)를 나열합니다. 

이 엔드포인트를 누르면 `apps`라는 오브젝트 배열이 반환됩니다. `apps`의 각 개체에는 앱의 이름과 고유 식별자가 포함되어 있습니다. 

{% apiref postman %}  {% endapiref %}

## 사용량 제한

이 엔드포인트는 하루(24시간) 100건의 요청으로 사용량 제한이 있습니다.

## 요청 매개변수

이 요청은 매개 변수를 받지 않습니다.

## 요청 예시

```
curl --location --request GET 'https://rest.iad-01.braze.com/app_group/apps' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## 응답

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "apps": [
        {
          "name": "App Name",
          "api_key": 00000000-0000-0000-0000-000000000000
        }
    ],
    "message": "success"
}
```

### 문제 해결

다음 표에는 가능한 반환 오류와 관련된 문제 해결 단계가 나와 있습니다.

| 오류 | 문제 해결 |
| --- | --- |
| `401: Unauthorized` | API 키에 필요한 권한이 없습니다. API 키에 `apps.get` 권한이 있는지 확인하세요. |
| `403: Forbidden` | 이 회사에서는 기능 플리퍼를 사용하지 않습니다. 고객 성공 관리자에게 도움을 요청하세요. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
