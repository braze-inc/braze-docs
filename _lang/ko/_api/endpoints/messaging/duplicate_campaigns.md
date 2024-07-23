---
nav_title: "POST: 중복 캠페인"
article_title: "POST: 중복 캠페인"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "이 문서에서는 중복 캠페인 엔드포인트에 대해 자세히 설명합니다."

---
{% api %}
# API를 통한 중복 캠페인
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/campaigns/duplicate
{% endapimethod %}

> 이 엔드포인트를 사용하여 캠페인을 복제할 수 있습니다. 이 API 엔드포인트는 [Braze 대시보드에서 캠페인을 복제하는 것][1]과 유사합니다.

{% alert important %}
API를 통한 캠페인 복제는 현재 얼리 액세스 중입니다. 얼리 액세스 참여에 관심이 있는 경우 Braze 계정 매니저에게 문의하세요.
{% endalert %}

## 필수 구성 요소

이 엔드포인트를 사용하려면 `campaigns.duplicate` 권한이 있는 API 키를 생성해야 합니다.

## 사용량 제한

이 엔드포인트는 분당 100개의 API 호출로 제한됩니다.

## 요청 본문

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) The campaign identifier,
  "name": (required, string) The name of the resulting campaign,
  "description": (optional, string) The description of the resulting campaign,
}
```

## 요청 매개변수

| 매개 변수 | 필수 | 데이터형 | 설명 |
| --------- | ---------| --------- | ----------- |
|`campaign_id`| 필수 | 문자열 | [캠페인 식별자]({{site.baseurl}}/api/identifier_types/)를 참조하십시오. |
|`name`| 필수 | 문자열 | 결과 캠페인의 이름입니다. |
|`description`| 선택 사항 | 문자열 | 결과 캠페인에 대한 설명 필드입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}


## 응답

이 엔드포인트는 `202` 상태 코드를 반환하고 캠페인 생성은 비동기적으로 발생합니다. [보안 이벤트 다운로드][2]를 사용하여 캠페인이 복제된 시기와 API 키에 대한 기록을 볼 수 있습니다.



[1]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/duplicating_segments_and_campaigns#duplicating-segments-campaigns-and-canvases
[2]: {{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/?redirected=true#security-event-download

{% endapi %}
