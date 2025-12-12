---
nav_title: "POST: 소프트웨어 개발 키트 인증 키 만들기"
article_title: "POST: SDK 인증 키 생성"
search_tag: Endpoint
page_order: 0
layout: api_page
page_type: reference
description: "이 문서에서는 SDK 인증 키 Braze 엔드포인트 만들기에 대한 자세한 내용을 설명합니다."
---

{% api %}
# SDK 인증 키 생성
{% apimethod post %}
/app_group/sdk_authentication/create
{% endapimethod %}

> 이 엔드포인트를 사용하여 앱에 대한 새 SDK 인증 키를 생성하세요.

## Prerequisites

이 엔드포인트를 사용하려면 `sdk_authentication.create` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 본문
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```
```json
{
  "app_id": "App API identifier",
  "rsa_public_key_str": "RSA public key string", 
  "description": "description", 
  "make_primary": false
}
```

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | Description |
| --------- | -------- | --------- | ----------- |
| `app_id` | Required | 문자열 | 앱 API 식별자입니다. |
| `rsa_public_key_str` | Required | 문자열 | RSA 공개 키 문자열입니다. 유효한 RSA 공개키여야 하며, 그렇지 않으면 오류가 반환됩니다. |
| `description` | Required | 문자열 | SDK 인증 키에 대한 설명입니다. |
| `make_primary` | 선택 사항 | 부울 | `true` 로 설정하면 이 키가 생성될 때 기본 SDK 인증 키가 됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 예시 요청

```json
curl --location --request POST 'https://rest.iad-01.braze.com/app_group/sdk_authentication/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "app_id": "01234567-89ab-cdef-0123-456789abcdef",
  "rsa_public_key_str": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvvD+fgA0YuCUd/v35htn...\n-----END PUBLIC KEY-----", 
  "description": "SDK Authentication Key for iOS App", 
  "make_primary": false
}'
```

## 응답
```json
{
  "id": "key id"
}
```

## 응답 매개변수

| 매개변수 | 데이터 유형 | Description |
| --------- | --------- | ----------- |
| `id` | 문자열 | 새로 생성된 SDK 인증 키의 ID입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### 유효성 검사 규칙

이 엔드포인트에는 다음과 같은 유효성 검사 규칙이 있습니다:

- 앱당 최대 3개의 SDK 인증 키를 보유할 수 있습니다.
- RSA 공개 키 문자열은 올바른 형식의 유효한 RSA 공개 키여야 합니다.
- `app_id` 은 유효한 앱 API 식별자이어야 합니다.
- 설명은 비워 둘 수 없습니다.

{% endapi %}
