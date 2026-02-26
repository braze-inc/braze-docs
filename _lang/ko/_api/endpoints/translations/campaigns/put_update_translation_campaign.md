---
nav_title: "PUT: 캠페인에서 번역 업데이트"
article_title: "PUT: 캠페인에서 번역 업데이트"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "이 기사는 캠페인 엔드포인트에서 업데이트 번역에 대한 세부 정보를 설명합니다."
---

{% api %}
# 캠페인에서 번역 업데이트
{% apimethod put %}
/campaigns/translations
{% endapimethod %}

> 이 엔드포인트를 사용하여 캠페인의 여러 번역을 업데이트할 수 있습니다. 번역 기능에 대한 자세한 내용은 [메시징의 로캘을]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/) 참조하세요.

캠페인이 시작된 후 번역을 업데이트하려면 먼저 [메시지를 초안으로 저장]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/)해야 합니다.

{% alert important %}
이 엔드포인트는 현재 얼리 액세스 중입니다. Contact your Braze account manager if you're interested in participating in the early access.
{% endalert %}

## Prerequisites

이 엔드포인트를 사용하려면 `campaigns.translations.update` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## 경로 매개변수

이 엔드포인트에는 경로 매개 변수가 없습니다.

## 요청 매개변수

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | ---------| --------- | ----------- |
| `campaign_id` | Required | 문자열 | 캠페인의 ID입니다. |
| `message_variation_id` | Required | 문자열 | 메시지 변형의 ID입니다. |
| `locale_id`| Required | 문자열 | 로캘의 ID(UUID)입니다. |
| `translation_map` | 필수 | 객체 | 새 번역이 포함된 개체입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
모든 번역 ID는 GET 엔드포인트의 응답에서 찾을 수 있는 UUID(범용 고유 식별자)로 간주됩니다.
{% endalert %}

## 예시 요청

```json
{
    "campaign_id": "e24404b3-3626-4de0-bdec-06935f3aa0ab",
    "message_variation_id": "f14404b3-3626-4de0-bdec-06935f3aa0ad",
    "locale_id": "h94404b3-3626-4de0-bdec-06935f3aa0ad",
    "translation_map": {
        "id_3": "Ein Absatz ohne Formatierung"
    }
}
```

## 응답

이 엔드포인트에 대한 상태 코드 응답은 `200`, `400`, `404`, `429` 의 네 가지가 있습니다.

### 성공 응답의 예

```json
{
	"message": "success"
}
```

### 오류 응답의 예

`400` 상태 코드는 다음과 같은 응답 본문을 반환할 수 있습니다. 발생할 수 있는 오류에 대한 자세한 내용은 [문제 해결을](#troubleshooting) 참조하세요.

```json
{
	"errors": [
		{
			"message": "The provided locale code does not exist."
		}
	]
}
```

{% endapi %}
