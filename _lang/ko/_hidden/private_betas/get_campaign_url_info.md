---
nav_title: "GET: 캠페인을 위한 링크 별칭 목록"
layout: api_page
page_type: reference
hidden: true
permalink: /get_campaign_link_alias/

platform: API
channel:
  - Email
tool:
  - Canvas
  - Campaigns

description: "이 문서에서는 목록 링크 별칭 Braze 엔드포인트에 대한 세부 정보를 설명합니다."
---
{% api %}
# 캠페인에 대한 링크 별칭 나열
{% apimethod get %}
/campaigns/url_info/details
{% endapimethod %}

> 이 엔드포인트를 사용하여 특정 캠페인 메시지 배리언트에 설정된 링크 별칭을 나열합니다.

{% apiref postman %}  {% endapiref %}

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `campaign_id`  | 필수 | 문자열 | [캠페인 API 식별자]({{site.baseurl}}/api/identifier_types/#campaign-api-identifier)을 참조하십시오.|
| `message_variation_id `  |  필수 | 문자열 | 메시지 배리언트 API 식별자. 캠페인 세부 정보 페이지에서 캠페인에 대한 **API 식별자** 섹션 아래에서 이를 찾을 수 있습니다. |
| `includes_link_id` | 선택 사항 | 문자열 | Braze에서 할당한 특정 링크 식별자 또는 `null`. 이것은 특정 `link_id`에 의해 결과를 필터링하는 데 사용됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 요청 예시
```
curl --location --request GET 'https://rest.iad-01.braze.com/campaigns/url_info/details?campaign_id=4615a404-b2c2-421e-9a04-2233bb3ec4f9&message_variation_id=0ea708fe-36b4-43f7-9f5c-a0650ea2a7a0&includes_link_id=014tk4e0kg97' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## 응답

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "channel": "email",
  "name": "Variant 1",
  "link_data": [
    {
      "link_URL": "https://www.braze.com?lid=014tk4e0kg97",
      "link_id": "014tk4e0kg97",
      "content_block_path_info": [],
      "link_alias": "link5"
    }
  ],
  "message": "success"
}
```

### 문제 해결

다음 표에는 가능한 반환 오류와 관련된 문제 해결 단계가 나와 있습니다.

| 오류 | 문제 해결 |
| --- | --- |
| `Missing/Invalid Campaign ID` | 캠페인 API ID는 API 식별자여야 합니다. [캠페인 목록 엔드포인트 내보내기]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/)를 사용하거나 대시보드에 로그인하여 이를 찾을 수 있습니다. |
| `Missing/Invalid Message Variant ID` | 메시지 배리언트 API ID는 API 식별자여야 합니다. 대시보드에 로그인하거나 [캠페인 세부 정보 엔드포인트 내보내기]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/)를 사용하여 이를 찾을 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


{% endapi %}
