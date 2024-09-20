---
nav_title: "DELETE: 대시보드 사용자 계정 제거"
article_title: "DELETE: 대시보드 사용자 계정 제거"
alias: /delete_existing_dashboard_user/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 대시보드 사용자 계정 Braze 엔드포인트 제거에 대한 자세한 내용을 설명합니다."
---

{% api %}
# 대시보드 사용자 계정 제거
{% apimethod delete %}
/scim/v2/Users/{id}
{% endapimethod %}

> 이 엔드포인트를 사용하여 SCIM [`POST`]({{site.baseurl}}/scim/post_create_user_account/) 메서드에서 반환된 `id` 리소스를 지정하여 기존 대시보드 사용자를 영구 삭제합니다. 

이는 Braze 대시보드의 **사용자 관리** 섹션에서 사용자를 삭제하는 것과 유사합니다. SCIM 토큰을 얻는 방법에 대한 자세한 내용은 [자동화된 사용자 프로비저닝]({{site.baseurl}}/scim/automated_user_provisioning/)을 참조하세요.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#9c7c71ea-afd6-414a-99d1-4eb1fe274f16 {% endapiref %}

## 전제 조건

이 엔드포인트를 사용하려면 SCIM 토큰이 필요합니다. 자세한 내용은 [자동화된 사용자 프로비저닝]({{site.baseurl}}/scim/automated_user_provisioning/)을 참조하세요.

## 요금 제한

{% multi_lang_include rate_limits.md endpoint='delete dashboard user' %}

## 경로 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 | 설명
|---|---|---|---|
| `id` | 필수 | 문자열 | 사용자의 리소스 ID입니다. 이 매개변수는 `POST` `/scim/v2/Users/` 또는 `GET`  `/scim/v2/Users?filter=userName eq "user@test.com"` 메서드에서 반환됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## 요청 본문

```json
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-REST-API-KEY
```

## 요청 예시
```json
curl --location --request DELETE 'https://rest.iad-01.braze.com/scim/v2/Users/dfa245b7-24195aec-887bb3ad-602b3340' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-SCIM-TOKEN-HERE' \
```

## 응답

### 오류 응답 예시

```json
HTTP/1.1 204 Not Found
Content-Type: text/html; charset=UTF-8
```

이 ID를 가진 개발자가 Braze에 존재하지 않는 경우 엔드포인트는 다음과 같이 응답합니다.
\`\`\`json
HTTP/1.1 404 Not Found
Content-Type: text/html; charset=UTF-8

{
"schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
"detail": "User not found",
"status": 404
}
    \`\`\`
    {% endapi %}
