---
nav_title: "POST: 캔버스 복제하기"
article_title: "POST: 캔버스 복제하기"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "이 문서에서는 중복 캔버스 엔드포인트에 대한 세부 정보를 설명합니다."
---

{% api %}
# API를 사용한 중복 캔버스
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/canvas/duplicate
{% endapimethod %}

> 이 엔드포인트를 사용하여 캔버스를 복제합니다. 이 API 엔드포인트는 [Braze 대시보드에서 캔버스를 복제하는 것][1]과 유사합니다.

{% alert important %}
이 엔드포인트는 현재 얼리 액세스 중입니다. Contact your Braze account manager if you're interested in participating in the early access.
{% endalert %}

## Prerequisites

이 엔드포인트를 사용하려면 `canvas.duplicate` 권한으로 API 키를 생성해야 합니다.

## 사용량 제한

이 엔드포인트는 분당 100회의 API 호출로 제한됩니다.

## 요청 본문

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) The Canvas identifier,
  "name": (required, string) The name of the resulting Canvas,
  "description": (optional, string) The description of the resulting Canvas,
  "tag_names": (optional, string) The tags of the resulting Canvas,
}
```

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | ---------| --------- | ----------- |
|`canvas_id`| 필수 | 문자열 | [캔버스 식별자](https://www.braze.com/docs/api/identifier_types/)를 참조하세요. |
|`name`| 필수 | 문자열 | 결과 캔버스의 이름입니다. |
|`description`| 선택 사항 | 문자열 | 결과 캔버스에 대한 설명 필드입니다. |
|`tag_names` | 선택 사항 | 문자열 | 결과 캔버스에 대한 태그입니다. 기존 태그여야 합니다. 요청에 새 태그를 추가하면 원래 캔버스에 있던 모든 태그를 덮어쓰게 됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 응답

이 엔드포인트는 `202` 상태 코드를 반환하며, 캔버스 생성은 비동기적으로 이루어집니다. [보안 이벤트 다운로드][2]를 사용하여 캔버스가 언제, 어떤 API 키에 의해 복제되었는지에 대한 기록을 확인할 수 있습니다.

[1]: {{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/duplicating
[2]: {{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings

{% endapi %}
