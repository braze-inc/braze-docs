---
nav_title: "GET: SDK 인증 키 목록"
article_title: "GET: SDK 인증 키 목록"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "이 문서에서는 SDK 인증 키 목록 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."
---

{% api %}
# SDK 인증 키 목록
{% apimethod get %}
/app_group/sdk_authentication/keys
{% endapimethod %}

> 이 엔드포인트를 사용하여 앱의 모든 SDK 인증 키를 검색할 수 있습니다.

## Prerequisites

이 엔드포인트를 사용하려면 `sdk_authentication.keys` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | -------- | --------- | ----------- |
| `app_id` | 필수 | 문자열 | 앱 API 식별자입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 예시 요청

```json
curl --location --request GET 'https://rest.iad-01.braze.com/app_group/sdk_authentication/keys?app_id=01234567-89ab-cdef-0123-456789abcdef' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 응답

```json
{
  "keys": [
    {
      "id": "abcdef12-3456-7890-abcd-ef1234567890",
      "rsa_public_key": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvvD+fgA0YuCUd/v35htn...\n-----END PUBLIC KEY-----",
      "description": "SDK Authentication Key for iOS App",
      "is_primary": true
    },
    {
      "id": "fedcba98-7654-3210-fedc-ba9876543210",
      "rsa_public_key": "-----BEGIN PUBLIC KEY-----\nqWGfHOAiIwVzC/bTxwQZQQVzm/3ktgdNXRUDm5aIwVzCtxbNm5aIxOAiIwVzVHOA...\n-----END PUBLIC KEY-----",
      "description": "SDK Authentication Key for Android App",
      "is_primary": false
    }
  ]
}
```

## 응답 매개변수

| 매개변수 | 데이터 유형 | 설명 |
| --------- | --------- | ----------- |
| `keys` | 배열 | SDK 인증 키 개체의 배열입니다. |
| `keys[].id` | 문자열 | SDK 인증 키의 ID입니다. |
| `keys[].rsa_public_key` | 문자열 | RSA 공개 키 문자열입니다. |
| `keys[].description` | 문자열 | SDK 인증 키에 대한 설명입니다. |
| `keys[].is_primary` | 부울 | 이 키가 기본 SDK 인증 키인지 여부입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### 유효성 검사 규칙

이 엔드포인트에는 다음과 같은 유효성 검사 규칙이 있습니다:

- `app_id` 매개변수는 유효한 앱 API 식별자이어야 합니다.
- 앱이 작업 공간에 있어야 합니다.

{% endapi %}
