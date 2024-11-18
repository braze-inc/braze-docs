---
nav_title: "POST: 콘텐츠 블록 생성"
article_title: "POST: 콘텐츠 블록 생성"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 콘텐츠 블록 Braze 만들기 엔드포인트에 대해 간략하게 설명합니다."

---
{% api %}
# 콘텐츠 블록 생성
{% apimethod post %}
/content_blocks/create
{% endapimethod %}

> 이 엔드포인트를 사용하여 [콘텐츠 블록을]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) 만듭니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f1cefa8b-7a28-4e64-b579-198a4610d0a5 {% endapiref %}

## 필수 구성 요소
이 엔드포인트를 사용하려면 `content_blocks.create` 권한이 있는 [API 키]({{site.baseurl}}/api/api_key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 본문

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "name": (required, string) Must be less than 100 characters,
  "description": (optional, string) The description of the Content Block. Must be less than 250 character,
  "content": (required, string) HTML or text content within Content Block,
  "state": (optional, string) Choose `active` or `draft`. Defaults to `active` if not specified,
  "tags": (optional, array of strings) Tags must already exist
}
```

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `name` | 필수 | 문자열 | 콘텐츠 블록의 이름입니다. 100자 미만이어야 합니다. |
| `description` | 선택 사항 | 문자열 | 콘텐츠 블록에 대한 설명입니다. 250자 미만이어야 합니다. |
| `content` | 필수 | 문자열 | 콘텐츠 블록 내의 HTML 또는 텍스트 콘텐츠. |
| `state` | 선택 사항 | 문자열 | `active` 또는 `draft` 을 선택합니다. 지정하지 않으면 기본값은 `active` 입니다. |
| `tags` | 선택 사항 | 문자열 배열 | [태그가]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/) 이미 존재해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 요청 예시
```json
curl --location --request POST 'https://rest.iad-01.braze.com/content_blocks/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "name": "content_block",
  "description": "This is my Content Block",
  "content": "HTML content within block",
  "state": "draft",
  "tags": ["marketing"]
}'
```

## 응답

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "content_block_id": (string) Your newly generated block id,
  "liquid_tag": (string) The generated block tag from the Content Block name,
  "created_at": (string) The time the Content Block was created in ISO 8601,
  "message": "success"
}
```

## 문제 해결

다음 표에는 반환될 수 있는 오류와 관련 문제 해결 단계가 나와 있습니다.

| 오류 | 문제 해결 |
| --- | --- |
| `Content cannot be blank` | |
| `Content must be a string` | 콘텐츠가 따옴표로 묶여 있는지 확인합니다(`""`). |
| `Content must be smaller than 50kb` | 콘텐츠 블록의 콘텐츠는 총 50KB 미만이어야 합니다. |
| `Content contains malformed liquid` | 제공된 리퀴드는 유효하지 않거나 파싱할 수 없습니다. 유효한 Liquid로 다시 시도하거나 지원팀에 문의하세요. |
| `Content Block cannot be referenced within itself` | |
| `Content Block description cannot be blank` | |
| `Content Block description must be a string` | 콘텐츠 블록 설명이 따옴표로 묶여 있는지 확인합니다(`""`). |
| `Content Block description must be shorter than 250 characters` | |
| `Content Block name cannot be blank` | |
| `Content Block name must be shorter than 100 characters` | |
| `Content Block name can only contain alphanumeric characters` | 콘텐츠 블록 이름에는 문자(대문자 또는 소문자) `A` ~ `Z`, 숫자 `0` ~ `9`, 대시 `-`, 밑줄 `_` 중 하나를 포함할 수 있습니다 . 이모티콘, `!`, `@`, `~`, `&`, 기타 "특수" 문자와 같은 영숫자가 아닌 문자는 포함할 수 없습니다. |
| `Content Block with this name already exists` | 다른 이름을 사용해 보세요. |
| `Content Block state must be either active or draft` | |
| `Tags must be an array` | 태그의 형식은 문자열 배열로 지정해야 합니다(예: `["marketing", "promotional", "transactional"]`). | |
| `All tags must be strings` | 태그가 따옴표로 묶여 있는지 확인합니다(`""`). |
| `Some tags could not be found` | 콘텐츠 블록을 만들 때 태그를 추가하려면 해당 태그가 Braze에 이미 존재해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


{% endapi %}
