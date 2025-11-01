---
nav_title: "GET: 콘텐츠 블록 정보 보기"
article_title: "GET: 콘텐츠 블록 정보 보기"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 콘텐츠 블록 정보 보기 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."
---

{% api %}
# 콘텐츠 블록 정보 보기
{% apimethod get %}
/content_blocks/info
{% endapimethod %}

> 이 엔드포인트를 사용하여 기존 [콘텐츠 블록]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/)에 대한 정보를 호출할 수 있습니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#589adda3-0def-4369-9ddc-eae71923c0ee {% endapiref %}

## Prerequisites
이 엔드포인트를 사용하려면 `content_blocks.info` 권한이 있는 [API 키]({{site.baseurl}}/api/api_key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='default' %}

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `content_block_id`  | Required | 문자열 | 콘텐츠 블록 식별자입니다. <br><br>API 호출을 통해 콘텐츠 블록 정보를 나열하거나 [API 키]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) 페이지로 이동한 다음 하단으로 스크롤하여 콘텐츠 블록 API 식별자를 검색하면 이 정보를 찾을 수 있습니다.|
| `include_inclusion_data`  | 선택 사항 | 부울 | `true` 로 설정하면 API는 이 콘텐츠 블록이 포함된 캠페인 및 캔버스의 메시지 변형 API 식별자를 반환하여 후속 호출에서 사용할 수 있습니다.  결과에는 보관되거나 삭제된 캠페인 또는 캔버스가 제외됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 요청 예시
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/content_blocks/info?content_block_id={{content_block_id}}&include_inclusion_data=false' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## 응답

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "content_block_id": (string) the Content Block identifier,
  "name": (string) the name of the Content Block,
  "content": (string) the content in the Content Block,
  "description": (string) the Content Block description,
  "content_type": (string) the content type, html or text,
  "tags": (array) An array of tags formatted as strings,
  "created_at": (string) The time the Content Block was created in ISO 8601,
  "last_edited": (string) The time the Content Block was last edited in ISO 8601,
  "inclusion_count" : (integer) the inclusion count,
  "inclusion_data": (array) the inclusion data,
  "message": "success",
}
```

## 문제 해결

다음 표에는 가능한 반환 오류와 관련된 문제 해결 단계가 나와 있습니다.

| 오류 | 문제 해결 |
| --- | --- |
| `Content Block ID cannot be blank` | 콘텐츠 블록이 요청에 나열되어 있고 따옴표로 묶여 있는지 확인합니다(`""`). |
| `Content Block ID is invalid for this workspace` | 이 콘텐츠 블록이 존재하지 않거나 다른 회사 계정 또는 워크스페이스에 있습니다. |
| `Content Block has been deleted—content not available` | 이 콘텐츠 블록은 이전에 존재했을 수 있지만 삭제되었습니다. |
| `Include Inclusion Data—error` | 이 매개변수는 부울 값(참 또는 거짓)만 허용합니다. `include_inclusion_data` 값이 따옴표(`""`)로 묶이지 않았는지 확인하여 값이 문자열로 대신 전송되도록 합니다. 자세한 내용은 [요청 매개변수를](#request-parameters) 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


{% endapi %}
